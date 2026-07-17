# Wrinkle-bound Dark-excitation — Processed Summary

Downstream of the immutable `raw/` outputs; produced by
`scripts/wrinkle_bound_excitation.py`.

| Quantity | Value |
|---|---|
| Flat localized-state count (scalar & Dirac) | 0 |
| Fermion bound level (`dm=0.6, R=4`) | `E_0=0.5589 < m_dyn` (SUSY-QM vs direct agree 1e-4) |
| Scalar bound level (`U0=0.4, R=4`) | `E_0=0.9718 < m`, `xi_loc=4.24` |
| Finite-domain (tanh patch) | `E_0=0.8628` (localized) |
| Critical threshold | `U0_crit*R^2 = 2.79 (R=2), 2.90 (R=4), 3.15 (R=8)` |
| Tachyon/norm check | `E_0^2=0.944>0`, positive-norm |
| Wrinkle-off (`A_h->0`) | `E_0^2 -> m^2`, delocalizes (`xi_loc 2.6->7.8`) |
| Trapped-mode EOS | `w_X ~ KE/m = 0.028 << 1` (matter-like) |

The mechanism binds a matter-like state, but no coupling between the driven
wrinkle and a committed mode is derived; a genuinely new bound state is EFT-only.
Source CSVs: `raw/wrinkle_bound_eigen.csv`, `raw/wrinkle_threshold.csv`,
`raw/wrinkle_bound_profile.csv`.
