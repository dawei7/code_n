## Description

Given an array `points` where $\text{points}[i] = [x_{i}, y_{i}]$ represents a point on the **X-Y** plane, return `true` *if these points are a **boomerang***.

A **boomerang** is a set of three points that are **all distinct** and **not in a straight line**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $points = [[1,1],[2,3],[3,2]]$
- **Output:** `true`
#### Example 2

- **Input:** $points = [[1,1],[2,2],[3,3]]$
- **Output:** `false`
### Constraints

- $\text{points.length} = 3$

- $\text{points}[i].length = 2$

- $0 \le x_{i}, y_{i} \le 100$