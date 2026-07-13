# Generate Parentheses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 22 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-parentheses/) |

## Problem Description
### Goal
Given a positive integer `n`, construct strings containing exactly `n` opening parentheses and `n` closing parentheses. A string is well formed when parentheses close in proper nesting order: no prefix may contain more closings than openings, and the final counts must balance.

Return every distinct well-formed string of length `2n` exactly once. The collection may be listed in any order. Parentheses cannot be omitted, added, or replaced, so each result represents one complete arrangement of the supplied `n` pairs.

### Function Contract
**Inputs**

- `n`: positive `int`

**Return value**

A `List[str]` containing all valid length-`2n` parenthesis strings exactly once.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `["((()))", "(()())", "(())()", "()(())", "()()()"]`

**Example 2**

- Input: `n = 1`
- Output: `["()"]`

**Example 3**

- Input: `n = 2`
- Output: `["(())", "()()"]`

### Required Complexity

- **Time:** $O(n \cdot C_n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Generate only prefixes that can still become balanced**

Track how many opening and closing parentheses have been placed. An opening parenthesis may be added while fewer than `n` have been used. A closing parenthesis may be added only when fewer closers than openers have been used; this is the prefix-balance condition that prevents a closing parenthesis from appearing before its partner.

When the path reaches length `2n`, both counts equal `n`, and the path is a complete valid string.

**Backtrack over the two legal decisions**

On entry to each recursive state, the path contains exactly the recorded counts, both counts are at most `n`, and `closed <= opened`. Therefore every prefix is compatible with a well-formed sequence. Append one legal parenthesis, recurse, and remove it again so sibling branches begin from the same prefix.

When the path reaches length `2n`, the bounds force both counts to equal `n`. Copy the path into the output at that point; retaining the mutable path object itself would allow later backtracking to alter saved results.

**Trace the pruned tree**

For $n = 2$, the first character must be `(`. From `((`, only two closers can follow, producing `(())`. From `()`, another opener is permitted and must then be closed, producing `()()`. No invalid prefix such as `)(` is ever generated.

**Prefix feasibility generates exactly the Catalan set**

An emitted path uses `n` openers and `n` closers, and the branching rule never permits more closers than openers in any prefix. Those are precisely the two conditions for a well-formed parenthesis string, so every leaf is valid.

Conversely, every well-formed string respects the same bounds at every position: it opens only while openers remain and closes only when an unmatched opener exists. The search therefore contains its exact left-to-right choice path. That path is unique, so every valid string is emitted once and no duplicate construction exists.

#### Complexity detail

There are `Cₙ` valid strings, the nth Catalan number, and copying each length-`2n` path costs $O(n)$, so $O(n \cdot C_n)$ time is output-optimal. The recursion and mutable path use $O(n)$ auxiliary space; returned strings occupy $O(n \cdot C_n)$ output space.

#### Alternatives and edge cases

- **Generate all $2^{2n}$ bracket strings then validate:** correct after filtering but explores exponentially many impossible prefixes.
- **Dynamic programming by pair count:** combines smaller valid lists and also follows the Catalan recurrence, but retains many partial strings.
- **Breadth-first prefix construction:** uses the same pruning rules but stores an entire frontier rather than one depth-first path.
- The contract uses positive `n`. If a variant permits $n = 0$, its conventional combinatorial result is one empty sequence, but that API choice should be handled explicitly.
- Output order is unrestricted; changing whether the opening or closing branch is explored first changes order, not correctness.

</details>
