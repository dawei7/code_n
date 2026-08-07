## Description

You are given an integer array `nums` of length `n` and an integer `numSlots` such that $2 * numSlots \ge n$. There are `numSlots` slots numbered from `1` to `numSlots`.

You have to place all `n` integers into the slots such that each slot contains at **most** two numbers. The **AND sum** of a given placement is the sum of the **bitwise** `AND` of every number with its respective slot number.

- For example, the **AND sum** of placing the numbers `[1, 3]` into slot <u>`1`</u> and `[4, 6]` into slot <u>`2`</u> is equal to $(1 AND <u>1</u>) + (3 AND <u>1</u>) + (4 AND <u>2</u>) + (6 AND <u>2</u>) = 1 + 1 + 0 + 2 = 4$.

Return *the maximum possible **AND sum** of *`nums`* given *`numSlots`* slots.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `nums = [1,2,3,4,5,6], numSlots = 3`
- **Output:** `9`
- **Explanation:** One possible placement is [1, 4] into slot <u>1</u>, [2, 6] into slot <u>2</u>, and [3, 5] into slot <u>3</u>.
This gives the maximum AND sum of (1 AND <u>1</u>) + (4 AND <u>1</u>) + (2 AND <u>2</u>) + (6 AND <u>2</u>) + (3 AND <u>3</u>) + (5 AND <u>3</u>) = 1 + 0 + 2 + 2 + 3 + 1 = 9.
#### Example 2

- **Input:** `nums = [1,3,10,4,7,1], numSlots = 9`
- **Output:** `24`
- **Explanation:** One possible placement is [1, 1] into slot <u>1</u>, [3] into slot <u>3</u>, [4] into slot <u>4</u>, [7] into slot <u>7</u>, and [10] into slot <u>9</u>.
This gives the maximum AND sum of (1 AND <u>1</u>) + (1 AND <u>1</u>) + (3 AND <u>3</u>) + (4 AND <u>4</u>) + (7 AND <u>7</u>) + (10 AND <u>9</u>) = 1 + 1 + 3 + 4 + 7 + 8 = 24.
Note that slots 2, 5, 6, and 8 are empty which is permitted.
### Constraints

- $n = \text{nums.length}$

- $1 \le numSlots \le 9$

- $1 \le n \le 2 * numSlots$

- $1 \le \text{nums}[i] \le 15$