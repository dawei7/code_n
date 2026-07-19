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
