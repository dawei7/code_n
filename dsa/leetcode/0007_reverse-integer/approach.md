## General

**Pop one decimal digit and push it onto the reversed value**

Reversing a base-10 integer can be done without converting it to text. Repeatedly separate the last digit from `x`, remove that digit from `x`, and append it to the right side of `ans`.

Appending a digit `y` to an existing decimal number is

$$
\texttt{ans}_{new} = 10 \cdot \texttt{ans}_{old} + y.
$$

For a positive example, start with `x = 123` and `ans = 0`:

| Iteration | Popped `y` | Remaining `x` | New `ans` |
|---:|---:|---:|---:|
| 1 | `3` | `12` | `3` |
| 2 | `2` | `1` | `32` |
| 3 | `1` | `0` | `321` |

The loop ends when no digits remain. A trailing zero in the original becomes an early popped zero. For `120`, the updates are `0`, `2`, and `21`; integers do not retain a leading zero, so the correct result is `21`.

**Why negative digits need special handling in Python**

Many languages define integer division and remainder by truncating toward zero. Under that convention, the last digit of `-123` is `-3`. Python's `//` instead floors toward negative infinity, and `%` returns a nonnegative remainder when the divisor is positive:

```text
-123 % 10 == 7
-123 // 10 == -13
```

Those results are valid Euclidean division, but `7` is not the signed decimal digit the reversal needs.

The code first calculates

```python
y = x % 10
```

and then corrects a nonzero remainder when `x` is negative:

```python
if x < 0 and y > 0:
    y -= 10
```

For `x = -123`, `y` changes from `7` to `-3`. For a negative multiple of ten such as `-120`, the remainder is already `0` and must stay zero, which is why the condition also requires `y > 0`.

Once the signed last digit is known, the remaining integer is computed by

```python
x = (x - y) // 10
```

Subtracting `y` makes the numerator an exact multiple of ten, so floor division and truncation toward zero now agree. For `-123`, this becomes `(-123 - (-3)) // 10 = -120 // 10 = -12`.

The algorithm therefore keeps the sign inside every digit instead of taking `abs(x)` and reapplying a separate sign at the end. That is especially useful in fixed-width reasoning because the magnitude of $-2^{31}$ cannot be represented as a positive signed 32-bit integer.

**The decimal reversal relationship after each iteration**

Suppose `t` digits have been processed. `ans` is those `t` original low-order digits in reversed order, with the original sign. The current `x` is the original integer with exactly those low-order digits removed by truncation toward zero.

The signed remainder logic extracts the next low-order digit `y`. Multiplying `ans` by ten opens one decimal position, and adding `y` places the digit there. Updating `(x - y) // 10` removes exactly the same digit from the unprocessed portion. Thus each loop iteration transfers one digit from the end of `x` to the end of `ans`, preserving the reversal interpretation.

When `x` reaches zero, every original digit has been transferred and `ans` is the complete digit reversal.

**Check overflow before multiplying by ten**

The legal range is stored as

```python
mi, mx = -(2**31), 2**31 - 1
```

or

$$
\texttt{mi} = -2147483648,
\qquad
\texttt{mx} = 2147483647.
$$

The dangerous operation is `ans * 10 + y`. In a fixed-width environment, calculating an overflowing intermediate and checking afterward would be too late. The method instead tests the prefix before the multiplication:

```python
if ans < mi // 10 + 1 or ans > mx // 10:
    return 0
```

Python floor division gives

```text
mi // 10 + 1 == -214748364
mx // 10     ==  214748364
```

If `ans` is below `-214748364`, multiplying by ten is already below the minimum even before a digit is added. If it is above `214748364`, multiplying by ten is already above the maximum. Returning zero at that point is mandatory.

**Why this code does not separately check the boundary digit**

A general-purpose push check often has two extra cases:

- when `ans == 214748364`, the next digit must be at most `7`;
- when `ans == -214748364`, the next digit must be at least `-8`.

This implementation omits those explicit comparisons. Under this problem's input constraint, the omission is safe for a subtle reason.

Reaching either nine-digit boundary in `ans` means that the loop has already consumed nine digits and is about to pop the original number's most-significant tenth digit. Any legal positive 32-bit ten-digit input begins with `1` or `2`, so that final positive digit is never greater than `7`. Any legal negative ten-digit input has magnitude at most `2147483648`, so its final signed digit is `-1` or `-2`, never less than `-8`.

Therefore a boundary prefix that survives the strict test cannot be pushed out of range by the only digit a legal input can still provide. If this function accepted arbitrary-size input integers, that argument would fail and explicit `7`/`-8` boundary checks would be required.

**Trace the negative example**

For `x = -123`:

| Old `x` | Python `x % 10` | Corrected `y` | New `ans` | New `x` |
|---:|---:|---:|---:|---:|
| `-123` | `7` | `-3` | `-3` | `-12` |
| `-12` | `8` | `-2` | `-32` | `-1` |
| `-1` | `9` | `-1` | `-321` | `0` |

The sign naturally remains negative in `ans`; no final multiplication by a sign variable is needed.

If the guard ever proves that the next push would overflow, returning `0` immediately is correct because adding more reversed digits cannot repair an already invalid 32-bit prefix.

## Complexity detail

Let $d$ be the number of decimal digits in $\lvert x \rvert$. For nonzero `x`, $d = \lfloor\log_{10}\lvert x\rvert\rfloor + 1$.

- **Time complexity: $O(d) = O(\log\lvert x\rvert)$.** Each iteration removes one decimal digit and performs a constant amount of arithmetic and comparison work. For `x = 0`, the loop is skipped and the work is $O(1)$.
- **Space complexity: $O(1)$.** The method stores only `ans`, two limits, one digit, and the shrinking integer. It creates no string, list, recursion chain, or other input-sized structure.

Because the contract fixes `x` to 32 bits, there are at most ten decimal digits, so runtime is technically bounded by a small constant over the legal domain. The logarithmic notation describes how the arithmetic method scales with the number's magnitude and matches the manifest.

## Alternatives and edge cases

- **Extract an absolute magnitude and restore the sign:** This is simple in Python, but in a true signed 32-bit environment `abs(-2**31)` is not representable. Keeping signed digits avoids that special overflow.
- **Convert to a string:** Reverse the digit characters and parse the result. This uses $O(d)$ extra storage and sidesteps the intended arithmetic/overflow reasoning. It also still needs sign and range handling.
- **Post-update overflow check:** Python's arbitrary-precision integers make it possible to build a large result and compare afterward, but the stated environment forbids relying on a wider integer. A pre-update guard is the portable design.
- **General unrestricted-input guard:** For arbitrary-size input, add explicit boundary-digit checks for `7` and `-8` before the push. The shorter current guard depends on the original input already lying in the 32-bit range.
- **Zero:** The loop does not run and `ans = 0` is returned.
- **Trailing zeros:** Popped zero digits do not create leading zeros in an integer result. `120` becomes `21`, and `-120` becomes `-21`.
- **Negative multiples of ten:** Their Python remainder is zero, so the `y > 0` condition correctly avoids changing it to `-10`.
- **Most-negative input:** The algorithm never forms its positive magnitude. It processes signed digits and either returns the valid reversal or zero.
- **Overflowing reversal:** A legal input such as `1534236469` eventually creates an unsafe prefix, and the pre-push guard returns zero.
- **Reversal within range:** Values whose reversed form lies in `[mi, mx]` complete the loop and return that signed result.
- **Sign only affects digits:** No minus symbol is treated as a decimal position; negative digits accumulate the sign arithmetically.
