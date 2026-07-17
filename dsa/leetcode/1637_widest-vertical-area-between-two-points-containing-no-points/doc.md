# Widest Vertical Area Between Two Points Containing No Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1637 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/) |

## Problem Description
### Goal
You are given $n$ points on a two-dimensional plane, with `points[i] = [xi, yi]`. A vertical area is a fixed-width strip that extends infinitely in both directions along the y-axis.

Find the maximum width of such a strip whose open interior contains no given point. Points lying on either vertical boundary do not count as being inside the area, so they may define the strip's edges.

### Function Contract
**Inputs**

- `points`: an array of $n$ coordinate pairs, where $2 \le n \le 10^5$.
- Each `points[i]` contains exactly two integers `xi` and `yi`, with $0 \le \texttt{xi},\texttt{yi} \le 10^9$.

**Return value**

Return the greatest possible horizontal width of an infinitely tall vertical area containing no point in its open interior.

### Examples
**Example 1**

- Input: `points = [[8,7],[9,9],[7,4],[9,7]]`
- Output: `1`

The occupied x-coordinates are 7, 8, and 9, so either adjacent gap of width 1 is optimal.

**Example 2**

- Input: `points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]`
- Output: `3`

The empty strip bounded by x-coordinates 5 and 8 has width 3.

**Example 3**

- Input: `points = [[0,4],[10,2]]`
- Output: `10`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Discard the irrelevant coordinate.** A vertical strip extends without limit along the y-axis. Whether a point lies inside it therefore depends only on that point's x-coordinate; changing any y-coordinate cannot change the answer. Extract the $n$ x-coordinates and sort them.

**Only neighboring x-coordinates can bound an empty strip.** Consider any valid strip whose boundaries are occupied x-coordinates $a<b$. If another point has an x-coordinate strictly between them, that point lies inside the strip regardless of its y-coordinate, contradicting validity. Thus $a$ and $b$ must be consecutive in sorted x-coordinate order. Conversely, the open strip between any consecutive pair is empty by definition of consecutiveness, and points on its boundaries are allowed.

Scan adjacent sorted coordinates and return their largest difference. Duplicate x-coordinates contribute a zero gap but require no special handling. Because every valid candidate corresponds to an adjacent pair and every adjacent pair defines a valid candidate, the maximum scanned difference is exactly the widest area.

#### Complexity detail

Extracting coordinates and scanning gaps take $O(n)$ time. Sorting dominates at $O(n\log n)$ time. The extracted sorted array uses $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Sort the points in place:** Sorting full coordinate pairs by their first component avoids a separate extraction pass but mutates the input and has the same asymptotic bounds.
- **Ordered set:** Inserting x-coordinates into a balanced search tree and scanning them also takes $O(n\log n)$ time, with more overhead and no benefit from repeated coordinates.
- **Compare every pair:** Testing all possible boundary pairs is quadratic and still needs a way to establish that no intermediate x-coordinate exists.
- With exactly two points, their absolute x-coordinate difference is the answer, including zero when they share an x-coordinate.
- Multiple points may share one x-coordinate; duplicates create zero-width adjacent gaps and do not hide a wider gap elsewhere.
- Points on a chosen boundary are permitted, while even one point with a strictly intermediate x-coordinate invalidates that strip.
- Extreme y-coordinates have no effect because the strip has infinite height.

</details>
