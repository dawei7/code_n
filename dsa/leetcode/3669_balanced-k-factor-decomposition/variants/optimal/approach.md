## General

**The objective depends only on the smallest and largest factors**

We need exactly `k` positive integers whose product is `n`. For one candidate list, the maximum difference between any two entries is

`maximum_factor - minimum_factor`.

There is no need to compare every pair separately. The source carries the minimum and maximum chosen so far and evaluates their spread after the last factor is determined.

Because `k <= 5` and `n <= 10^5`, exhaustive enumeration of divisor-based factorizations is feasible once divisors can be retrieved efficiently.

**Precompute divisors for every possible remainder**

Outside the class, the source constructs `g` for all integers below `100001`:

`g[x]` is the list of every positive divisor of `x`.

The nested loops visit each `i` and append it to `g[j]` for every multiple `j` of `i`. Thus `i` is placed exactly in the lists of numbers it divides.

When the DFS has remaining product `x`, every valid next factor must divide `x`. The precomputed list `g[x]` supplies exactly those choices without testing all integers.

This table is global and built when the module is loaded, before `minDifference` runs. That fact materially affects the exact source’s standalone time and space even though the manifest omits it.

**Build exactly `k` factors through a remaining product**

The recursive state `dfs(i, x, mi, mx)` means:

- Positions `i + 1` through `k - 1` of `path` have already been chosen.
- Their product has been divided out.
- `x` is the product still needing decomposition.
- `mi` and `mx` are the smallest and largest chosen factors so far.
- Positions zero through `i` still need factors.

Initially `i = k - 1` and `x = n`, so all `k` positions remain.

When `i > 0`, the loop chooses any divisor `y` of `x`, writes it at `path[i]`, and recurses with remaining product `x // y`. Since `y` divides `x` exactly, no fraction or invalid remainder can appear.

The minimum and maximum are updated to include `y`.

**Let the final remaining quotient be the last factor**

When `i == 0`, the recursion does not loop over another divisor. The only value that preserves the total product is the entire remaining `x`, so it becomes `path[0]`.

The complete product is

`x * every previously selected y = n`.

The source computes the candidate spread after including this final `x`:

`max(mx, x) - min(mi, x)`.

If it is strictly smaller than the best `cur`, the source copies `path` into `ans`.

The initial `mi = inf` and `mx = 0` work because all factors are positive. The first selected factor replaces both sentinel effects through `min` and `max`.

**Why every valid decomposition is visited**

Take any ordered factor tuple `(a0, a1, ..., a{k-1})` whose product is `n`.

At the first recursive choice, `a{k-1}` divides `n`, so it appears in `g[n]`. After dividing it out, `a{k-2}` divides the remaining product. Continuing this argument, the DFS can choose every tuple suffix in order, leaving `a0` as the final quotient.

Therefore every ordered factor decomposition appears on some recursion path. The source evaluates its exact maximum-minus-minimum spread and retains the smallest encountered value. It cannot miss a better decomposition.

Conversely, every recursion path chooses exact divisors and leaves the quotient as the final factor, so every evaluated list is valid.

**The source enumerates ordered, not non-decreasing, decompositions**

The manifest summary says each non-decreasing decomposition is enumerated once. The exact source does not impose `y >=` or `y <=` any prior factor.

For `k = 2`, choosing divisor two yields factors `[n/2, 2]`, while choosing `n/2` yields the reversed list `[2, n/2]`. Both are evaluated.

This duplication does not affect the answer because order is irrelevant and both permutations have the same spread. It does increase the number of recursion paths compared with a symmetry-pruned non-decreasing search.

**Trace `n = 44, k = 3`**

One recursion path chooses factor 11, leaving four. It then chooses factor two, leaving final quotient two. The path is `[2, 2, 11]` with spread nine.

Other branches produce arrangements such as `[1, 4, 11]` with spread ten or `[1, 2, 22]` with spread 21. Since nine is smaller, the best answer becomes `[2, 2, 11]` or one of its enumerated permutations.

For `n = 100, k = 2`, choosing divisor ten leaves quotient ten, producing spread zero. No spread can be negative, so this is globally optimal.

**Why copying `path` is necessary**

`path` is reused and overwritten as DFS explores later branches. Assigning `ans = path` would store only another reference to the mutable working list, allowing later recursion to change the saved answer.

The slice `path[:]` creates an independent snapshot of the best candidate.

**Exact preprocessing and storage costs**

Let `M = 100000`. The global sieve performs roughly

`M/1 + M/2 + ... + M/M = O(M log M)`

append operations and stores the same order of total divisor entries.

The manifest reports only `O(F)` time and `O(k)` space, apparently treating divisor access as free external preprocessing. In the standalone source, module initialization costs `O(M log M)` time and space before the per-call DFS.

This distinction matters for faithful complexity reporting.

## Complexity detail

Let `F` denote the number of divisor-choice recursion edges or states visited for the particular `(n, k)`. Each edge performs constant work, and each completed candidate copies `k <= 5` entries only when it improves the best. The per-call search is `O(F * k)` in the most literal bound and `O(F)` when fixed `k` is treated as a constant.

The recursion depth and working `path` use `O(k)` space. The saved answer also uses `O(k)`.

However, exact standalone cost includes the global divisor table with `M = 10^5`:

- Precomputation time: `O(M log M)`.
- Persistent table space: `O(M log M)`.

Total first-load-plus-call time is `O(M log M + F)` for fixed `k`, and total memory is `O(M log M + k)`.

If `g` is shared across many calls and its initialization is amortized or excluded as preexisting infrastructure, the manifest’s per-call `O(F)` time and `O(k)` additional search space become reasonable. They are not the full cost of loading this exact file.

## Alternatives and edge cases

- **Enumerate only non-decreasing factors:** Require each next factor to respect an ordering bound. This removes permutation duplicates and matches the manifest summary more closely.
- **Generate divisors on demand:** Trial division up to `sqrt(x)` avoids the global `O(M log M)` table and may be preferable for one call.
- **Prime-factor distribution:** Factor `n` and distribute prime factors among `k` buckets. Searching balanced allocations can reduce redundant divisor recursion but is more involved.
- **Greedily choose factors near the `k`-th root:** Closeness is a useful heuristic but does not prove the minimum spread for arbitrary divisor structure.
- **Factor one:** Ones are valid positive factors and allow exactly `k` entries even when few nontrivial factors exist.
- **Perfectly balanced decomposition:** If all `k` factors can be equal, spread zero is optimal and cannot be improved.
- **Tied optimal decompositions:** The source updates only on a strict improvement and returns the first minimum-spread tuple encountered, which is allowed.
- **Order of returned factors:** The problem permits any order, so the source need not sort `ans`.
- **Global variable shadowing:** The nested parameter named `mx` shadows the module’s divisor-limit variable `mx` only within DFS; Python resolves each scope correctly.
- **Recursion depth:** It is at most `k <= 5` and is safe under ordinary Python limits.
- **Input range:** The table covers every permitted `n <= 10^5`.
- **Missing imports:** The stored source uses `List` and `inf` without imports. Standalone Python requires the corresponding `typing` and `math` imports unless provided by the harness.
