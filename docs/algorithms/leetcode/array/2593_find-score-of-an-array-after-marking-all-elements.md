# Find Score of an Array After Marking All Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2593 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue), Simulation |
| Official Link | [find-score-of-an-array-after-marking-all-elements](https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/) |

## Problem Description & Examples
### Goal
The objective is to calculate a total score by iteratively selecting the smallest available number in an array. When a number is selected, it is added to the score, and that number along with its immediate left and right neighbors are "marked" (rendered unavailable for future selection). This process continues until all elements in the array are marked.

### Function Contract
**Inputs**

- `nums`: A list of positive integers (`List[int]`).

**Return value**

- `score`: A 64-bit integer representing the total sum of the selected elements.

### Examples
**Example 1**

- Input: `nums = [2, 1, 3, 4, 5, 2]`
- Output: `7`
- Explanation: Select 1 (index 1), mark indices 0, 1, 2. Remaining: [4, 5, 2]. Select 2 (index 5), mark indices 4, 5. Remaining: [4]. Select 4 (index 3), mark index 3. Total: 1 + 2 + 4 = 7.

**Example 2**

- Input: `nums = [2, 3, 5, 1, 3, 2]`
- Output: `5`
- Explanation: Select 1 (index 3), mark indices 2, 3, 4. Remaining: [2, 3, 2]. Select 2 (index 0), mark indices 0, 1. Remaining: [2]. Select 2 (index 5), mark index 5. Total: 1 + 2 + 2 = 5.

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy Strategy** combined with **Sorting** or a **Min-Heap**. By sorting the elements based on their values (and indices for tie-breaking), we ensure that we always process the smallest available element first. A boolean array is used to track the "marked" status of each index to ensure $O(1)$ lookup time during the simulation.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the length of the array. This is dominated by the sorting step. The subsequent linear scan through the sorted elements takes $O(N)$.
- **Space Complexity**: $O(N)$ to store the indexed elements and the boolean array tracking marked indices.
