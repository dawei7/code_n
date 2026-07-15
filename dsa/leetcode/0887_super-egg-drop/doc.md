# Super Egg Drop

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 887 |
| Difficulty | Hard |
| Topics | Math, Binary Search, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/super-egg-drop/) |

## Problem Description
### Goal
You have `k` identical eggs and a building with floors labeled from `1` through `n`. An unknown integer threshold $f$ satisfies $0 \leq f \leq n$: an egg dropped above floor $f$ breaks, while an egg dropped at or below floor $f$ does not break.

In one move, choose any floor from `1` through `n` and drop an unbroken egg there. A broken egg cannot be used again, but an egg that survives remains available. Return the minimum number of moves needed to determine $f$ with certainty, accounting for the worst possible sequence of outcomes.

### Function Contract
**Inputs**

- `k`: the number of identical eggs, where $1 \leq k \leq 100$.
- `n`: the number of floors, where $1 \leq n \leq 10^4$.

**Return value**

Return the minimum worst-case number of egg drops required to identify the threshold floor $f$ exactly.

### Examples
**Example 1**

- Input: `k = 1, n = 2`
- Output: `2`

With one egg, testing floor `1` and then floor `2` when necessary is the only way to distinguish all three possible threshold values.

**Example 2**

- Input: `k = 2, n = 6`
- Output: `3`

**Example 3**

- Input: `k = 3, n = 14`
- Output: `4`

### Required Complexity
- **Time:** $O(k\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Ask how many floors a move budget can resolve**

Let $F(t,e)$ be the greatest number of consecutive floors whose threshold can be determined with $t$ moves and $e$ eggs. At the first tested floor, a break leaves $t-1$ moves and $e-1$ eggs for the floors below, while survival leaves $t-1$ moves and $e$ eggs for the floors above. The tested floor separates those two ranges, so

$$
F(t,e)=F(t-1,e-1)+1+F(t-1,e)
=\sum_{i=1}^{e}\binom{t}{i}.
$$

Terms with $i>t$ are zero. For a fixed candidate `moves`, compute this sum iteratively from one binomial coefficient to the next, stopping as soon as the covered range reaches `n`.

**Binary-search the minimum sufficient budget**

One move can resolve at least one floor, and `n` moves always suffice by testing upward with one egg, so the answer lies in `[1, n]`. Because $F(t,k)$ never decreases as $t$ grows, binary search finds the smallest `moves` for which $F(\texttt{moves},k) \geq n$.

The recurrence describes exactly what one drop can distinguish in its two possible outcomes, so $F(t,e)$ is both achievable and an upper bound for any $t$-move strategy. Consequently, a candidate budget is feasible precisely when its coverage reaches `n`; choosing the first feasible budget therefore gives the minimum worst-case number of moves.

#### Complexity detail

Binary search tests $O(\log n)$ candidate move counts. Each coverage test computes at most $k$ binomial terms and stops early once it reaches `n`, for $O(k\log n)$ time. Only the current coefficient, coverage total, and binary-search bounds are stored, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Dynamic programming by moves:** Repeatedly applying `reachable[e] = reachable[e] + reachable[e - 1] + 1` is concise and uses $O(k)$ space, but costs $O(kT)$ time when the answer is $T$.
- **Floors-and-eggs minimax DP:** Trying every first-drop floor for every state is correct but costs $O(kn^2)$ time without further optimization.
- **Binary search inside each minimax state:** Monotonic break and survive costs reduce the classic state DP to roughly $O(kn\log n)$ time, still more than the coverage formulation needs.
- **One egg:** Every floor must be tested from bottom to top in the worst case, so the answer is `n`.
- **Many eggs:** When eggs are no longer limiting, `moves` outcomes cover up to $2^{\texttt{moves}}-1$ floors.
- **Threshold zero:** If the first tested egg breaks, the remaining search range correctly includes the possibility $f=0$.
- **Threshold at the roof:** The strategy must also distinguish $f=n$, where no tested egg ever breaks.

</details>
