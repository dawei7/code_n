## General

**Each element contributes an absolute difference**

For a query target $x$, changing value $v$ to $x$ requires exactly

$$
|v-x|
$$

unit operations. Elements are independent, so the total answer is

$$
\sum_{v\in\texttt{nums}}|v-x|.
$$

Computing this sum by scanning all values for every query would take $O(nm)$. Sorting once lets the solution aggregate all values below and above each target with prefix sums.

**Sort and build cumulative sums**

After `nums.sort()`, values less than a target form a prefix and values greater than it form a suffix.

`s = list(accumulate(nums, initial=0))` creates an array of length $n+1$ where

$$
\texttt{s[i]}=\sum_{j=0}^{i-1}\texttt{nums[j]}.
$$

The initial zero makes sums of the first $i$ elements available directly and makes an empty prefix safe.

`s[-1]` is the total sum of all values.

This indexing convention is worth fixing mentally: `s[i]` excludes `nums[i]`. Consequently, when a binary search returns partition index $i$, `s[i]` is exactly the sum on its left, while `s[-1] - s[i]` is exactly the sum on its right. No minus-one boundary cases are needed for empty or full partitions.

**Cost of decreasing values above the target**

The first bisection is

`i = bisect_left(nums, x + 1)`.

Because values and queries are integers, this finds the first value at least $x+1$, which is the first value strictly greater than $x$. Values from $i$ through $n-1$ must be decreased.

Their original sum is `s[-1] - s[i]`. After conversion, their total would be `(n - i) * x`. The required decrements are

`s[-1] - s[i] - (n - i) * x`.

Values exactly equal to $x$ are excluded from this suffix because they cost zero.

**Cost of increasing values below the target**

The second bisection is

`i = bisect_left(nums, x)`.

This is the first position whose value is at least $x$, so indices before it contain exactly the values strictly below the target.

Their converted total would be `x * i`, while their current sum is `s[i]`. The number of increments is

`x * i - s[i]`.

Adding lower and upper costs gives the full absolute-difference sum. Equal values fall between the two strict groups and correctly contribute nothing.

**Trace the first query**

Sort `[3,1,6,8]` into `[1,3,6,8]` with prefix sums `[0,1,4,10,18]`.

For target one, the upper boundary starts at index one. Upper values sum to $17$, and reducing three values to one costs $17-3=14$. No value is below one, so lower cost is zero. The answer is fourteen.

For target five, values above are $6$ and $8$: cost is $(6+8)-2\cdot5=4$. Values below are $1$ and $3$: cost is $2\cdot5-(1+3)=6$. Total is ten.

**Why queries are independent**

The function never changes values to a query target. It only computes costs from the original sorted array and prefix sums. Every query therefore starts from the same data, as required.

The one actual mutation is sorting `nums` at preprocessing time. Sorting changes order but not the multiset, and absolute-difference cost depends only on values. Callers needing original order must pass a copy.

**Why binary search boundaries are exact**

Using `x+1` in the first search is safe because all values are integers. It is equivalent to `bisect_right(nums,x)`.

The second lower bound excludes equals from the lower group. Together, the groups partition all non-equal values without overlap or omission.


For every lower value $v<x$, the prefix formula contributes $x-v$. Summed over $i$ values, this is $ix-\sum v$.

For every upper value $v>x$, the suffix formula contributes $v-x$. Summed over its count, this is $\sum v-count\cdot x$.

These are precisely all terms of the required absolute-difference sum. Thus each query answer is exact.

## Complexity detail

Let $n$ be the number of values and $m$ the number of queries. Sorting costs $O(n\log n)$, and prefix construction costs $O(n)$. Each query performs two $O(\log n)$ binary searches and constant arithmetic, giving $O(m\log n)$.

Total time is $O(n\log n+m\log n)$. The prefix array and Python sorting workspace use $O(n)$ space, and the required output uses $O(m)$. The input is sorted in place.

## Alternatives and edge cases

- **Scan per query:** Directly summing absolute differences costs $O(nm)$ time.
- **Use `bisect_right`:** It can replace the `x+1` lower-bound search and expresses the upper partition directly.
- **All values equal target:** Both formulas are zero.
- **Target below all values:** The lower group is empty and only decrements contribute.
- **Target above all values:** The upper group is empty and only increments contribute.
- **Duplicate values:** Binary-search boundaries group every equal occurrence correctly.
- **Large totals:** Answers can exceed 32-bit range, so fixed-width implementations need 64-bit arithmetic.
- **Independent queries:** No computed operation is applied to `nums`.
- **Input mutation:** Sorting changes order but not query costs.
