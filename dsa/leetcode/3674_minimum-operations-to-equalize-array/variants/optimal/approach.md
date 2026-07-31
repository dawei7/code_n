## General

There are only two possible answers. If every element already equals the first element, zero operations are both feasible and minimal.

Otherwise, zero operations cannot work because the current array contains at least two different values. One operation is always sufficient: choose the entire array. Its bitwise AND is one well-defined value, and the operation writes that same value into every position. Therefore any nonconstant array has minimum answer exactly one; the actual AND value never needs to be computed.

Scan the array for a value different from `nums[0]`. Return `1` immediately when such a value appears, or return `0` after the scan finishes.

## Complexity detail

For an array of length $n$, the worst case examines all $n$ elements, taking $O(n)$ time and $O(1)$ auxiliary space. Reading the input is necessary to distinguish an all-equal array from one whose only differing value is last, so the linear worst-case time bound is optimal.

The benchmark uses its `size` as $n$ and supplies an all-equal array, forcing the complete scan. A correct slower comparator checks every pair for a mismatch and therefore performs quadratic work on the same inputs.

## Alternatives and edge cases

- **Compute the global bitwise AND:** It produces the value written by a full-array operation, but that value is irrelevant to the minimum count.
- **Compare every pair:** Pairwise equality testing is correct but costs $O(n^2)$ instead of one linear scan.
- **Single element:** A one-element array is already equal and requires zero operations.
- **Difference at the final position:** The scan must not assume equality from a matching prefix.
- **Different values with the same AND:** Any initially nonconstant array still needs one operation, regardless of the resulting AND.
- **Already equal values:** Performing an operation is allowed but not minimal, so the answer is zero.
