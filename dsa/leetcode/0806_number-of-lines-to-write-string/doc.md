# Number of Lines To Write String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 806 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-lines-to-write-string/) |

## Problem Description

### Goal

Given widths for the 26 lowercase English letters and a string `s`, write the characters of `s` from left to right on lines that can contain at most `100` pixels. Put as many consecutive letters as possible on the current line before beginning the next line.

Return `[lines, lastWidth]`, where `lines` is the total number of lines used and `lastWidth` is the pixel width occupied on the final line. Characters cannot be split or reordered, and a new line begins only when the next character would exceed `100`.

### Function Contract

**Inputs**

- `widths`: 26 positive widths in alphabet order from `a` through `z`.
- `s`: a nonempty lowercase English string.

**Return value**

- `[line_count, final_width]`, where `line_count` is the number of lines used and `final_width` is the occupied width on the last line.

### Examples

**Example 1**

- Input: `widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"`
- Output: `[3,60]`
- Explanation: Ten letters fit per full line, leaving six letters on the third line.

**Example 2**

- Input: `widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"`
- Output: `[2,4]`
- Explanation: The nine width-10 letters and two `a` characters occupy 98 units; the last `a` starts a new line.

**Example 3**

- Input: `widths = [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5], s = "aaaaaaaaaaaaaaaaaaaa"`
- Output: `[1,100]`
- Explanation: A line exactly at the capacity does not wrap.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Maintain the active line**

Begin with one line of width zero. For each character, use its alphabet index to retrieve the width. If adding it would exceed 100, start a new line whose initial width is that character's width; otherwise, add it to the current line.

The two maintained values describe the layout of the processed prefix. When the next character fits, appending it preserves that layout. When it does not, the writing rule requires a line break immediately before that character, and the update creates exactly that next line. Induction over the string makes the final line count and width exact.

**Preserve exact capacity**

The comparison must be `current_width + character_width > 100`. Equality means the character still fits, so using `>=` would create an extra line for exact fills.

#### Complexity detail

For a string of length `n`, each character causes one table lookup and constant arithmetic, giving $O(n)$ time. The width table belongs to the input, and the scan stores only two counters, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Accumulate then subtract overflow:** Add each width first and, when the total exceeds 100, increment the line count and reset to the current character; this is equivalent when the overflowing character is retained correctly.
- **Re-layout every prefix:** Simulating the string again for each growing prefix is correct but takes $O(n^2)$ time.
- **Build physical line strings:** Grouping characters into strings uses unnecessary $O(n)$ storage when only counts and widths are needed.
- **Exact width 100:** Keep the character on the current line.
- **First character:** It always occupies the initially counted first line.
- **Single character:** Return one line and that character's width.
- **Width lookup:** Index by `ord(character) - ord('a')` so the supplied alphabet-order table is respected.

</details>
