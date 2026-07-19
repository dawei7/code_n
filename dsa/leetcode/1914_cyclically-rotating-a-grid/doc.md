# Cyclically Rotating a Grid

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/cyclically-rotating-a-grid/) |
| Frontend ID | 1914 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Matrix, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an $R\times C$ integer matrix in which both dimensions are even. Its cells form nested rectangular layers: the outer border is the first layer, the border remaining after removing it is the next layer, and so on.

One cyclic rotation moves every element of every layer to its adjacent position in the counter-clockwise direction. Apply this operation exactly `k` times to all layers and return the resulting matrix. Layers rotate independently, and their different perimeter lengths mean the same `k` can produce different effective shifts.

### Function Contract

**Inputs**

- `grid`: an $R\times C$ matrix of integers.
- `k`: the positive number of counter-clockwise rotations.
- $2 \le R,C \le 50$, and both $R$ and $C$ are even.
- $1 \le \texttt{grid[row][column]} \le 5000$.
- $1 \le k \le 10^9$.

**Return value**

- Return the matrix after every layer has been rotated counter-clockwise by `k` positions.

### Examples

**Example 1**

- Input: `grid = [[40,10],[30,20]], k = 1`
- Output: `[[10,20],[40,30]]`

Each corner value moves to the next corner in the counter-clockwise direction.

**Example 2**

- Input: `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2`
- Output: `[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]`

The outer and inner layers each advance two positions along their own perimeter.

**Example 3**

- Input: `grid = [[1,2,3,4],[5,6,7,8]], k = 1`
- Output: `[[2,3,4,8],[1,5,6,7]]`

The single rectangular layer has perimeter eight.

### Required Complexity

- **Time:** $O(RC)$
- **Space:** $O(RC)$

<details>
<summary>Approach</summary>

#### General

**Describe one layer in movement order**

For layer `d`, its boundaries are `top = left = d`, `bottom = R - 1 - d`, and `right = C - 1 - d`. Enumerate its coordinates in the direction a value moves under a counter-clockwise rotation:

1. down the left edge, including both corners;
2. right across the bottom edge, excluding the repeated left corner;
3. up the right edge, excluding the repeated bottom corner;
4. left across the top edge, excluding both repeated corners.

Every border cell appears exactly once. Because both dimensions are even, there are $\min(R,C)/2$ complete rectangular layers and no unlayered center row or column.

**Map directly to the final position**

If a layer contains $P$ coordinates, only `k % P` matters. A value at coordinate-list index `i` moves to index `(i + k) % P`, since the list follows the counter-clockwise movement direction. Write each source value directly into that target coordinate of a copied result matrix.

Each layer is disjoint, so these writes cannot conflict. Within a layer, adding a fixed offset modulo $P$ is a permutation: every source reaches one target and every target receives one source. It therefore produces exactly the same arrangement as applying the one-step cyclic move `k` times.

#### Complexity detail

Across all layers, the coordinate lists contain exactly the $RC$ matrix cells. Building the lists and writing the shifted values takes $O(RC)$ time, independent of the magnitude of `k`. The copied result and layer coordinates use $O(RC)$ auxiliary space in the worst case.

#### Alternatives and edge cases

- **Simulate one rotation at a time:** Moving every perimeter once for each of `k` steps is direct but can take $O(kRC)$ time and is infeasible when $k$ is large.
- **In-place cycle decomposition:** Following permutation cycles can reduce auxiliary storage, but careful visited-state and corner handling make it more error-prone.
- **Perimeter multiple:** If `k % P == 0`, that layer remains unchanged even though other layers may move.
- **Two-row or two-column grid:** The grid has one thin layer; corner exclusion is essential to avoid duplicate coordinates.
- **Different layer perimeters:** Reduce `k` separately for every layer.
- **Repeated values:** Equal values do not change the coordinate mapping and may make a rotation visually indistinguishable.

</details>
