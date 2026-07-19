# Sum Game

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sum-game/) |
| Frontend ID | 1927 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String, Greedy, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Alice and Bob play on an even-length string `num` containing decimal digits and question marks. Alice moves first. On each turn, the current player chooses one remaining `"?"` and replaces it with any digit from `0` through `9`. Play ends after every question mark has been replaced.

Bob wins exactly when the sum of the digits in the first half equals the sum in the second half. Alice wins when those sums differ. Assuming both players choose optimally, determine whether Alice has a winning strategy.

### Function Contract

**Inputs**

- `num`: an even-length string containing only digits and `"?"`.
- $2 \le \lvert\texttt{num}\rvert \le 10^5$.

**Return value**

- Return `true` if Alice can force unequal final half sums.
- Return `false` if Bob can force equality.

### Examples

**Example 1**

- Input: `num = "5023"`
- Output: `false`

There are no moves, and both halves sum to five.

**Example 2**

- Input: `num = "25??"`
- Output: `true`

Alice can make equality impossible with her first replacement.

**Example 3**

- Input: `num = "?3295???"`
- Output: `false`

Under optimal replies, Bob can always balance the final sums.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Summarize each half**

Let $S_L$ and $S_R$ be the sums of fixed digits in the left and right halves. Let $Q_L$ and $Q_R$ be their question-mark counts. A single scan computes all four values.

**Handle an odd number of moves**

If $Q_L+Q_R$ is odd, Alice makes both the first and last move. On the final move at most one digit could make the half sums equal, so Alice can choose another digit. She therefore wins.

**Pair moves when the count is even**

With an even number of unknowns, consider Alice's move together with Bob's reply. For two unknowns in the same half, Bob can choose the complementary digit so their combined contribution is nine. For unknowns in opposite halves, he can mirror Alice's digit to cancel their effect on the difference.

After optimal pairing, Bob can force equality precisely when the known difference is offset by half of the unmatched-side contribution:

$$
S_L-S_R+\frac{9}{2}(Q_L-Q_R)=0.
$$

Avoid fractions by testing

$$
2(S_L-S_R)+9(Q_L-Q_R)=0.
$$

If this balance is zero, Bob can maintain the pairing strategy and wins; otherwise Alice can preserve a nonzero difference and wins.

#### Complexity detail

The algorithm visits all $N$ characters once and performs constant work per character, giving $O(N)$ time. It stores four counters and a few scalar values, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Minimax over replacements:** Each question mark branches over ten digits, producing an exponential game tree.
- **Dynamic programming by possible sums:** Tracking turns and half differences uses substantially more than linear time and space.
- **Use only question-mark parity:** An even move count is not sufficient for Bob; the known sum and side imbalance must also match.
- **No question marks:** Alice wins exactly when the already-fixed half sums differ.
- **All question marks:** Equal counts in both halves give zero balance, so Bob wins when the total length is even.
- **Compensated imbalance:** Two extra unknowns on one side can offset a known sum gap of nine.

</details>
