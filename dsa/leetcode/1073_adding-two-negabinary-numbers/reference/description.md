### 1. Description

Given two numbers `arr1` and `arr2` in base **-2**, return the result of adding them together.

Each number is given in *array format*:  as an array of 0s and 1s, from most significant bit to least significant bit.  For example, `arr = [1,1,0,1]` represents the number $(-2)^3 + (-2)^2 + (-2)^0 = -3$.  A number `arr` in *array, format* is also guaranteed to have no leading zeros: either $arr = [0]$ or $\text{arr}[0] = 1$.

Return the result of adding `arr1` and `arr2` in the same format: as an array of 0s and 1s with no leading zeros.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $arr1 = [1,1,1,1,1], arr2 = [1,0,1]$
- **Output:** `[1,0,0,0,0]`
- **Explanation:** arr1 represents 11, arr2 represents 5, the output represents 16.
#### Example 2

- **Input:** $arr1 = [0], arr2 = [0]$
- **Output:** `[0]`
#### Example 3

- **Input:** $arr1 = [0], arr2 = [1]$
- **Output:** `[1]`

### 4. Constraints

- $1 \le \text{arr1.length}, \text{arr2.length} \le 1000$

- $\text{arr1}[i]$ and $\text{arr2}[i]$ are `0` or `1`

- `arr1` and `arr2` have no leading zeros