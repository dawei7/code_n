# Check if DFS Strings Are Palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3327 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Tree, Depth-First Search, Hash Function |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/) |

## Problem Description

### Goal

A tree with $n$ nodes numbered from $0$ through $n-1$ is rooted at node $0$. The array `parent` describes its edges: `parent[0] = -1`, and for every other node `i`, `parent[i]` is its parent. The string `s` also has length $n$, with `s[i]` assigned to node `i`.

Define a shared, initially empty string `dfsStr`. A DFS call on node `x` recursively visits every child of `x` in increasing numerical order, then appends `s[x]` after all those child calls return. For each possible starting node `i`, empty `dfsStr`, perform that DFS on `i`, and determine whether the resulting postorder string is a palindrome.

Return a boolean array `answer` of length $n$ in which `answer[i]` records that result for the subtree rooted at node `i`. Every call uses a freshly emptied string; characters produced outside that subtree do not participate.

### Function Contract

**Inputs**

- `parent`: A length-$n$ parent array describing a valid tree rooted at node $0$.
- `s`: A length-$n$ string of lowercase English letters, where `s[i]` labels node `i`.

The constraints are $1\leq n\leq10^5$, `parent[0] = -1`, and $0\leq\texttt{parent[i]}<n$ for $i\geq1$.

**Return value**

Return a length-$n$ boolean list whose entry for node `i` is true exactly when the DFS string generated from `i` is a palindrome.

### Examples

#### Example 1

- **Input:** `parent = [-1, 0, 0, 1, 1, 2], s = "aababa"`
- **Output:** `[true, true, false, true, true, true]`
- **Explanation:** The root produces `"abaaba"`, node $1$ produces `"aba"`, and node $2$ produces `"ab"`. Only the last of those three strings is not a palindrome; every leaf produces one character.

#### Example 2

- **Input:** `parent = [-1, 0, 0, 0, 0], s = "aabcb"`
- **Output:** `[true, true, true, true, true]`
- **Explanation:** The root produces `"abcba"`, and every other node is a leaf, so all five strings are palindromes.
