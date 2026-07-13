# Tenth Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 195 |
| Difficulty | Easy |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/tenth-line/) |

## Problem Description
### Goal
Given the text file `file.txt`, count its lines from the beginning using one-based positions. Locate the line at position ten, where the first physical line is position one regardless of its text contents.

Write exactly the tenth line to standard output when it exists, preserving that line's content rather than splitting it into words. If the file contains fewer than ten lines, produce no output and no placeholder or error message. Earlier and later lines must not be printed. Keep the solution in the source-native Bash file-and-stdout form instead of converting it to a callable function.

### Function Contract
**Inputs**

- `file.txt`: a text file with zero or more lines

**Return value**

Write exactly the tenth line to stdout, or write nothing when the file has fewer than ten lines.

### Examples
**Example 1**

- File has lines `Line 1` through `Line 12`
- Output: `Line 10`

**Example 2**

- File has exactly ten lines
- Output: its final line

**Example 3**

- File has nine lines
- Output: nothing

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

`sed` can address a command to one exact input line. The `-n` flag suppresses its default behavior of printing every line, while `10p` says to print only line number ten:

```bash
sed -n '10p' file.txt
```

If the stream reaches line ten, `sed` prints that line exactly once, including a blank line if the tenth record is empty. If end-of-file arrives earlier, the numeric address is never reached and stdout remains empty.

The distinction between the tenth line and the first ten lines matters. A command such as `head -n 10` alone returns too much data; it would need a second stage to select the last line. A single addressed stream command states the contract directly.

Suppressed default output ensures no unaddressed line can be emitted. The numeric address `10` matches exactly the tenth input record, and `p` emits that record without altering its contents. Therefore a present tenth line is the sole output, while a file with fewer than ten lines produces none.

#### Complexity detail

The shown command scans the input stream and uses constant state, giving $O(n)$ worst-case time in the file length and $O(1)$ auxiliary space. A variant such as `sed -n '10{p;q;}'` can stop immediately after printing, making work proportional only to the first ten lines.

#### Alternatives and edge cases

- `awk 'NR == 10 { print; exit }'` is equally direct and stops after the target line.
- `head -n 10 | tail -n 1` is readable but launches two processes and must still handle a short file according to the tool semantics.
- Loading the complete file into an array wastes space.
- Empty and nine-line files produce no output. An empty tenth line still produces one newline because it is a real line.

</details>
