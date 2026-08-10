## General

**Produce exactly one answer for every integer**

The output must describe the integers from `1` through `n` in increasing order. The solution therefore loops over `range(1, n + 1)`. Python includes the starting value and excludes the stopping value, so `n + 1` is necessary to process `n`. Each iteration appends exactly one string to `ans`; after the loop, the list has exactly `n` elements, and list index `i - 1` represents integer `i`.

For each integer, the required categories overlap. A multiple of `15` is also a multiple of `3` and a multiple of `5`. The order of the conditional chain is what resolves that overlap correctly.

**Test the most specific condition first**

An integer is divisible by both `3` and `5` exactly when it is divisible by their least common multiple. Because `3` and `5` are coprime, their least common multiple is `15`. Thus `i % 15 == 0` is an exact test for the combined `"FizzBuzz"` case.

The first branch checks this combined condition. Only if it is false does the `elif` chain test divisibility by `3`, then divisibility by `5`. If none of those conditions is true, the integer is converted to its decimal string with `str(i)`.

The ordering is essential. If `i % 3 == 0` were tested first, `i = 15` would enter that branch and append only `"Fizz"`; Python would skip the remaining `elif` branches. Testing the intersection first ensures every multiple of both divisors receives the combined label.

The four actions are:

- append `"FizzBuzz"` when `i % 15 == 0`;
- otherwise append `"Fizz"` when `i % 3 == 0`;
- otherwise append `"Buzz"` when `i % 5 == 0`; and
- otherwise append `str(i)`.

Because this is one `if`/`elif`/`elif`/`else` chain, exactly one action runs. No integer can add two separate list items, and no integer can add none.

**Why remainder zero means divisible**

For integers $i$ and $d>0$, division gives a quotient and a remainder. The divisor $d$ divides $i$ precisely when that remainder is zero. Python's `%` operator computes the remainder, so `i % d == 0` directly expresses divisibility by `d`. The input values are positive, so there are no sign subtleties.

For a short trace with `n = 5`:

- `1` has nonzero remainder modulo `3`, `5`, and `15`, so append `"1"`.
- `2` also reaches the fallback, so append `"2"`.
- `3 % 3 == 0`, so append `"Fizz"`.
- `4` reaches the fallback, so append `"4"`.
- `5 % 5 == 0`, so append `"Buzz"`.

At `i = 15`, the first condition succeeds, so the list receives one `"FizzBuzz"` entry.

**Why the classification is complete and correct**

Take any processed integer `i`. There are only two high-level possibilities: it is divisible by both `3` and `5`, or it is not. In the first case, divisibility by `15` is true and the first branch appends the required combined label.

In the second case, `i` may be divisible by `3` alone, divisible by `5` alone, or divisible by neither. The second branch handles the first possibility, the third handles the second, and the `else` handles the last. The preceding failure of the combined test ensures that a successful single-divisor branch really is the appropriate remaining category.

This case split is exhaustive and mutually exclusive as executed by the chain. Therefore each output position contains exactly the string demanded for its integer. Since the loop processes every integer once and preserves their order, the entire returned list is correct.

**Why this direct method is optimal**

The required output contains `n` separate strings. Any correct algorithm must produce all `n` entries, so it needs at least $\Omega(n)$ time simply to write the result. This solution performs a constant number of remainder tests and one append per integer, achieving $O(n)$ time. It therefore meets the unavoidable asymptotic lower bound.

The code also keeps the logic close to the fixed four-rule contract. A more configurable mapping structure can be useful for a generalized version with many divisor-label pairs, but for exactly `3` and `5`, direct conditions avoid extra iteration and make precedence explicit.

## Complexity detail

Let $n$ be the input upper bound. The loop executes exactly $n$ iterations. Each iteration performs at most three modulo comparisons, one possible integer-to-string conversion, and one list append. Under the usual fixed-width integer model for the stated constraint, each is constant work, so the total time complexity is $O(n)$.

The returned list contains $n$ strings, so its required output space is $O(n)$. This is the space complexity recorded by the variant manifest. Apart from that output, the algorithm stores only the loop variable and a constant amount of conditional state, giving $O(1)$ auxiliary space.

The decimal strings for ordinary numbers contain up to $O(\log i)$ characters in a fully bit-sensitive model. Under the fixed constraint $n \le 10^4$, their maximum length is bounded by a small constant. More generally, the total number of output characters would account for the digits written, but the standard analysis for this problem treats each bounded integer conversion and output item as constant-sized.

## Alternatives and edge cases

- **Two independent divisibility checks with concatenation:** Start an empty string, append `"Fizz"` if divisible by `3`, append `"Buzz"` if divisible by `5`, and use the number if the string remains empty. This naturally builds `"FizzBuzz"` and is easy to extend, with the same asymptotic bounds. The chosen chain is equally efficient and explicit for the fixed rules.
- **Divisor-to-label mapping:** Iterate through pairs such as `(3, "Fizz")` and `(5, "Buzz")`. This is preferable when mappings are configurable, but introduces a nested loop and requires preserving mapping order so combined labels are spelled correctly.
- **Precompute the 15-value cycle:** Divisibility categories repeat every 15 integers, but ordinary numeric entries do not repeat because their text changes. Cycle precomputation adds complexity without improving the required $O(n)$ output time.
- **Check `3` before `15`:** This is incorrect in an `if`/`elif` chain because multiples of 15 would stop at `"Fizz"`. The combined condition must come first.
- **Use `i % 3 == 0 and i % 5 == 0`:** This is logically equivalent to `i % 15 == 0`. It performs two explicit checks and may be clearer when the divisors are not coprime; for `3` and `5`, the single least-common-multiple test is exact.
- **`n == 1`:** The loop executes once and returns `["1"]`; no special case is needed.
- **Upper endpoint:** `range(1, n + 1)` includes `n`. Using `range(1, n)` would silently omit the final required entry.
- **Multiples such as 3 and 5:** They enter exactly one single-label branch because the earlier combined test failed.
- **Multiples of 15:** They enter the first branch and never fall through to a shorter label.
- **Nonmultiples:** `str(i)` is necessary because every output element must be a string, not an integer.
- **Positive-input guarantee:** The contract starts at `n = 1`; behavior for zero or negative upper bounds is outside the problem and need not be added to the algorithm.
