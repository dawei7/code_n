### 1. Description

You are given a 2D integer array `stockPrices` where $\text{stockPrices}[i] = [\text{day}_{i}, \text{price}_{i}]$ indicates the price of the stock on day $\text{day}_{i}$ is $\text{price}_{i}$. A **line chart** is created from the array by plotting the points on an XY plane with the X-axis representing the day and the Y-axis representing the price and connecting adjacent points. One such example is shown below:

![](images/1920px-pushkin_population_historysvg.png)

Return *the **minimum number of lines** needed to represent the line chart*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/ex0.png)

- **Input:** $stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]$
- **Output:** `3`
- **Explanation:**
The diagram above represents the input, with the X-axis representing the day and Y-axis representing the price.
The following 3 lines can be drawn to represent the line chart:
- Line 1 (in red) from (1,7) to (4,4) passing through (1,7), (2,6), (3,5), and (4,4).
- Line 2 (in blue) from (4,4) to (5,4).
- Line 3 (in green) from (5,4) to (8,1) passing through (5,4), (6,3), (7,2), and (8,1).
It can be shown that it is not possible to represent the line chart using less than 3 lines.
#### Example 2

![](images/ex1.png)

- **Input:** $stockPrices = [[3,4],[1,2],[7,8],[2,3]]$
- **Output:** `1`
- **Explanation:**
As shown in the diagram above, the line chart can be represented with a single line.

### 4. Constraints

- $1 \le \text{stockPrices.length} \le 10^{5}$

- $\text{stockPrices}[i].length = 2$

- $1 \le \text{day}_{i}, \text{price}_{i} \le 10^{9}$

- All $\text{day}_{i}$ are **distinct**.