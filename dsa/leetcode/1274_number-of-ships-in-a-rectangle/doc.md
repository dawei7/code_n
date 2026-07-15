# Number of Ships in a Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1274 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ships-in-a-rectangle/) |

## Problem Description

### Goal

Ships occupy distinct integer-coordinate points in a Cartesian plane. Their locations are hidden, so they cannot be read or enumerated directly. Instead, the supplied `Sea` interface provides `hasShips(topRight, bottomLeft)`, which reports whether at least one ship lies inside or on the boundary of the inclusive axis-aligned rectangle between those corners.

Given `topRight` and `bottomLeft`, return the exact number of ships in that rectangle. There are at most $10$ ships in the requested region, and a solution that calls `hasShips` more than $400$ times is rejected.

### Function Contract

**Inputs**

- `sea`: a hidden `Sea` object exposing only `hasShips(topRight, bottomLeft)` for rectangular existence queries.
- `top_right`: a `Point` whose `x` and `y` fields give the target rectangle's upper-right coordinate $(x_2,y_2)$.
- `bottom_left`: a `Point` whose fields give the lower-left coordinate $(x_1,y_1)$, where $0 \le x_1 \le x_2 \le 1000$ and $0 \le y_1 \le y_2 \le 1000$.
- At most $s=10$ distinct ships lie in the target rectangle. Let $C=\max(x_2-x_1+1,y_2-y_1+1)$ be its larger side length.

**Return value**

- Return the number of hidden ship points inside the target rectangle, including its boundary.

### Examples

**Example 1**

- Input: `ships = [[1,1],[2,2],[3,3],[5,5]], top_right = [4,4], bottom_left = [0,0]`
- Output: `3`

**Example 2**

- Input: `ships = [[1,1],[2,2],[3,3]], top_right = [1000,1000], bottom_left = [0,0]`
- Output: `3`

**Example 3**

- Input: `ships = [], top_right = [7,9], bottom_left = [2,4]`
- Output: `0`

### Required Complexity

- **Time:** $O(s \log C)$
- **Space:** $O(\log C)$

<details>
<summary>Approach</summary>

#### General

**Use the oracle to prune empty water**

For a rectangle with valid corner order, first ask `sea.hasShips` whether it contains anything. A negative answer proves that the entire region contributes zero, regardless of its area. If a positive rectangle has shrunk to one coordinate, that point contains exactly one ship.

**Split occupied rectangles without overlap**

Otherwise choose the midpoint of each coordinate range and partition the rectangle into four disjoint quadrants. The left quadrants end at `mid_x`, while the right quadrants begin at `mid_x + 1`; similarly, the lower quadrants end at `mid_y` and the upper ones begin at `mid_y + 1`. Skip any quadrant whose corners are inverted. Recursively count the remaining quadrants and add their results.

Every ship belongs to exactly one child because the four coordinate ranges neither overlap nor leave gaps. Empty children return zero after one oracle query. Repeated halving eventually reduces every occupied path to a single point, which contributes one. Therefore the sum counts every ship in the original rectangle exactly once. Because only branches whose rectangles still contain ships continue splitting, the sparse search stays within the interface's $400$-query budget for the legal grid and ship limits.

#### Complexity detail

At each of $O(\log C)$ levels, only rectangles associated with the at most $s$ ships can remain active; each active rectangle creates at most four constant-time oracle queries. The work is therefore $O(s \log C)$. Depth-first recursion stores one path plus constant local state per level, requiring $O(\log C)$ auxiliary space.

The legal values satisfy $s \le 10$ and $C \le 1001$. Those fixed limits, together with the explicit $400$-query contract, make honest runtime scaling unsuitable; the package uses bounded-domain proof and boundary-property regression instead.

#### Alternatives and edge cases

- **Query every coordinate:** It is simple but can make more than one million calls and violates the $400$-query limit.
- **Split along only one axis:** It can work, but four-way subdivision reduces both coordinate ranges together and gives the required shallow search on a two-dimensional grid.
- **Overlapping midpoint quadrants:** Including the midpoint in both sides double-counts ships and can prevent progress; one side must start at the midpoint plus one.
- **Empty target rectangle:** The initial oracle call returns false, so the answer is `0` immediately.
- **Single coordinate:** A positive oracle result means that exact point holds one ship.
- **Ships on boundaries:** The oracle is inclusive, and the non-overlapping quadrant boundaries assign each such ship to exactly one child.
- **Narrow rectangles:** Invalid quadrants created when one dimension has length one must be skipped rather than queried.

</details>
