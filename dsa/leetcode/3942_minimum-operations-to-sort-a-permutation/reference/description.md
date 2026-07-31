## Description

You receive a permutation `nums` of all integers from $0$ through $n-1$. The target arrangement is increasing order: `[0,1,...,n-1]`.

Only two whole-array operations are allowed:

- **Reverse:** reverse the order of every element in the array.
- **Rotate Left by One:** remove the first element, shift every remaining element one position left, and append the removed element at the end.

Return the minimum number of allowed operations required to reach the increasing target. If no sequence of reversals and one-position left rotations can sort the permutation, return `-1`.
