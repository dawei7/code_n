# Collatz Conjecture

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR29 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR29](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR29) |

---

## Problem Statement

You are required to write a recursive function to implement the Collatz conjecture (also known as the 3n + 1 problem). The Collatz conjecture is a mathematical sequence defined as follows:

- Start with any positive integer $n$.
- If $n$ is even, divide it by $2$.
- If $n$ is odd, multiply it by $3$ and add $1$.
- Repeat the process with the resulting number until $$ becomes $1$.
- The conjecture suggests that no matter what value of $n$ you start with, you will always eventually reach $1$.

Your task is to implement this process recursively and return the number of steps it takes for $n$ to become $1$.

---

## Input Format

- The only line of input contains a single non-negative integers $n$.

---

## Output Format

- Output the number of steps required for $n$ to reach $1$.

---

## Constraints

- $1 \leq n \leq 1000000000$

---

## Examples

**Example 1**

**Input**

```text
6
```

**Output**

```text
8
```

**Explanation**

- Start with 6
   - 6 is even, so divide by 2: 6 / 2 = 3
   - 3 is odd, so multiply by 3 and add 1: 3x3 + 1 = 10
   - 10 is even, so divide by 2: 10 / 2 = 5
   - 5 is odd, so multiply by 3 and add 1: 5x3 + 1 = 16
   - 16 is even, so divide by 2: 16 / 2 = 8
   - 8  is even, so divide by 2: 8 / 2 = 4
   - 4 is even, so divide by 2: 4 / 2 = 2
   - 2 is even, so divide by 2: 2 / 2 = 1
   - It took 8 steps to reach 1.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Collatz Conjecture in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR29)

### [](#problem-statement-1)Problem Statement:

You are required to write a recursive function to implement the Collatz conjecture (also known as the 3n + 1 problem). The Collatz conjecture is a mathematical sequence defined as follows:

Start with any positive integer n.

- If n is even, divide it by 2.

- If n is odd, multiply it by 3 and add 1.

Repeat the process with the resulting number until it becomes 1.

The conjecture suggests that no matter what value of n you start with, you will always eventually reach 1. Return the number of steps it takes for n to become 1.

### [](#approach-2)Approach:

- **Base Case:** If N=1, return 0, because no steps are required.

- **Recursive calls:** Depending on whether N is even or odd, apply the respective rule and recursively calculate the number of steps for the next number.

### [](#complexity-3)Complexity:

- **Time Complexity:** The time complexity is `O(log n)` on average, but in the worst case (when `n` is odd and requires more multiplications), it could be higher for certain numbers.

- **Space Complexity:** The space complexity is `O(log n)` due to the recursion stack depth.

</details>
