# Gate Registry

Allowed statuses: `PROPOSED`, `SPECIFIED`, `RUNNING`, `PASS`, `FAIL`, `INCONCLUSIVE`, `SUSPENDED`, `RETIRED`.

Every gate below is a migrated legacy record. **No gate has an independent
reviewer verdict in this repository**; each carries `Reviewer verdict: PENDING`.
Kill criteria are transcribed from the source derivations, not invented.

## P4-DEWRINKLE-01 — DE-interface wrinkle

Status: INCONCLUSIVE

### Scientific question

Does the committed microscopic action contain a distinct, healthy,
long-wavelength collective *interface* variable — a conserved Volovik-type
vacuum variable or an interface height `h(x)` — independent of the microscopic
sigma, that could seed dark-energy-interface structure?

### Scope

Phase-0 operator catalog plus the quadratic kernel of the only available
collective scalar (the condensate amplitude), on the shared Euclidean 4-ball
regulator `|p| < Lambda`. No halo/SPARC/RAR/BTFR/relic/CMB/lensing/cosmology; no
paper `.tex`.

### Locked assumptions

Committed microscopic content only (constituent fermion with NJL dynamical mass,
chiral field, massive omega); `m_dyn = 0.20`; cutoffs `Lambda in {1.0, 2.0}`;
`N_mult = 6`. No interface degree of freedom is added.

### Inputs

Legacy branch `de-interface-wrinkle` HEAD `5ee543c9c7c37082c1053f438aa10a4a65ee7234`.

### Analytic anchors

Exact identity `Pi_S - Pi_P = -8 N_mult m^2 L(q^2) < 0`; NJL amplitude mode
`m_sigma = 2 m_dyn`; relativistic O(4) kernel `K_t = c_2`.

### Regression anchors

`tests/test_dark_energy_anchors.py` (`P4-DEWRINKLE-01`): `K_t = c_2 = +0.1543`,
`m_sigma/m_dyn = 2.006`, `xi*Lambda = 2.492` at `Lambda = 1`; archive
regeneration of `dewrinkle_kernel.csv` / `dewrinkle_sigma.csv` within tolerance.

### Kill criterion

Transcribed from `derivations/de_interface_wrinkle.md`: the gate is load-bearing
at Phase 0 — if the current committed action contains no distinct, conserved,
Volovik-type interface collective variable independent of the already-characterized
modes, the pre-registered exit is `INCONCLUSIVE: NO MICROSCOPIC INTERFACE
VARIABLE`. The correlation-length gate reads `xi*Lambda >= 10` PASS /
`3..10` marginal / `< 3` microscopic-fail; a finite-k wrinkle requires `c_2 < 0`
with `c_4 > 0` and `k_star/Lambda <= 0.2`; `K_t > 0` is the no-ghost health gate.

### Required computations

Operator catalog; Volovik/induced-source audit; scalar/pseudoscalar bubble by
QMC and by deterministic quadrature at two cutoffs; `m_sigma`, `xi`.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, tests.

### Result

No distinct interface variable exists: the only collective scalar is the
microscopic sigma (`m_sigma = 2.006 m_dyn`, `xi*Lambda = 2.492 < 3`, MICROSCOPIC);
candidates 2–4 are absent; the induced source couples to the full `epsilon` (no
Volovik self-tuning). Verdict verbatim: `INCONCLUSIVE — NO MICROSCOPIC INTERFACE
VARIABLE HAS BEEN IDENTIFIED`.

### Reviewer verdict

PENDING

### Consequences

The gate cannot close positively or negatively for a wrinkle until an interface
degree of freedom is explicitly added to the microscopic action and re-derived.
The dark-matter framing in the legacy verdict is Paper 1 content (cross-repo).

### Repository branch

`sync/legacy-de-migration`

### Relevant files

`derivations/de_interface_wrinkle.md`; `scripts/de_interface_wrinkle.py`;
`results/de-interface-wrinkle/` (raw `dewrinkle_output.txt`,
`dewrinkle_kernel.csv`, `dewrinkle_sigma.csv`, `dewrinkle_verdict.txt`).

### Migration provenance

`zetacheng/kappa-c2a`, branch `de-interface-wrinkle`, HEAD
`5ee543c9c7c37082c1053f438aa10a4a65ee7234`.

### Date opened

2026-07-17 (migrated legacy record).

### Date closed

Open — INCONCLUSIVE; awaiting an added interface DOF and independent review.

## P4-DRIVEN-01 — Driven DE-interface wrinkle

Status: FAIL

### Scientific question

Can continuous sea-to-interface injection generate and sustain a finite-wavelength
wrinkle that behaves as a positive-energy, matter-like (cold-dark-matter-like)
dark-matter seed?

### Scope

Driven-dissipative EFT feasibility test (generalized Swift–Hohenberg), 1D solver
plus 2D spectral cross-check and a 15-point parameter scan. An EFT model
enlargement, not a derivation from the committed action.

### Locked assumptions

Introduced EFT parameters `h, Q, K, mu^2, tau_0, kappa, lambda, alpha_i, beta`
and dissipation `K d_t u` (none derived). Operating point
`mu_eff^2 = -0.02, tau_eff = -0.30, kappa_eff = +1.0, K = 1, lambda = 1`.

### Inputs

Legacy branch `driven-interface-wrinkle` HEAD `2a80c9db07654c51978891f6bac4a9518ea8a6dd`.

### Analytic anchors

Linear growth rate `s(k) = -(mu_eff^2 + tau_eff k^2 + kappa_eff k^4)/K`;
single-mode saturation `A^2 = 4 K s_max/(3 lambda)`; pure-gradient EOS
`w = -1/3` exactly.

### Regression anchors

`tests/test_dark_energy_anchors.py` (`P4-DRIVEN-01`): `k_star/Lambda = 0.3873`,
`s_max = +0.0425`, `A ~ 0.238` (predicted vs measured), static `w = -0.338`;
cold-DM-like scan fraction `0/15`.

### Kill criterion

Transcribed from `derivations/driven_interface_wrinkle.md`: a finite-k band
requires `tau_eff < 0`, `kappa_eff > 0`, and `tau_eff^2/(4 kappa_eff) > mu_eff^2`;
long-wavelength requires `|tau_eff|/(kappa_eff Lambda^2) <~ 0.02` (a fine-tuning);
the Phase-6 premise is a positive-energy, matter-like wrinkle with `|w| << 1`.
The simultaneous target `{k_star/Lambda <= 0.1, E_wrinkle > 0, |w| << 1,
long-lived}` must be non-empty. Regression sign anchors: no injection
(`tau_eff > 0`) must flatten; `kappa_eff -> 0` with `tau_eff < 0` must run to
cutoff (unhealthy); `lambda = 0` must be unbounded.

### Required computations

Linear dispersion; ETD1 and IMEX-spectral 1D saturation; 2D spectral check;
15-point `(mu_eff^2, tau_eff)` scan; static-pattern stress `(rho, p, w)`.

### Required deliverables

Derivation, exact scripts, immutable outputs, provenance, verdict, tests.

### Result

A finite-k wrinkle forms and saturates (three methods agree, `A ~ 0.238`), but
the Phase-6 premise fails: static EOS `w ~ -1/3..-1/2` (DE-like/wall-like, not
pressureless), cold-DM-like region empty (`0/15`), long-wave needs fine-tuning,
and nothing is derived from the committed action. Verdict verbatim:
`DRIVEN WRINKLE EXISTS BUT IS NOT DARK-MATTER-LIKE`; `MICROSCOPIC / EFT-ONLY /
FAILED`.

### Reviewer verdict

PENDING

### Consequences

The driven interface cannot supply an in-framework cold-dark-matter wrinkle; a
pressureless, in-framework, baryon-trapping wrinkle is not available. The
formation/saturation of the finite-k wrinkle as an EFT is separately recorded
(`P4-CL-002`, `SUPPORTED`). DM framing is Paper 1 content (cross-repo).

### Repository branch

`sync/legacy-de-migration`

### Relevant files

`derivations/driven_interface_wrinkle.md`;
`scripts/driven_interface_wrinkle.py`, `scripts/driven_wrinkle_2d.py`;
`results/driven-interface-wrinkle/`.

### Migration provenance

`zetacheng/kappa-c2a`, branch `driven-interface-wrinkle`, HEAD
`2a80c9db07654c51978891f6bac4a9518ea8a6dd`.

### Date opened

2026-07-17 (migrated legacy record).

### Date closed

2026-07-17 — closed negative for the dark-matter route (Phase-6 premise fails);
EFT-only.

## P4-SEA-01 — Sea-interface phase conversion

Status: INCONCLUSIVE

### Scientific question

Does an explicit higher-dimensional (5D) Sea-interface action support a healthy
advancing Sea→lattice wall whose motion maps to four-dimensional cosmic
expansion, together with a curvature-triggered reverse transition and a regular
black-hole core?

### Scope

5D model-enlargement foundation gate (Phases 0–12), wall units `lambda = v = 1`
and a separate black-hole pilot in `G = M = L = 1`. Not a derivation from the
committed 4D action.

### Locked assumptions

5D mostly-plus signature; two potentials (degenerate double well A and
asymmetric first-order B); Hayward black-hole pilot metric. No cosmology,
information-recovery, or paper language.

### Inputs

Legacy branch `sea-interface-phase-conversion` HEAD `1cd94b5dde72745006b3fec67b40b227fd8eaacb`.

### Analytic anchors

BPS wall tension `sigma = (2 sqrt2/3) sqrt(lambda) v^3 = 0.9428`; core invariants
`R(0) = 12/L^2`, `R_mn R^mn(0) = 36/L^4`, `K(0) = 24/L^4`; exterior deviation
`f - (1 - 2GM/r) = 4 G^2 L^2 M^2/r^4`.

### Regression anchors

`tests/test_dark_energy_anchors.py` (`P4-SEA-01`): `sigma_A = 0.9428`,
`Z_h = 0.943 > 0`, `w_eff ~ -0.997`, symbolic core invariants `(12, 36, 24)`;
archive regeneration of `sea_wall_profile.csv` / `sea_bh_core.csv` within
tolerance.

### Kill criterion

Transcribed from `derivations/sea_interface_phase_conversion.md`: the wall
(Phases 1–3), the `w = -1` 4D source (Phase 5), small leakage (Phase 6), the
finite critical curvature `I_c` / reverse melting (Phase 7), the vanishing
unwinding barrier (Phase 8), energy conservation (Phase 9), and the regular BH
core plus GR exterior (Phases 10–11) must all be constructible; the single
genuine gap is the wall-motion → 4D cosmic-expansion map `a(t)` (Phase 4), which
the minimal action does NOT fix. A negative-mode wall, non-finite tension, a
non-conserved energy ledger, or a divergent core invariant would fail the
foundation. Regression sign anchors: `Delta V = 0 -> v_wall = 0`; `xi = 0 -> no
reverse transition`; `|Phi| > 0 constrained -> E_unwind > 0` (protection holds).

### Required computations

Static phases and wall tension (two potentials, two methods); fluctuation
spectrum; traveling-wall velocity and energy balance; reverse-transition profile
and unwinding barrier; black-hole core invariants (symbolic and numeric),
geodesic completeness, exterior deviation.

### Required deliverables

Derivation, exact scripts, immutable outputs, provenance, verdict, tests.

### Result

9 of 10 sub-gates PASS as an EFT construction (healthy finite-tension wall;
normalizable zero mode, `Z_h > 0`, no negatives; advancing driven wall;
`w_eff ~ -1`; `P_leak/P_in ~ 1e-12`; finite `I_c` reverse transition; vanishing
unwinding barrier on melting; energy conserved into the Sea; regular de Sitter
core, geodesically complete, Schwarzschild exterior). **The tenth sub-gate does
not pass — it is undefined**: the wall-motion → 4D expansion map `a(t)`
(expansion-as-cell-creation, Phase 4) is not fixed by the minimal action (the
binding gap). Verdict verbatim: `HEALTHY ADVANCING WALL EXISTS, BUT ITS MOTION
HAS NOT BEEN DERIVED TO PRODUCE FOUR-DIMENSIONAL COSMIC EXPANSION`.

### Reviewer verdict

PENDING

### Consequences

The Sea-interface construction is viable as an EFT enlargement (`P4-CL-004`,
`SUPPORTED`), but the expansion map remains the binding gap (`P4-CL-005`,
`INCONCLUSIVE`). Nothing about cosmology, dark matter, black-hole observations,
or information recovery is established.

### Repository branch

`sync/legacy-de-migration`

### Relevant files

`derivations/sea_interface_phase_conversion.md`; `scripts/sea_interface.py`,
`scripts/sea_bh_core.py`; `results/sea-interface-phase-conversion/`.

### Migration provenance

`zetacheng/kappa-c2a`, branch `sea-interface-phase-conversion`, HEAD
`1cd94b5dde72745006b3fec67b40b227fd8eaacb`.

### Date opened

2026-07-17 (migrated legacy record).

### Date closed

Open — foundation constructible as an EFT, but the load-bearing expansion map is
undefined (binding gap); awaiting independent review.

## P4-WRINKLE-EXC-01 — Wrinkle-bound dark excitation

Status: INCONCLUSIVE

### Scientific question

Does a driven wrinkle bind a genuinely new localized dark state out of an
existing microscopic mode, through a coupling derived in-framework?

### Scope

Spectral bound-state test: scalar (KG) and fermion (Dirac) in imported wrinkle
backgrounds (Gaussian well, tanh patch, widths `R = 2, 4, 8`), plus an EFT `chi`
control. The driven wrinkle `h` is imported from the accepted driven-interface
EFT.

### Locked assumptions

`m_dyn = 1` units; fermion condensate mass-well `dm = 0.6`, scalar well
`U0 = 0.4`, `R = 4`. Any new `chi` field is an EFT enlargement control, not an
in-framework derivation.

### Inputs

Legacy branch `wrinkle-bound-excitation` HEAD `17c187df09966e2a89bb73489d5cdd121ade3f21`.

### Analytic anchors

Flat thresholds `E_th = m` (scalar), `m_dyn` (fermion); SUSY-QM squared-operator
`-chi'' + [m(x)^2 -/+ m'(x)] chi = E^2 chi`; 3D s-wave finite-well threshold
`U0_crit R^2 ~ 2.8`.

### Regression anchors

`tests/test_dark_energy_anchors.py` (`P4-WRINKLE-EXC-01`): flat `n_localized = 0`;
fermion `E_0 = 0.5589`, scalar `E_0 = 0.9718`; `U0_crit R^2 in {2.79, 2.90,
3.15}`; `w_X ~ 0.028`; archive regeneration of `wrinkle_threshold.csv` within
tolerance.

### Kill criterion

Transcribed from `derivations/wrinkle_bound_excitation.md`: a discrete
`E_0^2 < m^2` must appear once `U_0 R^2` exceeds the finite 3D s-wave geometric
threshold (`~2.7`), be positive-norm and non-tachyonic (`E_0^2 > 0`), and
delocalize as the wrinkle amplitude `A_h -> 0` (`E_0 -> E_th`); a flat interface
and a wrong-sign (barrier) well must bind nothing. In-framework closure requires
a **derived** coupling between the driven wrinkle and a committed microscopic
mode; its absence returns `INCONCLUSIVE`.

### Required computations

Candidate-sector audit; flat localized-state counts; bound eigenvalues and
localization lengths (two methods each); critical-threshold scan; tachyon/norm
checks; wrinkle-off dissolution; trapped-mode EOS.

### Required deliverables

Derivation, exact script, immutable output, provenance, verdict, tests.

### Result

The spectral mechanism is sound (attractive well binds a state above the finite
threshold; scalar and fermion; delocalizes as `A_h -> 0`; absent for flat and
wrong-sign) and the bound mode is matter-like (`w_X ~ 0.03`), but there is **no
derived coupling** between the accepted driven wrinkle and any committed mode:
under a condensate identification a mass-well localizes an *existing* fermion,
and a genuinely new bound state exists only as an EFT `chi`. Verdict verbatim:
`WRINKLE-BOUND EXCITATION GATE INCONCLUSIVE: NO MICROSCOPIC COUPLING BETWEEN THE
WRINKLE AND EXISTING MODES HAS BEEN DERIVED`.

### Reviewer verdict

PENDING

### Consequences

No in-framework wrinkle-only dark excitation is established. The dark-matter
interpretation (occupation-dependent matter-like source, baryon attraction) is
Paper 1 content (cross-repo).

### Repository branch

`sync/legacy-de-migration`

### Relevant files

`derivations/wrinkle_bound_excitation.md`;
`scripts/wrinkle_bound_excitation.py`; `results/wrinkle-bound-excitation/`.

### Migration provenance

`zetacheng/kappa-c2a`, branch `wrinkle-bound-excitation`, HEAD
`17c187df09966e2a89bb73489d5cdd121ade3f21`.

### Date opened

2026-07-17 (migrated legacy record).

### Date closed

Open — INCONCLUSIVE in-framework; awaiting a derived wrinkle-mode coupling and
independent review.

## P4-MONOPOLE-01 — Terminated transmutation/monopole chain

Status: FAIL

### Scientific question

Does the transmutation/monopole chain of Paper 4 v6.3 proceed — i.e. does
`S_mono = 640 * kappa_U` land inside the pre-registered window `[140, 550]`?

### Scope

Arithmetic consequence of the inherited controlled coefficient `kappa_U`; a
closed, negative gate. No new computation is performed in this repository.

### Locked assumptions

`kappa_U = -17/(1152 pi^2)` in the controlled small-`m/Lambda` limit (inherited);
pre-registered acceptance window `[140, 550]` with required value `+0.144`.

### Inputs

`kappa_U` from `P5-CL-003` in `zetacheng/5-topological-sector` (`VERIFIED`
there); Paper 4 v6.3 arithmetic.

### Analytic anchors

`S_mono = 640 * kappa_U = -85/(9 pi^2) = -0.95`.

### Regression anchors

`tests/test_dark_energy_anchors.py` (`P4-MONOPOLE-01`): `640 * (-17/(1152 pi^2))
= -85/(9 pi^2)` and the numeric value `-0.957`, asserted to lie outside
`[140, 550]`.

### Kill criterion

Pre-registered: `S_mono` must lie within the window `[140, 550]`. **This kill
criterion has fired**: `S_mono = -0.95` is outside the window and of opposite
sign (required `+0.144`). The chain terminates.

### Required computations

None beyond the transcribed arithmetic on the inherited `kappa_U`.

### Required deliverables

Claim-ledger entry with the cross-repo dependency named; this registry entry;
regression anchor for the arithmetic and the window test.

### Result

`S_mono = 640 * kappa_U = -85/(9 pi^2) = -0.95`, outside `[140, 550]` and of
opposite sign to the required `+0.144`. The transmutation/monopole chain
terminates. Recorded as `P4-CL-007`, `SUPPORTED` (arithmetic is Paper 4's; the
input is external).

### Reviewer verdict

PENDING

### Consequences

The monopole route is closed, negative. Any revival requires a different
controlled coefficient or a re-registered window, with a new gate.

### Repository branch

`sync/legacy-de-migration`

### Relevant files

`CLAIMS.md` (`P4-CL-007`); `MIGRATION.md` (cross-repo item 4);
`tests/test_dark_energy_anchors.py`.

### Migration provenance

Cross-repository input: `P5-CL-003` in `zetacheng/5-topological-sector`
(`kappa_U = -17/(1152 pi^2)`, `VERIFIED`). Arithmetic is Paper 4 v6.3's.

### Date opened

2026-07-17 (recorded from Paper 4 v6.3).

### Date closed

2026-07-17 — closed negative; the kill-window criterion fired.
