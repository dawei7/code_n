### 1. Description

You are given a string `moves` consisting of the characters `'U'`, `'D'`, `'L'`, `'R'`, and `'_'`.

Starting from the origin `(0, 0)`, each character represents one move on a 2D plane:

- `'U'`: Move up by 1 unit.

- `'D'`: Move down by 1 unit.

- `'L'`: Move left by 1 unit.

- `'R'`: Move right by 1 unit.

- `'_'`: Can be independently replaced with any one of `'U'`, `'D'`, `'L'`, or `'R'`.

Return the maximum **Manhattan distance** from the origin that can be achieved after all moves have been performed.

### 2. Function Contract

**Inputs**

- `moves`: A nonempty string whose characters are `U`, `D`, `L`, `R`, or `_`.

Each fixed character contributes its prescribed unit displacement. Every occurrence of `_` may be assigned independently, so different wildcards may use different directions.

Let $x$ be the net rightward displacement from the fixed `R` and `L` commands, let $y$ be the net upward displacement from the fixed `U` and `D` commands, and let $q$ be the number of underscores.

**Return value**

Return the greatest possible value of $\lvert x_{\mathrm{final}}\rvert+\lvert y_{\mathrm{final}}\rvert$ after replacing all $q$ wildcards and performing all moves.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** moves = "L_D_"

**Output:** 4

**Explanation:**

One optimal choice is:

- `'L'`: `(0, 0) -> (-1, 0)`

- `'_'` treated as `'D'`: `(-1, 0) -> (-1, -1)`

- `'D'`: `(-1, -1) -> (-1, -2)`

- `'_'` treated as `'L'`: `(-1, -2) -> (-2, -2)`

The final Manhattan distance from the origin is $|0 - (-2)| + |0 - (-2)| = 4$.

</div>
#### Example 2

<div class="example-block">
**Input:** moves = "U_R"

**Output:** 3

**Explanation:**

One optimal choice is:

- `'U'`: `(0, 0) -> (0, 1)`

- `'_'` treated as `'U'`: `(0, 1) -> (0, 2)`

- `'R'`: `(0, 2) -> (1, 2)`

The final Manhattan distance from the origin is $|0 - 1| + |0 - 2| = 3$.

</div>

### 4. Constraints

- $1 \le \text{moves.length} \le 10^{5}$

- `moves` consists of only `'U'`, `'D'`, `'L'`, `'R'`, and `'_'`.