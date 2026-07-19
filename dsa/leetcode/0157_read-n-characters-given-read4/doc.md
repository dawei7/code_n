# Read N Characters Given Read4

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 157 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/read-n-characters-given-read4/) |

## Problem Description
### Goal
A file can be accessed only through `read4`, a supplied primitive that copies up to four next characters and reports how many it obtained. Implement one call that attempts to read at most `n` characters from the file's current position into the caller's destination.

Stop as soon as `n` characters have been copied or `read4` reveals end of file, and return the number actually copied under the native contract. Never expose characters fetched beyond the requested limit. The app-friendly form receives `content` as the file and returns the copied substring, but it must model the same sequential primitive behavior, including $n = 0$ and files shorter than four characters.

### Function Contract
**Inputs**

- `content`: app-local representation of the file consumed by `read4`
- `n`: maximum number of characters requested by this single read call

**Return value**

The characters copied during the call, stopping after `n` characters or at end of file. The submit-ready implementation instead fills LeetCode's caller-provided buffer and returns the copied count.

### Examples
**Example 1**

- Input: `content = "abc", n = 4`
- Output: `"abc"`

**Example 2**

- Input: `content = "abcde", n = 5`
- Output: `"abcde"`

**Example 3**

- Input: `content = "abcd", n = 2`
- Output: `"ab"`
