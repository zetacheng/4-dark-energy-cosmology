# DE-interface Wrinkle Gate (`P4-DEWRINKLE-01`)

Tests whether the committed microscopic action contains a healthy
long-wavelength collective *interface* variable (a Volovik vacuum variable or an
interface height) distinct from the already-characterized modes. Phase-0 exit:
none exists — the only collective scalar is the microscopic sigma.

Reproduce with:

```text
python -m scripts.de_interface_wrinkle
```

Outputs are written to `regen/` (git-ignored); `raw/` is the immutable archive.
Operating point and headline numbers: `config.json`, `processed/summary.md`.
Verdict: `verdict.md` (full text in `raw/dewrinkle_verdict.txt`). Dark-matter
framing in the legacy verdict is Paper 1 content (see `MIGRATION.md`).
