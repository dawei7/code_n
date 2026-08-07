## Description

You are given two integer arrays `start` and `target`, where each array is of the form `[x, y]` representing a cell on a standard 8 x 8 chessboard.

Return `true` if a knight can move from `start` to `target` in an **even** number of moves. Otherwise, return `false`.

**Note:** A valid knight move consists of moving two squares in one direction and one square perpendicular to it. The figure below illustrates all eight possible moves from a cell.

![](images/knight.png)

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">start = [1,1], target = [2,2]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

One possible sequence of moves is `(1, 1) -> (3, 2) -> (2, 4) -> (4, 3) -> (2, 2)`.

The knight reaches the target in 4 moves, which is even. Thus, the answer is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">start = [4,5], target = [6,6]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**​​​​​​​

It is impossible to reach `target = [6, 6]` from `start = [4, 5]` in an even number of moves. Thus, the answer is `false`.

</div>

**Constraints:**

	- `start.length == target.length == 2`

	- `0 <= start[i], target[i] <= 7`
