# Number of Adjacent Elements With the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2672 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-adjacent-elements-with-the-same-color](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/).

### Goal
You are given an integer `n` representing the number of elements in a 0-indexed array, initially uncolored (represented by color 0). You are also given a 2D integer array `queries`, where each `queries[i] = [index, color]` indicates that the element at `index` should be updated to `color`. After each query, you must determine and return the total number of adjacent pairs of elements that have the same *positive* color. An adjacent pair `(nums[j], nums[j+1])` contributes to the count if `nums[j] == nums[j+1]` and `nums[j]` is a positive color (i.e., not 0).

### Function Contract
**Inputs**

- `n`: An integer representing the number of elements in the array. `1 <= n <= 10^5`.
- `queries`: A list of lists of integers, where each inner list `[index, color]` represents a query. `1 <= len(queries) <= 10^5`. `0 <= index < n`. `1 <= color <= 10^5`.

**Return value**

- `List[int]`: A list of integers, where `ans[i]` is the number of adjacent pairs with the same positive color after the `i`-th query.

### Examples
**Example 1**

- Input: `n = 4`, `queries = [[0, 2], [1, 2], [3, 1], [1, 1]]`
- Output: `[0, 1, 1, 0]`
- Explanation:
    - Initially, `colors = [0, 0, 0, 0]`, adjacent pairs = 0.
    - Query 1: `[0, 2]`. `colors = [2, 0, 0, 0]`. Adjacent pairs = 0.
    - Query 2: `[1, 2]`. `colors = [2, 2, 0, 0]`. Adjacent pairs = 1 (`(colors[0], colors[1])`).
    - Query 3: `[3, 1]`. `colors = [2, 2, 0, 1]`. Adjacent pairs = 1 (`(colors[0], colors[1])`).
    - Query 4: `[1, 1]`. `colors = [2, 1, 0, 1]`. The pair `(colors[0], colors[1])` is no longer same-colored. Adjacent pairs = 0.

**Example 2**

- Input: `n = 1`, `queries = [[0, 1], [0, 2]]`
- Output: `[0, 0]`
- Explanation:
    - Initially, `colors = [0]`, adjacent pairs = 0.
    - Query 1: `[0, 1]`. `colors = [1]`. No adjacent pairs possible for `n=1`. Adjacent pairs = 0.
    - Query 2: `[0, 2]`. `colors = [2]`. No adjacent pairs possible for `n=1`. Adjacent pairs = 0.

**Example 3**

- Input: `n = 5`, `queries = [[0, 1], [1, 1], [2, 1], [3, 2], [4, 2], [2, 2]]`
- Output: `[0, 1, 2, 2, 3, 3]`
- Explanation:
    - Initial: `[0,0,0,0,0]`, count = 0
    - `[0,1]`: `[1,0,0,0,0]`, count = 0
    - `[1,1]`: `[1,1,0,0,0]`, count = 1 (pair `(0,1)`)
    - `[2,1]`: `[1,1,1,0,0]`, count = 2 (pairs `(0,1)`, `(1,2)`)
    - `[3,2]`: `[1,1,1,2,0]`, count = 2
    - `[4,2]`: `[1,1,1,2,2]`, count = 3 (pairs `(0,1)`, `(1,2)`, `(3,4)`)
    - `[2,2]`: `[1,1,2,2,2]`. `colors[1]` was `1`, now `colors[2]` is `2`, so `(1,2)` is no longer a pair. `colors[3]` was `2`, now `colors[2]` is `2`, so `(2,3)` becomes a pair. Net change: `(1,2)` removed, `(2,3)` added. Count remains 3.

---

## Solution
### Approach
The problem can be solved using a direct simulation approach. We maintain the current state of the array of colors and a running count of adjacent same-colored pairs. For each query, an element's color is updated. This update only affects the adjacency status of the element with its immediate left and right neighbors.

The core idea is to:
1.  Initialize an array `colors` of size `n` with all elements set to 0 (uncolored).
2.  Maintain a variable `current_adjacent_pairs` to store the total count.
3.  For each query `[index, new_color]`:
    a.  Record the `old_color` at `colors[index]`.
    b.  Before updating `colors[index]`, check its left neighbor (`index - 1`) and right neighbor (`index + 1`). If `colors[index]` formed a same-colored pair with either neighbor (and `old_color` was not 0), decrement `current_adjacent_pairs`.
    c.  Update `colors[index]` to `new_color`.
    d.  After updating, re-check its left neighbor (`index - 1`) and right neighbor (`index + 1`). If `colors[index]` now forms a same-colored pair with either neighbor (and `new_color` is not 0), increment `current_adjacent_pairs`.
    e.  Store the `current_adjacent_pairs` count in the results list.
4.  Handle boundary conditions carefully for `index = 0` (no left neighbor) and `index = n - 1` (no right neighbor).

This approach avoids re-scanning the entire array after each query, making each query an O(1) operation.

### Complexity Analysis
- **Time Complexity**: `O(N + Q)`
    - Initializing the `colors` array takes `O(N)` time.
    - There are `Q` queries. Each query involves a constant number of array accesses, comparisons, and arithmetic operations (checking up to two neighbors, updating one element, and updating the count). Thus, each query takes `O(1)` time.
    - The total time complexity is `O(N + Q)`.
- **Space Complexity**: `O(N + Q)`
    - An array `colors` of size `N` is used to store the current state of element colors, contributing `O(N)` space.
    - A list `results` of size `Q` is used to store the answer for each query, contributing `O(Q)` space.
    - The total space complexity is `O(N + Q)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, queries: list[list[int]]) -> list[int]:
    # Initialize the array with 0s, representing uncolored elements.
    colors = [0] * n

    # Initialize the count of adjacent pairs with the same positive color.
    current_adjacent_pairs = 0

    # List to store the result after each query.
    results = []

    # Process each query
    for index, new_color in queries:
        old_color = colors[index]

        # Step 1: Decrement count for adjacencies involving the old_color at 'index'.
        # We only decrement if the old_color was positive (not 0) and formed a pair.

        # Check left neighbor (index - 1)
        if index > 0:
            # If the left neighbor had the same old_color (and old_color was positive),
            # this pair is about to be broken.
            if colors[index - 1] == old_color and old_color != 0:
                current_adjacent_pairs -= 1

        # Check right neighbor (index + 1)
        if index < n - 1:
            # If the right neighbor had the same old_color (and old_color was positive),
            # this pair is about to be broken.
            if colors[index + 1] == old_color and old_color != 0:
                current_adjacent_pairs -= 1

        # Step 2: Update the color of the element at 'index'.
        colors[index] = new_color

        # Step 3: Increment count for adjacencies involving the new_color at 'index'.
        # We only increment if the new_color is positive (not 0) and forms a new pair.

        # Check left neighbor (index - 1)
        if index > 0:
            # If the left neighbor now has the same new_color (and new_color is positive),
            # a new pair is formed.
            if colors[index - 1] == new_color and new_color != 0:
                current_adjacent_pairs += 1

        # Check right neighbor (index + 1)
        if index < n - 1:
            # If the right neighbor now has the same new_color (and new_color is positive),
            # a new pair is formed.
            if colors[index + 1] == new_color and new_color != 0:
                current_adjacent_pairs += 1

        # Add the current count of adjacent pairs to the results list.
        results.append(current_adjacent_pairs)

    return results
```
</details>
