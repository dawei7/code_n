# Reach a Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 754 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/reach-a-number/) |

## Problem Description

### Goal

You start at position `0` on an infinite number line and want to reach integer `target`. On the `i`th move, beginning with $i = 1$, choose either direction and travel exactly `i` positions left or right.

Return the minimum number of moves required to land exactly on `target`. The direction may change independently on every move, but the move distance is fixed by its one-based move number; passing the target during an earlier move is allowed.

### Function Contract

**Inputs**

- `target`: an integer position, possibly negative or zero.

**Return value**

- The minimum count of successively longer signed moves whose sum equals `target`.

### Examples

**Example 1**

- Input: `target = 2`
- Output: `3`
- Explanation: Moves `+1`, `-2`, and `+3` finish at `2`.

**Example 2**

- Input: `target = 3`
- Output: `2`
- Explanation: Moving `+1` and then `+2` reaches `3` directly.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Use symmetry to target a non-negative distance**

Reflecting every chosen direction negates the final position without changing the move count. Work with `distance = abs(target)`.

**Characterize what a fixed number of moves can reach**

If all `m` moves point right, their sum is the triangular number $S = m(m + 1) / 2$. Reversing move `i` changes the total by `2i`. Therefore `distance` is reachable in `m` moves exactly when `S >= distance` and `S - distance` is even. The numbers `1` through `m` can form every subset sum from `0` through `S`, so an even excess can always be removed by reversing moves whose lengths sum to `(S - distance) / 2`.

**Jump directly to the first large enough triangular number**

Solve `m(m + 1) / 2 >= distance` using the integer square root of `1 + 8 * distance`, then correct upward by at most one step. If the excess is odd, add moves until its parity becomes even. At most two additional moves are needed: adding the next move toggles parity when that move is odd, and otherwise the following move toggles it.

The initial `m` is the smallest with enough total distance, and the parity loop chooses the first such `m` whose signed moves can equal the target. Every smaller count fails either the magnitude or parity condition, so the returned count is minimum.

#### Complexity detail

On the word-RAM model for the bounded integer input, the integer-square-root calculation and at most three corrections use a constant number of operations, giving $O(1)$ time. Only a few integer variables are stored, giving $O(1)$ space.

#### Alternatives and edge cases

- **Accumulate steps one by one:** Stop when the triangular sum is large enough with matching parity; this is simple and correct but takes $O(\sqrt{|target|})$ iterations.
- **Binary search for the first triangular bound:** This avoids the square-root formula but uses $O(\log |target|)$ time before the parity correction.
- **Breadth-first search over positions:** It explores many duplicate states and is unnecessary once magnitude and parity are recognized.
- **Negative target:** Absolute value is sufficient because every route can be reflected.
- **Target zero:** No move is needed, so return `0`.
- **Odd excess:** Reaching or passing the magnitude alone is insufficient; signed sums preserve the triangular sum's parity.

</details>
