## General

Let the chosen final value be $x$, which cannot be below the current maximum. Define the total number of required unit increments and the largest single-element deficit as

$$
D(x) = nx - \sum_i \texttt{nums[i]},
\qquad
L(x) = x - \min_i \texttt{nums[i]}.
$$

**Pricing one fixed target**

A two-index operation consumes two deficits belonging to different elements. At most $\lfloor D(x)/2 \rfloor$ pairs exist by total quantity. The element with deficit $L(x)$ also needs enough increments among all other elements to partner with it, so at most $D(x)-L(x)$ pairs are possible. When `cost2` is cheaper than two single operations, the maximum useful pair count is therefore

$$
P(x) = \min\!\left(\left\lfloor\frac{D(x)}{2}\right\rfloor,\ D(x)-L(x)\right).
$$

The remaining $D(x)-2P(x)$ increments must be single operations. This construction is feasible: if the largest deficit is no more than all other deficits combined, deficits can be paired until fewer than two remain; otherwise every non-largest deficit pairs with the largest one and its excess remains single.

If `cost2 >= 2 * cost1`, pairing never saves money. Raising the target only adds work, so using single operations to reach the current maximum is immediately optimal. The same conclusion holds for at most two elements: paired increments cannot reduce their difference.

**Why only four targets matter**

Assume $n \ge 3$ and pairs are cheaper. The largest deficit stops being the bottleneck at the smallest integer $b$ satisfying $2L(b) \le D(b)$:

$$
b = \max\!\left(\max_i \texttt{nums[i]},
\left\lceil\frac{\sum_i \texttt{nums[i]} - 2\min_i \texttt{nums[i]}}{n-2}\right\rceil\right).
$$

Below $b$, the fixed-target cost is a linear function of $x$, so its minimum on that interval is at the current maximum or at $b-1$. From $b$ onward, all but possibly one deficit can be paired. Targets with the same parity form strictly increasing sequences because increasing $x$ by $2$ adds $2n$ deficits and therefore positive cost. Thus the first balanced target of each parity, $b$ and $b+1$, suffices. Evaluating the current maximum, $b-1$, $b$, and $b+1$ covers every possible optimum.

## Complexity detail

Computing $n$, the sum, the minimum, and the maximum takes $O(n)$ time. Every candidate target is then priced with a constant number of arithmetic operations, so total time is $O(n)$.

Only scalar aggregates and a constant-size candidate set are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every target through twice the maximum:** The optimum is guaranteed within that range, but scanning value space costs $O(n + M)$ even with aggregate formulas, where $M = \max(\texttt{nums})$.
- **Recompute every deficit for every target:** This direct method is correct but costs $O(nM)$ and is the principal slower comparison used by the benchmark.
- **Simulate operations:** Greedily choosing indices operation by operation can require an enormous number of steps and obscures the fixed-target pairing bound.
- A one-element or already-equal array costs zero.
- With two elements, a paired increment preserves their difference, so only single increments can close the original gap.
- When `cost2 >= 2 * cost1`, pair operations can be replaced by two no-more-expensive single operations.
- The minimum must be taken on full integer costs; apply the modulus only to the final answer.
- Parity matters after deficits become balanced, which is why both $b$ and $b+1$ are checked.
