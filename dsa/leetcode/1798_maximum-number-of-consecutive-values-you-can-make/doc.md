# Maximum Number of Consecutive Values You Can Make

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/) |
| Frontend ID | 1798 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You have several coins, and `coins[i]` is the value printed on the $i$-th coin. Each coin may be selected at most once. The value of a chosen subset is the sum of its coins; choosing no coins produces value $0$.

Determine the maximum number of consecutive integer values, beginning with $0$, that can be formed from subsets of the given coins. Equivalently, return the smallest nonnegative value that cannot be formed.

### Function Contract

**Inputs**

- `coins`: a list of $n$ positive integers, where $1 \le n \le 4 \cdot 10^4$ and $1 \le \texttt{coins[i]} \le 4 \cdot 10^4$.

**Return value**

- Return the number of consecutive values starting from $0$ that can be formed by selecting each coin zero or one time.

### Examples

**Example 1**

- Input: `coins = [1,3]`
- Output: `2`

The values $0$ and $1$ are formable, but $2$ is not.

**Example 2**

- Input: `coins = [1,1,1,4]`
- Output: `8`

Every value from $0$ through $7$ can be formed.

**Example 3**

- Input: `coins = [1,4,10,3,1]`
- Output: `20`

The coins can form every value from $0$ through $19$.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Represent all known subset sums by one interval**

Suppose the processed coins can form every value in the interval $[0,r)$. Initially no coins have been processed, so only $0$ is formable and $r=1$. The variable $r$ is therefore both the first value not yet known to be formable and the number of consecutive values currently covered.

**Process coins from smallest to largest**

Sort the values. If the next coin has value $c \le r$, combining it with every already-formable value in $[0,r)$ creates every value in $[c,c+r)$. Because $c \le r$, this new interval touches or overlaps the old interval, so their union covers $[0,r+c)$. Update `r += c`.

**Stop at the first unavoidable gap**

If the next sorted coin satisfies $c>r$, value $r$ cannot be formed. The processed coins produce only combinations below $r$, while every unused coin is at least $c$ and is already too large. No later coin can close this gap, so $r$ is the required answer.

Repeatedly applying the extension rule proves that the maintained interval contains every value it claims. The gap argument proves that stopping cannot miss another representation, establishing the greedy method's correctness.

#### Complexity detail

Sorting $n$ coins takes $O(n \log n)$ time, and the greedy scan takes $O(n)$ time. The app-local implementation creates a sorted copy, which uses $O(n)$ auxiliary space and leaves its input unchanged.

#### Alternatives and edge cases

- **Subset-sum set:** Explicitly insert every reachable sum, but the number of distinct sums can grow with the total coin value and is unnecessary when only the first gap matters.
- **Boolean subset-sum table:** Dynamic programming can mark all attainable values, but its time and space depend on the sum of all coins rather than only $n$.
- **No coin of value one:** The first sorted coin exceeds the initial boundary, so only value $0$ is formable and the answer is `1`.
- **Duplicate coins:** Each occurrence is a separate usable coin and extends the covered interval independently.
- **Gap after several extensions:** Return the current boundary immediately; larger remaining coins cannot repair it.
- **All coins extend coverage:** After the scan, the answer is one plus the sum of all coins.

</details>
