## Description

Given an array `nums` with `n` objects colored red, white, or blue, sort them **<a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> **so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
### Function Contract

**Inputs**

- `nums`: An array whose entries are the color codes `0`, `1`, or `2`.

**Return value**

Return `None`; reorder `nums` in place so all `0` values come first, followed by all `1` values and then all `2` values.

### Examples

#### Example 1

- **Input:** `nums = [2,0,2,1,1,0]`
- **Output:** `[0,0,1,1,2,2]`
#### Example 2

- **Input:** `nums = [2,0,1]`
- **Output:** `[0,1,2]`
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 300$

- $\text{nums}[i]$ is either `0`, `1`, or `2`.

**Follow up:** Could you come up with a one-pass algorithm using only constant extra space?