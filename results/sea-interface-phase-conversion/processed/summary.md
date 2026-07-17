# Sea-interface Phase-conversion — Processed Summary

Downstream of the immutable `raw/` outputs; produced by
`scripts/sea_interface.py` (Phases 0-9) and `scripts/sea_bh_core.py` (10-12).

| Quantity | Value |
|---|---|
| Wall tension A (BPS/shoot vs relax) | 0.9428 = `(2sqrt2/3)` vs 0.968 (agree) |
| Wall tension B | 0.168 (> 0) |
| Fluctuation spectrum | zero mode ~0 (overlap 1.000), no negatives, `Z_h=0.943>0` |
| Traveling wall | `v_wall = Delta V/(Gamma Z_h)`; `Delta V=0 => v=0` |
| Effective 4D EOS | `w_eff ~ -0.997 ~ -1` (DE-like) |
| Leakage | `P_leak/P_in ~ 2.6e-12` |
| Critical curvature | `I_deg ~ 0.008`, `I_c(spinodal) ~ 0.128` (finite) |
| Unwinding barrier | `E_unwind(0)=1>0`, `-> 0` at `I_c` |
| BH core invariants | `R(0)=12/L^2, R_mn^2(0)=36/L^4, K(0)=24/L^4` (finite) |
| Geodesics | complete (`tau=1.23` finite to a regular de Sitter core) |
| Exterior | `f-(1-2GM/r)=4G^2 L^2 M^2/r^4`, Schwarzschild recovered |

Sub-gate tally: 9/10 PASS as an EFT enlargement; the tenth (wall-motion -> 4D
expansion map) is undefined by the minimal action (the binding gap). Source
CSVs: `raw/sea_wall_profile.csv`, `raw/sea_reverse_transition.csv`,
`raw/sea_bh_core.csv`.
