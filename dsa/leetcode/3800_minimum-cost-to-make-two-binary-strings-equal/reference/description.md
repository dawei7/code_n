### 1. Description

You are given two binary strings `s` and `t`, both of length `n`, and three **positive** integers `flipCost`, `swapCost`, and `crossCost`.

You are allowed to apply the following operations any number of times (in any order) to the strings `s` and `t`:

- Choose any index `i` and flip $s[i]$ or $t[i]$ (change `'0'` to `'1'` or `'1'` to `'0'`). The cost of this operation is `flipCost`.

- Choose two **distinct** indices `i` and `j`, and swap either $s[i]$ and $s[j]$ or $t[i]$ and $t[j]$. The cost of this operation is `swapCost`.

- Choose an index `i` and swap $s[i]$ with $t[i]$. The cost of this operation is `crossCost`.

Return an integer denoting the **minimum** total cost needed to make the strings `s` and `t` equal.

### 2. Function Contract

**Inputs**

- `s`: A binary string of length $n$.
- `t`: A binary string with the same length as `s`.
- `flipCost`: The positive cost of flipping one bit in either string.
- `swapCost`: The positive cost of swapping two different positions within one string.
- `crossCost`: The positive cost of swapping the two bits at the same position across the strings.

Both strings may be changed, and the permitted operations may be repeated and interleaved freely.

**Return value**

Return an integer equal to the smallest possible sum of operation costs that leaves `s` and `t` identical at every index.

### 3. Examples

#### Example 1

- **Input:** s = "01000", t = "10111", flipCost = 10, swapCost = 2, crossCost = 2

- **Output:** 16

- **Explanation:** We can perform the following operations:

- Swap $s[0]$ and $s[1]$ ($swapCost = 2$). After this operation, `s = "10000"` and $t = "10111"$.

- Cross swap $s[2]$ and $t[2]$ ($crossCost = 2$). After this operation, `s = "10100"` and $t = "10011"$.

- Swap $s[2]$ and $s[3]$ ($swapCost = 2$). After this operation, `s = "10010"` and $t = "10011"$.

- Flip $s[4]$ ($flipCost = 10$). After this operation, $s = t = "10011"$.

The total cost is $2 + 2 + 2 + 10 = 16$.

#### Example 2

- **Input:** s = "001", t = "110", flipCost = 2, swapCost = 100, crossCost = 100

- **Output:** 6

- **Explanation:** Flipping all the bits of `s` makes the strings equal, and the total cost is $3 * flipCost = 3 * 2 = 6$.

#### Example 3

- **Input:** s = "1010", t = "1010", flipCost = 5, swapCost = 5, crossCost = 5

- **Output:** 0

- **Explanation:** The strings are already equal, so no operations are required.

### 4. Constraints

- $n = \text{s.length} = \text{t.length}$

- $1 \le n \le 10^{5}$

- $1 \le flipCost, swapCost, crossCost \le 10^{9}$

- `s` and `t` consist only of the characters `'0'` and `'1'`.
