## General

**Search for the largest achievable minimum gap**

After choosing `k` candies, sort their prices. The smallest absolute difference among any pair is attained by some adjacent pair in that sorted selection. If every adjacent selected-price gap is at least `x`, then every more distant pair also differs by at least `x`.

This turns a candidate tastiness `x` into a yes-or-no question: can at least `k` prices be selected so consecutive selected prices differ by at least `x`?

Feasibility is monotone. If gap `x` is achievable, every smaller gap is achievable using the same basket. If `x` is impossible, every larger gap is also impossible. Binary search can therefore locate the greatest feasible value.

**Sort prices before the greedy check**

`price.sort()` arranges candies in nondecreasing price order. Candies remain distinct objects even when prices are equal; duplicate values simply have gap zero.

Sorting makes it possible to greedily choose the earliest next price satisfying the required difference.

**Greedily select the smallest possible next price**

Inside `check(x)`, `pre` is the last chosen price and `cnt` is the number chosen.

The initialization `pre=-x` makes the first positive price automatically eligible:

$$
\texttt{cur}-(-x)=\texttt{cur}+x\ge x.
$$

Thus the first sorted price is selected without a special branch.

For each later `cur`, it is selected exactly when `cur-pre>=x`. The greedy check always takes the earliest price that can follow the previous choice.

**Why choosing early maximizes how many candies fit**

Suppose some feasible selection's next chosen price is `y`, while greedy chooses an eligible `g<=y`. Replacing `y` with `g` does not violate the gap from the prior selected price because `g` was eligible. It can only leave at least as much room for every future choice because future prices need to be `x` above a no-larger previous value.

Applying this exchange repeatedly shows that after any number of selections, the greedy method's last chosen price is no greater than that of any other method selecting the same count. Therefore, if any selection can reach `k` candies, greedy reaches at least `k` as well.

`check(x)` is consequently an exact feasibility test, not a heuristic.

**Binary-search boundaries**

The minimum possible tastiness is zero, so `l=0` is always feasible. The largest price difference in the entire array is `price[-1]-price[0]`, so no pairwise minimum can exceed it; this becomes `r`.

The upper midpoint

`mid=(l+r+1)>>1`

is the ceiling of their average. If `check(mid)` succeeds, `mid` remains a possible answer and `l=mid`. Otherwise, `mid` and all larger gaps are impossible, so `r=mid-1`.

Using the upper midpoint prevents an infinite loop when `l` and `r` are adjacent and the lower value is feasible.

When they meet, `l` is the largest feasible tastiness.

**Trace the main sample**

Sorting `[13,5,1,8,21,2]` gives `[1,2,5,8,13,21]`.

For candidate gap 8, greedy selects 1, then 13, then 21, reaching three candies. Gap 8 is feasible.

For gap 9, greedy selects 1, then 13, but no remaining price is at least 22, so it selects only two. Gap 9 is infeasible. The optimum is therefore eight.

**Duplicate prices**

When all prices equal and `k>=2`, every basket contains two candies with price difference zero. `check(0)` selects enough candies, while every positive candidate fails. Binary search returns zero.

**Why only adjacent selected prices need checking**

If selected prices in sorted order are $p_1\le p_2\le\cdots\le p_k$, then for any nonadjacent pair $p_i,p_j$ with $j>i+1$,

$$
p_j-p_i
=
(p_{i+1}-p_i)+\cdots+(p_j-p_{j-1}).
$$

All terms are nonnegative, so this distance is at least each intervening adjacent gap. The basket's minimum pairwise distance must therefore occur between adjacent selected prices. Enforcing the greedy gap from each selected price to the next is sufficient to enforce tastiness across every pair.


The greedy test returns true exactly for achievable candidate gaps. Feasibility changes monotonically from true to false as the candidate increases. Binary search returns the boundary's last true value, which is precisely the maximum possible minimum pairwise difference.

## Complexity detail

Let $n$ be the number of candies and $R=\max(\texttt{price})-\min(\texttt{price})$. Sorting costs $O(n\log n)$. Each feasibility check scans $n$ prices, and binary search performs $O(\log(R+1))$ checks.

Total time is

$$
O(n\log n+n\log(R+1)).
$$

Python's in-place Timsort can use $O(n)$ temporary memory in the worst case. The greedy check itself uses $O(1)$ state. The input list is mutated by sorting.

## Alternatives and edge cases

- **Enumerate baskets:** There are too many $\binom nk$ selections.
- **Dynamic programming:** It is unnecessary because monotone feasibility has a greedy solution.
- **`k=2`:** The optimum is the global maximum-minus-minimum price gap.
- **`k=n`:** Every candy is selected, so the answer is the smallest adjacent gap after sorting.
- **Duplicate prices:** They may force tastiness zero.
- **Candidate zero:** Every candy can follow the previous one, so it is always feasible.
- **First selection:** `pre=-x` is a compact way to accept the first positive price.
- **Upper midpoint:** It guarantees progress when maximizing a feasible integer.
- **Distinct candies:** Equal prices can still belong to different candy objects.
- **Mutation:** The exact method sorts `price` in place.
