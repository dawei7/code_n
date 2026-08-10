## General

A partition after the first `i` elements is valid exactly when

$$
\max(\texttt{nums}[0:i])
\le
\min(\texttt{nums}[i:n]).
$$

The solution precomputes suffix minima so each possible split can be checked while scanning prefix maxima from left to right. The first valid split is automatically the one with the smallest left side.

**Build suffix minimums.** Array `mi` has length `n + 1`. Its intended meaning is

$$
\text{mi}[i]=\min(\texttt{nums}[i:n]).
$$

The extra entry `mi[n]` is positive infinity, representing the minimum of an empty suffix for recurrence convenience. Scanning backward:

```text
mi[i] = min(nums[i], mi[i + 1])
```

combines the current value with the minimum of everything to its right.

**Scan candidate split positions.** The second loop enumerates values with indices starting at one:

```text
for i, v in enumerate(nums, 1):
```

After processing `v = nums[i - 1]`, variable `mx` is the maximum of the first `i` elements. The right subarray would begin at original index `i`, whose minimum is `mi[i]`.

If `mx <= mi[i]`, every left value is at most `mx`, and every right value is at least `mi[i]`. Therefore every left value is less than or equal to every right value.

The loop returns immediately at the first such `i`. Candidate sizes are visited as 1, 2, 3, and so on, so no smaller valid left length exists.

**Why comparing only extremes is sufficient.** The condition formally compares every left/right pair. If the largest left element is at most the smallest right element, then for any left $a$ and right $b$,

$$
a\le\max(\text{left})
\le\min(\text{right})
\le b.
$$

Conversely, if every pair satisfies $a\le b$, the largest left must be at most the smallest right. The extremes test is therefore exactly equivalent to the full condition.

**Nonempty right side.** The problem requires both parts nonempty. The code's loop technically reaches `i = n`, where `mi[n] = inf` and the condition would always succeed. However, the input guarantee says a valid partition exists, meaning an earlier `i<n` is found and returned. A defensive general implementation could stop the scan before the final element.

**Example `[5,0,3,8,6]`.** Suffix minima beginning at indices 1, 2, and 3 are 0, 3, and 6. Prefix maxima after sizes 1, 2, and 3 are all 5. Splits of sizes 1 and 2 fail because $5>0$ and $5>3$. Size 3 succeeds because $5\le6$, producing left `[5,0,3]` and right `[8,6]`.

For `[1,1,1,0,6,12]`, the prefix maximum stays 1. Every split before the zero fails because its right suffix minimum is zero. Once the zero is absorbed into the left side, the right suffix begins at 6 and the condition $1\le6$ succeeds. This shows why seeing a small late value forces the left interval to expand even though the early prefix itself appeared well ordered.
Before testing size `i`, `mx` equals the exact maximum of the candidate left prefix, and `mi[i]` is the exact minimum of its complementary suffix. The test is equivalent to partition validity. Since sizes are tested in ascending order, the returned valid size is minimal.

The code initializes `mx = 0`. This is safe because the contract guarantees every array value is nonnegative. A version supporting negative values should initialize it to negative infinity or the first element.

The suffix array is what makes early return reliable. Without knowing the minimum of every unscanned value, comparing the prefix maximum only with `nums[i]` could accept too soon: a still later right-side element might be smaller and violate the all-pairs condition.

## Complexity detail

Let $n$ be the array length. The backward suffix pass and forward prefix pass are both linear.

- **Time complexity:** $O(n)$.
- **Space complexity of the exact solution:** $O(n)$ for the suffix-minimum array.

The manifest's $O(1)$ space corresponds to the editorial's one-pass no-array method, not this exact suffix-array implementation. The current code must retain `mi`.

## Alternatives and edge cases

- **One-pass constant-space method:** Track the current left maximum, global maximum seen, and boundary; extend the boundary whenever a later value is below the left maximum. This matches the manifest's $O(1)$ space.
- **Prefix maxima plus suffix minima arrays:** Precompute both and test splits. It is clear but uses two $O(n)$ arrays instead of one.
- **Try every pair across every split:** This can cost $O(n^3)$ and ignores extreme summaries.
- **Sort values:** Sorting destroys contiguity and original split positions.
- **Smallest valid left size one:** The first test returns immediately.
- **Equal boundary values:** The condition allows equality, so `mx <= mi[i]` is correct.
- **Repeated numbers:** Minima and maxima naturally handle them.
- **Guaranteed partition:** Ensures return before the empty-right sentinel split.
- **Nonnegative values:** Justifies `mx = 0`; broader inputs need a different initialization.
- **Two elements:** The only legal split is after the first element and is guaranteed valid by the test data.
- **Suffix sentinel:** Infinity makes the recurrence simple but should not be used to accept an empty right side.
- **Input unchanged:** The solution reads values and builds summaries without rearranging the array.
- **Minimality:** Early return is correct only because split sizes are scanned from smallest to largest.
