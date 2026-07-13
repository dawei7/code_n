# Strobogrammatic Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 246 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number/) |

## Problem Description
### Goal
Given a nonempty decimal string `num`, imagine rotating its written digits by 180 degrees. Rotation reverses the order of positions and transforms only valid digit pairs: `0`, `1`, and `8` map to themselves, while `6` and `9` map to each other.

Return `True` when the rotated result exactly reproduces the original string. Any digit without a valid rotated form makes the answer `False`, as does a mismatched pair at mirrored positions. The comparison uses the entire numeral as written rather than its parsed integer value, so positions and characters must agree exactly after rotation.

### Function Contract
**Inputs**

- `num`: a non-empty decimal string

**Return value**

`True` exactly when rotating every digit by 180 degrees and reversing their positions reproduces `num`.

### Examples
**Example 1**

- Input: `num = "69"`
- Output: `True`

**Example 2**

- Input: `num = "88"`
- Output: `True`

**Example 3**

- Input: `num = "962"`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Rotation couples mirrored positions**

Valid rotations are `0->0`, `1->1`, `6->9`, `8->8`, and `9->6`. Move pointers inward and require the rotated left digit to equal the right digit.

Before each step, every digit pair outside the pointers is known to rotate into its mirrored partner.

**Pairwise compatibility is necessary and sufficient**

A 180-degree rotation reverses position order and applies the digit mapping. Therefore every valid numeral must match each left digit with its mapped right digit. If all mirrored pairs satisfy the mapping, rotating every digit reconstructs the original string in reverse positional order, so the entire numeral is strobogrammatic.

#### Complexity detail

At most half the string is examined, giving $O(n)$ time. The fixed five-pair mapping and two indices use constant space.

#### Alternatives and edge cases

- **Build the rotated string:** is simple but uses $O(n)$ extra space.
- Digits `2`, `3`, `4`, `5`, and `7` are immediately invalid; a middle digit must be `0`, `1`, or `8`.

</details>
