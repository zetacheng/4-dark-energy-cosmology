# Sea–Interface phase-conversion foundation gate — minimal 5D action for a
space-creating advancing wall and a curvature-triggered reverse transition with a
regular black-hole core.

**Model status (declared).**

THIS IS A HIGHER-DIMENSIONAL SEA–INTERFACE MODEL-ENLARGEMENT TEST, NOT A DERIVATION
FROM THE CURRENT FOUR-DIMENSIONAL ACTION.

The committed 4D action contains no Sea phase, no extra coordinate, no phase
boundary, no bulk-to-wall flux, and no inverse high-curvature transition. All prior
branch results (positive and negative) are preserved and are NOT reinterpreted as
having derived this action. No SPARC/halo/relic/CMB/lensing/BH-phenomenology/
information-recovery/paper language; stop at the foundation verdict.

## Phase 0 — conventions and dimensions

1. metric signature mostly-plus `(-,+,+,+,+)` in 5D (`eta_{MN}=diag(-1,1,1,1,1)`).
2. coordinates `x^M=(x^mu, y)`, `mu=0..3`, `y` the extra (bulk) direction.
3. dimensions (natural units, [mass]=1): in 5D `[S]=0`, `d^5x=[-5]` => `[Phi]=3/2`,
   `[V]=5`, `[lambda]=5-4*(3/2)=... ]` — with `V=(lambda/4)(Phi^2-v^2)^2`,
   `[lambda]+2[Phi]... => [lambda]=5-4[Phi]... ` we keep `lambda` dimensionful; `[v]=[Phi]=3/2`;
   `[M_5^3]=3 => [M_5]=1`; Yukawa `[Y]=5-4-3/2-3/2=-1`... in practice we work in
   dimensionless wall units (set `lambda=v=1`, measure `y` in `1/(sqrt(lambda)v)`)
   and report the BH pilot in gravitational units — the two are NOT mixed.
4. wall tension `sigma_wall = int dy [ (1/2)(Phi_0')^2 + V(Phi_0) - V_ref ]`
   `= int dy (Phi_0')^2` on the BPS-degenerate wall.
5. Sea phase `Phi=Phi_Sea` (symmetric/false or `Phi~0`), lattice phase
   `Phi=Phi_lattice` (broken/true, `Phi=v`); the condensate `|Phi|` is the order
   parameter (lattice) that melts (`->0`) in the Sea.
6. positive bulk-to-wall flow `T^{y0}_Sea > 0`: energy flowing from the bulk (`+y`)
   into the wall, converting Sea->lattice.
7. curvature: `R_5` Ricci scalar; invariants `R`, `R_{MN}R^{MN}`,
   `K=R_{MNRS}R^{MNRS}` (Kretschmann) — `K` is used because `R=0` on a Schwarzschild
   exterior while tidal curvature is nonzero.
8. fifth dimension effectively SEMI-INFINITE: Sea at `y->-inf`, lattice at `y->+inf`.

## Phase 1 — static phases and wall

Potentials tested: A tilted double well `V=(lambda/4)(Phi^2-v^2)^2 + eps Phi`;
B asymmetric first-order `V=a Phi^2 - b Phi^3 + c Phi^4` (`a,b,c>0`, a false
`Phi=0` and true `Phi=Phi_+` vacuum with a barrier). Two locally stable phases
require `V''(Phi_i)>0` at two minima with a barrier between; map that region.

**Degenerate (BPS) wall** (`eps=0`, potential A): `Phi_0 = v tanh(k y)`,
`k=v sqrt(lambda/2)`, `sigma = int (Phi_0')^2 dy = (2 sqrt2/3) sqrt(lambda) v^3 > 0`.
Gates: `sigma>0`, `int (Phi_0')^2 < inf`, and the only non-positive fluctuation mode
is the translational zero mode. Solved two ways (shooting + relaxation).

## Phase 2 — wall fluctuation spectrum

`H_wall = -d_y^2 + V''(Phi_0(y))` (with `+xi_5 R_5` when curvature is on). For the
`tanh` kink this is the Poeschl-Teller operator: a normalizable zero mode
`psi_0 ~ Phi_0'` (no negative modes => healthy), a bound shape/thickness mode, and a
continuum above `m_Sea^2=V''(Phi_vac)`. `Z_h = int (Phi_0')^2 > 0` (positive kinetic
norm of the interface). Classify healthy / metastable-bubble / tachyonic /
non-normalizable.

## Phase 3 — driven traveling wall

Formulation A (honest): conserved 5D stress `nabla_M T^{MN}_total=0` with a Sea flux
`T^{y0}_Sea!=0`; the wall energy balance follows from conservation, not an added
non-conserved 4D source. Formulation B (phenomenological, labelled): damped
`Box_5 Phi + Gamma_Phi u.d Phi - V'(Phi)=0`; traveling ansatz
`Phi(y-v t)`. Multiplying the traveling-wave equation by `Phi'` and integrating
gives the STEADY velocity from energy balance:

    Gamma v int (Phi')^2 = Delta V   =>   v_wall = Delta V / (Gamma Z_h),

i.e. the vacuum-energy difference `Delta V = V(Phi_Sea)-V(Phi_lattice)` drives the
wall against friction `Gamma`. Energy balance `P_in = P_cell + P_diss + dE_wall/dt`;
at steady state `dE_wall/dt=0` (fixed profile), `P_in = Delta V * v * A`,
`P_diss = Gamma v^2 Z_h A`. Stable advancing wall = fixed comoving profile, fixed
thickness, slowly-varying `v`, no runaway heating, no growing shape mode.

## Phase 4 — cell-creation bookkeeping and the expansion map

`dot N_cell = A_wall v_wall n_cell^{(5)}`; `P_cell = eps_cell dot N_cell`
(definable). The map `a(t)=a[h_0(t)]` from wall displacement `h_0(t)` to the 4D
scale factor is NOT fixed by the minimal action: converting bulk volume at the wall
defines a cell-creation RATE, but whether that manifests as 3-space dilation `a(t)`
or as time-slice creation requires an extra tiling/induced-metric assumption
(brane-cosmology warp, or a cell->3-volume rule). We therefore record: the
bookkeeping `dot N`, `P_cell` are defined; the `a(t)` map is NOT uniquely fixed =>
classify ADVANCING WALL EXISTS, BUT EXPANSION-AS-CELL-CREATION IS NOT YET DEFINED
(illustrated under a stated brane-induced-metric assumption, flagged as an add-on).

## Phase 5 — effective 4D stress tensor

`T_{mu nu}^eff = int dy T_{mu nu}^{(5)}`. A codim-1 wall filling 4D spacetime (a
3-brane) integrates to `T_{mu nu}^eff = -sigma_wall g_{mu nu} + delta T` (isotropic
tension in all four worldvolume directions) => `w_eff = -1` at leading order
(DE-like), with kinetic/flux residual `|delta T| ~ O(v^2) sigma << sigma` for a slow
wall. Separate: (1) homogeneous vacuum, (2) wall tension (w=-1), (3) wall kinetic,
(4) flux, (5) particle/KK production, (6) residual excitations.

## Phase 6 — leakage

Adiabatic (thick, slowly-moving) wall radiates exponentially little: scalar
radiation, bound/continuum wall modes, fermion pairs (if `2 m_f < ` gap), KK modes,
dark radiation, anisotropic stress, wall-position ripples, worldvolume Lorentz
violation. Target `P_leak/P_in << 1`, computed not assumed; a thick smooth wall with
`v<<1` gives `P_leak/P_in ~ exp(-c/(v * thickness * m_gap))`.

## Phase 7 — curvature-triggered reverse transition

`V_eff(Phi; I) = V(Phi) + (1/2) xi_5 I Phi^2 + Delta V_density(Phi; rho)`, `I` a
curvature invariant (use `K=R_{MNRS}^2`, since `R=0` outside Schwarzschild). The
`xi_5 I Phi^2` term raises the lattice (`Phi!=0`) energy relative to the Sea
(`Phi~0`). Increasing `I`: (1) lattice minimum becomes metastable when
`V_eff(Phi_lat) > V_eff(Phi_Sea)` (`I = I_deg`); (2) the barrier disappears
(spinodal) at `I_c` where `V_eff''` at the lattice side vanishes; (3) Sea preferred.
Requirement: `Phi_lattice -> Phi_Sea` continuously or via controlled first-order
BEFORE any invariant diverges — for Schwarzschild `K=48 G^2 M^2/r^6 -> inf` as
`r->0`, so `K` crosses `I_c` at a finite `r_melt>0`, melting the core condensate.

## Phase 8 — topological unwinding

Winding is protected only on the vacuum manifold `|Phi|=v_eff`. Unwinding requires a
path `U_s(x)` through `|Phi|=0`; the barrier `E_unwind ~ (potential barrier) x
(core volume) ~ v_eff^4`-type. As the condensate melts (`v_eff(I) -> 0` for
`I -> I_c`), `E_unwind(I) -> 0`. Require `E_unwind(0)>0`, `E_unwind(I_c)->0`
(winding decays once the condensate melts) — else the reverse interpretation fails.

## Phase 9 — energy return to the Sea

Reverse flux `T^{0y}_{lattice->Sea}` with full `nabla_M T^{MN}_total=0`. Local
ledger `Delta E_4D + Delta E_wall + Delta E_Sea + E_rad = 0`: melted 4D matter energy
is TRANSFERRED (bulk Sea + wall + emitted modes), not destroyed. All channels
reported.

## Phase 10-11 — regular black-hole core pilot and exterior

Static spherical `ds^2=-f dt^2 + dr^2/f + r^2 dOmega^2`, `f=1-2Gm(r)/r`,
`m(r)=4pi int_0^r r'^2 rho_eff dr'`. Core in Sea phase (`Phi(0)->Phi_Sea`, melted)
=> finite `rho_eff(0)=rho_Sea` (de Sitter core) => `m(r) ~ (4pi/3) rho_Sea r^3`,
`f ~ 1 - (8pi G rho_Sea/3) r^2` (regular de Sitter core). Concretely the Hayward form
`f = 1 - 2GM r^2/(r^3 + 2GM L^2)` realizes this: `f(0)=1-r^2/L^2` (de Sitter),
`f(inf)=1-2GM/r + O(1/r^4)` (Schwarzschild). Regular-core gates: `rho(0)<inf`,
`R(0)<inf`, `R_{mu nu}^2(0)<inf`, `K(0)<inf` (all finite); radial geodesics extend
through `r=0` (de Sitter core geodesically complete). Curvature invariants by
symbolic algebra AND numeric. Exterior `f = 1 - 2GM/r + O(r^{-2-delta})`,
`Phi->Phi_lattice`; report the leading correction.

## Phase 12 — information bookkeeping

ENERGY TRANSFER IS TRACKED; QUANTUM INFORMATION RECOVERY IS NOT ESTABLISHED. We
track energy channels (bulk Sea, wall d.o.f., outgoing radiation, inaccessible Sea
microstates) only; no unitarity/paradox claim.

## Regressions

degenerate `Delta V=0` -> static translational wall; no Sea flux `T^{y0}=0` -> wall
does not steadily advance unless `Delta V!=0` drives it; excess flux -> `v` rises
then wall destabilizes past a limit; no curvature coupling `xi_5=0` & no
`Delta V_density` -> no reverse transition (unless density alone triggers it);
wrong-sign `xi_5` -> phase boundary shifts the analytically-predicted way; constrain
`|Phi|>0` -> unwinding fails; low-curvature exterior -> lattice phase + ordinary 4D
EFT recovered.

## Pre-registered verdicts

Exactly one printed. Expectation: the wall (Phase 1-3), its `w=-1` 4D source
(Phase 5), small leakage (Phase 6), the finite critical curvature `I_c`/reverse
melting (Phase 7), the vanishing unwinding barrier (Phase 8), energy conservation
(Phase 9), and the regular BH core + GR exterior (Phase 10-11) are all
CONSTRUCTIBLE and pass as an EFT enlargement; the single genuine gap is the
wall-motion -> 4D cosmic-expansion map `a(t)` (Phase 4), which the minimal action
does NOT fix. If that gap binds, the honest verdict is HEALTHY ADVANCING WALL
EXISTS, BUT ITS MOTION HAS NOT BEEN DERIVED TO PRODUCE FOUR-DIMENSIONAL COSMIC
EXPANSION (with the reverse-transition + regular-core successes documented).
