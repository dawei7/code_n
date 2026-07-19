# Count Common Words With One Occurrence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2085 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/count-common-words-with-one-occurrence/) |

## Problem Description

### Goal

You are given two arrays of lowercase English words, `words1` and `words2`. A word qualifies only when it occurs exactly once in `words1` and exactly once in `words2`. Merely appearing in both arrays is insufficient: a second occurrence in either array disqualifies that word.

Return the number of distinct word values that satisfy this condition. Positions do not have to match between the arrays, and the answer counts qualifying values rather than pairs of indices.

### Function Contract

**Inputs**

- `words1`: an array of between $1$ and $1000$ lowercase English strings.
- `words2`: another array of between $1$ and $1000$ lowercase English strings.
- Every word has length from $1$ through $30$.

Let $S$ be the total number of characters across both arrays:

$$
S = \sum_{w \in \texttt{words1}} \lvert w \rvert
  + \sum_{w \in \texttt{words2}} \lvert w \rvert.
$$

**Return value**

Return the number of word values whose frequency is exactly one in each array.

### Examples

**Example 1**

- Input: `words1 = ["leetcode", "is", "amazing", "as", "is"]`, `words2 = ["amazing", "leetcode", "is"]`
- Output: `2`
- Explanation: `"leetcode"` and `"amazing"` occur once in each array. `"is"` is repeated in `words1`, while `"as"` is absent from `words2`.

**Example 2**

- Input: `words1 = ["b", "bb", "bbb"]`, `words2 = ["a", "aa", "aaa"]`
- Output: `0`
- Explanation: No word occurs in both arrays.

**Example 3**

- Input: `words1 = ["a", "ab"]`, `words2 = ["a", "a", "a", "ab"]`
- Output: `1`
- Explanation: Only `"ab"` occurs exactly once in both arrays.

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Why membership alone loses necessary information**

A set can reveal whether a word appears in both arrays, but it erases multiplicity. The condition distinguishes frequency one from frequency two or more, so retain a separate frequency count for each word in each array.

**Counting before comparing**

Scan `words1` into one frequency map and `words2` into another. Then inspect the keys from either one map. A word contributes one precisely when both stored counts equal $1$. Iterating one map is sufficient: a word absent from the other map has count zero there and therefore cannot qualify.

**Why every qualifying value is counted exactly once**

Each distinct word has one key in the inspected frequency map. The test accepts that key if and only if the word occurs once in both original arrays, matching the contract. Because map keys are unique, no qualifying value can contribute more than once, regardless of its positions in the inputs.

#### Complexity detail

Building and querying hash maps processes the characters used to hash the input strings, for expected time $O(S)$. The maps can retain every distinct word and its characters, so their space usage is $O(S)$. The final pass over distinct keys is bounded by the number of input words and therefore by $S$, since every word is nonempty.

#### Alternatives and edge cases

- **Sort both arrays:** Sorting exposes equal-value runs whose lengths can be compared, but it costs $O(S \log N)$ comparison work in a model with $N$ words and also requires careful two-pointer handling.
- **Repeated array counts:** Calling a linear count operation for every candidate is correct but can rescan both arrays for every word, producing quadratic behavior.
- **Set intersection:** Intersecting sets detects common values but incorrectly includes a word repeated in either input.
- A word repeated in only one array is disqualified even if it occurs exactly once in the other.
- Identical word positions are irrelevant; only the two independent frequencies matter.
- The two arrays may have no values in common, in which case the answer is zero.

</details>
