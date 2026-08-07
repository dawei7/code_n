### 1. Description

You are given two **positive** integers `n` and `k`.

An integer `x` is called **k-palindromic** if:

- `x` is a palindrome.

- `x` is divisible by `k`.

An integer is called **good** if its digits can be *rearranged* to form a **k-palindromic** integer. For example, for $k = 2$, 2020 can be rearranged to form the *k-palindromic* integer 2002, whereas 1010 cannot be rearranged to form a *k-palindromic* integer.

Return the count of **good** integers containing `n` digits.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that *any* integer must **not** have leading zeros, **neither** before **nor** after rearrangement. For example, 1010 *cannot* be rearranged to form 101.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, k = 5

**Output:** 27

**Explanation:**

*Some* of the good integers are:

- 551 because it can be rearranged to form 515.

- 525 because it is already k-palindromic.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 1, k = 4

**Output:** 2

**Explanation:**

The two good integers are 4 and 8.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, k = 6

**Output:** 2468

</div>

### 5. Constraints

- $1 \le n \le 10$

- $1 \le k \le 9$