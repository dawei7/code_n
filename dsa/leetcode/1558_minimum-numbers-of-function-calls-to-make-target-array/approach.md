## General

**Read the operations through binary representation**

The two allowed actions match the two basic ways binary numbers are built.

Incrementing one array element adds one unit to that element. Doubling all elements shifts every binary representation left by one bit.

Because a double affects the entire array in one call, all target values can share the same sequence of binary place-value shifts. Individual one-bits still require element-specific increment calls.

The source computes:

`sum(v.bit_count() for v in nums) + max(0, max(nums).bit_length() - 1)`.

The first term counts all one-bits across targets. The second counts the shared global doublings.

**Understand one target in isolation**

Suppose a value's binary digits are processed from most significant to least significant. Start at zero. To append each later binary digit, double the current value and then increment if that new digit is one.

For binary `101`, increment to one for the leading bit, double to two, do not increment for zero, double to four, then increment to five.

The number of increment steps is the number of one-bits, called the population count. Python's `v.bit_count()` returns exactly that value.

The number of doublings after the leading bit is one less than the bit length.

**Share doublings across the whole array**

Different targets may have different bit lengths. Align all binary representations at their least significant bit and imagine leading zeros for shorter values.

Process bit columns from the highest column needed by any value. At a column, increment each array entry whose target has a one there. Then, unless this is the final column, double the entire array once to shift every partial value toward the next place.

Only the longest target determines how many columns exist. If the maximum target has bit length $B$, exactly $B-1$ global doubles are sufficient for every element.

Shorter values simply receive no increments in leading columns, so their zeros remain zero through those early doubles.

**Why the all-zero case needs max with zero**

For zero, `bit_length()` is zero. If every target is zero, `max(nums).bit_length() - 1` would be negative one even though no operation is needed.

`max(0, ...)` clamps the doubling count to zero. Every zero also has `bit_count() == 0`, so the entire expression correctly returns zero.

The input array is guaranteed nonempty, making `max(nums)` safe.

**A reverse-process proof of optimality**

It is tempting to say every one-bit simply needs an increment, but ordinary addition can carry across bits. A clean lower-bound proof comes from reversing the process.

Imagine reducing `nums` back to the all-zero array. The inverse of an increment is decrementing one chosen positive element by one. The inverse of a global double is dividing every element by two, but that is possible only when all current values are even.

Whenever an element is odd, no global division can occur until that element is decremented. Every odd element therefore forces one individual reverse call. After all odd elements are decremented, all values are even and one global halving removes their lowest bit column.

Repeat this rule. Across all bit columns, a value is odd once for each one-bit in its binary representation, so forced decrements total the sum of bit counts. Global halvings occur once between successive bit columns, for $B-1$ calls.

This reverse sequence is forced at each bit layer and exactly corresponds to a valid forward construction. It proves both necessity and sufficiency of the formula.

**Tracing nums one and five**

Binary one is `1` and binary five is `101`. Their bit counts are one and two, giving three individual increments.

The maximum bit length is three, so two global doubles are required. Total calls are five.

One valid forward schedule increments the second element for its leading one, doubles twice while adding the appropriate lower one-bits, and performs the first element's one increment in the final column. The precise order within a bit column may vary, but the counts cannot improve.

**Why bit_count and bit_length are the exact source operations**

The solution does not loop over bit positions explicitly. Python's integer methods perform those calculations internally.

The generator supplies each population count lazily to `sum`. No collection of counts or binary strings is built.

## Complexity detail

Let $N$ be array length and $B$ the maximum target bit length. Scanning for `max` costs $O(N)$ comparisons. Computing `bit_count` for each arbitrary-precision integer can inspect $O(B)$ machine-level bit information, giving the manifest bound $O(NB)$.

With the contract's values at most $10^9$, $B \le 30$ is fixed, so the practical and fixed-domain bound is $O(N)$.

Only generator state, the running sum, and the maximum value are retained. Auxiliary space is $O(1)$ beyond input and output. Python's integer result fits the problem's guaranteed 32-bit answer range.

## Alternatives and edge cases

- **Simulate forward bit columns:** It makes the construction explicit and produces the same popcount-plus-doublings total.
- **Reverse all values iteratively:** Count odd elements, decrement them conceptually, then halve all values. It is correct but would copy or mutate values and loop over $B$ levels.
- **Breadth-first search over arrays:** The state space is enormous and ignores the binary structure.
- **All zeros:** Both terms become zero because of the explicit clamp.
- **One nonzero target:** The formula reduces to its population count plus bit length minus one.
- **Power of two:** It has one set bit and needs one increment plus the required doublings.
- **Many equal values:** Increment calls remain individual, but every doubling is shared.
- **Different bit lengths:** Leading zero columns require no work for shorter values.
- **Maximum value:** It determines the number of shared doubles, not the sum or average.
- **Increment count:** Each one-bit across every element contributes one forced reverse decrement.
- **No overflow construction:** The exact source never materializes intermediate arrays.
- **Nonempty input:** It guarantees `max(nums)` is defined.
- **Fixed numeric bound:** It makes bit-method costs constant per element in practice, while the manifest retains the general $B$ factor.
