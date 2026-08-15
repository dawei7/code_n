### 1. Description

You are given an integer `n`.

An integer is called **Monobit** if all bits in its binary representation are the same.

Return the count of **Monobit** integers in the range `[0, n]` (inclusive).

### 2. Function Contract

**Inputs**

- `n`: A nonnegative integer that forms the inclusive upper endpoint of the range.

Let $N=\texttt{n}+1$, the number of integers in `[0, n]`.

Binary representations are the ordinary forms without leading zeroes. In particular, zero is represented by `"0"`.

**Return value**

Return how many integers from `0` through `n`, including both endpoints, have a binary representation made entirely from one repeated bit.

### 3. Examples

#### Example 1

- **Input:** n = 1

- **Output:** 2

- **Explanation:** 

- The integers in the range `[0, 1]` have binary representations `"0"` and `"1"`.

- Each representation consists of identical bits. Thus, the answer is 2.

#### Example 2

- **Input:** n = 4

- **Output:** 3

- **Explanation:** 

- The integers in the range `[0, 4]` include binaries `"0"`, `"1"`, `"10"`, `"11"`, and `"100"`.

- Only 0, 1 and 3 satisfy the Monobit condition. Thus, the answer is 3.

### 4. Constraints

- $0 \le n \le 1000$
