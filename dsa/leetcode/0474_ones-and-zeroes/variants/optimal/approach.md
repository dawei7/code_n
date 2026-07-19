## General
**Treat zeros and ones as two knapsack resources**

Let `best[z][o]` be the largest number of processed strings selectable with at most `z` zeros and `o` ones. Count the zeros and ones of each string to obtain its two resource costs.

**Update both budgets backward**

For a string costing `(zeros, ones)`, iterate zero capacity from `m` down to `zeros` and one capacity from `n` down to `ones`. Update from `1 + best[z - zeros][o - ones]`. Descending order ensures the source state belongs to earlier strings, so the current string cannot be selected twice.

**Why the recurrence is optimal**

For every capacity pair, an optimal subset either excludes the current string and keeps the old value, or includes it and combines the string with an optimal subset under the remaining budgets. The maximum of those exhaustive cases is optimal by induction over processed strings.

## Complexity detail
For `k` strings, each update visits at most $(m + 1)(n + 1)$ capacity pairs, giving $O(k \cdot m \cdot n)$ time. The two-dimensional table uses $O(m \cdot n)$ space.

## Alternatives and edge cases
- **Three-dimensional DP:** stores a layer per string and is easier to derive, but uses $O(k \cdot m \cdot n)$ space.
- **Memoized include/exclude recursion:** explores the same states with $O(k \cdot m \cdot n)$ bounds and recursion overhead.
- **Enumerate every subset:** is correct but takes $O(2^k)$ choices before budget checking.
- **Forward capacity iteration:** incorrectly permits reusing the same string multiple times.
- **Zero budget in one dimension:** strings consuming only the other character may still be selected.
- **Duplicate strings:** remain distinct selectable items and must not be deduplicated.
- **String exceeding either budget:** contributes no update but does not affect other choices.
