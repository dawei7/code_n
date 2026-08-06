## Description

You are given two integers `n` and `m` representing the number of rows and columns of a grid, respectively.

You are also given a 2D integer array `sources`, where `sources[i] = [r_i, c_i, color_​​​​​​​i]` indicates that the cell `(r_i, c_i)` is initially colored with `color_i`. All other cells are initially uncolored and represented as 0.

At each time step, every currently colored cell spreads its color to all adjacent **uncolored** cells in the four directions: up, down, left, and right. All spreads happen simultaneously.

If **multiple** colors reach the same uncolored cell at the same time step, the cell takes the color with the **maximum** value.

The process continues until no more cells can be colored.

Return a 2D integer array representing the final state of the grid, where each cell contains its final color.
