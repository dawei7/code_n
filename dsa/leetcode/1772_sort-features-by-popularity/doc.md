# Sort Features by Popularity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1772 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-features-by-popularity/) |

## Problem Description

### Goal

An ordered array `features` lists distinct product features, and each string in `responses` contains space-separated words from one customer response.

A feature's popularity is the number of responses that mention it at least once. Repeating the same feature several times in one response still contributes only one mention.

Return all features in descending popularity. When two features have equal popularity, preserve their relative order from the original `features` array.

### Function Contract

**Inputs**

- `features`: an ordered array of distinct lowercase feature words.
- `responses`: an array of lowercase, space-separated response strings.

Let $F=\lvert\texttt{features}\rvert$, let $W$ be the total number of response-word occurrences, and let $U$ be the maximum number of distinct words in one response.

**Return value**

- Return every input feature exactly once, ordered by decreasing number of responses containing that feature.
- Break popularity ties by the feature's original index.

### Examples

**Example 1**

- Input: `features = ["cooler","lock","touch"]`, with responses `"i like cooler cooler"`, `"lock touch cool"`, and `"locker like touch"`.
- Output: `["touch","cooler","lock"]`
- Explanation: `"touch"` appears in two responses. `"cooler"` and `"lock"` each appear in one, so their original order breaks the tie.

**Example 2**

- Input: `features = ["a","aa","b","c"]`, with responses `"a"`, `"a aa"`, `"a a a a a"`, and `"b a"`.
- Output: `["a","aa","b","c"]`
- Explanation: Repeated `"a"` words in one response count once; `"aa"` and `"b"` tie and retain their input order.

**Example 3**

- Input: `features = ["z","a","m"]`, with responses that mention none of them.
- Output: `["z","a","m"]`
- Explanation: All popularity counts are zero, so the original order is unchanged.
