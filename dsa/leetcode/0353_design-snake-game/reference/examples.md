## Examples

**Example 1**

- Input: `operations = ["SnakeGame","move","move","move","move","move","move"], arguments = [[3,2,[[1,2],[0,1]]],["R"],["D"],["R"],["U"],["L"],["U"]]`
- Output: `[null,0,0,1,1,2,-1]`
- Explanation: Start with `SnakeGame(3,2,[[1,2],[0,1]])`. Moving `R` and then `D` leaves the score at `0`. The next `R` reaches `(1,2)`, eats the first food, and returns `1`, causing the second food to appear at `(0,1)`. Moving `U` returns `1`; moving `L` eats the second food and returns `2`. The final `U` crosses the upper border, so it returns `-1`.

```text
head positions:
(0,0) --R--> (0,1) --D--> (1,1) --R--> (1,2) food #1
       --U--> (0,2) --L--> (0,1) food #2 --U--> outside board
scores:          0          0          1          1          2       -1
```
