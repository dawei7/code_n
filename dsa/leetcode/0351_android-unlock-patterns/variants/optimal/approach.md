## General
**Encode only moves that cross another key**

Most pairs of keys can be connected immediately. The exceptional pairs cross a key exactly halfway between them: `1-3` crosses `2`, `1-7` crosses `4`, `3-9` crosses `6`, `7-9` crosses `8`, and `1-9`, `3-7`, `2-8`, and `4-6` cross `5`. Store these intermediate keys in a symmetric `skip` table. A transition is legal when its destination is unused and its intermediate key is either zero or already visited.

**Merge prefixes with the same future choices**

For a fixed length, a state key `(visited, current)` records the selected-key bitmask and the last key. Its value is the number of distinct legal prefixes that reach that state. Those prefixes have exactly the same legal continuations because future legality depends only on the visited set and current key, so their counts can be propagated together.

For every state, try each destination. When the move is legal, add its prefix count to `(visited | bit, destination)` in `next_states`. Replacing the current state map with `next_states` advances every represented pattern by one key. The sum of the new state counts is therefore the exact number of patterns of that length, and it contributes to the answer whenever the length is at least `m`.

**Weight the three symmetric starting classes**

The four corners are rotationally equivalent, as are the four edge keys, while the center stands alone. Initialize representative states for keys `1`, `2`, and `5` with weights `4`, `4`, and `1`. Every sequence from a corner representative has exactly one rotated counterpart for each corner, and likewise for an edge representative, so these weights count all nine possible starting keys without changing any transition rule. Length one contributes the sum of those weights, which is nine.

**Why every valid pattern is counted exactly once**

Each transition enforces both source rules: the destination has not appeared, and any crossed key has appeared. Every propagated prefix is therefore valid. Conversely, the next key in any valid pattern passes those two checks, so induction on length shows that its complete sequence reaches the corresponding state. Different sequences follow different transition histories; merging only adds their counts and never identifies them as one sequence. Summing the weights consequently counts every valid pattern exactly once.

## Complexity detail
Let $K=9$ be the number of keys. There are at most $K2^K$ pairs of visited masks and current keys. Each reachable state tries at most $K$ destinations once, giving $O(K^2 \cdot 2^K)$ time. The current and next state maps together contain $O(K \cdot 2^K)$ entries, while the skip table uses $O(K^2)$ space, so total auxiliary space is $O(K \cdot 2^K)$. With the fixed Android keypad, both bounds are small constants.

## Alternatives and edge cases
- **Memoize current key, mask, and remaining length:** is correct, but the extra remaining-length dimension repeats state work across requested totals and exceeds the repository step budget on the maximum legal range.
- **Backtracking without merged state counts:** is correct but revisits equivalent suffix states and approaches permutation growth as the maximum length increases.
- **Generate permutations before validation:** performs still more wasted work because illegal jumps are not pruned when they first occur.
- The intermediate-key rule depends on history: `1 -> 3` is illegal initially but becomes legal after visiting key `2`.
- Adjacent and non-collinear moves do not require an intermediate key.
- Length one has exactly nine patterns, and no pattern can exceed nine because keys cannot repeat.
