# Results

Raw outputs are immutable and must never be edited manually. Processed results must contain provenance identifying the processing script, its commit, the exact raw input, configuration, branch, date, and environment.

Every result directory must include:

- `README.md`;
- configuration;
- raw output;
- processed table;
- verdict;
- commit hash;
- branch;
- date;
- environment information.

Recommended layout:

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

Use the shared `raw/`, `processed/`, and `figures/` directories only for migration staging or repository-level indexes; gate artifacts should use the layout above.
