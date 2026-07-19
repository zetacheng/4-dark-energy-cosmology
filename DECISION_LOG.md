# Decision Log

This is an append-only record. Do not rewrite or remove earlier decisions; add a superseding entry instead.

## 2026-07-15 — Separate the five papers into five repositories

### Decision

Maintain each of the five papers in its own repository, with this repository dedicated exclusively to Paper 4.

### Reason

Separate repositories make scientific scope, gates, results, reviews, and paper updates independently traceable.

### Evidence

The repository mapping and infrastructure mandate approved by the Principal Investigator.

### Consequences

Material belonging to another paper repository must not be imported here. Cross-paper dependencies must be referenced explicitly rather than merged silently.

### Supersedes

None.

### Related gate

None; infrastructure decision.

### Related branch and files

`main`; repository governance files.

## 2026-07-19 — Import Paper 4 v6.3 source and accept the migration verdict

### Decision

Import the PI-supplied `paper4_dark_energy_v6_3.tex` and accept the migration of
the Paper 4 scientific record from `zetacheng/kappa-c2a`
(`sync/legacy-de-migration`) at its migrated statuses.

### Reason

The migration content was independently verified and found sound; the only
outstanding gap — the paper source — is now closed by the PI supplying v6.3.

### Evidence

`reviews/claude/2026-07-19-de-migration.md` (22 raw artifacts content-identical
to the pinned source; scope held; five verdicts verbatim; claim statuses match
verdicts; scripts run bare; 13 tests pass; anchors live under a driven-dispersion
mutation; imported v6.3 references the same terminated-chain result).

### Consequences

Migrated claims may be cited at their stated statuses. Nothing is `VERIFIED`
(first reviewer record here). `P4-CL-007`'s `kappa_U` input is owned by
`zetacheng/5-topological-sector` (`P5-CL-003`). The open gates remain open; none
blocks the merge.

### Supersedes

None (append-only). Refines the migration recorded in `MIGRATION.md`.

### Related gate

`P4-DEWRINKLE-01`, `P4-DRIVEN-01`, `P4-SEA-01`, `P4-WRINKLE-EXC-01`,
`P4-MONOPOLE-01`.

### Related branch and files

`sync/legacy-de-migration`; `paper/paper4_dark_energy_v6_3.tex`;
`reviews/claude/2026-07-19-de-migration.md`; `CLAIMS.md`; `GATES.md`;
`MIGRATION.md`.
