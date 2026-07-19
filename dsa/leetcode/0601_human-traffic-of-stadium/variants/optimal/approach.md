## General
**Remove noncrowded rows first**

Keep only records with `people >= 100`. A below-threshold row must break a qualifying run and should not receive a group.

**Turn consecutive identifiers into a constant key**

Order the crowded rows by `id` and assign `ROW_NUMBER()`. Within a consecutive run, both `id` and row number increase by one, so `id - row_number` stays constant. A missing identifier or filtered-out low-attendance row makes the difference change and starts a new group.

**Measure each run without collapsing its rows**

Use a partition count over the derived group key. Every row retains its original columns while gaining its run length. Filter for counts at least three, then sort the surviving records by visit date.

**Why every returned row belongs to a valid run**

Rows share a group exactly while their crowded identifiers are consecutive. The partition count is therefore the full length of that maximal run. Keeping groups of size at least three includes every member of each qualifying run and excludes both low-attendance rows and shorter crowded segments.

## Complexity detail
For `n` stadium rows, filtering is linear and window ordering/grouping generally costs $O(n \log n)$ time. The windowed relation uses $O(n)$ working space.

## Alternatives and edge cases
- **Lag plus cumulative run starts:** mark a new group whenever the previous crowded identifier is not one less, then cumulatively sum markers; it has the same asymptotic bound.
- **Three self-joins:** detect qualifying triples and union their members, but avoiding omissions and duplicates is more cumbersome.
- **Correlated three-row checks:** can test whether each row lies in a qualifying triple but may rescan the table per row and take $O(n^2)$ time.
- **Exactly 100 people:** qualifies because the threshold is inclusive.
- **Exactly two crowded rows:** do not qualify.
- **Run longer than three:** return every row, not only one triple.
- **Low-attendance row:** breaks consecutive crowded runs.
- **Missing identifier:** also breaks a run.
- **Several separate runs:** return all qualifying runs.
- **Output ordering:** use visit date ascending after filtering.
