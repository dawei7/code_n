# Combination Sum

| | |
|---|---|
| **ID** | `backtrack_03` |
| **Category** | backtracking |
| **Complexity (required)** | $O(N^(T/M)$) Time, $O(T/M)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Combination Sum](https://leetcode.com/problems/combination-sum/) |

## Problem statement

Given an array of **distinct** integers `candidates` and a target integer `target`, return a list of all **unique combinations** of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.
The same number may be chosen from `candidates` an **unlimited number of times**. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

**Input:** An integer array `candidates` and an integer `target`.
**Output:** A list of lists representing valid combinations.

## When to use it

- The canonical algorithm for the **Unbounded Knapsack** problem when you need to return the *actual paths/items* rather than just the mathematical minimum or maximum count.
- It tests your ability to manage Backtracking state while allowing infinite reuse of elements.

## Approach

**1. The Decision Tree:**
Because we can reuse elements, the tree can theoretically branch infinitely! However, we only care about paths that sum exactly to `target`. If our sum exceeds `target`, we immediately stop exploring that branch (this is called **Pruning**).
Furthermore, to avoid generating duplicate combinations (e.g. `[2, 2, 3]` and `[2, 3, 2]`), we MUST enforce an order. We do this by maintaining a `start_index`. We are only allowed to pick the current element, or elements *to the right* of it. We can never look back left!

**2. The Backtracking State:**
`backtrack(start_index, current_combo, current_sum)`:
- `start_index`: Prevents looking backwards (prevents `[3, 2, 2]`).
- `current_combo`: The numbers chosen so far.
- `current_sum`: The sum of the chosen numbers.

**3. Base Cases (The Pruning):**
- If `current_sum == target`: We found a valid combo! Append a copy to `result` and return.
- If `current_sum > target`: We overshot. This branch is dead. Return immediately!

**4. The Recursive Step:**
Loop `i` from `start_index` to `len(candidates)`.
- **Make choice:** Add `candidates[i]` to our combo and sum.
- **Recurse:** Call `backtrack(i, combo, sum)`.
  *(CRITICAL: Notice we pass `i`, NOT `i + 1`! Because we are allowed to reuse `candidates[i]` an infinite number of times, we must stay at `i` for the next depth of the tree).*
- **Backtrack:** Pop the element, subtract from sum.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for backtrack_03: Combination Sum.

Given a list of positive integers and a target, return every
unique combination that sums to target. Each input element may
be used any number of times. Sort the input first and always
recurse forward (i >= start) to avoid duplicates.
"""


def solve(candidates, target, n):
    candidates = sorted(candidates)
    result = []

    def helper(start, remaining, path):
        if remaining == 0:
            result.append(list(path))
            return
        if start == n or remaining < 0:
            return
        for i in range(start, n):
            if candidates[i] > remaining:
                break
            path.append(candidates[i])
            helper(i, remaining - candidates[i], path)
            path.pop()

    helper(0, target, [])
    return result
```

</details>

## Walk-through

`candidates = [2, 3]`, `target = 5`.

1. `backtrack(0, [], 0)`:
   - Loop `i=0` (`num=2`).
     - `backtrack(0, [2], 2)`:
       - Loop `i=0` (`num=2`).
         - `backtrack(0, [2, 2], 4)`:
           - Loop `i=0` (`num=2`).
             - `backtrack(0, [2, 2, 2], 6)`: `6 > 5`. Prune! Return.
           - Loop `i=1` (`num=3`).
             - `backtrack(1, [2, 2, 3], 7)`: `7 > 5`. Prune! Return.
       - Loop `i=1` (`num=3`).
         - `backtrack(1, [2, 3], 5)`: `5 == 5`. SUCCESS! Append `[2, 3]`. Return.
   - Loop `i=1` (`num=3`).
     - `backtrack(1, [3], 3)`:
       - Loop `i=1` (`num=3`).
         - `backtrack(1, [3, 3], 6)`: `6 > 5`. Prune! Return.

Result: `[[2, 3]]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N^(T/M)$) | $O(T/M)$ |
| **Average** | $O(N^(T/M)$) | $O(T/M)$ |
| **Worst** | $O(N^(T/M)$) | $O(T/M)$ |

*Where N is the number of candidates, T is the target value, and M is the minimum value in the candidates array.*
The maximum depth of the recursive tree is T/M (e.g. if the target is 10 and the smallest coin is 1, the depth is 10).
At each node, the tree branches N times.
Total time complexity is extremely loose, bounded roughly by $O(N^{\frac{T}{M}})$.
Space complexity is $O(T/M)$ corresponding to the maximum depth of the recursive call stack.

## Variants & optimizations

- **Sorting Optimization:** If you sort the `candidates` array ascending before starting, you can apply an incredibly powerful prune! Inside the `for` loop, if `current_sum + candidates[i] > target`, you can immediately `break` the entire `for` loop, because all subsequent candidates will be even larger!
- **Combination Sum II (No Reuse, Duplicates in Input):** If candidates can only be used ONCE, pass `i + 1` in the recursion. If the input contains duplicate numbers (e.g. `[10, 1, 2, 7, 6, 1, 5]`), you must sort first, and add `if i > start_index and candidates[i] == candidates[i-1]: continue` to prevent duplicate result sets!
- **Coin Change:** If the question ONLY asks for the *minimum number of coins* required, do NOT use Backtracking! That is an Unbounded Knapsack problem that should be solved with a 1D DP array in strictly $O(N x T)$ time.

## Real-world applications

- **Financial Ledger Balancing:** Finding the specific combination of recurring, unbounded transactions (e.g., $5 deposits) that sum to an observed discrepancy in an accounting log.

## Related algorithms in cOde(n)

- **[backtrack_01 - Subsets](backtrack_01_subset-sum-decision.md)** — The fundamental problem, where elements can only be used once.
- **[dp_17 - Partition Equal Subset Sum](../dynamic/dp_17_partition-equal-subset-sum.md)** — The identical problem, but returning a boolean rather than the actual paths.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
