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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track how many continuation bytes are owed**

Maintain `remaining`, the number of `10xxxxxx` bytes required to finish the current character. When it is positive, the next byte must have its two highest bits equal to `10`; accept it and decrement the debt, or reject immediately.

**Classify a byte only when a new character begins**

With no outstanding debt, a leading zero bit represents a complete one-byte character. Prefixes `110`, `1110`, and `11110` begin two-, three-, and four-byte characters and set the debt to one, two, or three. Every other prefix is invalid in the problem's structural UTF-8 model.

**Reject unfinished characters at the end**

Every accepted continuation discharges exactly one byte promised by its leader. Therefore the scan partitions the array into valid character shapes whenever no prefix check fails. The final result is valid precisely when `remaining` is zero; a positive value means the last character ended early.

**Honor the requested validation scope**

The contract asks whether the bytes match UTF-8 length and continuation patterns. It does not ask to reject overlong encodings, surrogate code points, or values beyond Unicode's scalar range, so the algorithm does not introduce those extra semantic rules.

#### Complexity detail

Each of the `n` bytes undergoes a constant number of masks and comparisons, for $O(n)$ time. The continuation counter uses $O(1)$ space.

#### Alternatives and edge cases

- **Index by character length:** determine a leader's width and inspect the next one to three bytes directly; it has the same bounds but needs careful index advancement.
- **Convert bytes to binary strings:** can make prefixes visual but allocates temporary text and obscures simple masks.
- **Consume a front-deleting array:** can validate correctly, but repeated shifts may take $O(n^2)$ time.
- A continuation byte cannot begin a character.
- A leader at the end is invalid when it still requires continuation bytes.
- Five-byte and longer historical prefix shapes are invalid.
- ASCII bytes may appear between or after multibyte characters.

</details>
