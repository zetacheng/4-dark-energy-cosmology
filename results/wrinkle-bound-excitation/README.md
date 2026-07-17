# Wrinkle-bound Dark-excitation Gate (`P4-WRINKLE-EXC-01`)

Tests whether a driven wrinkle binds a localized dark state out of an existing
mode that has none on the flat interface. The spectral mechanism works, but no
coupling between the accepted driven wrinkle and any committed microscopic mode
is derived; a genuinely new bound state exists only as an EFT enlargement.

Reproduce with:

```text
python -m scripts.wrinkle_bound_excitation
```

Outputs go to `regen/` (git-ignored); `raw/` is immutable. Operating point and
headline numbers: `config.json`, `processed/summary.md`. Verdict: `verdict.md`
(full text in `raw/wrinkle_bound_verdict.txt`). Dark-matter interpretation is
Paper 1 content (see `MIGRATION.md`).
