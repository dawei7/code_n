### 1. Description

You are given a 2D integer array `logs` where each $\text{logs}[i] = [\text{birth}_{i}, \text{death}_{i}]$ indicates the birth and death years of the $i^{\text{th}}$ person.

The **population** of some year `x` is the number of people alive during that year. The $i^{\text{th}}$ person is counted in year `x`'s population if `x` is in the **inclusive** range $[\text{birth}_{i}, \text{death}_{i} - 1]$. Note that the person is **not** counted in the year that they die.

Return *the **earliest** year with the **maximum population***.

### 2. Function Contract

**Inputs**

- `logs`: Input parameter (`List[List[int]]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $logs = [[1993,1999],[2000,2010]]$
- **Output:** `1993`
- **Explanation:** The maximum population is 1, and 1993 is the earliest year with this population.

#### Example 2

- **Input:** $logs = [[1950,1961],[1960,1971],[1970,1981]]$
- **Output:** `1960`
- **Explanation:** The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

### 4. Constraints

- $1 \le \text{logs.length} \le 100$

- $1950 \le \text{birth}_{i} < \text{death}_{i} \le 2050$
