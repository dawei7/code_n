# Reverse Prefix of Word

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2000 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-prefix-of-word/) |

## Problem Description

### Goal

Given a lowercase string `word` and a lowercase character `ch`, locate the first occurrence of `ch` in `word`. If it occurs at index $i$, reverse exactly the prefix from index $0$ through index $i$, including that occurrence, while leaving every character after $i$ in its original position and order.

If `ch` does not occur anywhere in `word`, no prefix is selected and the original string must be returned unchanged.

### Function Contract

**Inputs**

- `word`: a string of $N$ lowercase English letters, where $1 \le N \le 250$.
- `ch`: one lowercase English letter.

**Return value**

Return `word` with the prefix ending at the first occurrence of `ch` reversed, or return `word` unchanged when `ch` is absent.

### Examples

**Example 1**

- Input: `word = "abcdefd", ch = "d"`
- Output: `"dcbaefd"`
- Explanation: The first `d` is at index $3$, so `"abcd"` becomes `"dcba"`.

**Example 2**

- Input: `word = "xyxzxe", ch = "z"`
- Output: `"zxyxxe"`
- Explanation: The first `z` ends the prefix `"xyxz"`, whose reversal is `"zxyx"`.

**Example 3**

- Input: `word = "abcd", ch = "z"`
- Output: `"abcd"`
- Explanation: Since `z` is absent, the string is unchanged.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Find the boundary once.** Search `word` from left to right for `ch`. This explicitly selects the first occurrence, which matters when `ch` appears several times. If the search returns no index, the contract already determines the answer.

**Reverse only the selected region.** For a found index $i$, take the inclusive prefix `word[:i + 1]`, reverse it, and append the untouched suffix `word[i + 1:]`. These two pieces partition the original string, so no character is lost, duplicated, or moved across the prefix boundary.

The reversed prefix has exactly the required order, and the suffix is copied verbatim. Therefore, the construction satisfies both parts of the contract. An occurrence at index $0$ selects a one-character prefix and naturally leaves the string unchanged.

#### Complexity detail

Finding the first occurrence and constructing the returned $N$-character string each take $O(N)$ time. Python strings are immutable, so the slices and final result use $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Stack for the prefix:** Pushing through the first occurrence and popping into the result is also linear but requires more explicit state than direct reversal.
- **Two pointers on a character list:** Swapping inward is linear and useful in languages with mutable strings; Python still needs an $O(N)$ list and final join.
- When `ch` is absent, return the original value without reversing the whole string.
- When `ch` is the first character, reversing the one-character prefix makes no visible change.
- When `ch` occurs repeatedly, only its first occurrence defines the boundary.
- A one-character word is unchanged whether its character matches `ch` or `ch` is absent.

</details>
