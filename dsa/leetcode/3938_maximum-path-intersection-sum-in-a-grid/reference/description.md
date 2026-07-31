## Description

An integer matrix `grid` is crossed by two monotone paths with opposite vertical directions:

- The first path starts at the top-left cell and finishes at the bottom-right cell. At each step, it moves either one cell right or one cell down.
- The second path starts at the bottom-left cell and finishes at the top-right cell. At each step, it moves either one cell right or one cell up.

The **intersection** of a chosen pair of paths consists of every cell visited by both paths. Its score is the sum of the values in those shared cells.

Choose both paths so that their intersection score is as large as possible, and return that maximum score. Matrix values may be negative, so the best intersection is not necessarily the one containing the most cells.
