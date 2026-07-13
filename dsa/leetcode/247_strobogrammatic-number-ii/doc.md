# Strobogrammatic Number II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 247 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number-ii/) |

## Problem Description
### Goal
Given a positive integer `n`, generate every decimal string of exactly that length that looks unchanged after a 180-degree rotation. Mirrored positions must use compatible pairs `00`, `11`, `69`, `88`, or `96`, and a middle position in an odd-length numeral must rotate to itself.

Return all valid strobogrammatic strings in any order. Multi-digit results cannot begin with `0`, although the one-digit numeral `"0"` is valid. Include each numeral once and no string of a different length. The task returns textual numerals so their exact digit positions are preserved rather than parsed and reformatted as integers.

### Function Contract
**Inputs**

- `n`: the positive required number of digits

**Return value**

All length-`n` strobogrammatic strings in any order, without leading zeros unless $n = 1$.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `["11","69","88","96"]`

**Example 2**

- Input: `n = 1`
- Output: `["0","1","8"]`

**Example 3**

- Input: `n = 3`
- Output: `["101","111","181","609","619","689","808","818","888","906","916","986"]`

### Required Complexity

- **Time:** $O(n \cdot 5^{n/2})$
- **Space:** $O(n \cdot 5^{n/2})$

<details>
<summary>Approach</summary>

#### General

**Build from the center outward**

The empty center seeds even lengths; `0`, `1`, and `8` seed odd lengths. Wrap every shorter valid center with one of `00`, `11`, `69`, `88`, or `96`.

**Leading zero is forbidden only at the final wrapper**

`00` is valid inside a numeral but invalid as the outermost pair when the final length exceeds one.

Every intermediate string is strobogrammatic and has the required parity. Wrapping with a valid rotating pair preserves that property.

**Removing the outer pair reverses the construction uniquely**

Every valid length-`n` numeral has one allowed outer rotating pair. Removing that pair leaves a valid length-`n-2` center, so repeated removal reaches the appropriate empty or one-digit seed. The recursive construction can therefore reproduce every answer. Conversely, each allowed wrapper preserves rotational symmetry, and excluding only the outermost `00` pair removes exactly the multi-digit strings with a leading zero.

#### Complexity detail

The output family grows exponentially with roughly five choices per digit pair; constructing each length-$n$ string gives output-sensitive $O(n \cdot 5^{n/2})$ time and result space.

#### Alternatives and edge cases

- **Enumerate all $10^{n}$ numerals then test:** explores overwhelmingly invalid candidates.
- One digit has exactly three answers; internal zeros remain allowed.

</details>
