"""Local publication gates. Run from repo root: python -B -m unittest discover -s tests -v."""
from pathlib import Path
import ast
import hashlib
import json
import re
import shutil
import tempfile
import unittest
from urllib.parse import unquote, urlsplit

import yaml  # Required: no reduced-parser fallback.

FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}


def frontmatter(text):
    """Require delimited YAML; SafeLoader rejects executable YAML tags."""
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError("Missing YAML frontmatter delimiters")
    end = lines.index("---", 1)
    data = yaml.safe_load("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise ValueError("Frontmatter must be a mapping")
    return data

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {"project-prd", "business-context-map", "workflow-or-agent"}


class RepositoryTests(unittest.TestCase):
    def assert_skill_schema(self, text, folder):
        data = frontmatter(text)
        self.assertLessEqual(set(data), FIELDS)
        self.assertLessEqual({"name", "description"}, set(data))
        name = data["name"]
        self.assertIsInstance(name, str)
        self.assertRegex(name, r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
        self.assertLessEqual(len(name), 64)
        self.assertEqual(name, folder)
        description = data["description"]
        self.assertIsInstance(description, str)
        self.assertTrue(description.strip())
        self.assertLessEqual(len(description), 1024)
        if "compatibility" in data:
            self.assertIsInstance(data["compatibility"], str)
            self.assertTrue(data["compatibility"].strip())
            self.assertLessEqual(len(data["compatibility"]), 500)
        if "metadata" in data:
            self.assertIsInstance(data["metadata"], dict)
            for key, value in data["metadata"].items():
                self.assertIsInstance(key, str)
                self.assertIsInstance(value, str)
        for field in ("license", "allowed-tools"):
            if field in data:
                self.assertIsInstance(data[field], str)
        self.assertTrue(text.split("---", 2)[2].strip())

    def test_agent_skills_schema(self):
        for name in sorted(SKILLS):
            with self.subTest(skill=name):
                self.assert_skill_schema((ROOT / "skills" / name / "SKILL.md").read_text(), name)

    def test_original_unquoted_yaml_is_rejected(self):
        # Reconstruct the exact original malformed header, not a made-up colon case.
        text = (ROOT / "skills/business-context-map/SKILL.md").read_text()
        match = re.search(r'^description: "(.*)"$', text, re.M)
        self.assertIsNotNone(match)
        original = text[:match.start()] + "description: " + match[1] + text[match.end():]
        with self.assertRaises(yaml.scanner.ScannerError):
            frontmatter(original)
        self.assertEqual(frontmatter(text)["description"], match[1])

    def test_schema_rejects_invalid_contracts(self):
        valid = {"name": "project-prd", "description": "Write a brief."}
        changes = [
            {"name": "Project-prd"}, {"name": "project--prd"},
            {"name": "-project-prd"}, {"name": "other-folder"},
            {"name": "a" * 65}, {"description": ""},
            {"description": "a" * 1025}, {"description": ["not a string"]},
            {"author": "custom top-level field"},
            {"metadata": {"version": 1.0}}, {"metadata": ["not a mapping"]},
            {"compatibility": "a" * 501}, {"allowed-tools": ["not a string"]},
        ]
        for change in changes:
            with self.subTest(change=change):
                text = "---\n" + yaml.safe_dump(valid | change) + "---\nBody\n"
                with self.assertRaises(AssertionError):
                    self.assert_skill_schema(text, "project-prd")
        for text in ["No header", "---\n- not a mapping\n---\nBody"]:
            with self.assertRaises(ValueError):
                frontmatter(text)
        with self.assertRaises(yaml.constructor.ConstructorError):
            frontmatter("---\nname: !!python/object:object {}\n---\nBody")

    def test_prd_four_files_are_unchanged(self):
        expected = {
            "SKILL.md": "fe4ed7b5242d2485b13966a432a1e7eb9798da6ca3725ab45f91bff90ac1cb62",
            "PRD-TEMPLATE.md": "8f1f6336c1ad315eed34de9ca9e8b771b3049ba5cf14cfe98eae14f89936494e",
            "THIRD-PARTY-NOTICES.md": "b98e32a1ad7bc85fb4e008450ba5ea2c3ff8377f6c16aca22efaa020d248735b",
            "SOURCE-REUSE.md": "d1ad45f516cba937ffcb1cdee0fe70bada1b2e522c6a69065f0a84164f4d72b2",
        }
        for name, digest in expected.items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((ROOT / "skills/project-prd" / name).read_bytes()).hexdigest(), digest)

    def test_companion_metadata_and_draft_status(self):
        articles = {"business-context-map": "context-is-king", "workflow-or-agent": "the-case-for-boring-automation"}
        for name, slug in articles.items():
            text = (ROOT / "skills" / name / "SKILL.md").read_text()
            data = frontmatter(text)
            self.assertEqual(data["license"], "CC-BY-4.0")
            self.assertEqual(data["metadata"], {
                "author": "Pedro Borrero, borre.ro", "support": "none", "version": "1.0",
                "source": "https://borre.ro/newsletter/" + slug,
            })
            self.assertIn("Article publication pending.", text)
            self.assertEqual(text.count("https://borre.ro/newsletter/"), 1)

    def test_companion_procedural_instructions_are_unchanged(self):
        expected = {
            "business-context-map": "511880c73c22c2661f31a51937dbad70675bdb901b43dec1236db8cdaf0259ce",
            "workflow-or-agent": "46f83f456966a0608a77799341dcc300e35b79b7a36abc66d1b0c4a236a22bb0",
        }
        for name, digest in expected.items():
            text = (ROOT / "skills" / name / "SKILL.md").read_text()
            procedure = text.split("---", 2)[2].split("## About this skill")[0]
            self.assertEqual(hashlib.sha256(procedure.encode()).hexdigest(), digest)

    def assert_human_first_skill_table(self, text):
        """Check the reader-facing catalogue, not its paragraph wording."""
        tables = re.findall(r"(?:^\|[^\n]*\|[ \t]*(?:\n|$))+", text, re.M)
        catalogues = [table for table in tables if "skills/" in table]
        self.assertEqual(len(catalogues), 1, "Expected one skill catalogue")
        table = catalogues[0]
        rows = [[cell.strip() for cell in line.strip().strip("|").split("|")]
                for line in table.splitlines()]
        self.assertEqual(len(rows), 5, "Expected header, separator and three skills")
        for row in rows:
            self.assertEqual(len(row), 2, "Catalogue needs skill then purpose, no licence column")
        self.assertEqual(rows[0][0], "Skill", "First column must name the skill")
        self.assertTrue(rows[0][1])
        for cell in rows[1]:
            self.assertRegex(cell, r"^:?-{3,}:?$")
        self.assertNotRegex(table, r"(?i)\blicen[cs]e\b|\bMIT\b|\bCC-BY(?:-4\.0)?\b")
        names = {
            "skills/project-prd/SKILL.md": "Project PRD",
            "skills/business-context-map/SKILL.md": "Business context map",
            "skills/workflow-or-agent/SKILL.md": "Workflow or agent",
        }
        targets = []
        for first, purpose in rows[2:]:
            match = re.fullmatch(r"\[([^\]\n]+)\]\((skills/[^\s)]+/SKILL\.md)\)", first)
            self.assertIsNotNone(match, "First cell must be a linked, human-readable skill name")
            label, target = match.groups()
            self.assertIn(target, names)
            self.assertEqual(label, names[target], "Use the skill name, not a slug or path")
            targets.append(target)
            self.assertTrue(purpose, "Second cell must explain the purpose")
            self.assertNotRegex(purpose, r"skills/[^\s)]+/SKILL\.md")
        self.assertEqual(sorted(targets), sorted(names), "Each skill must appear exactly once")

    def test_readme_skill_table_is_human_first(self):
        self.assert_human_first_skill_table((ROOT / "README.md").read_text())

    def test_skill_table_guard_rejects_reader_regressions(self):
        header = "| Skill | What it helps you do |\n| --- | --- |\n"
        rows = [
            "| [Project PRD](skills/project-prd/SKILL.md) | Write a project brief. |\n",
            "| [Business context map](skills/business-context-map/SKILL.md) | Map business knowledge. |\n",
            "| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Plan a process. |\n",
        ]
        valid = header + "".join(rows)
        self.assert_human_first_skill_table(valid)
        old = ("| Need | Read and apply | Licence |\n| --- | --- | --- |\n"
               "| Write a brief | [Project PRD](skills/project-prd/SKILL.md) | MIT |\n"
               "| Map knowledge | [Business context map](skills/business-context-map/SKILL.md) | CC-BY-4.0 |\n"
               "| Plan a process | [Workflow or agent](skills/workflow-or-agent/SKILL.md) | CC-BY-4.0 |\n")
        misplaced = header + "".join(
            f"| {cells[1].strip()} | {cells[0].strip()} |\n"
            for row in rows for cells in [row.strip().strip("|").split("|")]
        )
        invalid = {
            "old need-first licence table": old,
            "names in second column": misplaced,
            "duplicate skill replaces another": header + rows[0] + rows[0] + rows[2],
            "missing skill": header + "".join(rows[:2]),
            "extra duplicate row": valid + rows[0],
            "slug instead of readable name": valid.replace("[Project PRD]", "[project-prd]"),
            "unlinked name": valid.replace("[Project PRD](skills/project-prd/SKILL.md)", "Project PRD"),
            "empty purpose": valid.replace("Write a project brief.", ""),
            "licence ID in purpose": valid.replace("Write a project brief.", "MIT"),
            "licence instead of purpose column": valid.replace("What it helps you do", "Licence"),
        }
        for name, text in invalid.items():
            with self.subTest(regression=name), self.assertRaises(AssertionError):
                self.assert_human_first_skill_table(text)

    def test_readme_index_and_shared_agent_pointer(self):
        for name in ("README.md", "AGENTS.md", "CLAUDE.md"):
            self.assertTrue((ROOT / name).is_file(), f"Required shared guidance missing: {name}")
        readme = (ROOT / "README.md").read_text()
        agents = (ROOT / "AGENTS.md").read_text()
        claude = (ROOT / "CLAUDE.md").read_text()
        for name in SKILLS:
            self.assertIn(f"skills/{name}/SKILL.md", readme)
            self.assertIn(name, agents)
        self.assertIn("[AGENTS.md](AGENTS.md)", claude)
        self.assertLess(len(claude.splitlines()), 12)
        self.assertIn("https://github.com/pxb/boringBits", readme)
        self.assertNotIn("Publication pending", readme)
        self.assertNotIn("https://borre.ro/newsletter/", readme)
        for target in ("docs/compatibility.md", "CONTRIBUTING.md", "LICENSE", "THIRD-PARTY-NOTICES.md"):
            self.assertRegex(readme, rf"\[[^\]\n]+\]\({re.escape(target)}\)")
        # Require practical read/apply guidance without pinning whole paragraphs.
        for concept in (r"\b(?:read|load)\b", r"\bresources\b", r"\baccess\b", r"\b(?:text|attachments?)\b"):
            self.assertRegex(readme.lower(), concept)
        self.assertRegex(readme.lower(), r"native[^.\n]*install[^.\n]*not tested")
        self.assertIn("feat/openai-marketplace", readme)
        self.assertIn("Sparse paths: leave blank", readme)
        self.assertNotIn("plugins/codex", readme)
        self.assertNotRegex(readme, r"Git ref:.*`main`")
        self.assertIn("Brief approval is not execution permission", agents)

    def test_mixed_licences_and_notices(self):
        licence = (ROOT / "LICENSE").read_text()
        notices = (ROOT / "THIRD-PARTY-NOTICES.md").read_text()
        for phrase in ["MIT License", "CC-BY-4.0", "skills/project-prd", "skills/business-context-map", "skills/workflow-or-agent", "not a blanket MIT licence"]:
            self.assertIn(phrase, licence)
        for phrase in ["Permission is hereby granted", 'THE SOFTWARE IS PROVIDED "AS IS"', "Pedro Borrero"]:
            self.assertIn(phrase, licence)
        for phrase in ["6cf33adb05b3543452e3df349483e30971d89cdf", "creativecommons.org/licenses/by/4.0/", "skills/project-prd/THIRD-PARTY-NOTICES.md", "Consulted, not adapted"]:
            self.assertIn(phrase, notices)

    def assert_local_reference(self, page, target):
        parsed = urlsplit(target)
        if parsed.scheme in {"https", "http", "mailto"} or not parsed.path:
            return
        self.assertFalse(parsed.scheme or parsed.netloc, target)
        decoded = unquote(parsed.path)
        self.assertFalse(Path(decoded).is_absolute(), target)
        resolved = (page.parent / decoded).resolve()
        self.assertTrue(resolved.is_relative_to(ROOT), target)
        self.assertTrue(resolved.is_file(), f"{page.relative_to(ROOT)} -> {target}")

    def test_local_markdown_and_backtick_resource_links(self):
        for page in ROOT.rglob("*.md"):
            if ".git" in page.parts:
                continue
            text = page.read_text()
            targets = re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", text)
            # A code-formatted external link label names an upstream path, not a local file.
            prose = re.sub(r"\[[^\]\n]+\]\(([^\s)]+)\)", "", text)
            targets += re.findall(r"`([\w./-]+\.md)`", prose)
            for target in targets:
                with self.subTest(page=page.relative_to(ROOT), target=target):
                    self.assert_local_reference(page, target)

    def test_reference_guard_rejects_missing_and_escaping_paths(self):
        for target in ["../outside.md", "%2e%2e/outside.md", "/etc/passwd", "missing.md", "file:///etc/passwd", "//example.com/file"]:
            with self.subTest(target=target), self.assertRaises(AssertionError):
                self.assert_local_reference(ROOT / "README.md", target)

    def test_public_file_allowlist_and_text_only_skills(self):
        expected = {
            ".gitignore", "README.md", "AGENTS.md", "CLAUDE.md", "LICENSE",
            "THIRD-PARTY-NOTICES.md", "CONTRIBUTING.md", "docs/compatibility.md",
            "requirements-test.txt", "tests/test_repository.py",
            "plugin.json", ".agents/plugins/marketplace.json",
            "skills/project-prd/SKILL.md", "skills/project-prd/PRD-TEMPLATE.md",
            "skills/project-prd/THIRD-PARTY-NOTICES.md", "skills/project-prd/SOURCE-REUSE.md",
            "skills/business-context-map/SKILL.md", "skills/workflow-or-agent/SKILL.md",
        }
        files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts}
        self.assertEqual(files, expected)
        for path in files:
            p = ROOT / path
            self.assertFalse(p.is_symlink(), path)
            self.assertEqual(p.stat().st_mode & 0o111, 0, path)
            self.assertNotIn(b"\0", p.read_bytes(), path)
            p.read_text(encoding="utf-8")
            if path.startswith("skills/"):
                self.assertEqual(p.suffix, ".md")
        for p in ROOT.rglob("*"):
            if ".git" not in p.relative_to(ROOT).parts:
                self.assertFalse(p.is_symlink(), str(p))

    def test_no_known_secret_or_private_operational_patterns(self):
        patterns = [
            r"gh[pousr]_" + r"[A-Za-z0-9]{30,}",
            r"github_" + r"pat_[A-Za-z0-9_]{30,}",
            r"sk-" + r"[A-Za-z0-9_-]{32,}",
            "-----BEGIN " + r"(?:OPENSSH |RSA |EC )?PRIVATE KEY-----",
            r"https?://[^\s/]+:[^\s/]+@",
            "/" + "vault/", "/opt/" + "hermes-state/", "/work/" + "borre.ro",
            "HERMES_" + "WEBHOOK_SECRET", "n8n." + "borre.ro",
            "bypass" + "Permissions", "dangerously-" + "skip-permissions",
        ]
        for p in ROOT.rglob("*"):
            if not p.is_file() or ".git" in p.relative_to(ROOT).parts:
                continue
            text = p.read_text()
            for pattern in patterns:
                self.assertIsNone(re.search(pattern, text), f"{p.relative_to(ROOT)}: forbidden pattern")

    def assert_delivery(self, root):
        """Chosen skills-only contract, not an official marketplace JSON Schema.

        The official portable schema is validated separately, without network
        access or a vendored copy in this suite. These stricter repository gates
        also cover OpenAI metadata, local-source semantics and resource closure.
        """
        manifest_path = root / "plugin.json"
        self.assertTrue(manifest_path.is_file(), "Missing root portable manifest")
        manifest = json.loads(manifest_path.read_text())
        self.assertEqual(set(manifest), {
            "$schema", "name", "version", "description", "author",
            "homepage", "repository", "extensions",
        })
        self.assertEqual(manifest["$schema"], "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json")
        self.assertEqual(manifest["name"], "boring-bits")
        self.assertEqual(manifest["version"], "0.1.0")
        self.assertIsInstance(manifest["description"], str)
        self.assertTrue(manifest["description"].strip())
        self.assertEqual(manifest["author"], {"name": "Pedro Borrero", "url": "https://borre.ro"})
        self.assertEqual(manifest["homepage"], "https://borre.ro")
        self.assertEqual(manifest["repository"], "https://github.com/pxb/boringBits")
        self.assertEqual(set(manifest["extensions"]), {"com.openai"})
        overlay = manifest["extensions"]["com.openai"]
        self.assertEqual(set(overlay), {"interface"})
        interface = overlay["interface"]
        self.assertEqual(set(interface), {
            "displayName", "shortDescription", "developerName", "category", "websiteURL",
        })
        self.assertEqual(interface["displayName"], "Boring Bits")
        self.assertEqual(interface["developerName"], "Pedro Borrero")
        self.assertEqual(interface["category"], "Productivity")
        self.assertEqual(interface["websiteURL"], "https://borre.ro")
        self.assertIsInstance(interface["shortDescription"], str)
        self.assertTrue(interface["shortDescription"].strip())

        catalogue_path = root / ".agents/plugins/marketplace.json"
        self.assertTrue(catalogue_path.is_file(), "Missing marketplace manifest")
        catalogue = json.loads(catalogue_path.read_text())
        self.assertEqual(set(catalogue), {"name", "interface", "plugins"})
        self.assertEqual(catalogue["name"], "boring-bits")
        self.assertEqual(catalogue["interface"], {"displayName": "Boring Bits"})
        self.assertEqual(len(catalogue["plugins"]), 1)
        entry = catalogue["plugins"][0]
        self.assertEqual(set(entry), {"name", "source", "policy", "category"})
        self.assertEqual(entry["name"], manifest["name"])
        self.assertEqual(entry["policy"], {"installation": "AVAILABLE", "authentication": "ON_INSTALL"})
        self.assertEqual(entry["category"], "Productivity")
        source = entry["source"]
        self.assertEqual(set(source), {"source", "path"})
        self.assertEqual(source["source"], "local")
        self.assertTrue(source["path"].startswith("./"))
        selected = (root / source["path"]).resolve()
        self.assertTrue(selected.is_relative_to(root.resolve()), "Source escapes marketplace root")
        self.assertEqual(selected, root.resolve(), "Package must select canonical repository root")
        self.assertEqual(source["path"], "./")

        found = {p.parent.name for p in selected.glob("skills/*/SKILL.md")}
        self.assertEqual(found, SKILLS, "Root discovery must find all three skills")
        self.assertEqual(len(list(selected.rglob("SKILL.md"))), 3, "No copied skill bodies")
        required = {
            "plugin.json", ".agents/plugins/marketplace.json", "LICENSE", "THIRD-PARTY-NOTICES.md",
            "skills/project-prd/PRD-TEMPLATE.md", "skills/project-prd/SOURCE-REUSE.md",
            "skills/project-prd/THIRD-PARTY-NOTICES.md",
        } | {f"skills/{name}/SKILL.md" for name in SKILLS}
        for relative in sorted(required):
            resource = selected / relative
            self.assertTrue(resource.is_file(), f"Missing packaged resource: {relative}")
        for path in selected.rglob("*"):
            if ".git" not in path.relative_to(selected).parts:
                self.assertFalse(path.is_symlink(), "No symlink escape or duplicate alias")
        forbidden = {"mcp.json", ".mcp.json", ".app.json", ".codex", ".codex-plugin", "hooks", "scripts"}
        self.assertFalse(forbidden & {p.name for p in selected.iterdir()}, "No runtime/config side effects")
        return required

    def test_openai_root_package_discovery(self):
        self.assert_delivery(ROOT)

    def test_openai_delivery_rejects_manifest_and_catalogue_regressions(self):
        changes = [
            ("plugin.json", lambda d: d.update(name="Boring Bits")),
            ("plugin.json", lambda d: d.update({"$schema": "https://example.com/wrong-schema"})),
            ("plugin.json", lambda d: d.update(license="MIT")),
            ("plugin.json", lambda d: d.update(skills="./skills/")),
            ("plugin.json", lambda d: d["extensions"]["com.openai"].update(hooks="./hooks/hooks.json")),
            ("plugin.json", lambda d: d["extensions"]["com.openai"].update(apps="./.app.json")),
            ("plugin.json", lambda d: d["extensions"]["com.openai"]["interface"].update(capabilities=["Write"])),
            (".agents/plugins/marketplace.json", lambda d: d.update(name="wrong-marketplace")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0].update(name="wrong-plugin")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"].clear()),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"].append(d["plugins"][0].copy())),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0].update(policy={})),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["policy"].update(installation="INSTALLED_BY_DEFAULT")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(path="./../outside")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(path="/etc")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(path="./.agents/plugins")),
            (".agents/plugins/marketplace.json", lambda d: d["plugins"][0]["source"].update(source="url")),
        ]
        with tempfile.TemporaryDirectory(prefix="boring-bits-contract-") as tmp:
            for index, (relative, change) in enumerate(changes):
                with self.subTest(case=index, file=relative):
                    fixture = Path(tmp) / str(index)
                    shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns(".git"))
                    path = fixture / relative
                    data = json.loads(path.read_text())
                    change(data)
                    path.write_text(json.dumps(data))
                    with self.assertRaises(AssertionError):
                        self.assert_delivery(fixture)

    def test_openai_delivery_rejects_missing_resources_and_sparse_selection(self):
        required = self.assert_delivery(ROOT)
        with tempfile.TemporaryDirectory(prefix="boring-bits-resources-") as tmp:
            for index, relative in enumerate(sorted(required)):
                with self.subTest(missing=relative):
                    fixture = Path(tmp) / str(index)
                    # Build an incomplete checkout, rather than mutating real files.
                    for path in ROOT.rglob("*"):
                        rel = path.relative_to(ROOT)
                        if path.is_file() and ".git" not in rel.parts and rel.as_posix() != relative:
                            dest = fixture / rel
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            dest.write_bytes(path.read_bytes())
                    with self.assertRaises(AssertionError):
                        self.assert_delivery(fixture)
            sparse = Path(tmp) / "sparse"
            sparse.mkdir()
            # Selecting only a plugin subdirectory cannot deliver this root package.
            with self.assertRaisesRegex(AssertionError, "Missing root portable manifest"):
                self.assert_delivery(sparse)

    def test_openai_delivery_rejects_duplicate_symlink_and_runtime_payloads(self):
        additions = {
            "copied/skills/project-prd/SKILL.md": "Copied skill body",
            "mcp.json": '{"mcpServers": {}}',
            ".mcp.json": '{"mcpServers": {}}',
            ".app.json": '{"apps": {}}',
            "hooks/hooks.json": "{}",
            ".codex/config.toml": "[plugins]\n",
            ".codex-plugin/plugin.json": "{}",
            "scripts/install.sh": "exit 0\n",
        }
        with tempfile.TemporaryDirectory(prefix="boring-bits-boundary-") as tmp:
            for index, (relative, text) in enumerate(additions.items()):
                with self.subTest(addition=relative):
                    fixture = Path(tmp) / str(index)
                    shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns(".git"))
                    added = fixture / relative
                    added.parent.mkdir(parents=True, exist_ok=True)
                    added.write_text(text)
                    with self.assertRaises(AssertionError):
                        self.assert_delivery(fixture)
            fixture = Path(tmp) / "symlink"
            shutil.copytree(ROOT, fixture, ignore=shutil.ignore_patterns(".git"))
            (fixture / "alias").symlink_to(ROOT / "skills", target_is_directory=True)
            with self.assertRaises(AssertionError):
                self.assert_delivery(fixture)

    def test_test_script_syntax(self):
        ast.parse((ROOT / "tests/test_repository.py").read_text())

    def test_exactly_three_canonical_skills(self):
        found = {p.parent.name for p in ROOT.glob("skills/*/SKILL.md")}
        self.assertEqual(found, SKILLS)
        self.assertEqual(len(list(ROOT.rglob("SKILL.md"))), 3)


if __name__ == "__main__":
    unittest.main()
