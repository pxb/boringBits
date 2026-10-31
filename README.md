# Boring bits

Practical ways to make AI useful in a business: reusable skills, playbooks, patterns, field notes and examples. Start with the decision or process, not the tool.

By Pedro Borrero, [borre.ro](https://borre.ro).

Source: https://github.com/pxb/boringBits. Native plugin adapters are not implemented; see [compatibility notes](docs/compatibility.md).

## Start here

| Need | Read and apply | Licence |
| --- | --- | --- |
| Turn an idea or existing requirements into a concise brief for review | [Project PRD](skills/project-prd/SKILL.md), with its [template](skills/project-prd/PRD-TEMPLATE.md) | MIT, with retained upstream notices |
| Decide what your AI should know and where it should get that knowledge | [Business context map](skills/business-context-map/SKILL.md) | CC-BY-4.0 |
| Separate fixed automation steps from AI judgement, checks and human approvals | [Workflow or agent](skills/workflow-or-agent/SKILL.md) | CC-BY-4.0 |

The two companion skills stand alone. Their associated articles are drafts, not published reading prerequisites. Original article identifiers remain in skill metadata only as provenance.

## Use with an assistant

Give your assistant access to this checkout, then ask it to read [AGENTS.md](AGENTS.md) and the selected skill before applying it to your task. For example:

> Read skills/project-prd/SKILL.md and its companion resources. Apply it to these notes. Interview me about material gaps, then return the brief for review. Do not execute the project.

If your assistant cannot read repository files, provide the selected skill as text or an attachment, together with its resources and licence notices. For Project PRD, keep all four files in its folder together. Check that the assistant has actually received them; a repository URL alone does not install or register a skill in a web or mobile chat.

This explicit read/apply mode needs file access and ordinary instruction-following. It does not require a particular agent vendor or browsing tool. When current public research would help but browsing is unavailable, state that limitation rather than inventing sources or plan limits. Never submit confidential business context to a public search.

**Native plugin adapters are not implemented.** Native skill discovery, installation and invocation are host-specific and untested here. See [compatibility and boundaries](docs/compatibility.md).

## What lives here

- `skills/`: canonical instructions and their resources; no duplicate vendor-specific bodies.
- `docs/`: useful supporting guidance, starting with compatibility.
- `tests/`: local publication gates, not native-host tests or CI receipts.

Playbooks, patterns, field notes and examples belong here when there is substantive, reviewed material to share. Empty category directories and draft articles are not included in this first cut.

## Check or contribute

Python 3.10+ and PyYAML are needed for validation only, not to read or use the skills. In your chosen Python environment:

```sh
python -m pip install -r requirements-test.txt
python -B -m unittest discover -s tests -v
```

See [contribution guidance](CONTRIBUTING.md). There is no installer, bootstrap hook, telemetry or automatic execution.

## Licensing

This repository is mixed-licence, not blanket MIT. New toolkit code and documentation, and Project PRD subject to its retained upstream notices, use MIT. The two existing companion skills retain CC-BY-4.0. See [LICENSE](LICENSE) for exact scope and [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md) for attribution, provenance and changes. Reusing a skill does not license the confidential business facts you supply to it.
