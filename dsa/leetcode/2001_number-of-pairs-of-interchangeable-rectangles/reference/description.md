## Description

You are given `n` rectangles represented by a **0-indexed** 2D integer array `rectangles`, where `rectangles[i] = [width_i, height_i]` denotes the width and height of the `i^th` rectangle.

Two rectangles `i` and `j` (`i < j`) are considered **interchangeable** if they have the **same** width-to-height ratio. More formally, two rectangles are **interchangeable** if `width_i/height_i == width_j/height_j` (using decimal division, not integer division).

Return *the **number** of pairs of **interchangeable** rectangles in *`rectangles`.
