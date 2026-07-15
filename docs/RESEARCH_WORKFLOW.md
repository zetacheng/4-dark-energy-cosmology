# Research Workflow

## Purpose

This repository uses scientific gates to separate proposed interpretations from reviewed, reproducible results.

## Roles

### ChatGPT

ChatGPT handles conceptual discussion, physical interpretation, analytic derivation planning, gate design, preparation of calculation specifications, and identification of assumptions and competing interpretations. ChatGPT does not certify numerical results.

### Codex

Codex handles repository maintenance, symbolic and numerical implementation, tests, regression anchors, reproducibility, result files, and branch and commit discipline. Codex must not promote a result into a paper claim without review.

### Claude

Claude is the independent reviewer/discriminator. It reviews derivations and results, issues a verdict on whether a gate passes, identifies overclaims, and updates the paper only after results are accepted.

### User / Principal Investigator

The Principal Investigator owns the physical programme, approves assumptions, gates, and scope changes, accepts or rejects final verdicts, and decides when paper text may be updated.

## Gate lifecycle

1. Open a gate in `GATES.md` and create one `gate/<gate-name>` branch.
2. Lock the scientific question, scope, assumptions, conventions, inputs, analytic anchors, regression anchors, kill criterion, computations, and deliverables.
3. Commit the derivation note before production code.
4. Implement, test, and store immutable raw outputs plus provenance-tracked processed artifacts.
5. Record the result without suppressing failed or inconclusive outcomes.
6. Obtain an independent Claude verdict against the pre-registered criteria.
7. Obtain Principal Investigator acceptance or rejection.
8. Close the gate and merge accepted artifacts. Update paper text only when explicitly authorized.

No result is accepted merely because code runs. It requires anchors, tests, stored outputs, provenance, and independent review.
