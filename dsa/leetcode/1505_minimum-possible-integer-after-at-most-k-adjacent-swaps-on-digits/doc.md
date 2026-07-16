# Minimum Possible Integer After at Most K Adjacent Swaps On Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1505 |
| Difficulty | Hard |
| Topics | String, Greedy, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) |

## Problem Description
### Goal

The string `num` contains the decimal digits of a very large integer. One operation swaps two adjacent digits, and at most `k` such operations may be performed. Moving a digit left across $s$ digits consumes exactly $s$ adjacent swaps; all crossed digits shift one position right.

Return the lexicographically smallest digit string reachable within the budget, which is also the minimum numerical representation at the fixed input length. The result may begin with zero even though the input never does. Every digit occurrence must remain present, and fewer than `k` swaps may be used when additional operations cannot improve the result.

### Function Contract
**Inputs**

Let $n=\lvert\texttt{num}\rvert$.

- `num`: a string of decimal digits with $1\le n\le3\cdot10^4$ and no leading zero.
- `k`: the maximum number of adjacent swaps, with $1\le k\le10^9$.

**Return value**

Return the lexicographically smallest length-$n$ string obtainable by at most `k` adjacent swaps. Leading zeroes in the result are retained.

### Examples
**Example 1**

- Input: `num = "4321", k = 4`
- Output: `"1342"`
- Explanation: Bringing `1` to the front costs three swaps; the remaining swap brings `3` before `4`.

**Example 2**

- Input: `num = "100", k = 1`
- Output: `"010"`
- Explanation: The first zero moves left once. A leading zero is valid in the returned string.

**Example 3**

- Input: `num = "36789", k = 1000`
- Output: `"36789"`
- Explanation: The digits are already minimal, so spending swaps is unnecessary.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Choose the smallest reachable next digit**

Construct the result from left to right. At any step, each unselected original digit has a current rank among the remaining digits. Moving it to the next output position costs exactly that rank: one adjacent swap for every unselected digit currently before it.

Try digit values from `0` through `9`. For each value, only its earliest unselected occurrence can be cheapest; a later equal digit has all the same preceding obstacles plus at least one more occurrence. Select the first digit whose earliest occurrence costs at most the remaining budget, deduct that cost, and append it.

This choice is lexicographically forced. Any feasible result beginning with a larger digit is worse immediately. If an optimal result begins with the same digit value but uses a later occurrence, replacing it with the earlier identical occurrence costs no more and leaves the relative order of every other occurrence at least as favorable. Therefore the greedy prefix can always be extended to an optimal full result.

**Preserve occurrence order with ten queues**

Scan `num` once and place each original index into the queue for its digit. Popping from the front always exposes the earliest unselected occurrence of that value. This is important for duplicates: equal digits are interchangeable in the output, but consuming them in original order never wastes swaps.

Since the alphabet has only ten digits, testing all queues for each output position contributes a constant factor. The remaining challenge is computing the current rank of a queued original index after earlier selections have removed positions from throughout the string.

**Measure current rank with a Fenwick tree**

Maintain a Fenwick tree over original indices. A tree value of one means that position has already been selected and removed from the remaining sequence. For a candidate at original zero-based index $p$, let $R(p)$ be the number of removed positions at indices at most $p$. The number of still-present digits before the candidate is

$$
p-R(p).
$$

The candidate itself has not yet been removed, so an inclusive prefix query is safe. If this cost fits `k`, pop the occurrence, add one at index $p$ in the tree, and append its digit. Both the prefix query and update take $O(\log n)$ time.

At least the first remaining digit always has cost zero, so every output position chooses an occurrence. The queues ensure no occurrence is selected twice, and after $n$ iterations the answer contains exactly the input multiset.

**Why local greedy choices give the global minimum**

Assume the constructed prefix is shared with some optimal reachable result. At the next position, the algorithm selects the smallest digit value having an occurrence within budget. No feasible result with the same prefix can place a smaller value there, because the earliest occurrence of that smaller value already costs more than the available swaps and every later occurrence costs at least as much.

If another optimal result chooses a larger value, replacing that choice by the reachable smaller digit improves it. If it chooses the same value from later in the string, use the earlier queued occurrence instead. The replacement consumes no additional budget and only shifts intervening digits right while preserving their relative order. Thus an optimum exists with the extended greedy prefix. Induction over all positions proves the final string is minimum.

#### Complexity detail

Building the ten occurrence queues takes $O(n)$ time and space. For each of $n$ output positions, at most ten candidate queues are inspected. Every nonempty inspection performs a Fenwick prefix query, and the selected occurrence performs one update, each in $O(\log n)$ time. Ten is constant, so total time is $O(n\log n)$.

The queues, Fenwick array, and output list each store $O(n)$ data. Total auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Mutable-list greedy simulation:** Inspect the reachable prefix, remove its smallest digit, and append it to the answer. It is correct and intuitive, but repeated slicing, searching, and middle deletion take $O(n^2)$ time.
- **Segment tree:** Store active counts and query how many remain before an index. It provides the same $O(n\log n)$ bound but uses more code and memory than a Fenwick tree.
- **Repeated adjacent swaps:** Physically perform every swap. The allowed budget reaches $10^9$, so work proportional to `k` is impossible.
- **Leading zero:** Zero is considered before every other digit and may be moved to the front whenever its rank fits the budget.
- **Duplicate digits:** Always use the earliest remaining occurrence; selecting a later equal digit cannot improve the prefix and costs no less.
- **Budget larger than every inversion:** The result is all digits sorted ascending, including all zeroes at the front.
- **Already nondecreasing digits:** The first remaining occurrence always has cost zero, so the input is returned without spending budget.
- **Budget exhausted early:** Every later choice is the first remaining digit at cost zero, preserving the untouched suffix order.
- **One digit:** It is selected at zero cost and returned unchanged.
- **Very large `k`:** Only compare and subtract integer ranks; no loop iterates once per allowed swap.

</details>
