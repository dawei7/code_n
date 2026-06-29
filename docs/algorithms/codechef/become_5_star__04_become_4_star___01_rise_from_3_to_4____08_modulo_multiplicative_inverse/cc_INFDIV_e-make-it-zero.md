# E - Make it Zero

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INFDIV |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Modulo Multiplicative Inverse |
| Official Link | [INFDIV](https://www.codechef.com/practice/course/3to4stars/LP3TO408/problems/INFDIV) |

---

## Problem Statement

You are given two integers, $n$ and $m$. You want to make $m$ equal to $0$. You decide to keep repeating the following operation until $m$ becomes $0$:

- Choose an integer $r$, uniformly at random from the range $[1, n]$. Set $m$ equal to the remainder obtained on dividing it by $r$. That is, replace $m$ with $m \% r$, where $\%$ denotes the modulo operator.

Find the expected number of operations after which $m$ becomes $0$. Let the answer be equal to $E = \dfrac{P}{Q}$ for some integers $P$ and $Q$ such that $\gcd(P, Q) = 1$. Output the value of $P Q^{-1}$ modulo $10^9 + 7$, where $Q^{-1}$ denotes the modular inverse of $Q$ modulo $10^9 + 7$.

---

## Input Format

The only line of the input contains two integers $n$ and $m$.

---

## Output Format

Output one line containing the value of $P Q^{-1}$ modulo $10^9 + 7$ as described above.

---

## Constraints

- $1 \leq n \leq 200000$
- $1 \leq m \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3 2
```

**Output**

```text
500000005
```

**Explanation**

$m$ is initially $2$. In each operation, we choose a random number $r$ from $\{1, 2, 3\}$. If $r = 1$, then $m \% r = 0$, and we stop. If $r = 2$, then $m \% r = 0$, and we stop. If $r = 3$, then $m \% r = 2$, and we continue the process.

Hence, we will repeat the procedure until we get a $1$ or $2$. You can check that the expected number of steps needed to get this is $\frac{3}{2}$. Hence, we output $3 \times 2^{-1} = 3 \times 500000004 = 500000005 \mod 10^9 + 7$.
