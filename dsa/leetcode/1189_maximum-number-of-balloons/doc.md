# Maximum Number of Balloons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1189 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-balloons/) |

## Problem Description

### Goal

You are given a string `text` containing lowercase English letters. Its characters are the available supply for spelling the word `"balloon"`; each occurrence in `text` may be used at most once.

Determine the maximum number of complete instances of `"balloon"` that can be formed. Letters not used by that word may be ignored, while repeated letters must be supplied separately for every copy.

### Function Contract

**Inputs**

- `text`: A string of length $n$, where $1\le n\le10^4$, containing only lowercase English letters.

**Return value**

- The greatest number of complete `"balloon"` words that can be assembled from the characters of `text` without reusing a character.

### Examples

**Example 1**

- Input: `text = "nlaebolko"`
- Output: `1`

The available letters contain one complete set for `"balloon"`.

**Example 2**

- Input: `text = "loonbalxballpoon"`
- Output: `2`

**Example 3**

- Input: `text = "leetcode"`
- Output: `0`

The required letters cannot all be supplied even once.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Translate the word into resource requirements.** One copy of `"balloon"` consumes one `b`, one `a`, two `l` characters, two `o` characters, and one `n`. Count the occurrences of every character in `text`. Other letters never constrain the result and can be left unused.

**Measure how many copies each letter can support.** The counts of `b`, `a`, and `n` directly give their respective copy limits. Because each word needs two `l` characters and two `o` characters, their limits are `count["l"] // 2` and `count["o"] // 2`. The smallest of these five limits is attainable: reserving that many copies never asks for more of any required letter than is available. It is also an upper bound, because producing one additional word would exceed at least one limiting supply. Therefore that minimum is exactly the answer.

#### Complexity detail

The single scan of the $n$ input characters takes $O(n)$ time, and evaluating the five resource limits takes constant time. Since `text` uses a fixed alphabet of 26 lowercase English letters, the frequency table occupies $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Repeated word removal:** Searching for and deleting one set of letters at a time is correct, but repeated searches and shifts can require $O(n^2)$ time.
- **Sort and group:** Sorting `text` makes equal letters adjacent, but costs $O(n\log n)$ time when direct counting is sufficient.
- **Missing required letter:** If any of `b`, `a`, `l`, `o`, or `n` is absent, its copy limit is zero and so is the answer.
- **Doubled requirements:** A single `l` or a single `o` cannot support a word; integer division correctly accounts for both repeated letters.
- **Surplus and irrelevant characters:** Extra required letters and letters outside `"balloon"` do not increase the result once another required letter is limiting.
- **Character ownership:** Every input occurrence contributes to at most one output word, which is exactly what the frequency subtraction implicit in the ratios enforces.

</details>
