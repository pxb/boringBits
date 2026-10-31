# Compatibility and boundaries

## Two different modes

| Mode | What it means | Current evidence |
| --- | --- | --- |
| Explicit read/apply | Give an assistant repository/file access, ask it to read a selected skill and its resources, then use those instructions for your task | Portable Markdown and local structural validation only; no claim that every model follows every instruction reliably |
| Host-native discovery/install | A host discovers packaged skills, exposes them for selection and invokes them according to its own contract | OpenAI marketplace/package manifests provided; portable schema and isolated Codex catalogue discovery checked. ChatGPT desktop installation and live skill invocation not tested |

The canonical skill folders follow the [Agent Skills specification](https://agentskills.io/specification): YAML frontmatter with `name` and `description`, Markdown instructions and optional resources. [AGENTS.md](https://agents.md/) is a separate open convention for repository navigation and contribution guidance, not a plugin manifest. A plain CLAUDE.md pointer is intended to direct readers to the shared guidance, not invoke undocumented import syntax.

This broader repository layout is a local organisation convention. It is not a universal schema for Claude, ChatGPT, Codex or other hosts. Opening a GitHub URL in Claude web, an iOS app or a ChatGPT Plus conversation does not automatically register skills. Check the host's current documentation, available plan and actual file access before claiming native support.

## OpenAI delivery package

The package follows OpenAI's current [plugin packaging contract](https://developers.openai.com/plugins/build/plugins) and the [Agent Plugins manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json):

- Root `plugin.json` identifies the `boring-bits` package, version `0.1.0`. Its `extensions.com.openai` object supplies display metadata, not tools or permissions.
- `.agents/plugins/marketplace.json` exposes that single package as **Boring Bits**. Its local source `./` resolves from the selected repository root, not from the manifest's directory.
- Root `skills/` supplies all three canonical skills without copies or symlinks. Project PRD's template, source map and notice companion stay beside it; root licence and notices travel with the package.
- The optional manifest licence field is omitted: [LICENSE](../LICENSE) and [notices](../THIRD-PARTY-NOTICES.md) retain the per-file MIT and CC-BY-4.0 scopes. Version `0.1.0` identifies this first delivery wrapper, not a tagged release.
- Installation policy is `AVAILABLE`, not automatic installation. The documented `ON_INSTALL` authentication policy does not create a sign-in requirement: this skills-only package has no connected services, apps or credentials.

For review, use source `https://github.com/pxb/boringBits`, Git ref `feat/openai-marketplace`, and leave sparse paths blank. The full source is small; a sparse selection can exclude the marketplace, skills or legal resources. After a separately approved merge, use the then-current default branch (currently `feat/initial-toolkit`), or leave the ref blank if the client supports the repository default.

Workspace-admin GitHub import is a different flow: repository-root Path is blank and branch may be default or explicit, subject to workspace-admin access. A desktop marketplace import does not establish workspace publication, universal directory listing, account-wide sync or ChatGPT iOS/Plus availability. This change performs none of those actions.

No Claude Code adapter, custom installer, MCP service, hook or global configuration is shipped. Never duplicate canonical skill bodies merely to create vendor variants.

## Capabilities and permission

- Skills contain instructions, not executable payloads. Tools and credentials come from the host and the user's permissions, never from this repository.
- Reading a skill does not grant browsing, business-system access or authority to make changes. Use action descriptions rather than assuming a particular vendor tool name exists.
- Where research or current vendor-plan checking is requested but unavailable, identify that gap. Do not invent citations or silently substitute stale knowledge.
- Use only authorised context. Do not upload private material to public searches. A planning skill does not authorise sending, installing, spending, publishing or deployment.
- Project PRD requires its template and two companion provenance/notice files. Its interview, eight-heading structure and approval boundaries are unchanged.

## What validation proves

The offline test suite checks skill count, YAML parsing and selected Agent Skills constraints, PRD resource fingerprints, metadata, mixed licensing, draft status, the README index, shared-guidance pointer, local inline Markdown/backtick resource references, a finite public file allowlist and known secret/private-operation patterns. Delivery gates check the chosen manifest/marketplace shape, root-relative discovery, required resources, containment and absence of runtime/config additions, including negative fixtures. They are repository-specific checks, not an official marketplace JSON Schema.

Separately, the portable manifest was validated against the official draft-2020-12 schema with jsonschema. That schema does not validate OpenAI extension contents or marketplace semantics. Codex CLI `0.163.0`, with isolated HOME and CODEX_HOME and no account login, accepted the marketplace and listed `boring-bits@boring-bits` at the repository root as available, uninstalled and disabled. Its read-only `plugin/read` API discovered all three namespaced skills at their canonical paths, with no apps, MCP servers or hooks. This proves catalogue/package and skill discovery in that CLI, not a ChatGPT desktop installation or live model behaviour.

The link check supports the simple inline links and backtick file references used here. It is not a full Markdown parser, link availability checker or exhaustive secret detector. It deliberately does not fetch article URLs. Human review remains required before publication.

No CI run, ChatGPT desktop installation, live agent session or mobile compatibility pilot is established by these checks. No real user plugin was installed, enabled or registered; disposable CLI catalogue configuration was confined to an isolated test home.
