# Jason Lemkin

Video Title: The Agents #008: Agents Are Merging, Not Multiplying. Plus, Sam Blond on Why Outbound Isn't Dead.

Video URL: https://www.youtube.com/watch?v=dF_RcN4BkQU

## Transcript

We were talking about it earlier and I talked about on the la on the last show and a lot of people

in the industry kind of got let up, right? It was really good for build.com, but this guy that

builds an AB AI VP of finance wrote this LinkedIn post today. It's like Jason Lin and Amelia rolled

out this VP of finance. It seems really great, but here are the limitations. Some of it was right,

some of it was wrong, right? But it was a good analysis. We have budget. A budget to we're we're two

weeks into our VPF. We don't want to be running this agent. Okay. At the very end, he says, "Jason,

when you're ready, hit me up." >> I mean, it's it's an F, isn't it? From a sales perspective. >> Uh,

the way that we describe Monaco I is that this gives you um whether you're a founder, whether you're

a salesperson, just an employee at a company, it gives you leverage to spend time on what we would

describe as higher ROI activities, but really the activities that that agents actually can't do.

Agents are not hosting the agents podcast right now. like like the two of you are spending your time

doing this. That's certainly how like we describe the leverage that Monaco provides to customers.

It's not that like we're a silver bullet for go to market. It's that you can spend more of your time

customerf facing. You can spend more of your time doing the like creative campaigns that an agent

isn't going to do for you. Welcome everybody. We are back with the agents and the latest um an

exciting show we have and um our first with a very special guest. Our AI VP of finance went live

this week. Its first iteration and the part that surprised even us is where it lives. It didn't get

its own app but actually lives inside 10K our AI VP of marketing. You're going to hear more about

that. It's less a VP today. Don't get triggered folks. It's more like a scrappy director of

financing. It's learning but it's already running real finance work in production. And that's the

theme of today's show. Everyone keeps telling you the future's 100 specialized agents. Maybe so, but

what's happening in our stack is the opposite. The agents are collapsing into each other. We may

well have fewer agents doing more, going deeper, in essence, monor repos, all sharing a body of

knowledge. Uh, we'll see. So, I'm Jason. I'm here with Amelia. We're three humans, more than 20 AI

agents in production at Saster AI. And halfway through today, we're bringing in Sam Blonde, founder

and CEO of Monaco, which happens to be one of the agents we run. So, we'll get to grill the guy

whose product is on her own team. Uh, and with that, um, I want to tee it up uh, about our AI VP of

finance. I want Amelia to to to to do a deep dive, show us what we can. Um, but before we get there,

because a lot of folks will will be wondering what it is before we even describe what the VP of

finance is, or maybe you should talk about what we integrated to get there, so we'll understand how

it works. Like it is not just an application. It's not just an agent, right? It is. It leverages all

the APIs of all of our staff, doesn't it? >> It does. So, there's a few core components that and

I'll I'll talk through the feasibility and ease of use of integrating each of these tools into our

AIVP of finance. Things that 10K, traditionally, our AIVP of marketing, did not have previously when

it came to adding the finance component. So, the first one was build.com. Um, super easy, took less

than 10 minutes. I will say it's interesting because bill.com which many of you probably use well

you know for accounts receivables accounts payables um has a lot of we've been using it for many

years now so it has a bunch of historic data in it and the agent actually thought you still had to

ask support to get an API key so it's like hey maybe do bill.com first out of your whole finance

stack because you're going to have to reach out to support to get an API key and get access and that

could take a couple days so it said hey do this one first, not because it was going to be the

easiest, but because it thought it was going to take a couple days for us to get access. Lo and

behold, I go into bill.com. You could just make an API key yourself if you're an admin, which I was.

So, it actually took less time than the replet agent thought it was going to take to integrate with

bill.com. Now, it is read only, so you know, do with that knowledge what you will. It's not change.

It can change things in bill.com if you explicitly ask it to, but not everything. Like, um, for

instance, I was paying a bill this morning. I needed to change the category of like which account on

the ledger it should go to. >> Yep. >> Very deep in finance. Um, and it said it couldn't quite

change that. And it also didn't suggest that it should change that. It said, "Amelia, you should do

that yourself. Just log into bill.com and change it." And so, I did that myself. Now, what it can do

in bill.com, and this is the cool part, and I'll explain the rest of the stack there, but I'll I'll

walk you guys through a flow now that the finance component of 10K can do. So, now when we close a

deal, um 10K is hooked up to a number of things that we'll we'll explain next. But in Bill.com

specifically, it can now create the invoices automatically. So, it will read through the whole

contract. We'll talk about why it was a little bit lazy on reading the whole contract to find like

the payment terms, but it will read the contract. Um, it will attach it to Salesforce. It will mark

it as a close one with our Salesforce integration that was already there. But inbell.com

specifically now it will create the invoices based on what the actual close one contract is. And it

will do it in less than 30 seconds from a contract and a deal being closed. You're listening to the

official SAS AI podcast brought to you by Hey everyone. If you're using AI in your go to market or

you want to get going, then you need to try Monaco. We're on it. Zaster's on it. We love it. We use

it for outbound, but you can use it for everything actually. It's everything you need all in one

place. At Monaco, it's the all-in-one revenue platform and your system of record. It builds your

TAM, runs outbound, captures every interaction, and manages pipeline in one place. Allin-one great

unified platform. Go to monaco.com to learn more. Tell them to ask you. >> Okay. So, so we we're

using a lot. It sounds like Bill has become the hub of our of of our finance featur. Yeah. >> Okay.

And so before we get there, just walk us through just our general business process. Some folks are

often critical that disaster is different. It's not like everybody else. Um right now the main thing

we're doing it is for sponsorships, right? Correct. Um, and these sponsorships are going to range

from 45K at the low end for like a media sponsorship up to maybe 400K for a big sponsorship of our

events, media newsletters, stuff like that, right? So, it's a pretty wide birth. 35K to 40K.

Nothing's self-s served today at the moment, right? Um, it all goes through um some sort of sales

process. Sometimes a lot of it's an agentic process, but there's always a human today involved in

the closed, right? Yeah. >> Um, so just walk us through the flow and then and then and then when a

deal comes in, it's handed off to the agent. What what's the flow here? >> Yeah. So I'll I'll walk

you through before and after, right? So whatever a deal closed before 10k finance um we would send

one of the humans whoever closed the deal me David our prior sales rep would send it to finance and

then the humans on our finance side who are part-time humans at Saster would you know whenever they

log on they would look at the contract they wouldn't do anything in Salesforce because finance

doesn't have a login to Salesforce they would create the invoices in bill.com and again you have to

think of the average time of them doing that as a parttime time resource is probably the same day

but sometimes next day if it's >> it could be days to lag. >> It could be a day lag. Yeah. So

contract close to invoice creation was not 30 seconds like it is now. It was up to a day let's say.

>> Yep. >> So then finance would create the invoices. Our bill.com syncs to QuickBooks for all the

financers out there. So that's you know that syncs our books and our backend and our receivables and

all that. So that's basically what they're doing to track, you know, a sale has been made. Um, and

that money is coming in whenever money is coming in. So, you know, standard is net 30. Sometimes we

have split payments because, again, to Jason's point, they're like bigger invoices or they're year-

round stuff or sometimes we do want to collect the media um differently from the SAS annual for our

finances. A little quirky, but sometimes we we break up invoices, right? That's not uncommon these

days to break up some some invoices and payment terms. And then finance would then whenever they do

it send that to whoever was on the contract as being the finance PC, right? And that was that was

previously also why we started this exercise was because we had no automatic collections process

before this. And one of the first things that the replet agent flagged to me when I hooked up

bill.com it said hey you don't have automatic invoice from lenders on. And I said, "What do you

mean?" He said, "Well, Bill.com has these really nice automatic invoice reminders that you could

say, hey, this is this, you know, customer of yours just closed. You can turn on automatic reminders

so that Bill.com will remind them, you know, 5 days before it's due, one day past due and like 10

days past due." I was like, "What do you mean?" Like, our our our humans don't do that now. And

they're in bill.com. They've never bothered to turn this on to help us do collections this entire

time. >> It is interesting. I I don't want to interrupt it, but it is as we've hooked whether it's

Replet or Claude or Lovable up to APIs, right? Which is where you should start, right? They have

guard rails. They they are systems of record. They work, right? >> They're almost always finding >>

use cases that we did not know existed as humans. We just didn't know you could do that with that

piece of software, right? We did. We didn't know. We didn't know you automate invoicing and

reminders in bill.com. A new a new a new user might, right? But we've never even we didn't even you

and I didn't even set it up. We had no idea. >> But the agent instantly knows better ways to use a

product, right? >> Instantly, you know, instantly. I mean, it's funny. He got >> an upgrade. It's

people got the need to ask >> for support a little bit out like that was just outdated docs that he

found. It was just, you know, I was like, "Send me the link to that." And it was like an outdated

doc on bill and you know maybe Bill.com just quietly lets you do this now without asking support. >>

Well, outdated docs are an issue too with agents but keep going. >> That's the thing. Yeah. He he

sent me the bill.com support article which did say you have to ask for one but then I just turn it

off after it's after I flagged that I just you know turn it on. He was like okay I can see you know

it percolated. It can see everything. You can see the okay starting to populate our our a new

finance dashboard in 10k with receivables and payables and overdue. It was like, first, look at

these overdue invoices. Um, second, hey, you should probably turn on this automatic email reminders

cuz they're not on yet. So, you know, previously I had only gone into bill.com and hit approve or

approve and pay. I didn't really play around with it. I guess I should have because the agent

instantly, right, just knew everything about Bill.com and said, "Turn on these automatic invoice

reminders." >> I don't I don't mean to keep jumping around, but why did we do this and why did we

start here? You made the point that I think super interesting and important. There's so much stuff

with AI and agents you could automate today, right? There's so there's too much like it's an

overwhelming amount of things you could throw agents at today, but if it ain't broke, why fix it,

right? That there it's actually an interesting theme. So, you know, it goes back to the it's going

to become a meme. Why would you vibe code your own Salesforce? Well, you shouldn't. You know, we

we'll talk about this till the end of the show. You shouldn't. It's too complicated. It's too rich.

It's too collaborative. It you could, but why would you, right? Why we built our a VP of finance in

a small team, right? in a small organization is collection. Anyone that's run a startup will know

this. The most important part of a startup is collections. Now, when you get really big and you're a

public company and you're and you're generating massive cash flow, collections become second like

it's got to get done. But like if you're Adobe and you have 40% um operating margins, you don't

care. But for us, the money matters, right? We got to pay your commission, your bonuses. Um and and

and the humans, just as humans do, degraded. Our human team got worse at they stopped doing it. They

went on a vacation but never caught up. We got six figures behind on collections and it creates a

lot of stress because it's sometimes you have to write off collections if people don't get it. We

had that issue and sometimes it's just super awkward because organizations think they they want to

pay, right? Like like for an event it's just awkward to ask someone to pay for a booth 60 days

later. >> It's awkward. It's awkward. So we didn't build this because we wanted to make Stripe work

better or bill or even books, right? We did it to solve a large problem that humans in our org were

not had degraded. We're not getting done great. Collections that was worth your time. >> All this

other stuff might not have been worth your time. But the other stuff that the other benefits we're

getting from our a AI VP of finance work, it might not have been worth it if we didn't have a a high

pain point which was making collections better. >> Right. >> Correct. Um, so, so that was a big

piece of it. I was literally just explaining to the h the two Cubans who work part time in our

finance team. They were so confused about what this AIVB of finance does. They're like, "So, do we

just stop working?" I was like, "No, this this has been up for, first of all, this finance one has

been up for 30 days." And I was like, "And has anything changed majorly in your process?" They're

like, "Well, we still have to like, you know, double check things. we don't have to send invoices

anymore. I was like, "Yeah, because you were too slow to do." Yeah. But they like thought of it as

like a I literally said, "It's not a terminator. It's not going to come find Sarah Connor." Like,

it's literally a dashboard. It's hooked into bill.com. It will ask me before it ever does anything

in bill.com if it can do it. Sometimes it can't do it. And it is an agent for me to talk to about

finances in a way that has the whole picture that no two humans on planet Earth, even if they're

greatest finance people who are part-time, would have that kind of insight because we built him into

10K. He knows all the open deals. He knows all the history of Close One sponsors. He pu he's pushing

the contracts now directly into Salesforce, flipping them to close one, creating the invoices,

sending it to the customer within a minute of a deal being closed. Like that is just a level of

automation you can't get with any human being on planet Earth. Like that's just too quick for any

human, even if they're the greatest finance person on the planet to do and and to do all those

steps, right? Like to my point earlier, finance doesn't have access to Salesforce normally in any

org. like they're not going to upload that contract to close one and then send it to the customer

and say hey thanks for you know becoming a customer blah blah whatever you know the automated email

list and here's your invoices like they're just not going to do that >> yeah it is interesting you

made a good point by running first we started running Salesforce headless and it meant I could

access Salesforce and get access to our data understand how our customers and sponsors work which I

never could get for 10 years right I never even logged in when you have a finance agent whether it's

a VP of finance or whatever you want to call it >> you can query your financial and customer data

and get answers to questions that we just could never get answers to before with two part-time

contractors or a lot of startups use outsourced finance, right? And you just they'll never even if

they're good, they'll never know that much. Like the the person that does your books won't really

understand how cash flow works in the company or they might not or and the person um and the person

that that closes your books may not understand who your customers are or why they're in certain

categories or they or almost nobody can freaking build a model. What's our revenue going to look

like in 12 months? What's our cash burn? Like that that there are there's a subset of finance people

that can do that. And even the ones that can do it, they need enough familiarity with your business

cadence and workflow to build it. An agent doesn't. It can see all of this. And so it's just, you

know, it can supplement a larger team. Start with a problem, which is what we did. The problem was

collections quality had degraded. If you have a if you're if you're not even don't have a full-time

finance team, it's magical. >> Yeah. Because for 10 years I wasn't able to get basic questions

answered >> like what what's our sponsor renewal rate for the last four years where can we predict

revenue going forward are we ahead or behind right what will cash look like at the end of the year

can we take distributions can we take bonuses like I would have to wing this stuff >> now I could

ask the agent it wouldn't wait in 10 years right so this is you >> we we keep going but but we've

made this headless and now you can talk to your data in a way that you often can't with with

contractors consultants and agencies, you just can't talk to your data. >> Yeah. So speed was one

reason, right, of like this this process has worked a lot that speed across the board, right? I

don't have to flip a deal. David doesn't have to flip a deal in Salesforce when the contract is

signed. It just does it automatically. It uploads it. No mus, no fuss. It's there. Sends the invoice

within a minute. You're done. Like it'll automatically follow up with them before their build

becomes due for collections. Like it is collections and contracts on autopilot is the best thing.

Um, granted, again, it needed some tweaking. Like, it's been, you know, a couple weeks now. In the

first couple deals, it didn't want to read the whole contract. And I said, "You need to read the

whole contract, even if it's 20 pages because of all the terms. You got to read the whole thing to

make sure, you know, you're sending it to the right person. The payment terms are right. If there's

anything like out of our standard terms, we should put that in Salesforce so we have a record of

it." It improved upon itself. But, but back to your original question. So, bill.com was the first

thing we hooked up. The second thing we hooked up, which it's unclear if we actually needed to, but

for for projections and stuff, you need to, but if you're just doing like your AP and AR, you could

probably just hook up bill.com, your Asian, and be done. But we also hooked up QuickBooks, which is

synced to bill.com, but is handy to have for like super deep dive stuff. So, like I asked it some

test questions because some of our tax um payments were due and 10K was expert on like too good.

like he answered all these questions that our our separate tax team had. I I gave them to Ten and I

said, "Hey, I don't I don't I don't know the answers." Like I'm not going to wing it. It's

financials, right? I don't want to wing this, but you you now have bill.com and you have QuickBooks.

Can you understand these questions and tell me one what they're asking me in plain English so I

understand it. Two, what is the actual answer to their questions because I don't understand it. And

so it did both. it like very very nicely explained to me in and in ways I could understand what our

tax team was asking for, what they were looking for, something we had to do with Sask. So I had to

give the agent, you know, some inputs and able to answer their questions and then it was able to

write me what to write back to the tax team to answer their questions for taxes. So it was worth,

you know, I would say QuickBooks was the hardest one to hook up. You have to make an in it developer

account, which I didn't have. None of us had here. It was a pain in the butt. wasn't just like

bill.com where you could get, you know, your API key in two seconds. This was a developer account,

which to make a developer account, you have to go through like the security questionnaire, which you

should, right? Maybe it's better. It has this guardrail that it took me like an hour to do it. So,

you have to be really motivated to want to do it, but I did it. So, we got QuickBooks hooked up and

it was worth it because then it could answer all my questions kind of right away for like deep dive

tax questions. Now, if you don't if you don't need it for that or if you don't need it for like deep

projections, then you may not need it. You you could probably just get away with bill.com. But then

the last two things I hooked up were so those were two out of four. The last two things I hooked up

was Bracks because we use B right now for you know credit card payment. I was like just, you know,

if you're going to be our VP of finance agent, you got to know what credit card bills are coming up.

And um our Brex account also has receivables. Like we have an account there that receives payments,

so you kind of need that. And also because our deposits from Stripe go into B, I was like, you also

need B because then you can monitor all the Stripe deposits that we get for the tickets because

they're self-s served. Um, so I hooked up B again much like bill.com. Probably took 60 seconds.

Super easy. Then I had everything from Brex. And then the last thing I hooked up was Panda because

we currently use Panda for contracts. And so I was like, how do I get you the contract? And it said,

well, what are you using? I said, Panda do he said, give me the API. Now, this one I did have to ask

support to turn on the API access. So, that was a little bit of annoying, but they did do it same

day, so that was good. At first, it said ask your like sales rep. I was like, I don't have one. And

then I actually looked at our account to be like, who is our rep? And it, you know, back in the day,

you used to be able to log in and be like, David, it's your rep. It's faster. Um, I think people

have gone away from that because it didn't say that anywhere. I couldn't find a human that I had

actually known at the Anod do. >> Yeah. >> And so I just emailed support and they again they turned

it on same day and then it was super easy. So now that's how it's doing all the contracted

automation is it's got Panda do. So the second a deal is signed. It's actually funny/interesting.

10K will send us an automatic email that the deal will close and it will beat the Panda Do email.

like the last like 10 out of 10 times Tank is actually faster at alerting me than that a deal has

closed than Panda has even though it's Panda's API. Oh, let's go through a couple more things and

move on to the next point. But um at first I was thinking because it's interesting do sometimes

running an agent on top of these APIs and products makes them more valuable, right? Um Bill's more

valuable to us now, right? Much more valuable. Um, QuickBooks is terrible, but we'll probably stick

with it longer because we can access it, right? It's definitely made Salesforce more valuable. We've

talked about it. And then I was thinking Panda Do, you know, >> um, >> Panda Do is worth it for us,

but it's barely worth it. It's like a CPQ system, but when we had a larger sales team that was

constantly breaking rules and contracting, editing contracts without telling us, changing terms

without consent, breaking rules, it was like the best piece of software that that I said we should

use. Now with a very small team, not only do we have less needs, but could you vibe it away? Could

10K just build a contract in an invoice on its own? Do we even need Panda do at all? >> I mean, he

could. >> Yeah. And it's not cheap cheap Panda. It's not cheap cheap. They keep they raised the

price over the years even though we only need two seats. Yeah, >> part of that is in this exercise

it's you have to be on a certain plan to have API access, which surprisingly we're on for two. I was

surprised we were on it for two seats. I was like, I assume we're going to have to pay some sort of

upgrade. We were already on this crazy plan for two or three seats. It's interesting because for all

of these all of the things are 10K and just some of the times it's like, well, do you want me to

just do that for you? >> Yeah. And so it already kind of suggested it could just do a contract. And

I'll tell you why too. It didn't realize it could just do it for us until this week. Because this

week I added to our VP of finance commissions. And so I said, "Hey, you already have, you know, it's

been three weeks running where you get a contract. You again, this is pretty magical, guys. I I

don't want to understate like it sounds simple but this is such a gift especially if you're a

smaller company is that this automation thing whatever you call it agent automation whatever it is

takes a contract when the deal is closed flips the stage in Salesforce I mean my god thank you flips

the spill in Salesforce puts the contract in there updates the contacts in Salesforce sends the

invoice automates colle this is magical that it does this now but Now, also I added this week. I was

like, "Hey, now that you do steps one through four, why don't you do step five cuz it's almost the

end of the month, and I don't want to do step five manually, which I normally do, which is calculate

commissions." I was like, "You have the contract. Here are our commission rules. You can already see

in Salesforce who closed the deal. You've already made the invoices in bill.com, so you know the

payment terms. You know exactly if it's media or if it's for SAS or annual." I was like, "You have

basically all the components to calculate commissions." So, I just gave him our commissions policy

and then he took probably 30 minutes to add in this feature, but now he will calculate commissions

as like his fifth step. >> Would it have even occurred to you to buy a third party sales commission

software or uh would it even be worth it if there was a better product? Well, it wouldn't be worth

it. But in that process of it doing commissions, the agent was kind of hinting that it could serve

to do contracts. >> Well, that that goes back to the initial point we talked about how when you hook

up APIs, the agent will come up with use cases for the the API you didn't even know existed. Right.

Right. >> Um now it's sort of stinging why why are you using Panda do? >> We would have to maintain

it. We would have to make sure it works. But uh certainly agent can generate a contract, a PDF.

Yeah, certainly it can generate a PDF. Certainly it can send it already sends emails for marketing.

Certainly it can send to the customer. >> Yeah. >> The contract to sign like >> Yeah, >> it probably

needs some sort of Now the only thing I don't know on that piece. >> You're right. We're not going

to build our own e signature. >> Well, that's the thing, right? I was like the only missing

component would be the e signature part of like, you know, it being certified eastern. It's just

there's we could build our own or we could even integrate a cheaper API or something. this that

that's going to cross a level of complex there there's certain there's certain steps that we would

not build but everything else we could do we could we you know we could generate we could route it

we could lock it we could do the the CPQ part which is lock it down right we didn't buy Panda do for

an e signature instead of Adobe site we bought it to lock down rogue sales reps right the e

signature was just a bonus right >> now we still need that part but we may not need the rest >> we

could revisit this on our next episode I'll ask it now that it has this commissions piece. I'll ask

it what it thinks we should integrate just for the e e signature, right? Like if he already wants to

start making the contract, I wonder what he will say he wants to use. >> Okay, next point I wanted

to move on. Um there's more I want to talk about that we'll talk about in the next episode. So I

want to be a little critical um because the meta point is more interesting. So, one of the agents

we've used since almost since the beginning of our journey, probably our second or third is one

called Qualified, which Salesforce bought for a lot of money. >> Uh, Qualified does a lot of things.

It's doing more and more. It is, I think it's almost been rebranded as Salesforce >> Qualified from

Salesforce. >> Qualified from Salesforce. It's like agent force light. It's a good great product.

It's done a lot for us. If you go on to basically what it does for us and Amelia will dig in more is

qualify inbound leads which is very valuable instead of waiting weeks to see if a human decides it's

worth their time to reach out back to a human qualified answers all their questions gives them a

prospectus tells them about the sponsorship gives them group discounts for coming to our events

whatever they need it does it's magical right it's just great it's trained on our docs and it has a

video version of Amelia if you want to talk to a video version it's got a lot of cool stuff on it so

it's just support on steroids that qualifies prospects without them feeling like they're being

qualified. Right? It's not the only product that does this. There's plenty. We're not saying it's

the only one, but they reached out to us in the early days and got us going, which we're grateful

for, and it's it's worked great. It doesn't do everything until until actually this morning I went

to test it for for a Saster Post and I talked to Digital Amelia and she wanted to know what discount

I wanted to go to Saster AI annual, which was one month ago. Now, maybe it's our fault, maybe it's

qualified's fault, maybe it's in the middle. I don't want to over talk, but th there there is it's a

reminder. This this stuff is not set and forget. >> And I'll tell you why it happened, right? >> Why

doesn't it just isn't there just a body of knowledge or training on the back end that it should just

automatically update everything in 60 seconds. >> So, it's because it has so many articles and so it

has too much in it that says SAS annual 2026 May. That is a recurring problem we've had. Too much

data breaks guardrails break systems. Right. >> I want to keep going. I don't mean interrupt, but we

talked we might have talked about this on the last show. We built this VC pitch deck creator that's

done 5,000 VC pitch decks. And when we were away too, it broke. It started giving everyone an F. >>

Yeah. >> And I was so pissed, right? Why? Why? Like you did 4,000 decks. They seem to work pretty

good. Why are you giving everybody an F? And it's because I'd inadvertently added a 15th guardrail

to the system and it couldn't process all the guardrails. It was too many. >> Yeah. Yeah. And and

maybe if you told me I forgot, well then I guess it's our fault, but you're not telling me that we

forgot for the last six weeks to update this thing. >> I thought that was part of it. I thought I

was like, okay. Part of it might be because I haven't gone in to say, hey, override your knowledge

or whatever and say that annual is now 2027. So I did that in the last week. However, it does rec

crawl the website automatically every day. And we've obviously posted that the next disaster is in

2027. So, >> okay, but hold on. Let's be fair. Um, you told qualified to flip everything to sell

2027 or you just assumed it would do it reading documents on the internet. >> I No, no, no. I didn't

assume it would do it. I hoped it would. So then I told it this week I said, "Hey, flip to say

everything is 2020." >> You waited almost five weeks to fix the issue. Right. So I shouldn't give

Qualified an F. I should give them a C+ or B minus here. Right. If it is rec crawling our website

automatically every day, it should have seen that we did post these things about 2027. My other

thing I realized actually and me doing this exercise was it doesn't have an agent. >> There's no

built-in agent in qualified >> to talk to. >> It is there's no agent to talk to. >> It's just it's

just it's just classic rules and and uh >> and like there's a whole backend studio workflow. And I

was like, you know what? If this had been like 10K or replet, I could just hold it before SAS. Hey,

when the event's over, flip everything to 2027. There's no built-in agent. >> You remember when

Andrew Bucky from Claio came, public public uh e-commerce marketing company said that was their job

number one was their internal agent for every customer so that everyone is an expert on Claio. >>

Yeah. Like just launched 2.0. Their 2.0 has an agent because their 1.0 didn't. And I was like, this

is exactly what you needed to spend the team's time on because >> otherwise you can't have self-s

serve if you don't have the agent. Otherwise, you can't have self-s serve. Yeah, I started talking

to the new artisan agent cuz like I was, you know, used to 1.0, not 2.0. And so, it's handy to have

an agent in the app to talk to right away. So, I don't have to go ask an FTE for help or the team

for help there. >> There's a series of issues here. The first, which is interesting, which I give us

a bad grade on, but it's a learning, right? I give you a bad grade on even though generally I give

you an A+ but it's this is an issue across industry sometimes our many times maybe even most times

>> our intuitive expectations of what an AI agent or AI platform does is not what they actually do.

But you made the air quotes mistake of just assuming an agentic product will know to update itself

that it got out of date. Maybe not in an maybe not in real time, but you just assumed within fairly

quickly you would update anything that is out of date when new docs flowed into the system. Exactly.

>> You assumed when a new document was ingested that said Saster annual AI annual is May 11th

through 127 that would up that that would permeate the agent. And I actually think >> you are 95%

right to expect that. So you were right to assume that. I think at a software level I would just

assume you would get it wrong. I would just assume just like you got it. You you didn't approach it

as a software builder and the next time you'll get this right. >> Yeah. >> Okay. I want to keep

going. The next time actually we're gonna talk we might talk about one more fail and then we'll get

back into positivity mode. So one one other one other headache our endless journey of our worst most

expensive application Marquetto. Marquetto is not only our worst application but actually it's our

most expensive. So we've been on a journey to move off of uh Marquetto where sadly I was one of the

first 10 customers ever. The founder sold me personally. I used been a case study in the website in

the early days and now we sort of get attacked by the internal team and made uncomfortable. So it's

easy to say vibe code your own. It's much harder when you got to leave an existing platform with a

decade of data. All the kids on X saying I vioded my own CRM. Did how did you lift how did you lift

your data from your old system of record to your new one? We even talked about it with the data

bricks co-founder Saster. The lift is a big deal. The lift is a big deal. two interesting things

happened. So I you know we were away for a little bit post post annual because I need a break. So

nothing happened those days except I we you already built into 10K this newsletter builder that

we've shown folks and I built in an automation. Now it wasn't great but it did work while I was

gone. >> Oh yeah. We we we used AI to completely automate our it's through the content that we've

written but it completely automated our emails. Right. >> Yeah. Which was great. Um, a couple

things, you know, the memory got a little stale sometimes and so I had to push. It wasn't perfect,

but it did work. Like the news the newsletters went out um exactly on time. Every every day it

should have. So So there was >> worse than you did as a human just as an aside. Uh but but they did

work, right? So >> yeah, the quality went down a bit because it just picked the most recent. So, it

wasn't as good because I usually go in and I pick the ones I know people are either reading using

Google Analytics as like the top um or that I think are going to be, you know, good subject lines.

Yeah. Taste. Yeah. >> I think this is a trit term on Twitter. The agent when the agent took over our

newsletters while we were traveling um that was very helpful, but taste is I think is is a is an

excuse for thinking that you can't be replaced with an agent. But here it was impacted. The quality

was maybe 80% as good as when you did it. We didn't get like rant complaints because the content the

the content itself we wrote it's human created right. Yeah. >> But now we want to lift off of our

worst piece of software. >> So for many reasons we got to get off this thing. So where we're at

today is and to to your point of what Mark was talking about of you know he wants on Salesforce he

wants to get folks kind of deployed before they sign things. So I did sign upgrade if you will our

current Salesforce instance to include marketing cloud. nominally it was not it's not anywhere near

the price Marquetto charges us it's not even a third of the price so thankfully I was like you know

even if I don't stay on it it's a low risk right one it's a low risk in terms of just pure cost two

they couldn't quite get us deployed before we signed but they did start the implementation before I

signed and then when I signed I gave them the login to our marquetto they already they provisioned

Salesforce just provisioned you know marketing cloud out instantly that day and my FD Lindsay gave

them the login to marketing cloud for the the like let's say new FDE who's helping me on marketing

cloud so instantly they started taking an action we're not fully on it yet uh but I will say the day

that this happened which was right after SAS annual I asked 10K hey marketing cloud has been

provisioned can you access it and he goes you're right here it is yes of course what do you want to

do with your marketing he's like I don't think you're set up yet though like you need to do like a

DNS you need to do all this stuff and I was Okay, make a little checklist. I'll give it to the new

FTE that we have just for Marketing Cloud and I'll I'll flag this to them so that they could help me

do it. And they did. And so that's where we're at. So like 10K could in he already saw that we had

Marketing Cloud instantly. He wanted to send emails from Salesforce. I said, "Not yet. We have to

set up our you know, we have to set up our domains, warm them up, all that jazz. I have to move all

the contacts over um and sync everything." And so that was that's that's where we're at um today. So

we've been sinking things over from Marquetto to Salesforce, but you know at literally the goal is

to have this in the next, you know, couple weeks all marketing cloud just running headless the way

10K runs everything else. So some of the steps that they normally have to do to swap people over, we

don't have to do because we already do so much headless. Like it's just saved so much time. We're

implementing it for a headless use case, right? I already knew how to use Marquetto over 10 years. I

don't want to have to relearn everything in marketing cloud. I just want all the infrastructure

there so that 10K in me can send the emails we need to. The agent can do what it needs to do and

that's it. I don't need to relearn the wheel. And quite honestly, I don't want to relearn the wheel.

And I think that's okay today because the agent can do so much of it. >> Yep. >> It's Oh, Sam Blonde

is here. >> Yeah. >> Should I'm going to let Sam Blonde >> live. We have our first special guest on

the agents. We have Sam Blonde. Sam, many of you know from prior SAS engagements at CRO

Confidential, ran sales at Brex famously, Zenovs, uh was our first outbound leader in the old days

at Adobe Sign, Echosign, partnered Founders Fund, and now founder and CEO, one of the hottest GTM

startups >> on earth, the Gent's Monaco, the AI native sales platform, just raised a 50 million

series B led by Benchmark mere weeks after his series A raised 85 million in less than 6 months. And

more importantly, we were maybe one of the first 10 users of Monaco, right? First odd. How early

were we, Sam? >> Uh, you were design >> design. Okay. Just so you know, I give founders zero credit

for design. How you doing for design partners? Oh, we've got 10 design partners. How many customers

do you have? Oh, we have no >> You were pre-revenue. >> Pre-revenue. Okay. Design partners. Yeah.

Um, but we love it. And as a reminder to folks and obviously we're close to Sam in some senses we

have some bias but the more bias was just to use it. It set Ailia up. I wasn't even involved with a

great potential customer in Enthropic its first day. >> Yeah. >> Day one is as as as raw as the

product probably was as a design partner. Hard hard to get a better testimonial than that. Is it uh

set up an appointment with Enthropic? I mean those guys are doing pretty good, aren't they? >> Well,

first of all, um you're you're too gracious in the intro. So hopefully I can try and live up to even

just some small part of like entrance that you provided for me. Jason, thank you for having me.

Awesome to see you both. And I do sort of remember this does not happen for every customer to be

very clear. But I do sort of remember one of the one of the questions that we asked when we onboard

a customer is if you can have a meeting with anybody in the world, who would that who would that

company be? And I I sort of remember Ameilia, keep me honest, I I think the answer was anthropic. >>

Oh, well that's smart. Okay, now I understand that. >> I was like I know people at OpenAI but I

don't know anybody at Antropic really. So that would be my get, right? That would be my get my get

company on outbound. >> But that's smart, isn't it? That is a smart trick in the onboarding, right?

Ask me your dream customer. We'll put our best best energy, best agentic energy into it, right? >>

Certainly prioritize it above all else. No, no, that is not a commitment broadly like you tell us

we're going to get day one a meeting with that customer on, but it did work in this case, but it

worked. >> Um, it it worked. >> Yeah. Let me ask you a related question. One of the criticisms

because it relates to this that we get a lot at Saster because we share our results is we can't it

can't be reproduced. Saster has such a brand. Okay, now I want to get your feedback because it

relates to instantly getting a meeting with Enthropic, right? The brand probably has something to do

with that. Part of my response back is yes, but a lot more people have brand than you think. Monaco

probably even has a brand today and it wasn't even in market 800 between the those goddamn airplanes

flying everywhere the 7,000 billboards the tech crunch articles I'm using a sash classic sast room I

would say you have a mini brand today in market right you don't you're not salesforce right the

archer Daniel Midland hasn't heard of you but you have a mini brand already don't you >> we've been

deliberate about brand recognition with our target customer which is a founder and I think if you

were a San Francisco founder you have likely heard of Monaco at this and that's there's like intent

behind that So to answer the question for the broader audience, >> when do you need and because

you're working with raw startups, right? When do you need a brand to get the kind of results that

Amelia has? Where's that spectrum and what stuff just doesn't work if you don't have the air cover

of at least a micro brand? Well, I'll give you um my immediate reaction where Saster is not

necessarily unique, but you have like forced the the uh envelope or something on this one and then

where Saster actually is unique. The one where you are unique because you have forced it is just in

this concept of deploying agents. I think that you the two of you combined are exceptional at

deploying agents broadly, maybe more specifically go to market agents. You have experience doing it.

more than anything else, you're willing to put in the work to do it and to try and do it. >> I think

in um you know, July 2026, I I do think that most startups with with like oftentimes very technical

people in the companies you can deploy agents and so I I think that you're unique that you've

actually done it. >> I think it's an important it's an important point. Literally um Adam Alfano is

president of Salesforce that a million I know well but he he he texted me from Con Lions saying

these guys need you. Everyone is interested like there's so much budget at Con Lions right to for

agents in in marketing and media over there. There's so much budget but no one's doing it. And so

your point is we've we're just willing to actually do it which um which is different. Right. you are

doing the work and I think at this point it is it is a unique skill set that you all have to be able

to do this. Yeah, it it is something that other people can acquire the skill of and do if if they

put in the work. >> It's such a strange moment in the world where this stuff is just not that hard.

>> It is getting easier. >> Yeah. Okay. But let's finish the point because I think I get this. So

this is probably the number one question we get. Okay. So I asked you what was different about

Sasser. One you said you have a brand and the other said you're actually willing to do the work.

Right. Really important. But you're target unlike a lot of vendors that we've tal we talked to and

use, right? You know, you're targeting startups and a lot of them don't even have a mini brand like

Monaco. They're sub Monaco in terms of awareness. Why does it why does it or be honest, does it not

work if you're sub sub mini brand? This is the number one question I get. Right. But I think we

we've also could could get even more awareness if folks believed it would work if they didn't have a

brand bigger than Monaco. >> Yeah. So, so I think um a couple things and then I I'll get into like

brand specifically and and where Saster may be a little bit unique and then um maybe where there's

just variance. You said something like uh Monaco primarily does outbound. We're end to end in that

we manage pipeline and opportunities all the way through close. We replace sort of legacy CRM that

said on the demand gen side we are mostly outbound. We build your your TAM for you find companies.

agents will then, you know, outbound to people to ultimately generate meetings. And so, so you're

right about that part. And then I I think the thing that uh Saster is unique and that you've done

the work to deploy the agents, but anybody can deploy the agents. So you don't have to be unique yet

you you you have forced that. And then um where I think Saster is um actually unique is around the

brand. The brand does matter. There are three people in in this uh meeting room right now. It's

Jason, Amelia, and Sam. And on Monaco, it's Jason, Amelia, and Sam. Meaning like an agent that is

representing any of the three of us. The likelihood of that um getting a response and ultimately

converting into a customer, and it's actually true for for me and Monaco. Now, also with a bit of my

brand and then and then Monaco's brand, um we will have higher reply rates and conversion rates than

a very early stage startup that definitionally is unknown as a brand. So, so it is that actually

does matter. There's a second um thing that influences this which is um what I would just describe

as message market fit. So, Saster is unique here, but there are lots of companies that are also

unique and can have this even without the brand. And what I mean by that is you reach out to a um

marketing leader today that sells into technology companies and people that might be attending your

annual event. This is gold. If somebody told me I couldn't sponsor Saster and I couldn't have a

present at the event, I would be, excuse my language, I would be pissed. Like, like, do not take

this away from me. And so then, um, the like message market fit almost regardless of the brand. If

you hit a marketing person and you're like, we have the largest audience of AI, you know, attendees,

executives of any conference in the world, if a marketing person is crazy to not reply to that. So,

your message market fit is strong. You can apply that same logic across all of our customers where

had this saying at founders fund or some folks did where it was like we talked to a startup and they

had built a solution in search of a problem and and if you are a startup that has a solution in

search of a problem when somebody receives your message they're kind of like that doesn't resonate

with me that said there's like large variance here where I think both Sastri and Monaco have strong

message market fit and then other startups have less strong message market fit which is maybe a

precursor product market fit. >> Okay, but let's step back because that they are related, right? If

and maybe that hits one of the real issues. If you don't have message market fit, can can Monaco

magically create that for you? Because I think what you're saying, which makes total sense to me, is

listen, you don't have to have the biggest brand in the world, but you have to have some sort of

message market fit for the product to work, right? There's no AI magic that can create message

market fit if the market is reluctant to receive it, right? Because you could use you could use

cloud to come up with spitball ideas for message market. Do you do that or is that not your job? >>

When we onboard a customer, we share with them a document that we call the Monaco method. And as

part of that document, we are very opinionated in two areas. One is what we call the sequence

structure. And so this is like multi-channel. We do things like connection requests first. When that

connection request is accepted, we then send a message with an email. So like we are opinionated

about the ways that we are engaging through which channels with our audience that we believe result

in the highest reply rates. We also are very opinionated on the message structure itself like how to

structure a good email or message over LinkedIn or whatever channel we are leveraging. The value

prop is more predicated on like what does the company do and you as the customer have to help

educate our AI on what your value prop is. You understand your business far better than we do the

day that you onboard. We do train our AI on what your business does, but at the end of the day, like

your business is your business. The value prop is the value prop. The outcomes that you're driving

are the outcomes that you're driving. There's only so much we can do with like sequence structure

and message structure outside of like here's the actual thing. >> All right, let me just ask one

other question just because I get it so often, but the ones that um I think are the grouchiest on

this point, right, are let's say you're at 4 million in revenue, 40 million in revenue, pick your

number, growing 15 to 20%. you have product marketish fit, right? Someone's heard of you in the

market, but you're not hot anymore. And I think their criticism is, look, I've Sam, god damn it, I

I've watched you and all your effing success. I've got 20 reps on my closers on my team struggling

struggling to book anything in today's you're telling me this magic AI sauce is going to give me a

big lift. I don't they're they're the grouchiest of this whole thing. Can you help those folks? The

folks that are sort of stalled but but are growing, right? but they're growing 5%, 10%, 15%. Is

there can you help them with AI and with Monaco or are those ones you don't want to help? >> Two

things come to mind. The first is, you know, to take a step back, we've all seen like the memes on

like Outbound is dead and and that sort of thing. That is not true. Like like >> it's not true. It's

not true. >> It works. Like like there are three people think three out of three of us can attest to

outbound working. >> I forgot about that meme. I hear other means today but it's a good one to echo

right it really does work in today's world right you're selling your book but it's true >> concept

now like it is a different ver version of the outbound that existed even in 2018 so like outbound

evolved but it works and I think like can attest to that um >> I'll just I just I'll give one funny

example Ailia will think it's funny so so we we've just rolled out our AI VP of finance we were

talking about it earlier and I talked about on the la on the last show and a lot of people in the

industry kind of got let up right it was really good for build.com but this guy that builds an AB AI

VP of finance wrote this LinkedIn post today. It's like Jason Lin and Ameilia rolled out this VP of

finance. It seems really great, but here are the limitations. It's not going to work with really

complicated products. It's not going to work with variable price and it's not going to work well.

Some of it was right, some of it was wrong, right? But it's a good analysis. We have budget. A

million and I have budget to we're we're two weeks into our AB VPF. We don't want to be running this

agent. Okay. At the very end, he says, "Jason, when you're ready, hit me up. Look, I'm out. We're

outboundable. We're not wedded to this. It's like go sell us an agent that is materially better than

what we will drop it. We we do not want to spend the rest of our year building. Go Jason, go contact

me. You know, we outbound still works. Like I don't know whether outbound works to to if you're the

10,000th veteran to someone that has no interest in buying, but we are we're literally in market,

right? But but he him telling me at that's his best sales pitch is at the end of a LinkedIn post

saying, "Jason, I'm here when you're ready." I mean, it's it's an F, isn't it? From a sales

perspective. Um, in in this instance, you would think that an agent I don't know if that was the

human that wrote that message or >> Yeah, that's what I would think. Also, you almost wish it was

the AI in that the the AI almost certainly would have done a better uh job there. >> Yeah. So, it's

kind of it would have right >> maybe you're the host and asking questions, but like this is like a

bit of a question for you. I'm curious. Uh the way that we describe the Monaco I is that this gives

you um whether you're a founder, whether you're a salesperson, just an employee at a company, it

gives you leverage to spend time on what we would describe as higher ROI activities, but really the

activities that that agents actually can't do. Agents are not hosting the agents podcast right now.

Like like the two of you are spending your time doing this. And so I'm sort of curious like do you

think about your agents in a similar way where it gives you like the the leverage to spend your time

doing things that agents just just aren't as good at or or can't do that. That's certainly how like

we describe the leverage that Monaco provides to customers. It's not that like we're a silver bullet

for go to market. It's that you can spend more of your time customerf facing. You can spend more of

your time doing the like creative campaigns that an agent isn't going to do for you. Well, >> it's

interesting. And I want to get a million thoughts too. That is the narrative in social media out

there and it is inherent by definition true right we are able to we work harder than ever and we are

able to do higher value activities and then we were able to produce we have triple the output we

were before agents okay with fewer people right fewer people triple the output. So that's the math

you're describing, right? So, and that's a good way to describe it when for the Monaco sales team,

okay? But here's the truth. That's not really how it works now that we're the it's much more than

that. The first thing we do every day is talk to our agents. This is how it's not about leverage.

The fir Ameilia gets up in the morning, gets her coffee, and talks to 10K. That's the first thing

she does. I have a different flow for me. It allows me more creativity to build stuff, right? But

it's not about pro. Like literally she's talking to 10 10K today came came up with the idea to rip

out Panda do and build out our own contracting system. 10K I came up with that idea. So it's not

just about freeing up her time. It's that because she talks to this agent every day. Um we

collaborate. It's so it's more than it's more than that. You don't know what actually is going to

come out of your agents this week. We didn't know that by hooking the agent up to Bill Brex and

everything else you could come up with all this automation. Do you agree Millia? >> Oh 100. I'll say

too on and it ties to the outbound piece that you're you've been mentioning Sam is that I think some

people also have this misconception that because we use Monaco we use Asian force we use all these

like outbounding tools in artisan like that we don't still do high value outbound activities on top

of that which we absolutely do like >> every time even this week right so we're we're postual we've

sent out and this is maybe like a current customer flowrenewal flow right so we've sent out

sequences and I've used all the platforms because I just want to test how how the renewal rates and

responses rates are um post annual on the different platforms. So we've been, you know, giving that

up, sending out to folks because it can send to many more people within our customers, like

everybody who came to SAS and on the Monaco team, everybody who came to SAS on the Salesforce team

versus like when I email Salesforce, I'm probably only going to email Adam and Justin, like just my

top two people, right? Like it can do it can go deeper, but I'm still emailing Adam and Justin

myself. Like literally, even this week, I like sent the article we put up. I told him about some of

the stuff and issues we're having with Qualified. I was like, I'm still doing that. It's not again

to your point earlier like outbound is definitely not dead but I think the activities I'm doing are

much more high value when it comes to outbound and they're way more additive like doing this podcast

doing things like that still sending you know to your point more creative outbound campaigns that I

can come up with because the agent has freed me up because it's doing all the check the box normal

stuff that you should be doing with your prospects and customers. >> Yeah, it is. It is much more

valuable. Never had this time before. Actually, to answer Sam's question, I skipped ahead to this

collaboration piece, which is kind of crazy, right? But you have time. You never had time to do this

before the agents. >> No, I had to do the main normal stuff. >> Yeah, but you didn't even have time

to do it. You didn't even have time to s We didn't even You didn't You didn't do any Like, you

barely did any of it. Now you have time to do a little bit every single day >> and the results are

there. It's more revenue from it. we've generated more revenue because Amelia's time has been freed

up to just manually reach out to the highest value prospects and renewals because she doesn't have

to do all this other crap >> it's very freeing right um yeah I mean I think let's go I want to go

back and ask Sam a few questions while we have them but to to me I the way I think about to this

meta question is it's like support like support and coding got there before GTM and sales right and

support if you look what happened whatever vendor you talk to you know uh 50 to 70% 80% of support's

automated through AI. It used to be terrible. Now it's pretty good, right? And often it's better

than a mediocre human could do. It it really sales should be like that too. It doesn't mean humans

shouldn't be selling, but humans should not be doing so many of the activities that many companies

still practice. You just you shouldn't be doing it. And I personally think net net it means we'll

have sales teams about half the size we used to. Like owner for SMB does 2 million per rep, right?

So that's something that we wouldn't have thought was possible in the old days, right? You're you

don't have to be hyper efficient at Monaco when you don't want to be, but you can probably run it

twice the efficiency we've done in the past, right? If you want to in terms of bookings per rep,

right? >> You took the the words out of my mouth in that um I I think today it's 2x in two years. Is

it 5x is efficient like like revenue per rep than what we had preai? And then like what what the

business chooses to do with that level of efficiency I is is up to the business. You can have half

the size of the reps or you can have more reps and and continue to get more revenue per rep. If you

have the demand and and reps are spending all day customerf facing closing deals, you may want a

larger sales team if they were doing 5 million instead of one. But certainly you can make the trade-

off that we want to have a leaner sales team that we can grow much faster. >> I'll give you one

thought for what it's worth than let's talk a couple more sales things before we lose you. But I I I

think Ameilia and I agree with you. But the one thing that I think we've learned being at the

bleeding of agents, those relationships are more important than ever. They're with the FDs. They're

not We don't care about the sales people. >> Yeah. >> In fact, in the AI age, you want I don't even

want to talk to a salesperson. Get me my FDE. >> I don't I don't want to hear I don't I want to be

on text message with some kid. I want to talk to my FTE that fixes the fact that the qualified agent

is still selling SAS annual 2026 tickets. We that is a relationship or our FD at Replet. I talk to

them every day. We we just invited Ameilia up to their office to go pitch with them next week. Like

those relationships are better than than I've ever had with a software vendor. Like our FD relation

and I history of software I and I I think Emilia you'd agree too never had better relationships ever

than the FDS. This is under discussed and and I know we've got to move. Not everyone can have these

and but I don't want it to so so maybe even the definition of sales I think changes right those FDs

can be involved in the sales process they can even report to the CRO I don't care but that's where

the value lies not in a a sales rep that barely understands the product uh having freed up to spend

more time I mean I don't care I don't need Millie do you want any more time for most of our sales

reps you just want more FDU time right >> I don't even know in some cases I don't know who our sales

rep is. I just only know who like I don't know who my sales rep is to qualify. I know who your sales

contact is. >> I don't know who my sales contact is. Like I literally know who my FE is. >> Yeah, >>

I could imagine a world I don't Let's Let's get back into I could actually imagine a world in a

couple years, right? I mean, it's changing so fast, right? Where I think a mistake vendors are

making. I don't know how you're thinking about it. I think all vendors today should offer

immediately cancelellable contracts with no risk and instant downgrade and full data portability.

And the reason I say this is if you took all the risk out of the sales process for me. Mark Beni off

made this point actually on the 20VC with me and Harry last year, right? He said he wished he could

do this. He said at even at Salesforce, he wished everyone had an FDE and would be fully deployed

before they paid. This is Mark saying this. He said I can't. This is him last year. If you can do

this, I I don't need a sales rep most of the time because if I know I I'll sign up today. I'll give

you my credit card, send me the invoice, but give me my FTE and if if I don't like it, I'll just

cancel and I'm not going to get ripped off. Like Marquetto just wants to raise our prices 20% again

and all they do is threaten us. Like I don't like I I need to go through so many hoops to buy that

product, but then I need a human, but do I need a traditional AE? Do I need Ocean uh nudge me to

close the deal? I want my FTE. I don't know. And maybe that's good for Monaco because you you can

get rid of that middle part, right? >> Monaco provides all the value of getting them into the

funnel. >> We're we're moving in the direction that you described, which is the sort of like as

little of an upfront commitment as as we can sort of uh stomach or something because we do have to

allocate some resources and that's expensive and and we want we we have to make sure that there

aren't like you know people just kicking the tire or something and but philosophically very aligned

with what you described which is maybe there are two points there Jason not not just one. One is

like no long-term commitments and financial oblig contractual and financial obligations and we sort

of like live and die by the um benefits that we are providing to customers. I I think like that that

is a world that I think >> such a virtuous cycle too it forces you to be better doesn't it? >> It

absolutely like it's hard to argue as a customer that that is a uh better world to live in or

something like that. And then the second thing that comes to mind is um we we we want to do as much

of or all of the work that we can on behalf like just make getting up and running and successful as

easy as possible and as low lift as possible on the customer's part. Now it doesn't mean it's zero

because in some instances it it actually benefits the customer to provide some information through

like you know back and forth in in a meeting style environment. Um so it may not be like absolute

zero effort but um any effort is in the spirit of um like better outcomes and so like taking on as

much of the work on behalf of the customer as you possibly can. This is not the world in either of

those scenarios, Jason, that we've lived in for uh since the day that I joined Echosign, which is um

contracts with financial obligations that are at least 12 months long and when you buy something

like you can go consultants or you can do it yourself. >> Yeah. Yes. Yes. We'll give you the the

like your accounts on but like you you're you go uh get it set up. >> Yeah. It's a good thing. All

right. Two We keep going. Two more things I want to do before we lose you because certainly we've

gone longer than the nominal 20 minutes that Ameilia wanted to do for the the guests and the agents,

but if you have a couple more I want to do two more things. I want to talk about >> highlight of my

day. Let's let's keep going. >> Okay. I want to talk about because we were just just living this and

talking about I want to talk about how many agents and then I want to then I just want you to tell

us like a couple things coming on the road map for Monaco. So the first one you said it's

interesting you said what works well at Monaco is having digital Sam, digital Amelia, digital Jason

reach out, right? Get it? classic Parker Conrad old Zenit's playbook done again works right PRC you

know love uh you know it's just done right okay uh only a few people will get that um the problem

here's the problem there's four or five digital Jason and Amelia's >> there's one on our website

that I built to help founders qualified has a and it has a video of digital Amelia she's really

there so you can really talk to her and interact with her right there's a different digital Jason on

deli that answers other issues uh we have agent force which might come from a lot These come from

one of your email addresses, don't they, Amelia? There might be seven digital Amelia, two or three

digital Jasons. Um, how do we manage this? And are we going to tolerate having so many GTM agents in

12 months? >> Well, several things come to mind. I I think um you you all at Zaster um if we apply

sort of like your tech stack um you look like a let's call it a 100 plus person technology startup

and what I mean by that is like uh yes it is true and we'll go a little bit even more up market but

like the Brexes of the world right there's probably 1500 maybe 2,000 employees there are multiple

goto market agents and they live on top of Salesforce and they've got the inbound agent and they've

got the um outbound agent and they've got the uh I don't know insights and act like all of these

different tools like you all sort of are are like very mature relative to the headcount of uh SAS

from an a just a tech stack standpoint a go to market tech stack standpoint and by the way you were

unique in the way that you use Monaco in that you might be in of one that that we are not your

system of record or CRM replacement um and that we aren't your like effectively full go to market

stack and So philosophically we believe that the the like direction of the market is that you just

want one vendor and one vendor is your inbound agent, your outbound agent, your insights and it it

is all of your agents on living on one data plane with full access to all of the information in one

platform. um everything may be like talking to your salesforce but definitionally some things do

live in silos like it's difficult for um >> oh it's creates a lot of issues >> and so um one of the

the sort of like approaches that we have to building Monaco is not just that we are agent native in

the product itself >> but we believe the cost to building software is trending towards zero um I

don't know the exact math on this but we can build software today let's call it 5x faster than we

could three years ago before all of the um coding assistance Well, if that's true, >> faster. Yeah,

maybe more than probably more. >> It's reasonable to believe that in 3 years from now, we can build

5x faster than we can today, if not even more. And so then like if that is true, everything from a

go to market standpoint should live in the same place. Uh and that is >> Yeah. All right. Let me

just ask you one specific question. So I think you have to build everything then, right? Um like let

me an example like ride alongs, okay? agents that join sales calls. Okay, every there's a lot of

vendors building this and there's a lot of different approaches. My view is that in six months, 12

months uh ride alongs will be like notetakers. Every GTM agent will have to have a and some but some

aren't that good. But there you there's just no you like you would never send the 22-year-old kid

into a sales meeting without a ridealong agent making sure that they don't say things the Monaco

could do things that it can't do, right? >> Um so do you have to build that? Do you have to build

the digital AE? Do you have to build uh all the inbound qualif like inbound qualification is a huge

deal for us? >> Yes, >> it's a huge deal for like we could not run SAS without agentic inbound qual

you are you going to build all that over the next 12 months because otherwise you can't be the only

agent, right? >> Yeah. Um the the answer to your question is yes. From a from a sort of like

prioritization standpoint, inbound agent is um uh in development. So, so like imminent and near-

term. Um, the the like ride along thing, this is one where like I agree with you. Um, I um what we

could debate and and I actually don't even have a strong opinion on is the like format of this. Is

it like does digital Jason join calls? It's like notetakers. It's just going to happen. You can

criticize it. There's no excuse to like if I'm actually get dragged to his sales call, a Zoom,

there's they better know the answer to my questions in AI. So just like no doubt they will express

themselves in different ways. Some will be clones which I actually think we've learned from digital

Amelia unqualified people like the real people think you want cartoons or stuff. They want the

familiar like I actually think you should have digital Sam joining every call at Monaco because

people will trust and they know it's not you but they know it's trained like you. Okay. Why not have

every Monaco sales pitch have digital Sam on that Zoom as long as it's well reasonably well trained.

What's the downside? >> Um, >> what's the downside? There's only upside, right? >> We are totally

aligned whether it is digital SAM or something that is ensuring the the the like quality of

responses from the human that is AIEL that is surfacing the information or somehow stepping it like

what the format is may or may not be like digital person that joins as a third party. I I I don't I

don't have like a strong opinion there. Your original question is are we are we going to build it?

Yes, we were going to build that. We >> you have to build to achieve your vision. You have to build

everything, right? >> That that you nailed it. Like part of this is shouldn't shouldn't digital Sam,

Jason, Amelia or like whatever the format of the the like AI real time assistant, shouldn't that be

a feature? Like like shouldn't that be a feature of a broader platform that has far more information

than just whatever we've trained by feeding that one narrow product? Um, should shouldn't that be a

feature of like a far broader platform that uh has tailwinds from learning from the types of

customer experiences and all of the data? >> Yeah, it should be um I I I think the I think we're

just getting I think the early ride along products are pretty weak because they were poorly trained,

right? Some of the best ones now are from folks that do like enablement because enablement is

already trained in your organization, right? So if you enable your apps, you you get some benefits

from it, right? because it's it it's it's it's well trained automatically. But um it's just one

thing, but I just I say this to people, they think I'm crazy. It's like note-taker. Like I mean, we

can't even keep up with the noteakers, can we? But but why not? You should have write alongs. Every

GTM thing should have there's no there's no noteakers are just one little piece, right? They just

they just sort of help the noteaker. There should be no mistakes should be made in a sales call. No

mistakes there should be some sort of t-shirt. I need a better a more pathy way to say it, but no

all no mistakes behind or I don't I don't know what it is. It's just not because otherwise we'll

just talk to our because otherwise we just want to talk to our FD. >> That's right. >> Otherwise, we

just want to talk to our FD, right? Okay. So, tell us a couple things then we'll break. Tell us a

couple things coming because you're going now I learned you're going to build it all which I'm

supportive of. Right. It's a big vision. Um it'll be interesting to see where it goes. But I at

least think for your ICP you can do it because you have a great team and a lot of energy, right?

Whether that'll work in the enterprise, we'll find out, right? You may have you may have to cave,

right? when they when they give you eight figures, but they need integrations with 20 systems and

want you to have an external API and some other stuff, right? We'll see. But, uh, what's what's

coming the rest of the year that you're excited about? Uh, let's see. Well, one like event coming up

and then maybe I'll actually leverage something that you had described Amelia does every morning and

sort of apply that to Monaco. Um, so the the event that's coming up, we are going to GA. We think of

ourselves right now in public beta. We did this in uh February. So we're now, you know, four to five

months in this sort of like um uh public availability. Um but we will move to general availability

here in the next let's call it like four to six weeks. Uh a and so there are some really cool

technical advancements that um are coming alongside that specifically in this world of agents.

Jason, you talked about like inbound agent. It's just like agent overload uh that comes with uh GA.

We have been during this public beta process, we've really been training a lot of agents on the

activities that um our customers are taking in their accounts, but also our FDES are taking um and

so then truly agentic. There's one really cool one you you said that um Amelia wakes up every

morning and and starts talking to 10K um and like learns things about your business from the agent

that Amelia wouldn't otherwise know about the business. Is like these are my words, not yours, but

uh or certainly my interpretation. Um the like insights and actions agent is really cool where >>

Yeah, that's good. That's all we talk about. You have to have a great internal agent in the product.

You're just dated like it's just not cool, right? You got to have a great internal agent. Actsite in

Yeah. >> It's tell and it's just it's data trends. >> So, so inside of Monaco, I can it'll give me

all my insights and actions. I can talk to the agent and figure out stuff. I can I can riff on stuff

together. >> Well, you can riff on stuff together. um the Rivon stuff together is available today

and it's reactive. So in Monaco we have the like chat um and it lives on all of the data and you you

can chat and uh learn about your business proactively. Um the thing that I think is really cool is

the like we're going to tell you stuff about your business and you don't even know the question. You

don't have to know the questions. >> I seek comes up with three ideas a day for us. It's exhausting.

This our only kibbits is if you you miss a couple days it's got nine things it nags you to do. Uh

but but I would say like half of them are are pretty good, aren't I? I mean they're all good and

like half of them are really good prioritize. So if you're prior productizing like people are going

to people may not get it but they're going to love it, right? They're going to love it, right? >> It

is both the insight >> and then the what do you what should we do with this? Like and sometimes we

say startups the insight may or may not match the anecdotes, right? like we we can give an insight

and the person um reviews it, which we're doing right now as part of this like beta um where

somebody reviews it and they're like the data is correct and it's not something that we should

action like like those two things can be true. That said, what's really powerful is the like here is

the insight. >> Wow. like now that you say that it matches the anecdotes and then the action is the

like okay what are we going to do inside of Monaco given this learning where it's like

repprioritizing the way that we score your accounts or reach out to people who we're reaching out to

like all of this stuff is just on autopilot in a way that is is it used to be so much work >> uh and

and and now it's just like the like you're like yes uh it's really cool >> yeah okay that's pretty

exciting Um, >> cool. What else? What else did we miss? Anything else you want to hit today, Sam? I

know we went over. Anything else you wanted to talk about? >> Oh, you all are the best. Thank you

for having me on the show. Thank you for having me at the annual and just appreciate all of your

support. Um, so, um, thank you so much. >> Cool. Let's go GA, man. All right, everybody. Thanks.

Thanks again for joining the agents. Much more to talk about next week. Yeah. And again, going to

Sam's point, it it can seem like what we're doing is at the edge, and hopefully folks that watch and

listen benefit from that, but you can do everything we did. All we're doing is just is we're just

motivated to do more of this than you. Any single thing that we've done with our agents, you can do.

See you guys next week. Adios. Thanks. >> You're listening to the official SAS AI podcast brought to

you by Hey everyone. If you're using AI in your go to market or you want to get going, then you need

to try Monaco. We're on it. Saster's on it. We love it. We use it for outbound, but you can use it

for everything actually. It's everything you need all in one place. At Monaco, it's the all-in-one

revenue platform and your system of record. It builds your TAM, runs outbound, captures every

interaction, and manages pipeline in one place. All in one great unified platform. Go to monaco.com

to learn more. Tell them Sasker sent you.

## Summary (10 bullet points)

- I will say it's interesting because bill.com which many of you probably use well you know for accounts receivables accounts payables um has a lot of we've been using it for many years now so it has a bunch of historic data in...
- like they're not going to upload that contract to close one and then send it to the customer and say hey thanks for you know becoming a customer blah blah whatever you know the automated email list and here's your invoices...
- If you go on to basically what it does for us and Amelia will dig in more is qualify inbound leads which is very valuable instead of waiting weeks to see if a human decides it's worth their time to reach out back to a human...
- nominally it was not it's not anywhere near the price Marquetto charges us it's not even a third of the price so thankfully I was like you know even if I don't stay on it it's a low risk right one it's a low risk in terms of...
- Monaco probably even has a brand today and it wasn't even in market 800 between the those goddamn airplanes flying everywhere the 7,000 billboards the tech crunch articles I'm using a sash classic sast room I would say you...
- I hear other means today but it's a good one to echo right it really does work in today's world right you're selling your book but it's true >> concept now like it is a different ver version of the outbound that existed even...
- Not everyone can have these and but I don't want it to so so maybe even the definition of sales I think changes right those FDs can be involved in the sales process they can even report to the CRO I don't care but that's where...
- I I think um you you all at Zaster um if we apply sort of like your tech stack um you look like a let's call it a 100 plus person technology startup and what I mean by that is like uh yes it is true and we'll go a little bit...
- um everything may be like talking to your salesforce but definitionally some things do live in silos like it's difficult for um >> oh it's creates a lot of issues >> and so um one of the the sort of like approaches that we...
- like now that you say that it matches the anecdotes and then the action is the like okay what are we going to do inside of Monaco given this learning where it's like repprioritizing the way that we score your accounts or reach...

## Key B2B Marketing Learnings

- Start with customer and audience understanding before choosing content topics or formats.
- Distribution is part of the strategy, not a final step after publishing.
- Founder and executive voices can build trust faster when they share specific, experience-backed points of view.
- LinkedIn content works best when it teaches, provokes useful discussion, and makes expertise easy to remember.
- Organic content should connect to revenue by shaping demand, sales conversations, and buyer confidence.
- Brand building compounds when the message is consistent across posts, videos, newsletters, and community touchpoints.
- AI can speed up research and production, but the useful advantage still comes from sharp human judgment.
- Repurpose strong ideas across formats instead of treating every post or video as a one-time asset.
