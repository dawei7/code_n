### 1. Description

You are given an array of `n` integers, `nums`, where there are at most `50` unique values in the array. You are also given an array of `m` customer order quantities, `quantity`, where $\text{quantity}[i]$ is the amount of integers the $i^{\text{th}}$ customer ordered. Determine if it is possible to distribute `nums` such that:

- The $i^{\text{th}}$ customer gets **exactly** $\text{quantity}[i]$ integers,

- The integers the $i^{\text{th}}$ customer gets are **all equal**, and

- Every customer is satisfied.

Return `true`* if it is possible to distribute *`nums`* according to the above conditions*.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `quantity`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3,4], quantity = [2]`
- **Output:** `false`
- **Explanation:** The 0^th customer cannot be given two different integers.

#### Example 2

- **Input:** `nums = [1,2,3,3], quantity = [2]`
- **Output:** `true`
- **Explanation:** The 0^th customer is given [3,3]. The integers [1,2] are not used.

#### Example 3

- **Input:** `nums = [1,1,2,2], quantity = [2,2]`
- **Output:** `true`
- **Explanation:** The 0^th customer is given [1,1], and the 1st customer is given [2,2].

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums}[i] \le 1000$

- $m = \text{quantity.length}$

- $1 \le m \le 10$

- $1 \le \text{quantity}[i] \le 10^{5}$

- There are at most `50` unique values in `nums`.
