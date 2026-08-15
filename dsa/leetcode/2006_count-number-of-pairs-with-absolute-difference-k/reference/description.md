### 1. Description

Given an integer array `nums` and an integer `k`, return *the number of pairs* `(i, j)` *where* `i < j` *such that* $|\text{nums}[i] - \text{nums}[j]| = k$.

The value of `|x|` is defined as:

- `x` if $x \ge 0$.

- `-x` if `x < 0`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,2,1], k = 1`
- **Output:** `4`
- **Explanation:** The pairs with an absolute difference of 1 are:
- [**<u>1</u>**,**<u>2</u>**,2,1]
- [**<u>1</u>**,2,**<u>2</u>**,1]
- [1,**<u>2</u>**,2,**<u>1</u>**]
- [1,2,**<u>2</u>**,**<u>1</u>**]

#### Example 2

- **Input:** `nums = [1,3], k = 3`
- **Output:** `0`
- **Explanation:** There are no pairs with an absolute difference of 3.

#### Example 3

- **Input:** `nums = [3,2,1,5,4], k = 2`
- **Output:** `3`
- **Explanation:** The pairs with an absolute difference of 2 are:
- [**<u>3</u>**,2,**<u>1</u>**,5,4]
- [**<u>3</u>**,2,1,**<u>5</u>**,4]
- [3,**<u>2</u>**,1,5,**<u>4</u>**]

### 4. Constraints

- $1 \le \text{nums.length} \le 200$

- $1 \le \text{nums}[i] \le 100$

- $1 \le k \le 99$
