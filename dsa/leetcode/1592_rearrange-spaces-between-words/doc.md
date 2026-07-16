# Rearrange Spaces Between Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1592 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-spaces-between-words/) |

## Problem Description
### Goal

Given a string containing lowercase words and space characters, redistribute all existing spaces. Words are non-empty, appear in their original order, and are initially separated by at least one space; leading and trailing spaces may also be present.

Place the same number of spaces between every adjacent pair of words, maximizing that common number. If the spaces cannot be divided evenly among the gaps, put every leftover space at the end. The result must therefore have exactly the same length as the input.

The input always contains at least one word.

### Function Contract
**Inputs**

- `text`: A string of length $L$, where $1 \le L \le 100$, containing only lowercase English letters and spaces and at least one word.

**Return value**

Return the words in their original order with the maximum equal spacing between adjacent words and any remainder appended after the last word.

### Examples
**Example 1**

- Input: `text = "  this   is  a sentence "`
- Output: `"this   is   a   sentence"`

**Example 2**

- Input: `text = " practice   makes   perfect"`
- Output: `"practice   makes   perfect "`

**Example 3**

- Input: `text = "  hello"`
- Output: `"hello  "`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Separate content from whitespace**

Split `text` on whitespace to recover the words without any empty entries, and count all literal space characters in the original string. Let the counts be $W$ words and $S$ spaces. The output must retain those exact words, their order, and all $S$ spaces.

**Divide spaces among actual gaps**

When $W>1$, there are exactly $W-1$ internal gaps. Euclidean division gives

$$
S=q(W-1)+r,
$$

where $q=\lfloor S/(W-1)\rfloor$ and $0\le r<W-1$. Put exactly $q$ spaces in every gap and append the remaining $r$ spaces. No larger common gap is possible because it would require more than $S$ spaces, so this distribution is maximal.

When $W=1$, there are no internal gaps. Division by $W-1$ is undefined and no space can be placed between words, so append all $S$ spaces after the sole word.

Joining the words with the computed separator and adding the trailing remainder preserves every word and every space. Its length is the total word-character count plus $q(W-1)+r$, equal to the original length, which proves all contract conditions.

#### Complexity detail

Splitting, counting, joining, and producing the result each process or emit $O(L)$ characters, for $O(L)$ total time. The word list and returned string require $O(L)$ space.

#### Alternatives and edge cases

- **Manual one-pass tokenizer:** collect words and count spaces while scanning characters. It has the same $O(L)$ time and space bounds.
- **Repeated string copying:** append output characters by rebuilding the full prefix each time. It is correct but can take $O(L^2)$ time because earlier characters are copied repeatedly.
- **Single word:** append all spaces after it; never divide by zero.
- **No spaces:** joining leaves the already adjacent content unchanged; under the source contract this occurs only for one word.
- **Uneven division:** append the remainder only at the end, not across selected gaps.
- **Leading and trailing input spaces:** they are part of the total pool and lose their original positions.
- **Many consecutive spaces:** splitting must not create empty words.
- **Length preservation:** the output must contain exactly the input's word characters and total space count.

</details>
