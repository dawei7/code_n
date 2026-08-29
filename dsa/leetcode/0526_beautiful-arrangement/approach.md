## General

A beautiful arrangement is a permutation, so every number from one through `n` must be used exactly once. In addition, the number chosen for one-indexed position `i` must satisfy:

`value % i == 0 or i % value == 0`.

The solution constructs arrangements from left to right with backtracking. It rejects an incompatible placement immediately, so it never completes a permutation that already violates the divisibility rule.

**Precompute which values fit each position.** The nested loops examine every pair `(i, j)` from one through `n`. If either `j % i == 0` or `i % j == 0`, value `j` is appended to `match[i]`.

After this preprocessing, `match[i]` contains exactly the values legally placeable at position `i`. The recursive search can iterate this shorter compatibility list instead of retesting all values at every node.

For example, at position two, value one fits because two is divisible by one; value two fits because each divides the other; value four fits because four is divisible by two. A value such as three does not fit position two because neither divides the other.

**Track which values are already used.** Array `vis` is indexed by the numbers themselves. `vis[j]` is true exactly while value `j` occurs in the current partial arrangement. Index zero is unused because the problem labels values from one.

The recursive call `dfs(i)` means that positions one through `i - 1` have already received distinct compatible values and position `i` is next.

For every `j` in `match[i]`:

- if `vis[j]` is true, skip it because a permutation cannot repeat a value;
- otherwise mark `j` used;
- recursively fill position `i + 1`;
- unmark `j` after that call returns.

The final unmark is the backtracking step. It restores the exact state that existed before choosing `j`, allowing a sibling branch to try that value at another later-compatible position. Without restoration, choices from one branch would incorrectly constrain unrelated branches.

**Count a complete arrangement.** When `i == n + 1`, every real position from one through `n` has been filled. Each placement came from the corresponding compatibility list, and `vis` prevented reuse, so the partial construction is now a complete beautiful permutation. The code increments `ans` once and returns.

There is no need to store the permutation explicitly. The recursion depth identifies the current position, and `vis` records its chosen value set. The search only needs the count, not the arrangement contents.

For `n = 2`, `match[1]` contains both one and two because every integer is divisible by one. If position one receives one, position two can receive two, producing `[1, 2]`. If position one receives two, position two can receive one, producing `[2, 1]`. Both branches reach `dfs(3)`, so the result is two.

For `n = 1`, the single value one is compatible with the single position. Marking it leads immediately to `dfs(2)` and increments the answer once.

**Why every counted branch is valid.** A branch reaches the base case only after selecting one value for each position. Every selection came from `match[i]`, so every position satisfies at least one divisibility direction. The visited array makes the selected values distinct. Choosing `n` distinct values from the set of `n` labels uses every label exactly once, so the result is a valid permutation.

**Why every valid arrangement is counted.** Consider any beautiful permutation. At position one, its value belongs to `match[1]` and is initially unused, so the search contains that branch. The same statement holds at each later position because the permutation's value is compatible and has not appeared earlier. Following these choices reaches the base case. Distinct permutations differ at a first position, so they follow different branches and are counted exactly once.

The `nonlocal ans, n` declaration lets the nested function update the shared integer answer and read the method parameter. Only `ans` actually requires rebinding; including `n` makes the closure use explicit.

The small limit `n <= 15` makes pruned combinatorial search feasible. Precomputation removes repeated modulus work, while early compatibility filtering avoids exploring all invalid suffix permutations.

## Complexity detail

Building `match` checks $n^2$ position-value pairs, using $O(n^2)$ time and up to $O(n^2)$ stored compatibility entries.

The exact recursive implementation does not memoize used-value subsets. In the worst case, a backtracking permutation search may visit $O(n!)$ partial/complete branches, with up to $O(n)$ candidate iterations at a node under a loose bound. Divisibility pruning substantially reduces the actual search, but the source code does not guarantee the manifest's $O(n2^n)$ subset-DP bound.

Likewise, the exact working storage is $O(n^2)$ for `match` plus $O(n)$ for `vis` and recursion depth. The manifest's $O(2^n)$ space corresponds to a bitmask memoization table, which this implementation does not allocate. This distinction documents the exact code rather than attributing a different optimization to it.

## Alternatives and edge cases

- **Bitmask dynamic programming:** Store the number of ways for each used-value subset; the next position is determined by the subset size. It runs in $O(n2^n)$ time with $O(2^n)$ space and matches the manifest.
- **Memoized DFS by used mask:** It keeps the search formulation but merges partial arrangements that have selected the same set of values.
- **Generate every permutation first:** Checking divisibility only after completion wastes all work below an invalid early placement.
- **Test divisibility inside DFS:** It avoids `match` storage but repeats the same pair checks across many branches.
- **`n = 1`:** The sole placement `1` satisfies both divisibility directions and produces one arrangement.
- **Position one:** Every remaining value is compatible because every integer is divisible by one.
- **Value one:** It is compatible with every position because every position is divisible by one.
- **Backtracking restoration:** Failing to reset `vis[j]` would undercount by leaking a branch's choice into later branches.
- **No compatible unused value:** The loop makes no recursive call, correctly contributing zero arrangements from that partial state.
- **One-indexing:** Both compatibility construction and recursion use positions one through `n`; index zero is intentionally unused.
- **Answer accumulation:** Each base-case arrival represents one distinct full permutation, so incrementing by one is sufficient.
