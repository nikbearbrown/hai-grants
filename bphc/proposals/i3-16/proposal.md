# I3-16: From approved tables to editable, publication-ready charts

Staff should be able to point an agent at an approved table and say, “Show the trend for this audience, using our standards, in the format my team can edit.” The agent suggests the best chart, explains what it can and cannot show, and produces the requested native artifact where tool access allows. A human signs off on both the numbers and the design.

## Initial pilot

Start with BPHC's existing prototype and two recurring figure types: a time series and a comparison across groups. Agree on an approved input schema, source notes, style templates, accessibility expectations, and suppression rules. Use synthetic and approved public aggregate tables first. Prefer editable Excel and PowerPoint outputs for the BPHC pilot, while the underlying skill also supports other tools. Build a portable chart specification so changing the renderer cannot silently change the numerator, denominator, units, or inclusion rules. Figma is useful for editable design; Power BI for filterable reporting; Python for repeatable production. Neither an exported image nor a Figma mockup counts as a native editable Office chart.

Compare current manual formatting with skill-assisted production on matched tables. Reconcile displayed values to the source, independently check rates, and test sorting, rounding, missing and suppressed cells, labels, keyboard navigation where applicable, and whether staff can edit figures without rebuilding them. Measure active editing and review time separately. Treat any unsupported value or disclosure of suppressed data as a blocker. A prototype is not a compatibility claim or release approval.

## Book-based staff training

The [Visualizing Population Data with Agents blueprint](population-visualization-book/) turns the same workflow into a teaching resource. Use an original chapter exercise to teach staff why a chart fits, how to verify source data and suppression, and how to recheck a native editable chart after a change. The prototype works only from finalized, approved aggregate values, not new statistical analysis. Test native Excel and PowerPoint output and test editability in Word if BPHC requires it; confirmed support depends on the authoring environment. The book's planned Blender and game-engine walkthrough is a separate teaching extension, not a condition of the pilot.

## Handoff

Deliver two approved templates, synthetic fixtures with expected outputs, an editability and accuracy checklist, a comparison report, and a brief hands-on staff walkthrough for updating chart mappings and style tokens. The Fellow builds and tests the templates; Nik Bear Brown is the proposed project lead. A designated BPHC owner would approve input definitions, branding, accessibility, and release if selected. Fellow and staff participation are not confirmed.
