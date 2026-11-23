# Boring Bits

Boring Bits is a collection of practical tools for making AI useful in a business. It holds two kinds of skill, which are instructions you give an AI assistant: general skills for thinking through a piece of work, and BusinessBits, for running the business day to day.

By Pedro Borrero, [borre.ro](https://borre.ro).

## Skills

| Skill | What it helps you do |
| --- | --- |
| [Project PRD](skills/project-prd/SKILL.md) | Turn an idea or rough requirements into a project brief. The assistant asks follow-up questions and returns the brief for your review. |
| [Business context map](skills/business-context-map/SKILL.md) | Decide what your AI needs to know about your business, where that information lives and where to get it. |
| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Separate fixed automation from AI judgement, checks and human approvals when planning a process. |

## BusinessBits

[BusinessBits](businessbits/README.md) is the business partner in this repo: skills that run the everyday work of a one or two person UK business, grouped by business area and role. It starts with Revenue: setting up your business profile, handling enquiries, prospecting, proposals and the weekly pipeline review. They draft and record; you approve and send.

## How to use a skill

Choose a skill and ask Claude or another assistant to read it and its referenced resources. The assistant needs access to the repository files. If it cannot read them from GitHub, provide the skill and its resources as text or attachments.

For example:

> Read `skills/project-prd/SKILL.md` and its referenced resources in https://github.com/pxb/boringBits. Help me turn my notes into a project brief. Ask me about any important gaps, then give me the brief to review. Do not start building the project.

The skills guide a conversation; they do not install software or connect your systems. Native plugin installation is not available or tested yet. See the [compatibility notes](docs/compatibility.md) for details.

## Contributing

Suggestions and contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance and test commands.

## Licence

See [LICENSE](LICENSE) and [notices](THIRD-PARTY-NOTICES.md).
