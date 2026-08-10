## General

Each original value $x$ may be moved anywhere in the closed interval

$$
[x-k,x+k].
$$

The score depends only on the final maximum and minimum. Let

$$
\text{mi}=\min(\texttt{nums}),
\qquad
\text{mx}=\max(\texttt{nums}).
$$

The initial range is $\text{mx}-\text{mi}$. The smallest original value can be increased by at most $k$, and the largest can be decreased by at most $k$. Together these changes can close the gap by at most $2k$.

This suggests

$$
\text{mx}-\text{mi}-2k.
$$

A score cannot be negative, so the result is

$$
\max(0,\text{mx}-\text{mi}-2k).
$$

**Why this is a lower bound.** In any allowed result, the element originally equal to `mi` is at most $\text{mi}+k$, while the element originally equal to `mx` is at least $\text{mx}-k$. If $\text{mx}-k>\text{mi}+k$, those two particular final values alone remain separated by at least

$$
(\text{mx}-k)-(\text{mi}+k)
=\text{mx}-\text{mi}-2k.
$$

The overall maximum-minus-minimum cannot be smaller than the gap between any two final elements.

If the two adjustment intervals overlap, this arithmetic lower bound is negative, but zero is the universal lower bound for a range.

**Why the bound is achievable when a positive gap remains.** Suppose $\text{mx}-k>\text{mi}+k$. Move a minimum occurrence upward to $\text{mi}+k$ and a maximum occurrence downward to $\text{mx}-k$. For any intermediate original value $x$:

- if $x$ is too low, increase it toward the lower endpoint;
- if $x$ is too high, decrease it toward the upper endpoint;
- if it is already between those endpoints, leave it or choose zero adjustment.

Because $\text{mi}\le x\le\text{mx}$, its allowed interval intersects the target interval $[\text{mi}+k,\text{mx}-k]$. It can therefore be placed without extending either extreme. The achieved score is exactly the positive gap.

**Why zero is achievable when intervals overlap.** If $\text{mx}-\text{mi}\le2k$, then

$$
\text{mx}-k\le\text{mi}+k.
$$

The adjustment intervals of the smallest and largest values overlap. Every intermediate value's interval also covers at least part of this common central region. Choose one integer target in the intersection and move every element to it. All final values are equal, so score zero is achieved.

More explicitly, the intersection of all element intervals is determined by the largest lower endpoint and smallest upper endpoint. Since $x-k$ increases with $x$, the largest lower endpoint is $\text{mx}-k$. Since $x+k$ also increases with $x$, the smallest upper endpoint is $\text{mi}+k$. Thus every interval shares a common point exactly when $\text{mx}-k\le\text{mi}+k$. No intermediate element can destroy an overlap already established by the original extremes.

When the intervals do not all overlap, the same endpoint calculation identifies the unavoidable empty gap between $\text{mi}+k$ and $\text{mx}-k$. Moving the extremes to those nearest endpoints closes as much of the gap as any legal operation permits, while intermediate intervals can be clamped into the resulting band. This gives a constructive witness for the formula in both cases.

The operation permits any integer `x` from `-k` through `k` and may be applied at most once. Choosing zero is allowed, so “at most once” creates no additional restriction; every element simply selects one final point in its interval.

For `[0,10]` and $k=2$, the extremes can move to 2 and 8, leaving range 6. For `[1,3,6]` and $k=3$, the extreme intervals overlap at values such as 3 or 4, so all elements can be made equal and the answer is zero.

## Complexity detail

Let $n$ be the array length. Finding minimum and maximum each takes a linear scan. Two scans remain linear.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$ auxiliary space.

The input is not modified. Only two extremes and the returned arithmetic result are stored.

## Alternatives and edge cases

- **Adjust every element greedily:** Explicit choices are unnecessary because the achievable optimum depends only on original extremes.
- **Sort the array:** The minimum and maximum would become endpoints, but sorting costs $O(n\log n)$ and is stronger than needed.
- **Binary search a target interval:** This can test feasibility but adds complexity when the closed-form intersection is immediate.
- **One element:** Maximum equals minimum, so the score is zero for every `k`.
- **`k = 0`:** No value changes, and the formula returns the original range.
- **Original range exactly `2k`:** Extreme intervals touch at one value, and score zero is achievable.
- **Original range smaller than `2k`:** The raw subtraction is negative, so `max(0, ...)` is essential.
- **Duplicate extremes:** Every occurrence has the same movement interval and can be moved into the same optimal final range.
- **Intermediate elements:** They cannot force a wider result because their original values lie between the two extremes.
- **Integer target:** All endpoints are integers, so a nonempty overlap contains an integer boundary point.
- **At most one operation:** Selecting the entire adjustment in one step reaches any point in `[x-k,x+k]`; repeated operations are unnecessary.
- **No input mutation:** The solution computes the minimum score without constructing a transformed array.
