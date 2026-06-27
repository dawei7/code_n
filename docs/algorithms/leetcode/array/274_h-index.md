# H-Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 274 |
| Difficulty | Medium |
| Topics | Array, Sorting, Counting Sort |
| Official Link | [h-index](https://leetcode.com/problems/h-index/) |

## Problem Description & Examples
### Goal
Given an array of integers `citations` where each element represents the number of citations a researcher received for a particular paper, calculate the researcher's h-index. 

The h-index is defined as the maximum value $h$ such that the researcher has published at least $h$ papers that have each been cited at least $h$ times. The remaining papers must have no more than $h$ citations each.

### Function Contract
**Inputs**

- `citations`: `List[int]` - An array of non-negative integers representing citation counts.

**Return value**

- `int` - The calculated h-index of the researcher.

### Examples
**Example 1**

- Input: `citations = [3, 0, 6, 1, 5]`
- Output: `3`
- Explanation: The researcher has 5 papers in total. The citation counts are 3, 0, 6, 1, 5. There are 3 papers with at least 3 citations (specifically, 3, 5, and 6 citations), and the remaining 2 papers have at most 3 citations. Thus, the h-index is 3.

**Example 2**

- Input: `citations = [1, 3, 1]`
- Output: `1`
- Explanation: There is 1 paper with at least 1 citation, and the remaining papers have at most 1 citation.

**Example 3**

- Input: `citations = [10, 8, 5, 4, 3]`
- Output: `4`
- Explanation: There are 4 papers with at least 4 citations (10, 8, 5, and 4). The remaining paper has 3 citations.

---

## Underlying Base Algorithm(s)
The problem can be solved in $O(n \log n)$ time by sorting the array in descending order and finding the first index where the citation count is less than the paper's rank. 

However, we can achieve an optimal $O(n)$ time complexity using **Counting Sort / Bucket Sort**. 
Since a researcher with $n$ papers cannot have an h-index greater than $n$, any citation count larger than $n$ can be treated as exactly $n$. 

1. Create a bucket array of size $n + 1$ to record the frequency of papers with each citation count.
2. For any paper with $c$ citations:
   - If $c \ge n$, increment the bucket at index $n$.
   - Otherwise, increment the bucket at index $c$.
3. Iterate backward from $n$ down to $0$, keeping a running sum of the number of papers. The first index $i$ where the running sum of papers is greater than or equal to $i$ is the h-index.

---

## Complexity Analysis
- **Time Complexity**: $\mathcal{O}(n)$ where $n$ is the number of papers. We perform a single pass to populate the buckets and a single backward pass to find the h-index.
- **Space Complexity**: $\mathcal{O}(n)$ to store the bucket array of size $n + 1$.
