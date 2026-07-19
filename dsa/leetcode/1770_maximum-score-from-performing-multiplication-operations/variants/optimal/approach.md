## General
**Describe a state without storing both boundaries**

After `operation` removals, suppose `left_taken` came from the left. Then `operation - left_taken` came from the right. The next available indices are therefore `left_taken` and `n - 1 - (operation - left_taken)`. The operation number and left count determine the complete remaining boundary state.

**Branch on the only two legal removals**

Let $F(o,\ell)$ be the best score obtainable from operation $o$ onward after $\ell$ left removals. With multiplier $q_o$, left value $x_\ell$, and the determined right value $x_r$, the recurrence is

$$
F(o,\ell)=\max\left(q_o x_\ell+F(o+1,\ell+1),\ q_o x_r+F(o+1,\ell)\right).
$$

After $m$ operations, no multiplier remains, so every state in that layer has value $0$. The desired result is $F(0,0)$.

**Evaluate layers backward**

Process operations from $m-1$ down to $0$. At layer `operation`, only `left_taken` values from `0` through `operation` are reachable. Both successor values already belong to the next layer, so each state can take the better of its left and right transition.

**Reuse one score array safely**

Store the next layer in `scores`. While computing a layer, iterate `left_taken` upward. The right transition reads `scores[left_taken]` before that cell is overwritten, and the left transition reads `scores[left_taken + 1]`, which has not yet been touched in the current upward pass. Thus one array retains exactly the dependencies required by the recurrence.

Every legal sequence begins with either the current left value or the current right value. The recurrence evaluates both choices and combines each immediate product with the optimal continuation for its resulting state. Backward induction from the zero-operation base layer therefore proves that every stored value is optimal, including `scores[0]` for the original arrays.

## Complexity detail
Layer `operation` contains `operation + 1` states. Across all $m$ layers, the number of transitions is

$$
\sum_{k=1}^{m}k=\frac{m(m+1)}{2},
$$

so the running time is $O(m^2)$. The rolling score array has $m+1$ entries, requiring $O(m)$ space. The much larger value of $n$ affects only constant-time right-index calculations.

## Alternatives and edge cases
- **Enumerate every left/right sequence:** Trying both choices recursively without memoization takes $O(2^m)$ time.
- **Top-down memoization:** Caching `(operation, left_taken)` states has the same $O(m^2)$ time but uses $O(m^2)$ memo space and recursion depth $m$.
- **Full two-dimensional table:** This makes transitions visually explicit but stores $O(m^2)$ values when only adjacent layers are needed.
- **Negative values and multipliers:** Greedily taking the currently largest product can sacrifice a value needed by a later multiplier.
- **Exactly $m$ operations:** No operation may be skipped, even when both available products are negative.
- **More numbers than multipliers:** Middle values may remain unused; only the exposed ends can be selected.
- **Equal end values:** Both transitions may tie, and either produces the same optimal state value.
- **Single multiplier:** Compare the two original endpoints directly.
