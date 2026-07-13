# Hamming Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 461 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/hamming-distance/) |

## Problem Description
### Goal
Given two nonnegative integers `x` and `y`, compare their binary representations position by position. A bit contributes to the Hamming distance when one integer has `0` at that position and the other has `1`.

Return the total number of differing positions. Leading zeroes beyond both numbers' highest set bits match and add nothing, while a set bit present in only the larger-width representation does count. Equivalently, count set bits in $x \oplus y$. The task returns the distance only, not the differing indices or a binary string.

### Function Contract
**Inputs**

- `x`: a nonnegative integer
- `y`: a nonnegative integer

**Return value**

- The number of binary positions containing different bits in `x` and `y`

### Examples
**Example 1**

- Input: `x = 1, y = 4`
- Output: `2`

**Example 2**

- Input: `x = 3, y = 1`
- Output: `1`

**Example 3**

- Input: `x = 0, y = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(\log \max(x, y))$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use XOR to isolate disagreements**

At each bit position, XOR is one exactly when the corresponding bits of `x` and `y` differ. Therefore the Hamming distance is the number of set bits in $x \oplus y$; positions where both inputs agree disappear automatically.

**Remove one differing bit per iteration**

For a positive integer `difference`, subtracting one flips its lowest set bit to zero and changes only lower zero bits to one. ANDing the original value with `difference - 1` therefore clears exactly that lowest set bit. Repeating `difference & = difference - 1` and counting iterations processes every disagreement once.

**Why leading zeros need no handling**

Binary representations may be viewed as padded with infinitely many leading zeros. Beyond the highest set bit of either input, both values contain zero, so XOR has no additional set bits and the loop correctly stops.

#### Complexity detail

If `b` is the relevant bit width, the method performs one iteration per differing bit, at most $b = O(\log \max(x, y))$. Under the problem's fixed 32-bit bound this is also constant bounded work. Only the XOR value and counter are stored, giving $O(1)$ space.

#### Alternatives and edge cases

- **Shift and inspect the low bit:** checks every relevant position in $O(b)$ time and is equally direct.
- **Built-in population count:** expresses the same operation concisely when the language provides it.
- **Binary-string comparison:** works but allocates string representations and requires padding or XOR first.
- **Rebuild each bit mask from scratch:** remains correct but repeats prior shifts and takes $O(b^2)$ work.
- **Equal numbers:** XOR is zero, so the distance is zero.
- **One zero input:** the answer is the population count of the other input.
- **Highest allowed bit:** integer bit operations avoid sign or formatting ambiguity for nonnegative inputs.

</details>
