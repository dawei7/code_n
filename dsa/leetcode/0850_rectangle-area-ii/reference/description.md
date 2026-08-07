### 1. Description

You are given a 2D array of axis-aligned `rectangles`. Each $\text{rectangle}[i] = [x_{i1}, y_{i1}, x_{i2}, y_{i2}]$ denotes the $$i^{\text{th}}$$ rectangle where $(x_{i1}, y_{i1})$ are the coordinates of the **bottom-left corner**, and $(x_{i2}, y_{i2})$ are the coordinates of the **top-right corner**.

Calculate the **total area** covered by all `rectangles` in the plane. Any area covered by two or more rectangles should only be counted **once**.

Return *the **total area***. Since the answer may be too large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/rectangle_area_ii_pic.png)

- **Input:** $rectangles = [[0,0,2,2],[1,0,2,3],[1,0,3,1]]$
- **Output:** `6`
- **Explanation:** A total area of 6 is covered by all three rectangles, as illustrated in the picture.
From (1,1) to (2,2), the green and red rectangles overlap.
From (1,0) to (2,3), all three rectangles overlap.
#### Example 2

- **Input:** $rectangles = [[0,0,1000000000,1000000000]]$
- **Output:** `49`
- **Explanation:** The answer is $10^{18}$ modulo ($10^{9}$ + 7), which is 49.

### 4. Constraints

- $1 \le \text{rectangles.length} \le 200$

- $\text{rectanges}[i].length = 4$

- $0 \le x_{i1}, y_{i1}, x_{i2}, y_{i2} \le 10^{9}$

- $x_{i1} \le x_{i2}$

- $y_{i1} \le y_{i2}$

- All rectangles have non zero area.