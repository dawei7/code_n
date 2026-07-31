## General

**Turn the empty right side into the starting state**

Scan from right to left. Before the scan, `left_sum` is the sum of the entire
array and `right_product` is $1$, the product of an empty suffix. When visiting
index `i`, first subtract `nums[i]` from `left_sum`. The two maintained values
then represent exactly the elements strictly to the left and strictly to the
right of `i`, so their equality is precisely the balanced-index condition.
After the comparison, multiply `nums[i]` into `right_product` to establish the
state needed by the next index to the left.

Because the scan visits larger indices first, save every match rather than
returning immediately. A later saved match in scan order has a smaller index,
so the final saved value obeys the requested tie-break. In fact, positivity
makes the left sum strictly increase and the right product non-increase as an
index moves from left to right, so there can be at most one match; retaining
the general tie-handling rule keeps the implementation directly aligned with
the return contract.

**Cap products that can no longer match**

Let `total_sum` be the sum of all array elements. Every possible left sum is at
most `total_sum`. Therefore, once a suffix product would exceed `total_sum`, its
exact value is irrelevant: it cannot equal any left sum. All factors are
positive, so extending that suffix toward the left can never bring the product
back down.

Represent every such oversized product by the sentinel `total_sum + 1`.
Before multiplying by `nums[i]`, compare the current product with
`total_sum // nums[i]`; this division guard detects whether the multiplication
would cross the cap without first constructing a huge integer. The sentinel
then remains above all possible left sums for the rest of the scan. Thus the
cap preserves every equality decision while avoiding overflow and unbounded
integer growth.

## Complexity detail

Let $N$ be the array length. Computing the total and scanning the array each
take $O(N)$ time. The product is always bounded by `total_sum + 1`, whose
magnitude is at most $10^{14} + 1$ under the constraints, so every arithmetic
operation has bounded machine-scale width for this input domain. The algorithm
uses $O(1)$ auxiliary space.

The benchmark defines size as $N$. Repeated maximum values make every answer
`-1` and force a complete scan. The accepted method performs linear work,
whereas the correct slower control rebuilds both sides for each candidate index
and therefore performs quadratic work across the same tiers.

## Alternatives and edge cases

- **Prefix sums plus capped suffix products:** Precomputing both sides makes
  each comparison immediate but requires $O(N)$ auxiliary space instead of
  the constant-space reverse scan.
- **Exact arbitrary-precision suffix product:** Python can represent the full
  product, but its number of bits grows with the input and makes multiplication
  unnecessarily expensive; fixed-width languages would overflow outright.
- **Floating-point logarithms:** Comparing a logarithmic product with a sum can
  lose equality through rounding and cannot provide an exact decision.
- **Uncapped fixed-width multiplication:** Overflow may wrap a large suffix
  into an unrelated value and create or hide a match.
- **Empty left side:** Its sum is $0$. Since every array value is positive, a
  nonempty or empty right product is positive, so index `0` cannot be balanced.
- **Empty right side:** Its product is $1$, not $0$; this identity is required
  when the last index is tested.
- **Smallest-index requirement:** Saving a match while scanning backward means
  a smaller later-visited index replaces any previously saved one.
