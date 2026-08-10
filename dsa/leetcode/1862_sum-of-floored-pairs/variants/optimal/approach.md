## General

**Group ordered pairs by denominator value and quotient.** A direct calculation considers every ordered pair of indices, which is quadratic. Many indices share the same numeric value, and many numerator values produce the same floor quotient for a fixed denominator. The solution aggregates both kinds of repetition.

`cnt = Counter(nums)` records how many times each value occurs. Let `mx` be the largest value.

**Build prefix counts over the value domain.** Array `s` has indices zero through `mx`. For each value `i`,

`s[i] = s[i - 1] + cnt[i]`.

Thus `s[r] - s[l - 1]` gives the number of input occurrences with values in inclusive range `[l, r]`. Missing values contribute zero through the counter.

**Characterize one floor quotient bucket.** Fix denominator value `y`. For a positive integer quotient `d`:

`floor(x / y) = d`

exactly when

`d * y <= x <= (d + 1) * y - 1`.

The code enumerates `d = 1, 2, ...` while `d * y <= mx`. The upper endpoint is capped at `mx` because no numerator exceeds it.

The number of numerator occurrences in that bucket is:

`s[min(mx, d * y + y - 1)] - s[d * y - 1]`.

Each such numerator paired with one denominator occurrence contributes `d`. There are `cnt[y]` denominator indices having value `y`, so the total bucket contribution is denominator frequency times quotient times numerator frequency.

**Why quotient zero is omitted.** Numerators smaller than `y` produce floor quotient zero. Their total contribution is zero regardless of how many pairs exist, so the loop begins at one without losing anything.

**Count ordered index pairs correctly.** Frequencies multiply because every numerator occurrence can pair with every denominator occurrence. When numerator and denominator values are equal, their indices may also be equal; the problem permits all `i, j`, including `i = j`. `cnt[y] * cnt[y]` correctly includes those self-pairs and cross-pairs.

**Trace `nums = [2, 5, 9]` for denominator two.** Quotient one covers numerators two and three, finding the occurrence two and contributing one. Quotient two covers four and five, finding five and contributing two. Quotient four covers eight and nine, finding nine and contributing four. Empty quotient buckets contribute zero. The denominator-two total is seven.

The outer loop then handles denominator five and nine, adding their quotient-one pairs and producing the sample total ten.

**Why iterating all domain values is efficient.** For denominator `y`, the inner loop runs about `mx / y` times. Summed over positive `y`, this is the harmonic series:

`mx * (1 + 1/2 + 1/3 + ... + 1/mx)`,

which is `O(mx log mx)`. The `if cnt[y]` guard skips absent denominators and can only reduce work.

**Modulo handling.** After every bucket addition, `ans %= mod` keeps the accumulator bounded. Modular addition and multiplication preserve the final sum modulo the prime; unlike a maximization problem, reducing partial sums cannot change which result should be selected because there is no comparison between raw candidates.
Fix a denominator occurrence. Every numerator value belongs to exactly one quotient bucket, including the omitted zero bucket. Positive buckets are disjoint and cover all numerators at least `y`. The prefix difference counts each occurrence in its unique bucket, and multiplying by `d` gives its correct quotient contribution. Multiplying by denominator frequency and summing all present `y` counts every ordered pair exactly once.

## Complexity detail

Let `n = nums.length` and `U = max(nums)`. Building frequencies is `O(n)`. Prefix counts take `O(U)`. The nested quotient loops perform `O(U log U)` iterations in the worst case. Total time is `O(n + U log U)`.

The counter and prefix array store at most `O(U)` values, so auxiliary space is `O(U)`.

## Alternatives and edge cases

- **Enumerate all index pairs:** It is direct but costs `O(n^2)` time.
- **Sort and binary-search quotient ranges:** Possible, but value-domain prefix counts answer every bucket count in constant time.
- **All values equal:** Every ordered pair has quotient one, giving `n^2`.
- **Denominator larger than numerator:** Quotient zero is correctly omitted from the sum.
- **Self-pairs:** Each contributes one and is included by frequency multiplication.
- **Duplicate values:** Counter frequencies count each index occurrence, not merely each distinct value.
- **Capped final bucket:** `min(mx, ...)` prevents a prefix lookup beyond the array.
- **Positive-input dependency:** Denominators are never zero, so division and bucket stepping are safe.
- **Missing domain values:** `cnt[y]` is zero and no denominator work is needed.
- **Modulo frequency:** Reducing after each bucket is safe for a sum and prevents large accumulation.
- **Ordered pairs:** Numerator and denominator roles are distinct; the outer denominator loop preserves that direction.
- **Prefix lower endpoint:** Since `d >= 1` and `y >= 1`, `d * y - 1` is always a valid nonnegative index.
- **Inner-loop termination:** Once `d * y > mx`, every remaining quotient bucket begins above the largest numerator in the array. All such buckets are empty, so stopping at that exact condition omits no positive contribution and avoids pointless prefix queries.
- **Largest denominator:** When `y = mx`, only quotient one can be nonempty, and it contains precisely numerator occurrences equal to `mx`.
