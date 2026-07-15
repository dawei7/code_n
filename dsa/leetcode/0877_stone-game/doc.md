# Stone Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 877 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Game Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game/) |

## Problem Description
### Goal
Alice and Bob play with an even number of piles arranged in a row. Every `piles[i]` is a positive number of stones, and the total number of stones across all piles is odd, so the final scores cannot tie. The objective is to collect more stones than the other player.

Alice moves first, and the players then alternate turns. On each turn, the player removes the entire pile at either the beginning or the end of the remaining row. Play continues until no piles remain. Assuming both players play optimally, return `true` if Alice wins and `false` if Bob wins.

### Function Contract
**Inputs**

- `piles`: an array of an even number $n$ of piles, where $2 \leq n \leq 500$, $1 \leq \texttt{piles[i]} \leq 500$, and the sum of all pile sizes is odd.

**Return value**

Return `true` when Alice wins under optimal play; otherwise, return `false`.

### Examples
**Example 1**

- Input: `piles = [5,3,4,5]`
- Output: `true`

Alice can take an endpoint pile of `5` and preserve a winning response to either of Bob's choices.

**Example 2**

- Input: `piles = [3,7,2,3]`
- Output: `true`

**Example 3**

- Input: `piles = [1,2]`
- Output: `true`

Alice takes the pile containing `2`.

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition the original positions by parity**

Let

$$
E=\sum_{\substack{0\leq i<n\\i\text{ even}}}\texttt{piles[i]}
\qquad\text{and}\qquad
O=\sum_{\substack{0\leq i<n\\i\text{ odd}}}\texttt{piles[i]}.
$$

Because $E+O$ is odd, the two parity sums are unequal. One of them is therefore strictly more than half of all stones.

**Alice can force either parity**

At each of Alice's turns, the remaining row has even length, so its two endpoints came from opposite original index parities. Alice chooses the endpoint belonging to the parity she committed to. Bob then removes one endpoint from the odd-length remainder; regardless of his choice, the next row presented to Alice again has even length and opposite-parity endpoints.

By repeating this response, Alice collects every pile from her chosen original parity. She commits to whichever of $E$ or $O$ is larger and thus receives strictly more than half of all stones. The constraints alone guarantee her win for every valid input, so the requested boolean can be returned without inspecting `piles`.

#### Complexity detail

The result follows directly from the input guarantees, so returning `true` takes $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Interval score dynamic programming:** Storing the best score difference for each remaining interval solves the game generally in $O(n^2)$ time and $O(n)$ or $O(n^2)$ space, but the parity guarantee makes that work unnecessary here.
- **Recursive minimax:** Exploring both endpoint choices without memoization is correct but exponential; memoization reduces it to the interval DP.
- **Compute the parity sums:** If an actual move strategy were requested, scanning the piles would identify which parity Alice should choose, but the boolean winner is already fixed.
- **Two piles:** Alice simply takes the larger endpoint; the odd total guarantees their sizes differ.
- **Odd total:** This guarantee is essential to the constant result because it makes the two parity sums unequal and rules out a tied final score.
- **Optimal Bob:** Bob can choose which individual piles Alice sees next, but he cannot stop her from claiming the committed original parity.

</details>
