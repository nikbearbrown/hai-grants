# Visualizing Population Data with Agents

**Book blueprint**
**Subtitle:** From Census Tables and Public Health Charts to Walkable 3D Exhibits

## Purpose and audience

Give readers a population question, an approved table, and a coding agent. Teach them to decide which denominator, geography, comparison, and visual form answer the question; build the figure in their tool of choice; and confirm that a person can read it correctly. “Just formatting” is consequential: a missing footnote, a changed reference group, or a zero substituted for a suppressed value can change the claim.

This is the applied population companion to *Engentic Data Visualization*, not a second general chart catalogue. It uses the same [Data Visualization skill](../data-visualization/), plus a population-specific review checklist and a spatial walkthrough project. Analysts, public health staff, students, and designers are the primary audience. Start in a spreadsheet. Offer reproducible Python and a Kyle Walker–inspired R route for Census and geography labs. No engine is needed for the core statistical lessons.

## How readers learn

Start each chapter with a population question and a small table. Show a plausible misleading answer alongside the corrected chart. Explain the math before the build: what a rate divides by, what an interval means, why a pair of age groups may not be comparable, or what a change of geography means. The reader then asks Claude or Codex for two chart options, chooses one, approves a portable specification, builds in the chosen tool, and independently recomputes or reconciles one displayed value. End with a transfer exercise that changes the source, audience, tool, or geography.

Each lab ships an approved or synthetic fixture, data dictionary, prompt, selected and rejected chart, build source, rendered output, accessible table or text equivalent, and verification receipt. Use original examples. Real public datasets must be versioned with geography, period, definitions, permitted reuse, and exact data provenance. Do not treat a polished output as signoff.

## Part I. Count people before drawing marks

| Chapter | Question and main build | What the reader checks |
| --- | --- | --- |
| 1. Who is counted? | Compare a decennial count with an American Community Survey estimate. Build a plain table and a labeled comparison. | Published universe, geography, period, category definitions, and what an estimate is. No inference from a count that excludes some residents. |
| 2. What is the denominator? | Two fictional areas have different populations. Build counts and rates side by side; contrast crude with supplied age-adjusted rates. | Recompute a rate by hand; distinguish percentages, percentage points, and rates per population unit. Name the standard population when known. Never substitute one rate for another. |
| 3. What can be shown? | Compare reported, zero, missing, unreliable, not applicable, provisional, and suppressed entries. Build a publication table with explicit markers. | Apply the source agency's approved rules, not a made-up universal cutoff. Keep suppressed information out of labels, caches, exports, and totals that reveal it. |

## Part II. Choose a visual for the question

| Chapter | Main builds | Why and what to verify |
| --- | --- | --- |
| 4. Who lives here? | Population pyramids, age profiles, 100% stacked bars and a comparison table. | Counts show size; shares show composition. Name whether shares use the total population or each subgroup. Keep age bands and scale aligned. |
| 5. Where do people live? | Choropleth of a rate, proportional symbols for counts, linked ranked bars or a tile grid. | Join by approved area IDs and boundary vintage. Audit unmatched areas. Show how changing bins or map unit changes the reading; no individual locations. |
| 6. How is the population changing? | Trend lines, indexed series, paired slopes, and small-multiple pyramids. Optional age-period-cohort heatmap. | Preserve gaps and periods. Separate absolute and relative change. A heatmap can display cohort patterns, not identify three independent causal effects. |
| 7. How do groups compare? | Dot plots and dumbbells for absolute gaps; a rate-ratio view with named reference. | Absolute and relative gaps can move in different directions. Keep group definitions, order, comparison, and caveats visible. |
| 8. How sure are we? | Dot-and-interval, trend with an interval band, and optionally a funnel plot using supplied limits. | Name the interval and distinguish survey margins of error, confidence intervals and control limits. Show why ranking noisy small groups is misleading. |
| 9. How long do people live? | Published life-expectancy estimates with intervals and a survival curve from a supplied life table. | Explain a period life table without implying that it follows real individuals; keep data years, place, and uncertainty attached. |
| 10. Where do people move? | An aggregate origin-destination matrix, flow map, and Sankey/alluvial view. | Match units and time window, reconcile subtotals, and refuse to visualize sensitive or unapproved routes. Use the matrix when the map clutters. |
| 11. What should a resident take away? | Natural-frequency graphic, direct-labeled chart, and an accessible companion table. | Test comprehension with the stated audience. Review labels and group order with context; do not use a color ramp that implies hierarchy for unordered groups. |

## Part III. Publish without losing the evidence

12. **Walker-style Census lab.** Use Kyle Walker’s *Analyzing US Census Data* as a reference for Census and ACS workflows, geometry joins, and neighborhood maps. Build an original example with the agent; compare the R route with the canonical portable spec. Check survey vintage, denominator, and boundary vintage. Do not copy the book’s code, prose, or figures into the project. Historical atlas examples are optional and require separate references and rights checks.
13. **Encode a reporting style guide.** Convert a fictional agency guide into a versioned spec: typography, color tokens, labels and group ordering, units, suppression markers, footnotes, source, data period, publication date, geography, and reviewer approval. Use public Health of Boston tables only after source and rights verification. Do not use internal BPHC style rules unless authorized. The agent recommends and maps; deterministic rendering copies approved values; staff sign off.
14. **Round-trip an editable figure.** Build the same chart in a native Office object where supported; distinguish data-bound, editable shapes, and static images. Read chart series, axes, labels, and embedded data back and compare them to approved input. Edit one permissible sample value and show how revalidation catches drift. Check that the data behind an artifact is safe to distribute. Offer Figma, Power BI, Python, and D3 translations without assuming format parity.

## Part IV. Build a population exhibition people can walk through

15. **Block out the world in Blender.** Study the Crystal Palace example’s progression from one bay to repeated bays and its comparison between source drawings and rendered views. Build one original exhibit bay, then reuse it for four stations: population structure, geographic differences, trends, and uncertainty. Separate authored architecture, panels, labels, and data from each other. Keep a departures ledger for any illustrative geometry, omitted categories, or differences between a panel and its source. Do not require or distribute Crystal Palace assets without clearing their rights.
16. **Make it walkable in Godot.** Use Blender for scene and asset building; Godot is the reference engine for interactive navigation. Freeze an approved shared dataset and spec, then load each station by stable ID. Start with one floor, a guided route, manual navigation, a station menu and reset, plus fixed camera views for legibility. Export a Blender camera walkthrough as a separate, non-interactive option and match station order in a flat web or printable version. Provide captions or transcript for any narrated walkthrough. An engine walkthrough and a film are different deliverables.
17. **Port a station to Unity or Unreal.** Teach one equivalent station in each engine as a planned companion lab, not a requirement for the core book. Keep scene units, asset names, station IDs and chart values portable; adapt only the camera, controls, and interface layer. Verify imports and performance in the actual tested versions before claiming support. Compare startup time, frame pacing, legibility, and task completion with the Godot build. Prefer the flat chart when 3D makes values harder to compare.
18. **Capstone: a tour that sustains a claim.** Give a visitor three tasks: identify the larger share for an age band, locate an area with an unavailable estimate, and check whether a visible change refers to an absolute rate or a relative change. Answer the same questions in the 3D exhibit and the flat companion. Check counts, labels, units, omission masks, and source links against the same manifest. Include a clear station index, keyboard-only navigation, reduced-motion/static route, and text/table access without installing an engine.

**3D design rule:** Use the world for spatial context, guided sequencing, and exploration. Use aligned 2D marks and labels for precision. Do not use fake perspective, volume, lighting, or scale to make differences appear larger. Do not turn people into individually locatable marks. Start with synthetic aggregate data and use only release-approved aggregates in any distributed scene, including data packaged but not displayed.

**First vertical slice:** One synthetic population table, one 2D pyramid and one uncertainty table, one Blender bay, one navigable Godot room and one flat equivalent. Check the same two known values at every output and show a suppressed or unavailable row consistently. Expand only when the first room answers the reader’s question and passes navigation and readability checks.

## Role in the BPHC I3-16 proposal

The book and companion skill are proposed training and handoff materials, not evidence that the tool already works with BPHC inputs. The pilot remains focused on finalized, quality-checked, already suppressed aggregate tables; no new statistical analysis or policy decisions in the publishing system. Deliver two repeatable chart templates, initially a trend and a group comparison, and verify native editability in approved Office applications using their actual files. Build on BPHC’s prototype only after access and compatibility review. Use a chapter-based staff exercise to demonstrate a valid chart, an incorrect one, and a round-trip check after editing. **The 3D exhibit is a book extension, not a required grant deliverable.**

## Sources and production

- [Kyle Walker, *Analyzing US Census Data*](https://walker-data.com/census-r/index.html): demographic data and maps reference, not source material to redistribute.
- [Crystal Palace Blender example](https://github.com/nikbearbrown/csye-7270-building-virtual-environments/tree/main/blender/crystal-palace-1851-claude): local README, build files, orthographic views, controls and departures ledger reviewed for the method. No claim that the population exhibit or engine ports have been built.
- [Godot scene import documentation](https://docs.godotengine.org/en/stable/tutorials/assets_pipeline/importing_3d_scenes/available_formats.html): Blender-to-Godot transfer reference. Validate actual asset versions, selected formats, and editor behavior.
- The supplied population-visualization memo informed chart coverage, presentation rules, and the Office round-trip check. Historical assertions, release permissions, and funder-specific claims must be fact-checked before publication. No raw memo, scans, models, or media are included.

**Production order:** Draft original chapters from the blueprint → independent statistical and source fact-check → AI readiness check → revision → separate figures and walkthrough pass → render and round-trip checks → human review → Markdown, web/print, then EPUB or LaTeX as verified. Track native Office artifacts separately. Pin a reader-accessible version of the companion skill and provide an offline starter. A chapter is not done until the chart or scene has been opened, checked, and documented.
