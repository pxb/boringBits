# Boring Bits

Boring Bits is a collection of practical tools for making AI useful in a business. It starts with skills: instructions you can give an AI assistant to help you think through a piece of work.

By Pedro Borrero, [borre.ro](https://borre.ro).

## Skills

| Skill | What it helps you do |
| --- | --- |
| [Project PRD](skills/project-prd/SKILL.md) | Turn an idea or rough requirements into a project brief. The assistant asks follow-up questions and returns the brief for your review. |
| [Business context map](skills/business-context-map/SKILL.md) | Decide what your AI needs to know about your business, where that information lives and where to get it. |
| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Separate fixed automation from AI judgement, checks and human approvals when planning a process. |
| [Business setup](skills/business-setup/SKILL.md) | Set up the sales skills for your business: where your records live, your offer and prices, who you sell to, how you write, and the basic UK registrations. |
| [Enquiry](skills/enquiry/SKILL.md) | Decide what to do with an inbound enquiry, record it once and draft a reply for you to send. |
| [Prospecting](skills/prospecting/SKILL.md) | Find and research companies worth contacting, check every contact, and draft outreach you send yourself. |
| [Proposal](skills/proposal/SKILL.md) | Price the work, write the proposal and statement of work, and handle changes once a project is signed. |
| [Pipeline](skills/pipeline/SKILL.md) | Review open deals each week: what to chase, what to close, and whether you have time to deliver. |

The five sales skills are for one or two person UK businesses that live on sales, such as consultancies and agencies. Start with Business setup. They share one set of [record definitions](shared/RECORDS.md), and each skill carries its own copy so it works on its own. They draft and record; you approve and send.

## How to use a skill

Choose a skill and ask Claude or another assistant to read it and its referenced resources. The assistant needs access to the repository files. If it cannot read them from GitHub, provide the skill and its resources as text or attachments.

For example:

> Read `skills/project-prd/SKILL.md` and its referenced resources in https://github.com/pxb/boringBits. Help me turn my notes into a project brief. Ask me about any important gaps, then give me the brief to review. Do not start building the project.

The skills guide a conversation; they do not install software or connect your systems. Native plugin installation is not available or tested yet. See the [compatibility notes](docs/compatibility.md) for details.

## Contributing

Suggestions and contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance and test commands.

## Licence

See [LICENSE](LICENSE) and [notices](THIRD-PARTY-NOTICES.md).
