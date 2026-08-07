### 1. Description

*(This problem is an **interactive problem**.)*

You may recall that an array `arr` is a **mountain array** if and only if:

- $\text{arr.length} \ge 3$

- There exists some `i` with $0 < i < \text{arr.length} - 1$ such that:

		<li>$\text{arr}[0] < \text{arr}[1] < ... < arr[i - 1] < \text{arr}[i]$

- $\text{arr}[i] > arr[i + 1] > ... > arr[\text{arr.length} - 1]$

	</li>

Given a mountain array `mountainArr`, return the **minimum** `index` such that $\text{mountainArr.get}(index) = target$. If such an `index` does not exist, return `-1`.

**You cannot access the mountain array directly.** You may only access the array using a `MountainArray` interface:

- `MountainArray.get(k)` returns the element of the array at index `k` (0-indexed).

- `MountainArray.length()` returns the length of the array.

Submissions making more than `100` calls to `MountainArray.get` will be judged *Wrong Answer*. Also, any solutions that attempt to circumvent the judge will result in disqualification.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $mountainArr = [1,2,3,4,5,3,1], target = 3$
- **Output:** `2`
- **Explanation:** 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
#### Example 2

- **Input:** $mountainArr = [0,1,2,4,2,1], target = 3$
- **Output:** `-1`
- **Explanation:** 3 does not exist in the array, so we return -1.

### 4. Constraints

- $3 \le \text{mountainArr.length}() \le 10^{4}$

- $0 \le target \le 10^{9}$

- $0 \le \text{mountainArr.get}(index) \le 10^{9}$