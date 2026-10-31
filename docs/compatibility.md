# Compatibility and boundaries

## Two different modes

| Mode | What it means | Current evidence |
| --- | --- | --- |
| Explicit read/apply | Give an assistant repository/file access, ask it to read a selected skill and its resources, then use those instructions for your task | Portable Markdown and local structural validation only; no claim that every model follows every instruction reliably |
| Host-native discovery/install | A host discovers installed skills, exposes them for selection and invokes them according to its own contract | Not implemented or tested in this repository |

The canonical skill folders follow the [Agent Skills specification](https://agentskills.io/specification): YAML frontmatter with `name` and `description`, Markdown instructions and optional resources. [AGENTS.md](https://agents.md/) is a separate open convention for repository navigation and contribution guidance, not a plugin manifest. A plain CLAUDE.md pointer is intended to direct readers to the shared guidance, not invoke undocumented import syntax.

This broader repository layout is a local organisation convention. It is not a universal schema for Claude, ChatGPT, Codex or other hosts. Opening a GitHub URL in Claude web, an iOS app or a ChatGPT Plus conversation does not automatically register skills. Check the host's current documentation, available plan and actual file access before claiming native support.

No Claude Code plugin, OpenAI plugin adapter, marketplace manifest, custom installer, hook or global configuration is shipped. Adding an adapter later requires an official current contract and a real host/schema check. Never duplicate the canonical skill bodies merely to create vendor variants.

## Capabilities and permission

- Skills contain instructions, not executable payloads. Tools and credentials come from the host and the user's permissions, never from this repository.
- Reading a skill does not grant browsing, business-system access or authority to make changes. Use action descriptions rather than assuming a particular vendor tool name exists.
- Where research or current vendor-plan checking is requested but unavailable, identify that gap. Do not invent citations or silently substitute stale knowledge.
- Use only authorised context. Do not upload private material to public searches. A planning skill does not authorise sending, installing, spending, publishing or deployment.
- Project PRD requires its template and two companion provenance/notice files. Its interview, eight-heading structure and approval boundaries are unchanged.

## What local validation proves

The local test suite checks skill count, YAML parsing and selected Agent Skills constraints, PRD resource fingerprints, metadata, mixed licensing, draft status, the README index, shared-guidance pointer, local inline Markdown/backtick resource references, a public file allowlist and known secret/private-operation patterns. It includes negative schema and path fixtures and reconstructs the original invalid YAML description.

The link check supports the simple inline links and backtick file references used here. It is not a full Markdown parser, link availability checker or exhaustive secret detector. It deliberately does not fetch article URLs. Human review remains required before publication.

No CI run, native installation, live agent session or runtime-host compatibility pilot is established by these local checks. No skill was installed or registered as part of preparing this repository.
