## General

The task combines two conditions that the returned number must satisfy:

1. it must be a **positive integer** that is **strictly greater** than the average of the array; and
2. it must be **absent** from `nums`.

The important observation is that these conditions can be handled in that order. First determine the smallest integer that could possibly satisfy the positivity and average requirements. Then move upward only while the current integer is present in the array.

**Finding the first integer strictly above the average**

Let

$$
S = \sum_{x \in \texttt{nums}} x
$$

and let $n$ be the number of elements. The exact average is $S/n$. We need the smallest integer $k$ for which

$$
k > \frac{S}{n}.
$$

For any real number $a$, the smallest integer strictly greater than $a$ is

$$
\lfloor a \rfloor + 1.
$$

This formula also handles an average that is already an integer. For example, if the average is exactly $4$, the answer must start at $5$, not $4$, because the comparison is strict. If the average is $4.7$, its floor is $4$, so the first integer above it is again $5$.

The implementation computes this value as:

`sum(nums) // len(nums) + 1`

Python's `//` operator performs floor division when the divisor is positive, and `len(nums)` is always positive because the array is nonempty. That detail matters for negative sums. For instance, $-3/2=-1.5$, and `-3 // 2` is $-2$, the mathematical floor, so adding one gives $-1$, the smallest integer strictly greater than $-1.5$. No floating-point calculation is needed, so there is no danger of rounding an average such as $2/3$ incorrectly.

The requested result must also be positive. Therefore, if the first integer above the average is zero or negative, the search should begin at $1$. The line

`ans = max(1, sum(nums) // len(nums) + 1)`

combines both lower bounds. After this line, `ans` is exactly the smallest positive integer that is strictly greater than the average. It is not merely a convenient starting point: every smaller integer violates at least one of the two numerical requirements.

**Making absence checks fast**

The remaining question is whether the candidate occurs in `nums`. Repeatedly searching the original list would cost linear time per candidate. Instead, the solution creates

`s = set(nums)`

so membership checks are expected constant-time operations. Duplicates do not need special handling because the question only asks whether a value appears at least once.

If `ans` is in the set, it cannot be returned, so the only possible next candidate is `ans + 1`. The loop keeps increasing the candidate by one:

`while ans in s:`

`    ans += 1`

When the loop stops, `ans` is absent. Increasing an integer preserves both positivity and the property of being strictly greater than the average, so no numerical condition needs to be checked again.

Consider `nums = [3, 5]`. Its average is $4$, so the initial candidate is $5$. Because $5$ is present, the loop advances to $6$. Six is absent, and it is returned. This also explains why simply returning the first integer above the average would be insufficient.

As another example, take `nums = [-4, -2, 1]`. The average is $-5/3$, and its floor is $-2$. Adding one gives $-1$, but the result must be positive, so `max` changes the starting candidate to $1$. Since $1$ is present, the loop advances to $2$, which is the answer.

**Why stopping at the first missing candidate gives the minimum**

At initialization, every positive integer smaller than `ans` is disqualified because it is not strictly above the average. During the loop, each value that the algorithm passes over is disqualified because the set confirms that it is present in `nums`. Consequently, when the loop reaches its first absent value, every smaller positive integer has a known reason that it cannot be returned. The current value satisfies every requirement, so it is the smallest valid result.

The answer is guaranteed to be found. The array contains only finitely many distinct values, while the positive integers continue forever. Even if several consecutive values beginning at the threshold are present, eventually the loop reaches one that is not in the finite set.

## Complexity detail

Let $n$ be `len(nums)`, and let $k$ be the number of consecutive present integers beginning with the initial candidate.

Computing `sum(nums)` examines all $n$ elements, and constructing `set(nums)` also processes all $n$ elements. The loop performs $k + 1$ membership checks: one for each present candidate and one final failed check for the returned candidate.

Although the loop appears open-ended, $k \le n$. Every successful iteration corresponds to a different integer that is actually stored in the set, and a set built from $n$ array positions can contain at most $n$ distinct values. Therefore, the total expected running time is

$$
O(n + k) = O(n).
$$

The word “expected” reflects the usual expected constant time of Python hash-set membership. Under the standard hash-table model used for this solution, the manifest's `O(n)` bound is accurate.

The set stores at most $n$ distinct integers, so the auxiliary space usage is $O(n)$. The variables `ans` and the computed sum require only constant additional space.

## Alternatives and edge cases

- **Sorting first:** Sorting the distinct values would also make it possible to walk upward from the threshold, but sorting costs $O(n \log n)$ time. The hash set preserves linear expected time and expresses the only needed operation—membership—directly.
- **Repeated list membership checks:** Testing `ans in nums` without building a set can scan the whole array for every candidate. With up to $n$ consecutive candidates present, that approach can take $O(n^2)$ time.
- **Floating-point average:** Computing `sum(nums) / len(nums)` and then rounding introduces unnecessary floating-point behavior. Exact floor division gives the correct strict integer threshold for positive, zero, and negative sums.
- **An integral average:** If the average is exactly $a$, the search must begin at $a+1$, because “strictly greater” excludes $a$. The added one after floor division handles this automatically.
- **A negative average:** Positivity becomes the stronger lower bound, so the search begins at $1$. The `max(1, ...)` operation is essential here.
- **The initial candidate is present:** The loop skips it and every immediately following present value. For `[3, 5]`, it skips $5$ and returns $6$.
- **Duplicates:** Multiple copies of a number have the same effect as one copy: that number is present and must be skipped. Converting to a set intentionally removes multiplicity.
- **Values below the threshold:** Their presence is irrelevant because none can satisfy the strict-average requirement. The algorithm never wastes time searching downward.
- **A long consecutive run:** Even if all of the next several integers occur in the array, each successful loop iteration skips a distinct set member, so the scan remains linear overall.
