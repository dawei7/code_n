# Subsequence of Size K With the Largest Even Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2098 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/) |

## Problem Description

### Goal

You are given an integer array `nums` and an integer `k`. Among all subsequences containing exactly `k` elements, find the largest possible sum that is even.

A subsequence is formed by deleting any number of elements without changing the relative order of those retained. Because only the sum matters, choosing a set of positions also determines a valid subsequence in their original order. Return the largest even sum, or `-1` when no size-$k$ subsequence has an even sum.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: a list of $n$ integers, where $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.
- `k`: the required subsequence length, where $1 \le k \le n$.

**Return value**

Return the largest even sum obtainable from exactly `k` elements, or `-1` if no such choice exists.

### Examples

**Example 1**

- Input: `nums = [4,1,5,3,1]`, `k = 3`
- Output: `12`
- Explanation: The subsequence `[4,5,3]` has the largest even sum, $4 + 5 + 3 = 12$.

**Example 2**

- Input: `nums = [4,6,2]`, `k = 3`
- Output: `12`
- Explanation: All three values are selected.

**Example 3**

- Input: `nums = [1,3,5]`, `k = 1`
- Output: `-1`
- Explanation: Every possible one-element sum is odd.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Starting from the unconstrained maximum**

Sort the values in descending order and select the first `k`. No other size-$k$ choice has a larger unrestricted sum. If this total is even, it is immediately optimal because adding the parity requirement cannot produce a sum greater than the unrestricted maximum.

**Repairing an odd total with one exchange**

An odd total must change parity. Exchanging two values of the same parity leaves the parity unchanged, so a valid repair must replace one selected value with an unselected value of the opposite parity.

There are only two useful exchange types: remove the smallest selected even and add the largest unselected odd, or remove the smallest selected odd and add the largest unselected even. The sorted order exposes these four boundary candidates. For each feasible type, calculate the repaired sum and keep the larger result.

**Why one boundary exchange is sufficient**

Any even size-$k$ choice differing from the unrestricted top `k` must make enough exchanges to change the total parity. Consider one such choice. Among its exchanges, at least one removed and added pair has opposite parity. Using the smallest selected value of that removed parity and the largest unselected value of the added parity loses no more sum than that pair. This single exchange already produces an even total and is at least as large as a repair involving additional exchanges.

Consequently, the better of the two boundary exchanges is globally optimal. If neither exchange type is available, no size-$k$ selection can change the odd total to even, so return `-1`.

#### Complexity detail

Sorting $n$ values takes $O(n \log n)$ time. The selected and unselected scans take $O(n)$ additional time. The sorted copy or language sorting storage uses $O(n)$ space under the app contract, while the parity candidate records use constant extra space.

#### Alternatives and edge cases

- **Separate parity lists:** Sort even and odd values independently, build prefix sums, and try every feasible even count of selected odd values. This is also $O(n \log n)$ but uses more bookkeeping.
- **Dynamic programming by count and parity:** Tracking the best sum for every selected count and parity takes $O(nk)$ time, which is unnecessary at the maximum constraints.
- **Heap selection:** Maintain the `k` largest values and the needed parity-boundary candidates in $O(n \log k)$ time; this can improve work when `k` is small but is more intricate.
- When `k = n`, there are no unselected replacements; the sum itself must be even.
- Zero is even and may be the best or only parity-changing replacement.
- Duplicate values are separate selectable elements and require no special handling.
- A one-element answer exists exactly when at least one selected candidate can be even.

</details>
