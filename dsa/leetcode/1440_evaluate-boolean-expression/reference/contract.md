## Function Contract

**Inputs**

- `Variables(name, value)` contains one uniquely named integer variable per row;
- `Expressions(left_operand, operator, right_operand)` contains uniquely identified comparisons;
- each operand references a name present in `Variables`;
- `operator` is exactly one of `<`, `>`, or `=`.

Let $V$ be the number of rows in `Variables`, and let $E$ be the number of rows in `Expressions`.

**Return value**

Return one row per expression with columns `left_operand`, `operator`, `right_operand`, and `value`. Evaluate the relation between the two referenced integers and set `value` to exactly `true` or `false`. Output order is unrestricted.
