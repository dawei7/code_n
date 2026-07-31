## Function Contract

**Inputs**

- `s`: A binary string of length $n$.
- `t`: A binary string with the same length as `s`.
- `flipCost`: The positive cost of flipping one bit in either string.
- `swapCost`: The positive cost of swapping two different positions within one string.
- `crossCost`: The positive cost of swapping the two bits at the same position across the strings.

Both strings may be changed, and the permitted operations may be repeated and interleaved freely.

**Return value**

Return an integer equal to the smallest possible sum of operation costs that leaves `s` and `t` identical at every index.
