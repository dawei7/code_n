## General

**Append a binary block with arithmetic instead of strings**

Suppose `ans` is the numeric value of the binary concatenation for integers one through `i - 1`. To append the binary representation of `i`, the existing bits must move left by exactly the number of bits in `i`. If that length is `b`, the new value is

$$
\texttt{ans}\cdot 2^b + i.
$$

The source implements multiplication by $2^b$ as `ans << b`. It combines `i` with bitwise OR:

`(ans << i.bit_length()) | i`.

This OR is equivalent to addition here. Shifting left by `b` places `b` zero bits at the bottom of `ans`. Since `i` fits in exactly `b` bits, its set bits occupy only those zero positions, so OR introduces no carry or overlap.

**Get the correct block length**

`i.bit_length()` is the number of bits required to represent positive integer `i` without leading zeros. For example:

- one has binary `1` and bit length one;
- two has binary `10` and bit length two;
- three has binary `11` and bit length two;
- four has binary `100` and bit length three.

Those are precisely the block widths used by ordinary binary representation. No explicit conversion to a string is needed, and no special power-of-two counter is needed.

**Maintain the concatenation invariant**

Before the first iteration, `ans = 0` represents an empty bit string. At iteration `i`, assume `ans` is congruent modulo `mod` to the full concatenation through `i - 1`. Shifting by `i.bit_length()` and placing `i` in the new low bits constructs the concatenation through `i`.

The source then takes the result modulo

$$
10^9+7.
$$

Reducing after every append is valid because modular congruence is preserved by multiplication and addition:

$$
(a\bmod M)\cdot 2^b+i
\equiv a\cdot 2^b+i\pmod M.
$$

Thus the algorithm never needs to hold the astronomically large full concatenated integer. The reduced `ans` still contains all information needed for the final remainder.

**Trace `n = 3`**

Initially `ans = 0`.

For `i = 1`, bit length is one:

`(0 << 1) | 1 = 1`.

For `i = 2`, bit length is two:

`(1 << 2) | 2 = 4 | 2 = 6`.

Six is binary `110`, the concatenation of `1` and `10`.

For `i = 3`, bit length is two:

`(6 << 2) | 3 = 24 | 3 = 27`.

Twenty-seven is binary `11011`, the required concatenation `1 + 10 + 11`.

**Why leading zeros never appear**

Standard binary representations omit leading zeros, and `bit_length` measures that same minimal width. Appending `i` in exactly that width cannot add artificial zeros before its most significant bit. This matters because appending, for example, `0011` instead of `11` would shift later structure and change the final numeric bit string.

**Why the final answer is correct**

The loop invariant establishes that after iteration `i`, `ans` equals the value of the concatenation from one through `i` modulo `mod`. The base case is the empty prefix, and the shift-plus-OR transition appends precisely the next minimal binary representation. By induction, after `i = n` the returned value is exactly the requested concatenation modulo $10^9+7$.

## Complexity detail

The loop runs `n` times. Under the standard word-RAM model for values within the constraints, `bit_length`, a bounded-width shift, OR, and modulo are constant-time operations. `ans` remains below `mod` after every iteration, and the shift amount is at most the bit length of `n`, so intermediate values stay bounded. Total time is $O(n)$.

The method stores only `mod`, `ans`, and loop variable `i`. It constructs no binary strings or arrays, so auxiliary space is $O(1)$.

In arbitrary-precision bit-complexity analysis these integer operations depend on operand width, but here modulo reduction and the input bound keep that width small; the repository manifest uses the ordinary constant-word model.

## Alternatives and edge cases

- **Build one binary string:** Convert every integer with `bin(i)[2:]`, concatenate, parse, and reduce. It is direct but uses $O(n\log n)$ characters and constructs a huge integer.
- **Track bit length at powers of two:** Increase a counter when `i & (i-1) == 0`. This avoids calling `bit_length` and yields the same $O(n)$ time and $O(1)$ space.
- **Use multiplication and addition:** `ans = (ans * (1 << b) + i) % mod` is mathematically identical to shift and OR.
- **`n == 1`:** One iteration appends binary `1` and returns one.
- **Power-of-two boundary:** `bit_length` increases exactly at values such as two, four, and eight, ensuring the prior result shifts by the newly required width.
- **Modulo during every step:** This does not alter the final remainder and prevents the accumulator from growing with the total concatenated length.
- **OR versus addition:** They are interchangeable only because the shift clears all low `b` bits and `i` fits within them.
- **Positive-input guarantee:** `bit_length` for zero is zero, but the sequence begins at one, so every appended block has at least one bit.
- **No leading zeros:** Minimal bit length matches the problem’s conventional binary representation.
- **Large `n`:** The loop remains linear through $10^5$ and avoids any object proportional to the combined binary-string length.
