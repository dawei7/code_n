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

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Parse one encoded entry at a time**

Walk through the input string without first materializing every line. Count leading tabs to obtain the entry depth, then scan its name until the next newline while recording its length and whether it contains a dot. Under the problem's encoding, a dot identifies a file.

**Store cumulative directory prefixes by depth**

Let `prefix[depth]` be the length contributed by all ancestors of an entry at that depth, including the separators after those directories. For a directory name of length `k`, set the next depth's prefix to `prefix[depth] + k + 1`; the extra one is the slash before a descendant.

**Measure files without changing the directory stack**

A file at depth `d` has absolute length `prefix[d] + name_length`. Compare that value with the best seen so far. It does not become an ancestor, so no deeper prefix is created from it. A later shallower directory overwrites the stored prefix for its child depth, naturally discarding the old branch.

**Why each computed path has the correct ancestors**

The encoding lists an entry only after its parent branch. At the moment an entry of depth `d` is read, `prefix[d]` was last written by the most recent directory at depth $d - 1$, which is exactly its parent; all earlier components are already folded into that value. Thus every file length includes each ancestor and separator once.

#### Complexity detail

Let `n` be the encoded string length and `d` the maximum depth. Every character is examined a constant number of times, giving $O(n)$ time. The prefix array stores one integer per active depth and uses $O(d)$ space.

#### Alternatives and edge cases

- **Split into lines plus a depth map:** remains $O(n)$ time and is concise, but materializing all line substrings can use $O(n)$ auxiliary space.
- **Stack of directory names:** can track ancestry, but repeatedly joining the stack for files copies path text unnecessarily.
- **Search backward for each file's parent:** can revisit many earlier sibling entries and degrade to $O(n^2)$.
- A root-level file has no slash before its name.
- A hierarchy containing only directories returns zero.
- Sibling entries overwrite no ancestor state beyond their own deeper branch.
- Multi-level paths count exactly one slash between adjacent components.

</details>
