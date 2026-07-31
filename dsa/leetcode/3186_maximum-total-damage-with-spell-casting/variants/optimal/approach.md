## General

**Collapse identical spells into one decision.** If a damage value $x$ is selected, spells with the same damage do not conflict with one another. Because every damage is positive, taking only some of the available damage-$x$ spells can never be better than taking all of them. Count each value and replace its group by one weighted choice worth

$$
w(x)=x\cdot\operatorname{count}(x).
$$

**Order the decisions by damage.** Let $v_0<v_1<\cdots<v_{u-1}$ be the unique damage values. A choice at $v_i$ conflicts only with earlier values $v_i-2$ and $v_i-1$. All earlier values at most $v_i-3$ remain compatible.

Define `best[i]` as the maximum damage obtainable from the first $i$ unique values. Also let $p(i)$ be the number of unique values strictly smaller than $v_i-2$. The decision for $v_i$ is therefore

$$
\texttt{best[i+1]}=\max\bigl(\texttt{best[i]},\;w(v_i)+\texttt{best[p(i)]}\bigr).
$$

The first term skips $v_i$. The second takes every copy of $v_i$ and combines that group with the best solution ending before its conflict window. A pointer finds each $p(i)$: as $i$ increases, advance the pointer past values smaller than $v_i-2$. The pointer never moves backward.

These two recurrence branches exhaust every valid optimum. Any optimum either omits $v_i$, in which case its value is at most `best[i]`, or includes $v_i$, in which case it includes the whole group and its remaining choices are confined to the first $p(i)$ values. Conversely, both recurrence branches construct valid selections. Induction over the sorted values therefore proves that the final DP entry is the maximum possible total damage.

## Complexity detail

Let $n$ be the length of `power` and $u$ the number of distinct damage values. Frequency counting costs $O(n)$, sorting costs $O(u\log u)$, and the DP plus monotone pointer costs $O(u)$. Thus the total is $O(n+u\log u)$, which is $O(n\log n)$ in the worst case. The frequency map, sorted values, and DP array use $O(u)$ space, bounded by $O(n)$.

## Alternatives and edge cases

- **Binary search for the compatible prefix:** Searching for $p(i)$ independently at every value is correct and remains $O(n\log n)$ overall, but the monotone pointer makes the DP phase linear after sorting.
- **Quadratic weighted DP:** Scanning every earlier unique value for each $v_i$ directly implements the recurrence but costs $O(u^2)$ time when many powers are distinct.
- **Recursive memoization:** A take-or-skip recursion over sorted values expresses the same choices, but iterative DP avoids recursion depth and call overhead.
- **Equal powers:** They are mutually compatible; aggregate and take all copies whenever that value is selected.
- **Differences one and two:** Both are forbidden, so a compatible predecessor must be at most $v_i-3$.
- **Difference three:** This is the first compatible gap and must not be skipped by an off-by-one boundary.
- **Unsorted input:** Only the aggregated unique values are sorted; the original order has no effect on the answer.
- **Large totals:** Up to $10^5$ spells may each contribute $10^9$, so the result can exceed 32-bit integer range.
- **Single unique value:** Every spell can be cast, and the DP returns that value multiplied by its frequency.
