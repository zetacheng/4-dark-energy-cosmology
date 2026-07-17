# DE-interface wrinkle gate — is there a healthy long-wavelength collective
interface mode that could seed dark-matter structure?

**Scope.** Test the hypothesis: dark energy = approximately uniform equilibrium
interface between an underlying "Cosmo Energy sea" and the 4D lattice world; dark
matter = a NONUNIFORM collective deformation `q(x)=q_0+delta q(x)` (or interface
height/thickness `h(x)`) of that interface — NOT a B=1 skyrmion (that is the
now-reclassified UNIT-WINDING BARYONIC SOLITON GATE, verdict "cutoff-scale lattice
lump", which does NOT test this hypothesis). No halo/SPARC/RAR/BTFR/relic/CMB/
lensing/cosmology, no paper .tex, until this gate closes.

The gate is load-bearing at **Phase 0**: does the *current committed microscopic
action* contain a distinct, conserved, Volovik-type interface collective variable,
independent of the already-characterized microscopic modes? If not, the pre-
registered exit is `INCONCLUSIVE: NO MICROSCOPIC INTERFACE VARIABLE`.

---

## 0. Ontology-to-field translation and the operator catalog

The committed microscopic content (C2a + Fierz + omega branches, sharp Euclidean
4-ball `|p|<Lambda`, constituent mass `m=m_dyn`):

- constituent fermion `psi` with dynamical mass `m` (NJL gap);
- chiral field `U` = phase/orientation of the condensate `<psibar psi>` (pions,
  Goldstone) + amplitude fluctuation `sigma`;
- dynamical isoscalar vector `omega_mu` (Fierz/HS, massive `M_omega^2>0`).

**Every candidate interface variable, evaluated against the required properties
(operator; symmetry; conserved?; independent of the heavy sigma?; what fixes q_0;
how it enters the induced gravitational source):**

| candidate | operator | symmetry | conserved | indep. of sigma | q_0 fixed by | in the action? |
|---|---|---|---|---|---|---|
| (1) condensate amplitude | `q~psibar psi` | chiral (breaks) | NO | **NO — IS sigma** | gap eqn `dV/dm=0` | YES (=sigma) |
| (2) Volovik vacuum var. | conserved `q` (4-form / vac. charge) | shift/none | YES | would be | `rho_grav(q_0)=0` | **NO** |
| (3) cell density / height | `n_cell(x)`, `h(x)` | translation | (lattice #) | — | lattice filling | **NO (would enlarge model)** |
| (4) internal-dim displacement / mu-mode | brane/extra-dim | translation | — | — | — | **NO (no extra dim in action)** |
| (5) other composite already present | `psibar gamma_mu psi` (omega), `psibar i g5 tau psi` (pion) | U(1)_V / chiral | omega: charge; pion: Goldstone | omega massive; pion=phase | dynamics | YES but already characterized |

**Finding.** The only genuine collective *scalar* in the action is candidate (1),
the condensate amplitude, which IS the radial sigma. The distinct Volovik-type
conserved vacuum variable (2), an independent interface height (3), and an
internal-dimension mode (4) are **absent** from the committed action — positing any
of them ENLARGES the model. Candidate (5)'s composites are the already-characterized
massive omega and the Goldstone pion (the tested topological sector), neither an
"interface thickness."

**Regression B (decisive).** Candidate (1) is not independent of sigma; the scalar
two-point (Phase 2 below) gives `m_sigma = 2.01 m_dyn` — the textbook NJL amplitude
mode — so the condensate "interface" candidate is exactly the heavy radial scalar
the task pre-excludes, with `xi Lambda = 1/m_sigma ~ 2.5 < 3` (MICROSCOPIC).

Because no distinct interface collective variable can be derived from the current
action (candidate 1 = the microscopic sigma; 2,3,4 absent), the Phase-0 gate returns
INCONCLUSIVE. We nonetheless carry the analysis through Phases 1-2 (Volovik source
audit + the sigma kernel) to substantiate the exit quantitatively and to deliver the
Paper-4 induced-source audit, and we lay out (and code) the full kernel/finite-k/
nonlinear/stress/trapping machinery so it is ready should an interface variable be
added later.

---

## 1. Equilibrium condition and the induced-source (Volovik / Paper-4) audit

For a hypothetical conserved Volovik variable `q` with vacuum energy density
`epsilon(q)`, the thermodynamically correct GRAVITATING density is the grand
potential (chemical potential `mu=epsilon'(q)` enforced by q-conservation):

    rho_grav(q) = epsilon(q) - q epsilon'(q).

Equilibrium (Minkowski, zero external pressure) is `P = -rho_grav = 0`, i.e.

    rho_grav(q_0) = epsilon(q_0) - q_0 epsilon'(q_0) = 0,

which SELF-TUNES `q_0` with no fine-tuning (Volovik's cosmological-constant
mechanism). Fluctuation curvature: `d rho_grav/dq = -q epsilon''(q)`, so a stable
gravitating fluctuation needs `epsilon''(q_0) != 0` of the right sign.

**Audit of the current framework.** The induced gravitational action here is the
metric dependence of the fermion determinant; the induced vacuum term is the FULL
constituent vacuum energy `epsilon(m,Lambda)` (a genuine cosmological constant of
order `Lambda^4`), with NO conserved `q` and NO Lagrange-multiplier subtraction
enforcing `epsilon - q epsilon'`. Therefore:

    the induced Einstein source couples to the FULL epsilon, not to (epsilon - q epsilon').

Classification (mandatory): **"full vacuum energy sources gravity"** — the
self-tuning deep-sea (Volovik) subtraction is NOT realized microscopically in the
committed action. Per the task this records that the deep-sea explanation FAILS as
currently formulated; and since no distinct conserved collective `q` accompanies it,
the wrinkle-kernel calculation for such a `q` has no microscopic object to act on.

---

## 2. Quadratic kernel of the only available collective scalar (the condensate)

Operator `O_S = psibar psi` (candidate 1). Connected two-point from the fermion
loop (Euclidean, `S=(-i p.g+m)/(p^2+m^2)`), and the pseudoscalar partner
`O_P = psibar i g5 psi`:

    Pi_S(q) = -N_mult Int d^4p/(2pi)^4 Tr[S(p) S(p+q)],
    Pi_P(q) = -N_mult Int d^4p/(2pi)^4 Tr[(i g5)S(p)(i g5)S(p+q)].

Dirac traces (derived): numerators `4[m^2 - p.(p+q)]` (S) and `-4[m^2 + p.(p+q)]`
(P), so the exact identity

    Pi_S(q^2) - Pi_P(q^2) = -8 N_mult m^2 Int 1/[(p^2+m^2)((p+q)^2+m^2)]  < 0

(trace-level numerator identity is +8 m^2; the overall -N_mult loop prefactor flips
the sign), a clean regression anchor. By O(4) Euclidean invariance `Pi_{S,P}` depend only on
`q^2 = omega^2 + k^2`, so the induced kernel is **Lorentz/relativistic**:
`K_t = c_2` (the time and space `q^2`-coefficients are equal) — there is NO
separate slow interface dispersion `K_t << c_2`.

**Gap-subtracted kernel and the sigma pole.** The chiral gap equation fixes the
scalar coupling so the pion is massless: `1/(2G) = Pi_P(0)`. The sigma (amplitude)
inverse propagator is

    K_S(q^2) = Pi_P(0) - Pi_S(q^2) = A_0 + K_t q^2 + c_4 q^4 + ...,

with the pole at `q^2 = -m_sigma^2` (timelike). Measured (m=0.20, 4-ball Lambda=1):
`m_sigma = 2.01 m_dyn`, i.e. the standard NJL `m_sigma = 2 m_dyn`. Hence

    K_t = c_2 > 0 (no ghost),  m_q^2 ~ m_sigma^2 > 0 (homogeneously stable),
    xi = 1/m_sigma,  xi Lambda = 1/(2 m_dyn/Lambda) ~ 2.5 (m=0.2)  < 3  (MICROSCOPIC).

There is no `c_2<0` finite-k wrinkle: the relativistic `K(q^2)=A_0+K_t q^2+...` has
its static minimum at `k=0` (`c_2>0`), no preferred `k_star`. The mode is a healthy
but MICROSCOPIC relativistic scalar (= sigma), not a long-wavelength interface.

---

## 3-8 machinery (ready; not reached because Phase 0 is INCONCLUSIVE)

The health gates (`K_t>0`; `K(0,0)>=0`; `c_4>0` if `c_2<0`), the correlation-length
gate (`xi Lambda >= 10` PASS / `3..10` marginal / `<3` micro-fail), the finite-k
wrinkle test (`k_star^2 = -c_2/2c_4`, `K_min = m_q^2 - c_2^2/4c_4`; controlled iff
`k_star/Lambda <= 0.2, c_4>0`), the nonlinear saturation (`lambda_4>0`), the excess
energy `Int delta rho_wrinkle > 0`, the effective stress `(delta T_00, delta T_ij,
w, c_s^2)` with the pressureless test `|p|<<rho`, and the baryon-trapping potential
`V_b` minimum-inside test — are all specified and coded, and would run on a genuine
interface variable. For the only available scalar (sigma) they return: healthy,
homogeneously stable, no finite-k wrinkle, MICROSCOPIC (`xi Lambda<3`).

## Regressions

- **A (homogeneous limit)** `delta q=0`: recovers the equilibrium background, no
  spurious DM energy (trivial).
- **B (sigma separation)** `m_sigma = 2.01 m_dyn`: the condensate collective scalar
  IS the heavy radial sigma => the long-wavelength interface identification fails.
- **C (cutoff variation)** the scalar kernel / `m_sigma` scale with `m_dyn` (and the
  cutoff), `xi ~ 1/m_sigma` tracks the microscopic scale, not a `Lambda`-independent
  long length.
- **D (no-sea coupling switch)** there is no microscopic sea<->interface coupling in
  the action to switch off — corroborating the absence of an interface sector.
- **E (wrong-sign gradient)** flipping `K_t` (or `c_2`) sign turns the healthy
  relativistic scalar into a ghost/gradient-unstable mode (code-sign anchor).

## Pre-registered verdict (selected)

No distinct microscopic interface variable exists in the committed action (candidate
1 = the microscopic sigma with `m_sigma=2m_dyn, xi Lambda~2.5<3`; candidates 2,3,4
absent — positing them enlarges the model), and the induced source couples to the
full `epsilon` (no Volovik self-tuning). Therefore:

    DE-INTERFACE WRINKLE GATE INCONCLUSIVE:
    NO MICROSCOPIC INTERFACE VARIABLE HAS BEEN IDENTIFIED.

What is established: the only collective scalar the current theory supplies is the
microscopic sigma; the deep-sea self-tuning subtraction is not microscopically
realized. What is NOT established: any long-wavelength, positive-energy, matter-like
collective interface deformation — and therefore nothing about cosmological dark
matter. Closing this gate positively requires ADDING an interface degree of freedom
(a conserved Volovik `q` or an interface height `h`) to the microscopic action and
re-deriving — an explicit model enlargement, flagged as such.
