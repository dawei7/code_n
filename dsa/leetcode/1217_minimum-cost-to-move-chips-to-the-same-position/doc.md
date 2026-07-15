# Minimum Cost to Move Chips to The Same Position

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1217 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/) |

## Problem Description

### Goal

There are $n$ chips on a number line, and the $i$th chip is currently at `position[i]`. All chips must be moved to one common position.

In one step, a chip at `position[i]` may move to `position[i] + 2` or `position[i] - 2` at cost `0`. It may instead move to `position[i] + 1` or `position[i] - 1` at cost `1`. Any number of steps may be applied to each chip.

Return the minimum total cost needed to move all chips to the same position.

### Function Contract

**Inputs**

- `position`: A list containing the positions of $n$ chips, where $1\le n\le100$ and $1\le\texttt{position[i]}\le10^9$.

**Return value**

- The minimum total movement cost required to gather every chip at one position.

### Examples

**Example 1**

- Input: `position = [1,2,3]`
- Output: `1`

The chip at `3` can move to `1` by two units for free. Moving the chip at `2` to `1` costs `1`.

**Example 2**

- Input: `position = [2,2,2,3,3]`
- Output: `2`

Move both chips at `3` to `2`; each one-unit move costs `1`.

**Example 3**

- Input: `position = [1,1000000000]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce every position to its parity.** A free move changes a position by two, so repeated free moves can carry a chip to any other position of the same parity. They can never change an odd position into an even one or vice versa. Thus the exact coordinate and the distance between coordinates do not affect the paid cost.

**Choose which parity receives all chips.** If the common destination is even, every even-positioned chip arrives for free and every odd-positioned chip needs exactly one paid one-unit move before free moves finish the journey. The total is therefore the number of odd chips. An odd destination symmetrically costs the number of even chips, so return the smaller count.

**Why no cheaper arrangement exists.** Every chip whose starting parity differs from the destination's parity must cross between parity classes at least once, and only a one-unit move can do that, establishing the stated lower bound. One such paid move per mismatched chip followed by free two-unit moves attains the bound. Comparing the only two destination parities is consequently sufficient for the global minimum.

#### Complexity detail

One pass counts the $n$ chip parities, taking $O(n)$ time. Only the odd and even counts are stored, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Evaluate every occupied destination:** Computing the cost for each chip position is correct but repeats the parity count and takes $O(n^2)$ time.
- **Simulate individual moves:** Distances can be as large as $10^9$, so step-by-step movement performs unnecessary work and hides the parity invariant.
- **All positions share a parity:** Every chip can reach one of the occupied positions for free, so the answer is `0` even when the coordinates are far apart.
- **One chip:** It is already gathered and costs `0`.
- **Duplicate positions:** Each list entry is a separate chip and must contribute independently to its parity count.
- **Equal parity counts:** Either an odd or even destination attains the same minimum.

</details>
