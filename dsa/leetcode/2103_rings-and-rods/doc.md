# Rings and Rods

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2103 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/rings-and-rods/) |

## Problem Description

### Goal

There are ten rods labeled from `0` through `9` and $n$ rings. Every ring is red, green, or blue. The string `rings` has length $2n$ and encodes one ring per consecutive character pair: the first character is its color (`"R"`, `"G"`, or `"B"`), and the second is the digit labeling its rod.

For example, `"R3G2B1"` places a red ring on rod `3`, a green ring on rod `2`, and a blue ring on rod `1`. Count how many rods hold at least one ring of every color.

### Function Contract

**Inputs**

- `rings`: a string containing $n$ color-rod pairs, where $1 \le n \le 100$. Every even index contains `"R"`, `"G"`, or `"B"`, and every following index contains a digit from `"0"` through `"9"`.

**Return value**

Return the number of rods containing red, green, and blue rings.

### Examples

**Example 1**

- Input: `rings = "B0B6G0R6R0R6G9"`
- Output: `1`
- Explanation: Rod `0` has all three colors; rod `6` lacks green and rod `9` has only green.

**Example 2**

- Input: `rings = "B0R0G0R9R0B0G0"`
- Output: `1`
- Explanation: Repeated rings do not change that only rod `0` has every color.

**Example 3**

- Input: `rings = "G4"`
- Output: `0`
- Explanation: A single ring cannot supply all three colors.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Encoding color presence**

Assign one bit to each color, such as red `1`, green `2`, and blue `4`. Maintain one integer mask for each of the ten rods. Process `rings` two characters at a time, decode the rod digit, and combine the color bit into that rod's mask with bitwise OR.

Duplicate rings of a color leave the same bit set, so the masks record presence rather than frequency. A rod has all three colors exactly when its mask equals `1 | 2 | 4`, which is `7`.

**Counting completed rods**

After all pairs are processed, count masks equal to `7`. Every encoded ring contributes its color to exactly its named rod. Therefore each final mask contains precisely the set of colors present on that rod, and the equality test selects exactly the requested rods.

#### Complexity detail

Processing the $n$ pairs takes $O(n)$ time, followed by a scan of exactly ten rods. The mask array always has length ten, so it uses $O(1)$ auxiliary space independent of $n$.

#### Alternatives and edge cases

- **Set per rod:** Store color characters in ten sets and count sets of size three. This is equally linear and remains constant-space because both rods and colors have fixed domains.
- **Three boolean arrays:** Track red, green, and blue presence separately for each rod. This is explicit but uses more parallel state than a bitmask.
- **Repeated string searches:** For each encoded ring, search the input for the other colors on the same rod. This can be correct but costs $O(n^2)$ time.
- Multiple rings with the same color and rod do not affect the result after the first one.
- Colors may arrive in any order within the string.
- Several rods may independently contain all three colors, up to all ten rods.
- A rod with many rings still does not count if even one color is absent.

</details>
