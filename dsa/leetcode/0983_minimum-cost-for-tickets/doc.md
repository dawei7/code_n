# Minimum Cost For Tickets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 983 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-cost-for-tickets/) |

## Problem Description

### Goal

You plan train travel during one year. The strictly increasing array `days` lists every calendar day on which you will travel, using day numbers from `1` through `365`.

Three passes are available: a 1-day pass costs `costs[0]`, a 7-day pass costs `costs[1]`, and a 30-day pass costs `costs[2]`. A pass covers its stated number of consecutive calendar days, including the purchase day; for example, a 7-day pass starting on day `2` covers days `2` through `8`. Buy any combination of passes and return the minimum total cost that covers every listed travel day.

### Function Contract

**Inputs**

- `days`: a strictly increasing list of $N$ travel days, where $1\le N\le365$ and $1\le\texttt{days[i]}\le365$.
- `costs`: exactly three positive ticket prices, each from $1$ through $1000$, corresponding to durations $1$, $7$, and $30$.

**Return value**

- The minimum number of dollars required to cover every day in `days`.

### Examples

**Example 1**

- Input: `days = [1, 4, 6, 7, 8, 20], costs = [2, 7, 15]`
- Output: `11`
- Explanation: one optimal plan uses 1-day passes for days `1` and `20` plus a 7-day pass covering the middle travel days.

**Example 2**

- Input: `days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs = [2, 7, 15]`
- Output: `17`
- Explanation: a 30-day pass covers days `1` through `30`, and a 1-day pass covers day `31`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Define cost by covered travel prefix:** Let `dp[i]` be the minimum cost covering the first `i` listed travel days. To cover `days[i]`, the last purchase can be a 1-day, 7-day, or 30-day pass. The earlier portion of the plan is then an already solved prefix.

**Maintain coverage boundaries monotonically:** For the current travel day, advance a `week` pointer past every listed day earlier than `days[i] - 6`; those earlier days are not covered by a 7-day pass whose covered interval ends at the current day. Maintain `month` symmetrically using `days[i] - 29`. Because travel days increase, both pointers only move forward over the entire scan.

The three candidates are `dp[i] + costs[0]`, `dp[week] + costs[1]`, and `dp[month] + costs[2]`. Their minimum is `dp[i + 1]`. Every feasible plan has one of these three durations as its final pass, and removing that pass leaves exactly one of the represented optimal prefixes. Conversely, adding each candidate pass covers every travel day after its prefix boundary, so the recurrence considers all and only valid final choices.

#### Complexity detail

The main index and both coverage pointers each advance at most $N$ times, giving $O(N)$ time. The dynamic-programming array stores $N+1$ prefix costs and uses $O(N)$ space.

#### Alternatives and edge cases

- **Calendar-day DP:** Computing a cost for every day from `1` through `365` is simple and effectively constant-bounded here, but it does work on non-travel days and hides the input-sensitive linear structure.
- **Binary search each boundary:** Locating the first covered day independently gives $O(N\log N)$ time and is unnecessary because query boundaries increase.
- **Rescan every prefix:** Recomputing coverage boundaries from index zero for every state is correct but takes $O(N^2)$ time.
- **Sparse travel:** Calendar gaps cost nothing unless a purchased pass happens to span them.
- **Long pass cheaper than short pass:** The recurrence compares prices directly and does not assume longer durations cost more.

</details>
