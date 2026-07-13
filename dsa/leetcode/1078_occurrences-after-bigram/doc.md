# Occurrences After Bigram

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1078 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [occurrences-after-bigram](https://leetcode.com/problems/occurrences-after-bigram/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/occurrences-after-bigram/).

### Goal
Given a sentence and two words `first` and `second`, return every word that immediately follows an occurrence of the bigram `first second`.

### Function Contract
**Inputs**

- `text`: Sentence made of words separated by single spaces.
- `first`: First word in the bigram.
- `second`: Second word in the bigram.

**Return value**

List of words that appear directly after matching bigrams, in sentence order.

### Examples
**Example 1**

- Input: `text = "alice is a good girl she is a good student", first = "a", second = "good"`
- Output: `["girl", "student"]`

**Example 2**

- Input: `text = "we will we will rock you", first = "we", second = "will"`
- Output: `["we", "rock"]`

**Example 3**

- Input: `text = "hello world", first = "world", second = "hello"`
- Output: `[]`

---

## Solution
### Approach
Split the sentence into words. Iterate over triples of consecutive words. Whenever the first two words of a triple match `first` and `second`, append the third word to the answer.

The scan stops two words before the end because a matching bigram must have a following word to report.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of words in `text`.
- **Space Complexity**: `O(n)` for the split words and output.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
