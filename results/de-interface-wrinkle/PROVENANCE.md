# DE-interface Wrinkle Provenance

Source repository `zetacheng/kappa-c2a`, branch `de-interface-wrinkle`,
HEAD `5ee543c9c7c37082c1053f438aa10a4a65ee7234`.

## Raw artifacts (immutable, byte-identical)

| Original path | Destination path | sha256 | Transfer |
|---|---|---|---|
| `results/dewrinkle_output.txt` | `results/de-interface-wrinkle/raw/dewrinkle_output.txt` | `d9efd9c804c79077dcdc8e15923f6344bc2a8f852c8c0f10b31e9dc6d8707a49` | Copied byte-for-byte |
| `results/dewrinkle_kernel.csv` | `results/de-interface-wrinkle/raw/dewrinkle_kernel.csv` | `17174e875ce80076348df67f3a6f539404edbd9764c38b488adcf3b1a02d3c70` | Copied byte-for-byte (CRLF preserved) |
| `results/dewrinkle_sigma.csv` | `results/de-interface-wrinkle/raw/dewrinkle_sigma.csv` | `12f6f3071983e56544a9499a64136da7309c56989db960f1aed8bad3edee7d46` | Copied byte-for-byte (CRLF preserved) |
| `results/dewrinkle_verdict.txt` | `results/de-interface-wrinkle/raw/dewrinkle_verdict.txt` | `7c0a0989682a433f4167bb131c564837cd0d0f4a0f90b81ee396e07be3528cde` | Copied byte-for-byte |

## Code and derivation

| Original path | Destination path | Transfer |
|---|---|---|
| `scripts/de_interface_wrinkle.py` | `scripts/de_interface_wrinkle.py` | Import rewritten to package-relative (`from .fierz_verify import g, g5`); output path pointed at `results/de-interface-wrinkle/regen/`; physics logic unchanged |
| `fierz_verify.py` | `scripts/fierz_verify.py` | Vendored byte-for-byte as the gamma-matrix dependency. **Owned by `zetacheng/3-vector-sector`** (shared inherited base), retained here only so this gate's script runs |
| `derivation/de_interface_wrinkle.md` | `derivations/de_interface_wrinkle.md` | Copied byte-for-byte |

Regeneration (`python -m scripts.de_interface_wrinkle`) writes to
`results/de-interface-wrinkle/regen/` (git-ignored); it uses a fixed QMC seed
(11) but cross-platform float reduction order makes it match `raw/` only within
tolerance, not byte-for-byte.
