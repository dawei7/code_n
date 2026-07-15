# Previous Permutation With One Swap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1053 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/previous-permutation-with-one-swap/) |

## Problem Description

### Goal

Given an array `arr` of positive integers that are not necessarily distinct, exchange the values at exactly two positions to create a permutation that is lexicographically smaller than `arr`.

Among all smaller arrays obtainable by one swap, return the lexicographically largest one. Lexicographic order is determined by the values at the first position where two arrays differ. If no swap can produce a strictly smaller array, return `arr` unchanged.

### Function Contract

**Inputs**

- `arr`: an array of length $N$, where $1 \le N \le 10^4$ and $1 \le \texttt{arr[i]} \le 10^4$.

**Return value**

- The lexicographically largest array strictly smaller than the input that can be obtained with one swap, or the unchanged array if none exists.

### Examples

**Example 1**

- Input: `arr = [3,2,1]`
- Output: `[3,1,2]`
- Explanation: Swap `2` and `1`.

**Example 2**

- Input: `arr = [1,1,5]`
- Output: `[1,1,5]`
- Explanation: No swap produces a smaller permutation.

**Example 3**

- Input: `arr = [1,9,4,6,7]`
- Output: `[1,7,4,6,9]`
- Explanation: Swap `9` and `7`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Change the latest possible position:** Scan from right to left for the first index `pivot` satisfying `arr[pivot] > arr[pivot + 1]`. Everything to its right is non-decreasing. If no such descent exists, the array is already the smallest ordering of its multiset and no smaller one-swap result exists.

**Choose the closest smaller value:** To keep the result as large as possible after lowering `arr[pivot]`, select the greatest suffix value strictly smaller than it. Scanning from the right skips values greater than or equal to the pivot and stops at that greatest smaller value because the suffix is non-decreasing.

**Use the leftmost equal occurrence:** If the chosen suffix value occurs more than once, move left to its first occurrence before swapping. Swapping with a later equal copy would place the larger pivot earlier within the suffix and create a lexicographically smaller result. The leftmost copy therefore maximizes the suffix after the earliest changed position.

Any smaller result must first differ at some index where a larger value is swapped with a smaller later value. Choosing the rightmost feasible pivot preserves the longest possible prefix. At that pivot, choosing the largest smaller value maximizes the first changed entry, and the duplicate rule maximizes what follows. These lexicographic priorities prove the greedy swap is optimal.

#### Complexity detail

The pivot search, suffix candidate search, and duplicate adjustment each move only leftward across the array, taking $O(N)$ total time. The swap uses constant auxiliary storage, so space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate every swap:** Generate all $O(N^2)$ swapped arrays and retain the best smaller one. It is correct but quadratic even before array-copy or comparison costs.
- **Sort the suffix:** A full previous-permutation routine may reorder many positions, which violates the exactly-one-swap restriction.
- **Balanced value index:** Track suffix values in an ordered structure to query a predecessor, but the monotone suffix makes this unnecessary.
- **Already non-decreasing:** No smaller one-swap permutation exists.
- **Single element:** There are not two positions to exchange, so return it unchanged.
- **Duplicate target values:** Swap with the leftmost occurrence of the chosen suffix value.
- **Strictly smaller requirement:** Swapping equal values does not qualify as a smaller permutation.
- **Descending input:** The rightmost adjacent pair forms the optimal pivot and target.

</details>
