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

### Required Complexity

- **Time:** $O(W+F\log F)$
- **Space:** $O(F+U)$

<details>
<summary>Approach</summary>

#### General

**Index every feature before reading responses**

Create maps from each feature to its original index and to an initial popularity count of zero. Hash lookup then distinguishes exact feature words from unrelated tokens such as `"lock"` and `"locker"` in constant expected time.

**Deduplicate within each response**

Split one response into words and convert those words to a set. Visit each distinct word once; if it is a feature, increment that feature's count. The set enforces the definition that one response contributes at most one vote to a feature, regardless of repetition.

**Sort with the complete ranking key**

Sort the feature array using the pair `(-popularity, original_index)`. Negating the count places more popular features first, while the increasing original index implements the required stable tie rule explicitly rather than depending on hash-map iteration order.

Every count is incremented once for exactly those responses whose word set contains the feature, so it equals the stated popularity. The sorting key orders unequal counts descending and equal counts by their original positions. Consequently, the returned permutation satisfies both ranking rules and includes every feature once.

#### Complexity detail

Splitting and deduplicating all responses examines $W$ word occurrences in $O(W)$ expected time. Sorting $F$ features takes $O(F\log F)$ time, for $O(W+F\log F)$ total. The feature maps use $O(F)$ space, and the temporary set for one response uses at most $O(U)$ space.

#### Alternatives and edge cases

- **Scan every response for every feature:** This is correct but can take $O(FW)$ time and repeatedly tokenize the same text.
- **Count raw word occurrences:** A global frequency counter is incorrect because repeated mentions within one response must count only once.
- **Stable sort by count alone:** This works in languages guaranteeing stable sorting, but an explicit original index makes the tie contract portable and visible.
- **Repeated mention in one response:** It contributes one popularity point, not the repetition count.
- **Exact words only:** A feature is not mentioned merely because it is a substring of another response word.
- **No mentioned features:** Every count stays zero and the original feature order is returned.
- **Equal positive popularity:** Original order still breaks the tie.
- **Response with unrelated words:** Those tokens are ignored after the hash lookup.

</details>
