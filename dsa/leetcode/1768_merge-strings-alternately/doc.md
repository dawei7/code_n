# Merge Strings Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1768 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-strings-alternately/) |

## Problem Description

### Goal

You are given two strings, `word1` and `word2`. Construct a new string by taking characters alternately, beginning with the first character of `word1`, then the first character of `word2`, and continuing in that order.

If one input is longer, alternating stops after the shorter string is exhausted. Append all remaining characters of the longer string to the end without changing their order.

Return the resulting merged string.

### Function Contract

**Inputs**

- `word1`: a nonempty string of lowercase English letters, with $1 \le A \le 100$, where $A=\lvert\texttt{word1}\rvert$.
- `word2`: a nonempty string of lowercase English letters, with $1 \le B \le 100$, where $B=\lvert\texttt{word2}\rvert$.

**Return value**

- Return the length-$(A+B)$ string formed by alternating characters from `word1` and `word2`, starting with `word1`, followed by the unconsumed suffix of the longer input.

### Examples

**Example 1**

- Input: `word1 = "abc", word2 = "pqr"`
- Output: `"apbqcr"`
- Explanation: Both strings have the same length, so every character belongs to an alternating pair.

**Example 2**

- Input: `word1 = "ab", word2 = "pqrs"`
- Output: `"apbqrs"`
- Explanation: After `"apbq"`, the remaining suffix `"rs"` from `word2` is appended.

**Example 3**

- Input: `word1 = "abcd", word2 = "pq"`
- Output: `"apbqcd"`
- Explanation: After two alternating pairs, the suffix `"cd"` from `word1` remains.

### Required Complexity

- **Time:** $O(A+B)$
- **Space:** $O(A+B)$

<details>
<summary>Approach</summary>

#### General

**Alternate through the shared prefix**

Let `shared` be the smaller input length. For every index below `shared`, append `word1[index]` and then `word2[index]` to a character buffer. This directly enforces both the alternating order and the requirement that `word1` contributes first.

**Append both possible suffixes**

At index `shared`, at least one input has no characters left. Append `word1[shared:]` and then `word2[shared:]`; one slice is empty, while the other is exactly the required leftover suffix. This avoids a separate branch for which word is longer.

**Join once after all characters are placed**

Every index below `shared` contributes one character from each word in the required order. Every later index belongs to only the longer word and retains its original order in the appended suffix. Thus each input character appears exactly once in its prescribed output position. Joining the buffer once constructs that sequence without repeatedly copying an expanding immutable string.

#### Complexity detail

The paired loop handles $2\min(A,B)$ characters, and the two suffixes contain the remaining $\lvert A-B\rvert$ characters. Joining writes the $A+B$ output characters once, so total time is $O(A+B)$. The character buffer and returned string require $O(A+B)$ space.

#### Alternatives and edge cases

- **Two independent pointers:** Advancing a pointer for each word inside one loop is equally valid, but requires two boundary checks per iteration.
- **Repeated string concatenation:** Adding one character to an immutable result repeatedly can copy the existing prefix and degrade to $O((A+B)^2)$ time.
- **`zip_longest`:** A fill sentinel can express the alternation compactly, but it must be removed carefully and adds machinery unnecessary for two short suffixes.
- **Equal lengths:** Both suffixes are empty after the alternating loop.
- **Longer `word1`:** Only `word1[shared:]` contributes trailing characters.
- **Longer `word2`:** Only `word2[shared:]` contributes trailing characters.
- **Single-character inputs:** The result still starts with the character from `word1`.
- **Repeated letters:** Characters are placed by position; equality between values does not change the ordering.

</details>
