# Latest Time You Can Obtain After Replacing Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3114 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [latest-time-you-can-obtain-after-replacing-characters](https://leetcode.com/problems/latest-time-you-can-obtain-after-replacing-characters/) |

## Problem Description

### Goal

You are given a five-character string `s` that describes a time in 12-hour format. It has the form `"HH:MM"`, but any of its four digit positions may instead contain `"?"`. Valid hours range from `"00"` through `"11"`, and valid minutes range from `"00"` through `"59"`; therefore, `"00:00"` is the earliest time and `"11:59"` is the latest.

Replace every `"?"` with a decimal digit so that the completed string is a valid time and is as late as possible. Digits already present in `s` cannot be changed. The input guarantees that at least one valid completion exists, and the completed time string must be returned.

### Function Contract

**Inputs**

- `s`: A length-$5$ string in the form `"HH:MM"`. Position `2` is `":"`; every other position is a digit or `"?"`, and at least one valid completion from `"00:00"` through `"11:59"` exists.

**Return value**

- The lexicographically and chronologically latest valid 12-hour time obtainable by replacing all question marks.

### Examples

**Example 1**

- Input: `s = "1?:?4"`
- Output: `"11:54"`
- Explanation: The second hour digit can be `1`, and the largest valid minute with final digit `4` is `54`.

**Example 2**

- Input: `s = "0?:5?"`
- Output: `"09:59"`
- Explanation: The fixed leading zero permits hour `09`, while both minute positions can complete to `59`.
