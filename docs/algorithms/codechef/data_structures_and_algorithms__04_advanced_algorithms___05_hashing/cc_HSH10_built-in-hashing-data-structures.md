# Built-In Hashing Data Structures

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH10 |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH10](https://www.codechef.com/learn/course/hashing/HASH02/problems/HSH10) |

---

## Problem Statement

Most programming languages offer built-in data structures that implement hashing. For example, C++ has `std::unordered_map`, Java provides `HashSet` and `HashMap`, and Python has dictionaries.

These built-in hash maps also come with mechanisms to handle collisions efficiently.

### Task
Execute the code given in the IDE to explore how these built-in hashing data structures function.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- The first line of each test case contains a single integer $N$, denoting the length of array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

For each test case, output on a new line the maximum value of $A_1+A_N$ you can get after several right rotations.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
6
213512345
1234123
1000000000
987987435
134604389
23
```

**Output**

```text
0 1 2 3 4 5
```
