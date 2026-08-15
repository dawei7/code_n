### 1. Description

Given three integer arrays `a`, `b`, and `c`, return the number of triplets $(a[i], b[j], c[k])$, such that the bitwise `XOR` of the elements of each triplet has an **even** number of set bits.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** a = [1], b = [2], c = [3]

- **Output:** 1

- **Explanation:** The only triplet is $(a[0], b[0], c[0])$ and their `XOR` is: $1 XOR 2 XOR 3 = \text{00}_{2}$.

#### Example 2

- **Input:** a = [1,1], b = [2,3], c = [1,5]

- **Output:** 4

- **Explanation:** Consider these four triplets:

- $(a[0], b[1], c[0])$: $1 XOR 3 XOR 1 = \text{011}_{2}$

- $(a[1], b[1], c[0])$: $1 XOR 3 XOR 1 = \text{011}_{2}$

- $(a[0], b[0], c[1])$: $1 XOR 2 XOR 5 = \text{110}_{2}$

- $(a[1], b[0], c[1])$: $1 XOR 2 XOR 5 = \text{110}_{2}$

### 4. Constraints

- $1 \le \text{a.length}, \text{b.length}, \text{c.length} \le 100$

- $0 \le a[i], b[i], c[i] \le 100$
