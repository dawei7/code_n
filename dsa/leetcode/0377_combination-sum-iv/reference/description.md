### 1. Description

Given an array of **distinct** integers `nums` and a target integer `target`, return *the number of possible combinations that add up to* `target`.

The test cases are generated so that the answer can fit in a **32-bit** integer.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of distinct positive integers; a value may be chosen repeatedly.
- `target`: The positive sum that each counted sequence must reach.

**Return value**

Return the number of ordered sequences of values from `nums` whose sum equals `target`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3], target = 4`
- **Output:** `7`
- **Explanation:**
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
#### Example 2

- **Input:** `nums = [9], target = 3`
- **Output:** `0`

### 4. Constraints

- $1 \le \text{nums.length} \le 200$

- $1 \le \text{nums}[i] \le 1000$

- All the elements of `nums` are **unique**.

- $1 \le target \le 1000$

**Follow up:** What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?