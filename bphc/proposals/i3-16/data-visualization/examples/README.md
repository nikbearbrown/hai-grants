# Synthetic example: compare uptake across three service sites

**Question:** Which sites have the highest share of eligible visitors using a service? The input is a fictional, approved aggregate table. Do not use this example as real program data.

**Recommendation:** Horizontal bars for the comparable rates at Sites A and B, with denominator labels. Keep C in an adjacent accessible table and label it “not reported,” without a zero-length bar. A table alone is the simpler alternative when readers need precise counts. Do not chart counts alone: the sites have different denominators.

**Portable specification:** x = served / eligible × 100, domain 0–100 percent; y = site; sort known rates descending; format one decimal place; denominator next to each known value. Do not render or infer an unavailable value or total. Subtitle: “Share of eligible visitors served.” Source note: “Synthetic training fixture.” Text alternative: “Site B served 60.0% (30 of 50); Site A served 40.0% (48 of 120); Site C was not reported.” Reuse the same specification in any tool.

Run `python3 examples/check_fixture.py` from the skill folder to verify the reference calculations before rendering. This does not test a renderer.
