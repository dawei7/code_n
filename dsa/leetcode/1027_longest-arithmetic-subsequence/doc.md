# Longest Arithmetic Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1027 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-arithmetic-subsequence/) |

## Problem Description

### Goal

Given an integer array `nums`, return the length of its longest arithmetic subsequence.

A subsequence is formed by deleting zero or more elements without changing the relative order of those that remain in the original input array. A sequence `seq` is arithmetic when every adjacent calculation `seq[i + 1] - seq[i]` has the same fixed value for all valid `i`.

### Function Contract

**Inputs**

- `nums`: an array of $N$ integers, where $2 \le N \le 1000$ and $0 \le \texttt{nums[i]} \le 500$.

**Return value**

- The maximum number of elements in an arithmetic subsequence of `nums`.

### Examples

**Example 1**

- Input: `nums = [3,6,9,12]`
- Output: `4`
- Explanation: The entire array is arithmetic with common difference $3$.

**Example 2**

- Input: `nums = [9,4,7,2,10]`
- Output: `3`
- Explanation: The subsequence `[4,7,10]` has common difference $3$.

**Example 3**

- Input: `nums = [20,1,15,3,10,5,8]`
- Output: `4`
- Explanation: The subsequence `[20,15,10,5]` has common difference $-5$.

### Required Complexity

- **Time:** $O(N^2)$
- **Space:** $O(N^2)$

<details>
<summary>Approach</summary>

#### General

**Identify the state needed to extend a sequence:** Its final index alone is insufficient because arithmetic subsequences ending at the same value may have different common differences. Let `dp[i][difference]` be the longest arithmetic subsequence ending at index `i` with that difference.

**Use every earlier element as a predecessor:** For each pair `j < i`, compute `difference = nums[i] - nums[j]`. If an arithmetic subsequence with this difference already ends at `j`, appending `nums[i]` increases its length by one. Otherwise, the pair `nums[j], nums[i]` starts a length-two subsequence.

Several predecessors can produce the same state. Updating with the larger of its existing and candidate lengths is necessary: a later predecessor is not guaranteed to represent the longest chain. Track the largest state value as the answer.

Every stored length describes a valid subsequence because it is created by appending a later element with the required difference. Conversely, remove the last element from any arithmetic subsequence of length at least two; the remaining prefix is exactly a predecessor state considered by this transition. Thus the DP constructs an optimal state for every possible ending pair.

#### Complexity detail

There are $\binom{N}{2}$ ordered index pairs with `j < i`, and each hash-map lookup and update takes expected $O(1)$ time, giving $O(N^2)$ time. In the worst case, each of the $N$ ending indices stores $O(N)$ differences, so the maps use $O(N^2)$ space.

#### Alternatives and edge cases

- **Bounded-difference table:** Because values lie between $0$ and $500$, differences lie between $-500$ and $500$; fixed-width rows can replace hash maps while retaining $O(N^2)$ time and $O(N)$ space under these fixed source bounds.
- **Choose a starting pair and scan forward:** Greedily extend every pair by its required next value. This is correct but repeats suffix scans and takes $O(N^3)$ time.
- **Duplicate values:** Equal elements form arithmetic subsequences with common difference zero.
- **Negative difference:** A valid subsequence may decrease; differences must not be restricted to nonnegative values.
- **Minimum length:** Any two input elements form an arithmetic subsequence of length two.

</details>
