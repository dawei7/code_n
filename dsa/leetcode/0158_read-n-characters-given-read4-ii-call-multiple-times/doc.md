# Read N Characters Given read4 II - Call Multiple Times

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 158 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Simulation, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/) |

## Problem Description
### Goal
A file is consumed through `read4`, which may fetch up to four next characters at a time, but the reader's `read` method will be called repeatedly with different limits. Each call must continue from the logical position left by all preceding calls rather than restarting the file.

For every request, copy at most `n` next characters and stop early at end of file. If `read4` fetched extra characters that the current caller did not request, retain them for later calls instead of discarding or rereading them. The native method fills a caller buffer and returns a count; the app model returns one sequential substring per requested size, including empty strings after exhaustion.

### Function Contract
**Inputs**

- `content`: app-local representation of the persistent file consumed by `read4`
- `requests`: successive maximum character counts passed to the same reader instance

**Return value**

One string per request containing the characters returned by that call. The submit-ready implementation fills each caller buffer and returns its copied count while retaining unread primitive-buffer characters between calls.

### Examples
**Example 1**

- Input: `content = "abc", requests = [1,2,1]`
- Output: `["a","bc",""]`

**Example 2**

- Input: `content = "abcdef", requests = [1,3,2]`
- Output: `["a","bcd","ef"]`

**Example 3**

- Input: `content = "abcd", requests = [0,2,2]`
- Output: `["","ab","cd"]`
