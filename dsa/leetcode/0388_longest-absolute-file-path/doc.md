# Longest Absolute File Path

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 388 |
| Difficulty | Medium |
| Topics | String, Stack, Depth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-absolute-file-path/) |

## Problem Description
### Goal
Given a newline-separated textual file-system encoding, each line names one file or directory and its count of leading tab characters gives its depth. A child at depth $d + 1$ belongs beneath the nearest preceding directory at depth `d`; file names are identified by containing a dot.

Return the character length of the longest absolute root-to-file path, writing one `/` between components but not counting tabs or newline separators. Directories alone are not candidate endpoints. If no file occurs, return `0`. Several roots or branches may be represented, and path length must use the correct active ancestors for each line rather than all preceding names.

### Function Contract
**Inputs**

- `input`: the encoded hierarchy; each line is a directory or file name, and its leading-tab count is its depth

**Return value**

- Return the greatest character length of a root-to-file path when components are separated by `/`, or `0` if the hierarchy contains no file.

### Examples
**Example 1**

- Input: `input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"`
- Output: `20`

**Example 2**

- Input: `input = "a"`
- Output: `0`

**Example 3**

- Input: `input = "file.txt"`
- Output: `8`
