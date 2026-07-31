# Palindrome Rearrangement Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2983 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/palindrome-rearrangement-queries/) |

## Problem Description
### Goal
You are given a 0-indexed lowercase string `s` of even length and a list of
queries. A query `[a, b, c, d]` permits arbitrary rearrangement of the
characters in the inclusive substring `s[a:b]` in the first half and,
independently, of `s[c:d]` in the second half. The indices always satisfy
$0\le a\le b<N/2\le c\le d<N$.

For every query, decide whether those two rearrangements can make the entire
string a palindrome. Queries are independent: a rearrangement considered for
one query never changes the input seen by another. Return the Boolean answers
in query order.

### Function Contract
**Inputs**

- `s`: an even-length lowercase English string
- `queries`: inclusive index quadruples `[a, b, c, d]` obeying the half constraints above

Let $N=\lvert\texttt{s}\rvert$ and $Q=\lvert\texttt{queries}\rvert$. The
contract guarantees $2\le N\le10^5$ and $1\le Q\le10^5$.

**Return value**

Return a length-$Q$ Boolean list whose $i$th value states whether the
rearrangements allowed by query $i$ can produce a palindrome.

### Examples
**Example 1**

- Input: `s = "abcabc", queries = [[1,1,3,5],[0,2,5,5]]`
- Output: `[true,true]`

**Example 2**

- Input: `s = "abbcdecbba", queries = [[0,2,7,9]]`
- Output: `[false]`
- Explanation: The fixed middle characters cannot be made symmetric.

**Example 3**

- Input: `s = "acbcab", queries = [[1,2,4,5]]`
- Output: `[true]`
