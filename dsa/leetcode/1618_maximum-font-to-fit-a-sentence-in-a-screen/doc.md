# Maximum Font to Fit a Sentence in a Screen

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1618 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-font-to-fit-a-sentence-in-a-screen/) |

## Problem Description
### Goal
A lowercase sentence `text` must be rendered on a screen with maximum width `w` and maximum height `h`. The available font sizes are supplied in strictly increasing order. The interactive `FontInfo` interface reports the rendered width of one character at a chosen font and the rendered height of that font.

Choose the largest available font for which the entire sentence fits on one line: its height must not exceed `h`, and the sum of its character widths must not exceed `w`. Font metrics are non-decreasing as font size increases, so once a size is too large, every later available size is also too large. Return `-1` if even the smallest available font does not fit.

### Function Contract
**Inputs**

- `text`: a nonempty string of $n$ lowercase English letters.
- `w` and `h`: the screen's positive width and height limits.
- `fonts`: a nonempty strictly increasing list of $f$ available positive font sizes.
- `fontInfo`: a read-only interface with `getWidth(fontSize, ch)` and `getHeight(fontSize)` methods. Widths and heights are non-decreasing with font size.
- Let $\sigma$ be the number of distinct characters in `text`, so $1 \le \sigma \le 26$.

**Return value**

Return the largest value in `fonts` whose rendered sentence width is at most `w` and whose height is at most `h`; return `-1` if no available font fits.

### Examples
**Example 1**

- Input: `text = "helloworld", w = 80, h = 20, fonts = [6,8,10,12,14,16,18,24,36]`
- Output: `6`

**Example 2**

- Input: `text = "leetcode", w = 1000, h = 50, fonts = [1,2,4]`
- Output: `4`

**Example 3**

- Input: `text = "easyquestion", w = 100, h = 100, fonts = [10,15,20,25]`
- Output: `-1`
