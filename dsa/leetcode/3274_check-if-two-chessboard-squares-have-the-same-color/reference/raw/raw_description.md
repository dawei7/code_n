## Description

You are given two strings, `coordinate1` and `coordinate2`, representing the coordinates of a square on an `8 x 8` chessboard.

Below is the chessboard for reference.

![](images/screenshot-2021-02-20-at-22159-pm.png)

Return `true` if these two squares have the same color and `false` otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">coordinate1 = "a1", coordinate2 = "c3"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

Both squares are black.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">coordinate1 = "a1", coordinate2 = "h3"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

Square `"a1"` is black and `"h3"` is white.

</div>

**Constraints:**

	- `coordinate1.length == coordinate2.length == 2`

	- `'a' <= coordinate1[0], coordinate2[0] <= 'h'`

	- `'1' <= coordinate1[1], coordinate2[1] <= '8'`
