# Greatest Sum Divisible by Three

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1262 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/greatest-sum-divisible-by-three/) |

## Problem Description

### Goal

You are given an array `nums` of positive integers. Select any subset of its elements and add the selected values. Each array position may be used at most once, and the selection does not need to be contiguous.

Return the largest achievable sum that is divisible by $3$. Selecting no elements is allowed, so zero is always a valid candidate when no positive divisible sum can be formed.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1 \le n \le 4\cdot10^4$ and $1 \le \texttt{nums[i]} \le 10^4$.

**Return value**

- Return the maximum subset sum whose remainder modulo $3$ is zero.

### Examples

**Example 1**

- Input: `nums = [3, 6, 5, 1, 8]`
- Output: `18`
- Explanation: Selecting `3`, `6`, `1`, and `8` gives the largest divisible sum.

**Example 2**

- Input: `nums = [4]`
- Output: `0`

**Example 3**

- Input: `nums = [1, 2, 3, 4, 4]`
- Output: `12`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

For divisibility by three, the exact accumulated sum matters only for maximizing value within each remainder class. Maintain `dp[r]` as the largest sum obtainable from processed elements with remainder $r$. Initially, zero is reachable with remainder zero, while remainders one and two are unreachable.

**Include or exclude each value**

Copy the three previous states before processing a value. Excluding the value preserves every old state. Including it transforms a reachable residue `r` into `(r + value) % 3` with candidate sum `dp[r] + value`; maximize the destination state with that candidate. Reading only the old snapshot prevents one array value from being used more than once.

**Why three maxima are sufficient**

Suppose two processed subsets have the same remainder and one has the larger sum. Adding any identical future selection changes both sums by the same amount and preserves their shared remainder, so the smaller sum can never lead to a better final answer. Keeping only the maximum for each residue therefore loses no optimal solution.

After all values, `dp[0]` is the largest reachable sum divisible by three. The initial empty-subset state ensures it is at least zero.

#### Complexity detail

Each of the $n$ values updates exactly three remainder states, taking $O(n)$ time. The current and previous arrays contain three entries each, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate all subsets:** It directly checks every selection but takes $O(2^n)$ time.
- **Remove the cheapest residues greedily:** Starting from the total sum and removing one residue-one item or two residue-two items can be made correct, but requires careful symmetric cases and minimum tracking.
- **Recompute every prefix:** Rebuilding remainder DP from scratch for each prefix returns the same final answer but takes $O(n^2)$ time.
- **All values divisible by three:** Selecting every value is optimal.
- **No positive divisible subset:** The empty subset yields the required answer `0`.
- **Duplicate values:** Treat positions independently; equal values may all be selected when available.

</details>
