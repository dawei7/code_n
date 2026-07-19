# Maximum Number of Words You Can Type

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1935 |
| Difficulty | Easy |
| Topics | Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-words-you-can-type/) |

## Problem Description
### Goal
A keyboard has some malfunctioning lowercase letter keys, while every other
key works normally. The string `text` contains lowercase English words
separated by exactly one space, with no space before the first word or after
the last word.

The distinct broken keys are listed in `brokenLetters`. A word can be typed
fully only when none of its letters requires a broken key. Count and return
how many complete words in `text` remain typeable; partially typeable words do
not contribute.

### Function Contract
**Inputs**

- `text`: one or more lowercase words separated by single spaces, with total
  length $N$ satisfying $1 \le N \le 10^4$.
- `brokenLetters`: a string of $B$ distinct lowercase letters, where
  $0 \le B \le 26$.

**Return value**

- The number of words in `text` that contain no character from
  `brokenLetters`.

### Examples
**Example 1**

- Input: `text = "hello world", brokenLetters = "ad"`
- Output: `1`

Only `"hello"` avoids all broken keys.

**Example 2**

- Input: `text = "leet code", brokenLetters = "lt"`
- Output: `1`

**Example 3**

- Input: `text = "leet code", brokenLetters = "e"`
- Output: `0`
