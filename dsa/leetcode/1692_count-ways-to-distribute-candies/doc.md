# Count Ways to Distribute Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1692 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-ways-to-distribute-candies/) |

## Problem Description
### Goal

There are $n$ distinct candies, identified from 1 through $n$, and $k$ bags. Distribute every candy so that each bag receives at least one. The order of candies within a bag is irrelevant, and the bags themselves have no labels: rearranging the bags does not create a different distribution.

Two distributions differ when some pair of candies appears together in one distribution but belongs to separate bags in the other. Equivalently, count the partitions of the $n$ distinct candies into exactly $k$ nonempty groups. Return the number of such distributions modulo $10^9+7$.

### Function Contract
**Inputs**

- `n`: the number of distinct candies
- `k`: the exact number of nonempty, unlabeled bags, with $1 \le k \le n \le 1000$

**Return value**

The number of distinct valid distributions, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `n = 3, k = 2`
- Output: `3`

The three partitions are one singleton paired with the complementary two-candy group.

**Example 2**

- Input: `n = 4, k = 2`
- Output: `7`

There are four singleton-plus-triple partitions and three partitions into two pairs.

**Example 3**

- Input: `n = 20, k = 5`
- Output: `206085257`

The exact count is 1,881,780,996, whose remainder modulo $10^9+7$ is 206,085,257.
