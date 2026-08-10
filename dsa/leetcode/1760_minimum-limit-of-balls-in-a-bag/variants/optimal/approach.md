## General

**Binary-search the smallest feasible penalty**

The penalty is an integer between one and the largest original bag size. A candidate penalty `mx` asks a yes-or-no question: can every original bag be split into pieces of at most `mx` balls using no more than `maxOperations` splits?

Feasibility is monotone. If a penalty `mx` is achievable, every larger penalty is also achievable because the same splits still satisfy a weaker size limit. If `mx` is impossible, every smaller penalty is impossible because it would require at least as much splitting.

Therefore candidate penalties form a sequence of false values followed by true values. The exact solution uses `bisect_left` to find the first true candidate.

**Derive the splits required for one bag**

Consider an original bag with `x` balls. To keep every resulting bag at size at most `mx`, it must become at least:

$$
\left\lceil\frac{x}{\texttt{mx}}\right\rceil
$$

pieces. One split increases the number of pieces by exactly one, so making $p$ pieces needs $p-1$ operations. The minimum required operations are:

$$
\left\lceil\frac{x}{\texttt{mx}}\right\rceil-1.
$$

For positive integers, the exact source computes this without floating-point arithmetic as:

`(x - 1) // mx`.

To see why, write `x` as an exact multiple or a non-multiple of `mx`. If `x = q * mx`, then `(x - 1) // mx = q - 1`, matching $q$ pieces minus one split. If there is a remainder, integer division yields `q`, matching $q+1$ pieces minus one split.

For example, a bag of nine under limit three needs `(9 - 1) // 3 = 2` splits, producing three pieces. Under limit four, it also needs two splits because at least three pieces are required.

**Sum independent requirements**

Each original bag can only be split into descendants of itself; balls cannot be transferred between original bags. Therefore the minimum operations needed for a candidate penalty is the sum of the individual requirements:

`sum((x - 1) // mx for x in nums)`.

The nested helper `check(mx)` returns true exactly when that sum is at most `maxOperations`.

Using “at most” is important. A feasible solution does not have to spend every allowed operation. Extra splits could always reduce pieces further if legal, but they are unnecessary for proving that the candidate maximum is attainable.

**Use bisect on an implicit candidate range**

`range(1, max(nums) + 1)` represents every possible penalty from one through the largest bag. Python range objects store only their boundaries and support indexed access without materializing all values, which matters because the maximum may be $10^9$.

The call:

`bisect_left(range(1, max(nums) + 1), True, key=check)`

binary-searches this virtual sequence. With a key function, `bisect_left` evaluates `check` for probed range elements. Python Booleans order as `False < True`, so searching for `True` finds the first position whose feasibility key is true.

The returned value is a zero-based position in the range, not the candidate itself. Because range position zero corresponds to penalty one, the source adds one before returning.

**Why the search always finds a true value**

The upper candidate is `max(nums)`. With that penalty, every original bag already has size at most the limit, so each term `(x - 1) // mx` is zero. No operations are needed, and `check` is true.

The lower candidate one may be feasible or infeasible depending on the operation budget. Thus the searched Boolean sequence always contains at least one true value and `bisect_left` returns a valid in-range position.

**Trace the single-bag example**

For `nums = [9]` and two operations:

- Candidate five needs `8 // 5 = 1` split and is feasible.
- Candidate three needs `8 // 3 = 2` splits and is feasible.
- Candidate two needs `8 // 2 = 4` splits and is infeasible.

Monotonic search identifies three as the first feasible penalty. The construction `[3,3,3]` demonstrates achievability.

**Why the returned penalty is optimal**

`check(mx)` calculates the exact minimum number of splits necessary for all pieces to respect `mx`. Hence it returns true exactly for achievable penalties.

The predicate is monotone from false to true, and `bisect_left` returns the first true position. Adding one converts that position to its penalty value. Every smaller penalty is infeasible, while the returned penalty is feasible, so it is the minimum possible maximum bag size.

## Complexity detail

Let $n$ be the number of original bags and $M=\max(\texttt{nums})$. Computing the upper bound takes $O(n)$ time. Binary search probes $O(\log M)$ candidates. Each `check` call scans all $n$ bags and performs constant-time integer arithmetic, so total time is $O(n\log M)$, matching the manifest.

The range is lazy, the generator inside `sum` is lazy, and the algorithm stores only scalar search and arithmetic state. Auxiliary space is $O(1)$, excluding the input.

The exact helper does not stop early when its running sum exceeds `maxOperations`; `sum` evaluates every bag for each probe. An explicit loop could improve constants on infeasible candidates without changing the asymptotic bound.

## Alternatives and edge cases

- **Manual binary-search loop:** It expresses the same first-feasible search more familiarly and can use an early-exiting feasibility loop.
- **Test every penalty:** Scanning one through $M$ costs $O(nM)$ and is impossible when values reach $10^9$.
- **Repeatedly split a largest bag:** A naive heap decision does not directly capture the best final division count for each original bag and may require too many operations.
- **Floating-point ceiling:** `ceil(x / mx) - 1` is mathematically valid, but integer arithmetic avoids precision concerns.
- **Penalty one:** It requires exactly `x - 1` splits for a bag of size `x`.
- **No split needed for a bag:** When `x <= mx`, `(x - 1) // mx` is zero.
- **Exact multiple:** A bag of size `q * mx` needs `q - 1`, not `q`, splits.
- **Unused operations:** Feasibility requires no more than the budget, not exactly the budget.
- **Single bag:** The same formula and binary search apply without a special case.
- **All bags already small:** The optimum may still be smaller if operations permit further splits.
- **Large candidate range:** `range` avoids allocating up to $10^9$ integers.
- **Guaranteed true upper bound:** `max(nums)` needs zero operations.
- **Boolean ordering:** The bisect trick relies on false preceding true and on the predicate's monotonicity.
- **Positive sizes:** They make penalty one valid and ensure the integer split formula has its intended meaning.
