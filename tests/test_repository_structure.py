"""Verify the required research repository foundation and migration record."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = (
    # governance scaffolding
    "README.md",
    "PROGRESS.md",
    "GATES.md",
    "DECISION_LOG.md",
    "ROADMAP.md",
    "CLAIMS.md",
    "HANDOFF.md",
    "AGENTS.md",
    "CONVENTIONS.md",
    "CITATION.cff",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    "pyproject.toml",
    "Makefile",
    "MIGRATION.md",
    "paper/README.md",
    "paper/figures/.gitkeep",
    "derivations/README.md",
    "scripts/README.md",
    "scripts/__init__.py",
    "tests/README.md",
    "tests/test_repository_structure.py",
    "tests/test_dark_energy_anchors.py",
    "results/README.md",
    "results/raw/.gitkeep",
    "results/processed/.gitkeep",
    "results/figures/.gitkeep",
    "reviews/README.md",
    "reviews/chatgpt/.gitkeep",
    "reviews/claude/.gitkeep",
    "archive/README.md",
    "docs/RESEARCH_WORKFLOW.md",
    "docs/RESULT_SCHEMA.md",
    "docs/BRANCHING_POLICY.md",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/gate.yml",
    ".github/ISSUE_TEMPLATE/bug.yml",
    ".github/ISSUE_TEMPLATE/paper-sync.yml",
    ".github/workflows/ci.yml",
    # migrated derivations
    "derivations/de_interface_wrinkle.md",
    "derivations/driven_interface_wrinkle.md",
    "derivations/sea_interface_phase_conversion.md",
    "derivations/wrinkle_bound_excitation.md",
    # migrated gate scripts + vendored gamma module
    "scripts/fierz_verify.py",
    "scripts/de_interface_wrinkle.py",
    "scripts/driven_interface_wrinkle.py",
    "scripts/driven_wrinkle_2d.py",
    "scripts/sea_interface.py",
    "scripts/sea_bh_core.py",
    "scripts/wrinkle_bound_excitation.py",
    # immutable raw archives (representative + verdict), provenance, environment
    "results/de-interface-wrinkle/raw/dewrinkle_output.txt",
    "results/de-interface-wrinkle/raw/dewrinkle_verdict.txt",
    "results/de-interface-wrinkle/PROVENANCE.md",
    "results/de-interface-wrinkle/environment.txt",
    "results/driven-interface-wrinkle/raw/driven_verdict.txt",
    "results/driven-interface-wrinkle/raw/driven_output.txt",
    "results/driven-interface-wrinkle/PROVENANCE.md",
    "results/driven-interface-wrinkle/environment.txt",
    "results/sea-interface-phase-conversion/raw/sea_interface_verdict.txt",
    "results/sea-interface-phase-conversion/raw/sea_bh_output.txt",
    "results/sea-interface-phase-conversion/PROVENANCE.md",
    "results/sea-interface-phase-conversion/environment.txt",
    "results/wrinkle-bound-excitation/raw/wrinkle_bound_verdict.txt",
    "results/wrinkle-bound-excitation/raw/wrinkle_bound_output.txt",
    "results/wrinkle-bound-excitation/PROVENANCE.md",
    "results/wrinkle-bound-excitation/environment.txt",
)

REQUIRED_DIRECTORIES = (
    "paper",
    "paper/figures",
    "derivations",
    "scripts",
    "tests",
    "results",
    "results/raw",
    "results/processed",
    "results/figures",
    "results/de-interface-wrinkle/raw",
    "results/de-interface-wrinkle/processed",
    "results/driven-interface-wrinkle/raw",
    "results/driven-interface-wrinkle/processed",
    "results/sea-interface-phase-conversion/raw",
    "results/sea-interface-phase-conversion/processed",
    "results/wrinkle-bound-excitation/raw",
    "results/wrinkle-bound-excitation/processed",
    "reviews",
    "reviews/chatgpt",
    "reviews/claude",
    "archive",
    "docs",
    ".github",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
)


def test_required_files_exist() -> None:
    """All mandated files must exist as regular files."""
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    assert not missing, f"Missing required files: {missing}"


def test_required_directories_exist() -> None:
    """All mandated directories must exist."""
    missing = [path for path in REQUIRED_DIRECTORIES if not (ROOT / path).is_dir()]
    assert not missing, f"Missing required directories: {missing}"


def test_claimed_gates_are_registered() -> None:
    """Every gate ID cited in CLAIMS.md must have a matching heading in GATES.md.

    Guards the dangling-reference defect seen in the 3-vector-sector migration.
    """
    claims = (ROOT / "CLAIMS.md").read_text(encoding="utf-8")
    gates = (ROOT / "GATES.md").read_text(encoding="utf-8")
    cited = set()
    for row in claims.splitlines():
        if not row.startswith("| P4-"):
            continue
        cited.update(
            item.strip() for item in row.split("|")[5].split(",") if item.strip() != "None"
        )
    headings = set(re.findall(r"^## (P4-[A-Z0-9-]+)", gates, flags=re.MULTILINE))
    assert cited, "no P4 gate references found in CLAIMS.md"
    assert cited <= headings, f"Dangling gate references: {sorted(cited - headings)}"
