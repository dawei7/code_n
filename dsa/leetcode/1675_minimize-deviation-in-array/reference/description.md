### 1. Description

You are given an array `nums` of `n` positive integers.

You can perform two types of operations on any element of the array any number of times:

- If the element is **even**, **divide** it by `2`.

		<li>For example, if the array is `[1,2,3,4]`, then you can do this operation on the last element, and the array will be $[1,2,3,<u>2</u>].$

	</li>
- If the element is **odd**, **multiply** it by `2`.

		<li>For example, if the array is `[1,2,3,4]`, then you can do this operation on the first element, and the array will be `[<u>2</u>,2,3,4].`

	</li>

The **deviation** of the array is the **maximum difference** between any two elements in the array.

Return *the **minimum deviation** the array can have after performing some number of operations.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,2,3,4]`
- **Output:** `1`
- **Explanation:** You can transform the array to [1,2,3,<u>2</u>], then to [<u>2</u>,2,3,2], then the deviation will be 3 - 2 = 1.
#### Example 2

- **Input:** `nums = [4,1,5,20,3]`
- **Output:** `3`
- **Explanation:** You can transform the array after two operations to [4,<u>2</u>,5,<u>5</u>,3], then the deviation will be 5 - 2 = 3.
#### Example 3

- **Input:** `nums = [2,10,8]`
- **Output:** `3`

### 4. Constraints

- $n = \text{nums.length}$

- $2 \le n \le 5 * 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$