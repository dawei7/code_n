## General

The first subarray is forced to start at index 0, so `nums[0]` always
contributes to the total. Choosing the two cut positions that start the second
and third subarrays contributes the values at two distinct later indices.

Any pair of later indices in increasing order defines a valid three-part
partition, regardless of the elements between or after them. Therefore the
minimum additional cost is simply the sum of the two smallest values in
`nums[1:]`.

Scan the suffix while maintaining its smallest and second-smallest values,
then add them to the forced first value.

## Complexity detail

The suffix is scanned once, giving $O(N)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Sort the suffix:** Taking its first two sorted values is correct but costs $O(N\log N)$ time and extra storage.
- **Enumerate both cuts:** Trying every ordered pair of cut positions is correct but costs $O(N^2)$ time.
- **Exactly three elements:** Every element is necessarily a subarray start.
- **Duplicate minima:** Equal values at two distinct suffix positions may both be selected.
- **Small first element:** `nums[0]` is still forced; it cannot replace either later cut start.
