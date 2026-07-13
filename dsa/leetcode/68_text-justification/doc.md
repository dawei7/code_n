# Text Justification

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 68 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/text-justification/) |

## Problem Description
### Goal
You are given words in their required order and an exact line width. Greedily place as many consecutive words as fit on each line when separated by at least one space; every word is nonempty and no word exceeds the width.

Return lines of exactly `max_width` characters. For each nonfinal line with several words, distribute spaces as evenly as possible, putting any indivisible extras in the earlier gaps. A nonfinal one-word line is padded on the right. The final line uses single spaces between words and trailing spaces for the remaining width.

### Function Contract
**Inputs**

- `words`: a nonempty list of nonempty words, each no wider than the line
- `max_width`: the exact width of every returned line

**Return value**

A `List[str]` containing the justified lines in original word order.

### Examples
**Example 1**

- Input: `words = ["This","is","an","example","of","text","justification."], max_width = 16`
- Output: `["This    is    an", "example  of text", "justification.  "]`

**Example 2**

- Input: `words = ["What","must","be","acknowledgment","shall","be"], max_width = 16`
- Output: `["What   must   be", "acknowledgment  ", "shall be        "]`

**Example 3**

- Input: `words = ["word"], max_width = 8`
- Output: `["word    "]`

### Required Complexity

- **Time:** $O(C)$
- **Space:** $O(C)$

<details>
<summary>Approach</summary>

#### General

**Pack the longest consecutive word prefix that fits**

Starting at the next unused word, keep adding words while their total letter count plus one mandatory space for each existing gap remains at most `max_width`. When considering another word, the fit test must include the new gap before that word. Stop immediately before the first word that would exceed the width.

This packing decision is independent of later space distribution. The problem explicitly requires greedy line breaks, so a shorter aesthetically balanced line is not an alternative.

**Full justification is quotient-and-remainder distribution**

For a nonfinal line with at least two words, let `spaces = max_width - total_letters` and `gaps = word_count - 1`. Integer division gives:

```text
base, extra = divmod(spaces, gaps)
```

Every gap receives `base` spaces, and the first `extra` gaps receive one additional space. This uses every required space, keeps gap sizes within one of each other, and places larger gaps on the left exactly as required.

**Last and single-word lines follow a different rule**

The final line is joined with one space per gap and padded entirely on the right. A one-word line has no internal gap to divide by and uses the same right-padding form even when it is not final. Both cases must produce exactly `max_width` characters.

**Words are consumed once and never reordered**

Before building a line, all earlier words appear exactly once in correctly justified lines. The selected window is the longest next prefix that fits. Formatting changes only spaces between or after those words, so it consumes precisely that window without changing word order or content.

**Trace even and uneven gap distributions**

For `This is an` at width 16, the words use 8 characters, leaving 8 spaces across two gaps. Both receive 4, producing `This    is    an`. For `example of text`, the 13 letters leave 3 spaces across two gaps: quotient 1 and remainder 1 produce gaps of 2 and 1, yielding `example  of text`.

**Maximal packing and exact space division satisfy each line**

The packing loop adds the next word whenever it can still fit with the mandatory one-space gaps. Stopping means that word would exceed the width, so the chosen consecutive group is maximal as required.

For a normal line, dividing remaining spaces by the gap count assigns every gap the common quotient and the first remainder-many gaps one extra space. All spaces are used, gap sizes differ by at most one, and larger gaps occur leftmost. The final-line branch instead uses single internal spaces and pads only the right edge. Each emitted line therefore has exact width and the specified alignment.

#### Complexity detail

Let `C` include all word characters and emitted spaces. Each word is selected and emitted once, so time is $O(C)$. The returned lines occupy $O(C)$ space; per-line temporary pieces are bounded by that line's output.

#### Alternatives and edge cases

- **Repeatedly concatenate immutable strings one character at a time:** can introduce quadratic copying within long lines.
- **Center or right justification:** does not satisfy the specified gap distribution.
- **Dynamic line breaking:** is useful for typographic raggedness optimization but conflicts with this problem's mandatory greedy packing.
- A word exactly as wide as the line forms a one-word line with no padding. Every input word is guaranteed to fit individually.
- Avoid dividing by `word_count - 1` before checking the one-word case.

</details>
