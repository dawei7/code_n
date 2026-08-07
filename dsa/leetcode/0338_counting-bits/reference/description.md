### 1. Description

Given an integer `n`, return *an array *`ans`* of length *$n + 1$* such that for each *`i`* *($0 \le i \le n$)*, *$\text{ans}[i]$* is the **number of ***`1`***'s** in the binary representation of *`i`.

Do not solve it with built-in functions (i.e., like `__builtin_popcount` in C++).

### 2. Function Contract

**Inputs**

- `n`: The nonnegative upper endpoint of the integers to examine.

**Return value**

Return an array of length $n + 1$ whose value at index `i` is the count of `1` bits in $i$.

### 3. Examples

#### Example 1

- **Input:** $n = 2$
- **Output:** `[0,1,1]`
- **Explanation:**
0 --> 0
1 --> 1
2 --> 10
#### Example 2

- **Input:** $n = 5$
- **Output:** `[0,1,1,2,1,2]`
- **Explanation:**
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

### 4. Constraints

- $0 \le n \le 10^{5}$

**Follow up:**

- It is very easy to come up with a solution with a runtime of `O(n log n)`. Can you do it in linear time `O(n)` and possibly in a single pass?