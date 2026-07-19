# Current Handoff

## Current task

Migration of the Paper 4 scientific record from `zetacheng/kappa-c2a` onto
`sync/legacy-de-migration`: **reviewed, accepted, and the v6.3 source imported**
(`reviews/claude/2026-07-19-de-migration.md`, `DECISION_LOG.md` 2026-07-19).
Ready to merge to `main`.

## Scientific question

None being run. This is a migration and audit; the four gates carry their
pre-registered legacy verdicts, transcribed verbatim.

## Locked inputs

The four legacy branch HEADs (`de-interface-wrinkle`
`5ee543c9…`, `driven-interface-wrinkle` `2a80c9db…`,
`sea-interface-phase-conversion` `1cd94b5d…`, `wrinkle-bound-excitation`
`17c187df…`); byte-identical raw artifacts under `results/*/raw/`.

## Do not reopen

The migrated raw artifacts are immutable. Do not recompute, revise, or
reinterpret any migrated number; every value is the historical record.

## Required next input

The migration is reviewed and accepted and the v6.3 source is imported; **no item
blocks the merge to `main`**. The remaining work is the open gates themselves,
none blocking:

- `P4-DEWRINKLE-01`, `P4-WRINKLE-EXC-01` — INCONCLUSIVE in-framework; would need
  an added interface/coupling degree of freedom to close.
- `P4-SEA-01` — the wall-motion → 4D expansion map (the binding gap) is
  undefined; needs an extra tiling/induced-metric assumption.
- `P4-DRIVEN-01` — closed negative for the dark-matter route (EFT-only).
- `P4-MONOPOLE-01` — closed negative (kill-window fired).

Separately (non-blocking): the PI may supply bundled figures for v6.3
(`paper/figures/` empty), and Paper 1 owns the dark-matter framing of the
interface gates (cross-repo items in `MIGRATION.md`).

## Expected Codex output

None pending; the migration is reviewed, accepted, and ready to merge.

## Questions for ChatGPT

None.

## Questions for Claude

None outstanding. The independent migration review is landed
(`reviews/claude/2026-07-19-de-migration.md`): the migration is accepted, and
the gate verdicts are recorded faithfully with nothing promoted to `VERIFIED`.

## Role handoff

ChatGPT prepares conceptual analysis, derivation plans, gate designs, calculation
specifications, assumptions, and competing interpretations; it does not certify
numerical results. Codex maintains the repository, implements calculations, tests
and regression anchors, preserves reproducibility and result artifacts, and must
not promote a result into a paper claim without review. Claude independently
reviews derivations and results, issues gate verdicts, identifies overclaims, and
updates paper text only after acceptance. The Principal Investigator owns the
programme, approves assumptions, gates and scope changes, accepts or rejects
verdicts, and authorizes paper updates.
