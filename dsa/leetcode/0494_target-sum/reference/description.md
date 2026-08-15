### 1. Description

You are given an integer array `nums` and an integer `target`.

You want to build an **expression** out of nums by adding one of the symbols `'+'` and `'-'` before each integer in nums and then concatenate all the integers.

- For example, if `nums = [2, 1]`, you can add a `'+'` before `2` and a `'-'` before `1` and concatenate them to build the expression `"+2-1"`.

Return the number of different **expressions** that you can build, which evaluates to `target`.

### 2. Function Contract

**Inputs**

- `nums`: Input parameter (`List[int]`).
- `target`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,1,1,1,1], target = 3`
- **Output:** `5`
- **Explanation:** There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

#### Example 2

- **Input:** `nums = [1], target = 1`
- **Output:** `1`

### 4. Constraints

- $1 \le \text{nums.length} \le 20$

- $0 \le \text{nums}[i] \le 1000$

- $0 \le sum(\text{nums}[i]) \le 1000$

- $-1000 \le target \le 1000$
