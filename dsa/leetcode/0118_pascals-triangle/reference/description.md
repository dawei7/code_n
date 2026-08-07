## Description

Given an integer `numRows`, return the first numRows of **Pascal's triangle**.

In **Pascal's triangle**, each number is the sum of the two numbers directly above it as shown:

![](images/PascalTriangleAnimated2.gif)
### Function Contract

**Inputs**

- `numRows`: The positive number of rows to generate.

**Return value**

Return the requested rows as a top-to-bottom list of integer lists.

### Examples
#### Example 1

- **Input:** $numRows = 5$
- **Output:** `[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]`
#### Example 2

- **Input:** $numRows = 1$
- **Output:** `[[1]]`
### Constraints

- $1 \le numRows \le 30$