# Jewels and Stones

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 771 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jewels-and-stones/) |

## Problem Description

### Goal

Given strings `jewels` and `stones`, every character in `jewels` identifies a distinct stone type considered a jewel, while each character in `stones` represents one stone you own.

Return how many owned stones are jewels. Count repeated occurrences in `stones` separately, but use `jewels` only as the set of qualifying types. Letters are case-sensitive, so an uppercase and lowercase form are different stone types.

### Function Contract

**Inputs**

- `jewels`: a string of distinct case-sensitive jewel characters.
- `stones`: a string where each character represents one owned stone.

**Return value**

- The number of characters in `stones` that also occur in `jewels`, counting repeated stones separately.

### Examples

**Example 1**

- Input: `jewels = "aA"`, `stones = "aAAbbbb"`
- Output: `3`
- Explanation: The lowercase `a` and both uppercase `A` stones are jewels.

**Example 2**

- Input: `jewels = "z"`, `stones = "ZZ"`
- Output: `0`
- Explanation: Uppercase `Z` does not match lowercase `z`.

**Example 3**

- Input: `jewels = "b"`, `stones = "bbbb"`
- Output: `4`
- Explanation: Every occurrence is counted as a separate jewel stone.

### Required Complexity

- **Time:** $O(j+s)$
- **Space:** $O(j)$

<details>
<summary>Approach</summary>

#### General

**Build a membership set once**

Insert all `j` jewel characters into a set. Then scan the `s` stone characters and increment the answer whenever the current character belongs to that set.

The set contains exactly the symbols classified as jewels. Each position in `stones` is tested once and contributes one precisely when its symbol is in that classification, so repeated occurrences are counted independently and non-jewels never contribute.

#### Complexity detail

Building the set takes $O(j)$ time and scanning the stones takes $O(s)$ expected time, for $O(j + s)$ total. The set stores at most `j` symbols, using $O(j)$ space; with the fixed letter alphabet this is also bounded by a constant.

#### Alternatives and edge cases

- **Boolean lookup table:** Mark letter codes in a fixed-size array for the same $O(j + s)$ time and constant bounded space.
- **Search the jewel string for every stone:** This avoids a separate set but takes $O(js)$ time in the worst case.
- **Frequency counter for stones:** Summing counts for jewel symbols is correct, but stores more information than direct membership counting needs.
- **Case sensitivity:** `a` and `A` must remain separate symbols.
- **Repeated stones:** Every matching occurrence increments the result.
- **No matching stones:** Return zero.
- **Every stone is a jewel:** Return `len(stones)`.

</details>
