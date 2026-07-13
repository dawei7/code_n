# Maximum Elegance of a K-Length Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2813 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Greedy, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-elegance-of-a-k-length-subsequence](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/).

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

## Solution
### Approach
The problem is solved using a **Greedy approach with a Stack**. First, sort items by profit in descending order. Select the top $k$ items to establish an initial baseline. To potentially increase the elegance, we look for opportunities to swap an item from our current selection (that belongs to a category we already have multiple of) with an item outside our selection that introduces a new category. We maintain a stack of "duplicate" items (items whose category is already represented in our selection) to facilitate these swaps efficiently.

### Complexity Analysis
- **Time Complexity**: $O(n \log n)$ due to the initial sorting of items, where $n$ is the number of items. The subsequent iteration and stack operations take $O(n)$.
- **Space Complexity**: $O(n)$ to store the items, the set of seen categories, and the stack of duplicate items.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(items: list[list[int]], k: int) -> int:
    # Sort items by profit descending
    items.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0
    seen_categories = set()
    duplicates = []

    # Initial selection of top k items
    for i in range(k):
        profit, category = items[i]
        total_profit += profit
        if category in seen_categories:
            duplicates.append(profit)
        else:
            seen_categories.add(category)

    max_elegance = total_profit + len(seen_categories) ** 2

    # Try to swap duplicates for new categories from the remaining items
    for i in range(k, len(items)):
        profit, category = items[i]
        # Only swap if we have a duplicate to remove and the new item is a new category
        if category not in seen_categories and duplicates:
            seen_categories.add(category)
            # Remove the smallest profit duplicate
            total_profit -= duplicates.pop()
            total_profit += profit
            max_elegance = max(max_elegance, total_profit + len(seen_categories) ** 2)

    return max_elegance
```
</details>
