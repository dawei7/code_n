## General

**Search for the smallest feasible maximum**

An operation moves one unit only from index `i` to `i-1`. Mass can travel left but never right. The exact solution does not directly compute the known prefix-average formula described by the variant summary. Instead, it binary-searches a candidate maximum `mx` and asks whether the array can be rearranged, using legal leftward moves, so that every position is at most `mx`.

Feasibility is monotone: if a cap `mx` is achievable, every larger cap is also achievable by using the same operations. This true-then-true structure permits binary search for the smallest feasible cap.

**Process unavoidable overflow from right to left**

The helper `check(mx)` maintains `d`, the amount of excess mass from the processed suffix that must be pushed one position farther left if every processed position is to stay at most `mx`.

It scans `nums[:0:-1]`, which is a reversed copy containing indices $n-1$ down through 1. Index 0 is deliberately excluded because nothing can move left from it.

At a position containing `x`, the total mass that this position must handle is its own `x` plus overflow `d` received from positions to its right. The position can retain at most `mx`. Therefore the amount forced farther left is

`max(0, d + x - mx)`.

If `d + x <= mx`, the position has enough capacity to absorb all arriving excess, and no overflow continues, so `d` becomes zero. If the total exceeds the cap, exactly the difference must be moved left.

After processing positions 1 through $n-1$, all unavoidable overflow reaches index 0. That index initially contains `nums[0]` and cannot send anything farther left. The cap is feasible exactly when

`nums[0] + d <= mx`.

**Why this feasibility test is necessary**

Consider any suffix ending at the array's right edge. Its excess beyond the combined capacity `mx` per position cannot move right or disappear; it must cross the suffix's left boundary. The right-to-left recurrence computes precisely this forced excess for successively larger suffixes.

At each position, retaining up to `mx` is always best for reducing what must travel farther left. If even this maximum retention leaves `d` units, every valid sequence of operations must move at least that much left. When the final load at index 0 exceeds `mx`, no operation can repair it because index 0 has no legal destination to its left.

**Why the test is sufficient**

When the recurrence finds `nums[0]+d <= mx`, construct operations from right to left. At each position, move exactly the computed positive excess to its left neighbor and leave at most `mx` behind. These moves are legal because excess represents available positive units. Continuing left eventually gives index 0 no more than the cap.

Thus the recurrence is not only a lower-bound calculation; it describes a feasible redistribution whenever the final check passes.

For `nums = [3,7,1,6]` and `mx=5`:

- At index 3, value 6 leaves overflow 1.
- Index 2 handles `1+1=2`, which fits, so overflow returns to zero.
- Index 1 contains 7 and leaves overflow 2.
- Index 0 receives that overflow, reaching `3+2=5`, so cap 5 is feasible.

For cap 4, the propagated overflow eventually makes index 0 exceed 4, so it is infeasible.

**Binary-search mechanics**

The search interval starts at `left=0` and `right=max(nums)`. Zero is a safe lower bound because values are non-negative. The original array itself proves `max(nums)` feasible without any operations, so the upper bound is valid.

At each step, `mid = (left + right) >> 1` computes the floor midpoint. If `check(mid)` succeeds, the minimum feasible cap lies at or below `mid`, so `right=mid`. Otherwise every cap through `mid` is infeasible, so `left=mid+1`. When the bounds meet, that value is the first feasible cap.

**Relationship to prefix averages**

Because mass can only move left, the total of the first $i+1$ positions can never be moved outside that prefix to the right. Any cap $M$ must satisfy

$$
M \ge
\left\lceil
\frac{\texttt{nums}[0]+\cdots+\texttt{nums}[i]}{i+1}
\right\rceil
$$

for every prefix. The optimal answer is the maximum of these ceiling averages. That yields an $O(n)$ direct algorithm, but it is an alternative to the exact binary-search implementation, not what this file executes.

## Complexity detail

Let $n$ be the array length and $V=\max(\texttt{nums})$. Binary search performs $O(\log(V+1))$ feasibility checks. Each check scans $n-1$ values and performs constant-time arithmetic, giving $O(n\log(V+1))$ total time. This differs from the manifest's $O(n)$ claim for the direct prefix-average method.

The slice `nums[:0:-1]` allocates a reversed list of $n-1$ references on every call to `check`. Only one such slice exists at a time, so peak auxiliary space is $O(n)$, not the manifest's $O(1)$. Iterating indices with `range(len(nums)-1,0,-1)` would make the same feasibility test constant-space.

The accumulator `d` can reach the total array sum, up to $10^{14}$ under the constraints. Python integers are safe; fixed-width implementations need 64-bit arithmetic.

## Alternatives and edge cases

- **Maximum prefix ceiling average:** Maintain a running prefix sum and maximize `(sum+i)//(i+1)`. This directly computes the lower bound that is also achievable, giving the manifest's intended $O(n)$ time and $O(1)$ space.
- **Binary search without slicing:** Scan indices from right to left to preserve $O(n\log V)$ time while reducing auxiliary space to $O(1)$.
- **Simulate unit operations:** Moving one unit at a time can require an enormous number of steps because values reach $10^9$. Aggregated overflow represents all equivalent moves at once.
- **Already balanced under a cap:** The feasibility recurrence lets each position absorb incoming overflow up to `mx` and propagates only what is unavoidable.
- **Large first element:** Nothing can move from index 0 to the right, so the answer can never be below `nums[0]`.
- **Zeros:** They provide capacity to absorb overflow from the right and are handled by the same formula.
- **All values equal:** The original maximum is already minimal, and binary search finds that value.
- **Mass conservation:** Operations change positions but preserve the total sum; feasibility depends on distributing that fixed mass subject to one-way movement.
- **One-way restriction:** Using only the overall average is insufficient. Every prefix average matters because prefix mass cannot escape to the right.
- **Upper bound:** `max(nums)` is always feasible by performing no operations.
- **Manifest mismatch:** The exact code uses $O(n\log V)$ binary search and $O(n)$ transient slice space, not the one-pass constant-space formula.
