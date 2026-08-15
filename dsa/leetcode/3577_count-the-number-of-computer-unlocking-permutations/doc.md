# Count the Number of Computer Unlocking Permutations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3577 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Brainteaser, Combinatorics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-computer-unlocking-permutations/) |

## Problem Description

### Goal

There are $n$ locked computers labeled from $0$ through $n-1$. Computer $i$ has a distinct password whose difficulty is `complexity[i]`. The password of computer $0$ is already decrypted and acts as the root of the unlocking process.

To unlock computer $i>0$, some already unlocked computer $j$ must satisfy both $j<i$ and `complexity[j] < complexity[i]`. Thus an earlier label alone is insufficient: its password must also have strictly lower complexity.

Count the permutations of all computer labels that give a valid unlocking order, with computer $0$ first as the initially available root. Return the count modulo $10^9+7$.

### Function Contract

**Inputs**

- `complexity`: An integer array of length $n$, where $2\le n\le10^5$ and $1\le\texttt{complexity[i]}\le10^9$.

**Return value**

Return the number of valid unlocking permutations modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `complexity = [1,2,3]`
- **Output:** `2`
- **Explanation:** After computer `0`, either `1` or `2` may be unlocked first because the root has lower complexity than both.

#### Example 2

- **Input:** `complexity = [3,3,3,4,4,4]`
- **Output:** `0`
- **Explanation:** Computer `1` cannot be unlocked: the only smaller label is `0`, whose complexity is not strictly lower.

---
