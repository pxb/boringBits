# Boring Bits

Boring Bits is a collection of practical tools for making AI useful in a business. It starts with skills: instructions you can give an AI assistant to help you think through a piece of work.

By Pedro Borrero, [borre.ro](https://borre.ro).

## Skills

| Skill | What it helps you do |
| --- | --- |
| [Project PRD](skills/project-prd/SKILL.md) | Turn an idea or rough requirements into a project brief. The assistant asks follow-up questions and returns the brief for your review. |
| [Business context map](skills/business-context-map/SKILL.md) | Decide what your AI needs to know about your business, where that information lives and where to get it. |
| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Separate fixed automation from AI judgement, checks and human approvals when planning a process. |

## How to use a skill

Choose a skill and ask Claude or another assistant to read it and its referenced resources. The assistant needs access to the repository files. If it cannot read them from GitHub, provide the skill and its resources as text or attachments.

For example:

> Read `skills/project-prd/SKILL.md` and its referenced resources in https://github.com/pxb/boringBits. Help me turn my notes into a project brief. Ask me about any important gaps, then give me the brief to review. Do not start building the project.

The skills guide a conversation; they do not install software or connect your systems. See the [compatibility notes](docs/compatibility.md) for details.

## OpenAI marketplace import

This review branch adds a package for OpenAI's repo marketplace importer. In **Add plugin marketplace**, use:

- Source: `https://github.com/pxb/boringBits`
- Git ref: `feat/openai-marketplace`
- Sparse paths: leave blank

Choose **Boring Bits** to find all three skills in one package. For example, ask Project PRD to turn your notes into a brief for review, not start building.

The package has passed schema and isolated Codex discovery checks. ChatGPT desktop installation was user-reported on 31 October 2026. Screenshot-reviewed first invocation showed **Boring Bits > Project PRD**, its template and the first interview question. This was not independently reproduced; a full real-project pilot remains untested.

iPhone-only native installation through this GitHub marketplace route is not established. Desktop installation does not establish mobile availability or account-wide sync. This is not a public directory listing; see the [compatibility notes](docs/compatibility.md) for evidence and limits.

## Contributing

Suggestions and contributions are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance and test commands.

## Licence

See [LICENSE](LICENSE) and [notices](THIRD-PARTY-NOTICES.md).
