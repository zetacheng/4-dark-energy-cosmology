# Paper 4 Migration

## Source

Repository: `zetacheng/kappa-c2a`

Paper 4 owns the **dark-energy interface** programme: the equilibrium vacuum,
the Sea–interface, its wrinkles, phase conversion, the black-hole reverse
transition, and the terminated transmutation/monopole chain. Its scientific
record is spread across four legacy branches of `kappa-c2a`. This migration
imports **only** each branch's own gate content; the shared inherited base
(C2a, Fierz, omega) is owned by the companion repositories and is not imported.

## Source branches and HEAD commits

| Branch | HEAD commit | Gate |
|---|---|---|
| `de-interface-wrinkle` | `5ee543c9c7c37082c1053f438aa10a4a65ee7234` | DE-interface wrinkle (`P4-DEWRINKLE-01`) |
| `driven-interface-wrinkle` | `2a80c9db07654c51978891f6bac4a9518ea8a6dd` | Driven DE-interface wrinkle (`P4-DRIVEN-01`) |
| `sea-interface-phase-conversion` | `1cd94b5dde72745006b3fec67b40b227fd8eaacb` | Sea-interface phase conversion (`P4-SEA-01`) |
| `wrinkle-bound-excitation` | `17c187df09966e2a89bb73489d5cdd121ade3f21` | Wrinkle-bound dark excitation (`P4-WRINKLE-EXC-01`) |

## Administrative metadata

- [x] source inventory
- [x] commit provenance
- [x] branch provenance
- [x] ownership classification

## Paper source

- [x] latest Paper 4 source imported
- [ ] figures imported
- [x] bibliography imported (inline `thebibliography` in the source)

The PI has supplied `paper4_dark_energy_v6_3.tex`; it is imported under `paper/`
and verified against this branch's record on import (not edited): it references
the same terminated-chain result the gates record — `kappa_U = -0.00149` (exact
`-17/(1152 pi^2)`), `S_mono = 640 kappa_U = -0.95` outside `[140, 550]`, "the
chain terminates by its pre-registered criterion" — and is a self-contained
LaTeX document (`\end{document}` present, braces balanced). The bibliography is
carried inline in the source. **Bundled figures were not supplied**
(`paper/figures/` is empty); that box remains honestly unticked.

## Scientific record

- [x] DE-interface wrinkle gate (derivation, script, outputs, verdict)
- [x] Driven DE-interface wrinkle gate (derivation, scripts, outputs, verdict)
- [x] Sea-interface phase-conversion gate (derivation, scripts, outputs, verdict)
- [x] Wrinkle-bound dark-excitation gate (derivation, script, outputs, verdict)
- [x] scripts (branch-specific only)
- [x] raw outputs (byte-identical, immutable)
- [x] processed outputs
- [x] verdicts (transcribed verbatim)
- [x] claim ledger
- [x] gate registry
- [x] terminated monopole/transmutation chain (`P4-MONOPOLE-01`, cross-repo input)
- [x] failed and inconclusive routes preserved

## Source inventory (per branch)

Each branch carries an identical shared inherited base plus its own gate content.

**Shared inherited base (NOT migrated here — see Cross-paper ownership):**
`derive_kappa_closed.py`, `derive_classes.py`, `aggregate.py`, `p4_gate.py`,
`p6_check.py`, `p7_slope.py`, `production_scan.py`, `pv_check.py`,
`skyrme_fast.py`, `skyrme_full.py`, `skyrme_sign2.py`, `startup_regression.py`,
`fierz_verify.py`, `scripts/c6_gate.py`, `scripts/c_gw_loop.py`,
`scripts/omega_dynamization.py`, `scripts/omega_gates.py`,
`scripts/u3_fierz_gate.py`; `results/RESULTS_C2a.md`,
`results/TaskA_closed_form.md`, `results/TaskB_PV_signcheck.md`,
`closed_form_output.txt`, and all `c6_*`, `omega_*`, `u3_fierz_*`, `c_gw_*`
outputs; `derivation/c6_matching.md`, `derivation/diagram_classes.md`,
`derivation/omega_dynamization.md`, `derivation/omega_gates.md`,
`derivation/u3_fierz.md`.

**Branch-specific content migrated here (Paper 4's own):**

| Branch | Scripts | Derivation | Raw artifacts |
|---|---|---|---|
| `de-interface-wrinkle` | `scripts/de_interface_wrinkle.py` | `derivation/de_interface_wrinkle.md` | `dewrinkle_output.txt`, `dewrinkle_kernel.csv`, `dewrinkle_sigma.csv`, `dewrinkle_verdict.txt` |
| `driven-interface-wrinkle` | `scripts/driven_interface_wrinkle.py`, `scripts/driven_wrinkle_2d.py` | `derivation/driven_interface_wrinkle.md` | `driven_verdict.txt`, `driven_output.txt`, `driven_2d_output.txt`, `driven_dispersion.csv`, `driven_phase_diagram.csv`, `driven_profile.csv`, `driven_wrinkle_2d_field.csv` |
| `sea-interface-phase-conversion` | `scripts/sea_interface.py`, `scripts/sea_bh_core.py` | `derivation/sea_interface_phase_conversion.md` | `sea_interface_verdict.txt`, `sea_interface_output.txt`, `sea_bh_output.txt`, `sea_bh_core.csv`, `sea_reverse_transition.csv`, `sea_wall_profile.csv` |
| `wrinkle-bound-excitation` | `scripts/wrinkle_bound_excitation.py` | `derivation/wrinkle_bound_excitation.md` | `wrinkle_bound_verdict.txt`, `wrinkle_bound_output.txt`, `wrinkle_bound_eigen.csv`, `wrinkle_bound_profile.csv`, `wrinkle_threshold.csv` |

`dewrinkle_verdict.txt` is migrated in addition to the three files named in the
migration brief for `de-interface-wrinkle`: it is the branch's immutable
pre-registered verdict and is required to transcribe the gate verdict verbatim;
omitting it would drop part of the record. This is the single deliberate
addition to the brief's per-gate file lists.

## Vendored shared module

`scripts/de_interface_wrinkle.py` imports the Euclidean gamma matrices `g`, `g5`
from `fierz_verify`. `fierz_verify.py` is part of the **shared inherited base and
is owned by `zetacheng/3-vector-sector`** (the vector-sector / Fierz record). To
let `python -m scripts.de_interface_wrinkle` run without a `PYTHONPATH`, a
byte-identical copy of `fierz_verify.py` is vendored into `scripts/` and its
import is rewritten to a package-relative import. It is retained **only** as the
gamma-matrix / Fierz-basis dependency of the DE-interface-wrinkle gate; no Fierz
or vector-sector claim is asserted in this repository. Owner of record:
`zetacheng/3-vector-sector`.

## Cross-paper ownership and exclusions

- [x] Shared inherited base excluded. The C2a closed form, Fierz pinning, and
  omega dynamization are **already migrated elsewhere**: C2a / closed form / PV
  sign belong to `zetacheng/5-topological-sector` (claims `P5-CL-001/002/003/007`,
  `VERIFIED`); `u3_fierz_*`, `omega_*`, `c6_*`, `c_gw_*` belong to
  `zetacheng/3-vector-sector` (claims `P3-C-001/002/004/005`, `VERIFIED`). They
  are referenced, not re-imported.
- [x] Dark-matter framing excluded from Paper 4 claims. The `de-interface-wrinkle`
  and `wrinkle-bound-excitation` verdicts frame an interface deformation as a
  **dark-matter candidate**. Paper 4 owns only the **dark-energy interface**
  question; galaxy phenomenology, halos, SPARC, RAR, BTFR, relic abundance, and
  any DM-candidate claim belong to Paper 1 (`zetacheng/1-dark-matter-structure`).
  The migrated verdicts are kept verbatim, but their DM content is registered
  below as a **cross-repo item for the PI**, not as a Paper 4 claim.
- [x] `topo-mass-radius` not imported. The unit-winding baryonic soliton gate
  (verdict: "cutoff-scale lattice lump") belongs to `zetacheng/5-topological-sector`
  under `P5-OMEGA-01`. It is noted here as a cross-repo item only.

## Cross-repository items for the PI

1. **DM-candidate content of `de-interface-wrinkle`.** The verdict's statements
   about a long-wavelength collective interface deformation as a *dark-matter*
   seed (and its one-sentence dark-matter statement) belong to Paper 1. Paper 4
   keeps only the dark-energy-interface finding: no distinct microscopic
   interface variable exists in the committed action (`INCONCLUSIVE`).
2. **DM-candidate content of `wrinkle-bound-excitation`.** The verdict's
   "wrinkle-bound dark excitation", occupation-dependent matter-like source, and
   baryon-attraction discussion are Paper 1 dark-matter phenomenology. Paper 4
   keeps only: no derived driven-wrinkle-to-mode coupling exists in-framework
   (`INCONCLUSIVE`).
3. **`topo-mass-radius`** (`kappa-c2a`): unit-winding baryonic soliton, a
   cutoff-scale lattice lump. Owner: `zetacheng/5-topological-sector`
   (`P5-OMEGA-01`). Not migrated here.
4. **Monopole/transmutation input.** `P4-MONOPOLE-01` uses
   `kappa_U = -17/(1152 pi^2)`, whose evidence is `P5-CL-003` in
   `zetacheng/5-topological-sector` (`VERIFIED`). The arithmetic
   `S_mono = 640 kappa_U = -85/(9 pi^2) = -0.95` is Paper 4's; the input is not.

## Validation

- [x] source hashes recorded (sha256; see per-gate `PROVENANCE.md`)
- [x] raw outputs byte-identical to source (sha256 compared)
- [x] no raw outputs edited
- [x] scripts run bare (`python -m scripts.<module>`, no `PYTHONPATH`)
- [x] migrated regression tests pass
- [x] structure tests pass
- [x] Ruff passes
- [x] no claim promoted to `VERIFIED` (no reviewer record exists in this repository)

## Unresolved review items

- The v6.3 source (`paper4_dark_energy_v6_3.tex`, with an inline bibliography) is
  imported; only bundled **figures** were not supplied (`paper/figures/` empty).
- Independent Claude review is **landed and the migration accepted**
  (`reviews/claude/2026-07-19-de-migration.md`, `DECISION_LOG.md` 2026-07-19);
  statuses stand as migrated and no claim is `VERIFIED` (first reviewer record
  here).
- The two DM-candidate cross-repo items (1, 2 above) require Paper 1 ownership
  review.
- `topo-mass-radius` requires Paper 5 ownership handling; not this repository's.

## Migration assessment

`SCIENTIFIC RECORD MIGRATION COMPLETE — v6.3 SOURCE IMPORTED, REVIEW LANDED AND ACCEPTED.`

- Four Paper-4 gate records (derivations, scripts, immutable outputs, verbatim
  verdicts): complete and byte-identical.
- Claim ledger and gate registry: complete; nothing `VERIFIED`.
- Terminated monopole chain: recorded with its cross-repo dependency.
- Paper v6.3 `.tex` and inline bibliography: imported; bundled figures not supplied.
- Independent review: landed and migration accepted 2026-07-19
  (`reviews/claude/2026-07-19-de-migration.md`); nothing promoted to `VERIFIED`.
- DM-candidate framing and `topo-mass-radius`: intentionally not claimed here;
  flagged as cross-repo items.
