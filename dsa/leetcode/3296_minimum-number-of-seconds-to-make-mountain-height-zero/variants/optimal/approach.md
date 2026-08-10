## General

**Search time because feasibility is monotone.** Suppose the workers can remove the full mountain within $t$ seconds. Giving them any larger time cannot reduce what they can accomplish, so every time after $t$ is also feasible. The possible times therefore form a sequence of `False` values followed by `True` values. The first `True` is the minimum required time, which is exactly what binary search can locate.

The source represents candidate times with `range(10**16)` and calls `bisect_left(..., True, key=check)`. Python's keyed `bisect_left` does not build a Boolean list. It probes time values in the range, calls `check` for each probe, and finds the leftmost point where the monotone key equals `True`.

**Compute one worker's capacity at a fixed time.** If a worker with base time $w$ removes $x$ units, the successive costs are $w,2w,\ldots,xw$. Its total is

$$
w(1+2+\cdots+x)=w\frac{x(x+1)}2.
$$

Within candidate time $t$, the largest feasible $x$ satisfies

$$
w\frac{x(x+1)}2\le t.
$$

Solving the corresponding quadratic inequality gives

$$
x\le\sqrt{\frac{2t}{w}+\frac14}-\frac12.
$$

The source computes `int(sqrt(2 * t / wt + 1 / 4) - 1 / 2)` for every `wt`. Since the expression is nonnegative, `int` truncation has the same intended effect as taking the floor. The resulting integer is added to `h`, the total number of height units all workers can remove by time $t$.

Workers operate simultaneously, so capacities add. Assigning each worker up to its personal capacity produces a total of `h` removable units without making any worker exceed time $t$. If `h >= mountainHeight`, enough work can be distributed and `check(t)` returns `True`. If the sum is smaller, no allocation can reach the required height because every worker is already bounded by that capacity.

It is harmless if the summed capacity is greater than the mountain height. Workers may remove any non-negative integer amount, so excess theoretical capacity can simply remain unused.

**Why the binary-search domain is large enough.** The stop value `10**16` is excluded from the Python range, but every legal answer is below it. In the worst single-worker scenario, $H=10^5$ and $w=10^6$, so one worker needs

$$
10^6\cdot\frac{10^5(10^5+1)}2
=5{,}000{,}050{,}000{,}000{,}000,
$$

which is less than $10^{16}$. If multiple workers exist, they cannot make the minimum time worse than assigning all work to one of them. Thus the range contains at least one feasible time, and `bisect_left` returns a valid index rather than the insertion point at the stop.

**Why the first feasible time is optimal.** For each fixed $t$, the capacity formula yields the maximum work each worker can individually finish. Their sum is therefore an exact feasibility test in ideal arithmetic. Feasibility never changes from true back to false as $t$ increases. Binary search maintains the boundary between impossible and possible times and returns the smallest possible integer time.

**The implementation is not using an exact integer square root.** Despite the manifest summary, the expression contains ordinary `/` division and `math.sqrt`, so Python converts the calculation to double-precision floating point. Near a triangular-number boundary, rounding could theoretically place the computed value just below or above the exact integer and make one worker's capacity off by one. That can make `check` incorrect at a boundary and violate binary search's exactness.

The intended formula is mathematically right, and floating point often passes typical inputs, but an interview-quality robust version should use integer arithmetic—for example `isqrt(1 + 8 * (t // wt))` followed by a small correction—or verify the candidate with the original triangular inequality. The Approach must distinguish that reliable algorithm from what this exact source literally executes.

## Complexity detail

Let $W$ be the number of workers and $U=10^{16}$ be the fixed search-domain size. Binary search performs $O(\log U)$ feasibility probes, about 54. Each `check` scans all $W$ worker times and performs constant work, so total time is $O(W\log U)$. In terms of constraints, a tighter chosen upper bound could be expressed using the mountain height and a worker time, but the hard-coded $U$ makes the source's bound direct.

The checker stores only `h`, `t`, and the current worker time. `range` is a lazy constant-size object, and `bisect_left` is iterative. Excluding input storage, auxiliary space is $O(1)$. Floating-point operations remain constant-time at these fixed numeric ranges.

## Alternatives and edge cases

- **Exact integer inverse:** Let `q = t // wt`, compute `x = (isqrt(1 + 8*q) - 1) // 2`, and verify `x*(x+1)//2 <= q`. This preserves the same bounds and removes the source's floating-rounding risk.
- **Per-worker inner binary search:** Binary-search each worker's removable height inside every outer time check. It is exact but adds another logarithmic factor.
- **Priority queue simulation:** Repeatedly assign the next height unit to the worker whose next completion time is smallest. It can be useful when the mountain is small but costs roughly $O(H\log W)$ rather than logarithmic search over time.
- **Only one worker:** The answer is exactly `workerTimes[0] * H * (H + 1) // 2`; the general check and binary search still find it.
- **Height one:** A worker can remove the unit after its first base-time interval. The minimum worker time is the answer.
- **More capacity than height:** The test uses `>=` because unused capacity is allowed; requiring equality would be wrong.
- **Very slow worker:** Its computed capacity may be zero for small candidate times, which contributes nothing without requiring a special case.
- **Duplicate worker times:** Workers are separate and operate concurrently, so equal times must be counted separately; the loop correctly adds both capacities.
- **Floating-point boundary:** Exact triangular completion times are precisely where rounding by one is most dangerous. An integer square root or post-check should be preferred for guaranteed correctness.
- **Search upper bound:** `range(10**16)` excludes $10^{16}$, but the legal worst-case one-worker time is about $5.00005\cdot10^{15}$, so the answer is still contained.
- **Python-version requirement:** The `key` argument to `bisect_left` requires a sufficiently recent Python version. A manual binary-search loop avoids that compatibility dependency.
- **Manifest discrepancy:** The time and space classes are reasonable, but the source does not perform the claimed exact integer-square-root inversion.
