# Using a Robot to Print the Lexicographically Smallest String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2434 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/) |

## Problem Description

### Goal

A robot receives a lowercase string `s` and starts with an empty temporary string `t`. At each step, it may remove the first character of `s` and append that character to `t`, or remove the last character of `t` and write it onto the output paper.

Continue until both `s` and `t` are empty. Every input character must therefore move through the temporary string before being printed, while `t` behaves as a stack. Choose the operation order that makes the complete written string lexicographically smallest, and return that string.

### Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters.

Its length $n$ satisfies $1 \le n \le 10^5$.

**Return value**

- The lexicographically smallest string the robot can write using valid operations.

### Examples

#### Example 1

- **Input:** `s = "zza"`
- **Output:** `"azz"`

Push all three characters into `t`, then pop them in reverse order.

#### Example 2

- **Input:** `s = "bac"`
- **Output:** `"abc"`

After pushing `"ba"`, pop both characters to write `"ab"`, then move and print `"c"`.

#### Example 3

- **Input:** `s = "bdda"`
- **Output:** `"addb"`

The smallest character is reached before printing the stack in the best available order.
