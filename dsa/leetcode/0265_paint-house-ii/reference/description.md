## Description

The houses form a row, and every house must be painted with one of `k` colors. Painting costs depend on both the house and the chosen color. A valid plan paints every house while ensuring that neighboring houses never share a color.

The `n x k` matrix `costs` records these prices: `costs[i][j]` is the cost of assigning color `j` to house `i`. For example, `costs[0][0]` refers to color `0` on house `0`, while `costs[1][2]` refers to color `2` on house `1`.

Return the minimum total cost among all valid painting plans.
