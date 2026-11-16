---
name: enquiry
description: "Reads an inbound enquiry, decides whether it is real, records it once, and sets one next step with a date. Use when a message arrives from a potential customer, a referral or a contact form, and you need to decide what happens to it rather than just reply."
license: MIT
compatibility: "Any assistant that can read these files and the user's own records. No software, accounts or integrations are installed by this skill."
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "0.1"
  status: draft
  track: revenue
  role: sales-inbound
  mechanism: workflow and skill
  owns: the enquiry record
---

# Enquiry

An inbound message is the cheapest attention a business gets, and the easiest to lose. The job is not to answer quickly. It is to decide, once, whether this is real, and what happens next.

## 1. Get what you need before judging anything

Ask the user for these, and stop if they are missing. An assumed answer here is a wrong answer that looks like a right one.

- what a good customer looks like, and what is out of scope
- which channels actually reach the business, and which are ignored
- the response time the business wants to be measured against
- where existing client, proposal and invoice records live, so an enquiry from a current client is recognised as one

## 2. Capture it once

| Field | What goes in it |
|---|---|
| Who | Person and organisation, as they gave them |
| Where from | Channel, and the person or post that sent them |
| What they asked | Their own words, not a summary |
| Real | Person with a decision, a describable problem, and a reason now |
| Fit | Fit, partial or out of scope against the ideal customer |
| Value band | The band the enquiry suggests. Never a figure the user did not give |
| Timing | When they need it, and where that came from |
| Owner | One named person |
| Next step | One action and one date. Never empty |
| State | new, replied, qualifying, qualified, declined or dormant |

A second message in an existing thread updates the existing record. It does not create a new one.

## 3. Decide whether it is real

Three tests, in order:

1. Is there a person who can decide, or only a form?
2. Can they describe the problem in their own words?
3. Is there a reason it is being asked now?

Fail one and it may still be real; say which failed. Fail all three and it is noise: record it, decline it, and write the reason. A decline with a reason is how the ideal customer definition improves.

## 4. Set one next step

Every open enquiry has one action and one date. Not a status, not a note. If the right next step needs a person to decide something, the next step is that decision, with a name against it.

## 5. Draft the reply, do not send it

Answer what was actually asked. Ask only what is needed for the next decision. Promise nothing: no price, no date, no scope. Put the draft in front of the user with the record, and let them release it.

## 6. Check before you finish

- Every inbound message has exactly one record. Count both sides and compare.
- No record shows progress without a next step and a date.
- Anything unknown is marked unknown, not filled in.
- Every reply that goes out is in the outbound log, with the approval that released it.
- Existing clients are not treated as new.

## 7. Never

- send a reply without the user approving that exact message
- invent a budget, a deadline or a fit score to fill a field
- promise a price, a date or a scope
- mark an enquiry lost without a recorded reason
- create a second record for a thread, a forwarded copy or a duplicate arrival

## About this skill

Made by Pedro Borrero at borre.ro, an AI and Revenue Operations practice. Part of a set of business skills for a one-person company. Draft: written to be used and corrected, not published as a finished method.

Free to use and share under MIT, with credit to borre.ro. Provided as is, with no support.
