## General
**Define cost by covered travel prefix:** Let `dp[i]` be the minimum cost covering the first `i` listed travel days. To cover `days[i]`, the last purchase can be a 1-day, 7-day, or 30-day pass. The earlier portion of the plan is then an already solved prefix.

**Maintain coverage boundaries monotonically:** For the current travel day, advance a `week` pointer past every listed day earlier than `days[i] - 6`; those earlier days are not covered by a 7-day pass whose covered interval ends at the current day. Maintain `month` symmetrically using `days[i] - 29`. Because travel days increase, both pointers only move forward over the entire scan.

The three candidates are `dp[i] + costs[0]`, `dp[week] + costs[1]`, and `dp[month] + costs[2]`. Their minimum is `dp[i + 1]`. Every feasible plan has one of these three durations as its final pass, and removing that pass leaves exactly one of the represented optimal prefixes. Conversely, adding each candidate pass covers every travel day after its prefix boundary, so the recurrence considers all and only valid final choices.

## Complexity detail
The main index and both coverage pointers each advance at most $N$ times, giving $O(N)$ time. The dynamic-programming array stores $N+1$ prefix costs and uses $O(N)$ space.

## Alternatives and edge cases
- **Calendar-day DP:** Computing a cost for every day from `1` through `365` is simple and effectively constant-bounded here, but it does work on non-travel days and hides the input-sensitive linear structure.
- **Binary search each boundary:** Locating the first covered day independently gives $O(N\log N)$ time and is unnecessary because query boundaries increase.
- **Rescan every prefix:** Recomputing coverage boundaries from index zero for every state is correct but takes $O(N^2)$ time.
- **Sparse travel:** Calendar gaps cost nothing unless a purchased pass happens to span them.
- **Long pass cheaper than short pass:** The recurrence compares prices directly and does not assume longer durations cost more.
