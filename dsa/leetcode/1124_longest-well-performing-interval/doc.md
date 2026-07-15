# Longest Well-Performing Interval

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1124 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Stack, Monotonic Stack, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/longest-well-performing-interval/) |

## Problem Description

### Goal

The array `hours` records how many hours one employee worked on each consecutive day. A day is a tiring day if and only if the employee worked strictly more than `8` hours on that day; every other day, including a day of exactly `8` hours, is non-tiring.

A well-performing interval is a contiguous interval of days in which the number of tiring days is strictly larger than the number of non-tiring days. Among all intervals in `hours`, return the greatest possible length of a well-performing interval. Return `0` when no interval satisfies the strict majority condition.

### Function Contract

**Inputs**

- `hours`: an integer array of length $n$, where $1 \le n \le 10^4$ and $0 \le \texttt{hours[i]} \le 16$.

**Return value**

The length of the longest contiguous interval containing strictly more tiring days than non-tiring days.

### Examples

**Example 1**

- Input: `hours = [9,9,6,0,6,6,9]`
- Output: `3`
- Explanation: `[9,9,6]` is a well-performing interval of maximum length.

**Example 2**

- Input: `hours = [6,6,6]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Replace hours with a signed balance.** Treat each tiring day as $+1$ and each non-tiring day as $-1$. A contiguous interval is well-performing exactly when the sum of its transformed values is positive. Let the running prefix score after index `i` be `score`; the problem becomes finding the longest pair of prefix positions whose later score is strictly greater than the earlier score.

**Take the whole prefix whenever possible.** If `score > 0` at index `i`, then the interval from index `0` through `i` is positive, so its length `i + 1` is automatically the longest interval ending there.

**Remember only the earliest occurrence of each score.** When `score <= 0`, a positive interval ending at `i` needs an earlier prefix with score below the current one. Because every update changes the score by exactly one, if any lower score has occurred, `score - 1` must also have occurred on the path to it. Using the earliest index stored for `score - 1` maximizes the interval length `i - first_seen[score - 1]`. Store a score only on its first occurrence, since a later copy can never form a longer interval with any future endpoint. These two cases examine every endpoint and therefore find the global maximum.

#### Complexity detail

The algorithm scans all $n$ days once, and each hash-table lookup or insertion takes expected $O(1)$ time, for $O(n)$ total time. The running score lies in $[-n,n]$, so the earliest-index map contains at most $O(n)$ entries and uses $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every interval:** Prefix sums make each interval test constant time, but there are $O(n^2)$ intervals, so this approach is too slow at the maximum input size.
- **Monotonic prefix stack:** A decreasing stack of prefix indices followed by a reverse scan also finds the widest positive-score gap in $O(n)$ time and $O(n)$ space, but is less direct here.
- **Exactly eight hours:** The strict threshold classifies `8` as non-tiring, so it contributes $-1$, not $+1$.
- **No tiring days:** No positive transformed sum exists, and the result remains `0`.
- **Positive total score:** The entire array is well-performing and must be returned with length $n$.

</details>
