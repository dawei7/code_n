## General

**Expand absolute values through sign choices**

For any real value $z$:

$|z|=\max(z,-z)$.

The target contains absolute differences in three coordinates: `arr1` value, `arr2` value, and index. Choosing signs converts it into the difference between two transformed point values.

For signs $a,b\in\{-1,1\}$, define:

`F(i) = a * arr1[i] + b * arr2[i] + i`.

For the sign orientation matching a chosen pair’s differences, the original expression equals `F(i) - F(j)` or its reversed ordering.

Expanding one form illustrates the connection:

`F(i) - F(j) = a * (arr1[i] - arr1[j]) + b * (arr2[i] - arr2[j]) + (i - j)`.

Choosing each sign to agree with the corresponding difference changes that signed difference into its absolute magnitude. If the index difference has the opposite sign, swapping the two endpoints makes it nonnegative while reversing both array differences; the available choices for `a` and `b` absorb those reversals.

**Only four transformations are needed**

There appear to be eight sign combinations across three absolute terms. The index coefficient is fixed to plus one because swapping `i` and `j` negates every difference. A form with negative index coefficient is captured by reversing the pair and negating the value-coordinate signs.

Thus all possibilities are covered by the four combinations of $a$ and $b$ while keeping `+i`.

`dirs = (1,-1,-1,1,1)` and `pairwise(dirs)` generate:

`(1,-1), (-1,-1), (-1,1), (1,1)`,

which are exactly the four sign pairs.

The unusual five-item `dirs` tuple is simply a compact way to produce those four adjacent pairs. It is not a sequence of geometric movement directions despite the variable name.

**Maximize a transformed difference by range**

For one sign pair, the greatest possible `F(i) - F(j)` is:

`max(F) - min(F)`.

The inner scan maintains `mx` and `mi` over transformed values seen so far. Their difference is compared with the global answer.

Even though updates occur online, by the end of the scan the full range for that transformation has been considered. Updating `ans` at every step is harmless and may discover the final maximum early.

The two endpoints producing maximum and minimum may occur in either index order. The original problem permits any `i,j`, and absolute values are symmetric, so order is irrelevant.

**Derive correctness for one pair**

Fix indices `i,j`. Select $a=1$ when `arr1[i]-arr1[j]` is nonnegative and negative one otherwise. Choose $b$ analogously for the second array. Choose orientation of `i,j` so the index difference is represented with plus coefficient.

Under that transformation, `F(i)-F(j)` equals the sum of the three absolute differences. The algorithm considers this sign pair and its range is at least that particular difference.

Conversely, every transformed difference is bounded by the corresponding sum of absolute differences because choosing signs cannot exceed absolute magnitude term by term. Therefore, the largest range across four forms equals, rather than merely bounds, the desired maximum.

More formally, for any fixed signs, $a\Delta x\le|\Delta x|$, $b\Delta y\le|\Delta y|$, and after endpoint orientation $\Delta i\le|\Delta i|$. Summing proves no computed range can exceed the true objective for its endpoint pair. The matching-sign construction proves at least one form attains every pair’s objective, establishing equality in both directions.

**Why no pair enumeration is needed**

The range summary compresses all $n^2$ index pairs for one linear form into its minimum and maximum. Four constant sign forms then cover every absolute-value orientation.

This is the central optimization from quadratic pair comparison to linear scanning.

The minimum and maximum do not need their indices. Once their transformed values are known, their difference already represents the objective for that pair under the chosen signs.

## Complexity detail

There are exactly four sign pairs. Each scans the $n$ aligned array positions once, so time is $O(4n)=O(n)$.

Only current extrema, loop variables, and the answer are stored. `zip` and `enumerate` are lazy iterators, so auxiliary space is $O(1)$.

Values can be negative, but minima and maxima initialized to infinities handle the first transformed point correctly.

## Alternatives and edge cases

- **Enumerate all index pairs:** Direct evaluation costs $O(n^2)$ and is unnecessary.
- **List all eight sign forms:** Correct but duplicates forms obtainable by swapping endpoints.
- **Precompute four transformed arrays:** Simplifies range calls but uses $O(n)$ extra space; streaming extrema are sufficient.
- **Equal indices:** The expression is zero, included implicitly but never needed when a positive larger pair exists.
- **Identical arrays:** Index distance and repeated value differences are still handled by the same forms.
- **Negative values:** Sign expansion works without special cases.
- **Repeated transformed values:** They do not affect the range.
- **Two elements:** Each form examines both, and the maximum equals the only nontrivial pair expression.
- **Large magnitudes:** Python integers avoid overflow in signed linear combinations.
- **Index term:** It is essential; omitting `+i` would solve only the two-array difference.
- **Pair symmetry:** It justifies fixing the index coefficient positive.
- **Direction tuple:** Consecutive pairs happen to enumerate all four sign combinations exactly once.
