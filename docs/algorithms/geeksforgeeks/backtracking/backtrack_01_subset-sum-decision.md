# Subsets (Power Set)

| | |
|---|---|
| **ID** | `backtrack_01` |
| **Category** | backtracking |
| **Complexity (required)** | $O(N * 2^N)$ Time, $O(N)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Subsets](https://leetcode.com/problems/subsets/) |

## Problem statement

Given an integer array `nums` of **unique** elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

**Input:** An integer array `nums`.
**Output:** A list of lists, where each inner list is a valid subset.

## When to use it

- The absolute foundation of Backtracking algorithms.
- Use it to generate every possible combination or grouping of elements without caring about permutations (ordering).

## Approach

**1. The Decision Tree:**
For every element in the array, we have exactly two choices:
1. **Include** the element in our current subset.
2. **Exclude** the element from our current subset.
Because there are N elements and 2 choices for each, there will be exactly 2^N leaves in our decision tree (the total number of subsets).

**2. The Backtracking State:**
We define a recursive function `backtrack(index, current_subset)`:
- `index`: Which element from `nums` are we currently making a decision on?
- `current_subset`: A list accumulating the choices we've made so far.

**3. Base Case:**
When `index == len(nums)`, it means we have made a decision (Include/Exclude) for EVERY element in the array. We have reached a leaf node!
We take a *snapshot* (copy) of `current_subset` and add it to our global `result` list. Then, we return to allow the tree to continue exploring.

**4. The Recursive Step (Backtracking):**
Inside our function, we execute our two choices:
- **Choice 1 (Include):** Add `nums[index]` to `current_subset`. Recurse to `index + 1`.
- **Choice 2 (Exclude):** Before we can recurse, we MUST "undo" the choice we just made! We pop `nums[index]` off `current_subset` (this is the defining action of Backtracking). Then we recurse to `index + 1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_01: Subset Sum (decision).

Classic backtracking: at each step, try including or excluding
the current element. Prune when the running sum is past the
target. Return True iff a subset sums exactly to target.
"""


def solve(arr, target, n):
    if n == 0:
        return target == 0

    def helper(i, remaining):
        if remaining == 0:
            return True
        if i == n or remaining < 0:
            return False
        # Include arr[i] or skip it.
        return helper(i + 1, remaining - arr[i]) or helper(i + 1, remaining)

    return helper(0, target)
```

</details>

## Walk-through

`nums = [1, 2]`. N=2.

1. `backtrack(0, [])`:
   - Include 1 -> `subset = [1]`. Call `backtrack(1, [1])`.
     - Include 2 -> `subset = [1, 2]`. Call `backtrack(2, [1, 2])`.
       - Base Case! Append `[1, 2]` to result. Return.
     - Backtrack -> pop `2`. `subset = [1]`.
     - Exclude 2 -> Call `backtrack(2, [1])`.
       - Base Case! Append `[1]` to result. Return.
   - Backtrack -> pop `1`. `subset = []`.
   - Exclude 1 -> Call `backtrack(1, [])`.
     - Include 2 -> `subset = [2]`. Call `backtrack(2, [2])`.
       - Base Case! Append `[2]` to result. Return.
     - Backtrack -> pop `2`. `subset = []`.
     - Exclude 2 -> Call `backtrack(2, [])`.
       - Base Case! Append `[]` to result. Return.

Result: `[[1, 2], [1], [2], []]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N * 2^N)$ | $O(N)$ |
| **Average** | $O(N * 2^N)$ | $O(N)$ |
| **Worst** | $O(N * 2^N)$ | $O(N)$ |

There are exactly 2^N nodes/leaves. At each leaf, copying the `current_subset` takes $O(N)$ time. Total time complexity is strictly $O(N x 2^N)$.
Space complexity is $O(N)$ for the recursion call stack and the `current_subset` list. (The output array taking $O(N x 2^N)$ space is usually excluded from auxiliary space analysis).

## Variants & optimizations

- **Subsets II (With Duplicates):** What if `nums = [1, 2, 2]`? The standard algorithm will generate duplicate subsets `[1, 2]` twice! To fix this: 1. Sort the array first. 2. When executing the "Exclude" branch, use a `while` loop to skip over any subsequent elements that are identical to `nums[index]`.
- **Bitmask Iteration:** You can completely avoid recursion! A binary number from `0` to `2^N - 1` perfectly represents every Include/Exclude decision. The i-th bit of the number determines if `nums[i]` is in the subset. This is $O(N x 2^N)$ time and $O(1)$ space, making it vastly superior for competitive programming.

## Real-world applications

- **Database Query Optimization:** Generating the power set of join conditions to evaluate the cost of all possible sub-query execution plans.
- **Feature Selection (Machine Learning):** Testing all possible subsets of variables to find the model with the highest predictive accuracy.

## Related algorithms in cOde(n)

- **[backtrack_02 - Permutations](backtrack_02_permutations.md)** — The difference between subsets (order doesn't matter) and permutations (order matters).
- **[dp_06 - Subset Sum](../dynamic/dp_06_subset-sum.md)** — If you only need to know IF a subset exists that sums to a target, an $O(N^2)$ DP array is infinitely faster than $O(2^N)$ backtracking!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
