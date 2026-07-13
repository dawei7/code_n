# Combination Sum II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 40 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/combination-sum-ii/) |

## Problem Description
### Goal
You are given positive candidate values, possibly including duplicates, and a positive target. Choose a subset of array positions whose values add exactly to the target. Each position may be used at most once, even when several positions store the same number.

Return every unique combination of values. Different index selections that produce the same multiset count as one answer, and value order does not distinguish combinations. The result collection may use any order. If no subset reaches the target, return an empty list.

### Function Contract
**Inputs**

- `candidates`: `List[int]` of positive integers, possibly with duplicates
- `target`: positive `int`

**Return value**

A `List[List[int]]` containing all unique target-sum combinations in any order.

### Examples
**Example 1**

- Input: `candidates = [10, 1, 2, 7, 6, 1, 5], target = 8`
- Output: `[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]`

**Example 2**

- Input: `candidates = [2, 5, 2, 1, 2], target = 5`
- Output: `[[1, 2, 2], [5]]`

**Example 3**

- Input: `candidates = [7, 7], target = 4`
- Output: `[]`

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort values but consume positions only once**

Sort candidates, then backtrack with a `start` index. Choosing position `i` recurses from $i + 1$, enforcing the use-once rule even when another position contains the same value. Positive values make the remainder strictly decrease, and sorted order allows the loop to stop once a value exceeds it.

**Duplicate skipping is local to one recursion depth**

At one recursion depth, skip `candidates[i]` when it equals `candidates[i - 1]` and `i > start`. Those sibling branches have identical path prefixes and identical next values; the earlier occurrence has access to every suffix position available to the later one, so the later branch cannot create a new value combination.

Do not skip the same value across different depths. Once one copy has been chosen, a second input position may legitimately supply another copy, as in `[1, 1, 6]`. The `i > start` condition is what distinguishes a duplicate sibling from a duplicate used deeper in the same path.

**Increasing source indices enforce the use-once rule**

The path contains increasing source indices, is nondecreasing by value, and sums to `target - remaining`. Each value is used at most once. Same-depth duplicate skipping leaves one representative for every distinct next value.

**Trace two equal values used at different depths**

After sorting `[10, 1, 2, 7, 6, 1, 5]`, the first branch may choose both separate 1 positions and then 6, yielding `[1, 1, 6]`. When backtracking to the root, the second 1 is skipped as a sibling, preventing duplicate versions of combinations beginning with one 1.

**The earliest equal sibling represents every suffix choice**

Advancing recursion to the next index after a choice ensures no input position can be reused. Any valid combination can be represented by selecting its occurrences in increasing sorted-index order, and the search includes that path.

At one recursion depth, equal-valued sibling choices would leave equivalent value paths and the later occurrence has no suffix option unavailable to the earliest occurrence. Keeping only the first equal sibling therefore removes duplicate representations without removing a unique value combination. Equal values may still be chosen at deeper levels, which correctly permits distinct duplicate positions within one result.

#### Complexity detail

The include/exclude search has up to $2^{n}$ position subsets, and copying an answer can cost $O(n)$, giving a loose $O(n \cdot 2^n)$ bound. Sorting costs $O(n \log n)$ and is dominated. The path and recursion use $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all subsets then deduplicate:** explores duplicate-heavy branches and stores a potentially huge set of tuples.
- **Frequency-count recursion:** branches on how many copies of each distinct value to use and can be efficient, but requires a separate compressed representation.
- **Reuse the current index:** would solve the unlimited-use variant instead and violate this problem's contract.
- Failing to sort makes same-depth duplicate skipping unreliable because equal values are no longer adjacent.
- Copy the path at remainder zero. Output order is unrestricted, but each emitted combination is naturally nondecreasing.

</details>
