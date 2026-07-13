# Sum of Matrix After Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2718 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [sum-of-matrix-after-queries](https://leetcode.com/problems/sum-of-matrix-after-queries/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/sum-of-matrix-after-queries/).

### Goal
Given an integer $n$ representing the dimensions of an $n \times n$ matrix (initially filled with zeros) and a 2D array of queries, calculate the sum of all elements in the matrix after executing all queries in the given order.

Each query is represented as a triplet `[type, index, val]`:
- If `type == 0`, set all elements in row `index` to `val`.
- If `type == 1`, set all elements in column `index` to `val`.

### Function Contract
**Inputs**

- `n` (`int`): The size of the $n \times n$ matrix.
- `queries` (`list[list[int]]`): A list of queries where each query is of the form `[type, index, val]`.

**Return value**

- `int`: The sum of all elements in the matrix after applying all queries.

### Examples
**Example 1**

- Input: `n = 3`, `queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]`
- Output: `23`
- Explanation:
  - Initially, the matrix is all 0s.
  - Apply row 0 = 1: Row 0 becomes `[1, 1, 1]`.
  - Apply col 2 = 2: Col 2 becomes `[2, 2, 2]`. Matrix is now `[[1, 1, 2], [0, 0, 2], [0, 0, 2]]`.
  - Apply row 2 = 3: Row 2 becomes `[3, 3, 3]`. Matrix is now `[[1, 1, 2], [0, 0, 2], [3, 3, 3]]`.
  - Apply col 0 = 4: Col 0 becomes `[4, 4, 4]`. Matrix is now `[[4, 1, 2], [4, 0, 2], [4, 3, 3]]`.
  - The sum of the matrix elements is `4 + 1 + 2 + 4 + 0 + 2 + 4 + 3 + 3 = 23`.

**Example 2**

- Input: `n = 3`, `queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]`
- Output: `17`
- Explanation:
  - After applying all queries, the final matrix state yields a sum of `17`.

**Example 3**

- Input: `n = 4`, `queries = [[0,1,2],[1,2,3]]`
- Output: `18`
- Explanation:
  - Row 1 is set to 2 (sum contribution: $4 \times 2 = 8$).
  - Column 2 is set to 3. This overwrites the cell at $(1, 2)$ with 3.
  - The final sum is $2 \times 3$ (remaining elements in row 1) + $3 \times 4$ (elements in column 2) = $6 + 12 = 18$.

---

## Solution
### Approach
The naive approach of simulating the matrix updates takes $O(q \times n)$ time, which is too slow for large inputs.

Instead, we can use **Backward Processing (Reverse Iteration)**. Since later queries overwrite earlier ones, the final value of any cell is determined by the *last* query that affected it. By iterating through the queries in reverse order (from last to first):
1. We keep track of which rows and columns have already been updated using hash sets or boolean arrays.
2. If we encounter a row query for a row that hasn't been updated yet:
   - It will successfully set the values of all cells in this row except for those columns that have already been updated by subsequent column queries.
   - The number of affected cells is $n - \text{count of unique columns already updated}$.
   - We add `val * (n - len(visited_cols))` to our total sum and mark this row as visited.
3. If we encounter a column query for a column that hasn't been updated yet:
   - It will successfully set the values of all cells in this column except for those rows that have already been updated by subsequent row queries.
   - The number of affected cells is $n - \text{count of unique rows already updated}$.
   - We add `val * (n - len(visited_rows))` to our total sum and mark this column as visited.
4. **Early Exit**: If all $n$ rows or all $n$ columns have been updated, any further queries will have zero impact on the final sum, allowing us to terminate early.

### Complexity Analysis
- **Time Complexity**: $O(q)$ where $q$ is the number of queries. We iterate through the queries list at most once. Set lookups and insertions take $O(1)$ average time.
- **Space Complexity**: $O(n)$ to store the visited rows and columns in hash sets.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, queries: list[list[int]]) -> int:
    visited_rows = set()
    visited_cols = set()
    total_sum = 0

    # Process queries in reverse order
    for type_i, index_i, val_i in reversed(queries):
        if type_i == 0:  # Row query
            if index_i not in visited_rows:
                visited_rows.add(index_i)
                total_sum += val_i * (n - len(visited_cols))
        else:  # Column query
            if index_i not in visited_cols:
                visited_cols.add(index_i)
                total_sum += val_i * (n - len(visited_rows))

        # Early exit if all rows or all columns are fully covered
        if len(visited_rows) == n or len(visited_cols) == n:
            break

    return total_sum
```
</details>
