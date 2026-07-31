## General

**Turn every query into a prefix query.** Sort the indices by `nums1`. When processing a first-array value $x$, every previously completed smaller-value group is eligible, and every later larger-value group is ineligible. The only subtlety is equality: indices with value $x$ must all receive their answers before any of their `nums2` values are admitted. Processing equal values as one group creates exactly that strict-inequality barrier.

**Keep only the useful prefix values.** Among all `nums2` values from completed groups, only the largest `k` affect any future answer. Maintain them in a min-heap and track their running sum. Push each newly eligible value; if the heap grows beyond `k`, remove its smallest entry. The heap then contains precisely the largest at most `k` values seen so far, and the running sum is the required answer for the next `nums1` group.

For each equal-value group, first write the current sum to every original index in that group. Only afterward insert the group's second-array values into the heap. This ensures that equal `nums1` values never select one another, while all strictly smaller groups remain represented. Writing through stored original indices restores the requested output order.

## Complexity detail

Let $n$ be the common array length. Sorting the indices costs $O(n\log n)$. Each index enters the heap once and can cause one removal, with each heap operation costing $O(\log k)$. The total time is therefore $O(n\log n+n\log k)=O(n\log n)$ because $k\le n$.

The sorted index array, answer, and heap use $O(n+k)=O(n)$ auxiliary space. The running sum may reach $k\cdot10^6$, so fixed-width implementations need a 64-bit integer.

## Alternatives and edge cases

- **Brute force per index:** Scanning all $j$ values and selecting the best candidates independently costs at least $O(n^2)$ time.
- **Sort every candidate list:** Rebuilding and sorting eligible values for each answer repeats almost all work and can cost $O(n^2\log n)$.
- **Maximum heap of every prefix value:** Retaining all values and extracting `k` repeatedly is more expensive; the size-`k` min-heap keeps exactly the relevant set and its sum.
- **Equal `nums1` values:** Add an equal-value group only after answering the whole group, because the comparison is strict.
- **Fewer than `k` candidates:** Sum all eligible positive values; do not return `-1` and do not pad the choice.
- **No candidates:** The empty choice is allowed and has sum zero.
- **`k = 1`:** The heap stores the single largest eligible `nums2` value.
- **`k = n`:** No eligible positive value needs to be discarded, although equality still excludes the current group.
- **Original order:** Sorting is internal; answers must be written back by original index.
- **Duplicate `nums2` values:** Equal contributions are independent elements and may all remain in the heap when capacity permits.
