# Form Largest Integer With Digits That Add up to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1449 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/) |

## Problem Description
### Goal

Nine painting costs are given, one for each decimal digit from `1` through
`9`: painting digit `i + 1` costs `cost[i]`. A digit may be painted any number
of times. Choose a non-empty sequence of these digits whose total cost is
exactly `target`; digit `0` is unavailable.

Among every integer that can be formed under those rules, return the
numerically largest one. The answer can contain thousands of digits, so return
its decimal representation as a string rather than converting it to a numeric
type. If no non-empty sequence has exactly the required total cost, return
`"0"`.

### Function Contract
**Inputs**

- `cost`: a list of exactly nine integers. `cost[i]` is the cost of digit
  `i + 1`, and $1 \le \texttt{cost[i]} \le 5000$.
- `target`: the exact total cost to spend, with $1 \le \texttt{target} \le 5000$.

Let $T=\texttt{target}$. Because every digit has positive cost, any feasible
answer contains at most $T$ digits.

**Return value**

Return the decimal string for the largest positive integer whose digit costs
sum to exactly `target`. Return `"0"` when the exact cost is unreachable.

### Examples
**Example 1**

- Input: `cost = [4, 3, 2, 5, 6, 7, 2, 5, 5], target = 9`
- Output: `"7772"`
- Explanation: Three `7` digits cost $3\cdot2$ and digit `2` costs $3$, for a
  total of $9$. Although `"977"` is also feasible, the four-digit answer is
  numerically larger.

**Example 2**

- Input: `cost = [7, 6, 5, 5, 5, 6, 8, 7, 8], target = 12`
- Output: `"85"`

**Example 3**

- Input: `cost = [2, 4, 6, 2, 4, 6, 4, 4, 4], target = 5`
- Output: `"0"`
- Explanation: Every available cost is even, so no combination totals the odd
  target.

**Example 4**

- Input: `cost = [1, 1, 1, 1, 1, 1, 1, 1, 1], target = 3`
- Output: `"999"`
- Explanation: Every three-digit choice has the same cost and length, so the
  largest digit is selected at every position.

### Required Complexity
- **Time:** $O(T)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

**Separate numeric comparison into length and lexicographic order**

All permitted digits are nonzero. Therefore any decimal string with more
digits represents a larger positive integer than every shorter string. Among
strings of equal length, ordinary lexicographic order determines numeric
order. The optimization can consequently be split into two priorities:
maximize the number of digits first, then make the earliest digit as large as
possible without losing that optimal length.

**Dynamic programming records only the best attainable length**

Let `dp[x]` be the maximum number of digits whose costs total exactly `x`.
Set `dp[0] = 0`, since the empty construction is the base state, and mark all
positive costs initially unreachable. For every total from `1` through
`target`, try each of the nine digit costs. If spending a digit's price leaves
a reachable remainder, that transition proposes one more digit:

`dp[total] = max(dp[total], dp[total - price] + 1)`.

This is an unbounded knapsack recurrence because the same digit transition may
be used repeatedly. Processing totals in ascending order makes every smaller
remainder available when needed. If `dp[target]` remains unreachable, no exact
cost composition exists and the required result is `"0"`.

The recurrence is complete because the last digit of any feasible construction
has some price from `cost`; removing it leaves a construction represented by
the corresponding smaller state. Conversely, adding that digit to a reachable
state always produces a valid construction for the larger total. Taking the
maximum therefore gives exactly the greatest feasible digit count for every
cost.

**Reconstruct the greatest optimal prefix greedily**

Start with `remaining = target` and inspect digits from `9` down to `1`. A
digit with price `p` can be appended to the answer whenever
`dp[remaining] == dp[remaining - p] + 1`. That equality proves that using the
digit preserves the maximum possible final length. Append the digit and reduce
`remaining` by `p` repeatedly while the equality continues to hold, then move
to the next lower digit.

At each position, the scan chooses the largest digit that still permits an
optimal-length completion. Any alternative with a smaller digit at the first
different position is lexicographically and numerically smaller, while a
larger digit has already been shown unable to preserve the optimal length.
After a choice, the same argument applies to the remaining cost. Thus the
reconstruction is the lexicographically largest among all maximum-length
answers, and hence the numerically largest feasible integer.

**Why storing whole candidate strings is unnecessary**

The length table contains all information needed to decide whether a digit can
belong to an optimal result. Constructing and comparing strings during every
DP transition repeatedly copies long prefixes and can make the algorithm
quadratic in $T$. Deferring string construction until reconstruction emits
each answer character only once.

#### Complexity detail

There are $T+1$ DP states and exactly nine possible digit transitions per
state. Nine is a fixed part of the decimal-digit contract, so filling the table
takes $O(9T)=O(T)$ time. Reconstruction examines nine digit values and appends
at most $T$ characters because every cost is at least one, adding $O(T)$ time.

The integer DP table uses $O(T)$ space. The returned string can also contain
$O(T)$ characters; apart from that required output, the reconstruction uses
only constant scalar state.

#### Alternatives and edge cases

- **String-valued dynamic programming:** Keep the numerically best full string
  for every cost. It is conceptually direct, but repeated concatenation,
  sorting, and comparison of strings up to length $T$ can require $O(T^2)$ or
  more total character work and $O(T^2)$ retained characters.
- **Greedy by cheapest digit alone:** The cheapest price helps maximize length,
  but local choices can leave an unreachable remainder or miss a higher digit
  that preserves the same final length. The DP feasibility condition is still
  necessary.
- **Numeric integer DP:** Converting candidates to machine integers overflows
  because a legal answer may contain thousands of digits.
- **Unreachable target:** If `dp[target]` is unreachable, return exactly
  `"0"`; it is the failure marker, not a paintable digit.
- **Equal digit costs:** Prefer the larger digit during descending
  reconstruction because it preserves the same length and cost.
- **Length versus leading digit:** A longer answer always wins. For example,
  `"111"` is larger than `"99"` even though each digit `9` is larger.
- **Exact spending:** A construction costing less than `target` is invalid;
  only states reached by exact transitions may participate.
- **Repeated digits:** The unbounded recurrence and reconstruction loops allow
  any digit to appear as many times as its cost fits.

</details>
