# Swap Adjacent in LR String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 777 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/swap-adjacent-in-lr-string/) |

## Problem Description

### Goal

Given equal-length strings `start` and `end` containing only `L`, `R`, and `X`, you may repeatedly replace an occurrence of `XL` with `LX` or an occurrence of `RX` with `XR`.

Return `True` if some sequence of these adjacent transformations changes `start` into `end`, and `False` otherwise. Symbol `X` represents an empty position: an `L` can move only left across empty positions, an `R` only right, and the relative order of all non-`X` symbols cannot be reversed.

### Function Contract

**Inputs**

- `start`: the initial nonempty string containing only `L`, `R`, and `X`.
- `end`: the desired string, with the same length and alphabet as `start`.

**Return value**

- `True` if a sequence of allowed adjacent swaps transforms `start` into `end`; otherwise `False`.

### Examples

**Example 1**

- Input: `start = "RXXLRXRXL", end = "XRLXXRRLX"`
- Output: `True`
- Explanation: Every nonempty token keeps its relative order, each `L` moves only left, and each `R` moves only right.

**Example 2**

- Input: `start = "X", end = "L"`
- Output: `False`
- Explanation: Swaps cannot create an `L` that is absent from the initial string.

**Example 3**

- Input: `start = "LXX", end = "XXL"`
- Output: `False`
- Explanation: Reaching the target would require the `L` to move right.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate token order from empty positions**

An allowed swap exchanges a token with an `X`; it never lets two `L` or `R` tokens cross. Deleting every `X` must therefore leave the same sequence of nonempty tokens in both strings. Two pointers can test this without constructing filtered strings: advance each pointer past `X`, then compare the next tokens.

**Enforce each token's direction**

Suppose the next matched token occurs at index `i` in `start` and index `j` in `end`. An `L` cannot move right, so $i < j$ is impossible. An `R` cannot move left, so $i > j$ is impossible. If the token types agree and the appropriate inequality holds, advance both pointers and examine the next pair.

These checks are necessary because swaps preserve token order and allow only the stated movement directions. They are also sufficient: matched tokens never cross, and each token can traverse the intervening `X` positions in its permitted direction until it reaches its target index. When both pointers exhaust their strings together, those compatible moves realize the target arrangement.

#### Complexity detail

Each pointer moves from left to right without retreating, so the scan takes $O(n)$ time. Only the two indices are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Filtered tokens plus position arrays:** Record the non-`X` token and index sequences for both strings, then compare them with the same directional rules; this is clear but uses $O(n)$ extra space.
- **Repeated swap simulation:** Perform legal adjacent swaps until the target appears; this can require quadratic work and needs careful move ordering to avoid getting stuck unnecessarily.
- **Breadth-first search over strings:** Exploring every reachable arrangement is correct only for tiny inputs because the state space grows combinatorially.
- **Identical strings:** Every token already satisfies its position constraint, so the answer is true.
- **Different token sequence:** A missing, extra, or reordered `L` or `R` makes transformation impossible regardless of the `X` positions.
- **Left token moving right:** If a matched `L` has $i < j$, reject immediately.
- **Right token moving left:** If a matched `R` has $i > j$, reject immediately.
- **All empty positions:** Two all-`X` strings are already equivalent.

</details>
