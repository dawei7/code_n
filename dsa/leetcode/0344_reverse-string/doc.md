# Reverse String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 344 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-string/) |

## Problem Description
### Goal
Given a mutable array of single-character strings, reverse the complete sequence. The original last character must become first, the original first must become last, and every other pair of mirrored positions must exchange contents.

Modify the supplied array in place and return nothing, using $O(1)$ extra memory rather than allocating another character array or returning a reversed copy. Preserve every character occurrence exactly once, including duplicates, spaces, and symbols. An array of length one remains unchanged, while an odd-length array keeps its middle character at the same index.

### Function Contract
**Inputs**

- `s`: the mutable list of single-character strings

**Return value**

- Returns `None`; after the call, `s` contains its original characters in reverse order.

### Examples
**Example 1**

- Input: `s = ["h", "e", "l", "l", "o"]`
- Output: `["o", "l", "l", "e", "h"]`

**Example 2**

- Input: `s = ["H", "a", "n", "n", "a", "h"]`
- Output: `["h", "a", "n", "n", "a", "H"]`

**Example 3**

- Input: `s = ["x"]`
- Output: `["x"]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Pair positions from opposite ends**

Reversal pairs positions that are equally far from opposite ends. Keep `left` at the beginning and `right` at the end. While `left < right`, swap `s[left]` with `s[right]`, then move both pointers inward.

**Why each swap finalizes two positions**

After each swap, the prefix before `left` and the suffix after `right` are already in their final reversed positions. The untouched middle still contains exactly the remaining original characters, so pairing its outermost two positions extends both finalized regions without disturbing earlier work. When the pointers meet or cross, every position has been finalized; a middle character in an odd-length array correctly remains where it is.

**Trace an odd-length array**

For `["h", "e", "l", "l", "o"]`, the first swap places `o` and `h`, the second places the two `l`/`e` endpoints of the remaining middle, and the center `l` needs no move.

#### Complexity detail

There are $\left\lfloor n / 2 \right\rfloor$ swaps, so the running time is $O(n)$. Only two indices and a constant-size temporary value used by the swap are needed, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Slice reversal or a new reversed list:** takes $O(n)$ time but allocates $O(n)$ extra storage and violates the in-place requirement.
- **Repeated front insertion:** can take $O(n^2)$ because every insertion shifts existing list elements.
- An empty list and a one-character list require no swaps.
- Duplicate characters do not change the pairing rule because positions, not character identities, determine the reversal.

</details>
