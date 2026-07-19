# Number of Strings That Appear as Substrings in Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1967 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/) |

## Problem Description
### Goal
Given an array of strings `patterns` and a string `word`, count how many array
entries occur as substrings of `word`. A substring is a contiguous sequence of
characters.

Each position in `patterns` is counted independently. Thus, if the same pattern
appears several times in the array and occurs in `word`, every copy
contributes one to the answer. A pattern contributes at most once regardless
of how many different occurrences it has inside `word`.

### Function Contract
**Inputs**

- `patterns`: a list of $P$ nonempty lowercase strings, where
  $1\le P\le100$ and each length is at most $100$.
- `word`: a nonempty lowercase string of length $M$, where $1\le M\le100$.
- Let $T$ be the sum of all pattern lengths and $L$ the maximum pattern
  length.

**Return value**

- The number of entries in `patterns` that occur contiguously in `word`.

### Examples
**Example 1**

- Input: `patterns = ["a", "abc", "bc", "d"], word = "abc"`
- Output: `3`

**Example 2**

- Input: `patterns = ["a", "b", "c"], word = "aaaaabbbbb"`
- Output: `2`

**Example 3**

- Input: `patterns = ["a", "a", "a"], word = "ab"`
- Output: `3`

### Required Complexity
- **Time:** $O(T+PM)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Build failure links for one pattern**

For each pattern, construct its KMP prefix table. At each pattern position, the
table records the longest proper prefix that is also a suffix of the prefix
ending there. When a comparison fails, this table identifies the longest
already-known candidate alignment instead of restarting from the beginning.

**Scan the word without retreating**

Traverse `word` once for that pattern while maintaining the number of matched
characters. On mismatch, follow prefix-table links until the current character
can extend the match or the match becomes empty. Reaching the full pattern
length proves that this array entry contributes one, so its scan may stop.

KMP examines each word character and each prefix-table link only a constant
amortized number of times. Repeating the independent test for every array
entry also naturally counts duplicate patterns separately, while stopping at
the first occurrence prevents multiple matches of one entry from being
overcounted.

#### Complexity detail

Building all prefix tables over time costs $O(T)$. Scanning the length-$M$ word
once for each of the $P$ patterns costs $O(PM)$, giving
$O(T+PM)$ total time. Only the current pattern's prefix table is retained, so
the auxiliary space is $O(L)$.

#### Alternatives and edge cases

- **Language substring operator:** This is concise and correct, but its
  algorithmic guarantees may be implementation-dependent.
- **Try every starting position:** Compare the pattern from scratch at each
  word position. Repeated near-matches can take $O(PML)$ time.
- **Aho-Corasick automaton:** Search all patterns together in one word scan.
  It can improve multi-pattern asymptotics but is substantially more complex
  for these small limits and must track duplicate multiplicities.
- A pattern longer than `word` cannot occur.
- Multiple occurrences of one pattern still contribute only one.
- Duplicate entries in `patterns` each contribute independently.

</details>
