"""Check reference values for the synthetic chart example; no external packages."""
import csv
from decimal import Decimal
from pathlib import Path

with Path(__file__).with_name("synthetic-uptake.csv").open(newline="") as f:
    rows = list(csv.DictReader(f))
assert len({r["site"] for r in rows}) == len(rows), "Duplicate site"
actual = {}
for r in rows:
    if r["status"] == "reported":
        served, eligible = Decimal(r["served"]), Decimal(r["eligible"])
        assert 0 <= served <= eligible and eligible > 0
        actual[r["site"]] = Decimal(100) * served / eligible
    else:
        assert r["status"] == "not_reported" and not (r["served"] or r["eligible"])
        actual[r["site"]] = None
assert actual == {"A": Decimal("40.0"), "B": Decimal("60.0"), "C": None}
assert sorted((k for k in actual if actual[k] is not None), key=actual.get, reverse=True) == ["B", "A"]
print("PASS: rates, sort order, and not-reported handling")
