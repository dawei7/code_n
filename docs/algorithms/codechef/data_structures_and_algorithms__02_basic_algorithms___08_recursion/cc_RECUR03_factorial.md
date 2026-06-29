# Factorial

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR03 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR03](https://www.codechef.com/learn/course/recursion/LRECUR01/problems/RECUR03) |

---

## Problem Statement

### Task
Given an integer $N$, calculate and output the factorial of a $N$.

**Factorial** of an integer $N$ is the product of first $N$ natural numbers.

Recursive equation for Factorial:
$Factorial(n) = N * Factorial(n-1)$, $Factorial(0) = 1$, $Factorial(1) = 1$

---

## Input Format

- Input contains a single integer $N$

---

## Output Format

Output the Factorial of $N$

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
5
```

**Output**

```text
120
```

**Explanation**

$1 \times 2 \times 3 \times 4 \times 5 = 120$

**Example 2**

**Input**

```text
0
```

**Output**

```text
1
```

**Explanation**

Factorial of $0$ is $1$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem link - [Factorial](https://www.codechef.com/learn/course/recursion/LRECUR01/problems/RECUR03)

### [](#problem-statement-1)Problem Statement:

Given an integer N, calculate and output the factorial of a N. Factorial of an integer N is the product of first N natural numbers.

Recursive equation for Factorial:

`Factorial(n) = N∗Factorial( n − 1 ), Factorial(0)=1, Factorial(1)=1`

### [](#approach-2)Approach:

The key idea of this solution is to use **recursion** to calculate the factorial of the number **N**. Recursion is a technique where a function calls itself to solve smaller subproblems until a base condition is met.

Here’s how the logic works:

- **Base Case**:

- If **N** is 0 or 1, the function directly returns 1 because by definition, **0! = 1** and **1! = 1**.

- **Recursive Case**:

- For any number greater than 1, the function multiplies **N** by the factorial of **N - 1**.

- This recursive call continues reducing the value of **N** until the base case is met, at which point the recursion stops, and the results are multiplied together to give the final result.

### [](#time-complexity-3)Time Complexity:

- **O(N)** because the function makes **N** recursive calls to calculate the factorial.

### [](#space-complexity-4)Space Complexity:

- **O(N)** due to the recursive call stack, where each recursive call takes space.

</details>
