# Evaluate the Bracket Pairs of a String

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/) |
| Frontend ID | 1807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The string `s` contains zero or more bracket pairs. Every pair encloses a non-empty key, as in `(name)` and `(age)` within `"(name)is(age)yearsold"`. Bracket pairs are properly closed and never nested, so each opening round bracket begins one complete key and its matching closing bracket ends it.

The array `knowledge` supplies known key-value associations. Each entry has the form `[key, value]`, and every key in this array is unique. Evaluate every bracket pair in `s`: replace the entire pair, including its brackets, with the associated value when its key is known, or with `"?"` when it is unknown. Lowercase letters outside brackets remain literal even if they spell a known key. Return the resulting string after all pairs have been evaluated.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters and round brackets, with $1 \le \lvert s \rvert \le 10^5$. Every opening bracket has a matching closing bracket, enclosed keys are non-empty, and pairs are not nested.
- `knowledge`: a list of at most $10^5$ two-string entries `[key, value]`. Every key is unique; keys and values contain from 1 through 10 lowercase English letters.
- Let $n = \lvert s \rvert$ and let

$$
k = \sum_{[\textit{key},\textit{value}] \in \texttt{knowledge}}
  \left(\lvert \textit{key} \rvert + \lvert \textit{value} \rvert\right).
$$

**Return value**

- Return a string in which every bracket pair has been replaced by its known value or by `"?"`, while all text outside bracket pairs retains its original order.

### Examples

**Example 1**

- Input: `s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]`
- Output: `"bobistwoyearsold"`

Both enclosed keys are known, so `(name)` becomes `"bob"` and `(age)` becomes `"two"`.

**Example 2**

- Input: `s = "hi(name)", knowledge = [["a","b"]]`
- Output: `"hi?"`

The key `"name"` is absent from `knowledge`.

**Example 3**

- Input: `s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]`
- Output: `"yesyesyesaaa"`

The same bracketed key may be evaluated repeatedly. The trailing unbracketed letters are not evaluated.
