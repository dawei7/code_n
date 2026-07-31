## General

**Inspect the decimal digits arithmetically**

For a positive integer, `n % 10` extracts its least significant decimal digit and `n //= 10` removes that digit. Repeating those operations visits every digit from right to left. Record whether any extracted digit equals `x`.

The digit extracted in the final iteration is the most significant digit of the original number. Keep overwriting `leading_digit` during the scan; when the loop ends, it therefore stores exactly the digit that determines whether the number starts with `x`. The result is true precisely when an occurrence was found and `leading_digit != x`.

**Why zero is handled separately**

The usual decimal representation of `0` is `0`, but an arithmetic loop conditioned on `n > 0` would perform no iterations. Returning `false` directly is correct for every `x`: when `x = 0`, the required digit occurs but is also the leading digit; when `x` is nonzero, it does not occur at all.

For a positive input, every decimal digit is extracted exactly once. Thus `found` is true exactly when the representation contains `x`, and the last extracted digit is exactly the first written digit. Combining those two facts implements both validity conditions without constructing a string.

## Complexity detail

Let $D$ be the number of decimal digits in `n`, taking $D=1$ when `n=0`. A positive input performs one constant-time iteration per digit, so the running time is $O(D)=O(\log N)$. The zero case returns immediately.

Only the current digit, a Boolean occurrence flag, and the leading digit are stored. The auxiliary space is therefore $O(1)$.

## Alternatives and edge cases

- **Convert to a string:** Checking membership and the first character is concise and still takes $O(\log N)$ time, but it allocates $O(\log N)$ character space.
- **Check only membership:** Finding `x` somewhere is insufficient when the most significant digit is also `x`; both conditions must be evaluated.
- **Stop at the first occurrence:** An early match does not reveal the leading digit unless that digit was determined separately, so the scan must either continue or compute the leading digit first.
- **Zero input:** `0` is written with one digit. It is invalid for `x = 0` because it starts with `0`, and invalid for every other `x` because that digit is absent.
- **Single positive digit:** If it equals `x`, the number starts with `x`; otherwise `x` is absent. Every one-digit number is therefore invalid.
- **Repeated target digits:** Multiple occurrences do not change the Boolean result; one non-leading occurrence is enough only when the leading digit differs from `x`.
