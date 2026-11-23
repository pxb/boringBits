---
name: prospecting
description: Finds and researches companies worth contacting for a small UK consultancy or agency, then drafts a short outreach sequence for the user to send. Starts from the clients the business already wins, checks every contact two ways, applies UK contact rules and suppression, and sends nothing itself. Use when the user asks for new leads, a prospect list, a weekly research pack, outreach to a named company, or more pipeline.
license: MIT
compatibility: Works best with web search and browsing. Recording needs persistent files or a connected store set up by business-setup. Paid research tools are optional.
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.1"
  status: draft
---

# Prospecting

Find a small number of companies that look like the clients the business already wins, prove each one is real and reachable, and give the user a research pack and drafts they can send themselves. Ten good accounts beat fifty thin ones.

Steps are labelled: **Fetch** reads a fact exactly, **Judge** needs weighing, **Check** tests the result, **Approve** is the user's decision, **Record** writes it down.

## 1. Read the profile and records (Fetch)

Read `business/profile.md` or the profile record in the user's store: buyers, proof, voice, channels, research tools and budget. Read [RECORDS.md](RECORDS.md). If there's no profile, offer business-setup first.

Load the suppression list, current clients and every organisation with an open enquiry or opportunity. Nothing on those lists goes into a pack.

## 2. Start from where the business already wins (Judge)

Before searching, write down in five lines what the best existing clients have in common: the situation they were in, who bought, what they bought first, what they bought next, and how they arrived. Use won opportunities and the profile's proof. If there are fewer than three wins, use the profile's buyer description and say the target is a hypothesis.

Rank on what the evidence rewards:
- **Room to grow beats first-deal size.** Multi-site businesses, groups and businesses that could buy more than one thing rank higher.
- **The low-commitment first sale.** Prefer accounts where the smallest, easiest first piece of work fits.
- **A matching proof.** An account that resembles a published case gets the stronger approach.

Engagement isn't fit. An owner who's interested and keen to talk is still the wrong account if the service or the price doesn't fit them.

## 2a. Work out how many accounts a week (Judge)

Work backwards from the run rate the business needs, rather than picking a number:

1. New clients needed in the period, from the profile's revenue goal and typical deal value.
2. Leads needed = new clients ÷ expected conversion. Use the profile's conversion assumptions, kept separate for qualified inbound leads and outbound prospects. Until the business has its own outcomes, these are assumptions: say so in the pack.
3. Accounts a week = outbound leads needed ÷ weeks in the period.

Example with invented numbers: two new clients a quarter from outbound, at an assumed 2% conversion, needs 100 accounts a quarter, about 8 a week.

Default floor, unless the profile says otherwise: at least 5 accounts a week per signal. To grow volume, add a signal. Then balance the total against delivery and everything else the business has to do that week, and tell the user if the formula asks for more than that leaves room for.

## 3. Find candidates (Fetch)

Use the cheapest route first: this assistant's own web search, the company register, company websites, then any paid tools in the profile, within budget. Record the cost of each paid call.

Use a signal: a dated, public reason this company might need help now. Examples: hiring for a role the work would support (a business advertising a job has published a budget for that need), a new site or product, an investment, a leadership change. For more accounts, add a signal rather than widening the area.

Industry codes on the register are self-reported. Treat them as a hint, never a rule.

## 4. Research each account (Fetch, then Check)

Follow [RESEARCH-METHOD.md](RESEARCH-METHOD.md) for every account. In short:

1. Confirm the legal entity on the company register, and resolve groups: if the parent or a sister company is a client or in the pipeline, suppress it.
2. Confirm the domain resolves and is the real email domain.
3. Find a **named person** who owns the problem. A generic inbox doesn't count. No named person, no account.
4. Check the contact two ways: the email is deliverable, **and** the person still holds the role (register appointments, the company's own team page, recent news). Deliverable alone is `verify-before-sending`.
5. Find one dated, sourced reason to contact them now. If there's no event, say the need is standing.
6. Match the closest proof from the profile.

Every fact carries a source link and one status: **Verified** (primary source), **Likely** (strong indirect), **Unverified**, **Conflicting** or **Not found**. Don't trust a search summary for dates: models surface old reports as current. Open the source.

## 5. Check the UK contact rules (Check)

Read [UK-CONTACT-RULES.md](UK-CONTACT-RULES.md). For each contact, set `basis` and the channel allowed. Sole traders and ordinary partnerships need consent or a soft opt-in before marketing email. A contact with no lawful basis for a channel doesn't get that channel.

## 6. Draft the sequence (Judge, then Check)

Default, unless the profile says otherwise: four touches over about three weeks, email first, LinkedIn second, a call only after a reply.

- Touch 1 opens with their real signal, in one or two lines, and asks one question about the cost of the problem.
- Touch 2 links the matching case study with its headline result.
- Touch 3 gives something useful on its own: a tip, a short check, a relevant fact with its source.
- Touch 4 asks permission to close the loop.

Rules: the user's voice from the profile. One call to action per touch. Never put the internal angle or research notes in a message. Never tell them facts about their own business they'd find intrusive. No claims the profile's proof can't back. The first message carries the privacy notice line when one is required.

Check each draft: every fact in it appears in the research with a source.

## 7. Deliver the pack (Approve)

Give the user a research pack, data-forward: one table of accounts (name, why now, contact and check status, proof match, channel allowed), then one short section per account with the facts, sources and the four drafts. No method notes or tool names in the pack.

The user picks which accounts to work, and sends every message. Nothing here sends, connects or writes to an external system.

## 8. Record (Record)

Create or update organisation and contact records for accounts the user accepts, with relationship `prospect`. An account that replies or engages becomes a `lead`. When the user reports what happened, append to `outcomes.md` and update `suppression.md` (90 days after contact; permanent for `not-interested`, `do-not-contact` and new clients). Outcomes are what later scoring learns from, so ask for them at the next run.

## 9. Check before finishing

- Every account has a named person, a resolving domain and a two-way contact check, or is labelled `verify-before-sending`.
- No account is suppressed, a client, or in the pipeline, including through a parent company.
- Every fact has a source and a status. No `not checked` entries: research it, or write `Not found`.
- Paid tool use is within the profile's budget and recorded.
- Nothing was sent.

## Never

- send, schedule or queue a message
- guess an email address and present it as checked, or guess a LinkedIn profile URL
- contact a sole trader or partnership by marketing email without consent or a soft opt-in
- use a paid tool beyond the profile's budget, or start a trial
- put internal notes, scores or angles in a message

## About this skill

Made by Pedro Borrero at borre.ro, from the research method behind two working prospecting loops. Part of the BoringBits sales skills for one or two person UK businesses. Draft. Free to use under MIT, with credit. Provided as is, with no support.
