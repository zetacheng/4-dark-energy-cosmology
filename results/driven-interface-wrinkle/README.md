# Driven DE-interface Wrinkle Gate (`P4-DRIVEN-01`)

A driven-dissipative EFT feasibility test (generalized Swift–Hohenberg): can
continuous sea-to-interface injection sustain a finite-wavelength wrinkle that
behaves as a dark-matter seed? It is an EFT model enlargement, not a derivation
from the committed action.

Reproduce with:

```text
python -m scripts.driven_interface_wrinkle
python -m scripts.driven_wrinkle_2d
```

Outputs go to `regen/` (git-ignored); `raw/` is immutable. Operating point and
headline numbers: `config.json`, `processed/summary.md`. Verdict: `verdict.md`
(full text in `raw/driven_verdict.txt`).
