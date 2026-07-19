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
