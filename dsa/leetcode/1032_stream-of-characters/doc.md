# Stream of Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1032 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Design, Trie, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/stream-of-characters/) |

## Problem Description

### Goal

Design a `StreamChecker` that is initialized with an array of lowercase English words. Characters then arrive one at a time through calls to `query(letter)`, and every new letter is appended to the stream seen so far.

For each query, return `true` if some non-empty suffix of the current stream is exactly one of the configured words. Otherwise, return `false`. Each answer must reflect all letters received up to that call while preserving the same initialized checker.

### Function Contract

**Inputs**

- `words`: an array of $D$ lowercase words, where $1 \le D \le 2000$ and every word length is between $1$ and $200$.
- `queries`: the app-local sequence of $Q$ lowercase characters passed one by one to `query`, with at most $4\cdot10^4$ calls.
- Define
$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert
$$
and $W=\max_{w\in\texttt{words}}\lvert w\rvert$.

**Return value**

- The app-local `solve(words, queries)` adapter returns the $Q$ Boolean query results in order.
- The native artifact exposes `StreamChecker(words)` and `query(letter)` directly.

### Examples

**Example 1**

- Input: `words = ["cd","f","kl"], queries = ["a","b","c","d","e","f","g","h","i","j","k","l"]`
- Output: `[false,false,false,true,false,true,false,false,false,false,false,true]`
- Explanation: The stream ends with `"cd"` after `d`, with `"f"` after `f`, and with `"kl"` after `l`.
