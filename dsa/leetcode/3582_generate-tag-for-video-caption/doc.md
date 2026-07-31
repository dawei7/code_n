# Generate Tag for Video Caption

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3582 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-tag-for-video-caption/) |

## Problem Description

### Goal

Convert a video caption into a tag by applying the required transformations in order. Join its space-separated words into camelCase and prefix the result with `#`. The first word must be entirely lowercase. For every later word, uppercase its first letter and lowercase every remaining letter.

Remove all characters other than English letters, while retaining the initial `#`. Finally, if the tag is longer than 100 characters, keep only its first 100 characters.

Return the resulting tag.

### Function Contract

**Inputs**

- `caption`: A string of length $n$, where $1\le n\le150$, containing only English letters and spaces.

**Return value**

Return the normalized camelCase tag beginning with `#` and containing at most 100 characters.

### Examples

**Example 1**

- Input: `caption = "Leetcode daily streak achieved"`
- Output: `"#leetcodeDailyStreakAchieved"`

**Example 2**

- Input: `caption = "can I Go There"`
- Output: `"#canIGoThere"`

**Example 3**

- Input: A single word containing 101 lowercase `h` characters.
- Output: `#` followed by 99 lowercase `h` characters.
- Explanation: The complete tag would contain 102 characters, so its final two letters are removed.

---
