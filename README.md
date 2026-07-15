# 4-dark-energy-cosmology

## Paper identity

- **Paper:** Paper 4
- **Working title:** Dark Energy, Sea–Interface Dynamics and Cosmology
- **Core scientific responsibility:** equilibrium vacuum, dark energy, Sea–Interface phase conversion, expansion mapping, wrinkles, black-hole reverse transition
- **Current status:** `INFRASTRUCTURE INITIALIZED`

This repository contains one paper only: Paper 4. Historical scientific progress will be imported separately; no progress is inferred during infrastructure initialization.

## Role separation

### ChatGPT

ChatGPT supports conceptual discussion, physical interpretation, analytic derivation planning, gate design, calculation specifications, and identification of assumptions and competing interpretations. ChatGPT does not certify numerical results.

### Codex

Codex maintains the repository; implements symbolic and numerical work; creates tests, regression anchors, reproducible artifacts, and result files; and maintains branch and commit discipline. Codex must not promote a result into a paper claim without review.

### Claude

Claude acts as an independent reviewer/discriminator: reviewing derivations and results, deciding whether a gate passes, identifying overclaims, and updating the paper only after results are accepted.

### User / Principal Investigator

The Principal Investigator owns the physical programme, approves assumptions, gates, and scope changes, accepts or rejects final verdicts, and decides when paper text may be updated.

## Directory guide

- `paper/`: paper source and figures after historical import.
- `derivations/`: pre-implementation analytic notes.
- `scripts/`: symbolic, numerical, and processing code.
- `tests/`: structure, regression, and scientific tests.
- `results/`: immutable raw outputs and provenance-tracked processed artifacts.
- `reviews/`: independent review records.
- `archive/`: preserved retired routes and historical material.
- `docs/`: workflow, result schema, and branching policy.

## Standard gate workflow

1. ChatGPT and the Principal Investigator specify the question, assumptions, anchors, deliverables, and kill criterion.
2. A derivation note is committed before production code.
3. Codex implements on one `gate/<gate-name>` branch, with tests and stored outputs.
4. Claude independently reviews the artifacts and records a verdict.
5. The Principal Investigator accepts or rejects the verdict and authorizes any paper update.

## Reproducibility commands

```text
make check
make test
make lint
make structure
```

> **Warning:** No result is accepted merely because code runs. Acceptance requires analytic and regression anchors, tests, stored outputs, provenance, and independent review.
