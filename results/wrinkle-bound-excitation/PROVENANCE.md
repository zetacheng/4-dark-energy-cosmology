# Wrinkle-bound Dark-excitation Provenance

Source repository `zetacheng/kappa-c2a`, branch `wrinkle-bound-excitation`,
HEAD `17c187df09966e2a89bb73489d5cdd121ade3f21`.

## Raw artifacts (immutable, byte-identical)

| Original path | Destination path | sha256 | Transfer |
|---|---|---|---|
| `results/wrinkle_bound_verdict.txt` | `.../raw/wrinkle_bound_verdict.txt` | `bba9324bde37d0a5b3945669c399369820b7a6ea462f5c99573a021a794b8bdd` | Copied byte-for-byte |
| `results/wrinkle_bound_output.txt` | `.../raw/wrinkle_bound_output.txt` | `e4ca28b3af66f8aa8fc028ebb85ae58b7ff08c2a9ec62875ddf2f55ad5495ee7` | Copied byte-for-byte |
| `results/wrinkle_bound_eigen.csv` | `.../raw/wrinkle_bound_eigen.csv` | `3bad1735b3b8422eaa7b73d0c9d0cd857cdceedb71d62d48a658c13b431f2a0f` | Copied byte-for-byte (CRLF preserved) |
| `results/wrinkle_bound_profile.csv` | `.../raw/wrinkle_bound_profile.csv` | `1babadc6d65b8e1f91ed26ca7b541ba11951f242fe41e287cd96f6557d556f47` | Copied byte-for-byte (CRLF preserved) |
| `results/wrinkle_threshold.csv` | `.../raw/wrinkle_threshold.csv` | `5b17b8e1aad3abc02e45041a4fec62fb9aaa741d295b7d586d469be92231e209` | Copied byte-for-byte (CRLF preserved) |

## Code and derivation

| Original path | Destination path | Transfer |
|---|---|---|
| `scripts/wrinkle_bound_excitation.py` | `scripts/wrinkle_bound_excitation.py` | Output path pointed at `results/wrinkle-bound-excitation/regen/`; physics logic unchanged (no intra-repo imports) |
| `derivation/wrinkle_bound_excitation.md` | `derivations/wrinkle_bound_excitation.md` | Copied byte-for-byte |

Regeneration: `python -m scripts.wrinkle_bound_excitation`, writing to
`results/wrinkle-bound-excitation/regen/` (git-ignored).
