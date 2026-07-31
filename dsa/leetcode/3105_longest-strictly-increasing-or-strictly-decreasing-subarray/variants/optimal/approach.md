## General

**Track runs that end at the current position.** Let `increasing` be the length of the strictly increasing subarray ending at the current element, and let `decreasing` have the analogous meaning for a strictly decreasing subarray. Both counters and the answer start at one because every one-element subarray satisfies either condition.

Compare each element with its predecessor. If the current value is greater, extend the increasing run by one and reset the decreasing run to one. If it is smaller, extend the decreasing run and reset the increasing run. Equality breaks both strict conditions, so both counters return to one.

After each comparison, update the answer from both counters. The counter definitions remain true by induction: a compatible strict comparison extends exactly the corresponding run ending at the previous position, while an incompatible comparison leaves only the current singleton as a run of that direction. Therefore every maximal strictly increasing or strictly decreasing subarray is measured when its final element is processed, and the largest recorded length is the required answer.

## Complexity detail

Let $n$ be the length of `nums` defined in the function contract. The algorithm performs one constant-time update for each adjacent pair, taking $O(n)$ time. It stores only the two current run lengths and the answer, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Two separate scans:** Scan once for strictly increasing runs and once for strictly decreasing runs. This remains $O(n)$ time and $O(1)$ space, but combines less naturally than updating both states together.
- **Restart from every left endpoint:** Extend a strictly increasing and a strictly decreasing candidate from every possible start. This is correct but takes $O(n^2)$ time on a fully monotonic array.
- **Sort the array:** Comparing `nums` with a sorted copy loses the contiguous-subarray requirement and cannot identify local monotonic runs.
- **Equal adjacent values:** Equality extends neither strict direction; both run lengths must reset to one.
- **Direction changes:** A peak or valley ends one run and begins a two-element run in the opposite direction through the same adjacent pair.
- **Single element:** With no adjacent comparison, the initialized answer of one is already correct.
