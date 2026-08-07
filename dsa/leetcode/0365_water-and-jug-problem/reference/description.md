### 1. Description

You are given two jugs with capacities `x` liters and `y` liters. You have an infinite water supply. Return whether the total amount of water in both jugs may reach `target` using the following operations:

- Fill either jug completely with water.

- Completely empty either jug.

- Pour water from one jug into another until the receiving jug is full, or the transferring jug is empty.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **  x = 3, y = 5, target = 4

**Output: **  true

**Explanation:**

Follow these steps to reach a total of 4 liters:

- Fill the 5-liter jug (0, 5).

- Pour from the 5-liter jug into the 3-liter jug, leaving 2 liters (3, 2).

- Empty the 3-liter jug (0, 2).

- Transfer the 2 liters from the 5-liter jug to the 3-liter jug (2, 0).

- Fill the 5-liter jug again (2, 5).

- Pour from the 5-liter jug into the 3-liter jug until the 3-liter jug is full. This leaves 4 liters in the 5-liter jug (3, 4).

- Empty the 3-liter jug. Now, you have exactly 4 liters in the 5-liter jug (0, 4).

Reference: The <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg&ab_channel=notnek01" target="_blank">Die Hard</a> example.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **  x = 2, y = 6, target = 5

**Output: **  false

</div>

**Example 3: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input: **  x = 1, y = 2, target = 3

**Output: **  true

**Explanation:** Fill both jugs. The total amount of water in both jugs is equal to 3 now.

</div>

### 2. Function Contract

**Inputs**

- `x`: The capacity of the first jug in liters.
- `y`: The capacity of the second jug in liters.
- `target`: The desired total amount across both jugs.

**Return value**

Return `true` if the permitted operations can produce exactly `target` total liters; otherwise return `false`.

### 3. Constraints

- $1 \le x, y, target \le 10^{3}$