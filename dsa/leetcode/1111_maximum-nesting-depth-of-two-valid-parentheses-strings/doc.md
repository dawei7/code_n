# Maximum Nesting Depth of Two Valid Parentheses Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1111 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/) |

## Problem Description

### Goal

A valid parentheses string (VPS) contains only `"("` and `")"`. The empty string is a VPS; concatenating two VPSs gives another VPS; and enclosing a VPS in one matching pair also gives a VPS. Its nesting depth is zero for the empty string, the greater depth of two concatenated VPSs, or one plus the depth of the enclosed VPS.

You are given a VPS `seq`. Assign every character to exactly one of two subsequences, `A` or `B`, while preserving source order in each subsequence. Both results must themselves be VPSs, and their lengths together equal `seq.length`. Minimize $\max(\operatorname{depth}(A), \operatorname{depth}(B))$.

Return an array `answer` of the same length as `seq`: `answer[i] = 0` assigns `seq[i]` to `A`, while `answer[i] = 1` assigns it to `B`. Multiple optimal assignments may exist, and any one is valid.

### Function Contract

**Inputs**

- `seq`: a valid parentheses string of length $n$.

**Return value**

- A length-$n$ array containing only `0` and `1`.
- The characters assigned to each value, read in their original order, must form a VPS.
- If the input depth is $d$, the larger resulting depth must be the optimal value $\lceil d/2 \rceil$.

### Examples

**Example 1**

- Input: `seq = "(()())"`
- One valid output: `[0,1,1,1,1,0]`

The outer pair goes to one subsequence and the two inner pairs go to the other, so neither result exceeds depth one.

**Example 2**

- Input: `seq = "()(())()"`
- One valid output: `[0,0,0,1,1,0,1,1]`

Other arrays are accepted when they produce two valid subsequences with the same minimum possible maximum depth.
