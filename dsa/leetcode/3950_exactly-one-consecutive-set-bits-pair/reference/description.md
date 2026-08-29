### 1. Description

You are given an integer `n`.

Return `true` if its binary representation contains **exactly one adjacent pair** of set bits, and `false` otherwise.

### 2. Function Contract

**Inputs**

- `n`: The integer whose binary representation is examined.

The representation of zero is `0`; positive values use their usual binary representation without leading zeroes.

**Return value**

Return `true` if exactly one neighboring pair of binary digits is `11`; otherwise, return `false`.

### 3. Examples

#### Example 1

- **Input:** n = 6

- **Output:** true

- **Explanation:** 

- Binary representation of 6 is `110`.

- There is exactly one adjacent pair of set bits (`"11"`). Thus, the answer is `true`.

#### Example 2

- **Input:** n = 5

- **Output:** false

- **Explanation:** 

- Binary representation of 5 is `101`.

- There is no adjacent pair of set bits. Thus, the answer is `false`.

### 4. Constraints

- $0 \le n \le 10^{5}$
