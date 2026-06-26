# Put Marbles in Bags

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2551 |
| Difficulty | Hard |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [put-marbles-in-bags](https://leetcode.com/problems/put-marbles-in-bags/) |

## Problem Description & Examples
### Goal
Given a sequence of marbles with specific weights, you must partition them into exactly `k` non-empty contiguous sub-segments. The cost of a partition is defined as the sum of the weights of the first and last marble in each of the `k` segments. Your objective is to calculate the difference between the maximum possible cost and the minimum possible cost achievable across all valid partitions.

### Function Contract
**Inputs**

- `weights`: A list of integers representing the weight of each marble in order.
- `k`: An integer representing the number of segments to partition the marbles into.

**Return value**

- An integer representing the difference between the maximum and minimum partition costs.

### Examples
**Example 1**

- Input: `weights = [1, 3, 5, 1], k = 2`
- Output: `4`
- Explanation: Possible partitions: ([1], [3, 5, 1]) cost 1+1 + 3+1 = 6; ([1, 3], [5, 1]) cost 1+3 + 5+1 = 10; ([1, 3, 5], [1]) cost 1+5 + 1+1 = 8. Max 10 - Min 6 = 4.

**Example 2**

- Input: `weights = [1, 3], k = 2`
- Output: `0`
- Explanation: Only one partition ([1], [3]) is possible. Max 4 - Min 4 = 0.

**Example 3**

- Input: `weights = [1, 1, 1], k = 3`
- Output: `0`
- Explanation: Only one partition ([1], [1], [1]) is possible. Max 4 - Min 4 = 0.

---

## Underlying Base Algorithm(s)
The problem can be reduced to a greedy selection strategy. When partitioning an array into `k` segments, we effectively choose `k-1` "cut points" between adjacent elements. If we choose a cut between `weights[i]` and `weights[i+1]`, the sum `weights[i] + weights[i+1]` is added to the total cost. Since the first and last elements of the entire array are always included in the cost regardless of the cuts, the problem simplifies to selecting the `k-1` largest and `k-1` smallest values from the set of adjacent sums `{weights[i] + weights[i+1]}`.

---

## Complexity Analysis
- **Time Complexity**: `O(N log N)`, where `N` is the number of marbles, due to the sorting of the adjacent sums.
- **Space Complexity**: `O(N)` to store the array of adjacent sums.
