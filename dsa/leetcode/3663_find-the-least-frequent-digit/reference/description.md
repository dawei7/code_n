### 1. Description

Given an integer `n`, find the digit that occurs **least** frequently in its decimal representation. If multiple digits have the same frequency, choose the **smallest** digit.

Return the chosen digit as an integer.

The **frequency** of a digit `x` is the number of times it appears in the decimal representation of `n`.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** n = 1553322

- **Output:** 1

- **Explanation:** The least frequent digit in `n` is 1, which appears only once. All other digits appear twice.

#### Example 2

- **Input:** n = 723344511

- **Output:** 2

- **Explanation:** The least frequent digits in `n` are 7, 2, and 5; each appears only once.

### 4. Constraints

- $1 \le n \le 2^{31}​​​​​​​ - 1$
