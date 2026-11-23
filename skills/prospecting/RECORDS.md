# Business records

The sales skills read and write the same records. This file defines them. Every skill carries an identical copy, so each one works when installed alone. The canonical copy is `shared/RECORDS.md` in the BoringBits repository.

## Where records live

The business setup skill picks the store and writes the choice into the profile, under **Records**. Read the profile before writing anything.

| Store | Use when | How records are kept |
|---|---|---|
| Files (the default) | The assistant can read and write files that persist between conversations | One folder, `business/`, in the user's working folder. Layout below |
| A connected CRM, database or spreadsheet | Files don't persist (most chat apps), or the user already keeps sales records somewhere | The profile maps each record and field below to the user's own tables and fields. Use the connector's own tools |

If the profile names a store you can't reach in this conversation, say so and stop. Don't fall back to another store without the user's yes, or records split across two places.

When a CRM is the store, the CRM is the record. Work with it: use its own stages and fields through the profile's mapping, and never keep a second pipeline in files or notes alongside it.

## File layout

```text
business/
  profile.md                       written by business setup
  records/
    organisations/<org-slug>.md
    contacts/<person-slug>.md
    enquiries/<yyyy-mm-dd>-<org-slug>.md
    opportunities/<org-slug>-<short-name>.md
    proposals/<opportunity-id>-v<n>.md
    activities/<yyyy-mm-dd>-<org-slug>-<type>.md
    outcomes.md                    one line per outcome, newest last
    suppression.md                 who not to contact, and until when
  drafts/                          messages waiting for the user's approval
```

Each record file starts with YAML frontmatter holding the fields below, then free notes. Slugs are lower case with hyphens. The record id is its file name without `.md`.

## Rules for every record

- **One record per real thing.** Before creating one, search for it by name, email domain and company number. Update the existing record instead of creating a duplicate.
- **Unknown is a value.** Write `unknown`. Never fill a field with a guess.
- **Sources travel with facts.** A fact from outside the conversation carries its source (a link or "the user said") and the date it was checked.
- **Dates are ISO** (`2026-11-16`). Money is a number plus a currency code (`4500 GBP`).
- **Nothing is deleted.** Close records with a status and a reason.

## The records

### organisation

| Field | Meaning |
|---|---|
| name | Trading name |
| legal_name | Registered name, if known |
| company_number | Registry number, if a registered company |
| legal_form | `limited`, `llp`, `plc`, `sole-trader`, `partnership`, `charity`, `public-body` or `unknown`. Decides which UK contact rules apply |
| domain | The real email domain, checked |
| sector | In plain words |
| size | Staff band, with source |
| parent | Parent organisation id, if part of a group |
| relationship | `prospect`, `lead`, `client`, `former-client`, `partner` or `none`. A prospect is an organisation the business chose to approach that hasn't engaged. It becomes a lead when it engages: an enquiry, a reply or a referral. Keep the two apart |

### contact

| Field | Meaning |
|---|---|
| name | Full name |
| organisation | Organisation id |
| role | Job title, with source and date checked |
| email | Address, if known |
| email_check | `deliverable-and-current`, `verify-before-sending` or `none`. Deliverable means the mailbox exists; current means the person still holds the role |
| linkedin | A profile URL found and matched, or `none`. Never a guessed URL |
| basis | The lawful basis for contacting them: `existing-client`, `enquired`, `consented`, `soft-opt-in`, `legitimate-interests-b2b` or `none` |
| notice_given | Date the privacy notice was given, or `no` |

### enquiry

| Field | Meaning |
|---|---|
| received | Date and channel |
| from | Contact id and organisation id |
| words | What they asked, in their own words |
| source | How they found the business |
| fit | `fit`, `partial` or `out-of-scope`, with the reason |
| status | `new`, `replied`, `discovery-booked`, `qualified`, `declined` or `dormant` |
| next_step | One action |
| next_date | One date |
| opportunity | Opportunity id, once qualified |

### opportunity

| Field | Meaning |
|---|---|
| organisation | Organisation id |
| contacts | Contact ids, with the decision maker marked |
| problem | The buyer's problem in their words |
| owner | The person at the buyer who owns the work, or `unknown`. An unknown owner is settled in the proposal's terms |
| approval_route | Who signs, and how |
| source | Enquiry id, prospecting batch, referral or partner |
| stage | `discovery`, `proposal`, `won` or `lost`. Scoping happens inside discovery. Delivery, acceptance and support are tracked outside the sales stages. With a CRM, use its own stage names through the profile's mapping |
| value | Expected value, or `unknown` |
| days | Estimated delivery days, and what the estimate is based on |
| start | Earliest start the buyer wants |
| next_step | One action |
| next_date | One date |
| close_reason | Required when the stage is `lost`: for example `no-response`, `no-fit`, `price`, `timing`, `chose-another` |

### proposal

| Field | Meaning |
|---|---|
| opportunity | Opportunity id |
| version | 1, 2, 3 |
| sent | Date sent, or `draft` |
| price | Price and basis (`fixed`, `day-rate` or `retainer`) |
| days | Delivery days the price assumes |
| acceptance_test | How both sides will know it is done |
| status | `draft`, `sent`, `accepted`, `declined` or `expired` |
| changes | Numbered change notes after signing |

### activity

| Field | Meaning |
|---|---|
| date | When |
| type | `email`, `call`, `meeting`, `linkedin`, `letter` or `note` |
| direction | `in` or `out` |
| with | Contact id and organisation id |
| summary | What happened, in two lines |
| approved_by | For anything sent out: who approved that exact message |

### outcomes.md

One line per outcome, appended, never edited:

`date | organisation id | channel | outcome | note`

Outcomes: `no-reply`, `replied`, `meeting-booked`, `not-interested`, `do-not-contact`, `proposal-sent`, `won`, `lost`. A lost line carries the close reason in its note.

### suppression.md

One line per organisation or contact not to approach:

`organisation or contact id | reason | until`

`until` is a date, or `permanent` for `do-not-contact`, `not-interested` and current clients. Any organisation contacted in the last 90 days is suppressed from new outreach until 90 days have passed, unless the user says otherwise.
