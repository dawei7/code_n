### 1. Description

You are given a **0-indexed binary** string `floor`, which represents the colors of tiles on a floor:

- $\text{floor}[i] = '0'$ denotes that the $$i^{\text{th}}$$ tile of the floor is colored **black**.

- On the other hand, $\text{floor}[i] = '1'$ denotes that the $$i^{\text{th}}$$ tile of the floor is colored **white**.

You are also given `numCarpets` and `carpetLen`. You have `numCarpets` **black** carpets, each of length `carpetLen` tiles. Cover the tiles with the given carpets such that the number of **white** tiles still visible is **minimum**. Carpets may overlap one another.

Return *the **minimum** number of white tiles still visible.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/ex1-1.png)

- **Input:** $floor = "10110101", numCarpets = 2, carpetLen = 2$
- **Output:** `2`
- **Explanation:**
The figure above shows one way of covering the tiles with the carpets such that only 2 white tiles are visible.
No other way of covering the tiles with the carpets can leave less than 2 white tiles visible.
#### Example 2

![](images/ex2.png)

- **Input:** $floor = "11111", numCarpets = 2, carpetLen = 3$
- **Output:** `0`
- **Explanation:**
The figure above shows one way of covering the tiles with the carpets such that no white tiles are visible.
Note that the carpets are able to overlap one another.

### 4. Constraints

- $1 \le carpetLen \le \text{floor.length} \le 1000$

- $\text{floor}[i]$ is either `'0'` or `'1'`.

- $1 \le numCarpets \le 1000$