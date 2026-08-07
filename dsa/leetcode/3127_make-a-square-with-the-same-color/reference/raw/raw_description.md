## Description

You are given a 2D matrix `grid` of size `3 x 3` consisting only of characters `'B'` and `'W'`. Character `'W'` represents the white color<!-- notionvc: 06a49cc0-a296-4bd2-9bfe-c8818edeb53a -->, and character `'B'` represents the black color<!-- notionvc: 06a49cc0-a296-4bd2-9bfe-c8818edeb53a -->.

Your task is to change the color of **at most one** cell<!-- notionvc: c04cb478-8dd5-49b1-80bb-727c6b1e0232 --> so that the matrix has a `2 x 2` square where all cells are of the same color.<!-- notionvc: adf957e1-fa0f-40e5-9a2e-933b95e276a7 -->

Return `true` if it is possible to create a `2 x 2` square of the same color, otherwise, return `false`.

<style type="text/css">.grid-container {
  display: grid;
  grid-template-columns: 30px 30px 30px;
  padding: 10px;
}
.grid-item {
  background-color: black;
  border: 1px solid gray;
  height: 30px;
  font-size: 30px;
  text-align: center;
}
.grid-item-white {
  background-color: white;
}
</style>
<style class="darkreader darkreader--sync" media="screen" type="text/css">
</style>
**Example 1:**

<div class="grid-container">
<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>
</div>

<div class="example-block">
**Input:** <span class="example-io">grid = [["B","W","B"],["B","W","W"],["B","W","B"]]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

It can be done by changing the color of the `grid[0][2]`.

</div>

**Example 2:**

<div class="grid-container">
<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>
</div>

<div class="example-block">
**Input:** <span class="example-io">grid = [["B","W","B"],["W","B","W"],["B","W","B"]]</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

It cannot be done by changing at most one cell.

</div>

**Example 3:**

<div class="grid-container">
<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item"> </div>

<div class="grid-item grid-item-white"> </div>

<div class="grid-item grid-item-white"> </div>
</div>

<div class="example-block">
**Input:** <span class="example-io">grid = [["B","W","B"],["B","W","W"],["B","W","W"]]</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The `grid` already contains a `2 x 2` square of the same color.<!-- notionvc: 9a8b2d3d-1e73-457a-abe0-c16af51ad5c2 -->

</div>

**Constraints:**

	- `grid.length == 3`

	- `grid[i].length == 3`

	- `grid[i][j]` is either `'W'` or `'B'`.
