# Bag of Tokens

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 948 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/bag-of-tokens/) |

## Problem Description

### Goal

You begin with the given amount of `power`, a score of zero, and a bag of unplayed tokens whose integer values are listed in `tokens`. Each token may be played at most once, in exactly one of two orientations.

Playing a token face-up is allowed when the current power is at least its value; this spends that much power and gains one score. Playing a token face-down is allowed when the current score is at least one; this gains power equal to the token's value and loses one score. You may stop after any number of plays. Return the maximum score that can be reached at any point.

### Function Contract

Let $n$ be the number of tokens.

**Inputs**

- `tokens`: a list of $n$ integers with $0 \le n \le 1000$ and `0 <= tokens[i] < 10000`.
- `power`: the initial nonnegative power, with `0 <= power < 10000`.

**Return value**

Return the greatest score achievable by playing each token at most once under the face-up and face-down rules.

### Examples

**Example 1**

- Input: `tokens = [100]`, `power = 50`
- Output: `0`

The token is too expensive to play face-up, and a zero score cannot pay for a face-down play.

**Example 2**

- Input: `tokens = [200, 100]`, `power = 150`
- Output: `1`

Play `100` face-up and stop.

**Example 3**

- Input: `tokens = [100, 200, 300, 400]`, `power = 200`
- Output: `2`

One optimal sequence plays `100` face-up, `400` face-down, then `200` and `300` face-up.

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort to expose the best exchange at each end.** After sorting token values, keep `left` at the cheapest unplayed token and `right` at the most expensive. Also track the current score and the greatest score seen.

If the current power can pay for `ordered[left]`, play that token face-up, advance `left`, and increase the score. Among all affordable face-up choices, the cheapest token gives the same one-point gain while leaving at least as much power for every future action, so choosing it cannot reduce the best attainable score.

If the cheapest token is unaffordable, no remaining token can be bought. When the score is positive and at least two tokens remain, play `ordered[right]` face-down and retreat `right`. Every face-down play costs the same one score, so selling the largest token supplies at least as much power as selling any other token and dominates those alternatives. If neither action is possible, or only one unaffordable token remains, stop.

These exchange arguments allow an optimal play sequence to be transformed so that every face-up play uses the current minimum and every necessary face-down play uses the current maximum. The two-pointer simulation therefore explores an optimal canonical sequence. Record the maximum after face-up plays because a later power trade temporarily lowers the current score.

#### Complexity detail

Sorting $n$ token values costs $O(n\log n)$ time, and the two pointers consume each token at most once in $O(n)$ additional time. The sorted copy contains $n$ values, giving $O(n)$ space.

#### Alternatives and edge cases

- **Sort the input in place:** The same greedy scan can avoid the explicit copied list when mutation is allowed, though the language's sorting implementation may still use auxiliary memory.
- **Search all play sequences:** Dynamic programming or backtracking over token subsets can find the optimum but has exponential state growth.
- **Repeatedly scan for extremes:** Find the cheapest affordable and largest sellable token by scanning all unplayed tokens before every move. It preserves the greedy choices but takes $O(n^2)$ time.
- **Empty bag:** No move is available, so the score remains zero.
- **Zero-valued tokens:** Each can be played face-up without reducing power and contributes one score.
- **Cannot make the first purchase:** With score zero, no face-down play is legal, so the answer is zero.
- **One unaffordable token remains:** Selling it would lower the score without leaving another token to buy, so stopping preserves the maximum.
- **Maximum versus final score:** A valid strategy may trade away a point after reaching its best score; the returned value is the peak, not necessarily the score after every chosen play.

</details>
