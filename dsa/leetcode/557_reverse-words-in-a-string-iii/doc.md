# Reverse Words in a String III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 557 |
| Difficulty | Easy |
| Topics | Two Pointers, String |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-words-in-a-string-iii/) |

## Problem Description
### Goal
Given a string containing at least one word, with words separated by exactly one space, reverse the character sequence inside each individual word. Keep the words in their original left-to-right order.

Return the transformed string with the single spaces between words unchanged. Characters cannot move from one word to another, and reversing one word has no effect on its neighbors. A one-character word remains unchanged; the task reverses word contents rather than reversing the word order or the complete string.

### Function Contract
**Inputs**

- `s`: a string of words separated by single spaces, with no leading or trailing space

**Return value**

- A string with each word reversed in place

### Examples
**Example 1**

- Input: `s = "Let's take LeetCode contest"`
- Output: `"s'teL ekat edoCteeL tsetnoc"`

**Example 2**

- Input: `s = "Mr Ding"`
- Output: `"rM gniD"`

**Example 3**

- Input: `s = "a"`
- Output: `"a"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Treat each word as an independent segment**

Split the input at spaces. The contract guarantees one space between adjacent words and no outer spaces, so this produces exactly the original word sequence without ambiguous empty segments.

**Reverse characters, not word positions**

For each segment, take its characters in reverse order. The list of segments remains in its original order, which distinguishes this task from reversing the order of words.

**Reassemble with the same separator**

Join the reversed segments with one space. This restores every separator while leaving punctuation or capitalization attached to the word characters they belong to.

**Why every output position is correct**

Each non-space character belongs to exactly one word and is placed at the mirrored offset within that same word. Each space is restored between the same pair of word positions. Therefore all words keep their order and boundaries, while every word's internal character order is reversed exactly once.

#### Complexity detail

Across all words, slicing visits each of the `n` input characters once and joining writes `n` output characters, so time is $O(n)$. The reversed word strings and returned string occupy $O(n)$ space.

#### Alternatives and edge cases

- **Two pointers on a mutable character array:** reverses each word range in $O(n)$ time and uses $O(n)$ storage in languages where strings are immutable.
- **Prepend one character at a time:** is correct but repeatedly copies the growing word and can take $O(n^2)$ time for one long word.
- **Reverse the complete string twice:** can first reverse everything and then restore word order, but is less direct for this contract.
- **Single-character word:** is unchanged.
- **Punctuation:** is an ordinary character and reverses with the rest of its word.
- **Capital letters:** retain their identity but move to the mirrored word position.
- **Separators:** word order and the single spaces between words must remain unchanged.

</details>
