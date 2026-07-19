# Truncate Sentence

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/truncate-sentence/) |
| Frontend ID | 1816 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A sentence is a sequence of words separated by exactly one space. It has no space before its first word or after its last word, and every word contains only uppercase or lowercase English letters. Thus, spaces are precisely the boundaries between consecutive words; punctuation and repeated separators do not occur.

Given such a sentence `s` and an integer `k`, retain the first `k` words in their original order and discard every later word. The value of `k` is at least 1 and does not exceed the number of words in `s`. Return the resulting sentence, preserving the single spaces between the retained words.

### Function Contract

**Inputs**

- `s`: a valid sentence with $1 \le \lvert s \rvert \le 500$, made only of English letters and single spaces, with no leading or trailing space.
- `k`: an integer from 1 through the number of words in `s`.
- Let $n = \lvert s \rvert$.

**Return value**

- Return the prefix of `s` containing exactly its first `k` words, without a trailing space.

### Examples

**Example 1**

- Input: `s = "Hello how are you Contestant", k = 4`
- Output: `"Hello how are you"`

The fourth word ends before `"Contestant"`, so that later word and its preceding separator are excluded.

**Example 2**

- Input: `s = "What is the solution to this problem", k = 4`
- Output: `"What is the solution"`

**Example 3**

- Input: `s = "chopper is not a tanuki", k = 5`
- Output: `"chopper is not a tanuki"`

Here `k` equals the sentence's word count, so the complete sentence remains.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Locate the boundary after the retained prefix**

Because every separator is exactly one space, the first word ends at the first space, the second at the second space, and so on. Scan `s` from left to right while counting spaces. When the count reaches `k`, the current space is immediately after the `k`th word. Return the slice before that index so neither the separator nor any later word is included.

**Handle a prefix that is the whole sentence**

A sentence with $w$ words contains exactly $w-1$ spaces. If `k` equals $w$, the scan never encounters a `k`th space. In that case every word is retained, so return `s` unchanged.

**Why the scan returns exactly the requested words**

Before the `k`th separator there are exactly `k` non-empty word regions: one before the first separator and one between every adjacent pair of separators. The input guarantees that no empty regions arise from consecutive spaces. Slicing at that separator therefore returns precisely the first `k` words. If that separator does not exist, validity of `k` means all words were requested.

#### Complexity detail

The scan examines at most the $n$ characters of `s` once, and constructing the returned prefix also takes at most $O(n)$ time. The returned string can contain $\Theta(n)$ characters, so total output-inclusive space is $O(n)$; the counter and index require only $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Split and join:** `s.split()` followed by joining the first `k` entries is concise and remains $O(n)$, but it constructs a list and separate word strings that the direct scan does not need.
- **Restart the scan for each boundary:** Finding the first boundary, then rescanning from the beginning for the second, and so on is correct, but it can examine the same prefix repeatedly and take $O(n^2)$ time.
- **Single-word sentence:** The scan finds no spaces and returns the only word, necessarily with `k = 1`.
- **Keep one word:** The first space ends the answer; if there is no space, the entire one-word sentence is returned.
- **Keep every word:** No `k`th space exists, so return `s` without creating a trailing separator.
- **Letter case:** Uppercase and lowercase letters are copied verbatim; they do not affect word boundaries.

</details>
