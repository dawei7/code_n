# Query Kth Smallest Trimmed Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2343 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Radix Sort, Quickselect |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [query-kth-smallest-trimmed-number](https://leetcode.com/problems/query-kth-smallest-trimmed-number/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/query-kth-smallest-trimmed-number/).

### Goal
Given a list of numbers, represented as strings, and a list of queries, determine for each query the original 0-indexed position of the k-th smallest number after trimming each number to its rightmost `trim` digits. The numbers in the input list all have the same length.

### Function Contract
**Inputs**

- `nums`: A list of strings, where each string `nums[i]` represents a non-negative integer. All strings in `nums` have the same length.
- `queries`: A list of lists, where each inner list `[k, trim]` represents a single query. `k` is a 1-indexed integer indicating the desired rank (e.g., 1 for the smallest, 2 for the second smallest), and `trim` is an integer indicating the number of rightmost digits to consider for trimming.

**Return value**

A list of integers. The `j`-th element of this list should be the original 0-indexed position of the k-th smallest trimmed number corresponding to `queries[j]`.

### Examples
**Example 1**

- Input: `nums = ["102", "473", "251", "814"]`, `queries = [[1, 1], [2, 3], [4, 2]]`
- Output: `[2, 2, 1]`
- Explanation:
    - For `[1, 1]`: Trim to 1 digit. Numbers become `[2, 3, 1, 4]`. Sorted: `[1, 2, 3, 4]`. The 1st smallest is `1` (from original index `2`).
    - For `[2, 3]`: Trim to 3 digits. Numbers become `[102, 473, 251, 814]`. Sorted: `[102, 251, 473, 814]`. The 2nd smallest is `251` (from original index `2`).
    - For `[4, 2]`: Trim to 2 digits. Numbers become `[02, 73, 51, 14]`. Sorted: `[02, 14, 51, 73]`. The 4th smallest is `73` (from original index `1`).

**Example 2**

- Input: `nums = ["001", "010", "001", "100"]`, `queries = [[1, 3], [2, 2]]`
- Output: `[0, 0]`
- Explanation:
    - For `[1, 3]`: Trim to 3 digits. Numbers become `[1, 10, 1, 100]`. Pairs `(value, original_index)`: `[(1,0), (10,1), (1,2), (100,3)]`. Sorted: `[(1,0), (1,2), (10,1), (100,3)]`. The 1st smallest is `1` (from original index `0`).
    - For `[2, 2]`: Trim to 2 digits. Numbers become `[01, 10, 01, 00]`. Pairs `(value, original_index)`: `[(1,0), (10,1), (1,2), (0,3)]`. Sorted: `[(0,3), (1,0), (1,2), (10,1)]`. The 2nd smallest is `1` (from original index `0`).

---

## Solution
### Approach
The core approach involves processing each query independently. For a given query `[k, trim]`:
1.  **Trimming and Pairing**: Iterate through the `nums` list. For each number string `num_str` at original index `i`, extract its rightmost `trim` digits using string slicing (`num_str[-trim:]`). Convert this substring into an integer. Store this trimmed integer along with its original index `i` as a pair `(trimmed_value, original_index)`.
2.  **Sorting**: Collect all such `(trimmed_value, original_index)` pairs into a temporary list. Sort this list. Python's default tuple sorting will sort primarily by `trimmed_value` and then by `original_index` for tie-breaking (which ensures stability and consistent results, though the problem typically allows any valid index in case of ties).
3.  **Selection**: After sorting, the `k`-th smallest trimmed number (1-indexed `k`) will be at index `k-1` in the sorted list. Retrieve the `original_index` from this `(k-1)`-th pair.

This process is repeated for every query.

### Complexity Analysis
Let `N` be the number of elements in `nums`, `Q` be the number of queries, and `L` be the maximum length of a number string in `nums`.

- **Time Complexity**: `O(Q * (N * L + N * L * log N))`
    - For each of the `Q` queries:
        - **Trimming and Pairing**: Iterating through `N` numbers. For each number, string slicing `num_str[-trim:]` takes `O(trim)` time, and converting the `trim`-length string to an integer `int()` also takes `O(trim)` time. Since `trim <= L`, this step is `O(N * L)`.
        - **Sorting**: We sort `N` pairs. Python's Timsort algorithm takes `O(N log N)` comparisons. However, comparing two large integers (which can have up to `L` digits) takes `O(L)` time. Therefore, the sorting step effectively takes `O(N * L * log N)`.
    - Combining these, each query takes `O(N * L + N * L * log N)`, which simplifies to `O(N * L * log N)` as `N * L * log N` dominates `N * L`.
    - Total time complexity for `Q` queries is `Q` times this, resulting in `O(Q * N * L * log N)`.
    - Given constraints `N, Q, L <= 100`, this is roughly `100 * 100 * 100 * log(100)` which is `10^6 * ~7 = 7 * 10^6` operations, well within typical time limits.

- **Space Complexity**: `O(N * L + Q)`
    - For each query, a temporary list `trimmed_data` is created to store `N` pairs. Each pair consists of an integer (which can be up to `L` digits long, requiring `O(L)` space in Python for large integers) and an integer index (`O(1)` space). Thus, this temporary list requires `O(N * L)` space.
    - The `results` list stores `Q` integers, requiring `O(Q)` space.
    - The total space complexity is `O(N * L + Q)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[str], queries: list[list[int]]) -> list[int]:
    """
    For each query [k, trim], finds the k-th smallest number after trimming
    each original number to its rightmost 'trim' digits, and returns its
    original 0-indexed position.
    """
    results = []

    for k, trim in queries:
        # Step 1: Trim numbers and store with original indices
        # We store (trimmed_value, original_index) pairs.
        # Python's int() handles leading zeros correctly (e.g., int("007") == 7).
        # Slicing num_str[-trim:] gets the rightmost 'trim' digits.
        trimmed_data = []
        for i, num_str in enumerate(nums):
            trimmed_val_str = num_str[-trim:]
            trimmed_val_int = int(trimmed_val_str)
            trimmed_data.append((trimmed_val_int, i))

        # Step 2: Sort the trimmed data.
        # Python's default sort for tuples sorts by the first element,
        # then by the second element (original_index) if the first elements are equal.
        # This provides a stable sort, which is generally good practice.
        trimmed_data.sort()

        # Step 3: Retrieve the original index of the k-th smallest.
        # k is 1-indexed, so we access the (k-1)-th element in the 0-indexed list.
        kth_smallest_original_index = trimmed_data[k - 1][1]
        results.append(kth_smallest_original_index)

    return results
```
</details>
