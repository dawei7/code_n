# Print Pattern

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR07 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR07](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR07) |

---

## Problem Statement

You are given an integer $N$, you have to print an upside down triangle with stars of base $N$.

For example: for $N = 5$:
```
*****
****
***
**
*
```

---

## Input Format

- You are given a single integer in input $N$.

---

## Output Format

You have to output a the pattern specified above based on the integer $N$.

---

## Constraints

$ 1 \leq N \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
```

**Output**

```text
****
***
**
*
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Print Pattern in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR02/problems/RECUR07)

### [](#problem-statement-1)Problem Statement:

Given an integer N, we need to print an upside-down triangle of stars where the base of the triangle has N stars and each subsequent row contains one less star than the row above it.

### [](#approach-2)Approach:

- **Loop through Rows**:

- Use a loop that starts from N and decrements down to 1.

- For each iteration, print the corresponding number of stars.

- **Print Stars**:

- In each iteration, print a row of stars based on the current row number.

### [](#complexity-3)Complexity:

- **Time Complexity:** O(N^2) . The total number of stars printed is N*(N+1)/2​, which results in O(N^2) total time due to the nested printing in each recursive call.

- **Space Complexity**: O(N) due to the recursion stack. Each recursive call adds a new frame to the stack until the base case is reached.

</details>
