## General
**Turning the strength definition into an ordered geometry problem**

The median cannot be determined from the original positions, so first sort a copy of `arr` in ascending order and read

$$
m=\texttt{ordered}\!\left[\left\lfloor\frac{n-1}{2}\right\rfloor\right].
$$

After sorting, values smaller than or equal to $m$ become farther from the median as their indices move left, while values greater than or equal to $m$ become farther as their indices move right. Thus, among any still-unselected contiguous interval of the sorted array, a strongest remaining value must be at one of its two endpoints. No interior value can be farther from $m$ than both extremes.

**Comparing the two possible strongest values**

Maintain pointers `left` and `right` at the current interval endpoints. Compare the endpoint strengths by their distances from $m$.

- If $\lvert\texttt{ordered[left]}-m\rvert$ is larger, select the left value and advance `left`.
- If the right distance is larger, select the right value and decrement `right`.
- If the distances tie, select the right value. Because the array is sorted, the right endpoint is at least as large as the left endpoint, exactly implementing the larger-value tie-breaker.

Append the selected endpoint and repeat until $k$ occurrences have been collected. The returned order happens to run from strongest to weakest, although the contract permits any permutation of the selected multiset.

**Why endpoint removal remains correct**

Initially, every array occurrence lies in the interval `[left, right]`, and the preceding geometric observation proves that the strongest one is an endpoint. The comparison chooses the stronger endpoint under both parts of the definition, so the first removal is correct.

After one endpoint is removed, all remaining occurrences still form a contiguous sorted interval around the same fixed median. The same argument therefore applies again. By induction, each iteration removes the strongest occurrence not chosen earlier. After $k$ iterations, the result contains exactly the top $k$ occurrences. Moving a pointer by one also preserves duplicate multiplicities: equal values at different indices are considered and removed independently.

## Complexity detail
Sorting the $n$ values costs $O(n\log n)$ time. The two-pointer selection performs exactly $k$ constant-time comparisons and removals, adding $O(k)$ time; because $k \le n$, the total remains $O(n\log n)$.

The app-local implementation sorts a copy so that callers retain their input, requiring $O(n)$ storage. The returned list holds $k$ values and is also bounded by $O(n)$. If input mutation is allowed, an in-place sort can reduce auxiliary storage apart from the output to the sorting implementation's own stack or workspace.

## Alternatives and edge cases
- **Sort directly by strength:** Compute the median, then sort all values by `(abs(value - median), value)` in descending order. This is correct and has the same asymptotic bounds, but it performs another full sort and repeatedly evaluates the ranking key instead of exploiting the already sorted order.
- **Heap selection:** After finding the median, maintain a min-heap of the best $k$ strength pairs. This takes $O(n\log k)$ selection time after median discovery and $O(k)$ heap space; obtaining the median by sorting still dominates unless a linear-time selection algorithm is also used.
- **Linear-time selection:** The median can be found with selection, and the $k$th strength threshold can be selected similarly. This can achieve expected or worst-case linear time with careful tie and multiplicity handling, but it is substantially more intricate than the required sorting solution.
- **Repeated maximum search:** Scanning every remaining value to choose one strongest occurrence at a time is correct, yet selecting $\Theta(n)$ values takes $O(n^2)$ time.
- **Even-length arrays:** The median is the lower middle value at index $\lfloor(n-1)/2\rfloor$, not the average of the middle pair and not the upper middle value.
- **Equal distances:** When endpoints are equally far from the median, the numerically larger right endpoint must be chosen first.
- **Duplicates:** Equal array entries are separate occurrences. Selecting one does not remove or represent all copies.
- **All values requested:** When `k == n`, every occurrence is returned; the arbitrary-order rule still applies.
- **Single-element input:** The lone value is the median and necessarily the single strongest result.
