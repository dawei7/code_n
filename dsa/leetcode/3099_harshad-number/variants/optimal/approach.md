## General

Preserve the original value because extracting its digits will consume a working copy. Repeatedly take `x % 10` to obtain the last decimal digit, add it to `digit_sum`, and remove that digit with `x //= 10`. When the working copy reaches zero, every digit has contributed exactly once.

The original number is a Harshad number precisely when `original % digit_sum == 0`. In that case, return the computed sum; otherwise, return `-1`. Since the contract guarantees that the original number is positive, at least one nonzero or positive digit is processed and `digit_sum` cannot be zero.

This follows directly from decimal representation: division by ten discards the digit just recovered by the remainder, so the loop visits all digits without omission or duplication. The final remainder test is exactly the definition of divisibility by the digit sum.

## Complexity detail

An integer `x` has $O(\log x)$ decimal digits, and each loop iteration removes one digit, so the running time is $O(\log x)$. Only the original value, the working copy, and the accumulated sum are stored, giving $O(1)$ auxiliary space. Under the legal bound $x \le 100$, at most three iterations occur; the package therefore uses a bounded-domain certificate backed by exhaustive validation rather than a misleading scaling benchmark over only one-, two-, and three-digit inputs.

## Alternatives and edge cases

- **Convert to text:** Sum `int(character)` for every character in `str(x)`. This is concise and has the same asymptotic time, but allocates a string proportional to the digit count.
- **Use fixed decimal places:** Because `x <= 100`, hundreds, tens, and ones can be extracted with fixed arithmetic. That is valid for this exact bound but less general than consuming digits in a loop.
- **Single-digit values:** Every integer from `1` through `9` is divisible by its only digit, so the returned sum equals the input.
- **Zeros inside the representation:** A zero digit contributes nothing to the sum but must not terminate extraction; `100` correctly has digit sum `1`.
- **Positive-input guarantee:** There is no division-by-zero case because `x >= 1` ensures a positive digit sum.
