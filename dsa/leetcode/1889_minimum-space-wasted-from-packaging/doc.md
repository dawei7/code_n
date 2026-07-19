# Minimum Space Wasted From Packaging

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-space-wasted-from-packaging/) |
| Frontend ID | 1889 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

There are $N$ packages, each of which must be placed alone in one box. The package sizes are given by `packages`. Several suppliers offer different sets of box sizes, described by `boxes`; supplier `j` offers an unlimited number of boxes of every size in `boxes[j]`. A package fits when its size is less than or equal to the chosen box size.

Choose exactly one supplier and obtain every required box from that supplier. Placing a package of size $p$ in a box of size $b$ wastes $b-p$ units of space. Minimize the sum of this waste over all packages. Return `-1` if no single supplier can fit every package; otherwise return the minimum total waste modulo $10^9+7$.

### Function Contract

**Inputs**

- `packages`: an array of $N$ package sizes.
- `boxes`: an array of $M$ suppliers, where `boxes[j]` lists supplier `j`'s distinct box sizes.
- Let $B$ be the sum of all suppliers' box-size counts and $K$ the maximum count for one supplier.
- $1 \le N,M,B \le 10^5$ and $1 \le K \le B$.
- Every package and box size lies between $1$ and $10^5$, inclusive.

**Return value**

- Return the minimum total unused space modulo $10^9+7$, or `-1` when every supplier is infeasible.

### Examples

**Example 1**

- Input: `packages = [2,3,5], boxes = [[4,8],[2,8]]`
- Output: `6`

The first supplier uses sizes `4`, `4`, and `8`, wasting $(4-2)+(4-3)+(8-5)=6$.

**Example 2**

- Input: `packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]`
- Output: `-1`

No supplier offers a box large enough for the size-`5` package.

**Example 3**

- Input: `packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]`
- Output: `9`

The third supplier provides the minimum-waste assignment.

### Required Complexity

- **Time:** $O(N\log N+B\log B+B\log N)$
- **Space:** $O(N+K)$

<details>
<summary>Approach</summary>

#### General

**Assign greedily within one supplier**

Once a supplier is fixed, each package should use that supplier's smallest box that can contain it. Any larger choice only increases waste and cannot help another package because every offered size has unlimited supply. Thus the remaining task is to evaluate this forced optimal assignment efficiently for every feasible supplier.

Sort the packages and each supplier's box sizes. A supplier whose largest box is smaller than the largest package is immediately infeasible. For any other supplier, process box sizes in ascending order. If the previous sizes have already covered the first `packed` packages, binary-search for the first remaining package larger than the current box size. Every package in the newly covered block uses this box size.

**Compare total capacity**

For a block of $c$ packages assigned to size $b$, add $bc$ to the supplier's total box capacity. The package-size sum is identical for every supplier, so minimizing total capacity also minimizes waste. After evaluating all feasible suppliers, subtract the sum of the package sizes once and apply the modulus.

The sorted blocks partition all packages: binary search assigns a package to the first box size that can hold it, which is precisely its smallest adequate size. Therefore each evaluated supplier receives its minimum possible waste, and taking the least such total over all feasible suppliers is globally optimal.

#### Complexity detail

Sorting the $N$ packages costs $O(N\log N)$. If supplier $j$ has $k_j$ sizes, sorting it costs $O(k_j\log k_j)$ and its binary searches cost $O(k_j\log N)$. Since $\sum_j k_j=B$, these totals are bounded by $O(B\log B)$ and $O(B\log N)$. A sorted package copy and one sorted supplier copy require $O(N+K)$ auxiliary space.

#### Alternatives and edge cases

- **Per-package linear box search:** Testing every offered box size for every package is correct but can take $O(NB)$ time.
- **Prefix sums of packages:** Segment waste may be computed directly as box capacity minus a package prefix-sum difference; minimizing capacity first avoids needing those prefix sums.
- **Infeasible supplier:** Its largest box cannot hold the largest package, so it must be skipped entirely.
- **Unlimited supply:** The same box size may serve any number of packages even though each supplier's listed sizes are distinct.
- **Exact fits:** A package assigned to an equal-sized box contributes zero waste.
- **Modulo timing:** Compare full supplier totals before applying the modulus; reducing candidates early could change their ordering.

</details>
