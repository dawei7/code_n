## Examples

**Example 1**

- **Input:** `operations = ["Excel","set","sum","set","get"], arguments = [[3,"C"],[1,"A",2],[3,"C",["A1","A1:B2"]],[2,"B",2],[3,"C"]]`
- **Output:** `[null,null,4,null,6]`
- **Explanation:** Constructing `Excel(3, "C")` creates a $3 \times 3$ sheet whose cells are all zero.

| row | A | B | C |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |

After `set(1, "A", 2)`, cell `A1` contains `2`.

| row | A | B | C |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 0 |

The call `sum(3, "C", ["A1", "A1:B2"])` counts `A1` once as an individual reference and once inside the range. It therefore stores and returns `4` in `C3`.

| row | A | B | C |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 0 | 0 | 4 |

Finally, `set(2, "B", 2)` changes `B2`. Because the formula in `C3` remains active, `C3` changes to `6`, and `get(3, "C")` returns `6`.

| row | A | B | C |
|---:|---:|---:|---:|
| 1 | 2 | 0 | 0 |
| 2 | 0 | 2 | 0 |
| 3 | 0 | 0 | 6 |
