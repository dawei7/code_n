## General

The input length is fixed at three, so there are only $3!=6$ positional orders. Evaluate all six and retain the largest result. This exhaustive search cannot miss the optimum because every legal concatenation corresponds to exactly one permutation of the three input positions.

Construct a concatenation numerically rather than allocating binary strings. Suppose the value already assembled is `value` and the next number is `number`. If `number` uses $b$ bits, shifting `value` left by $b$ positions creates exactly enough zero positions for that representation. Bitwise OR then places `number` into those positions, so `value = (value << number.bit_length()) | number` is identical to appending its no-leading-zero binary representation.

Apply that update to the three numbers in each permutation. The maximum of the six completed integers is therefore precisely the maximum legal binary concatenation.

## Complexity detail

The contract fixes both the array length at three and every value at at most seven bits. The algorithm evaluates six orders with three constant-width updates each, so its time and auxiliary space are both $O(1)$.

## Alternatives and edge cases

- **Binary strings:** Joining `bin(number)[2:]` for each order is direct and correct, but numeric shifts avoid temporary strings and repeated parsing.
- **Pairwise comparator sorting:** Comparing the two possible concatenations of each pair can derive an order, but enumeration is simpler and less error-prone for exactly three elements.
- **Duplicate values:** Permutation enumeration may revisit an identical bit string, but at most six orders exist, so correctness and asymptotic cost are unchanged.
- **Different bit lengths:** The shift must use each appended number's own `bit_length()`; a fixed-width shift would introduce forbidden leading zeros.
- **Maximum values:** Three copies of 127 produce 21 one-bits, which remain safely within the output range.
