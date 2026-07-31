## Examples

**Example 1**

- Input: `moves = "L_D_"`
- Output: `4`

- **Explanation:** One maximizing assignment replaces the first underscore with `D` and the second with `L`. The successive positions are `(0, 0) -> (-1, 0) -> (-1, -1) -> (-1, -2) -> (-2, -2)`. The endpoint therefore has distance $\lvert-2\rvert+\lvert-2\rvert=4$ from the origin.

**Example 2**

- Input: `moves = "U_R"`
- Output: `3`

- **Explanation:** Replace the underscore with `U`. The path is `(0, 0) -> (0, 1) -> (0, 2) -> (1, 2)`, so the final Manhattan distance is $\lvert1\rvert+\lvert2\rvert=3$.
