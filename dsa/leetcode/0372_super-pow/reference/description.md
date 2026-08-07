### 1. Description

Your task is to calculate $a^b$ mod `1337` where `a` is a positive integer and `b` is an extremely large positive integer given in the form of an array.

### 2. Function Contract

**Inputs**

- `a`: The positive integer base.
- `b`: The decimal digits of the positive exponent, from most significant to least significant.

**Return value**

Return the remainder of $a^b$ after division by `1337`.

### 3. Examples

#### Example 1

- **Input:** $a = 2, b = [3]$
- **Output:** `8`
#### Example 2

- **Input:** $a = 2, b = [1,0]$
- **Output:** `1024`
#### Example 3

- **Input:** $a = 1, b = [4,3,3,8,5,2]$
- **Output:** `1`

### 4. Constraints

- $1 \le a \le 2^{31} - 1$

- $1 \le \text{b.length} \le 2000$

- $0 \le b[i] \le 9$

- `b` does not contain leading zeros.