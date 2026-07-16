# Make Sum Divisible by P

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1590 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/make-sum-divisible-by-p/) |

## Problem Description
### Goal

Given an array of positive integers, remove one contiguous subarray so that the sum of the remaining elements is divisible by `p`. The removed subarray may be empty, so no removal is needed when the original sum is already divisible.

Minimize the number of removed elements. Removing the entire array is forbidden, even though that would leave a sum of zero. Return `-1` when no proper subarray can satisfy the divisibility condition.

### Function Contract
**Inputs**

- `nums`: An array of $N$ positive integers, where $1 \le N \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `p`: A divisor satisfying $1 \le p \le 10^9$.

**Return value**

Return the minimum length of a removable contiguous subarray, `0` if the total is already divisible by `p`, or `-1` if only removing the whole array could work.

### Examples
**Example 1**

- Input: `nums = [3,1,4,2], p = 6`
- Output: `1`

**Example 2**

- Input: `nums = [6,3,5,2], p = 9`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3], p = 3`
- Output: `0`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(\min(N,p))$

<details>
<summary>Approach</summary>

#### General

**Translate the remaining-sum condition**

Let the total remainder be

$$
t=\left(\sum \texttt{nums[i]}\right)\bmod p.
$$

If $t=0$, the empty removal is optimal. Otherwise, the remaining sum is divisible by `p` exactly when the removed subarray's sum is congruent to $t$ modulo `p`.

**Find the shortest subarray with the required remainder**

Let `prefix` be the remainder of the sum through the current index. If a previous prefix had remainder `previous`, then the intervening subarray has remainder

$$
(\texttt{prefix}-\texttt{previous})\bmod p.
$$

To make this equal $t$, search for a previous remainder

$$
\texttt{needed}=(\texttt{prefix}-t)\bmod p.
$$

Store the latest index at which each prefix remainder occurred. The latest matching prefix produces the shortest subarray ending at the current index, so older occurrences with the same remainder can safely be overwritten. Seed remainder zero at index `-1` to represent a subarray starting at index zero.

For every position, test the needed remainder before recording the current prefix, update the best length, and continue. If the best length remains $N$, the only matching interval was the forbidden whole array or no interval matched, so return `-1`. Otherwise return the best proper length.

Every candidate subarray whose remainder is $t$ is considered when its right endpoint is scanned. The hash table provides the closest valid left boundary for that endpoint. Taking the minimum across endpoints therefore finds the globally shortest valid removal, while the final strict comparison with $N$ enforces the whole-array prohibition.

#### Complexity detail

The initial sum and the prefix scan each take $O(N)$ time. Hash-table lookup and update are expected $O(1)$ per element, giving $O(N)$ total time.

At most one latest index is stored per distinct prefix remainder, bounded by both $N+1$ observed prefixes and $p$ possible remainders, so auxiliary space is $O(\min(N,p))$.

#### Alternatives and edge cases

- **Reverse suffix scan:** process indices from right to left and store the closest suffix position for each remainder. It is an independent $O(N)$ formulation of the same modular identity.
- **Enumerate all subarrays:** accumulate every removed sum and test the remainder. It is correct but takes $O(N^2)$ time.
- **Sliding window:** modulo conditions are not monotone as endpoints move, so positive values do not make a standard window reliable.
- **Already divisible:** return `0`; the empty subarray is permitted.
- **Only the whole array matches:** return `-1`, not $N$.
- **Single element:** the answer is `0` when that value is divisible by `p`, otherwise `-1`.
- **Prefix or suffix removal:** the seeded zero remainder and ordinary later prefixes cover both boundaries.
- **Repeated remainders:** retain the latest occurrence because it minimizes the current candidate length.
- **Large values:** reduce running sums modulo `p` to avoid unnecessary growth in fixed-width implementations.

</details>
