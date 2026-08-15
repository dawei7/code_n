### 1. Description

You are given an integer array `nums`.

The **binary reflection** of a **positive** integer is defined as the number obtained by reversing the order of its **binary** digits (ignoring any leading zeros) and interpreting the resulting binary number as a decimal.

Sort the array in **ascending** order based on the binary reflection of each element. If two different numbers have the same binary reflection, the **smaller** original number should appear first.

Return the resulting sorted array.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers to order.

Let $N=\lvert\texttt{nums}\rvert$. For each value $x$, let $R(x)$ denote the decimal value represented by the reversed binary digits of $x$.

**Return value**

Return an array containing every input occurrence, ordered by the key $(R(x),x)$ in ascending lexicographic order. Repeated equal values remain repeated in the result.

### 3. Examples

#### Example 1

- **Input:** nums = [4,5,4]

- **Output:** [4,4,5]

- **Explanation:** Binary reflections are:

- 4 -> (binary) `100` -> (reversed) `001` -> 1

- 5 -> (binary) `101` -> (reversed) `101` -> 5

- 4 -> (binary) `100` -> (reversed) `001` -> 1

Sorting by the reflected values gives `[4, 4, 5]`.

#### Example 2

- **Input:** nums = [3,6,5,8]

- **Output:** [8,3,6,5]

- **Explanation:** Binary reflections are:

- 3 -> (binary) `11` -> (reversed) `11` -> 3

- 6 -> (binary) `110` -> (reversed) `011` -> 3

- 5 -> (binary) `101` -> (reversed) `101` -> 5

- 8 -> (binary) `1000` -> (reversed) `0001` -> 1

Sorting by the reflected values gives `[8, 3, 6, 5]`.

Note that 3 and 6 have the same reflection, so we arrange them in increasing order of original value.

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10^{9}$
