## Description

A decimal number can be converted to its **Hexspeak representation** by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit `'0'` with the letter `'O'`, and the digit `'1'` with the letter `'I'`. Such a representation is valid if and only if it consists only of the letters in the set `{'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}`.

Given a string `num` representing a decimal integer `n`, *return the **Hexspeak representation** of *`n`* if it is valid, otherwise return *`"ERROR"`.
### Function Contract

**Input**

- `num`: a string containing the base-ten representation of a positive integer $n$, without leading zeros.

Let $d = \lfloor \log_{16} n \rfloor + 1$ be the number of digits in the uppercase hexadecimal representation of $n$.

**Return value**

- Return the Hexspeak representation after mapping every hexadecimal `0` to `O` and every hexadecimal `1` to `I`, provided that all remaining digits are uppercase letters from `A` through `F`.
- Return `"ERROR"` when any hexadecimal digit is from `2` through `9`.

### Examples

#### Example 1

- **Input:** $num = "257"$
- **Output:** `"IOI"`
- **Explanation:** 257 is 101 in hexadecimal.
#### Example 2

- **Input:** $num = "3"$
- **Output:** `"ERROR"`
### Constraints

- $1 \le \text{num.length} \le 12$

- `num` does not contain leading zeros.

- num represents an integer in the range $[1, 10^{12}]$.