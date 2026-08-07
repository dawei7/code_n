## Description

A cell `(r, c)` of an excel sheet is represented as a string `"<col><row>"` where:

- `<col>` denotes the column number `c` of the cell. It is represented by **alphabetical letters**.

		<li>For example, the $1^st$ column is denoted by `'A'`, the $2^nd$ by `'B'`, the $3^rd$ by `'C'`, and so on.

	</li>
- `<row>` is the row number `r` of the cell. The $$r^{\text{th}}$$ row is represented by the **integer** `r`.

You are given a string `s` in the format `"<col1><row1>:<col2><row2>"`, where `<col1>` represents the column `c1`, `<row1>` represents the row `r1`, `<col2>` represents the column `c2`, and `<row2>` represents the row `r2`, such that $r1 \le r2$ and $c1 \le c2$.

Return *the **list of cells*** `(x, y)` *such that* $r1 \le x \le r2$ *and* $c1 \le y \le c2$. The cells should be represented as **strings** in the format mentioned above and be sorted in **non-decreasing** order first by columns and then by rows.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/ex1drawio.png)

- **Input:** `s = "K1:L2"`
- **Output:** `["K1","K2","L1","L2"]`
- **Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrows denote the order in which the cells should be presented.
#### Example 2

![](images/exam2drawio.png)

- **Input:** `s = "A1:F1"`
- **Output:** `["A1","B1","C1","D1","E1","F1"]`
- **Explanation:**
The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.
### Constraints

- $\text{s.length} = 5$

- $'A' \le s[0] \le s[3] \le 'Z'$

- $'1' \le s[1] \le s[4] \le '9'$

- `s` consists of uppercase English letters, digits and `':'`.