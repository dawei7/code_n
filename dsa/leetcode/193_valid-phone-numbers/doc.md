# Valid Phone Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 193 |
| Difficulty | Easy |
| Category | Shell |
| Topics | Shell |
| Supported Languages | bash |
| Official Link | [LeetCode](https://leetcode.com/problems/valid-phone-numbers/) |

## Problem Description
### Goal
The file `file.txt` contains one candidate phone-number string per line. A line is valid only when the entire line matches either `xxx-xxx-xxxx` or `(xxx) xxx-xxxx`, where each `x` is a decimal digit and the spaces, hyphens, and parentheses occur exactly as shown.

Write every valid original line to standard output in its original file order. Reject lines with extra leading or trailing text, missing separators, misplaced whitespace, or the wrong number of digits, even if they contain a valid-looking fragment. Do not reformat accepted lines or print diagnostics for rejected ones; if no line matches, produce no output.

### Function Contract
**Inputs**

- `file.txt`: one candidate phone number per line

**Return value**

Write each original line matching `xxx-xxx-xxxx` or `(xxx) xxx-xxxx` to stdout, preserving file order.

### Examples
**Example 1**

- File lines: `987-123-4567`, `123 456 7890`, `(123) 456-7890`
- Output: the first and third lines

**Example 2**

- Line: `(555) 000-1234`
- Output: the same line

**Example 3**

- Line has an extra prefix or suffix
- Output: no line

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The two accepted forms differ only in their first three-digit block:

- `[0-9]{3}-` for `987-`
- `\([0-9]{3}\) ` for `(123) `, including exactly one literal space

They share the suffix `[0-9]{3}-[0-9]{4}`. Combine the two prefixes in one extended regular-expression alternative and anchor the entire expression with `^` and `$`:

```text
^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$
```

Use `grep -E` so braces and grouping have extended-regex meaning. The literal parentheses in the phone format must be escaped; the grouping parentheses around the alternatives must not. Anchors prevent a valid-looking substring inside `x987-123-4567y` from being accepted.

`grep` returns status 1 when no line matches. That is a normal empty-result case for this challenge, so a standalone script running under strict shell error handling may explicitly tolerate that status without printing anything.

Any matched line begins with exactly one permitted three-digit prefix, continues with exactly three digits, one hyphen, and four digits, and contains nothing else because of the anchors. It is therefore valid. Conversely, every valid input line uses one of the two prefix alternatives and the common suffix, so it matches the expression and is emitted. `grep` preserves the order and original text of matching lines.

#### Complexity detail

The regular-expression engine scans each input character a constant number of times for this fixed pattern, giving $O(n)$ time in total file size. Matching is streaming and uses $O(1)$ auxiliary state apart from I/O buffers.

#### Alternatives and edge cases

- Two separate `grep` commands can express the formats independently but either scan twice or need output merging that preserves order.
- An unanchored expression accepts prefixes, suffixes, or embedded valid substrings.
- `\d` is not portable across all `grep -E` implementations; `[0-9]` clearly expresses ASCII digits.
- The parenthesized form requires exactly one following space. Extra whitespace, missing punctuation, blank lines, and extra characters are rejected.

</details>
