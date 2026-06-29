# Three Friends

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | THREEFR |
| Difficulty Rating | 1074 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [THREEFR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/THREEFR) |

---

## Problem Statement

There are three friends; let's call them A, B, C. They made the following statements:
- A: "I have $x$ Rupees more than B."
- B: "I have $y$ rupees more than C."
- C: "I have $z$ rupees more than A."

You do not know the exact values of $x, y, z$. Instead, you are given their absolute values, i.e. $X = |x|$, $Y = |y|$ and $Z = |z|$. Note that $x$, $y$, $z$ may be negative; "having $-r$ rupees more" is the same as "having $r$ rupees less".

Find out if there is some way to assign amounts of money to A, B, C such that all of their statements are true.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X$, $Y$ and $Z$.

### Output
For each test case, print a single line containing the string `"yes"` if the presented scenario is possible or `"no"` otherwise (without quotes).

### Constraints
- $1 \le T \le 1,000$
- $1 \le X, Y, Z \le 1,000$

### Subtasks
**Subtask #1 (30 points):**
- $1 \le T \le 30$
- $1 \le X, Y, Z \le 3$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1 2 1
1 1 1
```

**Output**

```text
yes
no
```

**Explanation**

**Example 1**: One possible way to satisfy all conditions is: A has $10$ rupees, B has $9$ rupees and C has $11$ rupees. Therefore, we have $x = 1$, $y = -2$, $z = 1$.

**Example 2**: There is no way for all conditions to be satisfied.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 1
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/THREEFR)

[Contest: Division 1](https://www.codechef.com/LTIME65A/problems/THREEFR)

[Contest: Division 2](https://www.codechef.com/LTIME65B/problems/THREEFR)

**Setter:** [Praveen Dhinwa](https://www.codechef.com/users/dpraveen)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Basic Math and Linear Equations.

### PROBLEM:

There are three friends A, B and C. They make the following claim.

- A says that I have x Rupees more than B.

- B says that I have y Rupees more than C.

- C says that I have z Rupees more than A.

Given |x|, |y| and |z|, Find out if it’s possible to assign signs to x, y and z so that all three claims hold.

### SUPER QUICK EXPLANATION

- Answer is yes if and only if |x|+|y|+|z| = 2*max(|x|, |y|, |z|).

### EXPLANATION

Suppose Friend A has a Rupees, B has b Rupees and C has c rupees. Then, the three claims result in the following equations.

- a = b+x

- b = c+y

- c = a+z

Substituting value of a from 1 in 3, we get c = (b+x)+z.

Substituting value of b from 2 in this equation, we get c = (c+y)+x+z.

We have the final equation x+y+z = 0.

Two solutions exist.

One is to try every combination of signs for x, y and z and checking if it satisfies above relation at any time. It may take 8 (2^3) iterations in the worst case.

Other is to notice that the two values other than largest have to be assigned the same direction, while the largest value will be assigned opposite direction, to get sum 0.

See, if we assign a value other than largest value, same sign as largest, we can never get the sum 0 by assigning whichever sign to the third element. So, assign smaller two elements one direction, and largest value opposite direction and print Yes if the sum is 0. Otherwise, print No.

### Time Complexity

Time complexity is O(1) per test case.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/LTIME65/setter/THREEFR.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/LTIME65/tester/THREEFR.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/LTIME65/editorialist/THREEFR.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
