## General

**Convert both strings to exact fractions**

Repeating decimals can have different spellings for the same rational value. Text comparison or a fixed decimal expansion is unreliable, especially for `0.999... = 1`.

The solution parses each representation into Python's exact `Fraction` type. Fractions reduce to canonical numerator and denominator, so equality becomes mathematical equality.

**Separate the repeating part**

Variable `repeating` begins empty.

If `"("` appears, `text[:-1]` removes the closing parenthesis, then splitting at the opening one produces `main` and `repeating`.

Without parentheses, the entire input is `main`.

For `"123.00(1212)"`, main is `"123.00"` and repeating is `"1212"`.

**Separate integer and finite digits**

If main contains a decimal point, splitting it gives integer and non-repeating parts. The latter may be empty, as in `"1."`.

Without a decimal point, main is the integer and finite part is empty.

Initial value is `Fraction(int(integer), 1)`.

**Convert the finite decimal**

If finite string has `m` digits and integer value `A`, its contribution is `A / 10^m`.

The code adds `Fraction(int(non_repeating), 10**m)`.

Leading zeros remain meaningful through denominator length. Digits `"0012"` become `12/10000`, not `12/100`.

**Convert the repeating decimal**

If repeating block has `r` digits and integer value `B`, infinite repetition has value `B / (10^r - 1)`.

After `m` finite digits, the tail shifts right by `m` places:

`B / (10^m * (10^r - 1))`.

This is exactly the code's denominator.

For `0.1(6)`, finite contribution is `1/10` and repeating contribution `6/(10*9) = 1/15`. Their sum is `1/6`.

**Why the repeating formula works**

Let `z = 0.(B)` with block length `r`. Then `10^r z = B + z`.

Subtracting gives `(10^r - 1)z = B`, hence the formula. The finite prefix adds the factor `10^m`.

**Why `0.9(9)` equals `1.`**

Parsing `0.9(9)` gives finite `9/10` and repeating `9/(10*9) = 1/10`. Their sum is exactly one.

Parsing `1.` is also one. Fraction equality returns true without approximation or a special nine rule.

**Canonical equality**

`Fraction` reduces with greatest common divisors. `0.(52)` and `0.5(25)` may initially construct different numerator-denominator expressions, but both normalize to the same rational.

The outer method returns `parse(s) == parse(t)`.


Parsing adds three disjoint positional contributions: integer, finite decimal, and shifted repeating tail. Each formula equals its source digits' mathematical value.

Thus `parse` returns the exact represented rational number. Exact equality is true precisely when inputs represent the same number.

**Why no carry normalization is needed manually**

Representations with repeating nines effectively carry into an earlier digit. Fraction addition and reduction perform this algebra automatically.

Likewise, repeating zeros contribute zero and need no trimming. The parser can preserve the original parts while the numeric representation supplies canonicalization.

**Detailed equivalence example**

For `0.(52)`, repeating contribution is `52/99`.

For `0.5(25)`, finite part is `5/10` and repeating tail is `25/(10*99)`. Their sum is `495/990 + 25/990 = 520/990 = 52/99`.

The different strings therefore normalize to the same exact fraction.

**Why splitting is unambiguous**

The syntax has at most one decimal point. Parentheses are removed before splitting `main`, so integer and finite parts are isolated exactly.

The integer part is guaranteed nonempty. The repeating part is guaranteed nonempty whenever parentheses occur.

**Why period length preserves leading zeros**

Block `"09"` represents `9/99`, not `9/9`. Integer conversion drops the leading zero in the numerator, but `len(repeating)` keeps the two-digit denominator.

The same principle preserves finite leading zeros through `10^finite_length`.

**Exact arithmetic avoids infinite expansion**

The algorithm never materializes endlessly repeating digits. A finite numerator and denominator represent the complete infinite sequence.

This avoids arbitrary cutoffs and also handles periods written with different alignments or repeated copies.

**Valid denominators**

Repeating length is at least one, so `10^r - 1` is positive. Finite scaling is also positive. Every constructed fraction has a nonzero denominator.

**Parsing each input independently**

The helper has no shared state between `s` and `t`. Each string is converted solely from its own characters, and only the final normalized values are compared.

This prevents one representation's period length or decimal position from influencing the other. Equivalent inputs meet only through exact rational equality.

## Complexity detail

Let `L` be total input characters.

Splitting, integer conversion, and power construction process `O(L)` digits. With bounded lengths arithmetic is tiny; general textual time is `O(L)`.

Substrings and numeric objects use `O(L)` representation space.

## Alternatives and edge cases

- **Expand repetitions many times:** Approximate and may miss equality beyond the cutoff.
- **Floating point:** Rounding makes exact equality unsafe.
- **Manual normalized numerator:** Correct but duplicates `Fraction` behavior.
- **No decimal point:** Only integer contributes.
- **Trailing decimal point:** Empty finite part contributes zero.
- **Repeating zeros:** Tail is zero.
- **Repeating nines:** Fraction reduction handles carrying.
- **Leading fractional zeros:** Denominator length preserves positions.
- **Different period spellings:** Equivalent blocks normalize identically.
- **Nonnegative inputs:** No sign parsing is needed.
