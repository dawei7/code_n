## General

The same key character may appear at several positions on the ring. Choosing the nearest occurrence now is not always globally optimal because the chosen position becomes the starting alignment for the next character. Dynamic programming preserves every relevant ending position instead of making a premature greedy choice.

Let `n = len(ring)` and `m = len(key)`. The dictionary `pos` maps each character to all ring indices where it appears. This avoids scanning every ring cell when processing one key character; only matching alignments can be valid states.

**Circular rotation distance.** Between ring indices `j` and `k`, direct movement along one direction has length `abs(j - k)`. Going the other way around the circular ring has length `n - abs(j - k)`. The minimum rotation steps are therefore

`min(abs(j - k), n - abs(j - k))`.

This handles wraparound. Positions zero and `n - 1` are one rotation apart, not `n - 1` rotations apart.

**Define the DP state.** `f[i][j]` is the minimum total steps needed to spell `key[0]` through `key[i]` and finish with ring index `j` aligned at twelve o'clock. Only indices `j` in `pos[key[i]]` can have finite values.

The total includes both rotations and the center-button press for every character already spelled.

**Initialize the first key character.** Initially ring index zero is aligned. Reaching occurrence `j` of `key[0]` costs `min(j, n - j)` rotations. Pressing the button costs one more step, so

`f[0][j] = min(j, n - j) + 1`.

Every matching occurrence is initialized because different first choices can lead to different future costs.

For the ring `"godding"` and first key character `'g'`, occurrence zero costs one press with no rotation. Another `g` near the end can be reached by wrapping, but may or may not benefit later stages.

**Transition between matching occurrences.** For key position `i > 0`, choose a current occurrence `j` of `key[i]`. The previous character could have finished at any occurrence `k` of `key[i - 1]`. From that prior state, the candidate cost is

$$
f[i-1][k]
+\min\left(\lvert j-k\rvert,n-\lvert j-k\rvert\right)
+1.
$$

The first term is all earlier work, the second is the shortest circular rotation, and the final one presses the button for the current character. The nested loop tries every relevant `k` and keeps the minimum in `f[i][j]`.

No other history is needed. Once the previously spelled prefix and current aligned ring index are known, future rotations are independent of how that state was reached. This is the optimal-substructure property behind the DP.

**Why the transition is complete.** Any valid spelling route for `key[0:i+1]` must end the previous stage at some occurrence `k` of `key[i - 1]` and the current stage at some occurrence `j` of `key[i]`. The recurrence explicitly considers that pair and uses the shortest possible rotation between them. Conversely, every transition describes a legal rotation and press. Taking minima therefore neither omits a legal plan nor invents an impossible one.

After the final character, the ring may be aligned at any occurrence of `key[-1]`. The expression

`min(f[-1][j] for j in pos[key[-1]])`

selects the best complete route regardless of its ending alignment.

The guarantee that every key character occurs in the ring ensures each needed position list is nonempty and the final minimum is defined.

Correctness follows by induction over `i`. Initialization gives the exact cost of every legal first-character ending state. Assuming row `i - 1` is exact, the transition enumerates every possible previous ending occurrence and adds the exact cheapest rotation plus press to `j`. Its minimum is therefore the exact optimal cost for state `(i, j)`. The final minimum covers every legal ending state.

## Complexity detail

Let $R = len(ring)$ and $K = len(key)$. For each adjacent key-character pair, the exact source tries every occurrence of the current character against every occurrence of the previous character. In the worst case, both characters occur at all $R$ positions, so one row costs $O(R^2)$ and total time is $O(KR^2)$.

The table has $K$ rows and $R$ columns, using $O(KR)$ space. The position dictionary stores $O(R)$ indices. These are the exact source bounds and match the editorial's ordinary bottom-up DP, not the manifest's $O(KR)$ time and $O(R)$ space. Keeping only the previous and current rows would reduce table space to $O(R)$ but is not implemented here.

## Alternatives and edge cases

- **Greedy nearest occurrence:** It can choose a locally short rotation that leaves the ring poorly aligned for later key characters. DP is needed for global optimality.
- **Top-down memoization:** Cache states `(key_index, ring_index)` and recursively try matching occurrences. It expresses the same recurrence.
- **Space-compressed DP:** Retain only the preceding row because each transition depends only on `i - 1`. This achieves $O(R)$ table space.
- **Shortest-path formulation:** Treat `(key progress, ring position)` as graph states and use a priority queue. It can avoid some dense transitions but adds graph machinery.
- **Repeated current character:** Staying at the same ring occurrence costs zero rotation but still costs one button press.
- **Wraparound:** Always compare direct distance with `R - direct_distance`.
- **First ring character already matches:** Initialization charges zero rotation plus exactly one press.
- **Several final occurrences:** The answer must minimize across all of them rather than assume the first position list entry.
- **Guaranteed spellability:** Every key character has at least one ring occurrence, so no unreachable-key branch is required.
