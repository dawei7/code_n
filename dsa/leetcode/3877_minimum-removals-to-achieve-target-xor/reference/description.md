## Description

You are given an integer array `nums` and an integer `target`.

You may remove **any** number of elements from `nums` (possibly zero).

Return the **minimum** number of removals required so that the **bitwise XOR** of the remaining elements equals `target`. If it is impossible to achieve `target`, return -1.

The bitwise XOR of an empty array is 0.
### Function Contract

**Inputs**

- `nums`: The array from which any subset of indexed elements may be removed.
- `target`: The required XOR of the elements that remain.

Removing elements preserves the relative order of those retained, but XOR is order-independent. Equal values at different indices remain separate choices.

Let $n=\lvert\texttt{nums}\rvert$ and let $b=14$, the number of bits needed to represent every legal value and target. Every attainable subset XOR lies in $[0,2^b)$.

**Return value**

Return the smallest number of removed indices whose complementary retained subset has XOR `target`. Return `-1` when no retained subset—including the empty subset—has that XOR.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3], target = 2

**Output:** 1

**Explanation:**

- Removing $\text{nums}[1] = 2$ leaves `[nums[0], nums[2]] = [1, 3]`.

- The XOR of `[1, 3]` is 2, which equals `target`.

- It is not possible to achieve XOR = 2 in less than one removal, therefore the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,4], target = 1

**Output:** -1

**Explanation:**

It is impossible to remove elements to achieve `target`. Thus, the answer is -1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7], target = 7

**Output:** 0

**Explanation:**

The XOR of all elements is $\text{nums}[0] = 7$, which equals `target`. Thus, no removal is needed.

</div>
### Constraints

- $1 \le \text{nums.length} \le 40$

- $0 \le \text{nums}[i] \le 10^{4}$

- $0 \le target \le 10^{4}$