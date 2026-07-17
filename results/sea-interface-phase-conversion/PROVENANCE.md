# Sea-interface Phase-conversion Provenance

Source repository `zetacheng/kappa-c2a`, branch `sea-interface-phase-conversion`,
HEAD `1cd94b5dde72745006b3fec67b40b227fd8eaacb`.

## Raw artifacts (immutable, byte-identical)

| Original path | Destination path | sha256 | Transfer |
|---|---|---|---|
| `results/sea_interface_verdict.txt` | `.../raw/sea_interface_verdict.txt` | `5aa6a003a23658675e587350c85a5c69baab74b0bcc7d831952c46a1811716c4` | Copied byte-for-byte |
| `results/sea_interface_output.txt` | `.../raw/sea_interface_output.txt` | `51f14d31285d6f2221516041006f2c35d9dacdb77f0aac8abc3938618c02b786` | Copied byte-for-byte |
| `results/sea_bh_output.txt` | `.../raw/sea_bh_output.txt` | `4c220fbe2b970861d3b8ea9f59673acb5772eed15106695a313d2b7a49e58802` | Copied byte-for-byte |
| `results/sea_bh_core.csv` | `.../raw/sea_bh_core.csv` | `7be7480056a48f1ed2b2bfdd2bc7c9e8a99fac978e1e30d19cd1c5c17a14935a` | Copied byte-for-byte (CRLF preserved) |
| `results/sea_reverse_transition.csv` | `.../raw/sea_reverse_transition.csv` | `7b6a1619b70515784db5d800c3a26b94edb2ed1fc5e58c7a3b1eadff800b26eb` | Copied byte-for-byte (CRLF preserved) |
| `results/sea_wall_profile.csv` | `.../raw/sea_wall_profile.csv` | `e197f88883c64007bf4d65d6e773c72e89c3e70ee30acd2ddf303820f0d192c2` | Copied byte-for-byte (CRLF preserved) |

## Code and derivation

| Original path | Destination path | Transfer |
|---|---|---|
| `scripts/sea_interface.py` | `scripts/sea_interface.py` | Output path pointed at `results/sea-interface-phase-conversion/regen/`; physics logic unchanged (no intra-repo imports) |
| `scripts/sea_bh_core.py` | `scripts/sea_bh_core.py` | Output path pointed at `results/sea-interface-phase-conversion/regen/`; physics logic unchanged |
| `derivation/sea_interface_phase_conversion.md` | `derivations/sea_interface_phase_conversion.md` | Copied byte-for-byte |

Regeneration: `python -m scripts.sea_interface` (Phases 0-9) and
`python -m scripts.sea_bh_core` (Phases 10-12), writing to
`results/sea-interface-phase-conversion/regen/` (git-ignored).
