## General

**Hexadecimal groups binary bits four at a time**

One hexadecimal digit represents exactly four bits, called a nibble. A signed 32-bit integer therefore has exactly eight nibble positions:

$$
32/4=8.
$$

The exact solution examines those eight positions from most significant to least significant. For each position, it extracts a value from zero through fifteen and maps that value to the corresponding lowercase hexadecimal character.

This avoids any built-in integer-to-hexadecimal conversion.

**Handle zero separately**

The number zero has eight zero nibbles. The general loop suppresses leading zeroes, so it would append nothing for this input. The early branch returns `"0"`, the one case where a zero digit must be present.

For every nonzero number, at least one nibble is nonzero. Negative 32-bit values have nonzero high nibbles in two’s-complement form, so their result also cannot remain empty.

**Extract one nibble with shifting and masking**

The loop variable `i` runs through `7, 6, ..., 0`. Nibble `i` occupies bit positions `4*i` through `4*i + 3`.

The expression

```text
(num >> (4 * i)) & 0xF
```

performs two operations:

1. right shift by `4 * i`, moving the desired nibble into the lowest four bit positions;
2. bitwise AND with `0xF`, whose binary form is `1111`, discarding every bit except those lowest four.

The result `x` is always an integer from `0` through `15`.

For example, decimal `26` is binary `000...00011010`. At nibble position one, shifting right four gives binary `1`, so `x = 1`. At nibble position zero, masking the original low four bits gives binary `1010`, decimal ten.

**Map nibble values to lowercase characters**

The string

```text
chars = '0123456789abcdef'
```

acts as a lookup table. Its index equals the nibble value:

- indices `0..9` return decimal digit characters;
- indices `10..15` return `a..f`.

Thus `chars[10]` is `'a'`, and the two significant nibbles of 26 become `"1a"`.

Using a table avoids conditional arithmetic for alphabetic digits and guarantees lowercase output.

**Suppress only leading zero nibbles**

The result list `s` begins empty. The condition

```text
if s or x != 0:
```

means:

- before any significant digit, ignore a zero nibble;
- append the first nonzero nibble;
- after output has started, append every later nibble, including zero.

This distinction is essential. Leading zeros are forbidden, but zeros inside or at the end of the representation carry positional value. Decimal 256 is hexadecimal `100`; dropping the two low zero nibbles would incorrectly return `1`.

Once `s` is nonempty, its truth value keeps all remaining positions.

**Why negative Python integers still produce 32-bit two’s complement**

Python integers are not stored as fixed-width signed 32-bit values, and right shifting a negative number performs an arithmetic shift: conceptually, infinitely many leading one bits are copied. The final `& 0xF` is what makes this useful.

For each of the eight requested nibble positions, the mask selects exactly the four bits that a 32-bit two’s-complement representation has there. Infinite sign-extension bits above position 31 never enter the result because the loop stops at nibble seven.

For `num = -1`, arithmetic right shifting by any examined amount still gives `-1`, whose low four masked bits are `1111`. Every `x` equals fifteen, so the result is `"ffffffff"`.

For `num = -2`, the low nibble is `1110`, giving `e`, while all seven higher nibbles are `f`. The output is `"fffffffe"`.

An alternative implementation could first convert a negative value with `num += 2**32`. The exact nibble masking makes that explicit conversion unnecessary.

**Why negative outputs keep all eight digits**

In 32-bit two’s complement, every negative number has its most significant bit set. Therefore its top nibble is between `8` and `f`, never zero. Output begins immediately at `i = 7`, and all eight nibbles are appended.

This is correct: dropping high `f` or high sign-bearing digits would no longer display the full 32-bit bit pattern required by the contract.

**Tracing decimal 26**

For nibble positions seven down to two, extraction yields zero and `s` remains empty, so they are skipped.

At `i = 1`, extraction yields one. `x != 0`, so `'1'` is appended.

At `i = 0`, extraction yields ten. Since `s` is already nonempty, `'a'` is appended. Joining the list returns `"1a"`.

**A correctness argument**

The loop examines all eight disjoint four-bit groups of the signed 32-bit pattern in descending significance. Masking yields each group’s exact base-16 digit value, and the lookup table returns its canonical character.

Skipping zero groups only before the first nonzero group removes precisely the unnecessary leading zeroes. After output begins, no group is skipped, so place value is preserved. Negative values start in the highest group and therefore retain their complete two’s-complement representation. The separate zero branch supplies the only representation that would otherwise be empty.

Consequently the joined character sequence is exactly the required lowercase hexadecimal representation.

## Complexity detail

The loop always performs eight iterations because the input width is fixed at 32 bits. Every iteration does a bounded shift, mask, comparison, and optional append. Time complexity is $O(1)$.

The output contains at most eight characters, and the temporary list has the same fixed maximum size. Auxiliary space and output space are both $O(1)$ under the fixed-width contract.

This bounded domain is also why the package uses a bounded-domain complexity certificate: a legal input can never require more than eight hexadecimal digits. For a generalized $b$-bit integer, the analogous algorithm would take $O(b)$ time and space for the returned digits.

## Alternatives and edge cases

- **Repeated division by 16:** For a nonnegative value, repeatedly take remainder 16 and divide, then reverse the collected digits. Negative inputs first require conversion to their unsigned 32-bit value. This is correct but needs separate sign handling.

- **Add `2**32` for negatives:** Converting `num` to `num + 2**32` makes the unsigned two’s-complement value explicit, after which repeated division works. The exact masking method achieves the same result directly.

- **Built-in `hex`:** It would violate the explicit restriction against a direct library conversion and formats negative numbers with a minus sign rather than the required 32-bit two’s-complement representation.

- **`num = 0`:** The early return gives `"0"` instead of an empty string.

- **Small positive number:** High zero nibbles are skipped until its first significant digit.

- **Internal zero nibble:** Once output has started, zero is appended so values such as `0x1001` retain both middle zeros.

- **Positive maximum:** $2^{31}-1$ becomes `"7fffffff"`; the top nibble is seven because the sign bit is zero.

- **Negative one:** All 32 bits are one, producing eight `f` characters.

- **Minimum signed value:** $-2^{31}$ has bit pattern `1000...0`, producing `"80000000"`.

- **Lowercase requirement:** The lookup table uses `abcdef`, never uppercase letters.

- **Python sign extension:** Arithmetic right shift is safe here only because each extracted group is masked and exactly eight 32-bit groups are examined.

- **No leading-zero output for positives:** The `s or x != 0` gate starts output at the first nonzero nibble and preserves every later position.
