# Toss Strange Coins

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1230 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/toss-strange-coins/) |

## Problem Description

### Goal

You have `n` independent coins whose probabilities of landing heads are not necessarily equal. For the $i$th coin, `prob[i]` is the probability that its single toss produces heads; consequently, its probability of tails is `1 - prob[i]`.

Toss every coin exactly once. Given an integer `target`, return the probability that exactly `target` of the `n` coins show heads. Coins with probability `0` or `1` are allowed, and the requested count may be zero or may include every coin.

### Function Contract

**Inputs**

- `prob`: A list of $n$ head probabilities, where $1\le n\le1000$ and $0\le\texttt{prob[i]}\le1$.
- `target`: The exact required number of heads $t$, where $0\le t\le n$.

**Return value**

- The probability that exactly `target` coins land heads after all independent tosses.

### Examples

**Example 1**

- Input: `prob = [0.4]`, `target = 1`
- Output: `0.4`

The only coin must land heads.

**Example 2**

- Input: `prob = [0.5,0.5,0.5,0.5,0.5]`, `target = 0`
- Output: `0.03125`

All five fair coins must land tails, which has probability $(1/2)^5$.

**Example 3**

- Input: `prob = [0.5,0.5,0.5]`, `target = 2`
- Output: `0.375`

There are three equally likely choices for which one of the three coins lands tails.

### Required Complexity

- **Time:** $O(nt)$
- **Space:** $O(t)$

<details>
<summary>Approach</summary>

#### General

**Track probabilities by the current head count.** Let `dp[h]` be the probability that the coins processed so far have produced exactly `h` heads. Before any toss, `dp[0] = 1` and every positive head count has probability zero. Counts above `target` never need to be stored because later tosses cannot reduce the number of heads.

**Combine the two outcomes of each coin.** For a coin with head probability `p`, ending with `h` heads can happen in two disjoint ways: the previous state already had `h` heads and this coin lands tails, or the previous state had `h - 1` heads and this coin lands heads. Update `dp[h]` to `dp[h] * (1 - p) + dp[h - 1] * p`.

**Update head counts from high to low.** Descending order preserves every previous-layer value until it has supplied all transitions that need it. After updating positive counts, multiply `dp[0]` by `1 - p`, since zero heads remains possible only through another tail.

The two transition cases partition all outcome sequences according to the current coin's result. Induction over the processed coins therefore makes every `dp[h]` the exact probability of `h` heads, and `dp[target]` is the requested value after the final toss.

#### Complexity detail

For each of the $n$ coins, at most $t$ positive head-count states are updated, giving $O(nt)$ time. The rolling array contains $t+1$ probabilities, so auxiliary space is $O(t)$.

#### Alternatives and edge cases

- **Enumerate every outcome subset:** Summing the probability of each subset with exactly `target` heads is correct but takes $O(2^n)$ time.
- **Two-dimensional dynamic programming:** Storing one row per coin follows the same recurrence but uses $O(nt)$ space.
- **Zero target:** Only the zero-head state is needed, and its value becomes the product of all tail probabilities.
- **Target equal to `n`:** Every coin must land heads, so the result is the product of all head probabilities.
- **Certain coin:** A probability of `1` shifts all probability mass up one head; a probability of `0` leaves head counts unchanged.
- **In-place direction:** Updating from low to high would reuse the current coin and overcount outcomes.
- **Floating-point arithmetic:** The recurrence uses ordinary probability additions and multiplications; no modular reduction applies.

</details>
