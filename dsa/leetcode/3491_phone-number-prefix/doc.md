# Phone Number Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3491 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String, Trie, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/phone-number-prefix/) |

## Problem Description

### Goal

A collection of strings represents phone numbers. Each string consists only of decimal digits, and its leading zeros are meaningful characters rather than numeric padding. One phone number is a prefix of another when every character of the first number matches the opening characters of the second number. Equal strings also make two distinct array entries prefixes of one another.

Determine whether the collection is prefix-free: return `true` only when no phone number is a prefix of any other phone number in the array. Otherwise, including when the same phone number appears more than once, return `false`.

### Function Contract

**Inputs**

- `numbers`: An array of digit strings representing phone numbers.

The array contains between $2$ and $50$ strings. Every string has length from $1$ through $50$ and contains only characters from `'0'` through `'9'`.

Let

$$
S=\sum_{x\in\texttt{numbers}}\lvert x\rvert
$$

be the total number of input characters.

**Return value**

Return `true` if the array is prefix-free; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `numbers = ["1", "2", "4", "3"]`
- **Output:** `true`
- **Explanation:** Every number differs at its first character, so none prefixes another.

#### Example 2

- **Input:** `numbers = ["001", "007", "15", "00153"]`
- **Output:** `false`
- **Explanation:** `"001"` is the opening part of `"00153"`.
