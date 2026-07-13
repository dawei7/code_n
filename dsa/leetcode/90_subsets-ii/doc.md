# Subsets II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 90 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsets-ii/) |

## Problem Description
### Goal
You are given a nonempty integer list that may contain repeated values. Form subsets by selecting any collection of input occurrences, including selecting none or all of them, without using one occurrence more than once.

Return every distinct value multiset that can result. Choosing a different copy of an equal value with the same selected multiplicity does not create another subset, so duplicates must be suppressed. The subsets and their values may appear in any order, and the empty subset appears exactly once.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list that may contain duplicates

**Return value**

A list of all unique subsets in any outer or inner ordering.

### Examples
**Example 1**

- Input: `nums = [1,2,2]`
- Output: `[[],[1],[1,2],[1,2,2],[2],[2,2]]` in any order

**Example 2**

- Input: `nums = [0]`
- Output: `[[],[0]]`

**Example 3**

- Input: `nums = [1,1]`
- Output: `[[],[1],[1,1]]`

### Required Complexity

- **Time:** $O(n \cdot U)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort so interchangeable occurrences become adjacent siblings**

Sort `nums`, append a copy of the current path as one valid subset, then try positions from `start` onward. At one recursion depth, skip `nums[index]` when `index > start` and it equals `nums[index - 1]`. Those two choices would append the same value to the same prefix and expose equivalent suffix choices.

**The same value remains legal at a deeper multiplicity level**

The `index > start` condition restricts the skip to siblings. After selecting one copy and recursing with `start = index + 1`, the next equal copy is now the first choice at the deeper level and is allowed. That path represents using two copies rather than exchanging which single copy was used.

**Every recursion node represents one unique value multiset**

The path is a sorted multiset chosen from the processed positions. At each depth, exactly one branch represents choosing the next occurrence of any equal value, so sibling branches cannot emit the same multiset.

**Trace sibling skipping versus deeper reuse**

For sorted `[1,2a,2b]`, the root explores starting with 1 and with `2a`, but skips `2b` as an equivalent root choice. Inside the `2a` branch, `2b` is allowed, producing `[2,2]` once.

**Earliest equal copies give each subset one canonical path**

Every recursion path selects increasing source indices, so every emitted value list is a valid subset. For a subset needing `r` copies from an equal-value block, choose that block's earliest `r` available indices; this is its canonical source representation and the search permits it.

Choosing a later equal sibling at the same depth would produce an indistinguishable value path with no suffix option unavailable to the earlier copy, so it is skipped. Equal copies remain selectable at deeper levels, preserving multiplicity. Each unique subset therefore keeps one path and loses only duplicate representations.

#### Complexity detail

Let `U` be the number of unique output subsets. Copying paths of length up to `n` gives the output-sensitive $O(n \cdot U)$ bound. Sorting costs $O(n \log n)$ and recursion/path state uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Generate all $2^{n}$ index subsets then use a set:** performs duplicate work and stores normalization keys.
- **Frequency-map recursion:** directly chooses a count for each distinct value and is also output-sensitive.
- **Bit masks without duplicate skipping:** emit repeated subsets when equal values occupy different positions.
- If all `n` values are equal, the unique subsets are exactly the $n + 1$ possible multiplicities from zero through `n`.
- Sorting may change element order inside returned subsets, which is allowed because subset ordering is unrestricted.

</details>
