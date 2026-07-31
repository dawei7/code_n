# Find Words Containing Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2942 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-words-containing-character/) |

## Problem Description
### Goal
You are given a 0-indexed array of lowercase strings `words` and one
lowercase English character `x`. Examine each word independently and decide
whether `x` occurs anywhere within it. Multiple occurrences inside the same
word do not create duplicate results.

Return the indices of exactly those words that contain `x`. The returned
indices may appear in any order; preserving their order from `words` is one
valid choice.

### Function Contract
**Inputs**

- `words`: the nonempty array of lowercase English words
- `x`: the lowercase English character to locate

Let $W=\lvert\texttt{words}\rvert$ and define the total character count

$$
S=\sum_{w\in\texttt{words}}\lvert w\rvert.
$$

The contract guarantees $1\le W\le50$ and
$1\le\lvert\texttt{words[i]}\rvert\le50$.

**Return value**

A list containing each index `i` for which `x in words[i]` is true, in any
order.

### Examples
**Example 1**

- Input: `words = ["leet","code"], x = "e"`
- Output: `[0,1]`
- Explanation: Both words contain `"e"`.

**Example 2**

- Input: `words = ["abc","bcd","aaaa","cbc"], x = "a"`
- Output: `[0,2]`
- Explanation: Only the words at indices `0` and `2` contain `"a"`.

**Example 3**

- Input: `words = ["abc","bcd","aaaa","cbc"], x = "z"`
- Output: `[]`
- Explanation: None of the words contains `"z"`.
