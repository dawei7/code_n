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

### Required Complexity

- **Time:** $O(T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Separate the directory from its file records**

Split each description on spaces. The first token is the directory; every remaining token has the form `name(content)`. The input grammar excludes spaces from those components, so each file remains one token.

**Use content as the grouping key**

For a file token, locate its opening parenthesis. The prefix is the filename and the text between the parentheses is the complete content. Join the directory and filename with `/`, then append that full path to a hash-map bucket keyed by the exact content string.

**Why filtering buckets produces exactly the duplicates**

Every input file is inserted once into the bucket for its own content. Therefore two paths occupy the same bucket if and only if their supplied contents are equal. A bucket of size one represents a unique file and must be discarded; every bucket of size at least two is one complete duplicate group. Since content keys partition the files, no path can appear in the wrong group or in two groups.

#### Complexity detail

Let `T` be the total number of characters across all directory descriptions. Splitting, locating delimiters, extracting fields, hashing content, and constructing full paths process $O(T)$ characters in total, so expected time is $O(T)$. The content keys, full paths, and output buckets together store at most $O(T)$ characters.

#### Alternatives and edge cases

- **Sort content-path pairs:** parsing all files and sorting by content also exposes adjacent equal runs, but costs $O(T + F \log F)$ time for `F` files.
- **Compare every pair of files:** direct content comparisons are correct but require $O(F^2)$ comparisons before accounting for content length.
- **Filesystem hashing:** for real files too large to hold in memory, size and a cryptographic digest can identify candidates, followed by exact byte comparison to guard against collisions; this problem already supplies the complete contents.
- A content value appearing three or more times forms one group, not several pairs.
- Identical filenames in different directories are distinct paths and can still be duplicates.
- Equal prefixes do not matter: contents must match in full.
- Files with unique contents do not appear in the result.
- Output order is unspecified at both the group and path levels.

</details>
