### 1. Description

Given an array of integers `arr`, return `true` if we can partition the array into three **non-empty** parts with equal sums.

Formally, we can partition the array if we can find indexes $i + 1 < j$ with $(\text{arr}[0] + \text{arr}[1] + ... + \text{arr}[i] = arr[i + 1] + arr[i + 2] + ... + arr[j - 1] = \text{arr}[j] + arr[j + 1] + ... + arr[\text{arr.length} - 1])$

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** `arr = [0,2,1,-6,6,-7,9,1,2,0,1]`
- **Output:** `true`
- **Explanation:** 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

#### Example 2

- **Input:** `arr = [0,2,1,-6,6,7,9,-1,2,0,1]`
- **Output:** `false`

#### Example 3

- **Input:** `arr = [3,3,6,5,-2,2,5,1,-9,4]`
- **Output:** `true`
- **Explanation:** 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

### 4. Constraints

- $3 \le \text{arr.length} \le 5 * 10^{4}$

- $-10^{4} \le \text{arr}[i] \le 10^{4}$
