# Find Words That Can Be Formed by Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1160 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/) |

## Problem Description

### Goal

You are given an array of strings `words` and a string `chars`. A word is good when all of its characters can be taken from `chars`, with each occurrence in `chars` used at most once while forming that word.

The available pool is considered independently for every word: using a character to test one word does not consume it for later words. Letter multiplicity still matters within a word, so forming two copies of a letter requires at least two copies in `chars`. Return the sum of the lengths of all good strings in `words`.

### Function Contract

**Inputs**

- `words`: An array containing between $1$ and $1000$ lowercase English strings, each with length from $1$ through $100$.
- `chars`: A lowercase English string with length from $1$ through $100$, representing the reusable character pool for each individual word.

Define the total number of characters inspected as

$$
S = \lvert \texttt{chars} \rvert + \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

- The sum of the lengths of all words whose per-letter requirements do not exceed the corresponding frequencies in `chars`.

### Examples

**Example 1**

- Input: `words = ["cat","bt","hat","tree"]`, `chars = "atach"`
- Output: `6`

The good strings are `"cat"` and `"hat"`, contributing $3 + 3 = 6$.

**Example 2**

- Input: `words = ["hello","world","leetcode"]`, `chars = "welldonehoneyr"`
- Output: `10`

**Example 3**

- Input: `words = ["a","aa","aaa"]`, `chars = "aa"`
- Output: `3`

### Required Complexity

- **Time:** $O(S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count the shared pool once.** Build a frequency table for the 26 lowercase letters in `chars`. This table is never mutated while testing words, which models the rule that the full pool is available again for each word.

**Measure each word's requirements.** Build another 26-letter frequency table for the current word. The word is good exactly when every required count is at most the pool's count for that letter. If this componentwise comparison succeeds, add `len(word)` to the answer; otherwise add nothing.

The test is both necessary and sufficient. Exceeding the pool count for even one letter makes construction impossible because occurrences cannot be reused within a word. When every letter count fits, assign the required occurrences of each letter to distinct matching occurrences in `chars`; the assignments for different letters cannot conflict. Processing all words independently and summing precisely the accepted lengths therefore yields the requested total.

#### Complexity detail

Counting `chars` and every word visits exactly the $S$ characters in the displayed definition, so the total time is $O(S)$. Each frequency table has 26 entries because inputs contain only lowercase English letters. That alphabet size is fixed, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Remove letters from a copied pool:** This is correct but repeatedly copying and searching strings adds avoidable work compared with direct frequency comparison.
- **Call `count` for every word character:** Repeatedly rescanning both strings can make a length-$m$ word require $O(m^2)$ work.
- **Use a set of characters:** A set loses multiplicity and would incorrectly accept a word needing two copies when `chars` contains only one.
- **Reuse a depleted pool across words:** The pool resets for each word, so several good words may all rely on the same occurrences from `chars`.
- **Exact use of the pool:** A word may use every available character and remains good; unused pool characters are also allowed.
- **Repeated candidate words:** Each array entry is evaluated and contributes its length independently, even when two entries have identical text.

</details>
