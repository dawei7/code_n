## General

The last decimal digit of a positive integer `x` is `x % 10`. Removing that digit is integer division by ten, `x //= 10`. Repeating these operations visits the digits in exactly the order required for the reversal.

Maintain `reversed_n`, initially zero. For each extracted digit, shift the digits already collected one decimal place left with `reversed_n * 10`, then add the new digit. When no digits remain, `reversed_n` is the reversed integer. If `n` ends in zeros, they are extracted first but cause no numerical change while `reversed_n` is still zero, which correctly discards the leading zeros of the reversed representation.

Finally return `abs(n - reversed_n)`, directly applying the mirror-distance definition.

## Complexity detail

Let $D$ be the number of decimal digits in `n`, so $D=\lfloor\log_{10} n\rfloor+1$. The loop processes each digit once, taking $O(D)=O(\log N)$ time. It stores only two integers besides the input, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **String reversal:** Convert `n` to text, reverse the characters, and parse the result. This is concise and also takes $O(\log N)$ time, but it allocates $O(\log N)$ character space.
- **One digit:** Reversal leaves any one-digit input unchanged, so its mirror distance is `0`.
- **Trailing zeros:** Zeros at the end of `n` become leading zeros in the reversed digit sequence and have no effect on its integer value.
- **Palindromes:** If the decimal digits read the same in both directions, `n == reverse(n)` and the answer is `0`.
- **Absolute value:** Reversal may be either larger or smaller than `n`; the subtraction must be made nonnegative.
