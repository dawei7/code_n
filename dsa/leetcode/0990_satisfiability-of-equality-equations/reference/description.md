## Description

You are given an array of strings `equations` that represent relationships between variables where each string $\text{equations}[i]$ is of length `4` and takes one of two different forms: $"x_{i} = y_{i}"$ or $"x_{i}\neq y_{i}"$.Here, $x_{i}$ and $y_{i}$ are lowercase letters (not necessarily different) that represent one-letter variable names.

Return `true`* if it is possible to assign integers to variable names so as to satisfy all the given equations, or *`false`* otherwise*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $equations = ["a = b","b\neq a"]$
- **Output:** `false`
- **Explanation:** If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
#### Example 2

- **Input:** $equations = ["b = a","a = b"]$
- **Output:** `true`
- **Explanation:** We could assign a = 1 and b = 1 to satisfy both equations.
### Constraints

- $1 \le \text{equations.length} \le 500$

- $\text{equations}[i].length = 4$

- $\text{equations}[i][0]$ is a lowercase letter.

- $\text{equations}[i][1]$ is either `'='` or `'!'`.

- $\text{equations}[i][2]$ is `'='`.

- $\text{equations}[i][3]$ is a lowercase letter.