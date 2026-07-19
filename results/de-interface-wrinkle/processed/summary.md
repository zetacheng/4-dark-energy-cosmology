# DE-interface Wrinkle — Processed Summary

Downstream of the immutable `raw/` outputs; produced by
`scripts/de_interface_wrinkle.py`. No raw output was edited.

| Quantity | Lambda=1.0 | Lambda=2.0 |
|---|---|---|
| `K_t = c_2` (gradient coefficient) | +0.1543 (> 0, no ghost) | +0.2609 |
| `c_4` | -0.1196 | -0.1284 |
| `m_sigma / m_dyn` | 2.006 | 1.982 |
| `xi*Lambda = 1/m_sigma` | 2.492 (MICROSCOPIC < 3) | 2.522 |
| QMC vs analytic `Pi_S` max rel. | 4.33e-04 | 5.34e-04 |

Anchor identity `Pi_S - Pi_P = -8 N_mult m^2 L(q^2) < 0` holds. The static
kernel minimum is at `k = 0` (`c_2 > 0`): no finite-k wrinkle. Correlation
length is microscopic at both cutoffs, tracking `m_dyn` rather than a
cutoff-independent long length. Source: `raw/dewrinkle_kernel.csv`,
`raw/dewrinkle_sigma.csv`.
