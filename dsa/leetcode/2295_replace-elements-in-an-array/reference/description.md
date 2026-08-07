## Description

You are given a **0-indexed** array `nums` that consists of `n` **distinct** positive integers. Apply `m` operations to this array, where in the $$i^{\text{th}}$$ operation you replace the number $\text{operations}[i][0]$ with $\text{operations}[i][1]$.

It is guaranteed that in the $$i^{\text{th}}$$ operation:

- $\text{operations}[i][0]$ **exists** in `nums`.

- $\text{operations}[i][1]$ does **not** exist in `nums`.

Return *the array obtained after applying all the operations*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]`
- **Output:** `[3,2,7,1]`
- **Explanation:** We perform the following operations on nums:
- Replace the number 1 with 3. nums becomes [<u>**3**</u>,2,4,6].
- Replace the number 4 with 7. nums becomes [3,2,<u>**7**</u>,6].
- Replace the number 6 with 1. nums becomes [3,2,7,<u>**1**</u>].
We return the final array [3,2,7,1].
#### Example 2

- **Input:** `nums = [1,2], operations = [[1,3],[2,1],[3,2]]`
- **Output:** `[2,1]`
- **Explanation:** We perform the following operations to nums:
- Replace the number 1 with 3. nums becomes [<u>**3**</u>,2].
- Replace the number 2 with 1. nums becomes [3,<u>**1**</u>].
- Replace the number 3 with 2. nums becomes [<u>**2**</u>,1].
We return the array [2,1].
### Constraints

- $n = \text{nums.length}$

- $m = \text{operations.length}$

- $1 \le n, m \le 10^{5}$

- All the values of `nums` are **distinct**.

- $\text{operations}[i].length = 2$

- $1 \le \text{nums}[i], \text{operations}[i][0], \text{operations}[i][1] \le 10^{6}$

- $\text{operations}[i][0]$ will exist in `nums` when applying the $$i^{\text{th}}$$ operation.

- $\text{operations}[i][1]$ will not exist in `nums` when applying the $$i^{\text{th}}$$ operation.