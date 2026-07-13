# Most Common Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 819 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-common-word/) |

## Problem Description

### Goal

You are given a paragraph containing ASCII letters, spaces, and common punctuation, together with a list of banned words. Words are maximal consecutive groups of letters: punctuation and whitespace separate them, and capitalization does not distinguish one occurrence from another.

Normalize the paragraph's words to lowercase, discard every occurrence whose normalized form is banned, and return the word that appears most often among those remaining. The input guarantees that one allowed word has a strictly greater frequency than every other allowed word, so the result is unambiguous and must be returned in lowercase.

### Function Contract

**Inputs**

- `paragraph`: ASCII letters separated by spaces and punctuation from `!?',;.`.
- `banned`: distinct lowercase words that must not be counted.

**Return value**

- The uniquely most frequent non-banned word, written in lowercase.

### Examples

**Example 1**

- Input: `paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]`
- Output: `"ball"`
- Explanation: After case folding and excluding `hit`, `ball` is the only word appearing twice.

**Example 2**

- Input: `paragraph = "a, a, a, a, b,b,b,c, c", banned = ["a"]`
- Output: `"b"`
- Explanation: Punctuation separates the words, and `b` occurs three times among the allowed words.

**Example 3**

- Input: `paragraph = "Bob. hIt, baLl", banned = ["bob","hit"]`
- Output: `"ball"`
- Explanation: Comparisons are case-insensitive, and the result is normalized to lowercase.

### Required Complexity

- **Time:** $O(p + b)$
- **Space:** $O(u + b)$

<details>
<summary>Approach</summary>

#### General

**Treat every nonletter as a word boundary**

Scan a lowercase version of the paragraph one character at a time. Accumulate consecutive letters into the current word. On punctuation, whitespace, or a sentinel appended after the paragraph, finish that word and clear the buffer. The sentinel ensures the final word is processed even when the paragraph has no trailing punctuation.

**Exclude banned words before counting**

Store the banned words in a hash set. When a token ends, ignore it if it is banned; otherwise increment its frequency in a hash map. Set lookup prevents the banned list from adding a multiplicative scan for every token.

**Maintain the winner while frequencies change**

Whenever a word's count is incremented, compare that count with the best count seen so far and update the answer when it becomes larger. The contract guarantees a unique most frequent allowed word, so no tie-breaking rule is needed. Every paragraph token is normalized and counted exactly once, and the maintained maximum therefore ends at the required word.

#### Complexity detail

Let `p` be the paragraph length, `b` the total size of the banned input, and `u` the number of distinct allowed words. Building the banned set and scanning all characters takes $O(p + b)$ expected time. The banned set, frequency map, and current token use $O(u + b)$ entries plus at most one word's characters.

#### Alternatives and edge cases

- **Regular-expression tokenization:** Extracting `[a-z]+` after lowercasing is concise and has the same asymptotic behavior, but materializes the complete token list.
- **Count then call `max`:** Building all frequencies before selecting the winner is also linear and may be clearer when streaming is unnecessary.
- **Repeated list counting:** Calling `words.count(word)` for every occurrence is correct but can take $O(w^2)$ for `w` tokens.
- **Mixed case:** Normalize before banned-set lookup and counting.
- **Adjacent punctuation:** Empty buffers between delimiters do not represent words and are ignored.
- **Final word without punctuation:** The sentinel boundary flushes it.
- **Banned frequent word:** Exclude it entirely rather than counting it and choosing the next word afterward.

</details>
