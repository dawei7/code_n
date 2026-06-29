# Chef and Polygon Cakes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PCJ18C |
| Difficulty Rating | 1773 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PCJ18C](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PCJ18C) |

---

## Problem Statement

Chef is making polygon cakes in his kitchen today!

Since the judge panel is very strict, Chef's cakes must be beautiful and have sharp and precise $internal$ angles in arithmetic progression.

Given the number of sides, $N$, of the cake Chef is baking today and also the measure of its first angle(smallest angle), $A$, find the measure of the $K^{th}$ angle.

###Input:
- The first line contains a single integer $T$, the number of test cases.
- The next $T$ lines contain three space separated integers $N$, $A$ and $K$, the number of sides of polygon, the first angle and the $K^{th}$ angle respectively.

###Output:
For each test case, print two space separated integers $X$ and $Y$, such that the $K^{th}$ angle can be written in the form of $X/Y$ and $gcd(X, Y) = 1$

###Constraints
- $1 \leq T \leq 50$
- $3 \leq N \leq 1000$
- $1 \leq A \leq 1000000000$
- $1 \leq K \leq N$
- It is guaranteed the answer is always valid.

---

## Examples

**Example 1**

**Input**

```text
1
3 30 2
```

**Output**

```text
60 1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/PCJ18C)

[Contest](https://www.codechef.com/PCJ2018/problems/PCJ18C)

**Author:** [Madhav Sainanee](http://www.codechef.com/users/madhav_1999)

**Tester:** [Prakhar Gupta](http://www.codechef.com/users/prakhar17252)

**Editorialist:** [Prakhar Gupta](http://www.codechef.com/users/prakhar17252)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

Arithmetic Progression, Sum of internal angles of a polygon, Arithmetic of fractions.

### PROBLEM:

Given an n sided polygon with the first angle a, find out the k^{th} angle if all the angles are in Arithmetic Progression with the first angle being the smallest.

### QUICK EXPLANATION

Find out the sum of AP from the sum of internal angles of the polygon. The common difference can be calculated from the sum of AP and can be used to find the k^{th} angle.

### EXPLANATION:

The sum of internal angles of an n sided polygon, S = 180 \times (n - 2).

This also forms the sum of the AP, i.e. S = \frac {n}{2} (2a + (n - 1) d).

From the above equation, we can find out d as a fraction.

The K^{th} angle can then be can be found out as A_k = a + (k - 1) d.

Since the numerator and denominator A_k may not be co-prime by now, divide both of them by their gcd.

**Complexity:** The time complexity is O(1 + log(n^2)) per test case, due to the gcd.

**Note:** We also allowed naive O(N) gcd algorithm.

### AUTHOR’S SOLUTION:

Author’s solution can be found [here](https://www.codechef.com/viewsolution/19718357).

</details>
