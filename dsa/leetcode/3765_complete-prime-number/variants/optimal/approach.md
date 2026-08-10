## General

**Translate decimal pieces into an incremental scan**

If `num` has $D$ decimal digits, the required prefixes are the first 1, 2, through $D$ digits, and the required suffixes are the last 1, 2, through $D$ digits. The whole number appears in both families.

The source converts `num` to its decimal string `s` so it can visit the digits in their written order. It does not repeatedly slice and parse every prefix and suffix. Instead, it builds each next value from the previous one, checks it immediately, and stops on the first failure.

**Test primality by searching only through the square root**

The nested `is_prime(x)` helper first rejects every `x < 2`. This handles zero and one explicitly because neither is prime.

For `x >= 2`, it evaluates

`all(x % i for i in range(2, int(sqrt(x)) + 1))`.

For each candidate divisor `i`, `x % i` is zero exactly when `i` divides `x`. Zero is false in a Boolean context, while a nonzero remainder is true. Therefore `all(...)` returns true only when every tested divisor leaves a remainder.

Testing stops at $\lfloor\sqrt{x}\rfloor$. If a composite number can be written as $x=ab$ and both factors were greater than $\sqrt{x}$, then their product would be greater than $x$, which is impossible. Consequently every composite `x` has at least one factor no larger than its square root. Finding no divisor in this range is enough to establish primality.

For 2 and 3, the divisor range is empty. Python's `all` of an empty sequence is true, which is correct after the earlier `x < 2` rejection.

**Build prefixes from left to right**

The prefix accumulator starts at zero. For each character `c` in `s`, the update

`x = x * 10 + int(c)`

shifts the existing decimal digits one place left and appends the new digit. After processing the first $k$ characters, `x` is exactly the integer represented by the first $k$ digits.

For `num = 317`, the accumulator visits 3, then 31, then 317. Each value is passed to `is_prime` as soon as it is complete. If any prefix is nonprime, returning `False` is final: the definition requires every prefix and suffix to be prime, so no later check could repair the failed condition.

**Build suffixes from right to left without reversing their meaning**

After all prefixes pass, the source resets `x` to zero and sets `p = 1`. It iterates through `s[::-1]`, which exposes digits from right to left.

The update

`x = p * int(c) + x`

places the newly encountered digit to the left of the suffix already built. Then `p *= 10` prepares the next decimal place.

For `num = 317`:

- reading the final 7 gives `x = 7` and `p = 10`;
- reading 1 gives `x = 1 * 10 + 7 = 17` and `p = 100`;
- reading 3 gives `x = 3 * 100 + 17 = 317`.

Those are exactly the last one, two, and three digits as integers. Appending the reversed digit with `x = x * 10 + digit` would instead build 71 and 713, which are not the required suffixes.

**Why all required numbers are checked**

After the $k$th prefix iteration, the prefix invariant says that `x` equals the first $k$ digits. The loop runs once for every $k$ from one through $D$, so no prefix length is omitted.

After the $k$th suffix iteration, `p` has tracked the correct power of ten and `x` equals the last $k$ digits. This loop also covers every length from one through $D$.

Every rejection is sound because it comes from a required prefix or suffix that failed a valid primality test. If both loops finish, all $2D$ required checks have passed, so `True` is justified.

The full number is checked once as the last prefix and again as the last suffix. The second check is redundant for performance, but it accurately follows the source and does not change the result.

**Understand decimal zeros**

A zero occurring as a one-digit prefix or suffix immediately fails because zero is not prime. For a longer suffix with a leading zero in its digit spelling, integer interpretation naturally drops that zero. For example, the last two digits `"03"` build the integer 3. The arithmetic construction has exactly the same behavior as converting that substring to an integer.

## Complexity detail

Let $n$ denote the numeric value `num` and let $D=\lfloor\log_{10}n\rfloor+1$ be its decimal digit count.

A single primality test on value $x$ takes $O(\sqrt{x})$ worst-case time. A loose bound over $2D$ tests would be $O(D\sqrt n)$, but the tested prefix and suffix magnitudes grow geometrically by decimal length. Every $k$-digit piece is less than $10^k$, so the total trial-division work is bounded by

$$
\sum_{k=1}^{D} O\left(10^{k/2}\right)=O\left(10^{D/2}\right)=O(\sqrt n).
$$

There are two such families, which changes only the constant. String conversion and digit scans add $O(D)$ time, dominated by the stated $O(\sqrt n)$ worst-case bound. Composite pieces often stop earlier because `all` short-circuits at the first divisor.

The source stores `s` and also creates `s[::-1]`, each with $D$ characters. Its literal generalized auxiliary space is therefore $O(D)=O(\log n)$. The primality generator and `range` do not materialize all divisors.

Because the documented domain has `num <= 10^9`, $D\le 10$ is a fixed bound. Under that fixed-domain convention, the manifest reports $O(1)$ space. Both statements are useful: $O(1)$ under the given constraints, and $O(\log n)$ if the numeric domain is generalized.

## Alternatives and edge cases

- **Repeated decimal slicing:** Testing `int(s[:k])` and `int(s[-k:])` is straightforward, but repeatedly reparses digit sequences. The accumulators express the same values incrementally.
- **Sieve of Eratosthenes:** A sieve up to `num` would answer primality queries quickly after preprocessing but uses $O(n)$ time and space, excessive for only a few tested values.
- **Probabilistic or deterministic Miller–Rabin:** This is valuable for much larger integers, but trial division is simple and sufficient for `num <= 10^9`.
- **Check only the whole number:** A prime full number can still contain a composite shorter prefix or suffix; every length is required.
- **Check only prefixes:** Passing prefixes says nothing about the shorter suffixes, and conversely.
- **One-digit input:** The same value is checked in both loops and returns true exactly for 2, 3, 5, or 7.
- **A piece equal to zero or one:** `is_prime` rejects it before attempting division.
- **Even multi-digit piece:** Trial division finds divisor 2 immediately and short-circuits.
- **Perfect square:** Including `int(sqrt(x))` in the range is essential because the square root itself is a divisor.
- **Suffix containing a leading zero:** It is interpreted numerically, so `"03"` becomes 3.
- **Early failure:** Returning immediately is safe because the requirement is a conjunction of all prefix and suffix conditions.
- **Full-number duplicate test:** The source tests it as both a prefix and suffix. Skipping the second test would be a possible micro-optimization, not the current behavior.
- **Floating square root:** The constrained values are small enough for `sqrt` and integer conversion to identify the required trial bound reliably.
- **Input preservation:** Only local strings and integers are created; `num` is not modified.
