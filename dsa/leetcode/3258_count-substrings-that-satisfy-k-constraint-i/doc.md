# Count Substrings That Satisfy K-Constraint I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3258 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/) |

## Problem Description

### Goal

Given a binary string \`s\` and an integer \`k\`, inspect every non-empty substring. A substring satisfies the $k$-constraint when at least one of two conditions holds: it contains at most \`k\` zeroes, or it contains at most \`k\` ones.

The two conditions are joined by an inclusive OR. A substring may contain more than \`k\` copies of one bit and remain valid because the other bit count is small enough. Count and return all substrings satisfying the constraint; equal text at different positions represents different substrings.

### Function Contract

**Inputs**

- \`s\`: A binary string of length $n$, where $1 \le n \le 50$.
- \`k\`: A positive integer, where $1 \le k \le n$.

**Return value**

- The number of index intervals whose substring has at most $k$ zeroes or at most $k$ ones.

### Examples

#### Example 1

- **Input:** \`s = "10101", k = 1\`
- **Output:** \`12\`

Only \`"1010"\`, \`"0101"\`, and \`"10101"\` contain more than one of both bits.

#### Example 2

- **Input:** \`s = "1010101", k = 2\`
- **Output:** \`25\`

Exactly the substrings longer than five violate the constraint.

#### Example 3

- **Input:** \`s = "11111", k = 1\`
- **Output:** \`15\`

Every substring has zero zeroes, so all $5 \cdot 6 / 2$ substrings are valid.
