## Description

You are given an integer array `nums` and two integers `a` and `b` such that `a < b`.

An array is called **good** if it can be split into three **contiguous** parts, in this order, such that:

- Every element in the first part is **less than** `a`.

- Every element in the second part is **in** the range `[a, b]` inclusive.

- Every element in the third part is **greater than** `b`.

Any of the three parts **may be** empty.

In one **adjacent swap**, you may swap two **neighboring** elements of `nums`.

Return the **minimum number** of adjacent swaps required to make `nums` good. Since the answer may be very large, return it **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.
- `a`: The inclusive lower boundary of the middle part.
- `b`: The inclusive upper boundary of the middle part.

The boundaries satisfy `a < b`. Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

Return the minimum number of neighboring-element swaps that can arrange all values less than `a` first, all values in `[a, b]` next, and all values greater than `b` last. Return the count modulo $10^9+7$.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,3,2,4,5,6], a = 3, b = 4

**Output:** 1

**Explanation:**

- Swap $\text{nums}[1]$ and $\text{nums}[2]$. The array becomes `[1, 2, 3, 4, 5, 6]`.

- This array is good because it can be split into `[1, 2]`, `[3, 4]`, and `[5, 6]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [9,7,5,3], a = 4, b = 8

**Output:** 5

**Explanation:**

One sequence of optimal swaps is as follows:

- Swap $\text{nums}[2]$ and $\text{nums}[3]$. The array becomes `[9, 7, 3, 5]`.

- Swap $\text{nums}[1]$ and $\text{nums}[2]$. The array becomes `[9, 3, 7, 5]`.

- Swap $\text{nums}[0]$ and $\text{nums}[1]$. The array becomes `[3, 9, 7, 5]`.

- Swap $\text{nums}[1]$ and $\text{nums}[2]$. The array becomes `[3, 7, 9, 5]`.

- Swap $\text{nums}[2]$ and $\text{nums}[3]$. The array becomes `[3, 7, 5, 9]`.

- This array is good because it can be split into `[3]`, `[7, 5]`, and `[9]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [3,7,5,9], a = 4, b = 8

**Output:** 0

**Explanation:**

The array is already good. No swaps are needed.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $​​​​​​​1 \le \text{nums}[i] \le 10^{9}$

- $1 \le a < b \le 10^{9}​​​​​​​$