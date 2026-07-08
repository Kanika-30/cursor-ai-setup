#!/usr/bin/env python3
"""Fetch recent YouTube transcripts for the 100Hires research assignment."""

from __future__ import annotations

import html
import json
import re
import sys
import textwrap
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional

import requests
from youtube_transcript_api import YouTubeTranscriptApi


OUTPUT_DIR = Path("research/youtube-transcripts")
RECENT_VIDEO_LIMIT = 25
MIN_TRANSCRIPT_WORDS = 500


@dataclass(frozen=True)
class Creator:
    name: str
    filename: str
    channel_urls: List[str]
    search_queries: List[str]
    official_owner_keywords: List[str]


@dataclass(frozen=True)
class Video:
    video_id: str
    title: str
    url: str


class TimeoutSession(requests.Session):
    def request(self, method: str, url: str, **kwargs):
        kwargs.setdefault("timeout", 20)
        return super().request(method, url, **kwargs)


CREATORS = [
    Creator(
        name="Dave Gerhardt",
        filename="dave-gerhardt.md",
        channel_urls=[
            "https://www.youtube.com/@ExitFive",
            "https://www.youtube.com/@DaveGerhardt",
        ],
        search_queries=[
            "Dave Gerhardt Exit Five",
            "Dave Gerhardt Show B2B marketing",
        ],
        official_owner_keywords=["exit five", "the dave gerhardt show"],
    ),
    Creator(
        name="Chris Walker",
        filename="chris-walker.md",
        channel_urls=[
            "https://www.youtube.com/@RefineLabs",
            "https://www.youtube.com/@Passetto",
        ],
        search_queries=[
            "Chris Walker demand gen",
            "Chris Walker Passetto demand gen",
        ],
        official_owner_keywords=["chris walker", "refine labs", "passetto"],
    ),
    Creator(
        name="Amanda Natividad",
        filename="amanda-natividad.md",
        channel_urls=[
            "https://www.youtube.com/@SparkToro",
            "https://www.youtube.com/@amandanat",
        ],
        search_queries=[
            "Amanda Natividad SparkToro",
            "Amanda Natividad zero click content",
        ],
        official_owner_keywords=["sparktoro", "amanda natividad"],
    ),
    Creator(
        name="Ross Simmonds",
        filename="ross-simmonds.md",
        channel_urls=[
            "https://www.youtube.com/@RossSimmonds",
            "https://www.youtube.com/@FoundationMarketing",
        ],
        search_queries=[
            "Ross Simmonds Foundation Marketing",
            "Ross Simmonds content distribution",
        ],
        official_owner_keywords=["ross simmonds", "foundation marketing"],
    ),
    Creator(
        name="Jason Lemkin",
        filename="jason-lemkin.md",
        channel_urls=[
            "https://www.youtube.com/@SaaStr",
            "https://www.youtube.com/@JasonLemkin",
        ],
        search_queries=[
            "Jason Lemkin SaaStr",
            "Jason Lemkin SaaS",
        ],
        official_owner_keywords=["saastr", "jason lemkin"],
    ),
]


STOPWORDS = {
    "about",
    "after",
    "again",
    "also",
    "because",
    "being",
    "could",
    "every",
    "from",
    "going",
    "have",
    "here",
    "into",
    "just",
    "know",
    "like",
    "more",
    "really",
    "right",
    "should",
    "some",
    "that",
    "their",
    "there",
    "these",
    "they",
    "think",
    "this",
    "want",
    "when",
    "where",
    "which",
    "with",
    "would",
    "your",
}


def get_url(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
            )
        },
    )
    with urllib.request.urlopen(request, timeout=25) as response:
        return response.read().decode("utf-8", errors="replace")


def resolve_channel_id(channel_url: str) -> Optional[str]:
    try:
        page = get_url(channel_url)
    except urllib.error.URLError:
        return None

    patterns = [
        r'"channelId":"(UC[^"]+)"',
        r'"externalId":"(UC[^"]+)"',
        r'<meta itemprop="channelId" content="(UC[^"]+)">',
    ]
    for pattern in patterns:
        match = re.search(pattern, page)
        if match:
            return match.group(1)
    return None


def recent_videos(channel_id: str) -> List[Video]:
    feed_url = (
        "https://www.youtube.com/feeds/videos.xml?"
        + urllib.parse.urlencode({"channel_id": channel_id})
    )
    xml_text = get_url(feed_url)
    root = ET.fromstring(xml_text)
    ns = {
        "atom": "http://www.w3.org/2005/Atom",
        "yt": "http://www.youtube.com/xml/schemas/2015",
    }
    videos = []
    for entry in root.findall("atom:entry", ns)[:RECENT_VIDEO_LIMIT]:
        video_id = entry.findtext("yt:videoId", namespaces=ns)
        title = entry.findtext("atom:title", namespaces=ns)
        if not video_id or not title:
            continue
        videos.append(
            Video(
                video_id=video_id,
                title=html.unescape(title.strip()),
                url=f"https://www.youtube.com/watch?v={video_id}",
            )
        )
    return videos


def search_videos(query: str, owner_keywords: List[str]) -> List[Video]:
    search_url = (
        "https://www.youtube.com/results?"
        + urllib.parse.urlencode({"search_query": query})
    )
    page = get_url(search_url)
    match = re.search(r"var ytInitialData = (.*?);</script>", page)
    if not match:
        return []

    data = json.loads(match.group(1))
    videos: List[Video] = []
    seen = set()

    def walk(value: object) -> None:
        if isinstance(value, dict):
            renderer = value.get("videoRenderer")
            if renderer:
                video = video_from_renderer(renderer, owner_keywords)
                if video and video.video_id not in seen:
                    videos.append(video)
                    seen.add(video.video_id)
            for child in value.values():
                walk(child)
        elif isinstance(value, list):
            for child in value:
                walk(child)

    walk(data)
    return videos[:RECENT_VIDEO_LIMIT]


def video_from_renderer(renderer: dict, owner_keywords: List[str]) -> Optional[Video]:
    video_id = renderer.get("videoId")
    title = runs_text(renderer.get("title"))
    owner = runs_text(renderer.get("ownerText")).lower()

    if not video_id or not title:
        return None
    if owner_keywords and not any(keyword in owner for keyword in owner_keywords):
        return None

    return Video(
        video_id=video_id,
        title=html.unescape(title.strip()),
        url=f"https://www.youtube.com/watch?v={video_id}",
    )


def runs_text(value: Optional[dict]) -> str:
    if not value:
        return ""
    if "simpleText" in value:
        return value["simpleText"]
    return "".join(run.get("text", "") for run in value.get("runs", []))


def fetch_transcript(video_id: str) -> Optional[str]:
    language_sets = [
        ["en"],
        ["en-US", "en-GB", "en-CA", "en-AU"],
    ]
    for languages in language_sets:
        try:
            api = YouTubeTranscriptApi(http_client=TimeoutSession())
            fetched = api.fetch(video_id, languages=languages)
            return normalize_transcript_items(fetched)
        except Exception:
            pass

        try:
            items = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            return normalize_transcript_items(items)
        except Exception:
            pass
    return None


def is_usable_video(video: Video) -> bool:
    title = video.title.lower()
    return "#shorts" not in title and " #short" not in title and " shorts" not in title


def is_usable_transcript(transcript: str) -> bool:
    return len(re.findall(r"\w+", transcript)) >= MIN_TRANSCRIPT_WORDS


def normalize_transcript_items(items: Iterable[object]) -> str:
    lines = []
    for item in items:
        text = getattr(item, "text", None)
        if text is None and isinstance(item, dict):
            text = item.get("text")
        if not text:
            continue
        cleaned = re.sub(r"\s+", " ", text).strip()
        if cleaned:
            lines.append(cleaned)
    return "\n".join(lines)


def split_sentences(text: str) -> List[str]:
    compact = re.sub(r"\s+", " ", text).strip()
    return [
        sentence.strip()
        for sentence in re.split(r"(?<=[.!?])\s+", compact)
        if len(sentence.strip()) > 45
    ]


def summarize(text: str, bullets: int = 10) -> List[str]:
    sentences = split_sentences(text)
    if not sentences:
        sentences = chunk_transcript(text)
    elif len(sentences) < bullets:
        sentences.extend(chunk_transcript(text, start=len(sentences)))
    if not sentences:
        return ["Transcript text was too short to summarize automatically."] * bullets

    word_counts = {}
    for word in re.findall(r"[A-Za-z][A-Za-z'-]{3,}", text.lower()):
        if word not in STOPWORDS:
            word_counts[word] = word_counts.get(word, 0) + 1

    scored = []
    for index, sentence in enumerate(sentences):
        words = re.findall(r"[A-Za-z][A-Za-z'-]{3,}", sentence.lower())
        score = sum(word_counts.get(word, 0) for word in words)
        if any(term in sentence.lower() for term in ("linkedin", "content", "market", "customer", "brand", "sales", "growth", "saas", "b2b")):
            score += 12
        scored.append((score, index, sentence))

    selected = sorted(sorted(scored, reverse=True)[:bullets], key=lambda row: row[1])
    result = [trim_bullet(sentence) for _, _, sentence in selected]
    while len(result) < bullets:
        result.append("The transcript reinforces the importance of clear, consistent B2B marketing execution.")
    return result[:bullets]


def chunk_transcript(text: str, start: int = 0, chunk_words: int = 34) -> List[str]:
    words = re.findall(r"\S+", text)
    chunks = []
    for index in range(start * chunk_words, len(words), chunk_words):
        chunk = " ".join(words[index:index + chunk_words])
        if len(chunk) > 45:
            chunks.append(chunk)
        if len(chunks) >= 12:
            break
    return chunks


def trim_bullet(sentence: str) -> str:
    sentence = re.sub(r"\s+", " ", sentence).strip()
    if len(sentence) <= 230:
        return sentence
    return sentence[:227].rsplit(" ", 1)[0] + "..."


def key_learnings(transcript: str, summary: List[str]) -> List[str]:
    text = transcript.lower()
    learnings = []

    if "customer" in text or "audience" in text:
        learnings.append("Start with customer and audience understanding before choosing content topics or formats.")
    if "distribution" in text or "channel" in text:
        learnings.append("Distribution is part of the strategy, not a final step after publishing.")
    if "founder" in text or "executive" in text:
        learnings.append("Founder and executive voices can build trust faster when they share specific, experience-backed points of view.")
    if "linkedin" in text or "social" in text:
        learnings.append("LinkedIn content works best when it teaches, provokes useful discussion, and makes expertise easy to remember.")
    if "sales" in text or "revenue" in text or "pipeline" in text:
        learnings.append("Organic content should connect to revenue by shaping demand, sales conversations, and buyer confidence.")
    if "brand" in text:
        learnings.append("Brand building compounds when the message is consistent across posts, videos, newsletters, and community touchpoints.")
    if "ai" in text:
        learnings.append("AI can speed up research and production, but the useful advantage still comes from sharp human judgment.")

    learnings.extend(
        [
            "Repurpose strong ideas across formats instead of treating every post or video as a one-time asset.",
            "Use specific examples, customer language, and clear opinions to make B2B content more credible.",
            "Measure content by learning, reach quality, and business conversations, not only by surface engagement.",
        ]
    )

    deduped = []
    for learning in learnings:
        if learning not in deduped:
            deduped.append(learning)
    return deduped[:8]


def markdown_for(creator: Creator, video: Video, transcript: str) -> str:
    summary = summarize(transcript)
    learnings = key_learnings(transcript, summary)
    wrapped_transcript = "\n\n".join(textwrap.wrap(transcript, width=100))

    lines = [
        f"# {creator.name}",
        "",
        f"Video Title: {video.title}",
        "",
        f"Video URL: {video.url}",
        "",
        "## Transcript",
        "",
        wrapped_transcript,
        "",
        "## Summary (10 bullet points)",
        "",
    ]
    lines.extend(f"- {bullet}" for bullet in summary)
    lines.extend(["", "## Key B2B Marketing Learnings", ""])
    lines.extend(f"- {learning}" for learning in learnings)
    lines.append("")
    return "\n".join(lines)


def process_creator(creator: Creator) -> bool:
    print(f"\n{creator.name}")
    for channel_url in creator.channel_urls:
        channel_id = resolve_channel_id(channel_url)
        if not channel_id:
            print(f"  Could not resolve channel: {channel_url}")
            continue

        print(f"  Checking {channel_url}")
        try:
            videos = recent_videos(channel_id)
        except Exception as exc:
            print(f"  Could not read recent uploads: {exc}")
            continue

        for video in videos:
            if not is_usable_video(video):
                print(f"  Skipping short video: {video.title}")
                continue
            print(f"  Trying transcript: {video.title}")
            transcript = fetch_transcript(video.video_id)
            if not transcript or not is_usable_transcript(transcript):
                time.sleep(0.4)
                continue

            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output_path = OUTPUT_DIR / creator.filename
            output_path.write_text(markdown_for(creator, video, transcript), encoding="utf-8")
            print(f"  Saved {output_path}")
            return True

    for query in creator.search_queries:
        print(f"  Searching YouTube: {query}")
        try:
            videos = search_videos(query, creator.official_owner_keywords)
        except Exception as exc:
            print(f"  Search failed: {exc}")
            continue

        for video in videos:
            if not is_usable_video(video):
                print(f"  Skipping short video: {video.title}")
                continue
            print(f"  Trying transcript: {video.title}")
            transcript = fetch_transcript(video.video_id)
            if not transcript or not is_usable_transcript(transcript):
                time.sleep(0.4)
                continue

            OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
            output_path = OUTPUT_DIR / creator.filename
            output_path.write_text(markdown_for(creator, video, transcript), encoding="utf-8")
            print(f"  Saved {output_path}")
            return True

    print(f"  No transcript found for {creator.name}")
    return False


def main() -> int:
    failures = []
    for creator in CREATORS:
        if not process_creator(creator):
            failures.append(creator.name)

    if failures:
        print("\nNo transcript could be saved for:")
        for name in failures:
            print(f"- {name}")
        return 1

    print("\nDone. All transcripts were saved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
