### 1. Description

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is `1`, return *the area of the largest rectangle in the histogram*.

### 2. Function Contract

**Inputs**

- `heights`: The non-negative heights of consecutive unit-width bars.

**Return value**

Return the maximum area of an axis-aligned rectangle covered by consecutive histogram bars.

### 3. Examples

#### Example 1

![](images/histogram.jpg)

- **Input:** $heights = [2,1,5,6,2,3]$
- **Output:** `10`
- **Explanation:** The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
#### Example 2

![](images/histogram-1.jpg)

- **Input:** $heights = [2,4]$
- **Output:** `4`

### 4. Constraints

- $1 \le \text{heights.length} \le 10^{5}$

- $0 \le \text{heights}[i] \le 10^{4}$