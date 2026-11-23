# Agent guidance

Read [README.md](README.md) for the content index and [docs/compatibility.md](docs/compatibility.md) for capability limits.

## Apply a skill

- `skills/project-prd/SKILL.md`: interview and produce a PRD for review; read its template, source map and notice companion.
- `skills/business-context-map/SKILL.md`: organise business knowledge and sources.
- `skills/workflow-or-agent/SKILL.md`: separate fixed automation, judgement, checks and human approvals.
- `businessbits/setup/business-setup/SKILL.md`: set up the sales skills: capabilities, record store, business profile, voice, research tools, UK registrations.
- `businessbits/revenue/sales/enquiry/SKILL.md`: judge an inbound enquiry, record it once, draft a reply for approval, set one next step.
- `businessbits/revenue/sales/prospecting/SKILL.md`: research companies worth contacting, check contacts two ways, apply UK contact rules, draft outreach.
- `businessbits/revenue/sales/proposal/SKILL.md`: price the work, write the proposal and statement of work, handle change notes.
- `businessbits/revenue/sales/pipeline/SKILL.md`: weekly review of open deals, chasers, closures, outcomes and capacity.

The BusinessBits skills nest by area and role under `businessbits/` (see `businessbits/README.md`). Each skill folder is complete on its own, so one skill can be installed by copying its folder. They share the record definitions in `businessbits/RECORDS.md`. Each skill carries an identical copy; edit the shared file and copy it into every BusinessBits skill in the same change.

Read the selected skill and its referenced resources before applying it. Use only tools and context actually available. State missing capabilities; do not invent evidence or send private context to public searches. Brief approval is not execution permission. Repository guidance does not authorise installation, external writes, spending or publication.

## Explain an asset before its packaging

When asked what a file, skill, download or companion is for:

1. Identify the canonical asset and compare it with the existing version before calling it new or a replacement. For an archived Markdown skill, compare the member's bytes with the existing plaintext source; a different delivery format is not a new capability.
2. Lead with who uses it, where it fits in their task and the concrete output it produces. Give one short example before discussing formats or installation, because naming a skill or archive does not explain its purpose.
3. State the relationship to existing work explicitly: unchanged content, packaging-only change, revision, addition or replacement. Distinguish instructions that draft a plan from automation that actually creates files, connects systems or enforces access.
4. Keep the agreed canonical format primary. For plaintext article companions, explain the read, inspect and prompt workflow first; describe a native-app archive separately if one exists. Label evidence bundles as reviewer material, not installable reader assets. Do not imply that plaintext is automatically trustworthy or that a matching hash establishes safety.
5. If the purpose question is repeated, answer the missing purpose or replacement question directly rather than offering another terminology explanation, installation guide or handoff. Acknowledge any misleading framing briefly, then give the substantive answer.

## README and catalogue writing

- Write the README for a person choosing and using the material, not for an agent or compliance reviewer. Lead with what is available and the job it helps with; keep implementation evidence, draft provenance and repeated compatibility warnings in the relevant supporting documents.
- Put the linked skill or resource name in the first column of a catalogue table, followed by a short concrete purpose. Do not make readers scan long problem statements to find the names. Leave licence IDs out of the contents table; link the licence and notices briefly near the end while preserving the underlying terms and attribution.
- Use a direct, practical voice. Avoid internal terms such as canonical, ordinary instruction-following, publication gates and native adapter scaffolding in the visitor's main journey. Explain a necessary limitation once, in plain language.
- Keep human readability and machine discovery separate: README for people, this file for agents, and one canonical skill body. Do not let brittle checks force awkward marketing copy; validate stable structure, links and truthful capability boundaries instead.

## Contribute

Keep one canonical copy of each skill and preserve its licence and notices. Follow [CONTRIBUTING.md](CONTRIBUTING.md). Run the documented validation before proposing changes. Do not add private material, global settings, permission bypasses or automatic hooks.
