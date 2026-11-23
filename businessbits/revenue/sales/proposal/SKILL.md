---
name: proposal
description: Prices and writes a proposal and statement of work for a small consultancy or agency, and handles change notes once work is signed. Sets the price from value and the business's floor, writes scope, exclusions, acceptance and payment so scope creep has a written answer, and checks capacity before anything goes out. Use when the user needs a quote, proposal, statement of work or price, asks whether to offer a discount or how to handle pushback on price, or when a client asks for something extra during a project.
license: MIT
compatibility: Any assistant that can read these files. Recording needs persistent files or a connected store set up by business-setup.
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.1"
  status: draft
---

# Proposal

The proposal sells and the statement of work protects. Price the outcome, write down exactly what's included and how changes are handled, and let the user decide before anything goes out.

Steps are labelled: **Fetch** reads a fact exactly, **Judge** needs weighing, **Check** tests the result, **Approve** is the user's decision, **Record** writes it down.

## 1. Read the profile and the opportunity (Fetch)

Read `business/profile.md` or the profile record: offer, prices, day rate, floor, payment terms, proof, capacity, voice. Read [RECORDS.md](RECORDS.md) and the opportunity record with its notes and call activities. If there's no profile, offer business-setup first.

## 2. Decide whether to propose at all (Judge)

After discovery, write a proposal only when:

- the problem and what solving it is worth are captured in the buyer's words
- there's a first idea of the scope
- the work is deliverable, honest, addresses their actual problem and gives them value
- it is commercially viable within the profile's pricing. If it doesn't fit the standard prices, price it custom rather than forcing it into one

If one fails, tell the user which, and whether another conversation, a smaller first piece or a polite no is the better next step.

Scope and send the proposal before any work starts, including for friends and early clients. Work done ahead of an agreed price leaves the business either undercharging or surprising the client.

## 3. Confirm before pricing (Check)

Don't write a price until these are known. Ask the user for any that are missing:

- the buyer's problem in their words, and who owns it. If nobody is named, the proposal names ownership as a term to agree: who owns the work, the result and its upkeep
- what "done" looks like to the buyer: the acceptance test
- the systems, data and people the work depends on
- the budget, or that the user has asked
- whether the client may be named as a case study
- whether the work reuses something the business already has, or is built new for this client

Raise budget early, even with a friend.

If the buyer already pays another provider for part of this, that spend proves the need. It isn't an objection, and the other provider isn't a competitor to displace. Find the gaps around it (missing steps in the process, people without the time, repeated manual tasks) and propose work that complements what they already have.

## 4. Estimate the days (Judge)

Estimate from how long similar work actually took, not from first principles. Name the past job the estimate is based on. Estimates written from scratch usually run long; say so if there's no comparable job.

## 5. Check capacity (Check)

Compare the estimated days with free days in the delivery window: the profile's client days a week, minus days already booked on signed work and proposals likely to sign. If it doesn't fit, tell the user and offer a later start or a first phase that fits. Don't quietly send a proposal the business can't deliver.

## 6. Set the price (Judge, then Approve)

Follow [PRICING.md](PRICING.md). In short: choose the basis by the kind of service, check the effective day rate clears the floor, write one return-on-investment line from the buyer's own numbers, and name any discount with the full price it steps up to. The user sets the final figure.

## 7. Write the proposal and statement of work (Judge)

Use [SOW-TEMPLATE.md](SOW-TEMPLATE.md). The proposal is short and positive: their problem, what changes, proof, price, one next step. The statement of work states everything plainly: deliverables, what's included, limits, exclusions, client responsibilities with dates, assumptions, timeline, acceptance, payment, changes and support.

- Limits and exclusions belong in the statement of work, never in sales copy.
- Prices sit small, under the thing being sold, never the biggest element on the page.
- No claim the profile's proof can't back.
- The user's voice for the covering message.

## 8. Approve (Approve)

Show the user the price, the statement of work and the covering message. Nothing goes to the client until the user approves that exact version.

## 9. Changes after signing (Judge, then Approve)

A clear change line starts before signing: work back from the goal and the design spec, and state exactly what each deliverable is. Then, when a client asks for something during a project, decide whether it's in the statement of work.

- **In scope:** a defect (a deliverable not doing what the statement of work says) or one of the included small changes. Do it.
- **Out of scope:** as a rule of thumb, anything that adds a system, a deliverable or more than half a day. That includes adding or altering a trigger, outcome, screen, user group, connected system, agreed rule or approval step, extra revision rounds, extra meetings, or work caused by changes on the client's side. Price it as an add-on in a change note within two working days: what changes, the price, the effect on timeline and acceptance. Nothing starts until the client approves it in writing; an email reply counts.
- Ideas raised mid-project go on a parking list, unworked until quoted.
- If scope shrinks, the price comes down the same way.

## 10. Record (Record)

Proposal record with version, price, days and status. Opportunity stage moved to `proposal`. Each approved change note numbered on the proposal record. When the client decides, move the stage to `won` or `lost` and record the reason. Delivery and acceptance are tracked outside the sales stages.

## 11. Check before finishing

- The price clears the floor, and the effective day rate is stated to the user.
- The statement of work has an acceptance test, client responsibilities with dates, and who owns the work and its upkeep.
- The days fit capacity, or the user has been told they don't.
- Every claim in the proposal has proof in the profile.
- Nothing was sent.

## Output

- A proposal and statement of work, following [SOW-TEMPLATE.md](SOW-TEMPLATE.md), waiting for the user's approval.
- Records from [RECORDS.md](RECORDS.md): the proposal, and the opportunity moved to `proposal`, then to `won` or `lost` with a reason.
- After signing, change notes priced as add-ons.

## What it replaces

Pricing from scratch, writing the proposal and statement of work, and checking the price against the floor and the diary. Time saved: not yet measured.

## When it goes wrong

| Problem | What to do |
|---|---|
| Discovery left gaps | Stop at the confirm step and list what's missing |
| The buyer gave no numbers for the value line | Ask for them. Never invent them |
| The effective day rate is under the floor | Change the scope or the price, not the estimate |
| Committed work fills the months it would run | Offer a later start or a phase |
| No owner on the buyer's side | Make ownership a term of the proposal |

## Never

- send a proposal, price or change note without the user approving that exact version
- invent a client's budget, figures or return on investment
- absorb out-of-scope work silently
- promise a start date the capacity check can't support
- mark up third-party costs unless the profile says the business does

## About this skill

Made by Pedro Borrero at borre.ro. Part of BusinessBits, in the BoringBits repository, for one or two person UK businesses. Draft. Free to use under MIT, with credit. Provided as is, with no support.
