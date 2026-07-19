## General
**Sort to expose the cheapest candidates for each target**

Sort `nums` in ascending order. If a chosen group is raised to a target `nums[right]`, its cheapest possible members are a contiguous suffix ending at `right`: replacing any included smaller value with a larger excluded value cannot increase the cost.

Maintain a window `[left, right]` and its sum $S$. Raising every value in the window to the rightmost target $t$ costs

$$
t(\texttt{right}-\texttt{left}+1)-S.
$$

This subtracts the original total from the total the window would have after equalization.

**Shrink only when the current target is unaffordable**

Add each new rightmost value to the running sum. While the cost exceeds `k`, remove `nums[left]` from the sum and advance `left`. Removing the smallest window value gives the greatest possible cost reduction and leaves the cheapest candidates for the same target.

Once the inequality is restored, the entire window can become equal to `nums[right]`; record its length. As `right` advances, no previously removed left endpoint can become feasible again for a target that is at least as large, so both pointers move only forward.

**Why the largest feasible window is the answer**

Any optimal final value can be reduced to the largest original selected value: choosing a still larger target spends extra increments without adding candidates. For that original target in sorted order, the cheapest group of a given size is the contiguous block immediately to its left. The sliding window retains exactly the largest affordable such block for every possible target, so the maximum recorded length matches the global optimum.

## Complexity detail
Sorting takes $O(n\log n)$ time, and the two window pointers together visit each value at most twice for $O(n)$ additional work. The sorted representation and runtime sorting storage are bounded by $O(n)$ space; the window itself uses $O(1)$ scalar state.

## Alternatives and edge cases
- **Rescan leftward for each target:** It can accumulate deficits correctly but repeats work and takes $O(n^2)$ time.
- **Prefix sums plus binary search:** For each sorted target, binary-search the earliest affordable left endpoint in $O(\log n)$ time, also giving $O(n\log n)$ overall.
- **Frequency counting by value:** Bounded input values permit a counting-based variant, but it requires careful weighted-window accounting across empty values.
- **Already equal values:** They join a window at zero cost.
- **Exact budget:** A window whose cost equals `k` is feasible; shrink only when the cost is greater.
- **No useful increment:** The answer remains at least the largest frequency already present.
- **Only increases:** Values to the right of a target cannot be included by lowering them.
- **Single element:** Its maximum frequency is one.
- **Large products:** The term `target * window_size` can exceed 32-bit range even though each input does not.
- **Input order:** Sorting is essential; the original positions have no role in the result.
