# Little Elephant and Bamboo

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEBAMBOO |
| Difficulty Rating | 1761 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [LEBAMBOO](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/LEBAMBOO) |

---

## Problem Statement

### Problem Statement

Little Elephant from Zoo of Lviv likes bamboo very much. He currently has **n** stems of bamboo, **Hi** - height of **i-th** stem of bamboo (0-based numeration).

Today inspector Andrii from World Bamboo Association is visiting the plantation. He doesn't like current situation. He wants the height of **i-th** stem to be **Di**, for each **i** from **0** to **n-1**, inclusive.

Little Elephant is going to buy some special substance. One bottle of such substance he can use to single stem of bamboo. After using substance for stem **i**, the height of **i-th** stem is decrased by **1** and the height of **j-th** stem is increased by **1** for each **j** not equal to **i**. Note that it is possible for some of the stems to have negative height, but after all transformations all stems should have positive height.

Substance is very expensive. Help Little Elephant and find the minimal number of bottles of substance required for changing current plantation to one that inspector wants. If it's impossible, print **-1**.

### Input

First line contain single integer **T** - the number of test cases. **T** test cases follow. First line of each test case contains single integer **n** - the number of stems in the plantation. Second line contains **n** integers separated by single space - starting plantation. Next line of each test case contains **n** integers - plantation that inspector Andrii requires.

### Output

In **T** lines print **T** integers - the answers for the corresponding test cases.

### Constraints

1 <= **T** <= 50

1 <= **n** <= 50

1 <= **Hi, Di** <= 50

---

## Examples

**Example 1**

**Input**

```text
3
1
1
2
2
1 2
2 1
3
3 2 2
4 5 3
```

**Output**

```text
-1
1
5
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
1
2
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
2
1 2
2 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
3 2 2
4 5 3
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LEBAMBOO)

[Contest](http://www.codechef.com/OCT13/problems/LEBAMBOO)

**Author:** [Vitaliy](http://www.codechef.com/users/witua)

**Tester:** [Jingbo Shang](http://www.codechef.com/users/jingbo_adm)

**Editorialist:** [Ajay K. Verma](http://www.codechef.com/users/djdolls)

### DIFFICULTY:

EASY

### PREREQUISITES:

High school maths

### PROBLEM:

Given a set of N linear equations (of a very specific form) on N variables, find if it has a solution where all variables take non-negative integer values, and if so, find such a solution where sum of variables is minimum.

### QUICK EXPLANATION:

Since the equations are of a very specific form, they can be solved in linear time (discussed in more detail in the next section). One only needs to check if the solution consists of non-negative integer values. Also special care should be taken for the case N = 2, as in that case the set of equations is redundant.

### EXPLANATION:

We are given two arrays H and D of the same size N, where H[i] represents the current height of i-th stem and D[i] represents the target height of i-th stem. A single operation on the i-th stem reduces its height by one unit and increases the height of all other stems by one unit. The goal is to find the minimum number of operations using which we can achieve the target height of all stems, if possible.

Let us represent the number of operations performed on i-th stem by variable xi.

Clearly, xi must be a non-negative integer for all i.

Using these variables we can write the height of i-th stem at the end of all operations as follows:

H[i] - xi + (x1 + x2 + … + xi - 1 + xi + 1 + … + xN)

Let us represent (x1 + x2 + … + xN) by a new variable s. Using this new variable we can rewrite the above expression as

H[i] + s - 2xi

Since the target height of the i-th stem is D[i], this gives us the following equation:

D[i] = H[i] + s - 2xi

Adding all these N equations (corresponding to each i) we get the following equation:

D[1] + D[2] + … + D[N] = H[1] + H[2] + … + H[N] + s * N - 2 (x1 + x2 + … + xN)

i.e., D[1] + D[2] + … + D[N] = H[1] + H[2] + … + H[N] + s * (N - 2)

Let us define two new constants

d = D[1] + D[2] + … + D[N]

h = H[1] + H[2] + … + H[N]

Using these constants the above equation can be written as

d = h + s * (N - 2)

This equation may provide us the value of s, if N != 2. We will handle the case of N = 2 later, for the time being let us assume N != 2.

s = (d - h) / (N - 2)

If s is not an integer, or s < 0, then we can immediately deduce that no valid solution (non-negative integer valued) of the above system of equations exists. On the other hand, if s is a non-negative integer, then we can compute each of the xi and check if it is a non-negative integer.

D[i] = H[i] + s - 2xi.

Hence, xi = 0.5 * (s + H[i] - D[i])

If all xi’s are valid, then the number of operations is x1 + x2 + … + xN = s, which we have already calculated. Note that in this case, we do not have to minimize anything as there is a unique solution.

### Case where N = 2

In case of N = 2, we have only two equations:

D[1] = H[1] - x1 + x2

D[2] = H[2] - x2 + x1

Note that, the two equations are redundant, and hence they will either have no solution or an infinite number of solutions.

x1 - x2 = H[1] - D[1]

x1 - x2 = D[2] - H[2]

The LHS of both equations are the same, if the RHS are not the same, then we have no solution of this system of equations. On the other hand if the RHS are the same (say with value r), then we have infinitely many solutions, given by the following parametric representation:

x2 = t

x1 = t + r

where t is a free variable and can take any value.

Both x1 and x2 are non-negative. Hence t >= max(0, -r). Also we want to minimize (x1 + x2) = 2t + r, hence t must be as small as possible.

This means that in order to minimize the number of operations we should choose

t = max(0, -r)

The number of operations in this case is 2t + r = 2 * max(0, -r) + r = **abs**®.

### Time Complexity:

O (N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be put up soon.

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/October/Tester/LEBAMBOO.cpp).

</details>
