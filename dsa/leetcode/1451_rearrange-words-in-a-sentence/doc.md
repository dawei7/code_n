# Rearrange Words in a Sentence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1451 |
| Difficulty | Medium |
| Topics | String, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/rearrange-words-in-a-sentence/) |

## Problem Description
### Goal

The input is a sentence whose words are separated by exactly one space. Its
first character is uppercase, while all remaining letters are lowercase.
Rearrange the complete words into increasing order of word length. When two or
more words have the same length, preserve their relative order from the input.

Return the rearranged words as another single-space-separated sentence in the
same capitalization format: only the first letter of the new sentence is
uppercase and every other letter is lowercase. No word may be added, removed,
or internally rearranged.

### Function Contract
**Inputs**

- `text`: a non-empty sentence of length $N$, where
  $1 \le N \le 10^5$.
- `text` contains letters and single spaces between adjacent words. Its first
  letter is uppercase; all other letters are lowercase.

Let $W$ be the number of words in `text`.

**Return value**

Return a sentence containing the same $W$ words sorted by nondecreasing length,
stably preserving input order within each equal-length group. Separate words
with one space and capitalize only the first character of the result.

### Examples
**Example 1**

- Input: `text = "Leetcode is cool"`
- Output: `"Is cool leetcode"`

**Example 2**

- Input: `text = "Keep calm and code on"`
- Output: `"On and keep calm code"`
- Explanation: `"keep"`, `"calm"`, and `"code"` all have length four and
  remain in their original relative order.

**Example 3**

- Input: `text = "To be or not to be"`
- Output: `"To be or to be not"`
