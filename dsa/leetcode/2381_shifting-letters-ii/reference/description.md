## Description

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where $\text{shifts}[i] = [\text{start}_{i}, \text{end}_{i}, \text{direction}_{i}]$. For every `i`, **shift** the characters in `s` from the index $\text{start}_{i}$ to the index $\text{end}_{i}$ (**inclusive**) forward if $\text{direction}_{i} = 1$, or shift the characters backward if $\text{direction}_{i} = 0$.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to *`s`* are applied*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]`
- **Output:** `"ace"`
- **Explanation:** Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".
#### Example 2

- **Input:** `s = "dztz", shifts = [[0,0,0],[1,1,1]]`
- **Output:** `"catz"`
- **Explanation:** Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".
### Constraints

- $1 \le \text{s.length}, \text{shifts.length} \le 5 * 10^{4}$

- $\text{shifts}[i].length = 3$

- $0 \le \text{start}_{i} \le \text{end}_{i} < \text{s.length}$

- $0 \le \text{direction}_{i} \le 1$

- `s` consists of lowercase English letters.