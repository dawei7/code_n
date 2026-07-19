## General
**Supply the one range value absent from the indices**

Initialize an XOR accumulator with `n`. For every array index, XOR both the index and its stored value into the accumulator.

After processing a prefix, the accumulator is the XOR of `n`, every processed index, and every processed value. Equal range values cancel in pairs because $x \oplus x = 0$.

**Pair cancellation leaves only the missing value**

The indices contribute `0` through $n - 1$, and seeding with `n` completes the full expected range. The array contributes every member of that range except the answer. Each present value therefore occurs twice in the combined XOR and cancels with itself, while the missing value occurs only on the expected-range side and remains.

## Complexity detail
One constant-time XOR update per element gives $O(n)$ time. A single accumulator uses $O(1)$ space.

## Alternatives and edge cases
- **Set membership:** uses $O(n)$ extra space.
- **Test each candidate against the list:** can take $O(n^2)$.
- The missing value may be zero or `n`; a one-element input is handled identically.
