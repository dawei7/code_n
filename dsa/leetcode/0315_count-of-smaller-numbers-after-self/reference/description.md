## Description

Given an integer array `nums`, return* an integer array *`counts`* where *$\text{counts}[i]$* is the number of smaller elements to the right of *$\text{nums}[i]$.
### Function Contract

**Inputs**

- `nums`: The integer array whose later elements are counted.

**Return value**

Return an equally long integer array whose position `i` counts indices $j>i$ for which $\text{nums}[j] < \text{nums}[i]$.

### Examples

#### Example 1

- **Input:** `nums = [5,2,6,1]`
- **Output:** `[2,1,1,0]`
- **Explanation:**
To the right of 5 there are **2** smaller elements (2 and 1).
To the right of 2 there is only **1** smaller element (1).
To the right of 6 there is **1** smaller element (1).
To the right of 1 there is **0** smaller element.
#### Example 2

- **Input:** `nums = [-1]`
- **Output:** `[0]`
#### Example 3

- **Input:** `nums = [-1,-1]`
- **Output:** `[0,0]`
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$