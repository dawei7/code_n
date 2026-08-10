## General

The definition asks whether the sum of the squares of the decimal digits exceeds the ordinary digit sum by at least `50`. If the digits of `n` are `d_1,d_2,\ldots,d_D`, the direct expression is

$$
\left(\sum_{i=1}^{D} d_i^2\right)
-
\left(\sum_{i=1}^{D} d_i\right)
\ge 50.
$$

A literal implementation could maintain two accumulators and subtract them after all digits have been visited. The Optimal source makes a small but useful algebraic simplification first. Because subtraction distributes over a sum,

$$
\sum_{i=1}^{D} d_i^2-\sum_{i=1}^{D}d_i
=
\sum_{i=1}^{D}(d_i^2-d_i)
=
\sum_{i=1}^{D}d_i(d_i-1).
$$

Therefore each digit can contribute its complete effect on the final difference immediately. The variable `s` stores this accumulated difference; it is not the ordinary digit sum despite its short name.

**Why the per-digit transformation is safe**

The transformation does not approximate or change the condition. For every digit `d`, `d(d-1)` is exactly `d^2-d`. Adding these terms for all digits is exactly the requested square-sum minus digit-sum.

This form also reveals useful behavior:

- digit `0` contributes `0(0-1)=0`;
- digit `1` contributes `1(1-1)=0`;
- every digit from `2` through `9` contributes a positive amount;
- the largest single-digit contribution is `9 \cdot 8=72`.

Thus zeros and ones do not affect goodness, while sufficiently large digits can make the threshold reachable quickly. The source still processes all digits rather than returning early, which keeps the code simple and exactly matches the final comparison.

**Extracting decimal digits without building a string**

The loop uses

```python
n, x = divmod(n, 10)
```

For a nonnegative integer, division by ten separates the number into two parts. The quotient is the number with its last decimal digit removed, and the remainder is that last digit. Python's `divmod(n, 10)` returns both values together. The quotient is assigned back to the local variable `n`, and the remainder is assigned to `x`.

The next line,

```python
s += x * (x - 1)
```

adds `x^2-x` to the accumulated difference. Repeating this process removes one decimal digit per iteration. Eventually the quotient becomes zero and `while n` stops.

At the start of each iteration, `s` equals the sum of `d(d-1)` over every digit already removed from the original number. The still-unprocessed prefix is held in `n`. The iteration extracts exactly its final digit, adds exactly that digit's contribution, and replaces the prefix with the remaining quotient. When the loop terminates, no digits remain in the prefix, so `s` equals the complete square-sum minus digit-sum.

Finally,

```python
return s >= 50
```

uses `>=` because a difference equal to `50` is good; it does not have to be strictly greater.

**A complete trace**

Consider `n=529`. Initially `s=0`.

1. `divmod(529, 10)` gives quotient `52` and digit `9`. The contribution is `9 \cdot 8=72`, so `s=72`.
2. `divmod(52, 10)` gives quotient `5` and digit `2`. The contribution is `2 \cdot 1=2`, so `s=74`.
3. `divmod(5, 10)` gives quotient `0` and digit `5`. The contribution is `5 \cdot 4=20`, so `s=94`.

The loop ends, and `94 \ge 50` is true. Checking from the definition gives the same result: the square-sum is `25+4+81=110`, the digit sum is `5+2+9=16`, and their difference is `94`.

For contrast, `n=123` contributes `1\cdot0+2\cdot1+3\cdot2=8`, so it is not good.

Reassigning the parameter name `n` does not modify an integer owned by the caller. Python integers are immutable, and the assignment merely makes the local name refer to the next quotient.

## Complexity detail

Let `D` be the number of decimal digits in `n`. Every loop iteration removes exactly one digit, and each iteration performs a constant amount of arithmetic and assignment. The running time is therefore `O(D)`.

For positive `n`,

$$
D=\lfloor \log_{10} n \rfloor+1,
$$

so the same bound is commonly written as `O(\log n)`. The logarithm's base is irrelevant in big-O notation.

The algorithm keeps only the shrinking local value `n`, the extracted digit `x`, and the accumulator `s`. It does not allocate a list or string of digits. Its auxiliary space complexity is therefore `O(1)`.

The accumulator cannot decrease for decimal digits because every `x(x-1)` is nonnegative for `x \in \{0,\ldots,9\}`. This monotonicity is useful for intuition, although it is not required for the asymptotic analysis or for the final correctness of the comparison.

As with ordinary integer problems, these bounds use the standard unit-cost model for constrained arithmetic. Python supports arbitrary-precision integers, but the problem's normal input limits make each division and multiplication a constant-cost primitive for this analysis.

## Alternatives and edge cases

- **Two separate accumulators:** Summing `x` into one variable and `x^2` into another, then comparing their difference, is correct and has the same asymptotic bounds. The source's single accumulator more directly tracks the only quantity the answer needs.

- **String conversion:** Converting `n` to text and iterating over characters is also `O(D)` time, but it allocates `O(D)` extra storage for the decimal representation. Arithmetic extraction preserves constant auxiliary space.

- **Precomputed digit contributions:** A ten-entry table for `d(d-1)` could replace the multiplication. Because there are only ten possible digits, this remains correct, but it adds a collection without changing the asymptotic or practical structure of the solution.

- **Early success return:** Since contributions are nonnegative, the function could return `True` as soon as `s` reaches `50`. That optimization is valid for nonnegative decimal digits, but the source deliberately performs the straightforward full scan. Its worst-case complexity remains the same.

- **Threshold equality:** A final difference of exactly `50` must return `True`. The source correctly uses `>= 50` rather than `> 50`.

- **Digits zero and one:** These digits contribute zero, not a negative value. The factored form `d(d-1)` makes this explicit and shows that leading zeros, if decimal notation had them, would not matter.

- **Single large digit:** A number containing digit `9` already receives `72` from that digit alone and is therefore good regardless of its other digits. Digit `8` contributes `56` and has the same implication.

- **Input zero:** If zero is allowed, the loop executes zero times and returns whether `0 \ge 50`, which is `False`. This agrees with treating zero's only digit as `0`, whose contribution is zero.

- **Negative integers:** The digit-extraction loop is designed for the nonnegative input domain. Python floor division keeps a negative quotient negative in cases such as `divmod(-1, 10)`, so extending the problem to negatives without taking an absolute value could fail to terminate. That extension is outside the stated contract and should not be inferred from the concise loop.

- **Local parameter update:** Assigning the quotient back to `n` is safe because it changes only the function's local binding. The caller's integer value is immutable and remains unchanged.

- **No constant-time shortcut from the whole number:** The condition depends on every decimal digit rather than only the numerical magnitude. In the worst case all `D` digits must be inspected, making the digit scan asymptotically appropriate.
