# Minimum Garden Perimeter to Collect Enough Apples

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1954 |
| Difficulty | Medium |
| Topics | Math, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/) |

## Problem Description
### Goal
An infinite two-dimensional garden has an apple tree at every integer
coordinate $(i,j)$. The tree at that coordinate bears
$\lvert i\rvert+\lvert j\rvert$ apples.

Choose an axis-aligned square plot centered at the origin. Trees on the
boundary count as part of the plot, as do all trees in its interior. Given the
number of apples that must be collected, return the smallest possible
perimeter of such a square whose included trees bear at least that many
apples.

### Function Contract
**Inputs**

- `neededApples`: the required number of apples $A$, where
  $1 \le A \le 10^{15}$.

**Return value**

- The minimum perimeter of an axis-aligned square centered at $(0,0)$ that
  contains at least $A$ apples.

### Examples
**Example 1**

- Input: `neededApples = 1`
- Output: `8`

**Example 2**

- Input: `neededApples = 13`
- Output: `16`

**Example 3**

- Input: `neededApples = 1000000000`
- Output: `5040`

### Required Complexity
- **Time:** $O(\log A)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count apples in a square**

Let $k$ be the half-side length of a candidate square, so its integer
coordinates satisfy $\lvert i\rvert,\lvert j\rvert\le k$ and its perimeter is
$8k$. For a fixed horizontal coordinate, its $\lvert i\rvert$ contribution
appears at all $2k+1$ vertical coordinates. Because

$$
\sum_{i=-k}^{k}\lvert i\rvert=k(k+1),
$$

the horizontal contribution is $(2k+1)k(k+1)$. The vertical contribution is
identical. Therefore the square contains

$$
F(k)=2k(k+1)(2k+1)
$$

apples.

**Find the first sufficient half-side**

The count $F(k)$ strictly increases for nonnegative integer $k$. First double
an upper bound until its square is sufficient. Then binary-search the bounded
interval for the smallest $k$ satisfying $F(k)\ge A$. Every smaller half-side
has too few apples by the search boundary, while the selected half-side is
sufficient, so $8k$ is exactly the minimum perimeter.

#### Complexity detail

Both the exponential search and binary search examine $O(\log A)$ candidate
half-sides. Evaluating $F(k)$ takes constant time, giving $O(\log A)$ time
overall. The search retains only a constant number of integers and therefore
uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Increment the half-side one unit at a time:** This uses constant space and
  the same formula, but needs $\Theta(A^{1/3})$ candidate checks in the worst
  case instead of logarithmically many.
- **Closed-form cubic inversion:** Approximating the root of $F(k)=A$ can find
  a nearby half-side quickly, but floating-point rounding near an exact
  boundary still requires careful integer correction.
- The smallest positive requirement already needs $k=1$, because the
  zero-perimeter square at the origin contains no apples.
- If $A=F(k)$ exactly, half-side $k$ is sufficient; the comparison must not
  require a strict excess.
- Values up to $10^{15}$ require integer arithmetic wide enough for the cubic
  product in $F(k)$.

</details>
