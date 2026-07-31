# Minimum Cost to Convert String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2977 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Dynamic Programming, Graph, Trie, Shortest Path |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/) |

## Problem Description
### Goal
You are given equal-length lowercase strings `source` and `target`. Rule `i`
converts the whole string `original[i]` into the equal-length string
`changed[i]` for `cost[i]`.

An operation selects an occurrence of a rule's source string at some interval
and replaces it with that rule's destination. Any two operated intervals must
be disjoint or exactly identical. Thus one interval may undergo a sequence of
conversions, but two partially overlapping intervals are forbidden.

Apply any number of operations and return the minimum total cost to transform
`source` into `target`, or `-1` if no legal transformation exists. Duplicate
directed rules may occur.

### Function Contract
**Inputs**

- `source`: the initial lowercase string
- `target`: the desired lowercase string of the same length
- `original`: the source strings of the conversion rules
- `changed`: the equal-length destination strings of those rules
- `cost`: the positive costs of the corresponding rules

Let $N=\lvert\texttt{source}\rvert$, let $M$ be the number of distinct strings
appearing in either rule-string array, and let $S$ be their total distinct
length. The contract guarantees $1\le N\le1000$, at most `100` rules, rule
lengths from `1` through $N$, equal source/destination length within each rule,
and costs from `1` through $10^6$.

**Return value**

The minimum cost of a legal collection of disjoint-or-identical interval
operations, or `-1` when the target cannot be reached.

### Examples
**Example 1**

- Input: `source = "abcd"`, `target = "acbe"`, `original = ["a","b","c","c","e","d"]`, `changed = ["b","c","b","e","b","e"]`, `cost = [2,5,5,1,2,20]`
- Output: `28`
- Explanation: Single-character intervals independently realize the cheapest conversions.

**Example 2**

- Input: `source = "abcdefgh"`, `target = "acdeeghh"`, `original = ["bcd","fgh","thh"]`, `changed = ["cde","thh","ghh"]`, `cost = [1,3,5]`
- Output: `9`
- Explanation: Convert `bcd` once and convert the identical `fgh` interval twice through `thh`.

**Example 3**

- Input: `source = "abcdefgh"`, `target = "addddddd"`, `original = ["bcd","defgh"]`, `changed = ["ddd","ddddd"]`, `cost = [100,1578]`
- Output: `-1`
- Explanation: The two necessary intervals partially overlap, which the operation rules prohibit.
