## General

**Use a padded array to simplify indices**

The required sequence length is $2n-1$: value one occupies one position, while each of the other $n-1$ values occupies two.

The source allocates `path = [0] * (n * 2)` and intentionally leaves index zero unused. Meaningful positions are one through `2n-1`, and the returned result is `path[1:]`.

This one-based layout makes the second occurrence of value `i` naturally land at `u+i` when its first occurrence is at `u`. The condition `u + i < n * 2` is exactly the requirement that the second position stay at or below `2n-1`.

Zero means an unfilled position; valid sequence values begin at one, so the sentinel cannot be confused with placed data.

**Track whether each number remains available**

`cnt` is initialized with value two in every slot, then `cnt[1] = 1`. The implementation uses these values mainly as truthy availability flags:

- For `i >= 2`, a truthy `cnt[i]` means both required occurrences have not yet been placed. Placement writes both at once and sets `cnt[i] = 0`.
- For one, truthy `cnt[1]` means its single occurrence is still available. Placement sets it to zero.

On backtracking, a larger value is restored to two and one is restored to one. The precise positive number reflects required multiplicity even though the code never decrements one occurrence at a time.

**Always work on the earliest unfilled position**

`dfs(u)` attempts to complete the sequence from position `u` onward. If `path[u]` is already filled as the second occurrence of an earlier placement, it immediately calls `dfs(u + 1)`.

Otherwise, `u` is the earliest still-empty position. Choosing its value decides the first location at which all completions of the current prefix can differ. This is exactly the location that matters next for lexicographic order.

The base condition `u == n * 2` means every meaningful position one through `2n-1` has been passed. Because recursion skips only filled positions and never advances past an unfilled one without placing it, reaching the base means a complete valid sequence exists.

**Try larger values before smaller values**

For an empty `u`, the loop tries `i` from `n` down through two. A larger available value is therefore explored before any smaller value at the earliest undecided position.

A larger `i` can be placed only if its availability is truthy, its partner position `u+i` is within bounds, and that partner position is empty. When all hold, the source writes

`path[u] = path[u + i] = i`

and marks `cnt[i] = 0`. This single action enforces both the required multiplicity and exact distance.

If recursive completion fails, both positions return to zero and availability returns to two, restoring the exact state before trying the next candidate.

**Place one only after every larger candidate**

Value one has no second occurrence or distance requirement. The source handles it after the loop over `n` down to two. If available, it writes one at `u`, marks it used, and recurses.

Placing it last is important for lexicographic maximum: one is the smallest allowed value, so it should occupy the earliest empty position only when no larger choice can lead to a complete solution.

On failure, its position and count are restored just like larger placements.

**Stop at the first full solution**

When a recursive call returns true, every caller immediately returns true without undoing its successful placements. The top-level call's Boolean is not otherwise used; the completed values remain in `path` and are returned.

The problem guarantees that a solution exists, so `dfs(1)` eventually succeeds.

**Why the first solution is lexicographically largest**

At each earliest unfilled position, candidates are tried in descending order. Suppose the returned solution places value $v$ there. Every larger value was either immediately illegal or led, after exhaustive backtracking, to no valid completion with the already fixed prefix.

Therefore no valid sequence sharing the earlier prefix can place a value larger than $v$ at this position. Applying the same argument recursively to every later undecided position proves that no valid sequence is lexicographically greater than the first completion found.

Backtracking is necessary because the locally largest legal placement may block all future placements. The algorithm abandons it only after proving that entire branch impossible, then tries the next value.

**Why every completed path satisfies the contract**

One is placed at most once because its count becomes zero, and completion forces it to be placed exactly once. Each larger `i` is selected at most once, and selection writes exactly two copies at indices differing by `i`. Completion fills $2n-1$ positions, whose total required multiplicity is also $2n-1$, so every required number appears.

For `n=1`, `path` has meaningful index one. The larger-value loop is empty, one is placed, `dfs(2)` reaches the base, and `path[1:]` correctly returns `[1]`.

## Complexity detail

The backtracking search can explore factorially many arrangements in the worst case. Using the standard bound from the manifest, time is $O(n!)$, with substantial pruning from occupied positions, distance checks, and stopping at the first solution.

`path` and `cnt` each contain $2n$ entries, so they use $O(n)$ space. Recursion advances `u` from one toward `2n` and therefore has depth $O(n)$. Total auxiliary space is $O(n)$, matching the manifest.

The constraint $n\le20$ is what makes this pruned exponential search viable. There is no polynomial-time construction encoded in the exact source.

## Alternatives and edge cases

- **Ascending candidate order:** It would find the lexicographically smallest first solution, not the largest.
- **Generate every solution then compare:** It wastes memory and search after the first descending-order completion is already known to be maximal.
- **Bitmask availability:** A bitmask can replace `cnt` and make availability copying compact, while preserving the same backtracking.
- **Choose another empty position:** Filling the earliest empty position gives the direct lexicographic proof and generally stronger pruning.
- **`n = 1`:** Only the single one is placed.
- **Partner out of bounds:** `u+i < 2n` rejects the placement before indexing.
- **Partner already occupied:** The candidate cannot satisfy its exact-distance pair at this start and is skipped.
- **Occupied current position:** It is a previously placed second copy and must be skipped, not overwritten.
- **Value one:** It has one occurrence and no partner position.
- **Successful branch:** Placements are intentionally not undone when true propagates.
- **Failed branch:** Both positions and availability must be restored before trying another value.
- **Padding index zero:** It is never returned and exists only to make positions one-based.
