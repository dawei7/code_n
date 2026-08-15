# Maximum Product of Subsequences With an Alternating Sum Equal to K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3509 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/) |

## Problem Description

### Goal

Choose a non-empty subsequence of `nums`, preserving the selected elements' original order. For a selected sequence $a_0,a_1,\ldots,a_{m-1}$, its alternating sum is

$$
a_0-a_1+a_2-a_3+\cdots.
$$

The alternating sum must equal `k`. Among all such subsequences whose ordinary product does not exceed `limit`, return the largest product. The product is compared and returned as its actual integer value; it is not reduced modulo another number.

If no non-empty subsequence satisfies both the alternating-sum and product requirements, return `-1`. Zero-valued elements are significant: a subsequence may have product zero even when an earlier partial product would have exceeded `limit`.

### Function Contract

**Inputs**

- `nums`: A list of nonnegative integers from which a subsequence is selected.
- `k`: The exact target for the subsequence's even-position sum minus its odd-position sum.
- `limit`: The inclusive upper bound on the selected elements' product.

Let $n=\lvert\texttt{nums}\rvert$, $S=\sum_i \texttt{nums[i]}$, and $L=\texttt{limit}$. The constraints are $1 \le n \le 150$, $0 \le \texttt{nums[i]} \le 12$, $-10^5 \le k \le 10^5$, and $1 \le L \le 5000$. In particular, $S \le 1800$.

**Return value**

Return the maximum product at most `limit` among non-empty subsequences with alternating sum `k`, or `-1` when none exists.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3], k = 2, limit = 10`
- **Output:** `6`
- **Explanation:** `[1,2,3]` has alternating sum `1 - 2 + 3 = 2` and product `6`, which beats the product of the single-element subsequence `[2]`.

#### Example 2

- **Input:** `nums = [0,2,3], k = -5, limit = 12`
- **Output:** `-1`
- **Explanation:** No non-empty subsequence has alternating sum `-5`.

#### Example 3

- **Input:** `nums = [2,2,3,3], k = 0, limit = 9`
- **Output:** `9`
- **Explanation:** `[3,3]` has alternating sum zero and product `9`. The four-element choice has product `36`, which exceeds the limit.
