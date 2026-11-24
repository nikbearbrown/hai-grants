# Chart catalogue: choose by question

Start with what the reader needs to do. If the reader needs exact lookup or the evidence is too sparse for a pattern, use a table. Chart names are not instructions to manufacture missing fields.

| Reader task | Chart type | Use when | Avoid or check |
| --- | --- | --- | --- |
| Look up values | Table | Exact numbers, definitions or flags matter. | Do not bury missing/suppressed labels or use an image-only table. |
| Rank or compare categories | Horizontal bar | One quantitative value per category, with meaningful magnitude. | Start bars at zero; sort unless categories have an inherent order. |
| Compare many estimates | Dot plot / Cleveland dot chart | One estimate per category and aligned position saves space. | Label units; add intervals if interpretation depends on precision. |
| Compare subgroups | Grouped bar | Few categories and series with shared units. | Switch to small multiples when labels or comparisons get crowded. |
| Compare two points for each group | Dumbbell / slopegraph | Paired observations with identical units and definitions. | Connections are not trends between unobserved dates; show missing pairs explicitly. |
| Show seasonal or chronological change | Line | Ordered time series with comparable measures. | Preserve actual time spacing; gaps stay gaps. Do not use for unordered categories. |
| Show discrete counts per period | Column | Period totals are discrete and magnitude matters. | Zero baseline; make unequal period lengths explicit. |
| Compare trends at once | Small multiples | Several series need the same reading task. | Shared scales for direct comparisons, or visibly label independent scales. |
| Show distribution | Histogram | Many numeric observations; bins clarify shape. | Check bin sensitivity; normalize density correctly for unequal widths. |
| Show cumulative distribution | ECDF | Percent at or below a value matters. | Explain the upward steps and axes; do not confuse with a time series. |
| Compare spread | Box plot | Groups have enough observations for meaningful quantiles. | Define whiskers and show sample sizes; add points for small samples. |
| Compare distribution shape | Violin or density plot | Smooth shape matters and sample supports it. | Bandwidth can create or erase features; consider dots or box plots when sparse. |
| Show association | Scatterplot | Paired numeric values for each observation. | Address overplotting; show association, not causation. |
| Show dense paired observations | Hexbin | Too many points to read individually. | Clarify whether colors are counts, densities, or another statistic. |
| Show grid patterns | Heatmap | Two categorical dimensions or ordered bins form a matrix. | Include a calibrated legend, use a suitable palette, distinguish missing from zero. |
| Show part-to-whole by group | 100% stacked bar | Categories exhaust a defined whole and shares compare across groups. | Label totals or sample sizes separately; don't use for overlapping categories. |
| Show total and components | Stacked bar | Both total and composition matter and few components exist. | Internal segments lack a common baseline; use grouped bars for exact subgroup comparisons. |
| Show one simple composition | Pie / donut | Very few mutually exclusive categories make up exactly one meaningful whole. | Prefer bars for close values, multiple groups, or negative or overlapping values. |
| Show nested composition | Treemap | Hierarchical share with many leaves; broad proportions are enough. | Area is imprecise; prefer a table or bars for exact comparisons. |
| Explain increases and decreases | Waterfall | Contributions reconcile from a start to an end value. | Verify arithmetic and sign; unrelated changes do not form a waterfall. |
| Compare a metric to target | Bullet chart | Actual, target, and reference ranges share one scale. | Document target basis; don't imply thresholds are precise without evidence. |
| Show uncertainty | Dot and interval / error bars | An estimate has a valid uncertainty interval or other defined range. | Name the interval and method. Do not fabricate intervals or assume overlap answers a significance question. |
| Locate measured places | Symbol map | Location matters; mapped points or totals have a clear spatial reference. | Explain symbol sizing; avoid publishing sensitive locations. |
| Compare geographic rates | Choropleth | Meaningful comparable rates by area, with denominators and geography defined. | Don't shade raw counts by region as if they were rates. Mark suppressed and missing areas. Use bars if geography does not matter. |
| Show movement or transitions | Sankey / alluvial | Flows link stages and widths have verified quantities. | Label losses, units, and differing bases; avoid when links are only categorical. |
| Show relationships | Network diagram | Nodes and edges have defined meanings; topology is the actual question. | Check density; layout distance is not a metric unless explicitly encoded. |
| Show schedule or sequence | Timeline / Gantt | Events or tasks have dates, and duration matters for Gantt. | Mark estimated dates and dependencies; do not imply duration for point events. |

[The Data Visualisation Catalogue](https://datavizcatalogue.com/) is a companion reference for other forms. Prefer the simplest form that answers the specific question and survives the data checks in the skill.
