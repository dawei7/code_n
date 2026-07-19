## General
**Represent every error exactly:** Parse each price into its integer part and a fractional part measured in thousandths. Integer arithmetic avoids binary floating-point rounding when producing the required three-decimal string. Rounding a price with fractional part $f$ down contributes $f$ thousandths of error; rounding it up contributes $K-f$.

**Determine how many prices must round up:** Begin by rounding every price down. If that floor sum is $F$, exactly `target - F` non-integer prices must instead round up, because each such change raises the rounded sum by one. Integer prices cannot change the sum: their floor and ceiling are identical. A negative required count or a count larger than the number of non-integer prices makes the target impossible.

**Choose the cheapest changes:** Relative to rounding down, rounding a fractional part $f$ up changes the error by

$$
(K-f)-f=K-2f.
$$

This change decreases as $f$ grows, so the required prices to round up must have the largest fractional parts. Count occurrences of every possible thousandths value and consume those counts from $K-1$ downward. Start with the all-floor error, add `K - 2 * fraction` for every selected upward rounding, and format the resulting integer number of thousandths.

An exchange confirms optimality: if a solution rounds up a smaller fraction $a$ while rounding down a larger fraction $b$, swapping those choices preserves the rounded sum and changes the error by $2(a-b) \le 0$. Repeating the exchange leaves exactly the largest required fractions rounded up without increasing error.

## Complexity detail
Parsing the $N$ prices and filling the fractional-frequency array takes $O(N)$ time. Traversing its $K$ entries takes $O(K)$ time. The count array uses $O(K)$ auxiliary space; no per-price sorting or dynamic-programming table is needed.

## Alternatives and edge cases
- **Sort fractional parts:** Sorting them in descending order and choosing the largest required fractions is straightforward but costs $O(N\log N)$ time and $O(N)$ space.
- **Dynamic programming by upward-round count:** It can minimize the error for every possible count, but it repeats equivalent work and requires $O(N^2)$ time.
- **Floating-point arithmetic:** It risks an incorrectly formatted last decimal digit; parsing thousandths as integers is exact.
- **Integral price:** A fraction of zero contributes no error and cannot increase the rounded sum, because floor and ceiling are equal.
- **Target below the floor sum:** No rounding choice can reduce the sum enough, so return `"-1"`.
- **Target above the ceiling sum:** There are too few non-integer prices to supply the required increases, so return `"-1"`.
- **All floors or all ceilings:** A required upward count of zero or of every non-integer price is valid and handled without a special formula.
- **Equal fractional parts:** Their individual identities do not matter because they produce equal error changes.
