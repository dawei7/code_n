## General

**Charge each crossed boundary to the hop's destination.** A hop from index $i$ to $j$ earns

$$
(j-i)\cdot\texttt{nums}[j].
$$

There are $j-i$ unit boundaries between those indices. Think of the hop as earning `nums[j]` once for each boundary it crosses. A complete route from index zero to index $n-1$ crosses every boundary exactly once, and each boundary's contribution is the value at the next selected landing to its right.

For the boundary immediately after index $b$, any landing $j>b$ is possible. To maximize that boundary's contribution, it should be assigned the greatest value available in suffix `nums[b+1:]`. These choices can be made consistently: whenever the suffix maximum changes as boundaries move right, land at the index responsible for the current maximum.

The optimal total is therefore the sum of the appropriate suffix maximum for every boundary.

**The source represents suffix maxima by their indices.** It scans `nums` left to right while maintaining a monotonic stack `stk`. Before pushing index `i` with value `x`, it pops every stored index whose value is at most $x$:

`while stk and nums[stk[-1]] <= x: stk.pop()`.

After the loop, values at stack indices are strictly decreasing from bottom to top, while indices are increasing. More importantly, an index remains exactly when no value at least as large occurs to its right. These are the right-to-left strict suffix-maximum representatives, listed in increasing index order.

The final index always remains because nothing lies to its right. Therefore the later scoring loop necessarily reaches the required destination.

**Why dominated indices can be removed.** Suppose indices $p<q$ have `nums[p] <= nums[q]`. Any hop segment that might land at $p$ could instead extend to $q$ for boundaries up through $p$, receiving a value at least as large. Index $p$ cannot be the best next landing for any boundary before it once $q$ is known. Popping it loses no optimal route.

Using `<=` rather than `<` also removes earlier equal values. Keeping the later equal value is safe because it can reward at least all boundaries the earlier one could, plus possibly more boundaries between them, at the same per-boundary value.

**Turn stack breakpoints into hops.** The second loop starts `i=0`. For each surviving destination `j`, it adds

`nums[j] * (j - i)`

and then sets `i=j`. These are actual consecutive hops along the stack indices. The factor `j-i` counts the boundaries since the previous landing, and `nums[j]` is the maximum suffix value appropriate to all of them.

If stack index zero survives, its term has distance zero and contributes nothing. It merely updates `i` to zero, so it is harmless. The route still begins at zero.

**Why the constructed route is optimal.** For each unit boundary $b$, no route can earn more than

$$
\max_{j>b}\texttt{nums}[j]
$$

from crossing it, because the destination must lie to its right. Summing these maxima is an upper bound on every route.

The monotonic-stack destinations attain that bound boundary by boundary. Between two consecutive surviving indices, the later one's value is the greatest value anywhere to the right of each crossed boundary until the next breakpoint. The scoring loop assigns exactly that value to those boundaries. Because it reaches the last index, it is a valid route attaining the universal upper bound and is optimal.

**Trace `[4,5,2,8,9,1,3]`.** As values are scanned, indices with values $4,5,2,8$ are eventually dominated by the later value $9$ at index four. Value one at index five is then dominated by value three at index six. The surviving meaningful destinations are indices four and six. The route $0\to4\to6$ scores $4\cdot9+2\cdot3=42$.

For `[1,5,8]`, only the last index survives after larger values pop earlier ones. The route jumps directly from zero to two and earns $2\cdot8=16$.

## Complexity detail

Each index is pushed once and popped at most once. Although the inner `while` can pop several indices in one iteration, total stack operations across the scan are $O(n)$. The scoring loop visits at most $n$ survivors. Total time is $O(n)$.

The exact source's stack can contain all indices for a strictly decreasing array, so auxiliary space is $O(n)$, not $O(1)$. This conflicts with the manifest's stated $O(1)$ space. A direct right-to-left suffix-maximum sum can compute the same answer with one running maximum and constant space; the checked-in monotonic-stack implementation does not.

The answer may be large, and Python integers remain exact. `nums` is not mutated.

## Alternatives and edge cases

- **Right-to-left suffix maximum:** Start from the last value, move boundaries right to left, update a running maximum, and add it. This is $O(n)$ time and $O(1)$ space and matches the manifest exactly.
- **Quadratic DP:** For each index, try every later landing and memoize the best suffix score. It is correct but costs $O(n^2)$, as in the smaller version of the problem.
- **Greedy jump to the next larger value only:** A merely larger value may be dominated by an even larger later one; suffix maxima provide the actual criterion.
- **Strictly increasing array:** Earlier indices are repeatedly popped, leaving only the last index; one direct hop is optimal.
- **Strictly decreasing array:** Every index remains. Landing at each next position uses the greatest available suffix value for that boundary.
- **Equal values:** Earlier equal indices are popped by `<=`; delaying the landing loses nothing and can cover more boundaries at the same value.
- **First index on the stack:** Its zero-distance contribution is harmless.
- **Last index:** It always survives and guarantees the route reaches the destination.
- **Positive values:** The upper-bound interpretation is direct. The stated domain excludes negative values that could change whether extra boundaries should share a landing.
- **Input preservation:** The stack stores indices and never reorders `nums`.
- **Manifest mismatch:** Time is linear, but exact auxiliary space is $O(n)$ because of `stk`.
