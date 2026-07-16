# Find a Value of a Mysterious Function Closest to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1521 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Bit Manipulation, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/) |

## Problem Description
### Goal

For indices `l` and `r`, the given function takes the bitwise AND of every array value in the inclusive range from `min(l, r)` through `max(l, r)`. Thus every function result is the AND of one nonempty contiguous subarray.

Choose any legal pair of indices so that the absolute difference between this AND value and `target` is as small as possible. Return that minimum difference; the indices and the chosen subarray itself are not returned.

### Function Contract
**Inputs**

Let $n$ be the array length and $M$ its maximum value.

- `arr`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$ and every value is at most $10^6$.
- `target`: An integer satisfying $0 \leq \texttt{target} \leq 10^7$.

**Return value**

Return the minimum of

$$
\left\lvert\left(\mathop{\mathtt{AND}}_{k=l}^{r}\texttt{arr}[k]\right)-\texttt{target}\right\rvert
$$

over every nonempty contiguous interval with $0 \leq l \leq r < n$.

### Examples
**Example 1**

- Input: `arr = [9, 12, 3, 7, 15], target = 5`
- Output: `2`
- Explanation: Reachable AND values include 3 and 7, both two away from 5.

**Example 2**

- Input: `arr = [1000000, 1000000, 1000000], target = 1`
- Output: `999999`
- Explanation: Every nonempty subarray has AND value 1000000.

**Example 3**

- Input: `arr = [1, 2, 4, 8, 16], target = 0`
- Output: `0`
- Explanation: The AND of any adjacent pair is zero.

### Required Complexity

- **Time:** $O(n\log M)$
- **Space:** $O(\log M)$

<details>
<summary>Approach</summary>

#### General

**Keep only distinct ANDs ending at the previous position**

Suppose `previous` contains every distinct AND value of a subarray ending immediately before the current element. A subarray ending at the current position either starts there, producing the element itself, or extends one of those earlier subarrays, producing `candidate & value`. These two sources construct every possible ending-here value.

Deduplicate them in a set. For every resulting value, update the smallest absolute difference from `target`; if the difference reaches zero, return immediately because no better answer exists.

**Why the state remains small**

Extending a subarray with bitwise AND can only clear set bits; it can never restore one. Along the sequence of distinct AND values for progressively earlier starting positions, every strict change removes at least one bit. An integer no larger than $M$ has $O(\log M)$ bits, so at most $O(\log M)$ distinct values survive for one ending position.

Replacing `previous` after each element is safe because future subarrays care only about distinct AND values, not which starting indices produced them. The recurrence covers every interval exactly through its right endpoint, so scanning all endpoints considers the global optimum.

#### Complexity detail

For each of $n$ elements, at most $O(\log M)$ distinct prior values are extended and tested. Total time is $O(n\log M)$.

The current and previous sets each hold $O(\log M)$ integers, giving $O(\log M)$ auxiliary space. Under the source bound $M \leq 10^6$, each set has only a small constant number of bit-clearing states.

#### Alternatives and edge cases

- **Enumerate every subarray:** carrying a running AND for each left endpoint is correct but takes $O(n^2)$ time.
- **Segment tree plus binary search:** range-AND queries can locate value transitions, but the structure and proof are more involved than endpoint-state compression.
- **Sparse table:** constant-time range AND still leaves too many ranges unless combined with transition jumping.
- **Single element:** the answer is simply that value's distance from the target.
- **Exact target:** return zero as soon as any ending-state AND equals `target`.
- **Target above every array value:** AND cannot increase a value, but all endpoint states must still be considered to find the largest reachable result.
- **Repeated values:** deduplication collapses identical AND states immediately.
- **Rapid collapse to zero:** once zero occurs in an ending-state set, extending that state keeps it zero.

</details>
