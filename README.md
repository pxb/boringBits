# Boring Bits

Boring Bits is a collection of practical tools for making AI useful in a business. It starts with skills: instructions you can give an AI assistant to help you think through a piece of work.

By Pedro Borrero, [borre.ro](https://borre.ro).

## Skills

| Skill | What it helps you do |
| --- | --- |
| [Project PRD](skills/project-prd/SKILL.md) | Turn an idea or rough requirements into a project brief. The assistant asks follow-up questions and returns the brief for your review. |
| [Business context map](skills/business-context-map/SKILL.md) | Decide what your AI needs to know about your business, where that information lives and where to get it. |
| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Separate fixed automation from AI judgement, checks and human approvals when planning a process. |
| [Enquiry](skills/enquiry/SKILL.md) | Read an inbound enquiry, decide whether it is real, record it once and set the next step with a date. |
| [Market position](skills/market-position/SKILL.md) | Decide who the business is for, what it replaces and what proves each claim, then drop the claims nothing supports. |
| [Meeting prep](skills/meeting-prep/SKILL.md) | Build a one-page brief before a call: who is coming, what happened before, what changes the proposal and what must not be promised. |

## How to use a skill

Choose a skill and ask Claude or another assistant to read it and its referenced resources. The assistant needs access to the repository files. If it cannot read them from GitHub, provide the skill and its resources as text or attachments.

For example:

> Read `skills/project-prd/SKILL.md` and its referenced resources in https://github.com/pxb/boringBits. Help me turn my notes into a project brief. Ask me about any important gaps, then give me the brief to review. Do not start building the project.

The three sales skills above are part of a wider design: the business functions a one-person company runs on, mapped by role and by the event that starts each one. Start at [the business system](docs/business-system/README.md). Most of that map is unbuilt and says so.

The skills guide a conversation; they do not install software or connect your systems. Native plugin installation is not available or tested yet. See the [compatibility notes](docs/compatibility.md) for details.

## Contributing

Suggestions and contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance and test commands.

## Licence

See [LICENSE](LICENSE) and [notices](THIRD-PARTY-NOTICES.md).
