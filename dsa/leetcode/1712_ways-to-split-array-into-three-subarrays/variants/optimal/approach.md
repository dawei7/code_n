## General

**Describe a split with two ending indices**

Let the left subarray end at index `i` and the middle subarray end at index `r`. Then:

- left is `nums[0:i+1]`,
- mid is `nums[i+1:r+1]`,
- right is `nums[r+1:n]`.

All three must be nonempty, so `0 <= i <= n - 3` and `i + 1 <= r <= n - 2`. The outer loop `for i in range(n - 2)` visits exactly every legal left ending index.

**Use inclusive prefix sums**

`s = list(accumulate(nums))` creates inclusive prefix sums:

$$
s[t]=\sum_{u=0}^{t}\texttt{nums}[u].
$$

Let $T=s[-1]$ be the total. For a chosen pair `i,r`, the three sums are

$$
L=s[i],\qquad M=s[r]-s[i],\qquad R=T-s[r].
$$

Because every input value is nonnegative, `s` is non-decreasing. That monotonicity allows binary search even when zero values make some prefix sums equal.

**Convert the first inequality into a lower bound**

The requirement $L\le M$ becomes

$$
s[i]\le s[r]-s[i]
\quad\Longleftrightarrow\quad
s[r]\ge2s[i].
$$

The source calculates `s[i] << 1`, which is twice `s[i]`, then calls

`bisect_left(s, s[i] << 1, i + 1, n - 1)`.

The search interval uses Python's half-open bounds `[i+1,n-1)`, meaning possible middle endpoints `i+1` through `n-2`. `bisect_left` returns `j`, the first endpoint whose prefix sum is at least twice the left sum. Every legal endpoint before `j` violates $L\le M$.

**Convert the second inequality into an upper bound**

The condition $M\le R$ becomes

$$
s[r]-s[i]\le T-s[r]
\quad\Longleftrightarrow\quad
2s[r]\le T+s[i].
$$

Since prefix sums are integers, this is equivalent to

$$
s[r]\le\left\lfloor\frac{T+s[i]}2\right\rfloor.
$$

`(s[-1] + s[i]) >> 1` computes that floor by right-shifting the nonnegative sum one bit.

Starting at `j`, `bisect_right` finds the first position whose value is greater than the upper threshold:

`k = bisect_right(s, threshold, j, n - 1)`.

Thus valid middle endpoints are precisely the indices from `j` through `k-1`, and their number is `k - j`. If the lower bound already exceeds the upper bound, `bisect_right` returns `j` and contributes zero.

**Why duplicates in prefix sums are handled correctly**

Zero elements can make several adjacent `s` values equal. `bisect_left` chooses the first value satisfying the inclusive lower inequality, while `bisect_right` moves past the last value satisfying the inclusive upper inequality. Their left/right distinction is essential: equality is allowed in both problem conditions, so every endpoint on either boundary must be counted.

**Trace a simple split**

For `nums = [1,1,1]`, `s = [1,2,3]` and the only `i` is zero. The lower target is two, so `j=1`. The upper threshold is `floor((3+1)/2)=2`, and `bisect_right` within the legal endpoint range returns two. The contribution is one, corresponding to `[1] [1] [1]`.

For an all-zero array, every legal prefix value is zero. For each `i`, both inequalities hold for every legal `r`. The two bisections correctly return the full remaining middle-endpoint interval rather than discarding equal values.

**Why the total is correct**

Fix `i`. Monotonic prefix sums make the endpoints satisfying the lower bound a suffix of the legal search interval, and those satisfying the upper bound a prefix. Their intersection is exactly the contiguous range `[j,k)` counted by the source.

Every two-cut split has one unique `i` and `r`, so it appears in exactly one outer iteration. The algorithm adds it exactly when both derived inequalities hold. After processing all left endpoints, `ans` is the number of good splits.

The source applies `ans % mod` once at return. Python integers can hold the unreduced count, and reducing once is mathematically equivalent to reducing after each addition.

## Complexity detail

There are $n-2$ outer iterations. Each performs two binary searches on a non-decreasing array, each costing $O(\log n)$. Prefix-sum construction is $O(n)$, so the exact running time is $O(n\log n)$.

The manifest states $O(n)$ time, but this source does not implement the two monotonic pointers that would achieve that bound; calls to `bisect_left` and `bisect_right` remain logarithmic asymptotically even though their loops run in compiled Python-library code.

The prefix-sum list uses $O(n)$ space. All other state is scalar, so auxiliary space is $O(n)$, matching the manifest's space bound.

## Alternatives and edge cases

- **Two monotonic pointers:** As `i` increases, advance lower and upper middle endpoints without moving them backward. This achieves the manifest's $O(n)$ time but requires careful boundary maintenance.
- **Enumerate both cuts:** Check every `(i,r)` pair directly in $O(n^2)$ time, which is too slow at $10^5$ elements.
- **Negative values:** They would destroy prefix monotonicity and invalidate binary search; non-negativity is essential.
- **All zeros:** Every choice of two cut positions is good, and duplicate prefix sums are counted by left/right bisection.
- **Minimum length three:** Only one split exists, and the search interval contains one middle endpoint.
- **Equal adjacent sums:** Both inequalities are inclusive, so equality must be retained.
- **Nonempty right part:** The binary-search stop `n-1` excludes `r=n-1`.
- **Nonempty middle part:** The lower search begins at `i+1`.
- **No valid endpoint:** `k-j` is zero rather than negative because the upper search starts at `j`.
- **Large answer:** Modulo is applied at return; Python avoids overflow before then.
- **Bit shifts:** `<<1` means multiplication by two and `>>1` means floor division by two for these nonnegative sums.
