## General

Repeatedly summing decimal digits produces a number's **digital root**. Simulating the process works, but the follow-up asks for a constant-time solution without a loop or recursion. The exact solution uses the fact that a decimal number and the sum of its digits always have the same remainder modulo 9.

**Why digit sums preserve modulo 9**

Write a nonnegative decimal integer using digits $d_0,d_1,\ldots,d_k$:

$$
n=d_0+d_1\cdot10+d_2\cdot10^2+\cdots+d_k\cdot10^k.
$$

Because $10\equiv1\pmod9$, every power of ten also satisfies

$$
10^i\equiv1^i\equiv1\pmod9.
$$

Taking the decimal expansion modulo 9 therefore gives

$$
n\equiv d_0+d_1+d_2+\cdots+d_k\pmod9.
$$

So replacing a number by the sum of its digits does not change its remainder modulo 9. Applying the operation repeatedly preserves that same remainder at every stage, including the final one-digit result.

**Which one-digit value represents each remainder**

For a positive input, the final digital root must be one of `1` through `9`. These nine values represent the nine remainder classes modulo 9:

| Remainder modulo 9 | Positive digital root |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 0 | 9 |

The last row is the subtle one. A positive multiple of 9 has remainder zero, but its repeated digit sum cannot end at `0`: sums of the digits of a positive integer remain positive. Its correct digital root is `9`. The number zero itself is different; it begins and ends at `0`.

That gives the piecewise rule

$$
\operatorname{dr}(n)=
\begin{cases}
0,&n=0,\\
9,&n>0\text{ and }n\equiv0\pmod9,\\
n\bmod9,&\text{otherwise}.
\end{cases}
$$

**How the compact formula merges the positive cases**

For a positive number, the source computes

```text
(num - 1) % 9 + 1
```

Subtracting one shifts the positive range `1..9` to the zero-based range `0..8`. Modulo 9 then cycles every positive integer into that range, and adding one shifts the result back to `1..9`.

If `num` is not divisible by 9, this expression returns its ordinary remainder. For example, `38 - 1 = 37`, `37 % 9 = 1`, and adding one yields `2`.

If `num` is a positive multiple of 9, then `num - 1` has remainder `8`; adding one produces `9`, exactly handling the otherwise awkward zero-remainder case. For `18`, the calculation is `(18 - 1) % 9 + 1 = 17 % 9 + 1 = 8 + 1 = 9`.

Zero must remain a separate branch. Applying the positive formula to zero in Python would evaluate `(-1) % 9 + 1` as `8 + 1 = 9`, which is incorrect. The conditional `0 if num == 0 else ...` returns the required `0` before using the formula.

**Trace of the repeated process and the formula**

For `num = 38`, explicit digit summing gives

```text
38 -> 3 + 8 = 11 -> 1 + 1 = 2
```

Modulo 9 reaches the same conclusion immediately:

$$
(38-1)\bmod9+1=37\bmod9+1=1+1=2.
$$

For `num = 999`, explicit summing gives `27`, then `9`. Since `999` is a positive multiple of 9, the compact expression returns `9`, not zero.

For a number already from `1` through `9`, subtracting one produces `0` through `8`; modulo does nothing, and adding one restores the same digit. Thus the formula also handles the stopping case naturally.

**Why the result is the repeated digit sum, not merely a matching remainder**

Every digit-sum step preserves the modulo-9 class. Repeated summing must terminate because any number with at least two digits is replaced by a much smaller sum, and eventually a one-digit value remains. For positive input, that value lies in `1..9`. Within `1..9`, exactly one value represents the input's modulo-9 class according to the table above. The formula returns that unique value, so it must equal the terminal repeated digit sum.

## Complexity detail

The implementation performs one equality check and, for a positive input, one subtraction, one modulo operation, and one addition. The number of operations does not depend on the number of decimal digits, so under the fixed-width integer model and the stated 32-bit input bound, time complexity is $O(1)$.

It allocates no array, string, recursion frame, or other size-dependent structure. Auxiliary space is $O(1)$.

In an arbitrary-precision bit-complexity model, arithmetic cost can depend on the number of bits in `num`. That distinction is irrelevant here because the input is bounded by $2^{31}-1$ and the problem's intended model treats integer arithmetic as constant time.

## Alternatives and edge cases

- **Direct digit-sum simulation:** Repeatedly extract digits with `% 10` and `// 10` until one digit remains. It is easy to discover but uses loops and takes time proportional to the digits processed, missing the constant-time follow-up.
- **String conversion:** Convert the number to text and sum converted characters repeatedly. This is more allocation-heavy and still iterative.
- **Three-branch modulo formula:** Return `0` for zero, `9` for positive multiples of 9, and `num % 9` otherwise. It is equivalent to the exact compact expression but uses an additional explicit case.
- **`num = 0`:** This is the only input whose digital root is zero. It must be handled before the positive formula.
- **Positive multiple of 9:** The result is `9`, not `0`; subtracting one before modulo encodes this distinction.
- **Already one digit:** Values `1` through `9` map to themselves, while zero is handled separately.
- **Largest permitted input:** The formula uses only bounded integer arithmetic and does not depend on how many decimal digits the value contains.
- **Nonnegative-input assumption:** The mathematical digital root can be extended to negatives with a chosen convention, but the source and contract define only `num >= 0`.
- **Decimal-base dependency:** Modulo 9 appears because $10\equiv1\pmod9$. In base $b$, the analogous positive digital-root formula uses modulo $b-1$.
- **Divisibility intuition:** The familiar rule “a number is divisible by 9 exactly when its digit sum is divisible by 9” is a consequence of the same congruence used here.
