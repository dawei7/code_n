## General
**Turning element removals into value-elimination costs**

Count how many times each distinct integer occurs. If a value occurs $f$ times, reducing the unique count by one requires deleting all $f$ of its occurrences. Spending fewer than $f$ removals on that value changes no unique-count contribution at all. The optimization can therefore be viewed as buying as many complete value eliminations as possible with a budget of `k`, where each value has benefit one and cost equal to its frequency.

**Why the smallest frequencies must be paid first**

Sort the $U$ frequencies in ascending order. Suppose a plan completely deletes a value with frequency $b$ while retaining a value with smaller frequency $a \le b$. Replacing the deletion of the $b$-frequency value by deletion of the $a$-frequency value eliminates the same one distinct integer and costs no more removals. Any removals saved by this exchange remain available for another value.

Repeatedly applying this exchange transforms an optimal plan into one that removes a prefix of the sorted frequencies. Therefore, scanning those frequencies from smallest to largest cannot eliminate fewer distinct values than any other use of the same budget.

**Consuming the removal budget**

Initialize `remaining = U`. For each sorted frequency `count`, eliminate that value when `count <= k`: subtract `count` from `k` and decrement `remaining`. When the next full frequency exceeds the budget, stop; no later frequency is cheaper, so no additional distinct value can be eliminated.

Any leftover budget smaller than the next frequency may be spent on arbitrary occurrences of a surviving value. That partial deletion is necessary to reach exactly the requested number of removals but does not change the distinct count, so `remaining` is already the optimum.

**Why the returned count is attainable and minimal**

Every decrement of `remaining` corresponds to deleting every occurrence of one selected value, so the constructed count is attainable. The sorted-prefix exchange shows that no plan can fully delete more values for the same number of removals. Once the scan stops, every unprocessed value costs more than the leftover budget, proving that the returned number of unique integers cannot be improved.

## Complexity detail
Counting the array takes $O(N)$ time and stores $U$ frequencies. Sorting those frequencies takes $O(U \log U)$ time, which is within $O(N \log U)$ because $U \le N$. The greedy scan takes $O(U)$ time. The counter and frequency list together use $O(U)$ space.

## Alternatives and edge cases
- **Frequency buckets:** Because no frequency exceeds $N$, store how many distinct values have each frequency and consume buckets from one upward. This achieves $O(N)$ time and $O(N)$ space, trading a potentially larger array for removal of the sort.
- **Min-heap of frequencies:** Push all $U$ counts and repeatedly pop the cheapest affordable one. This is also greedy and takes $O(N + U \log U)$ time, but a full sort is simpler and usually has lower overhead.
- **Sort the original array into runs:** Sorting `arr` makes equal values contiguous, after which run lengths can be collected and sorted. It avoids a hash table but costs $O(N \log N)$ time and may mutate the input if performed in place.
- **Repeatedly recount values:** Searching the full array for each distinct value can still produce correct frequencies, but it takes $O(NU)$ time and fails to scale when many values are unique.
- **Zero removals:** No frequency can be eliminated, so the answer is the original distinct count $U$.
- **Remove the whole array:** When `k = N`, every frequency is consumed and the answer is zero.
- **Partial final frequency:** Spending the remaining budget on only some copies of a value does not reduce the unique count.
- **Equal frequencies:** Their internal order is irrelevant because they have identical elimination cost.
- **One distinct value:** The answer stays one until all $N$ occurrences are removed.
- **Large value magnitudes:** Values are hash-map keys only; their magnitude does not affect the greedy ordering.
