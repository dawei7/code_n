# Maximum Number of Coins You Can Get

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1561 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-coins-you-can-get/) |

## Problem Description
### Goal

There are $3G$ coin piles. On each step, you choose any three remaining piles. Alice takes the largest of those three piles, you take the next-largest pile, and Bob takes the last pile. Continue until no piles remain.

Given the number of coins in every pile, choose the groups to maximize the total number of coins that you receive, and return that maximum total.

### Function Contract
**Inputs**

- `piles`: An array of $N=3G$ positive integers, where $3 \le N \le 10^5$ and $1 \le \texttt{piles[i]} \le 10^4$.
- The array length is divisible by three; pile positions have no effect because each chosen triple may use arbitrary remaining piles.

**Return value**

Return the maximum total number of coins you can collect after all $G$ steps.

### Examples
**Example 1**

- Input: `piles = [2,4,1,2,7,8]`
- Output: `9`

**Example 2**

- Input: `piles = [2,4,5]`
- Output: `4`

**Example 3**

- Input: `piles = [9,8,7,6,5,1,2,3,4]`
- Output: `18`

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Reserve the cheapest piles for Bob**

Exactly $G$ piles go to each participant. Bob's pile only needs to be no larger than the two piles paired with it, so assigning him any large pile wastes value that could instead support your score. An exchange makes this precise: if Bob receives a pile larger than some pile assigned to Alice or you in another group, swapping those piles preserves the required order in a suitable regrouping and cannot reduce your total. Therefore an optimal arrangement can give Bob the smallest $G$ piles.

**Pair the remaining piles from largest to smallest**

The largest $2G$ piles remain for Alice and you. Sort them and pair adjacent values from the high end. In each pair Alice must take the larger value and you receive the smaller one. Pairing a very large pile with a much smaller eligible pile would only lower your gain; exchanging partners so nearby ranks are paired raises or preserves the smaller values awarded to you.

Thus, in the full ascending order, skip the smallest third, then take every other value beginning at index $G$. Equivalently, working downward, skip the current largest pile for Alice, take the next one for yourself, and repeat $G$ times. The unused smallest piles are assigned to Bob, one per pair.

#### Complexity detail

Sorting $N$ pile values takes $O(N\log N)$ time. Summing every other value in the upper two-thirds takes $O(N)$ additional time, so sorting dominates.

The implementation uses a separate sorted list, requiring $O(N)$ auxiliary space. An in-place sort can reduce language-dependent auxiliary storage, but the canonical implementation preserves its input and states the explicit copied-list bound.

#### Alternatives and edge cases

- **In-place sorting:** mutate `piles` and use the same rank selection. This avoids the explicit copy but changes the caller's array and still depends on the language's sorting workspace.
- **Repeated extrema extraction:** repeatedly remove the largest for Alice, the next-largest for you, and the smallest for Bob. It is correct but array searches and removals make it quadratic.
- **Counting sort:** pile values are at most $10^4$, so a frequency table can select ranks in $O(N+10^4)$ time. It is asymptotically faster for this bounded value domain but more specialized.
- **Single group:** with three piles, you necessarily receive the median.
- **Duplicate sizes:** equal values may be assigned to either player without changing the total; rank multiplicities remain valid.
- **All piles equal:** every one of your $G$ piles has the common value.
- **Large outliers:** Alice consumes one pile from each upper pair, preventing you from simply taking the globally largest $G$ piles.

</details>
