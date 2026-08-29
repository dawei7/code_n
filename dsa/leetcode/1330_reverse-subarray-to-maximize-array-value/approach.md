## General

The array value is the sum of absolute differences between adjacent elements. Reversing a subarray looks global, but almost all adjacent pairs keep the same contribution.

Inside the reversed section, a pair `(u, v)` becomes `(v, u)`, and:

$$
\lvert u-v\rvert=\lvert v-u\rvert.
$$

Only edges crossing the subarray boundaries can change. The exact Optimal solution starts with the original sum and separately considers reversals touching an array end and reversals with two interior boundaries.

**Original value and no-improvement option**

`s` is the sum of `abs(x - y)` for every adjacent pair. `ans` begins equal to `s`.

This preserves the option of reversing a one-element subarray or choosing a reversal with no gain. The algorithm never has to accept a negative improvement.

**Reversal beginning at index zero**

Suppose a reversed prefix ends at element `x`, followed by `y` outside the prefix. The old crossing edge contributes `abs(x - y)`.

After reversal, the original first element `nums[0]` becomes the prefix's right endpoint, so the new crossing edge is `abs(nums[0] - y)`.

The candidate value is:

`s + abs(nums[0] - y) - abs(x - y)`.

The first loop tests this for every adjacent pair `(x, y)`, covering every possible non-full prefix endpoint.

**Reversal ending at the last index**

For a reversed suffix beginning immediately after outside element `x`, its original first element is `y` and the array's last element moves next to `x`.

The old boundary cost is `abs(x - y)`, and the new cost is `abs(nums[-1] - x)`. The second candidate line tests:

`s + abs(nums[-1] - x) - abs(x - y)`.

Together, these two formulas cover every reversal touching exactly one array end. Reversing the whole array changes no absolute adjacent differences and is already represented by `ans = s`.

**Two interior boundaries**

An interior reversal changes two crossing edges. Let its left boundary pair be `(x, y)` and its right boundary pair be `(u, v)`, where `y` and `u` lie inside the reversed section.

Before reversal, boundary cost is:

$$
\lvert x-y\rvert+\lvert u-v\rvert.
$$

After reversal, `u` moves next to `x` and `y` moves next to `v`, giving:

$$
\lvert x-u\rvert+\lvert y-v\rvert.
$$

The gain is their difference.

Checking every pair of boundaries would be quadratic. The source uses a four-sign identity to maximize the new Manhattan-distance term in linear passes.

**Why four sign combinations appear**

For two two-dimensional points $(x,y)$ and $(u,v)$:

$$
\lvert x-u\rvert+\lvert y-v\rvert
=
\max_{(k_1,k_2)\in\{(1,1),(1,-1),(-1,1),(-1,-1)\}}
\left(k_1x+k_2y-k_1u-k_2v\right).
$$

The unusual expression:

`pairwise((1, -1, -1, 1, 1))`

generates exactly the four sign pairs:

`(1,-1)`, `(-1,-1)`, `(-1,1)`, and `(1,1)`.

For one fixed sign pair, define `F(x,y) = k1*x + k2*y` and old edge cost `B(x,y) = abs(x-y)`.

Choosing one boundary to maximize:

`F(x,y) - B(x,y)`

and another to minimize:

`F(x,y) + B(x,y)`

maximizes:

$$
F(x,y)-F(u,v)-B(x,y)-B(u,v),
$$

which is the gain for that sign orientation.

The inner scan records these extremes as `mx` and `mi`. `mx - mi` is the best gain represented by that sign pair. Trying all four signs covers every absolute-value orientation.

If the computed difference is negative, `max(mx - mi, 0)` uses zero instead, preserving the original value.

**Boundary ordering**

The extreme scan does not explicitly require the chosen left boundary to appear before the right boundary. If an extreme pair appears in the opposite order, the negated sign combination swaps the direction of the difference. Because all four sign pairs are examined, the same usable gain is represented with endpoints in valid order.

**Why the maximum is complete**

Any reversal is one of three types: touches the left end, touches the right end, or has two interior boundaries. The first scan evaluates the first two types exactly.

For an interior reversal, internal edge contributions cancel, and the four-sign transformation finds the maximum possible two-boundary gain. Since `ans` takes the maximum over the unchanged value and every category, the returned result is globally optimal.

## Complexity detail

Let $n$ be the array length.

Computing `s` visits $n-1$ adjacent pairs. The endpoint loop visits them once. The sign loop has exactly four iterations, each scanning all adjacent pairs.

The number of passes is constant, so total time is $O(n)$.

Only scalar values such as `s`, `ans`, `mx`, and `mi` are stored. `pairwise` iterates lazily, so auxiliary space is $O(1)$, matching the manifest.

Absolute values and arithmetic are constant-time under the bounded integer constraints.

## Alternatives and edge cases

- **Try every subarray and recompute:** It can take cubic time and repeats unchanged internal contributions.
- **Try every boundary pair using the gain formula:** Recognizing boundary-only changes reduces recomputation but remains $O(n^2)$.
- **Prefix reversal:** Exactly one original adjacent edge changes, handled by the first candidate formula.
- **Suffix reversal:** Exactly one edge changes, handled by the second formula.
- **Whole-array reversal:** Every edge merely changes orientation, so total value is unchanged.
- **Length two:** Any reversal preserves the sole absolute difference, and `ans` remains `s`.
- **Repeated equal values:** Zero-cost edges participate normally in the formulas.
- **Negative numbers:** Absolute differences and sign identities work without a nonnegative-value assumption.
- **No beneficial reversal:** Initializing `ans = s` and clipping interior gain at zero returns the original value.
- **Four sign pairs:** Omitting any can miss an absolute-value orientation and therefore the optimal reversal.
- **Lazy `pairwise`:** It does not allocate all adjacent tuples, preserving constant auxiliary space.
