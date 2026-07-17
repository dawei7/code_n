# Maximum Height by Stacking Cuboids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1691 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-height-by-stacking-cuboids/) |

## Problem Description
### Goal

You are given $n$ cuboids. Each entry `cuboids[i] = [width_i, length_i, height_i]` describes the three dimensions of one distinct cuboid. You may choose any subset, rotate each chosen cuboid by rearranging its dimensions, and place the chosen cuboids in a vertical stack.

An upper cuboid may rest on a lower cuboid only when its width, length, and height are each no greater than the corresponding dimension of the lower cuboid in their selected orientations. The stack's height is the sum of the selected vertical dimensions. Return the maximum height obtainable from a valid stack; each input cuboid can be used at most once.

### Function Contract
**Inputs**

- `cuboids`: a list of $n$ three-integer dimension lists, where $1 \le n \le 100$ and every dimension is between $1$ and $100$

**Return value**

The greatest total vertical height of any compatible stack made from a subset of the cuboids.

### Examples
**Example 1**

- Input: `cuboids = [[50, 45, 20], [95, 37, 53], [45, 23, 12]]`
- Output: `190`

After suitable rotations, all three cuboids fit in one stack with vertical dimensions 95, 50, and 45.

**Example 2**

- Input: `cuboids = [[38, 25, 45], [76, 35, 3]]`
- Output: `76`

Neither cuboid can be placed on the other, so the taller orientation of the second cuboid is optimal by itself.

**Example 3**

- Input: `cuboids = [[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]`
- Output: `102`

All six entries describe the same dimensions under rotation and may be stacked with height 17 each.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Give every rotation one canonical representation**

Sort the three dimensions inside every cuboid into ascending order. Use the first two entries as its horizontal sides and the largest entry as its vertical height. This loses no optimal stack: if one cuboid's dimensions can be paired with another's so every upper dimension is no larger, then their sorted dimension triples have the same coordinatewise relationship. Sorting both triples pairs the smallest with the smallest, the middle with the middle, and the largest with the largest.

The canonical orientation also chooses the largest possible height for every selected cuboid. Because all three sorted coordinates participate in the same containment test, making the largest coordinate vertical does not invalidate a compatible relation that another orientation could achieve.

**Turn the stack into a weighted ordered chain**

Sort the normalized triples lexicographically. If cuboid `top` can be placed on cuboid `bottom`, every coordinate of `top` is at most the corresponding coordinate of `bottom`, so `top` cannot appear after `bottom` in this order. Equal triples remain separate input cuboids and can all be used; their arbitrary relative order is sufficient.

Let `best[bottom]` be the greatest height of a valid stack whose bottom cuboid is `bottom`. Initially that stack contains only the bottom, contributing its largest normalized dimension. For each earlier `top`, test all three coordinate inequalities. When they hold, append `bottom` below the best stack ending at `top` and update with

$$
\texttt{best[bottom]} = \max\bigl(\texttt{best[bottom]},\; \texttt{best[top]} + \texttt{normalized[bottom][2]}\bigr).
$$

Every update preserves coordinatewise compatibility. Conversely, remove the bottom cuboid from any optimal stack ending there: the remaining stack ends at some earlier compatible cuboid whose optimal height has already been recorded. The transition therefore considers its exact predecessor, so induction over the sorted order proves that every `best` value is optimal. The maximum entry allows the chosen subset to end at any cuboid.

#### Complexity detail

Normalizing all triples takes $O(n)$ time, sorting them takes $O(n \log n)$ time, and checking every ordered pair takes $O(n^2)$ time. The DP array and normalized list require $O(n)$ auxiliary space because each cuboid has exactly three dimensions.

#### Alternatives and edge cases

- **Enumerate rotations as separate boxes:** three choices of vertical dimension per cuboid can also model orientations, but the state must prevent reusing the same physical cuboid; canonical normalization avoids that bookkeeping.
- **Repeated edge relaxation:** treating compatible pairs as a DAG and repeatedly relaxing every edge eventually finds the same longest weighted chain, but an unstructured $n$-round method takes $O(n^3)$ time.
- **Greedy by largest height:** selecting the tallest available cuboid can block several shorter compatible cuboids whose combined height is greater.
- **Compare only base dimensions:** the contract also requires the upper vertical dimension to be no greater, so all three normalized coordinates must pass.
- **Identical cuboids:** distinct equal triples may all be stacked because equality is allowed in every dimension.
- **Incomparable triples:** when one cuboid is larger in one coordinate but smaller in another, neither orientation permits the canonical coordinatewise relation and they cannot be adjacent.
- **One cuboid:** rotate its largest dimension vertically; the answer is that dimension.

</details>
