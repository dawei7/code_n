## General
**Locate the right boundary with a prefix maximum**

Scan left to right while maintaining the largest value seen. If `nums[i]` is smaller than that maximum, some earlier larger value must move past index `i` in the final ordering. Therefore any sufficient segment must extend through `i`; record it as the current right boundary. Equality is not a violation because the target order is nondecreasing.

**Locate the left boundary with a suffix minimum**

Scan right to left while maintaining the smallest value seen. If `nums[i]` is larger than that minimum, some later smaller value must move before index `i`. Any sufficient segment must therefore begin at or before `i`; update the left boundary.

**The two extreme violations define the minimum segment**

Outside the recorded left boundary, every value is no greater than all values to its right. Outside the recorded right boundary, every value is no smaller than all values to its left. Sorting the enclosed segment resolves every crossing inversion and connects correctly to both sorted outer regions. Shrinking either side would retain the violation that established that boundary, so no shorter segment can work.

**Detect an already sorted array**

If the prefix scan never finds a value below its prefix maximum, no right boundary is set. The whole array is already nondecreasing, so return zero; otherwise return `right - left + 1`.

## Complexity detail
The two directional scans examine each of the `n` values a constant number of times, taking $O(n)$ time. Only boundary indices and running extrema are stored, so extra space is $O(1)$.

## Alternatives and edge cases
- **Compare with a sorted copy:** find the first and last positions that differ from `sorted(nums)`; it is simple but costs $O(n \log n)$ time and $O(n)$ space.
- **Monotonic stacks:** a rising stack finds the left boundary and a falling stack finds the right boundary in $O(n)$ time, using $O(n)$ space.
- **Enumerate or expand inversions:** can become $O(n^2)$ if each element is repeatedly compared or shifted.
- **Already sorted array:** has no violating boundary and returns zero.
- **Single element:** is already sorted.
- **Two reversed elements:** require sorting the entire two-element array.
- **Duplicate values:** equality is allowed; use strict violation comparisons.
- **Violation near one end:** the minimal segment may begin at index zero or end at the last index.
- **Negative values:** comparisons work unchanged.
