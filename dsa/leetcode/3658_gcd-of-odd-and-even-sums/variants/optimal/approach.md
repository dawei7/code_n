## General

**Replace both sequences with closed forms**

The smallest `n` positive odd numbers are

`1, 3, 5, ..., 2n - 1`.

Their sum is `n^2`. One way to derive this is with the arithmetic-series formula: there are `n` terms, the first is one, and the last is `2n - 1`, so

`sumOdd = n(1 + 2n - 1) / 2 = n * 2n / 2 = n^2`.

There is also a geometric identity: adding the next odd number grows one square into the next square,

`1 = 1^2`,

`1 + 3 = 2^2`,

`1 + 3 + 5 = 3^2`,

and so on.

The smallest `n` positive even numbers are

`2, 4, 6, ..., 2n`.

Factoring out two gives

`sumEven = 2(1 + 2 + ... + n)`.

Since `1 + 2 + ... + n = n(n + 1)/2`,

`sumEven = n(n + 1)`.

The requested value is therefore

`gcd(n^2, n(n + 1))`.

**Factor out the common `n`**

Both numbers contain a factor of `n`:

`n^2 = n * n`

and

`n(n + 1) = n * (n + 1)`.

For positive `n`,

`gcd(n * a, n * b) = n * gcd(a, b)`.

Applying this identity gives

`gcd(n^2, n(n + 1)) = n * gcd(n, n + 1)`.

The problem is now reduced to the GCD of two consecutive integers.

The common-factor identity is exact because every common divisor of `a` and `b` becomes `n` times as large after both numbers are multiplied by `n`. Conversely, after removing the shared factor `n` from any greatest common divisor of `na` and `nb`, the remaining factor must divide both `a` and `b`. Thus factoring does not merely find one common divisor; it preserves the greatest one.

**Why consecutive integers are coprime**

Suppose a positive integer `d` divides both `n` and `n + 1`. A divisor of two numbers also divides their difference, so `d` must divide

`(n + 1) - n = 1`.

The only positive divisor of one is one. Therefore

`gcd(n, n + 1) = 1`.

Substituting this result gives

`gcd(n^2, n(n + 1)) = n * 1 = n`.

That is why the exact Optimal source can immediately return `n`. It is not skipping a computation that still depends on the input’s digits; the algebra proves that the requested GCD equals the input for every allowed positive `n`.

**Trace the examples**

For `n = 4`, the odd sum is `4^2 = 16` and the even sum is `4 * 5 = 20`. Factoring out four gives

`gcd(16, 20) = 4 * gcd(4, 5) = 4`.

For `n = 5`, the sums are `25` and `30`. Factoring gives

`gcd(25, 30) = 5 * gcd(5, 6) = 5`.

The same reasoning works for `n = 1`. The sums are one and two, whose GCD is one, matching the returned input.

**Why no loop or Euclidean algorithm is necessary**

One could generate the odd and even terms, add them, and call a GCD function. That would produce the correct result but repeat work already eliminated by the formulas.

Even using the closed forms and Euclid’s algorithm is more work than needed. Euclid would quickly discover that consecutive factors have GCD one, but the mathematical proof establishes that fact in advance. The direct return is the most specialized and optimal solution to this exact problem.

The derivation depends on the sequences being the first `n` positive odd and even numbers. If the ranges started elsewhere or skipped values, returning `n` would no longer be justified.

## Complexity detail

The source performs one return operation and no arithmetic loop, recursion, allocation, or GCD computation. Its time complexity is `O(1)`.

It stores no data structure whose size depends on `n`, so auxiliary space is `O(1)`.

Even an implementation that evaluates the closed forms uses only a fixed number of integer operations. The direct source goes one step further and avoids forming `n^2` and `n(n + 1)`, so fixed-width overflow is not a concern.

The proof has several algebraic steps, but proof length does not translate into runtime operations. Those steps justify simplifying the entire computation at authoring time.

## Alternatives and edge cases

- **Euclidean algorithm on the closed forms:** Compute `gcd(n^2, n(n + 1))` in `O(log n)` time. It is correct but slower and less specialized than returning the proven result.
- **Sum both sequences explicitly:** This takes `O(n)` time and adds unnecessary loop state.
- **Use arithmetic-series formulas only:** Computing both sums in `O(1)` and passing them to a library GCD is acceptable, but the remaining GCD also has a closed form.
- **Forget the common factor:** The factorization by `n` is what exposes consecutive integers and makes the final simplification possible.
- **Assume consecutive integers are coprime without explanation:** Their only common divisor must divide their difference one, which supplies the needed reason.
- **`n = 1`:** The first odd and even sums are one and two; the answer remains `n`.
- **Largest allowed `n`:** Returning `n` avoids constructing squared intermediate values and remains constant-time.
- **Positive-input guarantee:** Factoring the GCD as `n * gcd(n, n+1)` uses positive `n`. The constraints exclude zero and negative inputs.
- **Different sequence definitions:** The result `n` is specific to these exact first-`n` odd and even sums and should not be generalized blindly.
- **Input preservation:** The integer argument is immutable and no external state is changed.
