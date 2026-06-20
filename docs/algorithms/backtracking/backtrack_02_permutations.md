# Permutations

| | |
|---|---|
| **ID** | `backtrack_02` |
| **Category** | backtracking |
| **Complexity (required)** | $O(N * N!)$ Time, $O(N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Permutations](https://leetcode.com/problems/permutations/) |

## Problem statement

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.
A permutation is a rearrangement of all the elements into a specific sequential order.

**Input:** An integer array `nums` containing distinct numbers.
**Output:** A list of lists, where each inner list is a valid permutation.

## When to use it

- To generate every possible ordering of elements.
- Unlike Subsets, permutations care about order (`[1, 2]` is different from `[2, 1]`) and permutations must always contain EVERY element from the original array.

## Approach

**1. The Decision Tree:**
At the very first position of our permutation, we can pick ANY of the N numbers.
For the second position, we can pick ANY of the remaining N-1 numbers.
This creates a tree with exactly N! (N-factorial) leaves!

**2. The Backtracking State:**
We define a recursive function `backtrack(current_perm)`:
- `current_perm`: A list accumulating the numbers we've picked in order.
Because order matters, we do NOT use an `index` parameter to force ourselves to only look forward (like we did in Subsets). In Permutations, we always loop through the ENTIRE array `nums` to look for available numbers!

**3. Base Case:**
When `len(current_perm) == len(nums)`, our permutation is complete!
We append a copy to the global result and return.

**4. The Recursive Step (Backtracking):**
We loop through every number in `nums`.
If the number is ALREADY inside `current_perm`, we skip it (because we can't use the same element twice).
If it's available:
- We append it to `current_perm`.
- Recurse deeper.
- Backtrack: pop it off `current_perm` so the next iteration of the loop can try picking a different number for this position.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_02: Permutations.

Return every ordering of ``arr`` as a list of lists. Standard
backtracking: pick each unused element in turn, recurse, then
unpick. The output list of permutations is sorted so the
verify can do a plain equality check.
"""


def solve(arr, n):
    if n == 0:
        return [[]]
    result = []
    used = [False] * n

    def helper(path):
        if len(path) == n:
            result.append(list(path))
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                path.append(arr[i])
                helper(path)
                path.pop()
                used[i] = False

    helper([])
    result.sort()
    return result
```

</details>

## Walk-through

`nums = [1, 2]`. N=2.

1. `backtrack([])`:
   - Loop `num = 1`: not in `[]`. Append. `perm = [1]`.
     - `backtrack([1])`:
       - Loop `num = 1`: in `[1]`. Skip.
       - Loop `num = 2`: not in `[1]`. Append. `perm = [1, 2]`.
         - `backtrack([1, 2])`: Base Case! Append `[1, 2]` to result.
       - Backtrack: pop `2`. `perm = [1]`.
   - Backtrack: pop `1`. `perm = []`.
   - Loop `num = 2`: not in `[]`. Append. `perm = [2]`.
     - `backtrack([2])`:
       - Loop `num = 1`: not in `[2]`. Append. `perm = [2, 1]`.
         - `backtrack([2, 1])`: Base Case! Append `[2, 1]` to result.
       - Backtrack: pop `1`. `perm = [2]`.
       - Loop `num = 2`: in `[2]`. Skip.
   - Backtrack: pop `2`. `perm = []`.

Result: `[[1, 2], [2, 1]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N * N!)$ | $O(N)$ |
| **Average** | $O(N * N!)$ | $O(N)$ |
| **Worst** | $O(N * N!)$ | $O(N)$ |

There are exactly N! leaves. At each leaf, copying the array takes $O(N)$ time. Total time is strictly $O(N x N!)$.
*(Note: Finding `num in current_perm` takes $O(N)$ time, making the theoretical time $O(N^2 x N!)$. However, we can optimize this to $O(1)$ lookup using a Hash Set or boolean array).*
Space complexity is $O(N)$ for the recursion stack and the state list.

## Variants & optimizations

- **Permutations II (With Duplicates):** What if `nums = [1, 1, 2]`? The basic algorithm will yield duplicate permutations.
  1. Use a boolean `used[]` array instead of `num in current_perm` (because the two `1`s are distinct objects at different indices).
  2. Sort the array first.
  3. Inside the loop, skip identical neighbors IF their identical twin has NOT been used in the current recursive depth: `if i > 0 and nums[i] == nums[i-1] and not used[i-1]: continue`.
- **In-Place Swapping Optimization:** Instead of managing a separate `current_perm` list, you can manipulate the `nums` array directly! Pass an `index` representing the boundary of fixed elements. For the current `index`, loop `j` from `index` to `N`, swap `nums[index]` and `nums[j]`, recurse to `index+1`, and swap them back to backtrack!

## Real-world applications

- **Traveling Salesperson Problem (Brute Force):** Calculating the total distance for every single possible permutation of cities to visit to find the absolute shortest path.
- **Cryptography:** Brute-forcing all possible transposition ciphers or key shuffles.

## Related algorithms in cOde(n)

- **[backtrack_01 - Subsets](backtrack_01_subset-sum-decision.md)** — The $O(2^N)$ fundamental where order does not matter.
- **[backtrack_03 - Combination Sum](backtrack_03_combination-sum.md)** — A hybrid where order doesn't matter, but elements can be reused indefinitely!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
