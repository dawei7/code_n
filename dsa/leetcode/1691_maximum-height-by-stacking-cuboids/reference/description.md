## Description

Given `n` `cuboids` where the dimensions of the `i^th` cuboid is `cuboids[i] = [width_i, length_i, height_i]` (**0-indexed**). Choose a **subset** of `cuboids` and place them on each other.

You can place cuboid `i` on cuboid `j` if `width_i <= width_j` and `length_i <= length_j` and `height_i <= height_j`. You can rearrange any cuboid's dimensions by rotating it to put it on another cuboid.

Return *the **maximum height** of the stacked* `cuboids`.
