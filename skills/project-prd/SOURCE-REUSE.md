# Source reuse and provenance

Maintainer source map for this provisional pack, not a client prerequisite or installed skill. The template, guide and skill adapt the material below. Distribute adaptations with the complete [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md), in the same package or as a second attachment, rather than embedding notices in the template. This is a prudent retention policy for documented adaptations, not a claim that generic PRD ideas are copyrighted or that a substantiality threshold is definitely met. The notices concern adapted material, not business facts in a project brief. Paths, licences and commit IDs were checked against upstream repository trees and pinned files. Earlier proof concerns an old draft and is not evidence of the revised pack's behaviour.

## Upstream material actually adapted

| Upstream source | Immutable source and licence | Adaptation in this pack |
| --- | --- | --- |
| GitHub spec-kit | [`templates/spec-template.md`](https://github.com/github/spec-kit/blob/7370e592f3cd9c06e5b698983957e227c75b30e2/templates/spec-template.md); [MIT licence](https://github.com/github/spec-kit/blob/7370e592f3cd9c06e5b698983957e227c75b30e2/LICENSE) | Prioritised scope, a checkable smallest useful outcome and stable requirement IDs adapt its prioritised, independently testable journey and numbered requirement patterns. Observable success can be qualitative; baselines and targets need not be invented. Optional Given/When/Then scenarios also draw on this source. |
| Fission-AI OpenSpec | [`schemas/spec-driven/templates/spec.md`](https://github.com/Fission-AI/OpenSpec/blob/27c0515724decc633818c735ee596481eec78a8b/schemas/spec-driven/templates/spec.md); [MIT licence](https://github.com/Fission-AI/OpenSpec/blob/27c0515724decc633818c735ee596481eec78a8b/LICENSE) | Optional scenarios under requirements adapt its requirement/scenario structure and WHEN/THEN observation pattern, with Given available for context. The default is plain-language acceptance bullets. This is a product brief, not an OpenSpec delta. |
| obra superpowers | [`skills/brainstorming/SKILL.md`](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/brainstorming/SKILL.md); [MIT licence](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/LICENSE) | The kickoff adapts reading supplied context before questioning, focused questions and playback for correction. The brief adapts attention to current state, why now, non-goals, constraints and human review. |

## Independent additions and exclusions

The lean headings, human-readable approval metadata, material uncertainty labelling, bounded alternatives check, unknown-friendly readiness, approval boundary and optional supporting links are pack-specific. Scenario formatting draws on both spec-kit and OpenSpec. Excluded: spec-kit's feature branches, prescribed story counts and invented illustrative metrics; OpenSpec's added-requirement delta workflow; superpowers' mandatory design-and-build gate, implementation workflow and visual companion. Brief approval does not authorise implementation. No upstream code is executed or installed.

`myclaude` product-requirements is an AGPL-3.0 benchmark only, and `deanpeters` Product-Manager-Skills is a CC-BY-NC-SA benchmark only. Neither supplied wording or adaptation to this pack; no claim of a licence review beyond the stated benchmark classifications is made here.

## Guidance reviewed, not wording copied

These sources informed the review judgement, not a vendor PRD standard or copied wording:

- [Anthropic agent skills best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [OpenAI Build Skills](https://learn.chatgpt.com/docs/build-skills)
- [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices)
- [Devpost PRD skill, pinned raw source](https://raw.githubusercontent.com/challengepost/learn-ai-basics/a0f065781873e8a7ed9a9a705a8dafa6a0810439/skills/3-prd/SKILL.md)
- [Product on Purpose PRD skill, pinned raw source](https://raw.githubusercontent.com/product-on-purpose/pm-skills/85bd34523a0d0ed98baaca26a5ba3266dd014487/skills/deliver-prd/SKILL.md)
