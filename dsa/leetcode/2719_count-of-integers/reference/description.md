### 1. Description

You are given two numeric strings `num1` and `num2` and two integers $\text{max}_{sum}$ and $\text{min}_{sum}$. We denote an integer `x` to be *good* if:

- $num1 \le x \le num2$

- $\text{min}_{sum} \le \text{digit}_{sum}(x) \le \text{max}_{sum}$.

Return *the number of good integers*. Since the answer may be large, return it modulo $10^{9} + 7$.

Note that $\text{digit}_{sum}(x)$ denotes the sum of the digits of `x`.

### 2. Function Contract

**Inputs**

- `num1`: Input parameter (`str`).
- `num2`: Input parameter (`str`).
- `min_sum`: Input parameter (`int`).
- `max_sum`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $num1 = "1", num2 = "12", \text{min}_{sum} = 1, \text{max}_{sum} = 8$
- **Output:** `11`
- **Explanation:** There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.

#### Example 2

- **Input:** $num1 = "1", num2 = "5", \text{min}_{sum} = 1, \text{max}_{sum} = 5$
- **Output:** `5`
- **Explanation:** The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.

### 4. Constraints

- $1 \le num1 \le num2 \le 10^{22}$

- $1 \le \text{min}_{sum} \le \text{max}_{sum} \le 400$
