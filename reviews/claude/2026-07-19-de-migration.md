# Independent Review — Paper 4 migration from `kappa-c2a`

- **Reviewer:** Claude (independent reviewer / discriminator)
- **Date:** 2026-07-19
- **Scribe note:** this record is transcribed faithfully from the reviewer's
  findings; it does not add or alter any verdict.

**Migration reviewed:** `sync/legacy-de-migration` at `ea3c7ff` (plus the v6.3
source import), from `zetacheng/kappa-c2a` branches `de-interface-wrinkle`,
`driven-interface-wrinkle`, `sea-interface-phase-conversion`,
`wrinkle-bound-excitation`.

## Checks performed independently on a clean environment

1. **Artifact integrity.** All 22 raw files across the four gates are
   content-identical to the pinned source branches (SHA-256, line-ending
   normalized).
2. **Scope.** No shared inherited base (`derive_kappa`, `skyrme`, `u3_fierz`,
   `omega_*`, `c6_*`) and no `topo-mass-radius`. `fierz_verify.py` is vendored
   with an explicit ownership note pointing to `3-vector-sector`; no Fierz or
   vector-sector claim is asserted here.
3. **Verdict fidelity.** The five gate verdicts are transcribed verbatim.
4. **Claim–verdict agreement.** Each status matches its gate's pre-registered
   verdict, with the driven and sea gates correctly split into supported and
   unsupported propositions rather than collapsed to a single status.
5. **Executability and liveness.** All four migrated scripts run bare with no
   `PYTHONPATH`. Suite: 13 passed. A production-source mutation of the driven
   dispersion core (`kstar2` denominator `2 → 2.1`) makes the dispersion and
   archive-regeneration anchors FAIL; restored byte-identically. Anchors
   exercise production code, not re-typed constants.
6. **Paper source.** `paper4_dark_energy_v6_3.tex` imported and checked to
   reference the same terminated-chain result the gates record
   (`S_mono = -0.95 ∉ [140,550]`).

## Cross-repo dependency

`P4-MONOPOLE-01` / `P4-CL-007` rests on `P5-CL-003`
(`kappa_U = -17/(1152 pi^2)`, `VERIFIED` in `5-topological-sector`); the
arithmetic `S_mono = 640 kappa_U = -0.95`, outside the pre-registered
`[140,550]` window, is Paper 4's own.

## Disposition

Migration accepted. Statuses stand as migrated; nothing promoted to `VERIFIED`
(first reviewer record here). The gates' verdicts — three
`INCONCLUSIVE`/`FAILED` dark-energy routes, one EFT-level `SUPPORTED` wall
construction, one terminated monopole chain — are recorded faithfully.
