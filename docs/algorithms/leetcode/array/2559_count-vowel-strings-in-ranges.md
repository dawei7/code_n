# Count Vowel Strings in Ranges

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2559 |
| Difficulty | Medium |
| Topics | Array, String, Prefix Sum |
| Official Link | [count-vowel-strings-in-ranges](https://leetcode.com/problems/count-vowel-strings-in-ranges/) |

## Problem Description & Examples
### Goal
Given a list of strings and a set of query ranges, determine how many strings in each range start and end with a vowel. A string is considered valid if both its first and last characters are in the set {'a', 'e', 'i', 'o', 'u'}.

### Function Contract
**Inputs**

- `words`: A list of strings consisting of lowercase English letters.
- `queries`: A list of integer pairs `[li, ri]`, where each pair represents an inclusive range index in the `words` array.

**Return value**

- A list of integers where each element corresponds to the count of valid strings within the specified range `[li, ri]` for each query.

### Examples
**Example 1**

- Input: `words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]`
- Output: `[2,3,0]`

**Example 2**

- Input: `words = ["a","e","i"], queries = [[0,2],[0,1],[2,2]]`
- Output: `[3,2,1]`

---

## Underlying Base Algorithm(s)
The problem is solved using the **Prefix Sum** technique. By pre-calculating an array where each index `i` stores the cumulative count of valid strings from the start of the list up to index `i`, we can answer range queries in constant time $O(1)$ by calculating `prefix_sum[ri + 1] - prefix_sum[li]`.

---

## Complexity Analysis
- **Time Complexity**: $O(N + Q)$, where $N$ is the number of words and $Q$ is the number of queries. We iterate through the words once to build the prefix sum array and through the queries once to compute the results.
- **Space Complexity**: $O(N)$ to store the prefix sum array.
