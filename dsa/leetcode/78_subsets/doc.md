# Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 78 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/subsets/) |

## Problem Description
### Goal
You are given an array `nums` of unique integers. A subset chooses any collection of those values, from choosing none through choosing every value, without using an element more than once.

Return the complete power set containing all $2^{n}$ unique subsets. The empty subset and full input set must each appear exactly once. Value order inside a subset does not create another answer, and the solution set may be returned in any order.

### Function Contract
**Inputs**

- `nums`: a list of distinct integers

**Return value**

A `List[List[int]]` containing all $2^{n}$ subsets.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]` in any order

**Example 2**

- Input: `nums = [0]`
- Output: `[[],[0]]`

**Example 3**

- Input: `nums = [-1,2]`
- Output: `[[],[-1],[2],[-1,2]]` in any order

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Every input value contributes one independent binary decision**

Backtrack by input index. At every position, recurse once without the current value and once after appending it. Pop after the inclusion branch returns. When the index reaches the array length, every value has a fixed include/exclude decision, so copy the current path into the result.

**Depth records exactly which prefix has been decided**

At depth `i`, the path contains exactly the included values among `nums[0:i]` in original order. The two branches partition all subsets of that prefix according to whether they contain `nums[i]`.

**Trace the binary decision tree**

For `[1,2]`, excluding 1 leads to `[]` and `[2]`; including 1 leads to `[1]` and `[1,2]`. These four leaves are the complete power set.

**Include-or-exclude decisions are the power set**

For each distinct input value, a subset makes exactly one binary decision: include it or omit it. Reading those decisions in input order identifies one root-to-leaf branch of the recursion.

Conversely, every branch makes one decision for every value and therefore produces a valid subset. This one-to-one correspondence between subsets and binary branches proves that all $2^{n}$ subsets are emitted exactly once.

#### Complexity detail

There are $2^{n}$ outputs and copying a subset costs up to $O(n)$, for the output-tight $O(n \cdot 2^n)$ bound. The path and recursion use $O(n)$ auxiliary space, excluding the returned power set.

#### Alternatives and edge cases

- **Bit masks:** enumerate the same $2^{n}$ choices iteratively and offer equivalent asymptotic complexity.
- **Repeatedly extend the current result:** is concise but stores the growing output throughout, as required anyway.
- **Generate permutations then deduplicate:** creates redundant orders and performs far more work.
- The empty subset is the leaf that excludes every value; the full subset includes every value.
- Distinct input values guarantee different decision masks produce different subsets. Duplicate values require sibling suppression or frequency handling.

</details>
