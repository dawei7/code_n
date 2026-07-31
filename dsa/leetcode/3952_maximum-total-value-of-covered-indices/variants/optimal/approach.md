## General

**Decompose the token string into runs.** Consider a maximal run of $k$ tokens occupying indices $l$ through $r$. If $l>0$, those tokens can collectively cover $k$ distinct positions chosen from the $k+1$ indices `[l - 1, r]`. Any one position in that range can be omitted: to omit index $j$, move the tokens from $l$ through $j$ one step left and leave the tokens after $j$ in place. The resulting destinations are distinct and cover every other index in the range.

All values are positive, so using distinct destinations is never worse than making tokens collide. The best contribution of this run is therefore the sum over `[l - 1, r]` minus its minimum value. If $l=0$, no preceding index exists; leaving the entire initial run in place covers all $k$ positions, so its full sum contributes.

Different maximal runs are separated by at least one zero. The candidate range of a run includes only the zero immediately before it, so ranges for distinct runs do not overlap. Their optimal choices can be made independently and added.

The scan records the sum and minimum of each run. When the run starts after zero, it folds in `nums[l - 1]` and subtracts the range minimum; a run beginning at index zero keeps its full sum. Every covered-range value is processed once, establishing the maximum total described above.

## Complexity detail

Let $n=\texttt{nums.length}$. The outer scan advances monotonically, and the inner run scan visits each token position exactly once. Each position does constant work, so the running time is $O(n)$. The indices, current sum, current minimum, and answer use $O(1)$ auxiliary space.

The benchmark uses a single token run preceded by zero at lengths 32, 128, and 512. A linear control implementation passes these tiers. A correct quadratic implementation that tries every possible omitted position and recomputes the retained sum returns every expected answer but must fail scaling.

## Alternatives and edge cases

- **Two-state dynamic programming:** Tracking whether the previous position is occupied can model each token's stay-or-move choice in $O(n)$ time, but the run structure gives a shorter proof and less state.
- **Try every omitted index:** Evaluating all $k+1$ omissions by resumming a length-$k$ run is correct but costs $O(k^2)$ for one long run.
- **No tokens:** If `s` contains no `1`, no index is covered and the answer is zero.
- **Run beginning at zero:** There is no candidate position `-1`; the run contributes the sum of its existing indices without discarding a value.
- **Single-token run:** The token simply chooses the larger value between its initial index and the preceding index, when one exists.
- **Collisions:** Two tokens may target the same position, but because every value is positive and each run admits distinct destinations, a collision cannot improve the optimum.
- **Equal minima:** Any minimum-valued candidate may be omitted; only the maximum total is requested.
