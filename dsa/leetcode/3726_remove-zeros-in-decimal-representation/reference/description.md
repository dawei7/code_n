### 1. Description

You are given a **positive** integer `n`.

Return the integer obtained by removing all zeros from the decimal representation of `n`.

### 2. Function Contract

**Inputs**

- `n`: The positive integer whose decimal zero digits are removed.

The relative order of every nonzero digit must remain unchanged. Because `n` is positive, its representation contains at least one nonzero digit, so the result is always a positive integer.

**Return value**

Return the base-ten integer formed by concatenating all nonzero digits of `n` in their original order.

### 3. Examples

#### Example 1

- **Input:** n = 1020030

- **Output:** 123

- **Explanation:** After removing all zeros from 1**<u>0</u>**2**<u>00</u>**3**<u>0</u>**, we get 123.

#### Example 2

- **Input:** n = 1

- **Output:** 1

- **Explanation:** 1 has no zero in its decimal representation. Therefore, the answer is 1.

### 4. Constraints

- $1 \le n \le 10^{15}$
