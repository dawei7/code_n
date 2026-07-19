# Maximum Number of Eaten Apples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1705 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-eaten-apples/) |

## Problem Description
### Goal

An apple tree produces fruit during $n$ consecutive days. On day `i`, it grows `apples[i]` apples. Every apple from that batch becomes rotten on day `i + days[i]`, so it may be eaten on days from `i` through `i + days[i] - 1` but not on or after its expiration day. A zero-sized batch has `apples[i] = days[i] = 0`.

You may eat at most one apple per day. Apples can still be eaten after the first $n$ production days as long as an unexpired batch remains. Choose which available batch to consume from each day and return the maximum total number of apples that can be eaten before they rot.

### Function Contract
**Inputs**

- `apples`: a length-$n$ list where `apples[i]` is the batch size produced on day `i`
- `days`: a length-$n$ list where `days[i]` is that batch's lifetime in days
- $1 \le n \le 2 \cdot 10^4$, and every array value is between $0$ and $2 \cdot 10^4$
- `days[i] = 0` if and only if `apples[i] = 0`

Let $E$ be the number of apples ultimately eaten.

**Return value**

The maximum possible value of $E$ when at most one unexpired apple is eaten on each day.

### Examples
**Example 1**

- Input: `apples = [1, 2, 3, 5, 2], days = [3, 2, 1, 4, 2]`
- Output: `7`

Eating from the batches with the nearest expiration first preserves enough of the day-three batch to consume four apples from it through day six.

**Example 2**

- Input: `apples = [3, 0, 0, 0, 0, 2], days = [3, 0, 0, 0, 0, 2]`
- Output: `5`

Three apples are eaten on days zero through two, followed by two idle days and two more apples on days five and six.

**Example 3**

- Input: `apples = [2, 1, 10], days = [2, 10, 1]`
- Output: `4`

The short-lived batches are consumed first; only one of the ten apples produced on day two can be eaten before that batch expires.
