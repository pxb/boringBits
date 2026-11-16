# The business system

Skills, contracts and templates for running a one-person business with an AI assistant.

A business has functions a founder performs whether or not they have staff: finding work, doing it, getting paid, staying lawful, and deciding what to do next. This directory maps those functions onto roles, gives each one a skill that starts on a specific event, and binds them with rules so an assistant cannot invent a number, spend money, grant access or promise a date on its own authority.

## The test

Point an assistant at a founder's inbox, calendar, bank statements, invoices, repository and market. The business keeps running, and every claim that something worked can be read from the system where the work happened.

If a function cannot be checked, it does not belong here as a promise. It belongs here as a workflow with a verifier, or not at all.

## What is here

| File | What it covers |
|---|---|
| [01-business-breakdown.md](01-business-breakdown.md) | The founder's own definition of the business, which the rest of this directory has to match |
| [02-skill-map.md](02-skill-map.md) | 43 skills in 5 tracks under 26 roles, with what starts each one and how it is proved |
| [03-decisions.md](03-decisions.md) | Decisions already made, with the reason, so they are not reopened |
| [04-open-questions.md](04-open-questions.md) | What is known to be unproven |
| [05-review-brief.md](05-review-brief.md) | The brief for an independent review of this design |
| [06-conventions.md](06-conventions.md) | Rules that bind every skill: evidence, authority, state, settings, unknowns, failures |
| [templates](templates/prd.md) | The documents a build must produce: product requirements, architecture, design system |

## The five tracks

| Track | Purpose |
|---|---|
| Revenue | Demand, then sales, then the relationship after the sale |
| Deliver | Client work: won deal to accepted delivery, then support |
| Build | The software factory: requirements to shipped product, then upkeep |
| Company | Finance, billing and legal, so the entity stays solvent and lawful |
| Direction | Planning, decisions, market view, analysis |

Delivery is split in two because client work and building software fail in different ways and close differently. Academic symmetry is not a reason to merge them.

## State

- 43 skills mapped. Three are written here: [enquiry](../../skills/enquiry/SKILL.md), [market-position](../../skills/market-position/SKILL.md), [meeting-prep](../../skills/meeting-prep/SKILL.md).
- Six are partially covered by existing material. Twenty-six are named and unbuilt.
- The map is audited by [tools/skill_map.py](../../tools/skill_map.py): no two skills in a track may start on the same event, and every role must have a skill. The count in this directory is generated, not typed.

## How to use it

Start with the track that has money attached this month. Read the role, then the skill, then apply it against a real enquiry, invoice or build rather than a hypothetical one. Correct the skill when it is wrong; a skill nobody has used is a guess with formatting.

## Not included

- No installer, hooks, credentials or vendor configuration. These are documents an assistant reads.
- No private business facts. Settings such as rates, channels and response windows are the user's own values, supplied at the point of use.
