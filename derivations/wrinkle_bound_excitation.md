# Wrinkle-bound dark-excitation gate — does a driven wrinkle bind a localized
dark state out of an EXISTING microscopic mode that has no localized state on the
flat interface?

**Hypothesis:** Cosmo-sea -> driven DE-interface wrinkle (container) -> wrinkle-
induced spectral well -> localized dark excitation (the trapped mode) -> matter-like
population. Defining property: flat interface has NO localized dark state; the
wrinkled interface has >=1 healthy localized state. The wrinkle is NOT itself the DM
(accepted: its EOS is w~-1/3..-1/2); the TRAPPED MODE is the candidate. No
halo/SPARC/RAR/BTFR/relic/CMB/lensing/cosmology, no paper .tex; preserve all prior
branches.

## Model-status declaration (mandatory)

THIS GATE TESTS WHETHER AN EXISTING MICROSCOPIC MODE BECOMES WRINKLE-BOUND. ANY NEW
CHI FIELD IS AN EFT ENLARGEMENT CONTROL, NOT AN IN-FRAMEWORK DERIVATION.

The committed action has no independent interface field `h` and no sea-interface
coupling (established in the de-interface and driven-interface gates). Consequences:
the wrinkle background `h(x)` is IMPORTED from the accepted driven-interface EFT;
any trapped mode is sought first among fields already present (sigma, pi, omega,
fermion); a new `chi` is a separately labelled control.

## Candidate audit and the derived-coupling question

The wrinkle modifies a mode `X` via `H_X[h] = H_X^flat + Delta H_X[h]`. The
load-bearing question is whether `Delta H_X[h]` is DERIVABLE. There is NO `h*(op)`
term in the committed action, so:

| candidate | flat spectrum | derived coupling to the driven wrinkle `h`? |
|---|---|---|
| A sigma (m_sigma=2 m_dyn) | massive bulk particle | NO `h`-coupling in the action |
| B pi (Goldstone, massless) | gapless continuum | NO; and a massless mode cannot bind an ordinary state below a zero threshold without a gap/guided mechanism |
| C omega (M_omega^2>0) | massive bulk vector | NO `h`-coupling in the action |
| D fermion (mass m_dyn) | gapped continuum, threshold m_dyn | NO `h`-coupling; BUT a spatially-varying CONDENSATE m(x) (a sigma-background) DOES modify the Dirac operator microscopically |
| E chi (new) | set by hand | EFT control only |

**Conclusion of the audit.** For the DRIVEN wrinkle `h` there is NO derived coupling
to any committed mode => `NO IN-FRAMEWORK WRINKLE COUPLING IDENTIFIED` for A-D as
stated. The ONLY microscopically-derivable realization is to identify the "wrinkle"
with a **condensate / constituent-mass modulation** `m(x) = m_dyn - dm*env(x)` (a
sigma-background, which IS in the action). This is a distinct object from the driven
`h` and is flagged as an identification, not a derivation from the driven-interface
gate. Under it, Candidate D (fermion) and A (sigma) acquire a genuine, microscopic
`Delta H`; we compute those as mechanism DEMONSTRATIONS, and `chi` (E) as the EFT
control.

## Flat and wrinkled spectral operators

**Scalar (sigma / chi), Klein-Gordon, 3D radial** (`u = r psi`, l=0):

    -u'' + [ m^2 - U(r) ] u = E^2 u ,   U(r) = wrinkle-induced attractive well.

Flat `U=0`: continuum `E^2 >= m^2`, NO normalizable bound state. Well `U>0`: a
discrete `E_0^2 < m^2` appears once `U_0 R^2` exceeds the 3D s-wave threshold
(~2.7 for a Gaussian well; there IS a finite threshold in 3D, unlike 1D).

**Fermion (Dirac mass-well), squared/SUSY-QM form.** For `H = -i alpha.grad +
beta m(x)`, `H^2 = -grad^2 + m(x)^2 -/+ (mass-gradient term)`, so each chirality
solves a Schrodinger problem

    -chi'' + [ m(x)^2 -/+ m'(x) ] chi = E^2 chi ,   threshold  m_inf^2 = m_dyn^2.

A mass DIP lowers `m(x)^2` -> attractive well -> a fermion level enters the gap
`E_0^2 < m_dyn^2`. Flat `m=const`: no in-gap level. (Direct 1D Dirac diagonalization
is used as the independent cross-check.)

## Coupling derivation

- `chi` (E): `m_chi^2(x) = m_{chi,inf}^2 - g_chi W[h]`, `W[h]` a wrinkle functional
  ((grad h)^2 or h^2); `U(r) = g_chi W[h(r)]`. EFT parameters.
- fermion/sigma (D/A) under the condensate identification: `U(r)` and the mass-dip
  `dm(x)` are set by the condensate modulation amplitude — microscopic, but
  conditional on wrinkle == sigma-background.

## Bound-state criteria (all mandatory)

`0 < E_0^2 < E_th^2`; normalizable, finite grid-independent localization length
`xi_loc = 1/sqrt(m^2 - E_0^2)`; positive norm; `E_0^2 > 0` (no tachyon; `E_0^2<0`
is local condensation, NOT a DM state); robust under box/grid; and the CENTRAL
condition `h -> 0  =>  E_0 -> E_th and localization disappears`.

## Threshold, stability, occupation, EOS

- Critical wrinkle strength `W_crit` (amplitude x width x coupling) for the first
  discrete state; `N_bound(A_h, R_h, k_h)`.
- Lifetime: below-threshold state is spectrally stable vs one-particle escape;
  finite wrinkle domains leak (tunnelling), and the state follows a
  dissolving/driven wrinkle. Classify spectrally-stable / metastable / forced.
- Occupation: distinguish `<X>=0` (no condensate) from `n_localized=0` (no state).
- **EOS of the trapped mode.** A weakly-bound quantum (`E_0 ~ m`, kinetic
  `KE=m-E_0 << m`) is nearly at rest: `w_X = p_X/rho_X ~ KE/m << 1`, `c_s^2<<1` =>
  MATTER-like, unlike the container (`w~-1/3..-1/2`). Separate
  `T = T_wrinkle + T_X`; require the coarse-grained SOURCE to be matter-like:
  `rho_X >> |rho_wrinkle + 3 p_wrinkle|`. Note `rho+3p = rho(1+3w)`: for `w=-1/3`
  the container's active gravitational mass VANISHES (inert), for `w<-1/3` it is
  negative (repulsive) — so the trapped mode must supply/dominate the positive
  matter source.

## Regressions

flat `h=0` -> no state; `A_h->0` -> `E_0 -> E_th`, delocalizes; wrong-sign coupling
(`U -> -U`) -> well becomes a barrier, no state; box/grid convergence of
`(E_0, xi_loc)`; sector regressions (sigma=2m_dyn, fermion threshold m_dyn, omega
pole) recovered on flat background; chi control reproduces the standard finite-well
threshold; injection switch-off -> the state follows the dissolving wrinkle.

## Pre-registered verdicts

Exactly one printed. Given the audit (no derived `h`-coupling to committed modes),
the demonstrations (condensate mass-well binds an EXISTING fermion; chi bindable as
EFT control), and that even a successful trap localizes an existing bulk particle:

**Expected principal verdict:** `WRINKLE-BOUND EXCITATION GATE INCONCLUSIVE: NO
MICROSCOPIC COUPLING BETWEEN THE WRINKLE AND EXISTING MODES HAS BEEN DERIVED` — the
mechanism (attractive well binds a state) is generic and, under the condensate
identification, would localize an EXISTING fermion (matter-like `w_X~0`), while a new
`chi` is bindable only as an EFT enlargement; but no coupling between the accepted
DRIVEN wrinkle and the committed microscopic modes is derivable, so the in-framework
hypothesis is not closed.
