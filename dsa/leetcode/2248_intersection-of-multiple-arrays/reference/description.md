## Description

Given a 2D integer array `nums` where $\text{nums}[i]$ is a non-empty array of **distinct** positive integers, return *the list of integers that are present in **each array** of* `nums`* sorted in **ascending order***.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [[<u>**3**</u>,1,2,<u>**4**</u>,5],[1,2,<u>**3**</u>,<u>**4**</u>],[<u>**3**</u>,<u>**4**</u>,5,6]]`
- **Output:** `[3,4]`
- **Explanation:**
The only integers present in each of nums[0] = [<u>**3**</u>,1,2,<u>**4**</u>,5], nums[1] = [1,2,<u>**3**</u>,<u>**4**</u>], and nums[2] = [<u>**3**</u>,<u>**4**</u>,5,6] are 3 and 4, so we return [3,4].
#### Example 2

- **Input:** `nums = [[1,2,3],[4,5,6]]`
- **Output:** `[]`
- **Explanation:**
There does not exist any integer present both in nums[0] and nums[1], so we return an empty list [].
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $1 \le sum(\text{nums}[i].length) \le 1000$

- $1 \le \text{nums}[i][j] \le 1000$

- All the values of $\text{nums}[i]$ are **unique**.