## General

**Why ordinary left-to-right printing is not enough**

One printer turn can write one repeated character across any chosen interval, and later turns may overwrite parts of that interval. This means a turn can help positions that are far apart.

For `"aba"`, printing `"aaa"` across all three positions and then overwriting the middle with `"b"` takes two turns. Printing each visible run independently would incorrectly suggest three.

Because distant decisions interact through overwriting, the natural state is an interval rather than a single prefix count.

**Define the interval state**

`f[i][j]` is the minimum number of turns needed to produce the substring from index `i` through index `j`, inclusive.

A one-character interval needs exactly one turn, so:

`f[i][i] = 1`.

The table begins with infinity elsewhere. Each transition replaces infinity with the best proven construction for that interval.

**When the two endpoint characters match**

If `s[i] == s[j]`, the exact recurrence uses:

`f[i][j] = f[i][j - 1]`.

Why can the final character at `j` be obtained for free? Take an optimal schedule for `s[i:j]`, which ends at `j - 1`. Somewhere in that schedule, a turn prints the final desired character `s[i]` at position `i`. Extend that same repeated-character stroke through position `j`. Later turns used for the original interval do not reach outside `j - 1`, so they do not erase position `j`. Since `s[j]` equals `s[i]`, the extended schedule produces the larger interval with no additional turn.

The larger interval also cannot require fewer turns than its restriction to the first `j - i` positions: any schedule for `[i, j]`, when restricted to `[i, j - 1]`, gives a schedule for the shorter target using no more turns. Therefore, equality is exact, not merely an upper bound.

This rule captures the printer's ability to combine matching characters across positions that may later be overwritten.

**When the endpoints differ**

If `s[i] != s[j]`, one shared final-character stroke cannot directly account for both outer positions. The solution tries every split point `k` between `i` and `j - 1`:

`f[i][k] + f[k + 1][j]`.

Printing the left interval optimally and then the right interval optimally is always a legal schedule for the whole interval, so every split supplies a valid candidate.

For intervals with different endpoint characters, an optimal printing schedule can be separated at some boundary associated with the groups of turns that establish the two distinct outside results. Trying all boundaries ensures the recurrence includes that optimal separation. Taking the minimum avoids committing to a split before its cost is known.

At the extreme split `k = i`, the candidate prints the first character separately and solves the rest. At `k = j - 1`, it solves the prefix and prints the final character separately. Intermediate splits allow both sides to exploit their own internal matching-character savings.

**Why the table is filled in this order**

The outer loop moves `i` from right to left. For a fixed `i`, `j` moves from `i + 1` to the right.

This order guarantees every dependency is ready:

- `f[i][j - 1]` is earlier in the same row;
- `f[i][k]` has a smaller end and is earlier in the same row;
- `f[k + 1][j]` begins at an index larger than `i`, whose row was completed during an earlier outer-loop iteration.

No state reads an uncomputed infinity value as a real answer.

**Walk through `"aba"`**

Each diagonal state is one.

For `"ab"`, endpoints differ, and the only split gives `1 + 1 = 2`.

For `"ba"`, the same reasoning gives two.

For `"aba"`, the first and last characters match. The equal-endpoint rule sets `f[0][2] = f[0][1] = 2`. This corresponds to printing all three positions as `a` and then overwriting the middle with `b`.

**Walk through repeated runs**

For `"aaabbb"`, intervals consisting only of `a` or only of `b` collapse to one turn through repeated equal-endpoint transitions. Splitting between the runs gives one plus one, so the whole string needs two turns.

The implementation does not preprocess consecutive duplicates, but the recurrence naturally handles them.

**Why the dynamic program is correct**

Use induction on interval length. Length-one states are correct.

Assume all shorter intervals are solved optimally. If the current endpoints match, the stroke-extension argument proves the current optimum equals `f[i][j - 1]`, which is correct by induction.

If endpoints differ, every tested split combines two correct shorter schedules into a legal current schedule. The interval structure of an optimal printer schedule admits at least one such separating boundary when its endpoint results differ, so one candidate reaches the true optimum. Taking the minimum cannot fall below what any legal schedule can achieve. Therefore, `f[i][j]` is correct.

Induction reaches `f[0][n - 1]`, which the exact code returns as `f[0][-1]`.

## Complexity detail

Let `N` be the string length.

There are `O(N^2)` interval states. When endpoint characters differ, a state may test `O(N)` split points. In the worst case, total running time is `O(N^3)`.

The table contains `N * N` numeric entries, giving `O(N^2)` space. The algorithm is iterative, so it does not add a recursion stack.

Equal-endpoint states skip the split loop and can make particular inputs faster, but worst-case strings still require cubic work. Initialization of the table itself takes `O(N^2)` time and space.

## Alternatives and edge cases

- **Top-down memoization:** Recursively solve intervals and cache results. It uses the same asymptotic time and space but adds recursion overhead and computes only reached states.

- **Compress consecutive duplicate characters:** Replacing each run with one character does not change the minimum turns, because one stroke can cover the whole run. This can substantially reduce the effective `N` before dynamic programming.

- **Alternative matching-index recurrence:** Start by printing `s[i]` separately, then merge that turn with later positions whose character equals `s[i]`. This is another standard `O(N^3)` interval formulation.

- **Print each final run separately:** This fails on `"aba"` because overwriting allows the two `a` positions to share one earlier stroke.

- **Greedily print the most frequent character first:** Interval placement and overwrite order matter; frequency alone does not determine an optimal schedule.

- **One-character string:** The diagonal initialization returns one.

- **All characters equal:** Equal-endpoint reuse propagates one across the whole interval, so the answer is one.

- **All adjacent characters different:** Nonadjacent matches may still permit merging, so the method must retain the full interval reasoning.

- **Matching endpoints with a complex middle:** The endpoints can share a stroke while later turns repair the middle, which is precisely why `f[i][j - 1]` suffices.

- **Overwrite is allowed:** Treating previously printed characters as immutable would solve a different and easier problem.

- **Empty string:** The source guarantees length at least one. The exact return `f[0][-1]` assumes a nonempty table.

- **Fill order:** Iterating starts from left to right without changing the dependency structure could read unfinished right-subinterval states. The descending start index is essential.

- **Infinity initialization:** Every reachable nonempty interval receives a finite candidate. Infinity merely prevents an uninitialized value from winning a minimum.
