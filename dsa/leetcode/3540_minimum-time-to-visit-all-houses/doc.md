# Minimum Time to Visit All Houses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3540 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-visit-all-houses/) |

## Problem Description

### Goal

There are `n` houses labeled from `0` through `n - 1` around a circle. Two directed road systems connect neighboring houses. Moving forward from house `i` to `(i + 1) % n` covers `forward[i]` meters. Moving backward from house `i` to `(i - 1 + n) % n` covers `backward[i]` meters.

You walk at one meter per second and begin at house `0`. Visit the houses listed in `queries` in their given order. For every move from the current house to the next requested house, either direction around the circle may be used, independently of earlier moves.

Return the minimum total number of seconds required to complete all visits.

### Function Contract

**Inputs**

- `forward`: Forward-edge lengths, where `forward[i]` is the distance from `i` to `(i + 1) % n`.
- `backward`: Backward-edge lengths, where `backward[i]` is the distance from `i` to `(i - 1 + n) % n`.
- `queries`: The required house visits in order; the first target is not `0`, and consecutive targets differ.

Both road arrays have the same length $n$, where $2 \le n \le 10^5$. Every road length lies in $[1,10^5]$. Let $Q=\lvert\texttt{queries}\rvert$, where $1 \le Q \le 10^5$.

**Return value**

- The minimum total travel time, in seconds, starting from house `0` and visiting all query targets in order.

### Examples

#### Example 1

- **Input:** `forward = [1,4,4], backward = [4,1,2], queries = [1,2,0,2]`
- **Output:** `12`
- **Explanation:** Optimal choices reach the requested houses at cumulative times `1`, `5`, `8`, and `12`.

#### Example 2

- **Input:** `forward = [1,1,1,1], backward = [2,2,2,2], queries = [1,2,3,0]`
- **Output:** `4`
- **Explanation:** Following one forward edge for every visit completes a full circle in four seconds.
