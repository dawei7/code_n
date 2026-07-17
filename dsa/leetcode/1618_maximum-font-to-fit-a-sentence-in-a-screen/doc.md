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

### Required Complexity
- **Time:** $O(n+\sigma\log f)$
- **Space:** $O(\sigma)$

<details>
<summary>Approach</summary>

#### General

**Compress repeated metric queries.** Count how often each character appears in `text`. For a candidate font, request each distinct character width once, multiply it by that character's frequency, and sum the products. This produces exactly the sentence width while using at most $\sigma$ width queries instead of one query per character. Reject immediately when the font height exceeds `h`.

**Exploit monotone fit across the available sizes.** Both height and every character width are non-decreasing with font size. Therefore the predicate “this font fits within `w` and `h`” is true for an initial prefix of `fonts` and false thereafter. Binary-search that boundary. When the middle font fits, record it and search to the right; otherwise search to the left.

At termination, every font to the right of the recorded answer has been excluded directly or by monotonicity, while the recorded font passed both exact dimension checks. If no middle font ever fits, the initialized answer `-1` correctly represents an empty feasible prefix.

#### Complexity detail

Building the frequency map takes $O(n)$ time and $O(\sigma)$ space. Binary search tests $O(\log f)$ fonts, with one height query and at most $\sigma$ width queries per test, for $O(n+\sigma\log f)$ total time. The interface-call count is also $O((\sigma+1)\log f)$.

#### Alternatives and edge cases

- **Scan fonts from smallest to largest:** Reusing character frequencies gives $O(n+\sigma f)$ time, but ignores the monotone boundary and may query every font.
- **Query every character occurrence:** Width summation without frequency compression takes $O(n\log f)$ calls and can exceed the interactive query budget on repeated text.
- **Scan fonts from largest downward:** This may find the answer early, but in the worst case no font fits and all $f$ sizes are tested.
- A font whose dimensions equal `w` or `h` still fits because both limits are inclusive.
- A height failure is sufficient to reject a font without making any width queries.
- The answer is an available font value, not its index in `fonts`.
- If the smallest font fails, monotonicity proves that the correct result is `-1`.

</details>
