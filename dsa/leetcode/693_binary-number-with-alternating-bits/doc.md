# Binary Number with Alternating Bits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 693 |
| Difficulty | Easy |
| Topics | Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/binary-number-with-alternating-bits/) |

## Problem Description
### Goal
Given a positive integer `n`, inspect its binary representation without leading zeroes. It has alternating bits when every pair of adjacent bit positions contains different values, so each `0` is next to `1` and each `1` is next to `0` wherever a neighbor exists.

Return `True` if all adjacent bits alternate and `False` otherwise. A one-bit representation is valid because it has no adjacent pair that violates the condition; any occurrence of `00` or `11` makes a longer representation invalid.

### Function Contract
**Inputs**

- `n`: a positive integer

**Return value**

- `true` when the ordinary binary representation of `n` alternates between `0` and `1`; otherwise `false`

### Examples
**Example 1**

- Input: `n = 5`
- Output: `true`
- Explanation: `5` is `101` in binary.

**Example 2**

- Input: `n = 7`
- Output: `false`
- Explanation: `7` is `111`, which contains equal adjacent bits.

**Example 3**

- Input: `n = 11`
- Output: `false`
- Explanation: `11` is `1011`; its two least-significant bits are both `1`.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare neighboring bits directly**

The least-significant bit gives the first value to remember. Shift `n` right once, then repeatedly extract the new least-significant bit with $n \mathbin{\&} 1$. This new bit was immediately beside the remembered bit in the original representation.

**Stop at the first violation**

If the two bits are equal, that adjacent pair disproves alternation, so return `false`. Otherwise remember the current bit, shift again, and continue toward the most-significant bit.

**Why completing the scan is sufficient**

Every shift exposes exactly one previously unchecked adjacent pair. Returning early is therefore justified by a concrete equal pair. If the loop finishes, every adjacent pair in the representation has been checked and each differed, which is precisely the required condition.

#### Complexity detail

A positive integer has $floor(log2(n)) + 1$ significant bits. The scan performs constant work per bit, so it takes $O(\log n)$ time and stores only the current and previous bits, using $O(1)$ extra space.

#### Alternatives and edge cases

- **XOR consecutive shifts:** let `mask = n ^ (n >> 1)`; alternating bits make `mask` a run of `1` bits, testable with `mask & (mask + 1) = 0`. This is compact but less direct to derive.
- **Binary-string scan:** convert `n` to text and compare neighboring characters; it is also $O(\log n)$ time but allocates $O(\log n)$ space.
- A one-bit value such as `1` has no adjacent pair and is therefore alternating.
- Leading zeros are not part of the ordinary binary representation and must not be inspected.
- Equal bits anywhere in the representation are sufficient to return `false`, including at either end.

</details>
