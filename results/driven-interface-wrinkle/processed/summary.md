# Driven DE-interface Wrinkle — Processed Summary

Downstream of the immutable `raw/` outputs; produced by
`scripts/driven_interface_wrinkle.py` and `scripts/driven_wrinkle_2d.py`.

| Quantity | Value |
|---|---|
| Linear growth rate | `s(k) = -(mu_eff^2 + tau_eff k^2 + kappa_eff k^4)/K` |
| Operating point | `mu_eff^2=-0.02, tau_eff=-0.30, kappa_eff=+1.0, K=1` |
| Finite-k band | TRUE (`0.0225 > -0.02`) |
| `k_star/Lambda` | 0.3873 (cutoff-ward; long-wave needs tuning) |
| `s_max` | +0.0425 |
| Saturation amplitude | ETD1 0.2381, IMEX 0.2389, 2D 0.232 (predict 0.2380) |
| Static EOS `w` | -0.338 (1D), -0.334 (2D); pure-gradient limit -1/3 exactly |
| 15-point scan | band 9/15; long-wave 2/15; cold-DM-like 0/15 (EMPTY) |

The finite-k wrinkle exists and saturates, but its equation of state is DE-like
(`|w| ~ O(1)`), not cold-DM-like. Source CSVs: `raw/driven_dispersion.csv`,
`raw/driven_phase_diagram.csv`, `raw/driven_profile.csv`,
`raw/driven_wrinkle_2d_field.csv`.
