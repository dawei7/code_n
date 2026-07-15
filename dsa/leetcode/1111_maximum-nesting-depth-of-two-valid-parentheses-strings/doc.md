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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**View each pair as occupying one depth level:** While scanning a VPS, increment the current depth before handling an opening parenthesis. A closing parenthesis belongs to the same level as its matching opening parenthesis, so assign it using the current depth before decrementing.

**Alternate depth levels between the two subsequences:** Assign odd depths to one group and even depths to the other. Thus both characters of every matching pair receive the same group, while directly nested pairs alternate groups. Each group's extracted characters remain balanced: an opening assigned at some depth is matched by the closing assigned at that same depth, and no assigned closing can precede its matching opening.

**Why the split is optimal:** Suppose the original maximum depth is $d$. At a position reaching depth $d$, those $d$ simultaneously open pairs must be divided between two groups. One group must contain at least $\lceil d/2 \rceil$ of them, so no assignment can achieve a smaller maximum. Alternating levels gives one group the odd levels and the other the even levels, making their depths at most $\lceil d/2 \rceil$ and $\lfloor d/2 \rfloor$. It meets the lower bound and is therefore optimal.

#### Complexity detail

The scan processes each of the $n$ parentheses once and performs constant work per character, for $O(n)$ time. The returned assignment array uses $O(n)$ space. Apart from that required output, the depth counter uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Explicit stack of pair ownership:** Push a chosen group for each opening and pop it for the matching closing. It is correct but stores $O(n)$ auxiliary stack state that depth parity makes unnecessary.
- **Recompute every prefix depth:** It can derive the same assignments but rescans prefixes and takes $O(n^2)$ time.
- **Alternate complete primitive VPS blocks:** This keeps both outputs valid but does not split a deeply nested block, so it can leave the full depth in one group and be nonoptimal.
- **Flat input:** For `"()()"`, the original depth is one; assigning all pairs to either group is already optimal.
- **Deeply nested input:** Alternating levels divides the open pairs as evenly as possible between the groups.
- **Concatenated components:** Depth returns to zero between components, and the same parity rule handles each independently.
- **Output ties:** Swapping every `0` and `1` preserves validity and depth, and other optimal assignments may also exist.

</details>
