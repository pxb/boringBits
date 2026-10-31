"""Local publication gates. Run from repo root: python -B -m unittest discover -s tests -v."""
from pathlib import Path
import ast
import hashlib
import re
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
        self.assertIn("Publication pending", readme)
        self.assertNotIn("https://borre.ro/newsletter/", readme)
        self.assertIn("Native plugin adapters are not implemented", readme)
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

    def test_test_script_syntax(self):
        ast.parse((ROOT / "tests/test_repository.py").read_text())

    def test_exactly_three_canonical_skills(self):
        found = {p.parent.name for p in ROOT.glob("skills/*/SKILL.md")}
        self.assertEqual(found, SKILLS)
        self.assertEqual(len(list(ROOT.rglob("SKILL.md"))), 3)


if __name__ == "__main__":
    unittest.main()
