# Short Encoding of Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 820 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/short-encoding-of-words/) |

## Problem Description

### Goal

A valid encoding of `words` uses a reference string `s` ending in `#` and one starting index for every input word. Reading from that index up to, but not including, the next `#` must produce the corresponding word.

Return the length of the shortest possible reference string. One stored word can represent another when the latter is its suffix, because both can end at the same delimiter; duplicate input words may also share one occurrence. Every word that is not a suffix of another distinct word must appear explicitly with its own trailing `#`.

### Function Contract

**Inputs**

- `words`: a nonempty list of nonempty lowercase English words.

Let

$$
S = \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

Then $S$ is the total number of input characters.

**Return value**

- The minimum possible length of a valid `#`-delimited reference string encoding every input occurrence

### Examples

**Example 1**

- Input: `words = ["time", "me", "bell"]`
- Output: `10`
- Explanation: `"time#bell#"` stores `"me"` as a suffix of `"time"`.

**Example 2**

- Input: `words = ["t"]`
- Output: `2`
- Explanation: The shortest reference string is `"t#"`.

**Example 3**

- Input: `words = ["time", "time", "me"]`
- Output: `5`
- Explanation: Both duplicate words and the suffix `"me"` share `"time#"`.
