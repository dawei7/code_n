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

### Required Complexity

- **Time:** $O((n + E) \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Prioritize the batch that rots first**

Maintain a min-heap of available batches keyed by their exclusive expiration day. At the start of each day, add the newly produced nonempty batch. Remove heap entries whose expiration is at most the current day, because none of their remaining apples can be eaten.

If any valid batch remains, eat one apple from the heap minimum. When that batch still contains more apples, return its reduced count to the heap. Continue advancing days after production ends until no available batch remains.

**Why earliest expiration is safe**

Suppose a schedule eats an apple from a later-expiring batch on a day when an earlier-expiring batch is also available. Exchange those choices: eat the earlier batch now and reserve the later batch for the day on which the earlier apple was eaten, if such a day exists. The later apple remains valid for at least as long, so this swap never invalidates a future meal. If the earlier apple was never eaten, consuming it now simply replaces the later apple without reducing the total.

Repeated exchanges transform an optimal schedule into one that always consumes the earliest expiration. The heap implements exactly that greedy schedule. Removing expired batches is also safe because they can no longer appear in any feasible continuation.

**Continue beyond the production horizon**

Stopping at day $n-1$ would miss fruit whose expiration lies later. The loop condition therefore includes either an unprocessed production day or a nonempty heap. After the input ends, each successful iteration consumes one apple; expired batches are discarded before they can be counted.

#### Complexity detail

Each of the $n$ batches is inserted at most once and removed at most once. Every one of the $E$ eaten apples causes a heap removal and may cause one reinsertion, so the total running time is $O((n + E) \log n)$. At most $n$ distinct batches coexist in the heap, using $O(n)$ space.

#### Alternatives and edge cases

- **Scan all active batches daily:** selecting the minimum expiration by linear search is correct but can take quadratic time when many long-lived batches overlap.
- **First-in, first-out queue:** production order and expiration order can differ because batch lifetimes vary, so arrival order is not a safe priority.
- **Largest batch first:** batch size does not measure urgency and may allow a smaller, earlier batch to rot.
- **Zero-production day:** add no heap entry and still consume an older batch when one remains.
- **Exclusive expiration:** a batch expiring on `day` must be discarded before that day's meal.
- **Multiple expired batches:** remove all invalid heap minima, not only one, before choosing an apple.
- **After day $n-1$:** keep eating while the heap contains unexpired apples.
- **More apples than usable days:** a batch may retain fruit when it expires; only actually eaten apples contribute to $E$.

</details>
