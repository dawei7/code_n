## General

**Each adjacent pair determines choices for the row above**

For an allowed triple `ABC`, bottom pair `AB` may support top block `C`. The solution groups all triples by their ordered first two characters:

`d[(a, b)].append(c)`.

Order matters. Choices for `AB` do not automatically apply to `BA`.

Given a current row `s`, every adjacent pair must choose one permitted top character. Those choices, in order, form the entire next row, which has length one less.

**Reject a row as soon as one pair has no option**

DFS uses `pairwise(s)` to inspect every neighboring pair. For each pair it retrieves its list of possible top characters.

If any list is empty, no next row can be built from `s`, regardless of choices for other pairs. The method returns false immediately.

Otherwise the option lists are collected in `t`.

**Enumerate complete next rows with a Cartesian product**

`product(*t)` chooses one character from each adjacent pair’s option list. Each resulting tuple `nxt` is one complete candidate row above `s`.

Joining the tuple produces the string passed to recursive DFS. `any(...)` short-circuits as soon as one candidate row can reach the top; remaining combinations do not need exploration.

It is important to choose the whole next row consistently. Adjacent triangles share bottom blocks, but their top blocks simply become neighboring blocks in the next row; the Cartesian product represents every allowed combination.

**Base case**

A row of length one is already the pyramid’s top. No more triangle must be checked, so DFS returns true.

The bottom length is at least two, and every recursive level reduces length by exactly one, guaranteeing termination.

**Memoize row feasibility**

Different construction choices can lead to the same intermediate row. From that row upward, the answer depends only on the row string and the fixed allowed mapping, not on how the row was reached.

The `@cache` decorator stores the Boolean result for each row. If it reappears, DFS reuses the result rather than expanding its combinations again.

**Trace `"BCD"`**

Suppose `BC` can produce `C` and `CD` can produce `E`. The only next row is `"CE"`. If `CE` can produce `A`, the recursive chain reaches the single-character row `"A"` and succeeds.

If either original pair had no allowed top, `"BCD"` would fail immediately.

**Why local availability alone is insufficient**

Every pair in one row may have at least one possible top, yet all combinations may create a next row containing a pair with no allowed continuation. The algorithm must recursively test complete rows rather than merely confirm current local options.

**Why row strings are sufficient cache keys**

No rule depends on the level number, the choices made below, or how many times a color was previously used. Once a particular row has been formed, its possible upper pyramids are determined entirely by its adjacent pairs and the fixed `allowed` mapping.

Therefore two search branches reaching the same row have identical future success or failure. Caching by the row string merges exactly equivalent subproblems without discarding any relevant history.


For a row `s`, the Cartesian product enumerates every and only next row whose individual triangles are allowed. DFS returns true if any of those rows can recursively reach a one-block top.

By induction on row length, the base case is correct, and the recursive case is true exactly when some legal next-row choice leads to a complete legal pyramid. Therefore `dfs(bottom)` exactly answers the problem.

## Complexity detail

Let `n` be the bottom length and let `a` be the maximum number of top choices for one ordered pair. A complete pyramid has `n(n - 1)/2` non-bottom positions. A coarse worst-case search bound is therefore `O(a^(n(n - 1)/2))` combinations.

Memoization can greatly reduce repeated work by evaluating each distinct row string once. With alphabet size `A = 6`, the number of possible cached rows across lengths is `O(A^n)`. Cache storage plus recursion and mapping is therefore `O(A^n + |allowed|)` in a broad worst case.

The small constraints, especially `n <= 6`, keep exhaustive branching feasible.

## Alternatives and edge cases

- **Backtrack one top position at a time:** Build a candidate row incrementally and recurse when complete. This avoids materializing product tuples and allows additional pruning.

- **Bitmask transitions:** Encode each pair’s possible top letters as six bits for faster combination checks, at the cost of less beginner-friendly code.

- **Greedily choose the first allowed top:** A locally legal choice may block the next level while another choice succeeds. All alternatives may need exploration.

- **Check only current pairs:** Local feasibility does not guarantee a complete pyramid; recursive rows must also be valid.

- **Missing pair mapping:** The current row is impossible immediately.

- **Several paths reach the same row:** Caching prevents repeated expansion.

- **Allowed order:** `AB` and `BA` are distinct bottom patterns.

- **Single-character recursive row:** It is a completed top and succeeds without another lookup.
