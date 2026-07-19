## General
**Give each value combination one canonical order**

Sort candidates and carry a `start` index. At a state, choose any candidate from `start` onward. Recurse with the same index because the chosen value may be reused. Never return to a smaller index, so every multiset combination has exactly one nondecreasing representation instead of one path for every permutation.

Stop a loop when a candidate exceeds the remaining target; all later sorted candidates are also too large. When the remainder reaches zero, copy the path into the result.

**Positive values make remaining-target pruning sound**

On entry to a recursive state, the path is nondecreasing, sums to `target - remaining`, and all future choices come from `start` onward. Every chosen candidate is positive, so `remaining` strictly decreases and recursion must terminate.

After sorting, when a candidate exceeds `remaining`, every later candidate also exceeds it. Breaking the loop is safe. This pruning would not be valid with negative candidates, which is why positivity is a meaningful part of the contract.

**Trace reuse without permutation duplicates**

For candidates `[2, 3, 6, 7]` and target 7, the branch beginning with 2 may reuse 2 and then choose 3, producing `[2, 2, 3]`. It cannot later choose a smaller value, so no permutation duplicates arise. The branch starting at 7 emits `[7]` directly.

**One nondecreasing index path per multiset**

Every recursive path chooses only candidate values and is emitted only when its accumulated sum reaches the target, so every result is valid. Reuse passes the current index again, allowing any positive multiplicity of that candidate, while later recursion never returns to a smaller index.

Sort any valid multiset combination by candidate index. It defines one nondecreasing sequence that the search follows exactly, including repeated indices. No different recursion path can encode the same multiset because changing the choice order is forbidden. Every combination is therefore reachable once and only once.

## Complexity detail
If $m$ is the smallest candidate and $T$ the target, recursion depth is at most $T/m$, with up to $n$ choices per level in the loose worst case. This gives $O(n^{T/m})$ search time and $O(T/m)$ auxiliary path/stack space, excluding the potentially exponential output.

## Alternatives and edge cases
- **Generate ordered sequences then deduplicate:** explores all permutations of each combination and wastes exponential work and storage.
- **Dynamic programming of combination lists:** can reuse subtargets but stores many partial combinations and requires careful uniqueness rules.
- **Boolean subset-sum DP:** answers existence, not enumeration, and does not model unlimited reuse without modification.
- A candidate larger than `target` is never chosen. If no branch reaches remainder zero, the result is empty.
- Copy the current path when recording an answer; appending the mutable path object would let subsequent backtracking alter saved combinations.
