# Camelcase Matching

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1023 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Trie, String Matching |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/camelcase-matching/) |

## Problem Description

### Goal

You are given an array of query strings `queries` and a string `pattern`. A query matches when it can be formed by inserting zero or more lowercase English letters anywhere into `pattern`.

Return a boolean array aligned with the queries, where each value reports whether that query matches. Every pattern character must appear in order, and any query character not used to match the pattern must be lowercase. Consequently, an additional uppercase character makes a query invalid.

### Function Contract

**Inputs**

- `queries`: an array of $Q$ nonempty English-letter strings, where $1\le Q\le100$ and every query has length at most `100`.
- `pattern`: a nonempty English-letter string of length $P$, where $1\le P\le100$.

Define the total query length as

$$
S=\sum_{q\in\texttt{queries}}\lvert q\rvert.
$$

**Return value**

- A $Q$-element boolean array indicating whether each query can be produced from `pattern` by inserting only lowercase letters.

### Examples

**Example 1**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FB"`
- Output: `[True, False, True, True, False]`

**Example 2**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBa"`
- Output: `[True, False, True, False, False]`

**Example 3**

- Input: `queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], pattern = "FoBaT"`
- Output: `[False, True, False, False, False]`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Advance through matching pattern characters:** For one query, keep a pointer to the next unmatched pattern character. Scan the query left to right; when the current character equals that pattern character, advance the pointer.

**Reject unmatched uppercase letters:** If a query character does not match the next pattern character, it can only be an inserted character. Insertions are restricted to lowercase letters, so return false immediately when such a character is uppercase. Unmatched lowercase letters are skipped.

**Require the complete pattern:** After scanning the query, return true only if the pointer reached the end of `pattern`. This rejects queries that contain no forbidden uppercase insertion but still omit a required trailing pattern character.

The pointer matches pattern characters in their original order. Every skipped character is verified lowercase, so a successful scan gives exactly a valid insertion sequence; any valid insertion sequence makes the same scan succeed.

#### Complexity detail

Each query character is examined once, so all queries take $O(S)$ time. A pattern index is the only per-query state, giving $O(1)$ auxiliary space excluding the required boolean output.

#### Alternatives and edge cases

- **Dynamic programming:** Matching every query prefix against every pattern prefix is correct but costs $O(\lvert q\rvert P)$ time per query and additional space.
- **Remove lowercase letters:** Comparing uppercase skeletons is necessary but not sufficient when the pattern itself contains lowercase characters.
- **Exact query:** A query identical to `pattern` matches with no insertions.
- **Extra uppercase character:** It cannot be inserted and makes the query fail.
- **Missing pattern suffix:** Lowercase-only leftovers do not compensate for an unmatched pattern character.

</details>
