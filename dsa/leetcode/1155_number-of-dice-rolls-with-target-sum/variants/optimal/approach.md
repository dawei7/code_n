## General

**Define the count after a fixed number of dice**

Let `f[i][j]` be the number of ordered outcomes for the first `i` dice whose face values sum to `j`. Dice are distinguishable by their position in the roll sequence, so `(1, 6)` and `(6, 1)` are two different outcomes for two dice.

The final answer is `f[n][target]`.

The table has `n + 1` rows to include the state with no dice, and `target + 1` columns to include sum zero. It begins filled with zeros.

**Establish the only nonzero empty-roll state**

With zero dice, there is exactly one way to make sum zero: choose no face values at all. This empty outcome is represented by

`f[0][0] = 1`.

There are zero ways for zero dice to produce a positive sum, so every other cell in row zero remains zero. This base case gives the first real die something to build from. For example, `f[1][3]` receives `f[0][0]` from choosing face three and therefore becomes one.

**Choose the last die's face**

Suppose the algorithm is calculating `f[i][j]`. If the `i`th die shows face `h`, then the preceding `i - 1` dice must sum to `j - h`. The number of outcomes with that final face is `f[i - 1][j - h]`.

The last face can be any integer from one through `k`, provided it does not exceed `j`. Therefore, the recurrence is

`f[i][j] = sum(f[i - 1][j - h])`

for `1 <= h <= min(j, k)`.

These cases are disjoint because an outcome has exactly one last face value. They are exhaustive because every legal outcome ending at sum `j` must use one of the die's faces. Adding their counts gives the exact total.

The innermost loop implements this recurrence and reduces the partial sum modulo `10^9 + 7` after every addition. Modular addition is compatible with the final required remainder, so early reduction does not change the answer modulo the constant.

**Fill rows in dependency order**

Rows are processed from one die through `n`. Every transition for row `i` reads only row `i - 1`, which is already complete. Within a row, the order of sums is not required for dependency correctness because no state reads another cell from the same row.

The sum loop begins at one because positive-faced dice cannot produce a useful zero sum once at least one die is rolled. It stops at `min(i * k, target)`. The largest sum possible with `i` dice is `i * k`, so cells above that bound must be zero and do not need computation. The table also has no column beyond the requested `target`.

The code does not begin `j` at the minimum possible sum `i`. It visits some impossible low sums when `j < i`, but those states remain zero because every referenced previous state ultimately traces back to an impossible or zero base. This adds avoidable iterations without affecting correctness.

**Why the dynamic program is correct**

For zero dice, the initialized row gives the exact counts. Assume row `i - 1` correctly counts every sum for `i - 1` dice.

For a target sum `j` in row `i`, partition all valid outcomes according to the face `h` shown by the last die. Removing that last die leaves an outcome of `i - 1` dice with sum `j - h`, whose count is correct by the induction assumption. Conversely, appending face `h` to any outcome counted by `f[i - 1][j - h]` creates one unique valid `i`-die outcome of sum `j`.

Summing over all legal `h` therefore counts every valid outcome exactly once. By induction, all table rows are correct, including `f[n][target]`.

For two six-sided dice and target seven, the final-face choices one through six refer to previous sums six through one. Each previous state has one way, so the recurrence adds six, matching the six ordered pairs in the example.

**Why dynamic programming is needed**

Enumerating every complete roll would consider `k^n` outcomes, most of which do not sum to the target. Many partial rolls share the same pair consisting of dice used and current sum. The table merges all such histories into one count state, then extends that aggregate rather than re-enumerating each prefix.

The method stores counts rather than actual sequences because only the number is requested. The recurrence preserves multiplicity: different prefixes contributing to the same state remain represented in its numeric count and produce different extended outcomes when a face is appended.

## Complexity detail

Let `T` denote `target`. The exact code has loops over up to `n` dice, up to `T` sums, and up to `k` face values. Its worst-case time complexity is therefore `O(nTk)`. The smaller loop bounds `i * k` and `min(j, k)` reduce actual work for early rows and small sums but do not change this general upper bound.

The exact table contains `(n + 1)(T + 1)` integers, so its auxiliary space complexity is `O(nT)`.

These exact bounds differ from the local manifest, which states `O(nT)` time and `O(T)` space. Those improved bounds require two optimizations that are not present in `solution.py`:

- a sliding-window or prefix-sum recurrence to replace the inner face loop with constant work per state;
- rolling rows because row `i` depends only on row `i - 1`.

The protected implementation uses the direct triple-loop recurrence and retains every row. This approach documents that code accurately rather than assigning it the optimized variant's complexity.

The modulo operation keeps numeric values bounded for storage and required output, though it does not change the number of states or transitions.

## Alternatives and edge cases

- **Enumerate all `k^n` rolls:** This is exponential and repeats the same partial-sum subproblems. Dynamic programming aggregates them.
- **Top-down memoization:** A recursive function over dice remaining and sum remaining implements the same recurrence and may skip unreachable states. It still tries up to `k` faces per visited state and uses memo plus recursion stack.
- **Rolling two rows:** Since only the previous row is read, retaining two arrays reduces space to `O(T)` without changing the direct recurrence's `O(nTk)` time.
- **Sliding-window transition:** Consecutive sum states use overlapping ranges of the previous row. Maintaining a rolling range sum can reduce time to `O(nT)` and, combined with rolling rows, realizes the manifest's advertised bounds.
- **Feasibility precheck:** If `target < n` or `target > nk`, the answer is immediately zero. The exact table also produces zero naturally but does extra work.
- **One die:** Exactly one outcome exists when `target` is between one and `k`; otherwise the result is zero.
- **Minimum possible sum:** Sum `n` has exactly one outcome, with every die showing one.
- **Maximum possible sum:** Sum `nk` has exactly one outcome, with every die showing `k`.
- **Target above the possible maximum:** No computed row reaches that sum, so the final cell stays zero.
- **Impossible low intermediate sums:** Cells with `j < i` remain zero even though the exact loop visits them.
- **Ordered outcomes:** Swapping face values between dice generally creates another way, so combinations must not be treated as unordered multisets.
- **Modulo arithmetic:** Every addition is reduced modulo `10^9 + 7`, which is equivalent to reducing only the final exact count.
- **Manifest mismatch:** `O(nT)` time and `O(T)` space describe an optimized recurrence and rolling storage, not the exact full-table triple-loop source.
