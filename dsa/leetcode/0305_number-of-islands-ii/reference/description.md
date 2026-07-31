## Description

Start with an $m \times n$ binary grid in which every cell is water (`0`). An add-land operation changes the cell at a supplied position into land (`1`). The array `positions` lists these operations in order, with `positions[i] = [r_i,c_i]` identifying the cell changed by operation $i$.

Return an integer array `answer` such that `answer[i]` is the number of islands after the operation at `(r_i,c_i)`.

An island consists of horizontally or vertically adjacent land cells and is surrounded by water. The four outer edges of the grid may also be treated as water.
