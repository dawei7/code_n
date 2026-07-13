# Smallest Rectangle Enclosing Black Pixels

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 302 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Depth-First Search, Breadth-First Search, Matrix |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/) |

## Problem Description
### Goal
Given a nonempty binary image, `"1"` marks a black pixel and `"0"` marks a white pixel. All black pixels form one horizontally or vertically connected component, and coordinates `(x, y)` identify one known black pixel within it.

Find the tightest axis-aligned rectangle whose rows and columns contain every black pixel, then return its area. The rectangle's boundaries are the minimum and maximum occupied row and column, inclusive, even when white pixels lie inside that box. Do not return the perimeter or coordinates. Use the connected-image and known-pixel information to meet the required sublinear search behavior where applicable.

### Function Contract
**Inputs**

- `image`: a nonempty rectangular grid containing character `"0"` for white and `"1"` for black
- `x`: the row of a known black pixel
- `y`: the column of that pixel

**Return value**

The area of the tightest rectangle covering all black pixels.

### Examples
**Example 1**

- Input: `image = ["0010","0110","0100"], x = 0, y = 2`
- Output: `6`

**Example 2**

- Input: `image = ["1"], x = 0, y = 0`
- Output: `1`

**Example 3**

- Input: `image = ["01110"], x = 0, y = 2`
- Output: `3`

### Required Complexity

- **Time:** $O(m \log n + n \log m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Connected pixels have contiguous row and column projections**

Project every black pixel onto the row axis. Because the component is connected by horizontal and vertical steps, a path between its minimum and maximum black rows visits every intermediate row. Rows containing black pixels therefore form one contiguous interval. The same argument makes black-containing columns a contiguous interval.

The known pixel `(x, y)` lies inside both intervals. This provides an anchor for four binary searches: the first black column at or before `y`, the first white-only column after the black interval, and the analogous top and bottom row boundaries.

**Search for transitions rather than individual pixels**

To test a candidate column, scan its rows and ask whether any cell is black. On $[0,y]$, that predicate changes from false to true, so lower-bound search finds the left boundary. On $[y+1,n]$, it changes from true to false, so the complementary lower-bound search finds the exclusive right boundary.

Row searches use the same logic while scanning across columns. Once the boundaries are `left`, `right`, `top`, and `bottom`, the rectangle area is `(right - left) * (bottom - top)`.

For `["0010","0110","0100"]`, black rows span `0..2` and black columns span `1..2`. The exclusive boundaries give height three and width two, hence area six.

**Four exact boundaries determine the unique tight rectangle**

Each lower-bound search retains the relevant predicate transition because the connected component makes the searched half monotone around the known black row or column. The returned left and top indices contain black pixels, while their preceding indices do not; right and bottom are the first indices beyond the black projection.

Any enclosing rectangle must include these minimum and maximum black coordinates, so it cannot be narrower or shorter. The rectangle formed by them contains every black pixel by definition, making its area minimal.

#### Complexity detail

Each column predicate scans `m` rows and is evaluated $O(\log n)$ times for each horizontal boundary. Each row predicate scans `n` columns and is evaluated $O(\log m)$ times for each vertical boundary. Total time is $O(m \log n + n \log m)$, and the searches use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Scan the complete image:** is simple and correct but costs $O(mn)$ even when the component is tiny.
- **DFS or BFS from the known pixel:** visits only the connected component and can be attractive for sparse images, but requires $O(k)$ visited or traversal space in the worst case.
- A single black pixel has area one. Components touching an image edge need no sentinel cell because exclusive search bounds may equal `m` or `n`.

</details>
