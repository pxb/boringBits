# Review brief

For an independent review of this design. Give the block below to a reviewer with the repository checked out on the branch `feat/business-system`. Do not paste summaries of the design instead of the files: the point is to review what is in the branch.

The review is returned as a report, not as a commit. This repository publishes reviewed content only, and a reviewer who edits while judging produces a patch instead of a verdict.

---

You are reviewing a design for a host-neutral set of business skills: the functions a one-person business performs, written so any AI assistant can carry them, with rules that stop it inventing numbers, spending money, granting access or committing dates on its own authority.

Be blunt. A polite review wastes the only thing that matters here: finding the structural fault before the remaining forty bodies are written and inherit it.

## What the work is trying to become

One founder, no team. The assistant is pointed at an inbox, a calendar, bank statements, invoices, a code repository and the market. The business keeps running: enquiries answered, work built and accepted, invoices paid, obligations filed, decisions recorded with their basis. Every claim of success is readable from the system where the work happened.

## Read, in this order

1. [01-business-breakdown.md](01-business-breakdown.md) — the founder's own definition, which cannot be overruled.
2. [README.md](README.md) — what the system claims to do and what it excludes.
3. [02-skill-map.md](02-skill-map.md) — 43 skills, 5 tracks, 26 roles.
4. [03-decisions.md](03-decisions.md) — decisions already made. Do not reopen one unless it is wrong on its merits; if it is, name it and say why.
5. [04-open-questions.md](04-open-questions.md) — what is known to be unproven.
6. [06-conventions.md](06-conventions.md) — the rules binding every skill.
7. The three written skills: [enquiry](../../skills/enquiry/SKILL.md), [market-position](../../skills/market-position/SKILL.md), [meeting-prep](../../skills/meeting-prep/SKILL.md).
8. The [templates](templates/prd.md), and [the audit](../../tools/skill_map.py), which enforces the routing rule in code.
9. Run the test suite and report what it proves and what it does not.

## Judge these ten things, one to ten each

1. **Goal fit.** Does this let a founder run a business, or describe one? Name every function that produces a document rather than a decision or an outcome.
2. **Completeness.** What does a founder do in their first month that has no home here? Give the situation, then the missing function. Ignore anything already in the open questions unless you have a better answer than it does.
3. **Granularity and routing.** Two skills must never start on the same event. Find every pair a reader could plausibly confuse, name them, and say whether to merge, split or rename. This is the fault the author most expects you to find.
4. **Mechanism honesty.** Each function is a skill (judgement), a workflow (deterministic, unwatched), a product (state and arithmetic), a person, or a mix. Flag every function claimed for an assistant that can only be verified deterministically, and every workflow that quietly needs judgement.
5. **State and ownership.** Every object has exactly one owner. Find any object two skills could write.
6. **Evidence.** For each written skill, is the proof readable from a named system, or is it self-assessment? "The assistant confirms it" is not proof. Say which checks would fail in practice, and what would replace them.
7. **Contracts.** Are the shared rules in the right place? Name a missing one, and any rule sitting inside a skill that will therefore drift.
8. **Portability.** Would these files behave the same on Claude, ChatGPT and a local model? Name anything that assumes a particular host, file layout or invocation model.
9. **Safety.** Money, access, legal positions and commitments to third parties. Where could this cause harm, and is the approval gate binding or a sentence someone routes around?
10. **Publishability.** A stranger with a small business reads this and gets value. Where do they stop reading, and what makes them give up?

Score is the mean of the ten. The gate is 8. Below 8, say what single change would move the score most.

## Rules for the review

- Cite file and line for every defect. No defect without a location.
- Do not edit files, commit, open a pull request or create a repository. Return the review as your report.
- Do not praise. If something is fine, one line at most.
- Separate wrong from missing from unproven. They need different fixes.
- Anything that cannot be checked from the repository goes under unverified, not under defects.
- Judge structure before prose. A perfect skill body under the wrong track is worth nothing.
- Do not assume any particular vendor's skill format.

## Output

1. A score table: criterion, score, one line why, and the total against the gate of 8.
2. The single most important fault, in one paragraph.
3. Defects: file and line, what is wrong, whether it is wrong, missing or unproven, and the fix.
4. Confusable skills: the pairs, and the resolution you recommend.
5. Missing business functions: the situation, the function, where it belongs.
6. Anything wrong at the structure level: the five tracks, the 26 roles, the skill-to-role mapping.
7. Unverified claims the repository makes.
8. The one change that would move the score most, and why.
