# Take Gifts From the Richest Pile

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2558 |
| Difficulty | Easy |
| Topics | Array, Heap (Priority Queue), Simulation |
| Official Link | [take-gifts-from-the-richest-pile](https://leetcode.com/problems/take-gifts-from-the-richest-pile/) |

## Problem Description & Examples
### Goal
Given an array of integers representing piles of gifts and an integer representing the number of seconds, simulate a process where in each second, you select the pile with the largest number of gifts, replace it with the integer square root of its current value (rounded down), and repeat this for the specified duration. The goal is to return the total number of gifts remaining after all seconds have elapsed.

### Function Contract
**Inputs**

- `gifts`: A list of integers where each element represents the number of gifts in a pile.
- `k`: An integer representing the number of seconds (operations) to perform.

**Return value**

- An integer representing the sum of all gifts remaining in the piles after `k` operations.

### Examples
**Example 1**

- Input: `gifts = [25, 64, 9, 4, 100], k = 4`
- Output: `29`
- Explanation: After 4 operations, the piles become [5, 8, 9, 4, 10], summing to 29.

**Example 2**

- Input: `gifts = [1, 1, 1, 1], k = 4`
- Output: `4`
- Explanation: The square root of 1 is 1, so the piles remain unchanged.

**Example 3**

- Input: `gifts = [10], k = 1`
- Output: `3`
- Explanation: The pile of 10 becomes 3 (floor of sqrt(10)).

---

## Underlying Base Algorithm(s)
The problem is best solved using a **Max-Heap** (Priority Queue). Since we repeatedly need to extract the maximum element and re-insert a modified value, a max-heap allows for $O(\log n)$ extraction and insertion. In Python, we use `heapq` with negated values to simulate a max-heap.

---

## Complexity Analysis
- **Time Complexity**: $O(n + k \log n)$, where $n$ is the number of piles. Building the heap takes $O(n)$, and performing $k$ operations, each involving a heap pop and push, takes $O(k \log n)$.
- **Space Complexity**: $O(n)$ to store the heap of gift piles.
