## General

The task counts strings rather than checking one string. At every day, the next character can be present, absent, or late, but eligibility depends on two pieces of history:

- whether an absence has already been used;
- how many consecutive late days end the current prefix.

The memoized state `dfs(i, j, k)` captures exactly that information:

- `i` is the number of days already filled;
- `j` is the number of absences used, restricted to zero or one;
- `k` is the trailing consecutive-late count, restricted to zero, one, or two.

It returns the number of eligible completions from day `i` through day `n - 1`.

**Base case.** If `i >= n`, all positions have been filled without violating either rule. There is exactly one completion—the constructed record itself—so the function returns one.

**Append an absence only when none has been used.** If `j == 0`, the branch:

`dfs(i + 1, j + 1, 0)`

places `A`. It increases the total absence count to one and resets the late streak because an absence is not late.

When `j == 1`, this branch is omitted. A second absence would make the total not strictly fewer than two.

**Append a late day only when the current streak is below two.** If `k < 2`, the branch:

`dfs(i + 1, j, k + 1)`

places `L`. It preserves the absence count and extends the trailing run.

When `k == 2`, adding another late day would create `LLL`, so that branch is omitted.

**A present day is always legal.** The branch:

`dfs(i + 1, j, 0)`

places `P`. It preserves the absence count and resets the trailing late streak.

The answers of all legal next-character branches are added because they begin with different characters and therefore describe disjoint sets of records.

For `n = 1` from state `(0,0,0)`, the three branches generate `A`, `L`, and `P`. Each reaches the base case, so the answer is three.

For `n = 2`, all nine length-two combinations would exist without rules. Only `AA` is forbidden; no string of length two can contain `LLL`. The recurrence suppresses the second-absence branch after one `A` and returns eight.

**Why only the trailing late count matters.** A late streak that ended earlier can never become consecutive with future late days because an `A` or `P` broke it. If an earlier streak reached three, the branch would already have been prevented. Therefore the current suffix length is the complete information needed about lateness.

**Why `j` needs only two values.** States with two absences are invalid and never entered. The exact locations of zero or one earlier absence do not affect future choices; only whether the one allowed absence remains available matters.

**Why memoization changes exponential enumeration into linear state work.** Many different prefixes lead to the same `(i, j, k)`. For example, several valid prefixes of length ten may have one absence and end in no late days. Their possible suffixes are identical. `@cache` computes that completion count once.

There are only six history combinations for each day: two absence counts times three trailing-late counts.

**Apply the modulus within each state.** Counts grow exponentially with `n`. Returning `ans % mod` keeps cached values bounded while preserving the final result modulo $10^9+7$, because modular addition is compatible with ordinary addition.

**Why every counted record is valid.** The recurrence never adds a second absence or a third consecutive late. Present/absence resets are handled correctly. Reaching day `n` therefore certifies both conditions.

**Why every valid record is counted.** Read any eligible record left to right. At each position, its character corresponds to one recurrence branch. Eligibility guarantees that branch's guard is satisfied. Following these choices reaches the base case. Different records differ at some branch, so each is counted exactly once.

After the top-level result, `dfs.cache_clear()` releases memoized states.

## Complexity detail

There are at most $n\cdot 2\cdot 3=O(n)$ states, each performing at most three constant-time transitions. Time is $O(n)$.

The exact implementation stores $O(n)$ cached states and may use $O(n)$ recursive stack depth. Therefore its actual auxiliary space is $O(n)$, not the manifest's $O(1)$ bound. The manifest corresponds to a bottom-up DP retaining only the six states for the previous day.

For the maximum `n = 10^5`, ordinary Python recursion depth is also a practical limitation of this exact recursive source; an iterative six-state update avoids that issue while preserving the recurrence.

## Alternatives and edge cases

- **Six-state iterative DP:** Update counts for absence-used and trailing-late states one day at a time. It achieves $O(n)$ time and $O(1)$ space and matches the manifest.
- **Matrix exponentiation:** Represent the six-state transition as a matrix and exponentiate for $O(\log n)$ time, useful for much larger `n`.
- **Generate all strings:** There are $3^n$ candidates, so checking them afterward is infeasible.
- **Second absence:** Its branch is absent when `j == 1`.
- **Third consecutive late:** Its branch is absent when `k == 2`.
- **Present after late days:** It resets `k` to zero.
- **Absence after late days:** It also resets `k` while consuming the absence allowance.
- **`n = 1`:** All three single-character records are valid.
- **Modulo arithmetic:** Every state reduces its sum, preventing enormous cached integers.
- **Cache clearing:** It releases state after the answer is captured.
- **Large recursion depth:** The exact recursive form may need replacement by iterative DP for the largest legal input.
