# UTF-8 Validation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 393 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/utf-8-validation/) |

## Problem Description
### Goal
Given byte values from `0` through `255`, determine whether the complete array has structurally valid UTF-8 grouping. A character begins with a leading byte indicating a length from one through four bytes, followed by exactly the required number of continuation bytes.

Single-byte characters begin with `0`; multibyte leaders begin with `110`, `1110`, or `11110`; every continuation byte begins with `10`. Return `False` for an invalid leader, misplaced continuation, or truncated final character, and `True` only when all bytes are consumed by complete encodings. This task validates byte-pattern structure rather than decoding characters into text.

### Function Contract
**Inputs**

- `data`: byte values from `0` through `255`

**Return value**

- Return `True` when every byte belongs to a complete encoding with a valid leading-byte pattern and the required `10xxxxxx` continuation bytes; otherwise return `False`.

### Examples
**Example 1**

- Input: `data = [197,130,1]`
- Output: `True`

**Example 2**

- Input: `data = [235,140,4]`
- Output: `False`

**Example 3**

- Input: `data = [240,162,138,147]`
- Output: `True`
