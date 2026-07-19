# Check Whether Two Strings are Almost Equivalent

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2068 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/) |

## Problem Description

### Goal

The frequency of a letter in a string is its number of occurrences. Two equal-length lowercase English strings are almost equivalent when, for every letter from `a` through `z`, the absolute difference between its two frequencies is at most $3$.

Given `word1` and `word2`, return whether they are almost equivalent. A difference of exactly $3$ is allowed; any single letter whose frequency differs by $4$ or more makes the result false.

### Function Contract

**Inputs**

- `word1`: a lowercase English string of length $n$.
- `word2`: another lowercase English string of the same length, where $1 \le n \le 100$.

**Return value**

- Return `true` if every letter's two frequencies differ by at most $3$; otherwise return `false`.

### Examples

**Example 1**

- Input: `word1 = "aaaa", word2 = "bccb"`
- Output: `false`
- Explanation: The frequency of `a` differs by $4$, exceeding the limit.

**Example 2**

- Input: `word1 = "abcdeef", word2 = "abaaacc"`
- Output: `true`
- Explanation: The largest frequency difference is $3$, which is allowed.

**Example 3**

- Input: `word1 = "cccddabba", word2 = "babababab"`
- Output: `true`
- Explanation: Every letter's frequency difference is at most $3$.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Accumulate one signed difference per letter**

Create 26 counters initialized to zero. Scan the strings together. For each position, increment the counter belonging to the character from `word1` and decrement the counter belonging to the character from `word2`. After the scan, a counter equals that letter's first frequency minus its second frequency.

**Check the inclusive threshold**

Inspect all 26 counters and return true only when every absolute value is at most $3$. The counters capture all occurrences because each character in each string changes exactly one corresponding entry. Thus passing every threshold is precisely the definition of almost equivalence, while any failed entry identifies a disqualifying letter.

#### Complexity detail

The paired scan processes the $n$ positions once, and checking 26 counters is constant work, for $O(n)$ time. The fixed-size frequency-difference array uses $O(26)=O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Two frequency maps:** Count each string separately and compare their entries; this is also $O(n)$ but stores two sets of counters.
- **Recount for each occurrence:** Repeatedly scanning both strings for every encountered character is correct but can take $O(n^2)$ time.
- A difference of exactly $3$ is valid; the comparison is inclusive.
- Letters absent from both strings have difference zero and require no special handling.
- Equal string length does not guarantee almost equivalence because the excess counts may belong to different letters.
- Identical strings are always almost equivalent.

</details>
