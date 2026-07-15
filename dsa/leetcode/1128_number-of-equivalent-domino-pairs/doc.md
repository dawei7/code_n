# Number of Equivalent Domino Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1128 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/number-of-equivalent-domino-pairs/) |

## Problem Description

### Goal

You are given a list `dominoes`, where `dominoes[i] = [a,b]` records the two values on domino `i`. Two dominoes `[a,b]` and `[c,d]` are equivalent if they are identical in their current orientation, meaning $a=c$ and $b=d$, or if rotating one makes them identical, meaning $a=d$ and $b=c$.

Return the number of index pairs `(i, j)` satisfying $0 \le i < j < n$ for which `dominoes[i]` and `dominoes[j]` are equivalent. Distinct pairs of indices count separately even when several dominoes all belong to the same equivalence group.

### Function Contract

**Inputs**

- `dominoes`: an array of $n$ two-element integer arrays, where $1 \le n \le 4 \times 10^4$ and every half value lies in $[1,9]$.

**Return value**

The number of equivalent index pairs `(i, j)` with `i < j`.

### Examples

**Example 1**

- Input: `dominoes = [[1,2],[2,1],[3,4],[5,6]]`
- Output: `1`

**Example 2**

- Input: `dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Give both orientations one key.** Normalize `[a,b]` to the ordered pair $(\min(a,b), \max(a,b))$. A domino and its rotation then receive the same key, while two non-equivalent dominoes cannot share a key. Since each value is one digit, encode that pair as `10 * min(a, b) + max(a, b)` and use a fixed 100-entry frequency array.

**Count pairs when their second endpoint arrives.** Scan the dominoes from left to right. If `counts[key]` equivalent dominoes have already appeared, the current domino completes exactly that many new pairs: one with each earlier matching index. Add that frequency to the answer, then increment `counts[key]` for future dominoes.

Every valid pair is counted once, when its larger index is processed. No invalid pair is counted because only identical normalized keys contribute. If an equivalence group ultimately contains $k$ dominoes, its successive contributions are $0,1,\ldots,k-1$, whose sum is $k(k-1)/2$, exactly the number of index pairs in that group.

#### Complexity detail

The scan performs constant work for each of the $n$ dominoes, giving $O(n)$ time. Domino values are restricted to $1$ through $9$, so the fixed frequency array has 100 entries independent of $n$ and uses $O(1)$ space.

#### Alternatives and edge cases

- **Hash map of tuple keys:** A dictionary keyed by `(min(a, b), max(a, b))` has the same expected $O(n)$ time and is convenient if the value range is not fixed, but uses space proportional to the distinct keys.
- **Compare every pair:** Directly testing all `i < j` pairs is correct but requires $O(n^2)$ time.
- **Double domino:** `[x,x]` is unchanged by rotation and normalizes normally; each pair of its occurrences counts once.
- **Several equivalent dominoes:** A group of $k$ contributes $\binom{k}{2}$, not merely one pair.
- **Single domino:** With no earlier equivalent index, it contributes zero and the final answer is `0`.

</details>
