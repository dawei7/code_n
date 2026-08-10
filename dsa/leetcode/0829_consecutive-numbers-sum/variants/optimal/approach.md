## General

**Describe a sequence by its first value and length**

Suppose `n` is written as `k` consecutive positive integers beginning with `a`:

$$
n=a+(a+1)+(a+2)+\cdots+(a+k-1).
$$

There are `k` copies of `a`, and the added offsets sum to `0+1+\cdots+(k-1)=k(k-1)/2`. Therefore,

$$
n=ka+\frac{k(k-1)}2.
$$

Multiplying by two avoids fractions:

$$
2n=k(2a+k-1).
$$

For a fixed length `k`, this equation determines at most one starting value:

$$
2a=\frac{2n}{k}-k+1.
$$

The problem is therefore not asking us to search over every possible start. We can try each feasible length `k` and test whether the formula produces a positive integer `a`.

**The code doubles `n` once**

The statement `n <<= 1` replaces `n` with `2n` using a left bit shift. From that point onward, the local variable `n` means the doubled original target.

This transformation lets all later checks use integer arithmetic. There is no floating-point rounding and no need to represent the triangular term separately.

To avoid confusion, call the doubled value `N = 2n_{\text{original}}` in the mathematical discussion. The required equation becomes

$$
N=k(2a+k-1).
$$

**First condition: the length must divide the doubled target**

To make `N/k` an integer, the code requires

`n % k == 0`.

If `k` does not divide `N`, then `2a+k-1` cannot be an integer, so no integer starting value exists for that length.

When divisibility holds, the proposed doubled start is

`n // k - k + 1`,

which represents `2a`.

**Second condition: the start must be an integer**

Since the expression equals `2a`, it must be even. The check

`(n // k - k + 1) % 2 == 0`

tests exactly this parity requirement.

When both divisibility and parity hold, dividing that expression by two gives an integer `a`. The loop bound separately guarantees that `a` is positive, so this `k` describes one valid sequence and `ans` increases by one.

There cannot be two sequences with the same length because the formula determines one unique `a`.

**Derive the positive-start loop bound**

Positive integers require `a >= 1`, hence `2a >= 2`. From

$$
2a=\frac{N}{k}-k+1,
$$

we need

$$
\frac{N}{k}-k+1\ge2.
$$

Rearranging gives

$$
\frac{N}{k}\ge k+1,
$$

and therefore

$$
k(k+1)\le N.
$$

This is exactly the while condition `k * (k + 1) <= n` after doubling. When it fails, even the sequence `1+2+\cdots+k` is already larger than the original target. Longer positive consecutive sequences are also impossible, so the loop can stop.

The largest tested `k` is proportional to $\sqrt{N}$, which produces the square-root running time.

**Trace `n = 15`**

The code doubles the target to `N = 30`.

- `k = 1`: 30 is divisible by 1, and `30 - 1 + 1 = 30` is even. This gives `a = 15`, the one-term sequence `15`.
- `k = 2`: 30 is divisible by 2, and `15 - 2 + 1 = 14` is even. This gives `a = 7`, the sequence `7+8`.
- `k = 3`: 30 is divisible by 3, and `10 - 3 + 1 = 8` is even. This gives `a = 4`, the sequence `4+5+6`.
- `k = 4`: 30 is not divisible by 4, so no sequence has this length.
- `k = 5`: 30 is divisible by 5, and `6 - 5 + 1 = 2` is even. This gives `a = 1`, the sequence `1+2+3+4+5`.

After `k = 5`, the next bound is `6*7 = 42 > 30`, so the search ends with four representations.

**Why the count is exact**

Every consecutive-positive representation has a length `k` that satisfies the positive-start bound. Its equation makes `k` divide `N`, and the resulting `2a` is even, so the loop counts it.

Conversely, every counted `k` produces a positive integer start `a` through the derived formula. Substituting that value back into the arithmetic-series equation gives the original target exactly. Different lengths describe different representations. The counter therefore establishes a one-to-one correspondence between accepted lengths and valid sums.

## Complexity detail

The loop continues while `k(k+1) <= 2n_{\text{original}}`, so it tries `O(\sqrt n)` lengths. Each iteration performs a constant number of integer multiplications, divisions, remainders, comparisons, and additions. Time complexity is `O(\sqrt n)`.

The algorithm stores only the doubled target, `ans`, `k`, and constant-size arithmetic intermediates. Auxiliary space is `O(1)`.

Python integers do not overflow when doubling or multiplying `k(k+1)`. In a fixed-width language, a sufficiently wide integer type should be used for these intermediates.

## Alternatives and edge cases

- **Try every starting number and extend a running sum:** This can perform far more work and repeatedly constructs overlapping sequences. Searching by length reduces the question to divisibility and parity.

- **Sliding window of positive integers:** A two-pointer window can also find representations in roughly linear time relative to `n`, but `O(\sqrt n)` arithmetic is much faster for targets up to `10^9`.

- **Count odd divisors:** The number of consecutive positive representations is related to the number of odd divisors of `n`. Factoring can produce another square-root solution, but the length formula follows the sequence definition more directly.

- **One-term representation:** `k = 1` always succeeds, so every positive `n` has at least one representation consisting of itself.

- **Start must be positive:** The loop bound excludes sequences beginning at zero or a negative integer.

- **Even versus odd length:** The parity test uniformly handles both. Depending on `k`'s parity, divisibility conditions on `n` differ, but no separate cases are necessary.

- **Divisible but wrong parity:** Integer `N/k` alone is insufficient; if the derived `2a` is odd, `a` would be a half-integer and no valid sequence exists.

- **Parity works but no divisibility:** Integer division must not be used as if exact. The remainder check occurs first.

- **`n = 1`:** Only `k = 1` satisfies the bound and formula, so the answer is 1.

- **Mutated local `n`:** The shift changes only the local integer parameter binding; it does not alter external data.

- **Order inside the sum:** Consecutive sequences are naturally increasing from `a` to `a+k-1`. Writing the same terms in reverse does not create an additional representation.
