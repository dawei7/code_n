### 1. Description

Given an array of integers `arr` and an integer `k`. Find the *least number of unique integers* after removing **exactly** `k` elements**.**

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `arr = [5,5,4], k = 1`
- **Output:** `1`
**Explanation**: Remove the single 4, only 5 is left.

#### Example 2

- **Input:** `arr = [4,3,1,1,3,3,2], k = 3`
- **Output:** `2`
**Explanation**: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.

### 4. Constraints

- $1 \le \text{arr.length} \le 10^{5}$

- $1 \le \text{arr}[i] \le 10^{9}$

- $0 \le k \le \text{arr.length}$
