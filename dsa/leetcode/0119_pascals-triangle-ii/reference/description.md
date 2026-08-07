### 1. Description

Given an integer `rowIndex`, return the $rowIndex^th$ (**0-indexed**) row of the **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](images/PascalTriangleAnimated2.gif)

### 2. Function Contract

**Inputs**

- `rowIndex`: The zero-based Pascal's triangle row to return.

**Return value**

Return the values of the requested row from left to right.

### 3. Examples

#### Example 1

- **Input:** $rowIndex = 3$
- **Output:** `[1,3,3,1]`
#### Example 2

- **Input:** $rowIndex = 0$
- **Output:** `[1]`
#### Example 3

- **Input:** $rowIndex = 1$
- **Output:** `[1,1]`

### 4. Constraints

- $0 \le rowIndex \le 33$

**Follow up:** Could you optimize your algorithm to use only `O(rowIndex)` extra space?