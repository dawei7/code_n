## Description

You are given the array `paths`, where $\text{paths}[i] = [\text{cityA}_{i}, \text{cityB}_{i}]$ means there exists a direct path going from $\text{cityA}_{i}$ to $\text{cityB}_{i}$. *Return the destination city, that is, the city without any path outgoing to another city.*

It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]$
- **Output:** `"Sao Paulo"`
- **Explanation:** Starting at "London" city you will reach "Sao Paulo" city which is the destination city. Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".
#### Example 2

- **Input:** $paths = [["B","C"],["D","B"],["C","A"]]$
- **Output:** `"A"`
- **Explanation:** All possible trips are:
"D" -> "B" -> "C" -> "A".
"B" -> "C" -> "A".
"C" -> "A".
"A".
Clearly the destination city is "A".
#### Example 3

- **Input:** $paths = [["A","Z"]]$
- **Output:** `"Z"`
### Constraints

- $1 \le \text{paths.length} \le 100$

- $\text{paths}[i].length = 2$

- $1 \le \text{cityA}_{i}.length, \text{cityB}_{i}.length \le 10$

- $\text{cityA}_{i} \neq \text{cityB}_{i}$

- All strings consist of lowercase and uppercase English letters and the space character.