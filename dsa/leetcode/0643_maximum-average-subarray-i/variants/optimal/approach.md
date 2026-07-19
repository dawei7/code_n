## General
**Maximize the sum before dividing**

Every candidate contains the same positive number `k` of elements. Therefore, their averages have the same ordering as their sums, so division is needed only once after finding the maximum window sum.

**Initialize the first complete window**

Sum the first `k` values and use that as both the current and best sum. This is important when all values are negative: starting the best at zero would incorrectly prefer a nonexistent empty window.

**Slide by exchanging two endpoints**

When the window moves one position right, add the entering value and subtract the value exactly `k` positions behind it. Update the best sum after each exchange. Every length-`k` window is reached once without resumming its shared interior.

**Why no candidate is missed**

The initial window begins at index zero. Each subsequent iteration advances its start by one and maintains exactly the sum of that next window through one addition and subtraction. The sequence visits every legal start index through $N - k$, so the greatest recorded sum, divided by `k`, is the required maximum average.

## Complexity detail
The initial sum reads `k` values, and the sliding loop reads each remaining value once, for $O(N)$ total time. The current sum, best sum, and indices use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Prefix sums:** each window sum becomes a difference of two prefix values in $O(1)$ time, but the prefix array uses $O(N)$ extra space.
- **Resum every window:** directly sums each length-`k` slice and is correct, but can take $O(Nk)$ time.
- **Binary search an average threshold:** is useful for variable-length variants, but adds unnecessary complexity when the length is fixed.
- When $k = 1$, the answer is the largest element.
- When $k = N$, the only candidate is the entire array.
- All-negative input requires initializing from a real window rather than zero.
- Fractional and negative averages must use ordinary division after choosing the best sum.
