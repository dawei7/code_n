## General

**Understand what one operation can change**

For one bit position, `value XOR x` reverses the bit exactly when the
corresponding bit of `x` is one. ANDing that result with the original `value`
means an original zero remains zero, while an original one can either remain
one or be cleared. Choosing `x` therefore permits any subset of an element's
set bits to be removed independently.

**Maximize every result bit independently**

If no input value contains a bit, no operation can create it. If at least one
value contains the bit, retain that occurrence and clear the same bit from all
other elements that contain it. Its final parity is then odd, so the array XOR
contains that bit. These choices can be made simultaneously for every bit
position.

Thus the maximum reachable XOR contains exactly the union of all input bit
sets, which is their bitwise OR. Scan the array and accumulate that OR.

## Complexity detail

Let $n$ be the number of elements. One constant-time OR is performed per
element, giving $O(n)$ time. The accumulator requires $O(1)$ auxiliary space.
The linear bound is asymptotically optimal because an uninspected element may
be the sole source of an answer bit.

## Alternatives and edge cases

- **Per-bit scans:** Checking every supported bit across the whole array is correct but repeats the traversal and obscures the direct OR identity.
- **Enumerate cleared submasks:** Trying every reachable value for every element grows exponentially with the number of set bits.
- **Original XOR:** It may cancel duplicate bit occurrences and therefore need not be maximal.
- **Zero operations:** The unchanged array is one legal outcome, but operations can improve it.
- **Zeros:** A zero contributes no bit and remains zero after every operation.
- **Duplicate values:** Extra occurrences can have selected bits cleared so they do not force even parity.
