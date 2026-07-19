# Find Duplicate File in System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 609 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/find-duplicate-file-in-system/) |

## Problem Description
### Goal
Given a list `paths` of directory-information strings, parse every described file. Each string begins with a directory path followed by one or more records of the form `fileName(content)`, separated by spaces; combine the directory and file name to obtain that file's full path.

Group full paths by exact file content and return one group for every set of at least two files that have the same content. Omit files whose content is unique. The groups and the paths inside each group may be returned in any order, and files with equal names but different directories are distinct paths.

### Function Contract
**Inputs**

- `paths`: a list of directory descriptions. Each description starts with a directory path and is followed by one or more `name(content)` file records separated by spaces.

**Return value**

- A list containing one group of full file paths for each content value that occurs at least twice
- The groups and the paths within each group may be returned in any order
- Files whose content is unique are omitted

### Examples
**Example 1**

- Input: `paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]`
- Output: `[["root/a/1.txt", "root/c/3.txt"], ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"]]`

**Example 2**

- Input: `paths = ["data a.txt(red) b.txt(blue)", "archive c.txt(green)"]`
- Output: `[]`
