# Stone Game VIII

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/stone-game-viii/) |
| Frontend ID | 1872 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Prefix Sum, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Alice and Bob alternate turns on a row of stones, with Alice moving first. While more than one stone remains, the current player chooses a prefix containing at least two stones, removes that prefix, adds its total value to their score, and inserts one new stone with that same total at the left end of the remaining row.

The game ends with one stone. Alice chooses moves to maximize `Alice score - Bob score`, while Bob chooses moves to minimize it. Given the initial stone values, which may be negative, return the final score difference under optimal play. A move may combine any legal prefix, including the entire current row.

### Function Contract

**Inputs**

- `stones`: a list of $N$ integers with $2 \le N \le 10^5$ and $-10^4 \le \texttt{stones[i]} \le 10^4$.

**Return value**

- Return Alice's score minus Bob's score when both players choose optimally.

### Examples

**Example 1**

- Input: `stones = [-1,2,-3,4,-5]`
- Output: `5`

Alice can combine the first four stones for `2`; Bob then combines `[2,-5]` for `-3`, giving difference $2-(-3)=5$.

**Example 2**

- Input: `stones = [7,-6,5,10,5,-2,-6]`
- Output: `13`

Alice can combine the entire row immediately and score its total, `13`.

**Example 3**

- Input: `stones = [-10,-12]`
- Output: `-22`

Only one move is legal, so Alice must score the total `-22`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent every possible combined stone by a prefix sum**

After any sequence of moves, the leftmost stone equals the sum of some original prefix. Convert `stones[i]` in place to the prefix total through index `i`. A move that expands the combined prefix through `i` scores exactly this stored value, so the full changing row no longer needs to be simulated.

**Express a move as current gain minus the opponent's advantage**

If the current player takes prefix total $P_i$, the opponent then controls the continuation and can obtain its own optimal score difference. From the current player's perspective, that choice is $P_i$ minus the opponent's advantage. Choosing the entire row gives $P_{N-1}$ with no reply, which initializes `best`.

**Collapse all later choices while scanning backward**

When considering prefix endpoint `i`, the best difference available from endpoints later than `i` is already stored in `best`. The newly available choice produces `P_i - best`; alternatively, the player can retain the previous later choice. Therefore update `best = max(best, P_i - best)` from `i = N-2` down through `1`. Endpoint zero is illegal because a move must remove at least two stones. The final `best` is Alice's optimal difference.

#### Complexity detail

Building prefix sums and scanning them backward each take $O(N)$ time. Both transformations reuse the input array, and the recurrence keeps only one scalar, so auxiliary space is $O(1)$. If preserving the caller's array is required, copying it first changes auxiliary space to $O(N)$ without changing time.

#### Alternatives and edge cases

- **Quadratic game DP:** Evaluating every later prefix choice for every state follows the minimax definition directly but costs $O(N^2)$ time.
- **Recursive simulation:** Materializing each changed stone row creates many overlapping game states and can become exponential without the prefix-state reduction.
- **Two stones:** Only the whole-row move is legal, so the answer is their sum.
- **All-negative values:** A player may still prefer a less negative strategic choice; greedy selection by immediate score is unsafe.
- **Take every stone:** This is always a legal option and supplies the recurrence's base value.
- **Minimum prefix:** Index `1` is the earliest legal endpoint; index `0` must never be considered.
- **Input mutation:** In-place prefix sums are intentional for constant auxiliary space.

</details>
