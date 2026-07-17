# Driven DE-interface wrinkle gate — can continuous sea-to-interface energy
injection generate and sustain a finite-wavelength wrinkle that acts as a DM seed?

**Nature of this gate (declared up front).** This is a **driven-dissipative EFT
feasibility test** (a generalized Swift–Hohenberg pattern-formation problem), NOT a
derivation from the committed microscopic action. The previous DE-interface gate
established that the committed action contains **no interface variable and no
sea-coupling term**; therefore every ingredient here (`h`, `Q`, `K`, `mu^2`,
`tau_0`, `kappa`, `lambda`, the feedback `alpha_i`, `beta`, and the dissipative
`K d_t u` itself) is an **introduced EFT/phenomenological quantity**, none derived
from the current action. Result headline is capped accordingly:

    THIS IS A MINIMAL MODEL-ENLARGEMENT TEST, NOT A DERIVATION FROM THE CURRENT ACTION.

No halo/SPARC/RAR/BTFR/relic/CMB/lensing/structure-formation/cosmology; no paper
.tex. Preserve all prior branches (topo-mass-radius, de-interface-wrinkle, ...).

---

## Phase 0 — model-status of every ingredient (mandatory)

| ingredient | status |
|---|---|
| `h(x,t)=H(t)+u` interface field | **phenomenological enlargement** (no interface d.o.f. in the action) |
| `Q_0, delta Q` sea injection | **phenomenological source** (no sea-coupling in the action) |
| `K, mu^2, tau_0, kappa, lambda` | **introduced EFT parameters** (not derived) |
| `alpha_0, alpha_2, alpha_4, beta` | **free feedback parameters** |
| `K d_t u` dissipation | **phenomenological open-system assumption** |

So the strongest achievable outcome is an EFT feasibility statement, explicitly
flagged as a model enlargement.

## Field decomposition and injection law

    h(x,t) = H(t) + u(x,t),  <u>=0 ;  Q = Q_0(t) + delta Q(x,t).

Minimal driven-dissipative equation (Fourier convention `u ~ e^{s t + i k.x}`,
so `Lap -> -k^2`, `Lap^2 -> +k^4`):

    K d_t u = delta Q[u] - mu^2 u + tau_0 Lap u - kappa Lap^2 u - lambda u^3 + eta,
    delta Q[u] = alpha_0 u - alpha_2 Lap u - alpha_4 Lap^2 u + beta u^2 + ...

Combining restoring + injection:

    K d_t u = -mu_eff^2 u + tau_eff Lap u - kappa_eff Lap^2 u + beta u^2 - lambda u^3 + eta,
    mu_eff^2 = mu^2 - alpha_0 ,  tau_eff = tau_0 - alpha_2 ,  kappa_eff = kappa + alpha_4 .

Required signs `K>0, kappa>0, lambda>0` (health); `kappa_eff>0` for UV control.

## Phase 1 — homogeneous background (secondary)

`K dot H = F(Q_0,H,...)`; open-system continuity
`dot rho_int + 3 H_cosm (rho_int + p_int) = Q_0`. A quasi-constant `rho_DE` needs
`Q_0 ~ 3 H_cosm (rho_int + p_int)` (NOT imposed; it is the balance condition). This
background bookkeeping is recorded but not pursued into cosmology.

## Phase 2 — linear wrinkle instability (exact)

Linear growth rate (derived from the Fourier convention above):

    s(k) = -( mu_eff^2 + tau_eff k^2 + kappa_eff k^4 ) / K .

Finite-k band requires `tau_eff < 0, kappa_eff > 0`. Then

    k_star^2 = -tau_eff/(2 kappa_eff),
    s_max    = ( tau_eff^2/(4 kappa_eff) - mu_eff^2 ) / K,
    WRINKLE-FORMATION CONDITION:  tau_eff^2/(4 kappa_eff) > mu_eff^2.

Classification: no band / finite-k band / k=0 phase separation (`tau_eff>0, mu_eff^2<0`)
/ cutoff runaway. Reject as cutoff artifact if `k_star/Lambda > 0.2`; long-wave
target `k_star/Lambda <= 0.1`. Since `k_star ~ sqrt(|tau_eff|/kappa_eff)` is set by
EFT coefficients naturally `O(Lambda)`, `k_star/Lambda <= 0.1` requires
`|tau_eff|/(kappa_eff Lambda^2) <~ 0.02` — a **fine-tuning**.

## Phase 3 — nonlinear saturation

With `-lambda u^3` (`lambda>0`) the band saturates. Single-mode `u=A cos(k_star x)`:
projecting `-lambda u^3` onto the fundamental (`cos^3 = (3/4)cos + (1/4)cos 3`),
balance `K s_max A = (3/4) lambda A^3` gives

    A^2 = 4 K s_max / (3 lambda).

Late-time patterns tested (1D/2D, from noise): stationary periodic wrinkle /
localized lump / sheet / foam / phase separation / roughening / runaway. Report
amplitude and wavelength.

## Phase 5 — energy balance (driven open system)

Free-energy (restoring) functional
`F[u]=Int[ mu^2/2 u^2 + tau_0/2 (grad u)^2 + kappa/2 (Lap u)^2 + lambda/4 u^4 ]`,
`dF/dt = P_sea->wrinkle - P_dissipation`; steady state `<dF/dt>=0`. Require
`E_wrinkle > 0`. If the state lowers total physical energy without a conserved
barrier it is **phase conversion**, not a DM object.

## Phase 6 — effective stress and DM-like test (the decisive discriminator)

For the coarse-grained wrinkle the relativistic-scalar stress tensor of a **static**
pattern (dissipative attractor => no coherent oscillation, `<u_dot>=0`) gives, for a
field varying along one direction,

    rho = (1/2)(grad u)^2 + V,   p = -(1/6)(grad u)^2 - V,
    w = p/rho in [ -1 (V-dominated) , -1/3 (gradient-dominated) ].

Hence a static wrinkle is **DE-like / wall-like (`w<0`, `|w|~O(1)`), NOT cold-DM-like
(`|w|<<1`)**. Cold-DM `w~0` would require coherent kinetic oscillation (a wave
equation `K d_t^2 u`), i.e. a further enlargement — and even then it is speculative.
`c_s^2` for the pattern is `O(1)` (relativistic modes), not `<<1`. This is the
robust physics blocker independent of the tuning question.

## Phase 7 — baryon trapping pilot

Only meaningful with a positive-energy, long-lived, matter-like wrinkle. Two
channels: (i) gravitational coupling to `delta T_00`; (ii) local shift of the
baryon-knot energy in the wrinkle background. `V_b(x)` must have a minimum inside
the wrinkle. With `w<0` the "matter" trapping premise already fails at Phase 6, so
Phase 7 is reported as a pilot only.

## Phase 8 — parameter-space scan

Scan dimensionless `mu_eff^2/Lambda^2, tau_eff/K, kappa_eff Lambda^2/K, lambda/K,
delta Q/(K Lambda)`. Map: flat / long-wave wrinkle / microscopic wrinkle / phase
separation / roughening / runaway. Report the fraction/width satisfying ALL of
`k_star/Lambda<=0.1`, `E_wrinkle>0`, `|w|<<1`, long lifetime — expected to be EMPTY
because `|w|<<1` is never met by a static pattern (Phase 6).

## Regressions

- **No injection** `Q=0` (`alpha_i=0`): `tau_eff=tau_0>0` typically => interface
  flattens (no static nonlinear minimum). Confirms injection is what drives it.
- **No curvature feedback** `alpha_2=alpha_4=0`: homogeneous injection `alpha_0`
  only shifts `mu_eff^2`; with `tau_0>0` no finite-k band => no wrinkle.
- **No bending stiffness** `kappa_eff=0` with `tau_eff<0`: `s(k)` grows unbounded in
  `k` => negative tension runs to the cutoff (UNHEALTHY).
- **Positive tension** `tau_eff>0`: all finite-k modes decay (flat interface stable).
- **No saturation** `lambda=0`: unstable band grows without bound (leaves EFT).
- **Grid/cutoff variation**: `k_star` must be grid- and cutoff-independent (set by
  `tau_eff, kappa_eff`), not tracking `dx` or `Lambda`.

## Pre-registered verdicts

The full list from the task is carried in the solver; exactly one is printed from
the measured `(band, k_star/Lambda, E_wrinkle, w, lifetimes, V_b)`.

**Expected principal verdict.** The EFT robustly forms a finite-k Swift–Hohenberg
wrinkle (when tuned into `tau_eff<0, kappa_eff>0`, condition met), with positive
free energy, but the static pattern's equation of state is `w ~ -1/3..-1` (not
pressureless), so it is DE-like/wall-like, not cold-DM-like — and additionally
`k_star/Lambda<=0.1` needs fine-tuning and nothing is derived from the committed
action:

    DRIVEN WRINKLE EXISTS BUT IS NOT DARK-MATTER-LIKE.

(with the standing caveat DRIVEN WRINKLE EFT IS VIABLE BUT NO MICROSCOPIC
SEA-INTERFACE COUPLING HAS BEEN DERIVED). What is established: a driven interface
CAN pattern-form as an EFT; what is NOT: a pressureless, in-framework, baryon-
trapping cold-DM wrinkle.
