## Function Contract

**Inputs**

- `s`: a valid expression string containing only decimal digits, `+`, `-`, `*`, `/`, `(`, and `)`.

Every literal is non-negative. Parentheses determine grouping, multiplication and division bind more tightly than addition and subtraction, and equal-precedence operators are evaluated from left to right. The validity guarantee means that every operation, including division, is defined.

**Return value**

- The integer value of the complete expression, using truncation toward zero for every division.
