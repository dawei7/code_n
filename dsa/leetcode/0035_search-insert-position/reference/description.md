## Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.
### Function Contract

**Inputs**

- `nums`: An ascending array whose integer values are distinct.
- `target`: The integer to find or position for insertion.

**Return value**

Return the existing index of `target`, or its order-preserving insertion index if it is absent.

### Examples
#### Example 1

- **Input:** `nums = [1,3,5,6], target = 5`
- **Output:** `2`
#### Example 2

- **Input:** `nums = [1,3,5,6], target = 2`
- **Output:** `1`
#### Example 3

- **Input:** `nums = [1,3,5,6], target = 7`
- **Output:** `4`
### Constraints

- $1 \le \text{nums.length} \le 10^{4}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- `nums` contains **distinct** values sorted in **ascending** order.

- $-10^{4} \le target \le 10^{4}$