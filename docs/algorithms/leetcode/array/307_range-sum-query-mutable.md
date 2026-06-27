# Range Sum Query - Mutable

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `segtree_02` |
| Frontend ID | 307 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Design, Binary Indexed Tree, Segment Tree |
| Official Link | [range-sum-query-mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem Description & Examples
### Goal
Implement a data structure that supports efficient point updates and range sum queries on an array. Given an initial array, we must handle two types of operations: updating the value at a specific index and calculating the sum of elements within a specified range [left, right]. Using a Segment Tree allows both operations to be performed in logarithmic time, making it ideal for dynamic datasets.

### Function Contract
**Inputs**

- `arr`: A list of `n` integers representing the initial state of the array.
- `n`: An integer representing the length of the array.
- `queries`: A list of operations. Each operation is a tuple:
    - `('update', index, val)`: Sets `arr[index]` to `val`.
    - `('sum', left, right)`: Returns the sum of elements from index `left` to `right` inclusive.
- `q`: The number of operations to perform.

**Return value**

- A list containing the results of all 'sum' queries in the order they were requested.

### Examples
1. **Input**: `arr = [1, 3, 5]`, `queries = [('sum', 0, 2), ('update', 1, 2), ('sum', 0, 2)]`
   **Output**: `[9, 8]`
   *Explanation*: Initial sum [0, 2] is 1+3+5=9. After updating index 1 to 2, array becomes [1, 2, 5]. New sum [0, 2] is 1+2+5=8.

2. **Input**: `arr = [10, 20, 30, 40]`, `queries = [('sum', 1, 3), ('update', 0, 5), ('sum', 0, 1)]`
   **Output**: `[90, 25]`
   *Explanation*: Initial sum [1, 3] is 20+30+40=90. After updating index 0 to 5, array becomes [5, 20, 30, 40]. New sum [0, 1] is 5+20=25.

---

## Underlying Base Algorithm(s)
Segment Tree (Binary Tree structure where each node stores the sum of its children's ranges).

---

## Complexity Analysis
- **Time Complexity**: `O(n)` to build the tree, `O(log n)` per update, and `O(log n)` per range sum query.
- **Space Complexity**: `O(n)` to store the segment tree nodes, typically requiring an array of size `4n`.
