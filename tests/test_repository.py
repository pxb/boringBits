"""Local publication gates. Run from repo root: python -B -m unittest discover -s tests -v."""
from pathlib import Path
import ast
import hashlib
import json
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
SALES_SKILLS = {"business-setup", "enquiry", "prospecting", "proposal", "pipeline"}
SKILLS = {"project-prd", "business-context-map", "workflow-or-agent"} | SALES_SKILLS
# Folder of each skill. Toolkit skills sit in skills/; BusinessBits nests by area and role.
PATHS = {
    "project-prd": "skills/project-prd",
    "business-context-map": "skills/business-context-map",
    "workflow-or-agent": "skills/workflow-or-agent",
    "business-setup": "businessbits/setup/business-setup",
    "enquiry": "businessbits/revenue/sales/enquiry",
    "prospecting": "businessbits/revenue/sales/prospecting",
    "proposal": "businessbits/revenue/sales/proposal",
    "pipeline": "businessbits/revenue/sales/pipeline",
}
BB_RECORDS = "businessbits/RECORDS.md"
CATALOGUE = {
    "skills/project-prd/SKILL.md": "Project PRD",
    "skills/business-context-map/SKILL.md": "Business context map",
    "skills/workflow-or-agent/SKILL.md": "Workflow or agent",
}
BB_CATALOGUE = {
    "setup/business-setup/SKILL.md": "Business setup",
    "revenue/sales/enquiry/SKILL.md": "Enquiry",
    "revenue/sales/prospecting/SKILL.md": "Prospecting",
    "revenue/sales/proposal/SKILL.md": "Proposal",
    "revenue/sales/pipeline/SKILL.md": "Pipeline",
}
# Contract sections every BusinessBits skill carries, beyond its numbered steps.
CONTRACT_HEADINGS = ("## Output", "## What it replaces", "## When it goes wrong", "## Never", "## About this skill")
# Supporting files sit in the Agent Skills subfolders, linked from SKILL.md, so hosts that copy
# only referenced files from those folders (Hermes installs from GitHub) bring them along.
SALES_RESOURCES = {
    "business-setup": {"templates/PROFILE-TEMPLATE.md"},
    "enquiry": set(),
    "prospecting": {"references/RESEARCH-METHOD.md", "references/UK-CONTACT-RULES.md"},
    "proposal": {"references/PRICING.md", "references/MARKET-COMPARISON.md", "templates/SOW-TEMPLATE.md"},
    "pipeline": set(),
}
RESOURCE_DIRS = {"references", "templates", "scripts", "assets"}
# sha256 of lower-case private names (clients, partners, people, internal systems).
# Stored as hashes so the gate itself does not publish them.
PRIVATE_NAME_HASHES = {
    "26b037d87338666f1fe5789d872889ce1ac3be091594ed84e7bfa32d221c86f5",
    "57a4911c9baba00aa0f5e297cccd982e32a136e7f8fbea988a2d26f8e99d02a5",
    "04f4010bfaae02b8fb74ed32dbdfd5b1cfb7c76b6d7c0b92f591f05d5a6da084",
    "552bdf4bbc9329b555b93e7c9b6a38f36c6edb58b0e7fca0392f79528cc1b9e6",
    "9997c063b22332c6307bcdf6076ff91010a0890e9ddf99277b69e6acc31a15dd",
    "4818c34613a2fa5fb96087aeafd6e40cfd78bbd887f0180585753ae7a3821222",
    "30bd72aabc1490662c6d57a5dadca8e9f8dce076a079f96acd2c73e2a98ab8d1",
    "a6a3d81d5168a5b2b7dd2c06aa4c4a28f8e535f2dc7f008bd7ddd1b3c312b9dd",
    "b55801bba9a4bc509f24427d36084bfbc4e8c688c56a4c4def1a437af86ed166",
    "aed295549829e61e7af96b0d178d4e91fa99190486a4d19509abeb6718d9ecd0",
    "e52a1359297822655226696b53192f9085c5f161d1bda5cbaed8e9ceb64c904b",
    "84245172f59c8bd80e1454c3aa467a8d46a93dbf96c72309d9b3e42afa8b6d08",
    "b00821c4d40072f66d27a42e4ecf6f2a2a1130fdc50b533e28c79b2987d86fd8",
    "84cb95fc1f7c2813e74b2ee5b1de25ae400f1caf1d1e0e5f4097e0754b7d80fe",
    "cb607cc20b6562efe7dcb4cc6e267e69ade727b15c00703c1fd34adb223d3264",
    "6bc3879851c7e0f01f04183d58ae8ee05af37a48757fe324d96bf98a8eb11d1b",
    "a2212359b7e79fda79ef39d39ba37804ecc353951e76727f3eb20bffea677d77",
    "ebb1245696a936b70148d63657017c47c179bb26064832038d1478bb10bc08d9",
    "28812f61a0e85c8aba2afe971746fd9a94960fe2c344e74e59588399ca3bfce7",
    "bf79c9b69a5b6ca12f265895aff3ce23c83baf249c484a26dc5f3705c6219731",
}


def private_name_hits(text):
    words = re.findall(r"[a-z0-9]+", text.lower())
    hits = set()
    for size in (1, 2, 3):
        for i in range(len(words) - size + 1):
            phrase = " ".join(words[i:i + size])
            if hashlib.sha256(phrase.encode()).hexdigest() in PRIVATE_NAME_HASHES:
                hits.add(phrase)
    return hits


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
                self.assert_skill_schema((ROOT / PATHS[name] / "SKILL.md").read_text(), name)

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

    def assert_human_first_skill_table(self, text, names=None):
        """Check the reader-facing catalogue, not its paragraph wording."""
        tables = re.findall(r"(?:^\|[^\n]*\|[ \t]*(?:\n|$))+", text, re.M)
        catalogues = [table for table in tables if "SKILL.md" in table]
        self.assertEqual(len(catalogues), 1, "Expected one skill catalogue")
        table = catalogues[0]
        rows = [[cell.strip() for cell in line.strip().strip("|").split("|")]
                for line in table.splitlines()]
        names = CATALOGUE if names is None else names
        self.assertEqual(len(rows), len(names) + 2, "Expected header, separator and one row per skill")
        for row in rows:
            self.assertEqual(len(row), 2, "Catalogue needs skill then purpose, no licence column")
        self.assertEqual(rows[0][0], "Skill", "First column must name the skill")
        self.assertTrue(rows[0][1])
        for cell in rows[1]:
            self.assertRegex(cell, r"^:?-{3,}:?$")
        self.assertNotRegex(table, r"(?i)\blicen[cs]e\b|\bMIT\b|\bCC-BY(?:-4\.0)?\b")
        targets = []
        for first, purpose in rows[2:]:
            match = re.fullmatch(r"\[([^\]\n]+)\]\(([^\s)]+/SKILL\.md)\)", first)
            self.assertIsNotNone(match, "First cell must be a linked, human-readable skill name")
            label, target = match.groups()
            self.assertIn(target, names)
            self.assertEqual(label, names[target], "Use the skill name, not a slug or path")
            targets.append(target)
            self.assertTrue(purpose, "Second cell must explain the purpose")
            self.assertNotRegex(purpose, r"[^\s)]+/SKILL\.md")
        self.assertEqual(sorted(targets), sorted(names), "Each skill must appear exactly once")

    def test_readme_skill_table_is_human_first(self):
        self.assert_human_first_skill_table((ROOT / "README.md").read_text())
        self.assert_human_first_skill_table((ROOT / "businessbits/README.md").read_text(), BB_CATALOGUE)

    def test_skill_table_guard_rejects_reader_regressions(self):
        header = "| Skill | What it helps you do |\n| --- | --- |\n"
        rows = [
            "| [Project PRD](skills/project-prd/SKILL.md) | Write a project brief. |\n",
            "| [Business context map](skills/business-context-map/SKILL.md) | Map business knowledge. |\n",
            "| [Workflow or agent](skills/workflow-or-agent/SKILL.md) | Plan a process. |\n",
        ]
        valid = header + "".join(rows)
        three = {k: CATALOGUE[k] for k in ("skills/project-prd/SKILL.md", "skills/business-context-map/SKILL.md", "skills/workflow-or-agent/SKILL.md")}
        self.assert_human_first_skill_table(valid, three)
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
                self.assert_human_first_skill_table(text, three)

    def test_readme_index_and_shared_agent_pointer(self):
        for name in ("README.md", "AGENTS.md", "CLAUDE.md"):
            self.assertTrue((ROOT / name).is_file(), f"Required shared guidance missing: {name}")
        readme = (ROOT / "README.md").read_text()
        agents = (ROOT / "AGENTS.md").read_text()
        claude = (ROOT / "CLAUDE.md").read_text()
        bb_readme = (ROOT / "businessbits/README.md").read_text()
        self.assertIn("businessbits/README.md", readme)
        for name in SKILLS:
            if name in SALES_SKILLS:
                self.assertIn(PATHS[name].removeprefix("businessbits/") + "/SKILL.md", bb_readme)
            else:
                self.assertIn(f"skills/{name}/SKILL.md", readme)
            self.assertIn(f"{PATHS[name]}/SKILL.md", agents)
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
        native_statements = re.findall(r"\bnative\b[^.\n]*", readme.lower())
        self.assertTrue(any(
            "install" in statement
            and re.search(r"\b(?:not available|not implemented|unavailable)\b", statement)
            and re.search(r"\b(?:untested|not tested|not available or tested)\b", statement)
            for statement in native_statements
        ), "Qualify native installation as unavailable and untested; static checks are not host evidence")
        self.assertIn("Brief approval is not execution permission", agents)

    def test_mixed_licences_and_notices(self):
        licence = (ROOT / "LICENSE").read_text()
        notices = (ROOT / "THIRD-PARTY-NOTICES.md").read_text()
        for phrase in ["MIT License", "CC-BY-4.0", "skills/project-prd", "skills/business-context-map", "skills/workflow-or-agent", "not a blanket MIT licence", BB_RECORDS] + [PATHS[s] for s in sorted(SALES_SKILLS)]:
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
            # Files the sales skills create in the user's own workspace, and the repo-root
            # name of the shared records file, are named in backticks but are not links.
            targets += [t for t in re.findall(r"`([\w./-]+\.md)`", prose)
                        if not (t.startswith("business/") or t in {"outcomes.md", "suppression.md", BB_RECORDS})]
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
            "THIRD-PARTY-NOTICES.md", "CONTRIBUTING.md", "docs/compatibility.md", "docs/testing.md",
            "requirements-test.txt", "tests/test_repository.py",
            "skills/project-prd/SKILL.md", "skills/project-prd/PRD-TEMPLATE.md",
            "skills/project-prd/THIRD-PARTY-NOTICES.md", "skills/project-prd/SOURCE-REUSE.md",
            "skills/business-context-map/SKILL.md", "skills/workflow-or-agent/SKILL.md",
            ".gitattributes", BB_RECORDS, "businessbits/README.md",
            ".github/workflows/tests.yml",
        }
        for skill, extra in SALES_RESOURCES.items():
            for name in {"SKILL.md", "references/RECORDS.md", "evals/evals.json"} | extra:
                expected.add(f"{PATHS[skill]}/{name}")
        files = {p.relative_to(ROOT).as_posix() for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.relative_to(ROOT).parts}
        self.assertEqual(files, expected)
        for path in files:
            p = ROOT / path
            self.assertFalse(p.is_symlink(), path)
            self.assertEqual(p.stat().st_mode & 0o111, 0, path)
            self.assertNotIn(b"\0", p.read_bytes(), path)
            p.read_text(encoding="utf-8")
            if any(path.startswith(folder + "/") for folder in PATHS.values()):
                if "/evals/" in path:
                    self.assertEqual(p.name, "evals.json", path)
                else:
                    self.assertEqual(p.suffix, ".md", path)
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

    def test_exactly_the_canonical_skills(self):
        found = {p.parent.relative_to(ROOT).as_posix() for p in ROOT.rglob("SKILL.md") if ".git" not in p.parts}
        self.assertEqual(found, set(PATHS.values()))
        self.assertEqual(set(PATHS), SKILLS)
        self.assertEqual(len(list(ROOT.rglob("SKILL.md"))), len(SKILLS))

    def test_sales_skills_carry_identical_records(self):
        canonical = (ROOT / BB_RECORDS).read_bytes()
        for skill in sorted(SALES_SKILLS):
            with self.subTest(skill=skill):
                self.assertEqual((ROOT / PATHS[skill] / "references/RECORDS.md").read_bytes(), canonical,
                                 f"Copy {BB_RECORDS} into the skill unchanged")

    def test_sales_skill_shape(self):
        for skill in sorted(SALES_SKILLS):
            with self.subTest(skill=skill):
                text = (ROOT / PATHS[skill] / "SKILL.md").read_text()
                data = frontmatter(text)
                self.assertEqual(data["license"], "MIT")
                self.assertLess(len(text.splitlines()), 500)
                for heading in CONTRACT_HEADINGS:
                    self.assertIn(heading, text)
                self.assertRegex(text, r"(?:\(|then )Approve\b", "Every sales skill names an approval step")
                self.assertIn("[RECORDS.md](references/RECORDS.md)", text)
                links = {t for t in re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", text) if not t.startswith("http")}
                for target in links:
                    parts = target.split("/")
                    self.assertEqual(len(parts), 2, f"{skill}: link one level down, inside its own folder: {target}")
                    self.assertIn(parts[0], RESOURCE_DIRS, f"{skill}: supporting files go in {sorted(RESOURCE_DIRS)}: {target}")
                folder = ROOT / PATHS[skill]
                files = {f.relative_to(folder).as_posix() for f in folder.rglob("*") if f.is_file()}
                self.assertEqual({f for f in files if f != "SKILL.md" and not f.startswith("evals/")}, links,
                                 f"{skill}: every supporting file is linked from SKILL.md, and nothing else sits beside it")

    def test_sales_evals(self):
        for skill in sorted(SALES_SKILLS):
            with self.subTest(skill=skill):
                data = json.loads((ROOT / PATHS[skill] / "evals/evals.json").read_text())
                self.assertEqual(data["skill_name"], skill)
                self.assertGreaterEqual(len(data["evals"]), 5)
                for case in data["evals"]:
                    self.assertTrue(case["prompt"] and case["expected_output"] and case["expectations"])
                triggers = data["trigger_queries"]
                self.assertEqual(len(triggers), 20)
                self.assertEqual(sum(q["should_trigger"] for q in triggers), 10)

    def test_no_private_names_or_long_dashes(self):
        self.assertEqual(private_name_hits("A note about Muntons and Insight Energy"), {"muntons", "insight energy"})
        for p in ROOT.rglob("*"):
            if not p.is_file() or ".git" in p.relative_to(ROOT).parts or p.name == "test_repository.py":
                continue
            text = p.read_text()
            with self.subTest(file=p.relative_to(ROOT).as_posix()):
                self.assertEqual(private_name_hits(text), set())
                if p.relative_to(ROOT).parts[0] == "businessbits" or "evals" in p.parts:
                    self.assertNotIn("\u2014", text)


if __name__ == "__main__":
    unittest.main()
