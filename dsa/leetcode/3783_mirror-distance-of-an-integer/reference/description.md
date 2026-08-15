### 1. Description

You are given an integer `n`.

Define its **mirror distance** as: $abs(n - reverse(n))$​​​​​​​ where `reverse(n)` is the integer formed by reversing the digits of `n`.

Return an integer denoting the mirror distance of `n`​​​​​​​.

`abs(x)` denotes the absolute value of `x`.

### 2. Function Contract

**Inputs**

- `n`: A positive integer.

Reversing uses the usual decimal representation. Any zeros that become leading digits after reversal do not change the resulting integer; for example, reversing `10` produces the digit sequence `01`, whose integer value is `1`.

**Return value**

Return the absolute difference between `n` and the integer represented by its reversed decimal digits.

### 3. Examples

#### Example 1

- **Input:** n = 25

- **Output:** 27

- **Explanation:** 

- $reverse(25) = 52$.

- Thus, the answer is $abs(25 - 52) = 27$.

#### Example 2

- **Input:** n = 10

- **Output:** 9

- **Explanation:** 

- $reverse(10) = 01$ which is 1.

- Thus, the answer is $abs(10 - 1) = 9$.

#### Example 3

- **Input:** n = 7

- **Output:** 0

- **Explanation:** 

- $reverse(7) = 7$.

- Thus, the answer is $abs(7 - 7) = 0$.

### 4. Constraints

- $1 \le n \le 10^{9}$
