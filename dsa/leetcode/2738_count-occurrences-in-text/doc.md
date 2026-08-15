# Count Occurrences in Text

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2738 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| LeetCode | [Open problem](https://leetcode.com/problems/count-occurrences-in-text/) |

## Problem Description

### Goal

The `Files` table stores a unique file name and that file's text content. Determine how many files contain `bull` and how many contain `bear`, counting a file once for a word even if that word occurs several times in its content.

An occurrence is valid only when the exact lowercase word has a space immediately before and immediately after it. Embedded forms such as `bullet` and `bears`, punctuation-adjacent text such as `bull.`, and a target at the beginning or end of the content do not qualify. Return one row for each target word; row order is unrestricted.

### Function Contract

Let $R$ be the number of rows in `Files`, and let $S$ be the total number of characters across all `content` values.

**Inputs**

- `Files`: A table with unique varchar column `file_name` and text column `content`.

**Return value**

Return columns `word` and `count`. The two output rows must label `bull` and `bear` and report, for each label, the number of files containing at least one occurrence surrounded by spaces. The rows may appear in any order.

### Examples

#### Example 1

- **Input:** Three files contain valid `bull` occurrences; the second and third also contain valid `bear` occurrences.
- **Output:** `("bull", 3)` and `("bear", 2)`
- **Explanation:** Each qualifying file contributes once to the corresponding count.

#### Example 2

- **Input:** `Files = [("one.txt", " a bull bull bear bear z ")]`
- **Output:** `("bull", 1)` and `("bear", 1)`
- **Explanation:** Repetition inside one file does not increase the number of matching files.

#### Example 3

- **Input:** `Files = [("edges.txt", "bull starts while bears and bull. fail bear")]`
- **Output:** `("bull", 0)` and `("bear", 0)`
- **Explanation:** The targets are at a text boundary, embedded in a longer word, or adjacent to punctuation rather than spaces.
