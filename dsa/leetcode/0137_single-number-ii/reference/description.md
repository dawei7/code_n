## Description

Given an integer array `nums` where every element appears **three times** except for one, which appears **exactly once**. *Find the single element and return it*.

You must implement a solution with a linear runtime complexity and use only constant extra space.
### Function Contract

**Inputs**

- `nums`: An integer array satisfying the triples-plus-one frequency guarantee.

**Return value**

Return the unique element that occurs exactly once.

### Examples

#### Example 1

- **Input:** `nums = [2,2,3,2]`
- **Output:** `3`
#### Example 2

- **Input:** `nums = [0,1,0,1,0,1,99]`
- **Output:** `99`
### Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$

- Each element in `nums` appears exactly **three times** except for one element which appears **once**.