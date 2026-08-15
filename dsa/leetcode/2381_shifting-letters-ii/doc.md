# Shifting Letters II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2381 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/shifting-letters-ii/) |

## Problem Description

### Goal

Given a lowercase English string `s` and a list of range operations, apply every operation to the indicated inclusive substring. Each operation shifts its affected characters by one alphabet position, either forward or backward.

A forward shift maps each letter to its successor and wraps `'z'` to `'a'`; a backward shift maps each letter to its predecessor and wraps `'a'` to `'z'`. Operations may overlap, and their effects accumulate. Return the final string after all shifts have been applied.

### Function Contract

**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \le n \le 5 \cdot 10^4$.
- `shifts`: A list of $m$ triples `[start, end, direction]`, where $1 \le m \le 5 \cdot 10^4$, $0 \le \texttt{start} \le \texttt{end} < n$, and `direction` is `0` or `1`.

**Return value**

- Return the string produced after applying every range shift.

**Operation semantics**

- Both `start` and `end` belong to the shifted range.
- `direction = 1` shifts forward by one; `direction = 0` shifts backward by one.
- Alphabet arithmetic wraps modulo 26, and overlapping shifts combine algebraically.

### Examples

#### Example 1

- **Input:** `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`
- **Output:** `"ace"`
- **Explanation:** The intermediate strings are `"zac"`, `"zbd"`, and finally `"ace"`.

#### Example 2

- **Input:** `s = "dztz", shifts = [[0,0,0],[1,1,1]]`
- **Output:** `"catz"`
- **Explanation:** The first operation changes `'d'` to `'c'`, and the second wraps `'z'` forward to `'a'`.
