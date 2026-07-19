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

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Record the unusable keys**

Place the letters from `brokenLetters` in a set. Because every broken letter
is distinct and the alphabet has only 26 letters, membership checks are
constant time and the set's maximum size is fixed.

**Evaluate complete words**

Split `text` at its single spaces. A word is typeable exactly when every one of
its letters is absent from the broken-key set. Test the letters until a broken
one is found; then reject that whole word and continue with the next word.
Count each word whose scan finishes without such a match.

Every counted word uses only functioning keys, so it can be typed fully.
Every uncounted word contains a listed broken letter, making full typing
impossible. Since the words partition all non-space characters in `text`, this
classifies every word exactly once.

#### Complexity detail

Building the broken-key set examines $B \le 26$ letters. Splitting and checking
the words examines $O(N)$ characters in total, so the time is $O(N)$. The set
contains at most 26 entries and is therefore $O(1)$ space with respect to
$N$; the language's materialized word list may use $O(N)$ implementation
storage, but a streaming scan can achieve the stated auxiliary bound.

#### Alternatives and edge cases

- **Bit mask for broken letters:** Store the 26 possible keys as bits and test
  each character's bit. This preserves the same time and fixed-space bounds.
- **Revalidate every growing prefix:** Checking the entire prefix again after
  each newly typed character is correct, but one long word causes
  $O(N^2)$ repeated character checks.
- When `brokenLetters` is empty, every word is typeable.
- A broken letter appearing anywhere in a word rejects that entire word,
  regardless of how many other letters work.
- Broken letters that never appear in `text` do not reduce the answer.
- Repeated occurrences of one broken letter still reject only the containing
  word; words are counted, not characters.
- Spaces separate words and are not keyboard letters under consideration.

</details>
