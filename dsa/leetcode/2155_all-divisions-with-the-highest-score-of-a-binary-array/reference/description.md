## Description

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i` (where $0 \le i \le n)$ into two arrays (possibly empty) $\text{nums}_{left}$ and $\text{nums}_{right}$:

- $\text{nums}_{left}$ has all the elements of `nums` between index `0` and $i - 1$ **(inclusive)**, while $\text{nums}_{right}$ has all the elements of nums between index `i` and $n - 1$ **(inclusive)**.

- If $i = 0$, $\text{nums}_{left}$ is **empty**, while $\text{nums}_{right}$ has all the elements of `nums`.

- If $i = n$, $\text{nums}_{left}$ has all the elements of nums, while $\text{nums}_{right}$ is **empty**.

The **division score** of an index `i` is the **sum** of the number of `0`'s in $\text{nums}_{left}$ and the number of `1`'s in $\text{nums}_{right}$.

Return ***all distinct indices** that have the **highest** possible **division score***. You may return the answer in **any order**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [0,0,1,0]`
- **Output:** `[2,4]`
- **Explanation:** Division at index
- 0: nums_left is []. nums_right is [0,0,<u>**1**</u>,0]. The score is 0 + 1 = 1.
- 1: nums_left is [<u>**0**</u>]. nums_right is [0,<u>**1**</u>,0]. The score is 1 + 1 = 2.
- 2: nums_left is [<u>**0**</u>,<u>**0**</u>]. nums_right is [<u>**1**</u>,0]. The score is 2 + 1 = 3.
- 3: nums_left is [<u>**0**</u>,<u>**0**</u>,1]. nums_right is [0]. The score is 2 + 0 = 2.
- 4: nums_left is [<u>**0**</u>,<u>**0**</u>,1,<u>**0**</u>]. nums_right is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
#### Example 2

- **Input:** `nums = [0,0,0]`
- **Output:** `[3]`
- **Explanation:** Division at index
- 0: nums_left is []. nums_right is [0,0,0]. The score is 0 + 0 = 0.
- 1: nums_left is [<u>**0**</u>]. nums_right is [0,0]. The score is 1 + 0 = 1.
- 2: nums_left is [<u>**0**</u>,<u>**0**</u>]. nums_right is [0]. The score is 2 + 0 = 2.
- 3: nums_left is [<u>**0**</u>,<u>**0**</u>,<u>**0**</u>]. nums_right is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
#### Example 3

- **Input:** `nums = [1,1]`
- **Output:** `[0]`
- **Explanation:** Division at index
- 0: nums_left is []. nums_right is [<u>**1**</u>,<u>**1**</u>]. The score is 0 + 2 = 2.
- 1: nums_left is [1]. nums_right is [<u>**1**</u>]. The score is 0 + 1 = 1.
- 2: nums_left is [1,1]. nums_right is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{5}$

- $\text{nums}[i]$ is either `0` or `1`.