### 1. Description

Given an array of integers `arr`.

We want to select three indices `i`, `j` and `k` where $(0 \le i < j \le k < \text{arr.length})$.

Let's define `a` and `b` as follows:

- $a = \text{arr}[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]$

- $b = \text{arr}[j] ^ arr[j + 1] ^ ... ^ \text{arr}[k]$

Note that **^** denotes the **bitwise-xor** operation.

Return *the number of triplets* (`i`, `j` and `k`) Where $a = b$.

### 2. Function Contract

**Inputs**

- `arr`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `arr = [2,3,1,6,7]`
- **Output:** `4`
- **Explanation:** The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

#### Example 2

- **Input:** `arr = [1,1,1,1,1]`
- **Output:** `10`

### 4. Constraints

- $1 \le \text{arr.length} \le 300$

- $1 \le \text{arr}[i] \le 10^{8}$
