## Description

Given two arrays of integers with equal lengths, return the maximum value of:

$|\text{arr1}[i] - \text{arr1}[j]| + |\text{arr2}[i] - \text{arr2}[j]| + |i - j|$

where the maximum is taken over all $0 \le i, j < \text{arr1.length}$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $arr1 = [1,2,3,4], arr2 = [-1,4,5,6]$
- **Output:** `13`
#### Example 2

- **Input:** $arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]$
- **Output:** `20`
### Constraints

- $2 \le \text{arr1.length} = \text{arr2.length} \le 40000$

- $-10^{6} \le \text{arr1}[i], \text{arr2}[i] \le 10^{6}$