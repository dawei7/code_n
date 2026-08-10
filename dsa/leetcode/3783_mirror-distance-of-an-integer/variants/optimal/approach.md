## General

**Follow the decimal definition directly**

The mirror value is obtained by writing `n` in ordinary decimal form, reversing that finite digit sequence, and interpreting the result as an integer. The source expresses those three steps as

`int(str(n)[::-1])`.

`str(n)` produces the digits with no sign or leading zeros because `n` is positive. The slice `[::-1]` visits the complete string backward. Finally, `int(...)` converts the reversed spelling back to its numeric value.

The method returns the absolute difference between the original and this reversed value:

`abs(n - int(str(n)[::-1]))`.

Absolute value is needed because reversal may make the number either larger or smaller.

**Understand the reversal slice**

Python slicing has the form `sequence[start:stop:step]`. Omitting start and stop selects the whole string, while step `-1` traverses it from the final character to the first.

For `n=25`:

- `str(n)` is `"25"`;
- reversing gives `"52"`;
- integer conversion gives 52;
- `abs(25-52)` is 27.

For a one-digit number such as 7, reversal produces the same one-character string, so the mirror distance is zero.

**Let integer conversion handle newly leading zeros**

Trailing zeros in the original number become leading zeros in the reversed digit sequence. Decimal integer values do not retain leading zeros, and `int` applies exactly that rule.

For `n=10`, the intermediate reversed string is `"01"`. Converting it yields integer 1, so the result is nine.

For `n=1200`, the reversed string is `"0021"` and the mirror integer is 21. The source does not need to strip zeros manually.

Zeros in other positions remain meaningful. Reversing 102 produces `"201"`, so its mirror is 201 rather than 21.

**Why the expression returns exactly the contract value**

The decimal string contains each digit of `n` exactly once and in left-to-right order. Traversing that string with step negative one produces exactly the same digits in the opposite order—none are omitted, duplicated, or changed.

Integer conversion implements the specified interpretation of the reversed sequence, including removal of leading zeros. The subtraction compares the two required integers, and `abs` removes direction while preserving their numeric distance.

Every operation in the expression corresponds to one clause of the definition, so there is no search, greedy choice, or special numeric case left unresolved.

**Distinguish palindrome from mirror distance**

A decimal palindrome reads the same in both directions, so its mirror distance is zero. However, trailing zeros can also affect equality through numeric interpretation only in predictable ways; a positive number ending in zero cannot equal its shorter reversed positive value unless outside the given ordinary representation rules.

The method does not need to test palindrome status separately. If the values are equal, subtraction and absolute value naturally return zero.

**The source differs from the editorial and manifest narrative**

The local editorial and manifest describe arithmetic digit extraction with remainder and integer division. The exact Optimal source does not use a loop, modulo, or division; it uses string conversion and slicing.

Both strategies compute the same mirror integer, but their storage analysis differs. The source allocates decimal strings proportional to the digit count. Its generalized auxiliary space is $O(D)$, not the arithmetic approach's $O(1)$.

Under the explicit constraint `n <= 10^9`, at most ten characters are allocated, so this storage is bounded by a constant in the problem's fixed domain. The approach should still describe the actual objects created.

## Complexity detail

Let $D$ be the number of decimal digits, where $D=\lfloor\log_{10}n\rfloor+1$.

Creating `str(n)` takes $O(D)$ time. The reverse slice creates and fills another $D$-character string, and integer parsing also scans $D$ characters. Subtraction and absolute value are constant-time under the usual fixed-width problem model. Total time is $O(D)=O(\log n)$.

The original decimal string and reversed slice require $O(D)=O(\log n)$ temporary space in a generalized analysis. With the documented ten-digit ceiling, this simplifies to bounded $O(1)$ space, but it is not the loop-based constant-storage implementation described by the manifest.

## Alternatives and edge cases

- **Arithmetic reversal:** Repeatedly append `n%10` to a numeric accumulator and apply `n//=10`. It uses constant scalar storage and matches the editorial, but is not the exact source.
- **Manual character loop:** Prepending or collecting digits can reproduce the slice but is more verbose.
- **Forget `int` conversion:** Subtracting strings is invalid, and preserving `"01"` as text misses its numeric value of one.
- **Strip every zero:** Only leading zeros of the reversed spelling lose significance; internal and trailing reversed zeros remain part of the number.
- **One-digit input:** Reversal is identical and the result is zero.
- **Decimal palindrome:** The two numeric values match, so the result is zero.
- **Original trailing zeros:** They become harmless leading zeros in the reversed string.
- **Original internal zeros:** They move to new internal positions and remain significant.
- **Reversal larger than `n`:** `abs` handles the negative raw difference.
- **Reversal smaller than `n`:** `abs` preserves the positive distance.
- **Maximum legal input:** At most ten digits are processed.
- **Positive-input guarantee:** There is no minus sign to position during string reversal.
- **Source/manifest mismatch:** This exact implementation uses $O(D)$ temporary string storage even though the arithmetic alternative can use $O(1)$.
