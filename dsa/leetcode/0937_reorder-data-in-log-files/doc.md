# Reorder Data in Log Files

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 937 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [reorder-data-in-log-files](https://leetcode.com/problems/reorder-data-in-log-files/) |

## Problem Description

### Goal

Each string in `logs` contains space-delimited tokens. Its first token is an identifier, followed by at least one content word. A letter-log has only lowercase English letters in its content, while a digit-log has only digits there.

Reorder the logs so every letter-log comes before every digit-log. Sort letter-logs lexicographically by their complete content; when two contents are equal, sort those logs by identifier. Digit-logs must preserve their original relative order. Return the resulting list of unchanged log strings.

### Function Contract

**Inputs**

- `logs`: between $1$ and $100$ valid log strings, each with length from $3$ through $100$ and tokens separated by single spaces.

Let $S$ be the total number of characters, $L$ the number of letter-logs, and $C$ the maximum log length.

**Return value**

Return all original log strings in the required letter-log order followed by digit-logs in stable input order.

### Examples

**Example 1**

- Input: `logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]`
- Output: `["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]`

**Example 2**

- Input: `logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]`
- Output: `["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]`
