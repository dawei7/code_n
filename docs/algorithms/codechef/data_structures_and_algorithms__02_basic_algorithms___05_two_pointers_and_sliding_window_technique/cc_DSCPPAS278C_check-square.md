# Check Square

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS278C |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Two-Pointer |
| Official Link | [DSCPPAS278C](https://www.codechef.com/practice/course/two-pointers/POINTERP/problems/DSCPPAS278C) |

---

## Problem Statement

Given a positive integer $c$, decide whether it can be represented as sum of two square numbers that is **c = a2 + b2** or not, where a and b are two non-negative integers and $a \leq b$.

---

## Input Format

First line contains positive integers $c$.

---

## Output Format

Print **true** if it can be represented, else print **false**.

---

## Constraints

- $1 \leq c \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
25
```

**Output**

```text
true
```

**Explanation**

25 can be represented in form of 32 + 42 = 9+16=25.

**Example 2**

**Input**

```text
15
```

**Output**

```text
false
```

**Explanation**

15 can not be represented as the sum of two square numbers.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#problem-statement-1)Problem Statement:

Given a positive integer `c`, determine whether it can be expressed as the sum of two square numbers. In other words, you need to determine if there exist two non-negative integers `a` and `b` such that:  c = a^2 + b^2

#### [](#approach-2)Approach:

This problem can be solved using a two-pointer technique. The idea is based on the observation that if `c = a^2 + b^2`, then `a` and `b` must satisfy the equation for some values between `0` and the square root of `c`.

### [](#detailed-approach-3)Detailed Approach:

-

**Two-Pointer Technique**:

- Initialize two pointers:

- `left` starts at `0` (corresponding to `a`).

- `right` starts at `sqrt(c)` (corresponding to `b`).

- The goal is to find if there exists a pair `(a, b)` such that `a^2 + b^2 = c`.

-

**Iterative Search**:

- Calculate the sum `sum = left^2 + right^2`.

- Compare `sum` with `c`:

- If `sum == c`, return `true` because we have found the values `a` and `b`.

- If `sum < c`, increment the `left` pointer to increase the sum.

- If `sum > c`, decrement the `right` pointer to decrease the sum.

- Continue this process until `left` exceeds `right`.

-

**Return Result**:

- If no such pair is found by the time `left` exceeds `right`, return `false`.

### [](#complexity-4)Complexity:

- **Time Complexity**: The time complexity of this solution is `O(sqrt(c))`. This is because the maximum number of iterations is determined by the value of `sqrt(c)`, as both pointers move towards each other.

- **Space Complexity**: The space complexity is `O(1)`, as the solution only uses a few extra variables for computation.

[](#note-5)Note:

There are other approaches too to solve this problem. Can you think think of any?

</details>
