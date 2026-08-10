## General

The value of a nonempty subarray is its maximum element minus its minimum element. The crucial permission in this version of the problem is that the **same subarray may be selected more than once**. Therefore, after finding the best possible value of one subarray, the optimal strategy is to select a subarray attaining that value all $k$ times.

The exact source returns:

`k * (max(nums) - min(nums))`

The reasoning has two parts: the global range is an upper bound for every subarray, and that upper bound is attainable.

**Bounding every subarray value**

Let

$$
M=\max(\texttt{nums})
$$

and

$$
m=\min(\texttt{nums}).
$$

For any subarray `nums[l..r]`, its maximum cannot exceed the maximum of the entire array:

$$
\max(\texttt{nums}[l..r])\le M.
$$

Likewise, its minimum cannot be smaller than the global minimum:

$$
\min(\texttt{nums}[l..r])\ge m.
$$

Subtracting the second relationship from the first gives:

$$
\max(\texttt{nums}[l..r])-\min(\texttt{nums}[l..r])
\le M-m.
$$

Thus no individual subarray can have value greater than the global range $M-m$.

**Attaining the global range**

An upper bound is useful only if some legal subarray reaches it. The entire array is itself a nonempty subarray. It contains both an occurrence of $M$ and an occurrence of $m$, so its maximum is $M$, its minimum is $m$, and its value is exactly $M-m$.

A smaller subarray spanning an occurrence of the global minimum and an occurrence of the global maximum also attains this value, regardless of which one appears first. The source does not need to locate those indices because the whole array always supplies a simple witness.

Therefore, the maximum value of one selectable subarray is exactly:

$$
V=M-m.
$$

**Using repetition to optimize exactly $k$ choices**

Each of the $k$ chosen subarrays contributes at most $V$, so any total is bounded by:

$$
kV.
$$

The contract explicitly permits choosing the same pair of endpoints repeatedly. Select the entire array $k$ times. Every selection contributes $V$, giving total $kV$ and attaining the upper bound.

This removes all interaction among the $k$ choices. There is no need to find the second-best subarray, reserve endpoints, or prevent overlap. Repetition is legal, and the choices do not modify the array.

For `nums = [4, 2, 5, 1]`, the global maximum is $5$ and the global minimum is $1$, so $V=4$. With `k = 3`, selecting the entire array three times gives $3\cdot4=12$.

For `nums = [1, 3, 2]`, $V=3-1=2$. Selecting any value-two subarray twice produces total four. The examples use two different subarrays, but the rules would also permit selecting `nums[0..2]` twice.

**Why “exactly” $k$ causes no complication**

Subarray values are always nonnegative because a maximum is at least its corresponding minimum. Even if every value is identical and the best subarray value is zero, selecting it exactly $k$ times is legal and produces the only possible total, zero.

There is no advantage or possibility of selecting fewer than $k$ because the statement requires exactly $k$. Multiplication by `k` accounts for every required selection.

**What the one-line implementation actually scans**

Python's `max(nums)` scans the array once, and `min(nums)` scans it a second time. The source does not combine both extrema into one explicit loop. Two linear passes still have linear asymptotic time:

$$
n+n=2n=O(n).
$$

The nonempty-array constraint guarantees both built-ins receive at least one value, so neither needs a fallback initializer.

## Complexity detail

Let $n$ be the array length.

The exact source performs one $O(n)$ pass for `max` and another $O(n)$ pass for `min`. The subtraction and multiplication are constant-time under the usual bounded-integer model. Total time is $O(n)$.

An implementation could find both extrema in one explicit pass, but it would have the same asymptotic bound. The source favors the clarity of the two built-ins.

Only the global maximum, global minimum, and final arithmetic result are needed. The built-ins do not create copies of the array, so auxiliary space is $O(1)$.

The product can exceed 32-bit range: the largest possible difference is $10^9$ and $k$ can be $10^5$, producing up to $10^{14}$. Python integers grow as needed. A fixed-width implementation should use a 64-bit integer for the total.

Every element must be inspected in the worst case because an unseen position could contain a new global minimum or maximum. The linear running time is asymptotically optimal.

## Alternatives and edge cases

- **Enumerate all subarrays:** Computing every subarray range takes at least $O(n^2)$ candidates and is unnecessary because the entire array already attains the global upper bound.
- **Find the best $k$ distinct subarrays:** That solves the harder follow-up version, not this contract. Here, identical endpoints may be selected repeatedly.
- **Locate the minimum and maximum indices:** Their positions are unnecessary. The entire array contains both values and is always a legal witness.
- **Single-pass extrema:** Tracking `low` and `high` together avoids the second scan but remains $O(n)$ time and $O(1)$ space. It is a valid alternative, not the exact source form.
- **One-element array:** The global maximum equals the global minimum, every subarray value is zero, and the answer is zero for every legal $k$.
- **All elements equal:** The same zero-range reasoning applies even when the array has many possible subarrays.
- **Minimum appears after maximum:** Endpoint order does not matter because the subarray spanning both positions includes both extrema.
- **Multiple global extrema:** Any subarray containing at least one global minimum and one global maximum attains the same best value.
- **Large `k`:** No additional search is required. Repetition turns the answer into direct multiplication, but the total should use sufficiently wide integer arithmetic.
- **Overlapping selections:** Overlap is explicitly allowed and selections do not consume elements. Choosing one subarray places no restriction on the next choice.
