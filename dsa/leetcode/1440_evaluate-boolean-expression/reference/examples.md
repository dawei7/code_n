## Examples

**Example 1**

- **Input:** `Variables = [["x",66],["y",77]], Expressions = [["x",">","y"],["x","<","y"],["x","=","y"],["y",">","x"],["y","<","x"],["x","=","x"]]`

| name | value |
|---|---:|
| `x` | 66 |
| `y` | 77 |

| left_operand | operator | right_operand |
|---|:---:|---|
| `x` | `>` | `y` |
| `x` | `<` | `y` |
| `x` | `=` | `y` |
| `y` | `>` | `x` |
| `y` | `<` | `x` |
| `x` | `=` | `x` |

- **Output:** `[["x",">","y","false"],["x","<","y","true"],["x","=","y","false"],["y",">","x","true"],["y","<","x","false"],["x","=","x","true"]]`

| left_operand | operator | right_operand | value |
|---|:---:|---|:---:|
| `x` | `>` | `y` | `false` |
| `x` | `<` | `y` | `true` |
| `x` | `=` | `y` | `false` |
| `y` | `>` | `x` | `true` |
| `y` | `<` | `x` | `false` |
| `x` | `=` | `x` | `true` |

- **Explanation:** Look up both named variables for each expression and apply its stored comparison. With `x = 66` and `y = 77`, for example, `x < y` and `y > x` are true, while `x > y`, `x = y`, and `y < x` are false; comparing `x` with itself using `=` is true.
