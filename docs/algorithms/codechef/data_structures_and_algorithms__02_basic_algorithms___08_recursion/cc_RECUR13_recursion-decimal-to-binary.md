# Recursion - Decimal to Binary 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR13 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR13](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR13) |

---

## Problem Statement

You are given an integer $N$ and you have to output it in Binary Format.

---

## Input Format

- You are given a single integer $N$.

---

## Output Format

Output a Binary string representing $N$.

---

## Constraints

- $1 \leq N \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
27
```

**Output**

```text
11011
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## [](#problem-explanation-1)Problem Explanation

You are given an integer N and you have to output that number as a Binary String.

## [](#approach-2)Approach

To convert a number from Decimal to Binary, we have to append the right most bit to the string and then right shift bits so we can access the next bit. We repeat this until there are no set bits in the number. We can extract the right-most bit using (N&1) or (N\%2). And we can right-shift N using the bitwise operator (N>>=1) or by dividing N by 2. To do this using recursion we assume that the function returns the Binary String of the number so we return the string after concatenating the Binary string returned by the function after passing the number right shifted by 1 and the right-most bit as a character. As for the base condition, when there are no set bits in the number, we return an empty string.

## [](#code-3)Code
``def Binary(n):
    if(n==0):
        return ''
    return Binary(n//2) + str(n&1)

n = int(input())
print(Binary(n))
``

</details>
