# Attribution and provenance

Read [LICENSE](LICENSE) for the mixed-licence scope. The skills are by Pedro Borrero, borre.ro; upstream PRD adaptations are attributed separately below.

## Project PRD

The four-file prepared Project PRD pack is reproduced without changes under [skills/project-prd](skills/project-prd/SKILL.md). Its [source map](skills/project-prd/SOURCE-REUSE.md) identifies adaptations from GitHub spec-kit, Fission-AI OpenSpec and obra superpowers, including immutable source pins. The full retained MIT texts are in [skills/project-prd/THIRD-PARTY-NOTICES.md](skills/project-prd/THIRD-PARTY-NOTICES.md).

Keep these four files together when redistributing. Original contributions use MIT as scoped by the root licence; upstream attribution and notices remain intact. No older guides, validation receipts or generated artifacts are part of this distribution.

## Business context map and Workflow or agent

Original author: **Pedro Borrero, borre.ro**. Original version: **1.0**. Licence retained: **CC-BY-4.0**, https://creativecommons.org/licenses/by/4.0/ (full [legal code](https://creativecommons.org/licenses/by/4.0/legalcode)). Provided as is, with no support. Attribution does not imply endorsement of adaptations.

Provenance: borre.ro source revision `6cf33adb05b3543452e3df349483e30971d89cdf`, specifically:

- Business context map: source-relative path "src/content/newsletter/skills/business-context-map/SKILL.md".
- Workflow or agent: source-relative path "src/content/newsletter/skills/workflow-or-agent/SKILL.md".

These identify authoring sources, not files bundled here or a public source-repository access promise. The original author, version, support and article identifiers remain in each skill's metadata. Associated articles are drafts; source URLs are provenance identifiers, not advertised published articles.

Changes in this distribution:

- Business context map: quoted the YAML description so the literal `scales: standing` parses as part of a string. No semantic change to the description.
- Both companions: replaced the About paragraph's live-article wording with an explicit draft/publication-pending statement. Removed the duplicate body URL; original source URL remains in metadata.
- No changes to either skill's procedural instructions. Custom metadata was already nested under `metadata`; no field migration was needed.

The skills are distributed independently of article publication. No full articles or website assets are included.

## Consulted, not adapted: toolkit organisation

The separation of canonical skills from host-specific integration follows a general architectural pattern. [obra/superpowers porting guidance at revision 2ce8aa15d05bd57213e6f746f953aafb7ded7a8b](https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/docs/porting-to-a-new-harness.md) was consulted for that distinction. No installer, hook, bootstrap, persona, tool mapping or policy text was copied into this toolkit. This architectural consultation is separate from the actual PRD adaptations, whose MIT notices are retained above. No AGPL benchmark material was copied or adapted.

Format references: [Agent Skills specification](https://agentskills.io/specification) for skill frontmatter and resources; [AGENTS.md](https://agents.md/) for open repository guidance. Neither makes the whole repository layout a universal native installation schema.
