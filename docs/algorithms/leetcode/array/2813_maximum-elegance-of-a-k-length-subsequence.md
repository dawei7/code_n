# Maximum Elegance of a K-Length Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2813 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Stack, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [maximum-elegance-of-a-k-length-subsequence](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/) |

## Problem Description & Examples
### Goal
Given a list of items, each having a profit value and a category, select exactly $k$ items to maximize the "elegance" of the subsequence. Elegance is defined as the sum of the profits of the selected items plus the square of the number of distinct categories represented in the selection.

### Function Contract
**Inputs**

- `items`: A list of lists, where each inner list `[profit, category]` represents an item.
- `k`: An integer representing the number of items to select.

**Return value**

- An integer representing the maximum possible elegance score.

### Examples
**Example 1**

- Input: `items = [[3,2],[5,1],[10,1]], k = 2`
- Output: `17`
- Explanation: Select items [10, 1] and [3, 2]. Profit = 13, distinct categories = 2. Elegance = 13 + 2^2 = 17.

**Example 2**

- Input: `items = [[3,1],[3,1],[2,2],[5,3]], k = 3`
- Output: `19`
- Explanation: Select [5, 3], [2, 2], and [3, 1]. Profit = 10, distinct categories = 3. Elegance = 10 + 3^2 = 19.

**Example 3**

- Input: `items = [[1,1],[2,1],[3,1]], k = 3`
- Output: `7`
- Explanation: Select all items. Profit = 6, distinct categories = 1. Elegance = 6 + 1^2 = 7.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach with a Stack**. First, sort items by profit in descending order. Select the top $k$ items to establish an initial baseline. To potentially increase the elegance, we look for opportunities to swap an item from our current selection (that belongs to a category we already have multiple of) with an item outside our selection that introduces a new category. We maintain a stack of "duplicate" items (items whose category is already represented in our selection) to facilitate these swaps efficiently.

---

## Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the initial sorting of items, where $n$ is the number of items. The subsequent iteration and stack operations take $O(n)$.
- **Space Complexity**: $O(n)$ to store the items, the set of seen categories, and the stack of duplicate items.
