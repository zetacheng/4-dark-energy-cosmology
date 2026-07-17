# Current Handoff

## Current task

Migration of the Paper 4 scientific record from `zetacheng/kappa-c2a` onto
`sync/legacy-de-migration`, complete and pushed for review.

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

**Reviewer verification of this branch** — the next item. An independent
reviewer must check the byte-identity of the migrated artifacts, the verbatim
verdicts in the gate registry, the claim-status/text agreement in the ledger,
and the bare-invocation reproducibility of each script, then issue verdicts;
after that, PI acceptance. Separately, the PI must supply
`paper4_dark_energy_v6_3.tex` (source, figures, bibliography), and Paper 1 must
review the dark-matter framing of the interface gates (cross-repo items in
`MIGRATION.md`).

## Expected Codex output

None pending; the migration is delivered for review.

## Questions for ChatGPT

None.

## Questions for Claude

Independent-review verdicts for `P4-DEWRINKLE-01`, `P4-DRIVEN-01`, `P4-SEA-01`,
`P4-WRINKLE-EXC-01`, and `P4-MONOPOLE-01`, against their pre-registered kill
criteria.

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
