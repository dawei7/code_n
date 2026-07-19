# Backspace String Compare

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 844 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/backspace-string-compare/) |

## Problem Description
### Goal
Given strings `s` and `t`, interpret each as keystrokes entered into an initially empty text editor. A lowercase letter inserts itself, while `#` is a backspace that removes the most recently entered surviving character.

Backspacing when the editor is already empty leaves it empty. Return `true` if the two editors contain equal text after every keystroke has been processed, and `false` otherwise.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters and `#`, with $1 \leq \lvert s \rvert \leq 200$.
- `t`: another string over the same alphabet, with $1 \leq \lvert t \rvert \leq 200$.

**Return value**

Return whether the two strings produce identical final text under the backspace semantics.

### Examples
**Example 1**

- Input: `s = "ab#c", t = "ad#c"`
- Output: `true`

Both editors finish with `"ac"`.

**Example 2**

- Input: `s = "ab##", t = "c#d#"`
- Output: `true`

Both editors finish empty.

**Example 3**

- Input: `s = "a#c", t = "b"`
- Output: `false`
