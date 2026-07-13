# 1-bit and 2-bit Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 717 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/1-bit-and-2-bit-characters/) |

## Problem Description
### Goal
An encoding contains two character types: a one-bit character represented by `0`, and a two-bit character represented by either `10` or `11`. You are given a valid binary array `bits` whose final bit is `0`.

Return `True` if that final array element must be decoded as a standalone one-bit character, and `False` if it is the second bit of the last two-bit character. Decode from the beginning according to the character prefixes; individual bits cannot be regrouped out of order.

### Function Contract
**Inputs**

- `bits`: a valid nonempty binary encoding whose final element is `0`

**Return value**

- `true` when the final array element starts a one-bit character; otherwise `false` because it is the second bit of a two-bit character

### Examples
**Example 1**

- Input: `bits = [1,0,0]`
- Output: `true`

**Example 2**

- Input: `bits = [1,1,1,0]`
- Output: `false`

**Example 3**

- Input: `bits = [0]`
- Output: `true`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Decode only from known character boundaries**

Start at index zero, which must be a character boundary. A `0` is a complete one-bit character, so advance one position. A `1` must begin either `10` or `11`, so advance two positions regardless of its second bit. Each jump therefore lands on the next character boundary.

**Stop before deciding the final zero**

Continue decoding only while the current boundary lies before the last array index. There are then two possibilities: a jump lands exactly on the final index, or the preceding two-bit character jumps over it to the end of the array.

**Why the landing position answers the question**

The scan never enters the middle of a character because every jump uses the length dictated by that character's leading bit. Consequently, landing on the final index proves its `0` starts its own one-bit character. Reaching the array length instead proves the final zero was already consumed as the second bit of a two-bit character.

#### Complexity detail

Every iteration advances by at least one position, so at most $n - 1$ bits are inspected. The scan takes $O(n)$ time and stores only its current index, using $O(1)$ extra space.

#### Alternatives and edge cases

- **Trailing-one parity:** count consecutive `1` bits immediately before the final zero; the last zero stands alone exactly when that count is even.
- **Dynamic programming over prefix boundaries:** it can mark reachable decode positions, but deterministic character lengths make the extra $O(n)$ storage unnecessary.
- **Repeated suffix rebuilding:** decoding the first character and copying the remaining suffix into a new list is correct but may take $O(n^2)$ total time.
- A one-element input `[0]` already consists of one one-bit character.
- If the scan reaches the second-to-last index and sees `1`, its two-bit character necessarily consumes the final zero.
- Zeros earlier in the array each form independent one-bit characters and do not affect later boundaries.
- Runs of `1` bits before the last zero are resolved by their parity, not merely by the immediately preceding bit.

</details>
