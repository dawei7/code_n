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
