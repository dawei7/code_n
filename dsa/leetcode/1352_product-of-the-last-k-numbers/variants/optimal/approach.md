## General

Multiplying the last `k` stream values from scratch would take $O(k)$ time per query. Prefix products offer the multiplicative equivalent of prefix sums: divide one cumulative product by an earlier cumulative product to isolate a suffix. Zero is the only complication because division by a prefix product containing zero is impossible.

The checked-in class solves that complication by storing prefix products only for the positive suffix after the most recently added zero.

**Use one as a sentinel prefix**

The constructor initializes `self.s = [1]`. This leading one represents the product of zero numbers. It allows the first nonzero add to use the same formula as every later add.

If nonzero values two, five, and four are added, the list evolves as
`[1, 2, 10, 40]`. Entry zero is the empty product, entry one is the product of the first suffix value, and so on. In general, `self.s[p]` is the product of the first `p` nonzero values added since the latest zero.

**Append a cumulative product for a nonzero value**

For `num != 0`, `self.s.append(self.s[-1] * num)` multiplies the new value by the cumulative product already at the end. This preserves the prefix-product meaning in constant time.

All allowed nonzero values are positive, so cumulative products are positive and can later serve as exact divisors.

**Let a zero reset the useful history**

When `num == 0`, the method replaces the list with a fresh `[1]`. Any product query whose requested suffix reaches before or to this zero must return zero. Values earlier than the latest zero can never affect a nonzero answer, so their cumulative products are no longer needed.

Values added after the zero begin a new zero-free segment. Their prefix products are sufficient for every query wholly contained in that segment.

This reset does not mean the logical stream forgot its earlier length. Instead, the length of `self.s` reveals how many consecutive nonzero values occur at the end. There are exactly `len(self.s) - 1` such values.

**Answer a suffix query in constant time**

If `len(self.s) <= k`, fewer than `k` nonzero values have appeared since the latest zero. The contract guarantees the overall stream has at least `k` values, so the requested last `k` values must cross that zero. Their product is zero.

Otherwise, all last `k` values lie in the current zero-free segment. Let the segment contain `p` values. The final stored prefix is their full product. Dividing by the prefix through value `p - k` cancels everything before the requested suffix:

$$
\frac{P_p}{P_{p-k}}
= a_{p-k+1}a_{p-k+2}\cdots a_p.
$$

The Python indexing `self.s[-1] // self.s[-k - 1]` selects exactly those two prefixes. Integer division is exact because the earlier prefix is a factor of the later one.

For the suffix two, five, four, querying the last two computes `40 // 2 = 20`. If a zero occurred immediately before those values, querying four items finds `len(self.s) <= 4` and returns zero because that four-item suffix includes the zero.

Every query falls into exactly one of these cases: it crosses the latest zero or it lies entirely after it. The branch returns zero in the first case and the exact prefix quotient in the second, establishing correctness.

## Complexity detail

Each `add` performs either one multiplication and append or resets one list reference. Each `getProduct` performs a length check, constant-index accesses, and one division. Under the stated bounded-integer model, both methods take $O(1)$ time per call. Across $q$ total operations, time is $O(q)$.

The list stores one prefix product for every consecutive nonzero addition since the latest zero, plus the sentinel. In the worst case no zero is ever added, so it uses $O(q)$ persistent space.

Resetting on zero makes the old list unreachable and eligible for memory reclamation. It does not scan or clear its elements one by one, so the reset itself is constant-time at the language level.

## Alternatives and edge cases

- **Store the raw stream:** Multiply the last `k` values at query time. Adds are constant-time, but queries cost $O(k)$ and miss the follow-up target.
- **Prefix product plus zero counts:** Keep prefixes for the entire stream and a parallel zero-prefix count. This can answer whether a range contains zero but still must avoid dividing zero-valued cumulative products.
- **Segment tree:** Supports range products and point appends in logarithmic time, but it is unnecessarily complex when queries always ask for a suffix.
- **First operation is a query outside the contract:** The stream is guaranteed to contain at least `k` values before `getProduct(k)` is called.
- **Latest value is zero:** The list resets to `[1]`, so every positive-`k` query spanning the current end returns zero.
- **Several zeros:** Every zero simply resets again; only the most recent zero matters for suffix products.
- **`k == 1`:** The quotient returns the latest nonzero value, or zero if the latest value itself is zero.
- **Exact division:** The denominator is a stored prefix factor of the numerator, so `//` does not truncate a fractional value.
- **Sentinel one:** It represents the empty prefix and avoids a special branch when a query covers the entire current nonzero segment.
- **Object persistence:** State survives across method calls, and a zero deliberately discards only prefix data that can no longer contribute to a nonzero suffix.
