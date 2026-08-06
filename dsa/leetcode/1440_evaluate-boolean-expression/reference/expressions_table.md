## Expressions Table

| Column Name | Type |
|---|---|
| `left_operand` | varchar |
| `operator` | enum |
| `right_operand` | varchar |

The composite primary key is (`left_operand`, `operator`, `right_operand`). Each row represents one Boolean expression to evaluate. `operator` is one of `<`, `>`, or `=`, and both operand names are guaranteed to occur in `Variables`.
