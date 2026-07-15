# Consecutive Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1446 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/consecutive-characters/) |

## Problem Description
### Goal

The power of a string is the greatest length among its non-empty substrings
whose characters are all identical. Such a substring must occupy consecutive
positions: equal letters separated by a different letter belong to different
runs and cannot be combined.

Given a non-empty string `s` containing only lowercase English letters,
return its power. If several runs share the maximum length, return that common
length; the particular character or substring does not need to be reported.

### Function Contract
**Inputs**

- `s`: a string of length $n$, where $1 \le n \le 500$.
- Every character of `s` is a lowercase English letter.

**Return value**

Return an integer equal to the maximum number of consecutive occurrences of
one character anywhere in `s`.

### Examples
**Example 1**

- Input: `s = "leetcode"`
- Output: `2`
- Explanation: The two consecutive `"e"` characters form a longest
  single-character substring.

**Example 2**

- Input: `s = "abbcccddddeeeeedcba"`
- Output: `5`
- Explanation: The run `"eeeee"` is longer than every other run.

**Example 3**

- Input: `s = "abcdef"`
- Output: `1`
- Explanation: Every character starts a new run, so every valid non-empty
  single-character substring has length one.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The answer is the longest contiguous run**

A substring containing only one unique character cannot cross a position
where the character changes. Therefore the string is naturally partitioned
into maximal runs of equal characters, and the required power is simply the
largest run length. It is unnecessary to construct the substrings themselves
or count how many times a letter appears outside its current run.

**Extend or restart the current run**

Start with both the current run length and the best length equal to one,
because the contract guarantees a non-empty string. Scan from the second
character onward. If `s[i] == s[i - 1]`, position `i` extends the same run, so
increment the current length. Otherwise, the previous run has ended and the
new character begins a run of length one. After either transition, update the
best length with the current length.

For example, while scanning `"abbccc"`, the current lengths are
`1, 1, 2, 1, 2, 3`. Resetting at each boundary prevents the two `"b"`
characters from contributing to the following `"c"` run, while the running
maximum retains the completed length two until the `"c"` run surpasses it.

**Why a single scan is sufficient**

After processing position `i`, the current counter is exactly the length of
the maximal equal-character suffix ending at `i`: comparison with the
immediately preceding character either extends that suffix by one or proves
that it must restart at `i`. The best counter is the maximum of these suffix
lengths over every processed endpoint. Every non-empty single-character
substring has some right endpoint and is no longer than the maximal such
suffix at that endpoint, while each recorded suffix is itself valid.
Consequently, the final best counter is precisely the string's power.

#### Complexity detail

Let $n$ be the length of `s`. The scan visits each of the $n$ characters once
and performs constant work at each position, so it takes $O(n)$ time. Only the
current run length and the best length are retained; neither storage amount
depends on $n$, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Group consecutive characters:** A grouping iterator can form each maximal
  run and take the largest group length. It is also $O(n)$, but counting a
  group may add iterator machinery and the same run state still exists
  implicitly.
- **Expand from every starting position:** For each index, scan right while
  the character remains equal. This is correct, but an all-identical string
  causes $1+2+\cdots+n=O(n^2)$ comparisons because the same suffixes are
  revisited.
- **Global frequency table:** Counting total occurrences per letter is not
  sufficient. In `"abca"`, the letter `"a"` occurs twice but its longest
  consecutive run has length one.
- **Single character:** The initialized answer of one is returned without any
  loop iterations.
- **All characters equal:** The current run grows on every step, so the answer
  reaches $n$.
- **All adjacent characters different:** Every comparison restarts the run at
  one, and the power remains one.
- **Tied longest runs:** Only their length matters, so retaining either run's
  length gives the same answer.

</details>
