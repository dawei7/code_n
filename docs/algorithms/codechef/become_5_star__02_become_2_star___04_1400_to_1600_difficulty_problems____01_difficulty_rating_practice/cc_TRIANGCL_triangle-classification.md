# Triangle Classification

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIANGCL |
| Difficulty Rating | 1462 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [TRIANGCL](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/TRIANGCL) |

---

## Problem Statement

Triangle classification is an important problem in modern mathematics. Mathematicians have developed many criteria according to which a triangle can be classified. In this problem, you will be asked to classify some triangles according to their sides and angles.

According to their measure, angles may be:

- **Acute** — an angle that is less than 90 degrees

- **Right** — a 90-degrees angle

- **Obtuse** — an angle that is greater than 90 degrees

According to their sides, triangles may be:

- **Scalene** — all sides are different

- **Isosceles** — exactly two sides are equal

According to their angles, triangles may be:

- **Acute** — all angles are acute

- **Right** — one angle is right

- **Obtuse** — one angle is obtuse

**Triangles with three equal sides (equilateral triangles) will not appear in the test data.**

The triangles formed by three collinear points are not considered in this problem. In order to classify a triangle, you should use only the adjactives from the statement. There is no triangle which could be described in two different ways according to the classification characteristics considered above.

### Input

The first line of input contains an integer **SUBTASK_ID** denoting the subtask id this input belongs to.

The second line of input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The only line of each test case contains six integers **x1**, **y1**, **x2**, **y2**, **x3** and **y3** denoting Cartesian coordinates of points, that form the triangle to be classified.

It is guaranteed that the points are non-collinear.

### Output

For each test case, output a single line containing the classification of the given triangle.

If **SUBTASK_ID** equals 1, then the classification should follow the "<*Side classification starting with a capital letter*> triangle" format.

If **SUBTASK_ID** equals 2, then the classification should follow the "<*Side classification starting with a capital letter*> <*angle classification*> triangle" format.

Please, check out the samples section to better understand the format of the output.

### Constraints

- 1 ≤ **T** ≤ 60

- **|xi|**, **|yi|** ≤ 100

- Subtask 1 (50 points): *no additional constraints*

- Subtask 2 (50 points): *no additional constraints*

### Note

The first test of the first subtask and the first test of the second subtask are the example tests (each in the corresponding subtask). It's made for you to make sure that your solution produces the same verdict both on your machine and our server.

### Tip

Consider using the following condition in order to check whether two floats or doubles **A** and **B** are equal instead of traditional **A == B**: **|A - B| < 10-6**.

---

## Examples

**Example 1**

**Input**

```text
1
2
0 0 1 1 1 2
3 0 0 4 4 7
```

**Output**

```text
Scalene triangle
Isosceles triangle
```

**Example 2**

**Input**

```text
2
6
0 0 4 1 1 3
0 0 1 0 1 2
0 0 1 1 1 2
0 0 2 1 1 2
3 0 0 4 4 7
0 0 2 1 4 0
```

**Output**

```text
Scalene acute triangle
Scalene right triangle
Scalene obtuse triangle
Isosceles acute triangle
Isosceles right triangle
Isosceles obtuse triangle
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/TRIANGCL)

[Contest](http://www.codechef.com/LTIME32/problems/TRIANGCL)

**Author:** [Kanstantsin Sokal](http://www.codechef.com/users/kostya_by)

**Tester:** [Pavel Sheftelevich](http://www.codechef.com/users/pavel1996)

**Editorialist:** [Pawel Kacprzak](http://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

Basic geometry

### PROBLEM:

For a given triangle, you have to classify it according to its sides and angles.

### QUICK EXPLANATION:

Use [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance) to classify triangles according to their sides. You can use [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) in order to classify them according to their angles.

### EXPLANATION:

In this problem, your task is to classify a triangle given as 3 point with **integer coordinates**. It’s important to notice that there are no degenerated triangles in the input - this ones with all 3 collinear points.

Since all coordinates are integers, we are going to give a solution, which uses only operations over integers in order to avoid any floating point equality checking. This is a common trick, and it’s worth to consider using it while solving this kind of problems.

### SUBTASK 1

In the first subtask, you have to classify a triangle based on the lengths of the its sides, and there are two options here: either a triangle has **exactly 2 sides of equal lengths** or **all its sides have different lengths**. A triangle with all sides of equal lengths is guaranteed to not appear in the test cases, so we don’t consider such a triangles here.

The task is supposed to be pretty straightforward. Let d^2(A, B)  be the squared distance between points A and B. In other words, this is the squared length of a side of the triangle between points A and B.

Notice that d^2(A, B) can be easily computed (A.x - B.x)^2 + (A.y - B.y)^2, because its just a squared [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance).

In order to classify a triangle according to its sides, the only thing we need to do is to compare squared lengths of all its 3 sides. Either none of them are equal or exactly 2 of them are equal, which gives us the answer. Notice that we are using the fact that for two positive integers C and D, C and D are equal if and only if C^2 and D^2 are equal. This let us to avoid floating point operations here.

### SUBTASK 2

In the second subtask, besides doing the side classification as in the first subtask, you have to classify triangles according to their angles. More specifically, there are 3 options here. A given triangle may have either one right angle or one obtuse angle or all acute angles.

This seems to be slightly harder than the first subtask. You may think of using some sort of trigonometry functions here, but in fact, there is a quite clever and smooth solution based on [Pythagorean theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem).

Let a^2, b^2, c^2 be the squared lengths of sides of a triangle in non-descending order. Then the triangle has exactly **one right angle** if and only if a^2 + b^2 = c^2. Moreover, it has exactly **one obtuse** angle if and only if a^2 + b^2 < c^2. Otherwise, all its angles are **acute**. Since we know how to compute squared lengths of all the sides, we can easily classify a triangle according to its angles using this method. Notice that all these computations are again done only over integers.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME32/Setter/TRIANGCL.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME32/Tester/TRIANGCL.cpp).

</details>
