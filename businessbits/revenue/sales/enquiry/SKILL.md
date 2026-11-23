---
name: enquiry
description: Handles an inbound sales enquiry for a small consultancy or agency. Checks whether it is a fit, records it once, drafts a reply for approval and sets one next step with a date. Use when a message, form submission, referral or introduction arrives from a possible client, or when the user asks what to do about an enquiry or how to reply to one.
license: MIT
compatibility: Any assistant that can read these files. Recording needs persistent files or a connected store set up by business-setup.
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.1"
  status: draft
---

# Enquiry

An enquiry is the cheapest attention a business gets and the easiest to lose. Decide once whether it's real, record it once, and give it one next step.

Steps are labelled: **Fetch** reads a fact exactly, **Judge** needs weighing, **Check** tests the result, **Approve** is the user's decision, **Record** writes it down.

## 1. Read the profile (Fetch)

Read `business/profile.md`, or the profile record in the user's store. You need: who the business is for, its reasons to turn work down, reply time, voice and record store. If there is no profile, say so and offer to run business-setup first. If the user wants an answer now, carry on and mark every judgement that needed the profile as provisional.

Read [RECORDS.md](RECORDS.md) for the enquiry, contact, organisation and activity records.

## 2. Find what already exists (Fetch)

Search the records by person, email domain and organisation before creating anything.

- An existing client is not a new enquiry. Treat it as account work and tell the user.
- A second message in a thread updates the existing enquiry record.
- An organisation on the suppression list: tell the user, and don't draft outreach beyond a polite reply to what they asked.

## 3. Capture it (Record)

Create or update the enquiry record. Keep their words, not a summary. Fill only what the message and the user say. Everything else is `unknown`.

## 4. Judge the fit (Judge, then Check)

Fit has two halves, and both must hold:

- **Service fit:** what they expect is something the business can actually deliver, and deliver honestly.
- **Commercial fit:** what they want to pay can cover what the work costs.

Interest is not fit. A keen, technical, engaged founder can still expect something the service can't do, or want it cheaper than it can be done. Work volume on its own is not a reason to decline: a big job is a capacity question for the proposal.

Check the enquiry against the profile's signs of a good fit. When the profile is thin, use these. Each one is a question about the buyer's situation, not their sector:

1. Can they describe a piece of work that repeats, or a moment where things go wrong, in their own words?
2. Can the cost of the problem be described in time, quality, customers, risk or money, without inventing a return?
3. Is there a plausible route for the business to deliver it: the systems, the data, a person to approve the result?
4. Is there a paid path: budget, or a person who can find one?
5. Who will own the work, and how does a decision get made? If nobody is named yet, that's settled in the proposal's terms. It isn't a reason to refuse a call.

Turn it down, politely and with the reason recorded, when the profile's reasons to decline apply, when they want advice rather than a piece of work, when what they expect can't be delivered, when the price they want can't cover the work, or when the risk is beyond what a one or two person business can carry.

Write the fit as `fit`, `partial` or `out-of-scope`, with one line saying which questions passed and which failed. A failed question is a thing to ask on the call, not always a reason to decline.

Check: every claim in the fit line points to their words or the profile. If it doesn't, change it to `unknown`.

## 5. Choose one next step (Judge)

| Situation | Next step |
|---|---|
| Fit or partial | Offer a short discovery call. One call to action. Scoping happens inside discovery |
| Fit, but nobody is named as owning the work | Offer the discovery call anyway. Note ownership as a term the proposal must settle |
| Vague request ("we want an AI agent") | Offer a discovery call aimed at finding the work, and ask one question about where time goes today |
| Out of scope | A short, kind decline, with a pointer elsewhere if you know one |
| Existing client | Hand to the user as account work |

Every open enquiry has one action and one date. The date follows the profile's reply time. The default is the same working day.

## 6. Draft the reply (Judge, then Approve)

Write in the user's voice from the profile. Answer what they actually asked. Then:

- open the conversation with a question about the cost of the problem, never a capability pitch
- one call to action: the free discovery call, never a free audit or unpaid work
- no prices, dates or scope promises
- don't tell them facts about their own business that they didn't share
- short. Three or four sentences is usually enough

Put the draft in `business/drafts/` or show it in the conversation. The user sends it, or approves that exact text before anything sends it.

## 7. Record what happened (Record)

After the user approves and sends: an activity record with `approved_by`, the enquiry status updated, and the next step and date set. The organisation's relationship becomes `lead`. When a discovery call is booked, create the opportunity at stage `discovery` and link it from the enquiry.

## 8. Check before finishing

- One enquiry record per enquiry. Nothing duplicated.
- The enquiry has a next step and a date, or is closed with a reason.
- No field holds a guess.
- Nothing was sent without approval of that exact message.

## Output

- Records from [RECORDS.md](RECORDS.md): the enquiry, the organisation (as `lead`) and the person, created once or updated if they exist. An opportunity at `discovery` when a call is booked.
- One next step with a date.
- A reply in the user's voice, waiting for their approval: shown to them, or saved as an email draft when this assistant can create drafts.

## What it replaces

Reading the enquiry, checking whether the sender is already known, weighing the fit, writing the reply and logging it. Time saved: not yet measured.

## When it goes wrong

| Problem | What to do |
|---|---|
| No business profile | Run business setup first, or judge with the user and flag every gap |
| The sender already exists in the records | Update their records; never create a duplicate |
| Not enough to judge fit | Ask the one question that decides it in the reply, rather than decline |
| No voice set | Draft plainly and say the voice isn't set |

## Never

- send a reply without the user approving that exact message
- promise a price, a date or a scope
- invent a budget, a deadline or a fit score
- close an enquiry without a recorded reason
- treat an existing client as a new lead

## About this skill

Made by Pedro Borrero at borre.ro. Part of BusinessBits, in the BoringBits repository, for one or two person UK businesses. Draft. Free to use under MIT, with credit. Provided as is, with no support.
