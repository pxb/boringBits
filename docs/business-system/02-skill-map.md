# The business, as roles and skills

43 skills in 5 tracks, under 26 roles. Three are written in this repository; the rest are named and unbuilt, and the state is marked on every row.

Delivery is split in two, because client work and building software fail in different ways, get fixed by different people and close differently. A delivered engagement ends with access removed and a closure record. A product release repeats forever.

## How to read it

A role states the objective and the scope, so a reader can place themselves before reading a single skill. A skill states the event that starts it, the object it owns, what it produces, and how its work is proved.

| Track | Purpose |
|---|---|
| **Revenue** | Demand, then sales, then the relationship after the sale. |
| **Deliver** | Client work: won deal to accepted delivery, then support. |
| **Build** | The software factory: requirements to shipped product, then upkeep. |
| **Company** | Finance, billing and legal, so the entity stays solvent and lawful. |
| **Direction** | Planning, decisions, market view and analysis. |

## The routing rule

No two skills in a track share a trigger event. If two could fire on the same event, the assistant guesses, and the guess is the bug. That rule is enforced by `tools/skill_map.py`, which fails on a shared trigger, a role with no skill, or a skill on a role that does not exist.

## Coverage

43 skills: 17 written or partially written, 26 named and unbuilt.

### Revenue

*Demand, then sales, then the relationship after the sale.*  
11 skills across 6 roles: 3 written, 3 partial, 5 not built.

| Role | Objective | Scope |
|---|---|---|
| **Marketing lead** | Create demand that arrives already interested | Positioning, proof, content, campaigns, public surfaces |
| **Sales, inbound** | Turn interest into a qualified conversation | Enquiries, triage, fit, first response |
| **Sales, outbound** | Create conversations that were not going to happen | Target lists, research, first contact, sequences |
| **Sales, closing** | Turn a conversation into a signed commitment | Meetings, proposals, pricing, negotiation, pipeline truth |
| **Account management** | Grow and keep what was won | Onboarding, account plans, renewals, expansion |
| **Customer success** | Keep the account healthy enough to stay | Health signals, risk, intervention before renewal |

| Skill | Role | Starts when | Produces | Proved by | State |
|---|---|---|---|---|---|
| `market-position` | Marketing lead | Positioning is unclear, or a market is being entered | A stated position: who it is for, what it replaces, the proof | every claim backed by a demonstrable proof point | new |
| `content` | Marketing lead | A piece or a campaign is planned | Published assets, live and verified, with their measurement plan | published revision fetched back, campaign result read from channel | new |
| `enquiry` | Sales, inbound | An inbound message arrives | Enquiry record with real-or-not, fit, owner and next step | event identities reconciled to records | have |
| `prospect-research` | Sales, outbound | A named prospect is chosen for approach | Sourced brief and an approach decision with its basis | sampled claims opened and scored | have |
| `outbound` | Sales, outbound | A message to a named person is due | One message per purpose, sent, proved and stopped correctly | send log reconciled to loop state at send time | partial |
| `meeting-prep` | Sales, closing | A call is booked | A brief for that call: history, open items, questions, risks | every claim traceable to a record | new |
| `proposal` | Sales, closing | A scope needs a price, or terms change | A priced, margin-checked proposal and the terms accepted | price recomputed, acceptance read at the agreed level | have |
| `pipeline` | Sales, closing | A review point is reached, or a deal is lost | Open, stuck, expected and lost, with reasons | source query, unknowns shown as unknown | partial |
| `onboarding` | Account management | A deal is won | A started engagement: access, contacts, dates, acceptance criteria, payment terms | access read from granting systems, terms linked to the proposal | partial |
| `account` | Account management | A review point per account, or a renewal date approaches | An account plan, a health judgement, and a renewal or at-risk decision | health signals read from usage and payment data | new |
| `recovery-plan` | Customer success | An account shows risk or has complained | A named intervention with an owner and a review date | intervention recorded and its outcome re-checked | new |

### Deliver

*Client work: won deal to accepted delivery, then support.*  
7 skills across 5 roles: 2 written, 1 partial, 4 not built.

| Role | Objective | Scope |
|---|---|---|
| **Engagement lead** | Take a won deal to an accepted delivery | Scope, plan, progress, client communication, acceptance |
| **Business analyst** | Turn what the client said into something buildable | Functional requirements, clarifications, sign-off |
| **QA and UAT** | Prove the work does what was agreed | Test coverage, client acceptance testing, sign-off |
| **Support** | Keep what was delivered working | Breakages, fixes, updates, support window |
| **Delivery ops** | Make delivery repeatable | Access settlement, documentation, remedies, closure |

| Skill | Role | Starts when | Produces | Proved by | State |
|---|---|---|---|---|---|
| `requirements` | Business analyst | A deal is won or a change is requested | Functional requirements, clarified and signed, at one revision | traceability from the client's words to each requirement | have |
| `engagement` | Engagement lead | An engagement starts, or a progress review is due | A plan that fits capacity, and its current state with client-facing progress | committed dates versus calendar, state read from the task system | partial |
| `uat` | QA and UAT | Delivery is complete and the client must accept | A UAT record: cases, results, defects, sign-off or refusal | results from the client's own run, acceptance evidence recorded | new |
| `handover` | Delivery ops | An engagement ends | Settled access, accepted delivery, recorded closure, feedback | grant records read per item | have |
| `support` | Support | A breakage, question or change request arrives after delivery | A triaged, fixed and recorded outcome inside the support window | fix verified at the deployed revision, clock read from delivery date | new |
| `remedy` | Delivery ops | Something failed, is disputed or was refused | A contained, remedied, recorded exception with an accountable owner | case state and remedy recorded | new |
| `knowledge` | Delivery ops | Work must be repeatable by someone else | How the work is done, written where it can be found | a second person completes the task from the record | new |

### Build

*The software factory: requirements to shipped product, then upkeep.*  
8 skills across 8 roles: 1 written, 0 partial, 7 not built.

| Role | Objective | Scope |
|---|---|---|
| **Product manager** | Decide what the product is and is not | PRD, priorities, acceptance criteria |
| **Design** | Make it usable and consistent | Design system, patterns, component rules |
| **Architect** | Decide how it is built and why | Architecture, boundaries, technical decisions, ADRs |
| **Tech lead** | Turn a PRD into dispatched work | Chunking, sequencing, delegation, orchestration |
| **Engineer** | Make the change | Implementation, migrations, fixes |
| **Reviewer and QA** | Refuse to ship what is not proved | Code review, automated tests, evidence at revision |
| **Release engineer** | Ship it and be able to undo it | Release, notes, runbook, rollback |
| **Maintenance** | Keep the product alive after release | Dependencies, breakages, incident fixes, upkeep |

| Skill | Role | Starts when | Produces | Proved by | State |
|---|---|---|---|---|---|
| `prd` | Product manager | Requirements are agreed | A product requirements document with priorities and acceptance criteria | every requirement traced to a criterion, none invented | new |
| `design-system` | Design | A build starts, or a surface needs a component the system does not have | The rules a build must conform to, plus the template that makes conformance checkable | the rendered surface compared rule by rule, every off-system value listed | new |
| `architecture` | Architect | A build starts, or a structural decision must be made | Architecture and its decisions, each with rationale and consequences | each decision has a dated record and a named alternative rejected | new |
| `orchestration` | Tech lead | A PRD is approved | Chunked work, dispatched to agents or people, sequenced and tracked | every chunk maps to a criterion, every dispatch has a result | new |
| `implementation` | Engineer | A chunk is dispatched | A change on a branch that follows the PRD, architecture and design system, with its tests | build and tests pass at the branch revision, criteria and rules cited per change | new |
| `verification` | Reviewer and QA | A change is ready to check | A verdict with evidence at the revision: review, tests, conformance to PRD, architecture and design system | results read from the check systems, conformance checked against each rule, failures block | have |
| `release` | Release engineer | A change is approved | A shipped revision with notes, runbook and a rollback path | deployed revision identifier read back from the environment | new |
| `maintenance` | Maintenance | A dependency, breakage or incident appears after release | An updated, deployed and verified product, or a documented decision not to act | post-change health read from monitoring, not from intent | new |

### Company

*Finance, billing and legal, so the entity stays solvent and lawful.*  
11 skills across 4 roles: 3 written, 2 partial, 6 not built.

| Role | Objective | Scope |
|---|---|---|
| **Bookkeeper** | Keep the record accurate and reconciled | Cash, expenses, statements, period close |
| **Finance lead** | Get paid, pay on time, stay solvent | Invoicing, billing, payables, tax, budget, unit cost |
| **Legal and compliance** | Keep the entity lawful and covered | Contracts, terms, insurance, obligations, filings |
| **Ops and security** | Keep the means of production safe | Access, assets, subscriptions, backups, risk, incidents |

| Skill | Role | Starts when | Produces | Proved by | State |
|---|---|---|---|---|---|
| `cash` | Bookkeeper | A statement lands, or a commitment changes | Money available today, after pending commitments, with every cost evidenced | bank and commitments reconciled, receipts matched | new |
| `invoicing` | Finance lead | A billable event occurs, or a payment state changes | Invoices per the allocation policy, and their payment state including overdue | registry queried, payment read from bank or provider | have |
| `payables` | Finance lead | A liability needs a decision before it is due | Pay, defer or challenge, per liability, including payroll and tax | decision per liability, statement line per payment | have |
| `tax` | Finance lead | A filing period opens | Computed tax, set aside, and filed, with the receipt | filing receipt from the authority | partial |
| `period-close` | Bookkeeper | A period ends and statements exist | A reconciled period with the difference stated | statement matched to ledger in both directions | have |
| `budget` | Finance lead | A planning point is reached | Planned spend and runway against actual | actuals drawn from reconciled figures | new |
| `cost-model` | Finance lead | A price is being set or reviewed | What delivery costs per unit of work, with published inputs | arithmetic recomputable from the inputs | new |
| `contracts` | Legal and compliance | An agreement is needed or changes | Agreements in force, with dates, terms and the signed revision stored | signed revision stored and dated | new |
| `obligations` | Legal and compliance | A dated obligation exists | Every obligation with an owner, a date and a completion test | register reviewed on cadence, not remembered | partial |
| `estate` | Ops and security | A system, grant, asset or subscription changes | Systems, access, assets, subscriptions and restores, current | grants, charges and restores read from source | new |
| `risk` | Ops and security | A review point, or an incident | Known risks with owners and dates, and incidents contained and recorded | each risk dated, each incident time-lined | new |

### Direction

*Planning, decisions, market view and analysis.*  
6 skills across 3 roles: 2 written, 0 partial, 4 not built.

| Role | Objective | Scope |
|---|---|---|
| **CEO** | Choose what the business does and stops | Planning, priorities, opportunities, decisions, review |
| **CFO** | Say what the numbers mean | Margin, runway, concentration, trend, forecast read |
| **Analyst** | Watch the market so decisions are not guesses | Demand, competitors, pricing, change signals |

| Skill | Role | Starts when | Produces | Proved by | State |
|---|---|---|---|---|---|
| `review` | CEO | The configured cadence arrives | The decisions that need a person, at the cadence set | set difference against open decisions | have |
| `plan` | CEO | A planning point is reached | Where the business is going, what it will not do, and the targets that measure it | written, dated, referenced in later decisions | new |
| `business-analysis` | CFO | A period closes or a decision needs numbers | What the numbers mean: margin, runway, concentration, trend | every figure recomputable from closed accounts | new |
| `market-analysis` | Analyst | A decision needs outside context | Sourced, dated signals about demand, competitors, pricing and change | each signal sourced, dated and either acted on or dismissed | new |
| `opportunity` | CEO | A new service, market, client type or extra capacity is proposed | A decision with the evidence, the bet and the downside stated | evidence gathered before the decision is recorded | new |
| `decision-record` | CEO | Any decision is made | The decision, its basis, its owner and what happened | outcome evidence from the system where the outcome occurred | have |

## What is a rule, not a skill

Retention, recovery and scheduling are policies and workflows. Approval, authority, evidence, state, exceptions, obligations and notification are contracts shared by every skill, written once in `06-conventions.md`. A skill that restates a contract is how two skills start disagreeing.

## Decisions behind this map

- Roles come before skills, because a title carries an objective and a scope.
- Merge two candidates when they share a trigger event, an output object and an owner of state. Keep them apart when the output is a different artefact with its own lifecycle.
- The design system is about developing with a system, not curating one: the rules live in the skill, the documents live in templates, and conformance is checked when a change is reviewed.
- Client support and product maintenance stay separate: different owners, different clocks.
