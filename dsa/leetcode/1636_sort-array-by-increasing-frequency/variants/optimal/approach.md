## General
**Separate counting from ordering.** Scan `nums` once and store the number of occurrences of every distinct value in a frequency map. After this pass, the complete ordering rule for an element `value` is represented by the pair `(frequency[value], -value)`: the first component puts rarer values first, and the negative second component reverses the usual numeric order whenever frequencies tie.

**Apply one lexicographic sort.** Sort every element using that pair as its key. All copies of one value receive identical keys and therefore form one block. Between different blocks, a smaller frequency wins the first comparison; only equal frequencies reach the second comparison, where the larger original value has the smaller negated key and comes first.

These two comparisons exactly match the requested priority rules. The result preserves every input occurrence because sorting only permutes the array, and every pair of distinct value blocks is placed in the required relative order.

## Complexity detail
Counting takes $O(n)$ time, and comparison sorting $n$ elements takes $O(n\log n)$ time. The frequency map, key storage, and returned ordering use $O(n)$ space in the worst case when all values are distinct.

## Alternatives and edge cases
- **Sort distinct values, then expand:** Sort at most $n$ frequency-map keys by the same pair and append each key the recorded number of times. This has the same worst-case bounds and can avoid comparing repeated elements.
- **Fixed-range buckets:** Because values are restricted to $[-100,100]$, counts can be stored in a 201-slot array and emitted by frequency groups in $O(n+201)$ time, but that optimization depends on this small numeric domain.
- **Repeated minimum selection:** Repeatedly searching for the next block produces the right order but can require quadratic time.
- A one-element array is already correctly ordered.
- If all values are distinct, every frequency is one, so the result is the input values in strictly decreasing order.
- If all elements are equal, sorting leaves the array unchanged.
- Negative values use ordinary numeric comparison: for example, $-1$ precedes $-6$ when their frequencies tie because $-1$ is larger.
