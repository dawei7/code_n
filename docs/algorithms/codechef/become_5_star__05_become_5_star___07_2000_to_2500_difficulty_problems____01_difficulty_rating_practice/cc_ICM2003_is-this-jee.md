# Is This JEE

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ICM2003 |
| Difficulty Rating | 2206 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ICM2003](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ICM2003) |

---

## Problem Statement

Everyone loves short problem statements.

Given a function $ f(x) $ find its minimum value over the range $ 0 \lt x \lt π/2$

$
f(x) = ( x^2 + b*x + c ) / sin( x )
$

### Input:

- First-line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two real numbers $b, c$.

### Output:
For each test case, output the minimum value of $ f(x) $ over the given range. Absolute error of $10^{-6}$ is allowed.

### Constraints
- $1 \leq T \leq 100000$
- $1 \leq b,c \leq 20$

---

## Examples

**Example 1**

**Input**

```text
1
2 2
```

**Output**

```text
5.8831725615
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Is This JEE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ICM2003)

### [](#problem-statement-1)Problem Statement

Everyone loves short problem statements.

Given a function  f(x)  find its minimum value over the range  0 \lt x \lt π/2

f(x) = ( x^2 + b*x + c ) / sin( x )

### [](#approach-2)Approach:

**approach**

To solve the problem, the logic is to find the value of x in the interval (0,π/2) where the function f(x) = \frac{x^2 + b \cdot x + c}{\sin(x)}~ is minimized. The function involves a trigonometric term (sin(x)) and a quadratic term in the numerator. Since the function is continuous and differentiable in this range, we can use binary search to find the value of x that minimizes the function. The binary search will help us narrow down the minimum point by comparing the function’s value at different points in the range. For binary search, we start with an initial range of x values between 0 and π/2. We calculate the value of the function at the midpoint of the range and adjust the range based on whether the value at the midpoint is greater than or less than the desired function behavior. Once we find the minimum point, we compute the function’s value at this point and return it.

### [](#time-complexity-3)Time complexity

The time complexity is O(\log N) where N is the precision to which we want to find the minimum.

### [](#space-complexity-4)Space complexity

The space complexity is O(1) since we only use a few variables for storing intermediate results.

</details>
