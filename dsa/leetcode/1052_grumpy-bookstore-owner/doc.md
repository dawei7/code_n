# Grumpy Bookstore Owner

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1052 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/grumpy-bookstore-owner/) |

## Problem Description

### Goal

A bookstore is open for $N$ minutes. At the start of minute `i`, `customers[i]` customers enter, and all of them leave after that minute. The binary value `grumpy[i]` is `1` when the owner is grumpy during that minute and `0` otherwise. Customers are satisfied exactly when the owner is not grumpy while they visit.

The owner can use a secret technique once to remain not grumpy for exactly `minutes` consecutive minutes. Choose when to use that single interval and return the maximum total number of customers who can be satisfied during the day.

### Function Contract

**Inputs**

- `customers`: the $N$ customer counts, where $0 \le \texttt{customers[i]} \le 1000$.
- `grumpy`: a length-$N$ binary array describing the owner's current mood each minute.
- `minutes`: the technique duration $M$, where $1 \le M \le N \le 2\cdot10^4$.

**Return value**

- The maximum number of satisfied customers after applying the technique to at most one length-$M$ interval.

### Examples

**Example 1**

- Input: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- Output: `16`
- Explanation: Applying the technique during the final three minutes yields the maximum total.

**Example 2**

- Input: `customers = [1], grumpy = [0], minutes = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate guaranteed satisfaction:** Every customer arriving during a minute with `grumpy[i] == 0` is satisfied regardless of where the technique is used. Sum these customers once as the baseline.

**Measure only recoverable customers:** During a grumpy minute, those customers contribute nothing to the baseline but become satisfied if the chosen interval covers that minute. Thus each length-$M$ interval has an extra gain equal to the customer counts at its grumpy positions.

**Slide one fixed-length interval:** Add the recoverable count at the new right endpoint. Once the window exceeds $M$ positions, subtract the recoverable count leaving from the left. Track the greatest gain seen and add it to the baseline.

The baseline and window gain are disjoint: calm-minute customers are counted once regardless of the technique, and a grumpy-minute customer is counted only when covered by the chosen interval. The sliding window evaluates every possible consecutive interval of length $M$, so its maximum gain corresponds to an optimal single use of the technique.

#### Complexity detail

The baseline calculation and the sliding-window pass each inspect $N$ minutes, giving $O(N)$ time. Only scalar totals and indices are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Recompute every interval:** Sum recoverable customers separately for all $N-M+1$ windows. It is correct but takes $O(NM)$ time.
- **Prefix sums:** Build a prefix sum of recoverable customers and query each interval in constant time, using $O(N)$ extra space.
- **Mutate customer counts:** Zero out calm-minute entries and run a window over the remainder, but mutation is unnecessary and obscures the baseline.
- **All calm minutes:** Every customer is already satisfied; the technique adds zero.
- **All grumpy minutes:** The answer is the largest length-$M$ customer sum.
- **Full-day technique:** When $M=N$, every customer is satisfied.
- **Zero-customer minutes:** They do not affect either baseline or window gain.
- **Single minute:** The sole interval is the entire day.

</details>
