## Function Contract

**Inputs**

- `moves`: A nonempty string whose characters are `U`, `D`, `L`, `R`, or `_`.

Each fixed character contributes its prescribed unit displacement. Every occurrence of `_` may be assigned independently, so different wildcards may use different directions.

Let $x$ be the net rightward displacement from the fixed `R` and `L` commands, let $y$ be the net upward displacement from the fixed `U` and `D` commands, and let $q$ be the number of underscores.

**Return value**

Return the greatest possible value of $\lvert x_{\mathrm{final}}\rvert+\lvert y_{\mathrm{final}}\rvert$ after replacing all $q$ wildcards and performing all moves.
