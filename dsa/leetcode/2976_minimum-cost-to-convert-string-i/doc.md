# Minimum Cost to Convert String I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2976 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Graph, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-i/) |

## Problem Description

### Goal

You are given equal-length lowercase strings `source` and `target`. Each aligned
position may be transformed independently by applying any number of directed
single-character conversion rules.

Rule `i` changes `original[i]` into `changed[i]` and charges `cost[i]` each
time it is used. Multiple rules may describe the same directed character pair,
and intermediate characters may make a conversion cheaper or possible.

Return the minimum total cost to transform every position of `source` into the
corresponding position of `target`, or `-1` if any required character
conversion is impossible.

### Function Contract

**Inputs**

- `source`: the initial lowercase string
- `target`: the desired lowercase string of the same length
- `original`: the starting characters of the directed rules
- `changed`: the ending characters of those rules
- `cost`: the positive costs of the corresponding rules

Let $N=\lvert\texttt{source}\rvert$, $K=\lvert\texttt{cost}\rvert$, and
$A=26$ for the lowercase English alphabet. The contract guarantees
$1\le N\le10^5$, $1\le K\le2000$, equal rule-array lengths, distinct endpoints
within every rule, and $1\le\texttt{cost[i]}\le10^6$.

**Return value**

The minimum sum of conversion costs across all positions, or `-1` if at least
one aligned character pair is unreachable.

### Examples

#### Example 1

- **Input:** `source = "abcd"`, `target = "acbe"`, `original = ["a","b","c","c","e","d"]`, `changed = ["b","c","b","e","b","e"]`, `cost = [2,5,5,1,2,20]`
- **Output:** `28`
- **Explanation:** The cheapest aligned conversions cost `0`, `5`, `3`, and `20`.

#### Example 2

- **Input:** `source = "aaaa"`, `target = "bbbb"`, `original = ["a","c"]`, `changed = ["c","b"]`, `cost = [1,2]`
- **Output:** `12`
- **Explanation:** Each `a` reaches `b` through `c` for cost `3`.

#### Example 3

- **Input:** `source = "abcd"`, `target = "abce"`, `original = ["a"]`, `changed = ["e"]`, `cost = [10000]`
- **Output:** `-1`
- **Explanation:** No sequence of rules converts `d` into `e`.
