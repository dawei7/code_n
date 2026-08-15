### 1. Description

Write code that enhances all arrays such that you can call the `upperBound()` method on any array and it will return the last index of a given `target` number. `nums` is a sorted ascending array of numbers that may contain duplicates. If the `target` number is not found in the array, return `-1`.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** `nums = [3,4,5], target = 5`
- **Output:** `2`
- **Explanation:** Last index of target value is 2

#### Example 2

- **Input:** `nums = [1,4,5], target = 2`
- **Output:** `-1`
- **Explanation:** Because there is no digit 2 in the array, return -1.

#### Example 3

- **Input:** `nums = [3,4,6,6,6,6,7], target = 6`
- **Output:** `5`
- **Explanation:** Last index of target value is 5

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-10^{4} \le \text{nums}[i], target \le 10^{4}$

- `nums` is sorted in ascending order.

**Follow up: **Can you write an algorithm with $\mathcal{O}(\log n)$ runtime complexity?
