---
name: workflow-or-agent
description: Plans an automation step by step, deciding which steps should be fixed workflow steps, which need AI judgement, where checks and human approval go, and whether it should run as a personal AI task or on a workflow platform. Use when someone plans to automate a business process, asks whether to use an AI agent, or wants to review a supplier's automation proposal.
license: CC-BY-4.0
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "1.0"
  source: https://borre.ro/newsletter/the-case-for-boring-automation
---

# Workflow or agent

Help the user design an automation that is fixed where it matters and uses AI only where judgement is needed. Work from their real process, not a generic one.

## 1. Get the process

Ask for, or work out from what they've shared:
- what starts it (a time, an email, a form, a CRM change)
- each step, in order, as a person does it today
- where the facts come from (which system, file or website)
- what leaves the business at the end (an email, an invoice, a CRM update)
- how often it runs and roughly how long it takes by hand

If a step is vague ("sort out the lead"), ask what the person actually looks at and decides.

## 2. Label every step

Give each step exactly one label:

| Label | Use when | Runs as |
|---|---|---|
| Fetch | reading a fact that exists somewhere: a record, a price, a register, a file | a fixed step, no AI |
| Judge | the step needs reading, weighing or writing: fit, tone, what a call meant | an AI step, given only what it needs |
| Check | testing an AI step's output: right shape, quote really in the source, number in range, required fields present | a fixed step after every Judge |
| Approve | anything that leaves the business or can't be undone | a person |
| Record | logging what ran, what it cost and what it produced | a fixed step |

Rules:
- Never use AI to fetch a fact a fixed step can read exactly.
- Every Judge step is followed by a Check step. If a check fails, the item goes to a person, not back round the loop forever.
- Anything sent to a customer, paid, deleted or published gets an Approve step unless the user explicitly decides otherwise.
- Unexpected cases (missing data, a new kind of request) route to a person or to an agent step, and the route is written down.

## 3. Decide where it runs

A personal AI task (a scheduled task in Claude or ChatGPT) is fine when all of these hold:
- one person owns it and reads every result
- it runs on a time schedule, or on an event the tool supports
- a missed or failed run costs little
- the credentials involved belong to that person

Use a workflow platform (n8n, Make, Zapier, Power Automate or similar) when any of these hold:
- it must run for the business when that person is away, or after they leave
- it is triggered by an event from a system the personal tool can't watch (a CRM stage change, a webhook, a form)
- it touches several systems with shared business credentials
- failures must alert someone, and every run must leave a record
- other people need to see, change or approve it

If the user's AI has written code or a script for a step, suggest saving it as a skill (a folder with a SKILL.md) or moving it into the workflow platform, so it isn't lost when the chat ends.

Check the current plans and limits of the tools named against their own help pages before relying on them. They change often.

## 4. Output

Give the user:
1. A table: step, label, what it reads, what it produces, who or what does it.
2. Where it should run, and the one reason that decided it.
3. The checks, each written as a pass or fail test.
4. The approvals: who, and what they see before approving.
5. Risks: what happens if a source is down, a check fails, or the owner is away.

Keep it plain. No jargon the user didn't use first.

## 5. Reviewing a supplier's proposal

Ask the supplier:
- Which steps use AI, which don't, and why?
- What does one run cost, and where is that recorded?
- When the AI gets something wrong, what catches it before a customer sees it?
- Where does each fact come from, and can I see the source?
- What needs a person's approval?
- Whose accounts and credentials does it run on, and what happens if that person leaves?

If most answers are "the agent handles it", ask again.

## About this skill

Made by Pedro Borrero at borre.ro, an AI and Revenue Operations practice. Companion to the draft article "The case for boring automation". Article publication pending. The source URL in metadata records provenance, not a published article.

Free to use and share under CC BY 4.0, with credit to borre.ro. Provided as is, with no support.
