# Branching Policy

## Branch names

```text
gate/<gate-name>
paper/<paper-version>
review/<review-topic>
fix/<issue>
archive/<retired-route>
```

## Rules

- `main` contains accepted infrastructure and accepted closed gates only.
- Active calculations remain on a gate branch.
- Failed gate branches are preserved.
- Do not squash the history of scientific derivations.
- Prefer conventional commits.
- Tags mark accepted scientific milestones.
- One branch represents one scientific gate or one paper-edit task.
