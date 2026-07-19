# Driven DE-interface Wrinkle Provenance

Source repository `zetacheng/kappa-c2a`, branch `driven-interface-wrinkle`,
HEAD `2a80c9db07654c51978891f6bac4a9518ea8a6dd`.

## Raw artifacts (immutable, byte-identical)

| Original path | Destination path | sha256 | Transfer |
|---|---|---|---|
| `results/driven_verdict.txt` | `.../raw/driven_verdict.txt` | `964d9104d7f86be98968abcf3cd1d966e7951b0abf9ac09c2a0cbe5e4704332a` | Copied byte-for-byte |
| `results/driven_output.txt` | `.../raw/driven_output.txt` | `0c4a246c9f2781ecd462b78ebe3b4e0874e1a364b3e68725d62a8bc75f0e7c60` | Copied byte-for-byte |
| `results/driven_2d_output.txt` | `.../raw/driven_2d_output.txt` | `c4453bfbfca75ed7e76199da1f54393a26639fb779b62d7368e6737eac8dcef4` | Copied byte-for-byte |
| `results/driven_dispersion.csv` | `.../raw/driven_dispersion.csv` | `95b79ef2399b61c248463ba147180a5e3318d5a30257402c856b28fc4fb25a6a` | Copied byte-for-byte (CRLF preserved) |
| `results/driven_phase_diagram.csv` | `.../raw/driven_phase_diagram.csv` | `044bf3d6b38edb8377d33a5a9aea5bff52241cc58e866944b0e54fee41d8383e` | Copied byte-for-byte (CRLF preserved) |
| `results/driven_profile.csv` | `.../raw/driven_profile.csv` | `39aff4bfca2f302599e015a473005803709ac410151413a84626721706c1ba1e` | Copied byte-for-byte (CRLF preserved) |
| `results/driven_wrinkle_2d_field.csv` | `.../raw/driven_wrinkle_2d_field.csv` | `b8cb0261b01fb9e50f1b345387676f0795688949118b816d67d219945d5eb052` | Copied byte-for-byte (CRLF preserved) |

## Code and derivation

| Original path | Destination path | Transfer |
|---|---|---|
| `scripts/driven_interface_wrinkle.py` | `scripts/driven_interface_wrinkle.py` | Output path pointed at `results/driven-interface-wrinkle/regen/`; physics logic unchanged (no intra-repo imports) |
| `scripts/driven_wrinkle_2d.py` | `scripts/driven_wrinkle_2d.py` | Output path pointed at `results/driven-interface-wrinkle/regen/`; physics logic unchanged |
| `derivation/driven_interface_wrinkle.md` | `derivations/driven_interface_wrinkle.md` | Copied byte-for-byte |

Regeneration: `python -m scripts.driven_interface_wrinkle` (1D solver +
15-point scan) and `python -m scripts.driven_wrinkle_2d` (2D check), both
writing to `results/driven-interface-wrinkle/regen/` (git-ignored).
