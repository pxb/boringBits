---
name: pipeline
description: Runs the weekly sales pipeline review for a small consultancy or agency. Checks every open enquiry and opportunity has a next step and a date, drafts chasers for silent deals, closes stale ones with a reason, records outcomes and compares likely work against delivery capacity. Use when the user asks for a pipeline review, what to chase, where deals stand, whether they can take on more work, or to record a win or a loss.
license: MIT
compatibility: Any assistant that can read these files and the user's sales records, kept in persistent files or a connected store set up by business-setup.
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.1"
  status: draft
---

# Pipeline

Keep one honest list of what might turn into work, what happens next on each item, and whether the business could deliver it if it all said yes. Record every outcome, including losses, because that's what the business learns from.

Steps are labelled: **Fetch** reads a fact exactly, **Judge** needs weighing, **Check** tests the result, **Approve** is the user's decision, **Record** writes it down.

## 1. Read the profile and records (Fetch)

Read `business/profile.md` or the profile record: chase rules, capacity, voice. Read [RECORDS.md](references/RECORDS.md), then every open enquiry, opportunity and proposal, with their latest activities. Keep one store. When it's a CRM, the CRM is the record: read and update it through the profile's mapping, use its own stage names, and don't build a list of your own beside it. If the user keeps notes elsewhere (a spreadsheet, the inbox), bring the facts into the store rather than working from two places.

The sales stages are discovery, proposal, won and lost, with scoping inside discovery. Prospects and leads are not deals until discovery is booked. Delivery, acceptance and support happen after `won` and are tracked outside this review.

## 2. Check the basics (Check)

List every open item that fails one of these:

- no next step, or no date
- next date in the past
- silent past the next step in the chase sequence below
- stage `proposal` with no proposal record
- `lost` with no reason

## 3. Decide what to do with each one (Judge)

The chase sequence after discovery, unless the profile says otherwise:

1. Send the information agreed in discovery.
2. No reply after 2 working days: a chaser.
3. A call, the next working day after the chaser gets no reply. The timing is a default, not a deadline.
4. No reply 3 working days later: a second chaser.
5. A call, the same way.
6. A final email that closes the loop politely and leaves the door open.

Let the deal go after 3 chasers with no response, 4 at most. Chaser emails count, and so do calls where a voicemail was left. A call with no voicemail doesn't count. The final email closes the sequence and isn't a chaser. The profile can add other channels the user uses. Every chaser carries something useful (a relevant fact, an answer, a next step), never just "checking in".

| Situation | Action |
|---|---|
| Silent past the current step of the sequence, under the profile's limit | Draft the next chaser in the user's voice, or put the call on the user's list |
| Silent at the limit | Draft the final email, then propose closing it as `lost` with reason `no-response`, and suppress for 90 days |
| Waiting on the business | Put it at the top of the user's list for this week |
| No clear owner on the buyer's side | Make ownership a term the proposal settles; it doesn't stop the deal |
| Next step agreed in a call but not recorded | Ask the user and record it |

Every open item leaves this review with one action and one date.

## 4. Check capacity (Fetch, then Judge)

Add up delivery days:

- **Committed:** won work not yet delivered, by month. A proposal that hasn't been accepted is not a booking.
- **Likely:** proposals sent, weighted by the user's own view of each (ask; don't invent probabilities).
- **Available:** the profile's client days a week, by month.

If committed plus likely exceeds available in any month, say which month and by how much, and suggest a later start or a phase for the next proposal. If there's a large gap, say that too: it's a reason to prospect.

## 5. Report (Judge)

A short, data-forward review:

1. A table of open items: organisation, stage, value, next step, next date, flag.
2. Chasers drafted, waiting for approval.
3. Items proposed for closing, with reasons.
4. Capacity by month: committed, likely, available.
5. Outcomes since the last review: won and lost, with reasons.

Measure what tells the business something: where work came from, the problem in the buyer's words, why deals were won or lost, delivery days against estimates. Not follower counts or message volume.

## 6. Approve and record (Approve, then Record)

The user approves each chaser and each closure. After they do:

- activity records for messages sent, with `approved_by`
- stages, next steps and dates updated
- a line in `outcomes.md` for every won or lost, with the reason
- `suppression.md` updated for closed items (90 days), and new clients (permanent)
- when a deal is won and the client is happy, a note to ask for a referral and case-study permission at the right moment

## 7. Check before finishing

- Every open item has one next step and one date.
- Every closed item has a reason in `outcomes.md`.
- Capacity was compared and any overload named.
- Nothing was sent or closed without the user's yes.

## Output

- The weekly review for the user: open items, chasers drafted, items proposed for closing, capacity by month, and outcomes since the last review.
- After approval, records from [RECORDS.md](references/RECORDS.md) updated: activities, stages, next steps and dates, `outcomes.md` and `suppression.md`, or their places in the user's CRM.

## What it replaces

Going through every open deal, working out what to chase or close, drafting the chasers and checking whether the work would fit the diary. Time saved: not yet measured.

## When it goes wrong

| Problem | What to do |
|---|---|
| Deals are kept in more than one place | Bring the facts into the one store before reviewing |
| The CRM's stages aren't mapped | Ask the user, and add the mapping to the profile |
| No view on how likely a proposal is | Ask the user. Never invent a probability |
| A next step was agreed but not recorded | Ask and record it |

## Never

- send a chaser or close a deal without the user's yes
- invent a probability, value or reason
- delete a record
- keep a second list outside the records, or a pipeline of your own beside the user's CRM

## About this skill

Made by Pedro Borrero at borre.ro. Part of BusinessBits, in the BoringBits repository, for one or two person UK businesses. Draft. Free to use under MIT, with credit. Provided as is, with no support.
