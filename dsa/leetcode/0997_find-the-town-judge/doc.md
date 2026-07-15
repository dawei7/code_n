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

### Required Complexity

- **Time:** $O(N+E)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Combine both judge conditions in one score:** Give each person a score starting at zero. For every relationship `[a, b]`, decrement `a`'s score because trusting someone disqualifies that person, and increment `b`'s score because another person trusts them.

**Recognize the only possible final score:** A judge has outdegree zero and indegree $N-1$, so the judge's score is exactly $N-1$. Every nonjudge either has some outgoing trust, lacks at least one required incoming relationship, or both. Because trust pairs are unique and self-trust is forbidden, no other degree combination can also produce $N-1$.

After processing all relationships, scan labels from $1$ through `n` and return the one whose score is $N-1$. If none has that score, the rumor is false. The same reasoning covers the one-person town: with no relationships, its only resident has the required score zero.

#### Complexity detail

Processing the $E$ relationships and scanning the $N$ labels takes $O(N+E)$ time. The score array contains $N+1$ entries and uses $O(N)$ space.

#### Alternatives and edge cases

- **Separate indegree and outdegree arrays:** This is equally linear and may be more explicit, but stores two arrays instead of one combined score.
- **Check every candidate against every relationship:** Recounting degrees from the full edge list for each label takes $O(NE)$ time.
- **One-person town:** With `n = 1` and an empty trust list, person $1$ is the judge.
- **Judge trusts someone:** Any outgoing relationship disqualifies an otherwise universally trusted candidate.
- **Missing incoming relationship:** Being trusted by only some residents is insufficient.

</details>
