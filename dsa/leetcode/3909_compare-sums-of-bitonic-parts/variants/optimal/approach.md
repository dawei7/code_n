## General

**Recover both inclusive sums during one traversal**

Maintain `total_sum`, the prefix sum through the current element, the largest value seen, and `ascending_sum`. Because the array rises strictly to its unique peak, each new value on the ascending side is a new maximum. Whenever that happens, save the current prefix sum as `ascending_sum`. Values after the peak are smaller, so they never overwrite it. At the end of the traversal, `ascending_sum` is therefore the sum from index `0` through the peak.

The traversal also records `peak_value` and the sum of the entire array. Subtracting the ascending sum from the total removes the complete ascending part, including the peak. Add `peak_value` back once to obtain the inclusive descending sum:

$$
B=\texttt{total\_sum}-A+\texttt{peak\_value}.
$$

This identity is exactly where the rule that the peak belongs to both parts is enforced.

**Why the saved prefix identifies the unique split**

Before reaching the peak, strict increase guarantees that the current value exceeds every earlier value, so the saved prefix advances at every position. The peak is the final such update. Strict decrease then guarantees that no later value can equal or exceed the peak, leaving the saved prefix unchanged. Consequently, the two computed sums match the specified inclusive ranges, and the final three-way comparison returns the required code.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Every array element is visited once and performs constant work, so the running time is $O(N)$.

The algorithm stores only running sums, the peak value, and the saved ascending sum. Its auxiliary space usage is $O(1)$.

## Alternatives and edge cases

- **Find the peak, then sum two slices:** This is also $O(N)$ time, but materializing slices requires $O(N)$ auxiliary space; summing by index avoids the slices but needs multiple passes.
- **Binary-search for the peak:** Bitonic order permits an $O(\log N)$ peak search, but both part sums still require reading all $N$ values, so total time remains $O(N)$.
- **Forget to restore the peak:** Computing `total_sum - ascending_sum` yields only the elements strictly after the peak. The peak must be added back because it belongs to the descending part too.
- **Compare only the values around the peak:** The return value depends on complete part sums, not their lengths or endpoint values.
- **Equal sums:** Equality has its own output, `-1`; it must not fall through to either greater-sum branch.
- **Peak near either end:** The strictly increasing or decreasing side may be much longer, but both inclusive ranges and the one-pass identity remain valid.
- **Repeated values across sides:** Strictness applies within each monotone part. A value may occur once before and once after the peak without affecting the unique maximum or the sum calculation.
- **Large values:** A part sum may reach $10^{14}$, so fixed-width implementations need a 64-bit integer type.
