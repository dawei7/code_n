## General

**Find the exact operation count for a fixed k**

One operation chooses one index and subtracts `k` from that element. Operations on different indices do not interact, so the minimum total is the sum of the minimum operations required by each element separately.

For a positive value `x`, after `q` operations its value is `x - qk`. It becomes non-positive when

$$
x-qk\le0,
$$

or equivalently $q\ge x/k$. The least integer `q` satisfying this is

$$
\left\lceil\frac{x}{k}\right\rceil.
$$

The source calculates the ceiling using integer arithmetic:

`(x + k - 1) // k`.

This formula handles exact divisibility correctly. If `x = 6` and `k = 3`, it gives 2, because reaching zero is sufficient. If `x = 7`, it gives 3, allowing the final value to become negative.

Therefore the exact minimum operation count is

$$
\operatorname{nonPositive}(\texttt{nums},k)
=
\sum_{x\in\texttt{nums}}
\left\lceil\frac{x}{k}\right\rceil.
$$

The nested `check(k)` computes this sum as `t` and returns whether `t <= k * k`.

**Feasibility changes only once**

Binary search requires a monotone condition. As positive `k` grows, every ceiling term $\lceil x/k\rceil$ stays the same or decreases. At the same time, the allowed operation budget $k^2$ strictly increases.

Thus, once some `k` is feasible, every larger `k` is also feasible. The possible values have the form

`false, false, ..., false, true, true, ..., true`.

The answer is the first true position.

This monotonicity combines both sides of the inequality. It would not be enough to observe only that the required operations fall; the growing $k^2$ allowance makes feasibility even more firmly monotone.

**Choose safe search boundaries**

The source starts with `l = 1` because `k` must be a positive integer.

It uses the fixed upper bound `r = 10**5`. This value is always feasible under the stated constraints. Every `nums[i]` is at most $10^5$, so subtracting $10^5$ once makes each positive element non-positive. The required operation count is therefore $N\le10^5$, while

$$
r^2=10^{10}.
$$

Hence the first feasible value is guaranteed to lie in the inclusive interval `[l, r]`.

A tighter upper bound from the contract is

$$
H=\max\left(\max(\texttt{nums}),\left\lceil\sqrt N\right\rceil\right).
$$

At `k = H`, every element needs at most one operation and $N\le H^2$, so `H` is feasible. The exact source does not calculate or use this tighter bound; it always searches to $10^5$.

**Use lower-bound binary search**

While `l < r`, the source chooses

`mid = (l + r) >> 1`,

which is integer floor division by two for these nonnegative bounds.

If `check(mid)` is true, `mid` may be the first feasible value, but a smaller feasible value may exist. The source keeps `mid` by setting `r = mid`.

If the check is false, monotonicity proves every value at or below `mid` is false. The first true value must be at least `mid + 1`, so it sets `l = mid + 1`.

Each update preserves the fact that the first feasible value lies in `[l, r]` and strictly shrinks the interval. When the bounds meet, only one candidate remains, and the source returns it.

**Trace the first example**

For `nums = [3,7,5]`:

At `k = 2`, the operation counts are

$$
\left\lceil\frac32\right\rceil+
\left\lceil\frac72\right\rceil+
\left\lceil\frac52\right\rceil
=2+4+3=9.
$$

The allowance is $2^2=4$, so 2 is infeasible.

At `k = 3`, the counts are $1+3+2=6$, while the allowance is $3^2=9$. Thus 3 is feasible. Monotonicity makes every larger value feasible, and the failure at 2 proves 3 is the minimum.

**Why the summed count is genuinely minimal**

Each operation changes exactly one chosen element. Element `x` cannot become non-positive in fewer than $\lceil x/k\rceil$ operations, so any global plan needs at least the sum of those per-element lower bounds.

Applying exactly that many operations to each index achieves a non-positive value for every element. The lower bound is attainable, making the sum the true minimum rather than only an estimate. The feasibility test therefore matches the problem's definition exactly.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$ and let $M=10^5$ be the exact source's fixed upper search bound. One `check` scans all $N$ elements and costs $O(N)$ time. Binary search performs $O(\log M)$ checks, so exact-source time is $O(N\log M)$. With $M=10^5$, this is about 17 full scans.

The manifest states $O(N\log H)$ using the tighter problem-derived bound $H$. That would describe a version setting `r = H`. Since the source always uses $10^5$, $O(N\log 10^5)$ is the faithful bound; both are small logarithmic factors under the fixed constraints, but their parameterization differs.

The check retains only `t` and the current `x`, and binary search stores three integer bounds. No input-sized structure is allocated, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Use the tighter upper bound H:** Compute the maximum value and an integer ceiling square root of $N$, then binary-search through `H`. This can reduce iterations for small inputs and matches the manifest's named bound.
- **Linear search over k:** Testing 1, 2, 3, and so on eventually finds the answer but may require up to $10^5$ scans, giving $O(NM)$ time.
- **Stop a failed check early:** Once `t > k * k` during accumulation, the predicate can return false immediately. This improves some cases but does not change the worst-case bound.
- **Floating-point ceiling:** Using `ceil(x / k)` introduces unnecessary floating point. `(x + k - 1) // k` is exact for positive integers.
- **Single element equal to one:** `k = 1` needs one operation and permits $1^2=1$, so the answer is 1.
- **Exact divisibility:** An element reaching exactly zero is finished; the ceiling formula does not add an unnecessary extra operation.
- **Very large k:** Every element needs one operation once `k` reaches the maximum value, while the permitted budget continues growing quadratically.
- **All elements positive:** Every element requires at least one operation for every finite `k`, so the required count never falls below $N$.
- **Integer size:** The accumulated count and `k * k` fit ordinary fixed-width ranges here, and Python integers also eliminate overflow concerns.
- **Minimum-search branch condition:** A feasible midpoint remains a candidate through `r = mid`; using `r = mid - 1` with this loop structure could skip the answer.
