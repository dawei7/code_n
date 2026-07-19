# Check If String Is a Prefix of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1961 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/) |

## Problem Description
### Goal
Given a string `s` and an ordered array of strings `words`, determine whether
`s` is a prefix string of the array.

Specifically, `s` qualifies when there is a positive integer `k`, no larger
than the number of words, such that concatenating exactly the first `k` entries
of `words` produces `s`. The match must therefore end at a word boundary;
ending partway through the next word is not sufficient. Return whether such a
prefix exists.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $L$, where $1\le L\le1000$.
- `words`: between $1$ and $100$ nonempty lowercase English strings, each
  having length at most $20$.

**Return value**

- `True` if `s` equals the concatenation of the first `k` words for some
  positive valid `k`; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "iloveleetcode", words = ["i", "love", "leetcode", "apples"]`
- Output: `True`

**Example 2**

- Input: `s = "iloveleetcode", words = ["apples", "i", "love", "leetcode"]`
- Output: `False`

**Example 3**

- Input: `s = "abc", words = ["ab", "cd"]`
- Output: `False`

### Required Complexity
- **Time:** $O(L)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare the conceptual concatenation**

Maintain one position in `s` and visit the words in order. Compare every
character of the current word with the character at that position. A mismatch,
or another word character after all of `s` has been consumed, proves that no
later word boundary can repair the prefix.

**Accept only at a boundary**

After finishing each complete word, check whether the position equals $L$.
Only then return true. This boundary check enforces the requirement that `s`
be the concatenation of whole leading words rather than merely a character
prefix of their concatenation. If all words end before `s` is consumed, no
valid `k` exists and the result is false.

Every compared character must agree in any qualifying concatenation. When the
scan reaches a boundary at exactly $L$, the words visited so far explicitly
witness a valid positive `k`, so the method is both necessary and sufficient.

#### Complexity detail

The scan compares at most the $L$ characters of `s` plus the first character
that would exceed it, so the time is $O(L)$. It stores only the current
position and loop variables, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Build a growing concatenation:** Appending words and comparing after each
  boundary is simple, but immutable-string rebuilding can copy the accumulated
  prefix repeatedly and take $O(L^2)$ time.
- **Join every possible prefix:** This directly tests the definition but
  reconstructs overlapping content many times and uses unnecessary temporary
  storage.
- If `s` equals the first word, later words do not affect the true result.
- If `s` ends inside a word, the answer is false even when all consumed
  characters match.
- If the concatenation of every word is shorter than `s`, the answer is false.

</details>
