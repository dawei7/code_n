# Word Subsets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 916 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/word-subsets/) |

## Problem Description
### Goal

You are given two arrays of lowercase English strings, `words1` and `words2`. A string `b` is a subset of a string `a` when every letter occurring in `b` also occurs in `a` at least as many times. Multiplicity matters: for example, `"wrr"` is a subset of `"warrior"`, but not of `"world"`.

A word `a` from `words1` is universal when every string `b` in `words2` is a subset of `a`. Return all universal strings from `words1`. The answer may be returned in any order.

### Function Contract
**Inputs**

- `words1`: an array of unique lowercase English strings.
- `words2`: an array of lowercase English strings.
- Each array contains between $1$ and $10^4$ strings, and each string has length from $1$ through $10$.

Let the total number of input characters be

$$
S = \sum_{w \in \texttt{words1}} \lvert w \rvert
  + \sum_{w \in \texttt{words2}} \lvert w \rvert.
$$

**Return value**

A list containing exactly the strings in `words1` whose letter multiplicities satisfy every string in `words2`. Any output order is valid.

### Examples
**Example 1**

- Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]`
- Output: `["facebook","google","leetcode"]`

**Example 2**

- Input: `words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]`
- Output: `["leetcode"]`

**Example 3**

- Input: `words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]`
- Output: `["cccbb"]`
