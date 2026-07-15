# Result Schema

## Immutability and provenance

Raw outputs are immutable: never edit, normalize, or replace them manually. Re-runs produce new artifacts. Processed results must identify the exact processing script and commit, raw input paths and checksums, configuration, branch, execution date, and environment.

Every result directory must include:

- `README.md` describing the gate, operating point, regulator, cutoff, normalization, seeds, and status;
- a machine-readable configuration, normally `config.json`;
- raw output;
- a processed table;
- a reviewer-facing verdict;
- the producing commit hash;
- the branch name;
- the execution date;
- environment information.

## Recommended directory

```text
results/<gate-id>/
  README.md
  config.json
  raw/
  processed/
  figures/
  verdict.md
  environment.txt
```

The result `README.md` must list the exact command used and map each processed artifact to its script and raw inputs. Failed and inconclusive results remain stored.
