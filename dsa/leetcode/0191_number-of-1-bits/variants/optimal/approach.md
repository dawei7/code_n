## General
Brian Kernighan's bit trick removes one set bit per iteration:

$n = n \mathbin{\&} (n - 1)$.

To see why, write the suffix of any nonzero value through its least-significant one as `...1000...0`. Subtracting one changes that suffix to `...0111...1`: the lowest one becomes zero and every lower zero becomes one. ANDing with the original clears the changed low region while leaving every higher bit untouched. Exactly the least-significant set bit disappears.

Increment a counter each time this operation is performed and stop when `n` becomes zero. For `11`, whose binary form is `1011`, the values progress `1011 -> 1010 -> 1000 -> 0000`, so the counter reaches three.

Unlike checking every bit position, the loop count depends on the population count. Sparse inputs such as powers of two finish after one iteration, though the source's bounded positive-integer domain makes both strategies constant in the asymptotic notation requested here.

Each iteration clears exactly one set bit and does not change any other set bit. After `c` iterations, exactly `c` original one-bits have been removed, and all remaining one-bits are still present in the working value. The loop terminates precisely when none remain, so the counter equals the original number of set bits.

## Complexity detail
If the input contains `b` set bits, the loop takes $O(b)$ operations. Because $n \le 2^{31} - 1$, at most 31 positions can be set, so this is $O(1)$ time under the source contract. The working integer and counter use $O(1)$ space.

## Alternatives and edge cases
- Testing a mask across all 31 permitted value positions is simple and has the same bounded asymptotic cost, but always performs every check.
- Binary-string conversion followed by counting is concise but allocates a representation.
- Byte lookup tables can accelerate large batches at the cost of preprocessing or static storage.
- The smallest legal input, one, and every power of two return one; the largest legal input, $2^{31} - 1$, returns 31.
