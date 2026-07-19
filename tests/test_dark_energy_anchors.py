"""Regression anchors for the migrated Paper 4 gates.

Every anchor imports and runs the *real* migrated function — no re-typed
constants stand in for a computation. Each numeric anchor is paired with a
committed mutation assertion showing that a perturbed value falls outside the
tolerance used (the tolerance discriminates). A separate archive-verification
test regenerates a gate and compares it to the immutable ``raw/`` archive with
stated numerical tolerances (not byte-identity: cross-platform float reduction
order makes byte-identity unachievable).

Slow anchors (the QMC DE-interface gate) are marked ``@pytest.mark.slow`` and are
excluded from the default suite; run them with ``make test-slow``.
"""

import csv
import math
from pathlib import Path

import numpy as np
import pytest
import sympy as sp

from scripts.driven_interface_wrinkle import energy_eos, evolve1d, linear
from scripts.sea_bh_core import curvature_invariants_symbolic
from scripts.sea_interface import VA, tension, wall_shoot_bps
from scripts.wrinkle_bound_excitation import critical_U0, dirac_bound, kg_bound

ROOT = Path(__file__).resolve().parents[1]

# Inherited cross-repo input: kappa_U is P5-CL-003 in zetacheng/5-topological-sector.
KAPPA_U = -17.0 / (1152.0 * math.pi**2)


def _rows(path: Path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


# ---------------------------------------------------------------------------
# P4-DRIVEN-01 — driven DE-interface wrinkle
# ---------------------------------------------------------------------------
def test_driven_linear_dispersion_anchor() -> None:
    lp = linear(-0.02, -0.30, 1.0, 1.0)
    assert lp["band"] is True
    assert np.isclose(lp["kstar"], 0.3873, rtol=1e-3, atol=0)
    assert np.isclose(lp["smax"], 0.0425, rtol=1e-3, atol=0)
    # mutation: a 1% shift must leave the tolerance band
    assert not np.isclose(lp["kstar"] * 1.01, 0.3873, rtol=1e-3, atol=0)


def test_driven_saturation_anchor() -> None:
    r = evolve1d(-0.02, -0.30, 1.0, 1.0)
    lp = linear(-0.02, -0.30, 1.0, 1.0)
    a_pred = math.sqrt(4 * 1.0 * lp["smax"] / (3 * 1.0))
    assert np.isclose(float(r["A"]), 0.238, rtol=1e-2, atol=0)
    assert np.isclose(float(r["A"]), a_pred, rtol=2e-2, atol=0)
    # mutation: a 10% shift must leave the tolerance band
    assert not np.isclose(float(r["A"]) * 1.10, 0.238, rtol=1e-2, atol=0)


def test_driven_eos_is_de_like_not_cold_dm() -> None:
    r = evolve1d(-0.02, -0.30, 1.0, 1.0)
    w = float(energy_eos(r)["w"])
    # the recorded FAILED claim: static pattern is DE-like/wall-like, not cold-DM
    assert -0.55 < w < -0.30
    # mutation / discrimination: it is NOT cold-DM-like (|w| << 1)
    assert not (-0.05 < w < 0.05)


# ---------------------------------------------------------------------------
# P4-SEA-01 — sea-interface phase conversion
# ---------------------------------------------------------------------------
def test_sea_wall_tension_anchor() -> None:
    y = np.linspace(-25, 25, 5000)
    phi, y = wall_shoot_bps(1.0, 1.0, y)
    sigma, z_h = tension(phi, y, VA, 0.0)
    assert np.isclose(sigma, 0.9428, rtol=1e-3, atol=0)
    assert np.isclose(sigma, 2 * math.sqrt(2) / 3, rtol=1e-3, atol=0)
    assert z_h > 0
    # mutation: a 1% shift must leave the tolerance band
    assert not np.isclose(sigma * 1.01, 0.9428, rtol=1e-3, atol=0)


def test_sea_bh_core_invariants_are_finite() -> None:
    sy = curvature_invariants_symbolic()
    r, g, m, ell = sy["r"], sy["G"], sy["M"], sy["L"]
    sub = {g: 1, m: 1, ell: 1}
    r0 = sp.limit(sy["R"].subs(sub), r, 0)
    ric2_0 = sp.limit(sy["Ric2"].subs(sub), r, 0)
    kre_0 = sp.limit(sy["Kre"].subs(sub), r, 0)
    assert (r0, ric2_0, kre_0) == (12, 36, 24)
    # mutation: the finite de Sitter values are exact, not off by one
    assert r0 != 13


# ---------------------------------------------------------------------------
# P4-WRINKLE-EXC-01 — wrinkle-bound dark excitation
# ---------------------------------------------------------------------------
def test_wrinkle_flat_has_no_localized_state() -> None:
    flat = kg_bound(1.0, 0.0, 4.0)  # U0 = 0 => flat interface
    assert flat["E0sq"] >= 1.0  # >= m^2, so n_localized = 0


def test_wrinkle_threshold_and_bound_anchors() -> None:
    thresholds = {rr: critical_U0(1.0, rr) * rr**2 for rr in (2.0, 4.0, 8.0)}
    assert np.isclose(thresholds[2.0], 2.79, rtol=1e-2, atol=0)
    assert np.isclose(thresholds[4.0], 2.90, rtol=1e-2, atol=0)
    assert np.isclose(thresholds[8.0], 3.15, rtol=1e-2, atol=0)
    scalar = kg_bound(1.0, 0.4, 4.0)
    fermion = dirac_bound(1.0, 0.6, 4.0)
    assert np.isclose(scalar["E0"], 0.9718, rtol=2e-3, atol=0)
    assert np.isclose(fermion["E0"], 0.5589, rtol=2e-3, atol=0)
    assert scalar["bound"] and fermion["bound"]
    # mutation: a 1% shift must leave the tolerance band
    assert not np.isclose(fermion["E0"] * 1.01, 0.5589, rtol=2e-3, atol=0)


# ---------------------------------------------------------------------------
# P4-MONOPOLE-01 — terminated transmutation/monopole chain
# ---------------------------------------------------------------------------
def test_monopole_chain_terminates_outside_window() -> None:
    s_mono = 640 * KAPPA_U
    # exact form S_mono = -85/(9 pi^2)
    assert np.isclose(s_mono, -85.0 / (9.0 * math.pi**2), rtol=1e-12, atol=0)
    assert np.isclose(s_mono, -0.957, rtol=1e-3, atol=0)
    # the pre-registered kill criterion has fired: outside [140, 550] and wrong sign
    assert not (140.0 <= s_mono <= 550.0)
    assert s_mono < 0
    # mutation: the required value +0.144 is not what the arithmetic gives
    assert not np.isclose(s_mono, 0.144, rtol=1e-2, atol=0)


# ---------------------------------------------------------------------------
# Archive verification (fast): regenerate the driven gate and compare to raw/
# ---------------------------------------------------------------------------
def test_driven_archive_regeneration_matches_raw(tmp_path) -> None:
    """Regenerate the driven gate and compare to the immutable raw archive.

    Tolerance: rtol = 1e-6 on every numeric column, exact match on the ``class``
    label. The dispersion column is analytic and the pattern columns come from a
    fixed-seed deterministic solver, so they reproduce far inside 1e-6 here; the
    tolerance is stated (not byte-identity) because cross-platform float
    reduction order can differ well below it.
    """
    from scripts.driven_interface_wrinkle import main as driven_main

    driven_main(str(tmp_path))
    raw = ROOT / "results" / "driven-interface-wrinkle" / "raw"
    for name in ("driven_dispersion.csv", "driven_phase_diagram.csv", "driven_profile.csv"):
        old = _rows(raw / name)
        new = _rows(tmp_path / name)
        assert len(old) == len(new) and len(new) > 0
        for a, b in zip(old, new):
            for column, old_value in a.items():
                if column == "class":
                    assert a[column] == b[column]
                else:
                    assert np.isclose(
                        float(b[column]), float(old_value), rtol=1e-6, atol=1e-12, equal_nan=True
                    )


def test_driven_archive_tolerance_rejects_one_percent_mutation() -> None:
    """The archive tolerance discriminates: a 1% perturbation is rejected."""
    raw = ROOT / "results" / "driven-interface-wrinkle" / "raw" / "driven_profile.csv"
    values = [float(row["u"]) for row in _rows(raw)]
    baseline = max(abs(v) for v in values)
    assert baseline > 0
    assert not np.isclose(baseline * 1.01, baseline, rtol=1e-6, atol=1e-12, equal_nan=True)


# ---------------------------------------------------------------------------
# Slow anchors: the QMC DE-interface gate (~2-3 min)
# ---------------------------------------------------------------------------
@pytest.mark.slow
def test_de_scalar_kernel_anchor() -> None:
    from scripts.de_interface_wrinkle import scalar_kernel

    r = scalar_kernel(0.20, 1.0)
    assert np.isclose(r["Kt"], 0.1543, rtol=3e-3, atol=0)  # K_t = c_2 > 0, no ghost
    assert np.isclose(r["msig"] / 0.20, 2.006, rtol=3e-3, atol=0)  # NJL m_sigma = 2 m_dyn
    assert np.isclose(r["xiLam"], 2.492, rtol=3e-3, atol=0)  # xi*Lambda < 3 (microscopic)
    assert r["Kt"] > 0
    # mutation: a 5% shift must leave the tolerance band
    assert not np.isclose(r["Kt"] * 1.05, 0.1543, rtol=3e-3, atol=0)


@pytest.mark.slow
def test_de_archive_regeneration_matches_raw(tmp_path) -> None:
    """Regenerate the QMC DE-interface gate and compare to the raw archive.

    Tolerance: rtol = 1e-6 on the fitted sigma columns and rtol = 1e-6 on the QMC
    bubble columns. The fixed default_rng seed makes the QMC reproducible on this
    platform, but the tolerance is stated rather than byte-identity because a
    different BLAS/reduction order shifts the last digits.
    """
    from scripts.de_interface_wrinkle import main as de_main

    de_main(str(tmp_path))
    raw = ROOT / "results" / "de-interface-wrinkle" / "raw"
    for name in ("dewrinkle_kernel.csv", "dewrinkle_sigma.csv"):
        old = _rows(raw / name)
        new = _rows(tmp_path / name)
        assert len(old) == len(new) and len(new) > 0
        for a, b in zip(old, new):
            for column, old_value in a.items():
                assert np.isclose(
                    float(b[column]), float(old_value), rtol=1e-6, atol=1e-12, equal_nan=True
                )
