## General

A perfect number equals the sum of its positive divisors excluding itself. Testing every candidate from one through `num - 1` is unnecessary because divisors occur in complementary pairs.

If `i` divides `num`, then `num // i` also divides it, and

$$
i\left(\frac{\textit{num}}i\right)=\textit{num}.
$$

In each pair, at least one member is at most `sqrt(num)`. If both were larger than the square root, their product would exceed `num`. Therefore checking possible smaller factors only through the square-root boundary discovers every divisor pair.

**Treat divisor one separately.** For every `num > 1`, one is a proper divisor and should be included, while `num` itself should not. The source starts `s = 1` and begins trial division at `i = 2`. This includes one without also adding its complementary factor `num`.

The input `num = 1` is special. Its only positive divisor is itself, which must be excluded, leaving a proper-divisor sum of zero. Initializing `s = 1` would incorrectly make it appear perfect, so the method returns `False` immediately.

**Stay on the safe side of the square root without floating point.** The loop condition is

`i <= num // i`.

For positive integers, this is equivalent to `i * i <= num`, but it avoids multiplication overflow in fixed-width languages and avoids floating-point rounding from `sqrt`. It includes the exact square root when `num` is a perfect square.

When `num % i == 0`, `i` is a divisor and is added to `s`. Its paired divisor is `num // i`. Usually that is a different number and is also added.

For a perfect square, the two factors meet at the square root. If `i == num // i`, adding both would count the same divisor twice. The inner condition adds the quotient only when it differs from `i`.

For `num = 28`:

- `s` starts at one;
- `i = 2` divides, adding two and fourteen;
- `i = 4` divides, adding four and seven;
- other candidates through the square root do not divide.

The sum becomes `1 + 2 + 14 + 4 + 7 = 28`, so the method returns true.

For `num = 36`, the factor pair at `i = 6` is `(6, 6)`. The code adds six once. Even though thirty-six is not perfect, this example shows why the duplicate guard is necessary for accurate divisor sums.

For a non-square composite such as twelve, the scan sees pair `(2, 6)` and then `(3, 4)`, while one was already included. Its proper-divisor sum becomes `1 + 2 + 6 + 3 + 4 = 16`, so it is rejected. Notice that the larger factors six and four are never used as loop indices; they arrive as quotients of their smaller partners. This is precisely where the square-root improvement comes from.

**Why no divisor is omitted.** Consider any proper divisor `d > 1`. If `d <= sqrt(num)`, the loop tests `i = d` and adds it. If `d > sqrt(num)`, its complement `num / d` is smaller than the square root, and when the loop tests that complement, it adds `d` as the quotient. One was included initially, while `num` itself is never introduced because the loop begins at two. Thus `s` contains every proper positive divisor exactly once.

The running sum is not used to stop early. Although `s > num` proves the number cannot later become perfect because all future additions are nonnegative, omitting that optimization keeps the proof uniform. It does not change the worst-case square-root bound, and the final equality remains the single decision point.

After all pairs are processed, `s == num` is exactly the definition of a perfect number. No early decision is needed; the final equality handles primes, composites, squares, and known perfect numbers uniformly.

The algorithm increments `i` through non-divisors as well. More advanced prime-factorization formulas could skip work, but the square-root scan is simple, exact, and easily fast enough for `num <= 10^8`.

## Complexity detail

The candidate `i` runs from two through `floor(sqrt(num))`, performing constant-time division and remainder operations under the standard integer model. Time is $O(\sqrt{\textit{num}})$.

Only `s`, `i`, and temporary quotient/remainder values are stored, so auxiliary space is $O(1)$. The Boolean output is constant size.

## Alternatives and edge cases

- **Test every smaller integer:** It directly follows the definition but takes $O(num)$ time instead of exploiting divisor pairs.
- **Prime factorization formula:** The sum-of-divisors function can be derived from prime exponents, also using square-root factorization. It is more machinery than needed for one equality test.
- **Euclid–Euler perfect-number table:** Within a fixed numeric range, compare against generated even perfect numbers. This is fast but relies on a deeper theorem and a bounded domain rather than direct verification.
- **`num = 1`:** It is not perfect because excluding itself leaves no divisors. The explicit guard prevents the initial one from causing a false positive.
- **Prime number:** No candidate divides, so `s` remains one and cannot equal a prime greater than one.
- **Perfect square:** Its square-root divisor is added once through `i != num // i`.
- **Exclude the number itself:** Starting at factor two after pre-adding one avoids ever adding the pair `(1, num)`.
- **Overflow-safe boundary:** `i <= num // i` avoids evaluating `i * i` in a bounded integer type.
