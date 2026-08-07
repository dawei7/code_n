## Description

You are given an array `apple` of size `n` and an array `capacity` of size `m`.

There are `n` packs where the $$i^{\text{th}}$$pack contains$\text{apple}[i]$apples. There are `m` boxes as well, and the$$i^{\text{th}}$$box has a capacity of$\text{capacity}[i]$ apples.

Return *the **minimum** number of boxes you need to select to redistribute these *`n`* packs of apples into boxes*.

**Note** that, apples from the same pack can be distributed into different boxes.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $apple = [1,3,2], capacity = [4,3,1,5,2]$
- **Output:** `2`
- **Explanation:** We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
#### Example 2

- **Input:** $apple = [5,5,5], capacity = [2,4,2,7]$
- **Output:** `4`
- **Explanation:** We will need to use all the boxes.
### Constraints

- $1 \le n = \text{apple.length} \le 50$

- $1 \le m = \text{capacity.length} \le 50$

- $1 \le \text{apple}[i], \text{capacity}[i] \le 50$

- The input is generated such that it's possible to redistribute packs of apples into boxes.