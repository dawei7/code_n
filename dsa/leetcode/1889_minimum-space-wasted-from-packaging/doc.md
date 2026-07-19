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
