# Decisions

Each row was decided, with a reason. Reopen one only if it is wrong on its merits.

| Date | Decision | Reason | Consequence |
|---|---|---|---|
| 2026-11-16 | Standalone and host-neutral, not derived from one assistant's skill format | A system built by reading one vendor's skills inherits that vendor's gaps and cannot travel | Skill bodies carry no host syntax; any assistant that reads files can apply them |
| 2026-11-16 | Work top-down: business area, then role, then skill | Filling gaps against an existing library shrinks the design to what already exists | The map was built from the four areas upward |
| 2026-11-16 | Four areas, five tracks | Client delivery and product building fail differently, close differently and need different owners | Delivery split into Deliver and Build |
| 2026-11-16 | Roles before skills | A traditional title carries an objective and a scope in one line | 26 roles, each with a stated objective |
| 2026-11-16 | Merge rule: same starting event, same output object, same owner of state | Two skills starting on one event force a guess, and the guess is the bug | 68 candidate functions became 43 skills |
| 2026-11-16 | The routing rule is enforced by code, not documented | A documented rule is a rule nobody runs | The audit fails on a shared trigger, an orphan role or an orphan skill |
| 2026-11-16 | Three mechanisms, never interchangeable | A skill cannot do arithmetic on state, and a workflow cannot judge | Each skill states its mechanism; deterministic steps belong in a workflow |
| 2026-11-16 | Account recovery and delivery remedy stay separate | One rescues a relationship, one rescues a delivery, and the owner differs | Two skills, two starting events |
| 2026-11-16 | Client support and product maintenance stay separate | Different owners, different clocks, different evidence | Two skills |
| 2026-11-16 | The design system skill is about building with a system | The artefact is not the point; conformance is | The skill holds the rules, [templates](templates/design-system.md) holds the documents, review checks conformance |
| 2026-11-16 | Settings, never constants | An assumed rate or retention period is a wrong answer that looks like a right one | A skill that cannot read a setting stops and says which one |
| 2026-11-16 | This work lands on a branch of this repository | A new repository created without review is a public artefact nobody agreed to | Branch reviewed before it reaches the default branch |
