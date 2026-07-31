## General

**Group subarrays by their right endpoint**

Suppose a map stores, for every distinct value $v$, how many subarrays ending at the previous index have AND equal to $v$. When the next number `x` arrives, the singleton `[x]` contributes one occurrence of `x`. Extending every previous subarray changes its AND from $v$ to `v & x`, so add its frequency to that resulting key.

Different previous values may collapse to the same new AND. Summing their frequencies is essential because they represent different start indices even though their resulting value matches.

**Why the state remains small**

As a subarray extends leftward, bitwise AND can only clear set bits; it can never restore one. Whenever two consecutive distinct AND results differ, at least one previously set bit disappears. Values bounded by $10^9$ use at most 30 relevant bit positions, so subarrays ending at one index have only $O(\log M)$ distinct AND values.

After constructing the current map, its frequency under key `k` is exactly the number of qualifying subarrays ending here. Add that frequency to the global answer, then use the map for the next index.

The map invariant holds initially for the singleton. Every longer subarray ending at the current index uniquely extends a subarray ending one position earlier, and the transition computes its exact AND. Thus all and only current endings are represented with correct multiplicities, and summing the `k` frequencies counts every qualifying subarray once.

## Complexity detail

At each of $n$ indices, at most $O(\log M)$ distinct AND states are extended and merged. Time complexity is $O(n\log M)$ and auxiliary space is $O(\log M)$ for the previous and next state maps.

For the stated values, the number of active keys is at most a small constant tied to the 30-bit domain, but the logarithmic notation records why that bound exists.

## Alternatives and edge cases

- **Enumerate every subarray:** Extending an AND from each start index is correct but takes $O(n^2)$ time in the worst case.
- **Segment tree plus binary search:** Range-AND queries and monotone boundary searches can count valid endings, but the structure is more complex and uses $O(n)$ space.
- **Store every start separately:** This loses the benefit of merging equal AND values and may retain $O(n)$ states per endpoint.
- **Zero target:** Once a running AND reaches zero, further extensions remain zero; their distinct start indices must still be counted through the frequency.
- **Zero element:** Every subarray containing it has AND zero.
- **Single element:** It contributes one exactly when its value equals `k`.
- **Repeated values:** Equal AND states accumulate multiplicity rather than creating duplicate keys.
- **Impossible target bits:** If `k` contains a bit absent from every relevant element, no subarray can produce it.
- **Large answer:** Up to $n(n+1)/2$ subarrays may qualify, requiring a wide integer type.
