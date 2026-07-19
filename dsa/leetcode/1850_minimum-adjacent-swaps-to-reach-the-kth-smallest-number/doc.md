# Minimum Adjacent Swaps to Reach the Kth Smallest Number

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number/) |
| Frontend ID | 1850 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A digit string `num` represents a large integer. A wonderful integer uses exactly the same multiset of digits as `num` and has a greater numerical value. Order all wonderful integers by value, counting distinct digit arrangements in their ordinary lexicographic/numeric order.

The requested target is the $k$th smallest wonderful integer; the input guarantees that it exists. One operation swaps two adjacent digits in the current string. Return the minimum number of such swaps needed to transform `num` into that target arrangement.

### Function Contract

**Inputs**

- `num`: a digit string with $2 \le \lvert\texttt{num}\rvert \le 1000$.
- `k`: an integer with $1 \le k \le 1000$.
- The $k$th lexicographically larger distinct permutation of `num` is guaranteed to exist.
- Let $n=\lvert\texttt{num}\rvert$.

**Return value**

- Return the minimum number of swaps of neighboring positions required to change `num` into its $k$th next distinct digit permutation.

### Examples

**Example 1**

- Input: `num = "5489355142"`, `k = 4`
- Output: `2`

The fourth wonderful integer is `"5489355421"`, reachable with two adjacent swaps.

**Example 2**

- Input: `num = "11112"`, `k = 4`
- Output: `4`

The target is `"21111"`; the digit `2` must move four positions left.

**Example 3**

- Input: `num = "00123"`, `k = 1`
- Output: `1`

The next permutation is `"00132"`.
