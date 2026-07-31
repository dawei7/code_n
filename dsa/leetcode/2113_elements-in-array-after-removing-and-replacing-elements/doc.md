# Elements in Array After Removing and Replacing Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2113 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/) |

## Problem Description
### Goal

An integer array `nums` changes once per minute. At minute $0$, it contains all
of its original elements. During each of the next $m$ minutes, where
$m = \lvert\texttt{nums}\rvert$, the leftmost element is removed. The array is
therefore empty after minute $m$.

During the following $m$ minutes, the removed elements are appended one at a
time in their original order. This restores `nums` completely after minute
$2m$, and the same removal-and-replacement cycle then repeats indefinitely.

Each query gives a time and an index. Report the element occupying that
zero-based index at the specified time, or $-1$ when the current array is too
short to contain the index. Queries observe the process independently; they do
not advance a shared clock.

### Function Contract
**Inputs**

- `nums`: The original nonempty integer array. Let
  $m = \lvert\texttt{nums}\rvert$.
- `queries`: A list of pairs `[time, index]`. Let
  $q = \lvert\texttt{queries}\rvert$. Each `time` is a nonnegative integer,
  and each `index` is a valid index of the original `nums`.

**Return value**

Return a list of $q$ integers in query order. For each query, the result is the
element at `index` in the array at `time`, or `-1` if that position does not
currently exist.

### Examples
**Example 1**

- Input: `nums = [0, 1, 2], queries = [[0, 2], [2, 0], [3, 2], [5, 0]]`
- Output: `[2, 2, -1, 0]`

At minute $2$, only `[2]` remains. Minute $3$ is the empty point of the cycle,
and by minute $5$ the prefix `[0, 1]` has been restored.

**Example 2**

- Input: `nums = [2], queries = [[0, 0], [1, 0], [2, 0], [3, 0]]`
- Output: `[2, -1, 2, -1]`

With one element, the array alternates between full and empty every minute.

**Example 3**

- Input: `nums = [10, 20, 30, 40], queries = [[2, 0], [2, 1], [2, 2]]`
- Output: `[30, 40, -1]`

After two removals, the current array is `[30, 40]`; its indices are relative
to that remaining suffix.
