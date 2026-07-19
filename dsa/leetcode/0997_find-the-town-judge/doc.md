# Find the Town Judge

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 997 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Graph Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/find-the-town-judge/) |

## Problem Description

### Goal

A town contains `n` people labeled from $1$ through `n`, and a rumor says that one of them may be the town judge. If the judge exists, that person trusts nobody, every other person trusts the judge, and exactly one person satisfies both conditions.

Each pair `[a, b]` in `trust` states that person `a` trusts person `b`; a relationship absent from the list does not exist. Return the judge's label when the supplied relationships identify one, or return `-1` otherwise.

### Function Contract

**Inputs**

- `n`: the number of people, where $1\le\texttt{n}\le1000$.
- `trust`: a list of $E$ unique pairs, where $0\le E\le10^4$. Every pair contains different labels from $1$ through `n`.

Let $N=\texttt{n}$.

**Return value**

- The unique label that trusts nobody and is trusted by all other people, or `-1` if no such person exists.

### Examples

**Example 1**

- Input: `n = 2, trust = [[1, 2]]`
- Output: `2`

**Example 2**

- Input: `n = 3, trust = [[1, 3], [2, 3]]`
- Output: `3`

**Example 3**

- Input: `n = 3, trust = [[1, 3], [2, 3], [3, 1]]`
- Output: `-1`
- Explanation: Person $3$ is trusted by everyone else but violates the requirement to trust nobody.
