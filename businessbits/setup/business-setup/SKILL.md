---
name: business-setup
description: Sets up the BusinessBits skills for one small UK business. Works out what this assistant can do, picks where sales records live, writes the business profile (offer, prices, buyers, proof, voice, capacity, research tools) and checks the basic UK registrations. Use the first time someone uses the enquiry, prospecting, proposal or pipeline skills, when there is no business profile yet, when they ask to set up, change or review their business details, when they are getting started with BusinessBits or BoringBits, when records move to a new CRM or store, when choosing research tools, or when they want drafts to sound like them (learning how they write from their sent emails).
license: MIT
compatibility: Any assistant that can read these files. Saving the profile needs either persistent files or a connected store such as a CRM, database or spreadsheet.
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.2"
  status: draft
---

# Business setup

Set up the sales skills for a one or two person UK business, usually a consultancy or an agency. The other skills read what this one writes, so get it right once and keep it short.

Steps are labelled: **Fetch** reads a fact exactly, **Judge** needs weighing, **Check** tests the result, **Approve** is the user's decision, **Record** writes it down.

## 1. Look for an existing profile (Fetch)

Look for `business/profile.md` in the working folder, or a profile record in the user's connected store. If one exists, this is an update: show it, ask what changed, and edit only those parts. Never overwrite a profile wholesale.

## 2. Find out what this assistant can do (Fetch, then Check)

Check, don't assume:

| Capability | How to check |
|---|---|
| Files that persist | Can you list and write files in a folder the user will open again next time? Chat apps usually can't; Claude Code, Cowork and similar desktop agents usually can |
| Connected stores | Which CRM, database, spreadsheet or notes tools are connected in this conversation? List them by what they are |
| Web search and browsing | Can you search the web and open a page? |
| Email and calendar | Can you read sent mail? Can you create drafts? |

Tell the user in two or three lines what you found. If something is unclear, ask one question rather than guess.

## 3. Choose where records live (Judge, then Approve)

Read [RECORDS.md](references/RECORDS.md). Recommend one store:

- **Files** when files persist and the user has no sales records elsewhere. This is the default.
- **Their existing CRM, database or spreadsheet** when they already keep sales records there, or when files don't persist. Map each record and field in RECORDS.md to their tables and fields, including their own deal stages to discovery, proposal, won and lost, and write the mapping into the profile. Fields with no home stay in the notes of the nearest record. Work with the CRM as it is set up; don't ask the user to change it to suit the skills.

Write the recommendation as its own line, naming the store and one reason, for example: "Records: files in `business/`, because files persist here and nothing else is connected." Listing what the assistant can do is not a recommendation; the line is required even when the answer seems obvious. The user decides. Never move existing records without their yes.

## 4. Build the profile from what already exists (Fetch, then Judge)

Copy [PROFILE-TEMPLATE.md](templates/PROFILE-TEMPLATE.md). Fill it from material the user already has before asking anything: their website, a recent proposal, a price list, their LinkedIn profile, past invoices. Quote the source next to each fact.

Then ask only for what is still missing, in short batches of three or four questions. Every question carries its own default, written on the same line, so the user can accept it with one word: "Days a week on client work? (default: 3)". Where there is no sensible default, such as the trading name or what they sell, the default is what you found in their material, or `unknown`. A list of defaults kept apart from the questions doesn't count. Good defaults:

| Question | Default |
|---|---|
| Days a week for client work | 3, the rest for selling, writing and admin |
| How fast to answer an enquiry | The same working day |
| Chasing after discovery | Chaser after 2 working days, a call the next working day, a second chaser 3 working days later, a call, a final email. Let it go after 3 chasers, 4 at most; calls with a voicemail count, the final email doesn't |
| Never traded to lower a price | The floor day rate and the acceptance test |
| Outreach order | Email, then LinkedIn, then a call only after a reply |
| New accounts to research | At least 5 a week per signal, worked back from the clients needed |
| Expected conversion, for planning | Their own guess for qualified inbound and for outbound, recorded as an assumption until outcomes replace it |
| Payment terms | Builds 50% on signing and 50% on acceptance; fixed sessions paid before delivery; 14 days |

Write `unknown` for anything the user can't answer yet. The other skills treat `unknown` as a gap to flag, not a value to guess.

## 5. Voice (Fetch, then Judge)

If the user already has a writing-style guide or skill built from their own writing, use it as the voice and record where it lives. Don't collect emails again.

Otherwise, ask for five to ten emails the user actually sent: a reply to an enquiry, a follow-up, a proposal cover note. Read them and write five to eight plain rules about how they write (sentence length, greeting, sign-off, words they use, words they never use). Quote short examples.

Never build the voice from text an assistant wrote. If the user has no sent emails to share, write `voice: not set` and draft plainly until they do.

Messages and reports are different registers. Messages follow the voice rules. Reports for the user (a research pack, a pipeline review) are data-forward: tables, the key numbers in bold, short headings.

## 6. Research tools (Fetch, then Approve)

The prospecting skill researches with this assistant's own web search and browsing first. Then list the kinds of tool that can help, and ask which the user already pays for or would consider:

- the official company register (Companies House in the UK, free)
- job boards, for hiring signals
- a contact finder that returns named people and email patterns
- an email verifier
- a company enrichment service

Record what they have. Don't recommend a vendor unless the user asks. Any paid tool gets a monthly budget in the profile, and skills stop at the budget.

## 7. UK registrations check (Fetch, then Record)

Ask, and record the answer. This is a check, not legal or tax advice; point to the official source for each.

| Item | Why it matters | Where to check |
|---|---|---|
| ICO data protection fee | Most businesses that hold personal data, including a prospect list or a CRM, must pay it. Exemptions are narrow | The ICO's fee self-assessment at ico.org.uk |
| VAT registration | Registration is required once taxable turnover passes the threshold (£90,000 from April 2024; check the current figure) | gov.uk VAT registration |
| Professional indemnity insurance | Many clients ask for it before signing; it covers claims about advice or work | Their broker |
| Public liability insurance | Needed for on-site work | Their broker |

If an item is missing or unknown, say so plainly in one line and move on. Don't block setup on it.

## 8. Save and confirm (Approve, then Record)

Show the finished profile. Save it only after the user says yes: to `business/profile.md` with files, or as a profile record in their store. Create the empty `business/records/` folders from RECORDS.md when using files.

Then tell the user what they can ask for now:

- "Here's an enquiry, what should I do?" (enquiry)
- "Find me ten companies worth contacting this week." (prospecting)
- "Write a proposal for this." (proposal)
- "Review my pipeline." (pipeline)

## 9. Check before finishing

- Every fact in the profile has a source or says "the user said".
- No guessed values. Gaps say `unknown`.
- The user was told which store you recommend, in one line with a reason.
- Every question asked had its default beside it.
- The record store is reachable, and a test record can be written and read back. Remove the test record afterwards.
- Nothing was sent, bought or connected.

## Output

- The business profile, following [PROFILE-TEMPLATE.md](templates/PROFILE-TEMPLATE.md), with a source for every fact. It goes to `business/profile.md` in the user's working folder, or a profile record in their store. Never into a shared or public repository.
- With files, the empty `business/records/` folders from [RECORDS.md](references/RECORDS.md).
- A short note to the user of what's set, what's `unknown` and what to try first.

## What it replaces

The owner explaining their offer, prices, buyers and rules again in every conversation. They write it down once, in a form every other skill reads. Time saved: not yet measured.

## When it goes wrong

| Problem | What to do |
|---|---|
| Files don't persist and no store is connected | Say so. Give the user the finished profile to keep and paste in next time |
| The user can't answer a question | Write `unknown` and move on |
| A profile already exists | Update the parts that changed, never the whole profile |
| The store can't be written to or read back | Stop before saving and say what failed |

## Never

- move, merge or delete existing records without the user's yes
- connect a new tool, start a trial or enter credentials
- put the user's private details into a public search
- give legal or tax advice beyond pointing to the official source

## About this skill

Made by Pedro Borrero at borre.ro. Part of BusinessBits, in the BoringBits repository, for one or two person UK businesses. Draft. Free to use under MIT, with credit. Provided as is, with no support.
