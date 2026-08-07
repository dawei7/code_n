### 1. Description

Given a string `s`, return whether `s` is a **valid number**.

For example, all the following are valid numbers: `"2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"`, while the following are not valid numbers: `"abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"`.

Formally, a **valid number** is defined using one of the following definitions:

- An **integer number** followed by an **optional exponent**.

- A **decimal number** followed by an **optional exponent**.

An **integer number** is defined with an **optional sign** `'-'` or `'+'` followed by **digits**.

A **decimal number** is defined with an **optional sign** `'-'` or `'+'` followed by one of the following definitions:

- **Digits** followed by a **dot** `'.'`.

- **Digits** followed by a **dot** `'.'` followed by **digits**.

- A **dot** `'.'` followed by **digits**.

An **exponent** is defined with an **exponent notation** `'e'` or `'E'` followed by an **integer number**.

The **digits** are defined as one or more digits.

### 2. Function Contract

**Inputs**

- `s`: The candidate numeric string.

**Return value**

Return `true` exactly when the complete string conforms to one of the accepted integer-or-decimal forms with an optional exponent.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "0"

**Output:** true

</div>
#### Example 2

<div class="example-block">
**Input:** s = "e"

**Output:** false

</div>
#### Example 3

<div class="example-block">
**Input:** s = "."

**Output:** false

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 20$

- `s` consists of only English letters (both uppercase and lowercase), digits (`0-9`), plus `'+'`, minus `'-'`, or dot `'.'`.