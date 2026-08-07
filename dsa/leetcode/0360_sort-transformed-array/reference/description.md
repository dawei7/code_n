## Description

Given a **sorted** integer array `nums` and three integers `a`, `b` and `c`, apply a quadratic function of the form $f(x) = ax^2 + bx + c$ to each element $\text{nums}[i]$ in the array, and return *the array in a sorted order*.
### Function Contract

**Inputs**

- `nums`: An integer array sorted in ascending order.
- `a`: The coefficient of $x^2$.
- `b`: The coefficient of $x$.
- `c`: The constant term.

**Return value**

Return the ascending-order array containing `f(nums[i])` for every input position, with duplicate values preserved.

### Examples
#### Example 1

- **Input:** `nums = [-4,-2,2,4], a = 1, b = 3, c = 5`
- **Output:** `[3,9,15,33]`
#### Example 2

- **Input:** `nums = [-4,-2,2,4], a = -1, b = 3, c = 5`
- **Output:** `[-23,-5,1,7]`
### Constraints

- $1 \le \text{nums.length} \le 200$

- $-100 \le \text{nums}[i], a, b, c \le 100$

- `nums` is sorted in **ascending** order.

**Follow up:** Could you solve it in `O(n)` time?