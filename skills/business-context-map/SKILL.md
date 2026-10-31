---
name: business-context-map
description: "Maps where a business's knowledge lives and decides how AI should reach each part, at three scales: standing notes loaded up front for one person, shared folders and skills for a team, and a shared, permissioned source for the whole company. Use when setting up Claude or ChatGPT projects, writing standing instructions, organising files or skills for a team, or scoping a company knowledge base."
license: CC-BY-4.0
metadata:
  author: Pedro Borrero, borre.ro
  support: none
  version: "1.0"
  source: https://borre.ro/newsletter/context-is-king
---

# Business context map

Help the user decide what their AI should know, where that knowledge lives, and how the AI should get to it. More text is not better: give the AI the smallest set of material that does the job, and let it fetch the rest when it needs it.

## 1. Inventory

Ask what the business relies on, and where each thing lives today:
- who you sell to and why they buy
- what you sell and what it costs
- how you write and present
- decisions already made
- customer and deal history (usually the CRM and inboxes)
- documents: proposals, contracts, case studies, policies
- what only certain people may see (pay, HR, board, client confidential)

For each item note: where it lives, who keeps it up to date, how often it changes, and who may see it.

## 2. Place each item at a scale

| Scale | Put here | How the AI gets it |
|---|---|---|
| You | Short, stable facts one person uses every day | A standing notes file loaded at the start of every chat (project instructions, or a CLAUDE.md-style file) |
| Your team | Shared ways of working: templates, price lists, tone, checklists, repeatable procedures | Shared folders the AI reads when relevant, shared projects, and skills (folders with a SKILL.md) that load only when a task needs them |
| Your company | Large, fast-changing or sensitive material: CRM records, email history, documents | A shared source the AI queries: exact queries for records, search with citations for documents, access that follows existing permissions |

Rules:
- If it changes weekly or needs permissions, it does not belong in anyone's personal notes.
- Records questions ("how many", "which deals", "who hasn't replied") need an exact query, not a document search.
- Every answer drawn from company material should cite its source so a person can check it.
- One owner per file. A file nobody owns goes stale.

## 3. Write the standing notes (the "You" scale)

Draft one page, most important first, with the date at the top:
1. The business in five lines: what you sell, to whom, price range, where.
2. Customers: who buys, why, what worries them.
3. How you write: three rules and one example.
4. Decisions already made, so the AI stops re-suggesting them.
5. What it must never do: invent figures, name clients, send anything.
6. Where to look for more: the folders or sources it may read, by name.

Add one line: "If you don't know, say so. Don't invent figures."

## 4. Folder layout (the "Team" scale)

Propose a small layout the AI can navigate by name, for example:

```
business/
  NOTES.md            the standing notes
  customers/          ideal customer, objections, case studies
  pricing/            current price list, dated
  writing/            tone rules, approved examples
  decisions/          one file per decision, dated
  skills/             repeatable procedures as skills
```

Clear folder and file names matter: the AI uses them to decide what to open.

## 5. Output

Give the user:
1. The inventory table with a scale for each item.
2. A draft of the standing notes.
3. The folder layout.
4. What should move to a shared company source, and why (size, change rate or permissions).
5. Three checks to run in a month: are the notes still true, did two people get the same answer to the same question, and what would be lost if one person left.

Check the current features and plan limits of the user's AI tools against their own help pages before recommending one. They change often.

## About this skill

Made by Pedro Borrero at borre.ro, an AI and Revenue Operations practice. Companion to the draft article "Context is king". Article publication pending. The source URL in metadata records provenance, not a published article.

Free to use and share under CC BY 4.0, with credit to borre.ro. Provided as is, with no support.
