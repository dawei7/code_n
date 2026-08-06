## Hints

1. Frame the decision in terms of whether `target` satisfies the majority definition.
2. Determine the frequency of `target` and compare it with the array length.
3. Because `nums` is sorted, binary search can be used to determine that frequency.
4. One binary-search method finds the first and last occurrences of `target`, then derives its frequency from those boundary indices.
