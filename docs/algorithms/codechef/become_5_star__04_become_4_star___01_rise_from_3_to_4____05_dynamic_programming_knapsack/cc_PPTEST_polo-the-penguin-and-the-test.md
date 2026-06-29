# Polo the Penguin and the Test

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PPTEST |
| Difficulty Rating | 1603 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming - Knapsack |
| Official Link | [PPTEST](https://www.codechef.com/practice/course/3to4stars/LP3TO405/problems/PPTEST) |

---

## Problem Statement

###  Read problems statements in Russian [here](https://www.codechef.com/download/translated/COOK39/russian/PPTEST.pdf)

Polo, the Penguin, has a lot of tests tomorrow at the university.

He knows that there are **N** different questions that will be on the tests. For each question **i** (**i = 1..N**), he knows **C[i]** - the number of tests that will contain this question, **P[i]** - the number of points that he will get for correctly answering this question on each of tests and **T[i]** - the amount of time (in minutes) that he needs to spend to learn this question.

Unfortunately, the amount of free time that Polo has is limited to **W** minutes. Help him to find the maximal possible total number of points he can get for all tests if he studies for no more than **W** minutes.

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. The first line of each test case contains the pair of integers **N** and **W**, separated by a space. The following **N** lines contain three space-separated integers **C[i]**, **P[i]** and **T[i]** (**i = 1..N**).

### Output

For each test case, output a single line containing the answer to the corresponding test case.

### Constraints

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **100**

- **1** ≤ **C[i], P[i], T[i]** ≤ **100**

- **1** ≤ **W** ≤ **100**

---

## Examples

**Example 1**

**Input**

```text
1
3 7
1 2 3
2 3 5
3 3 3
```

**Output**

```text
11
```

**Explanation**

**Example case 1.** The best choice is to learn the first and the third questions and get **1*2 + 3*3 = 11** points.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINKS:

[Practice](http://www.codechef.com/problems/PPTEST)

[Contest](http://www.codechef.com/COOK39/problems/PPTEST)

**Author:** [Vitaliy Herasymiv](http://en.wikipedia.org/wiki/Dynamic_programming)

**Tester:** [Tasnim Imran Sunny](http://www.codechef.com/download/Solutions/COOK39/Setter/PPTEST.cpp)

**Editorialist:** [Tuan Anh](http://www.codechef.com/download/Solutions/COOK39/Tester/PPTEST.cpp)

## DIFFICULTY:

Easy

## PREREQUISITES:

[Dynamic Programming](http://en.wikipedia.org/wiki/Dynamic_programming)

## PROBLEM:

There are **N** questions. The **ith** question needs **T[i]** minutes to learn and will give you **C[i] × P[i]** points in the tests. You have **W** minutes to learn the questions. Your job is to find which questions to learn to maximise your score.

## EXPLANATION:

We need to choose a sub-set of **N** questions so that the total learning time does not exceed **W** and the total socore is

as large as possible. With the constraint **N ? 100 ** we cannot try out all possible sub-sets since the number of

sub-sets can be **2 100** which is extremely large.

We need to use dynamic programming in this problem. Let **F[i][j]** be the maximal score you can get if you spend no more than **j**

minutes to learn some questions amongst the first **i** questions. Now, there are two cases:

-
If you choose to learn the **ith** question then you get maximally **F[i - 1][j - T[i]] + C[i] × P[i]**
points. Be careful with the case where **j < T[i]**.

-
If you do not learn the **ith** question then you get maximally **F[i-1][j]** points.

The complexity of this solution is **O(N×W)**. For the initialization you need to set **F[0][j] = 0** for all
**0 ?   j ?   W**.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK39/Setter/PPTEST.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK39/Tester/PPTEST.cpp).

In the solution of problem setter and the tester an optimization is used to reduce the memory complexity.

With a little modification of the algorithm above we can solve this problem using a one-dimensional array of **W** elements.

The pseudo code is given below:

`
	FOR i -> 0 to W
		G[i] = 0
	ENDFOR

	(*)FOR i -> 1 to N
		FOR j -> W downto 0
			G[j] = max(G[j + T[i]], G[j] + C[i] × P[i])
	ENDFOR
`

After the **ith**iteration of the for loop (*), the value in G array is exactly as in the **ith**

row of the F array in the original algorithm. Notice that in the second For loop we need to consider the value of j in the decreasing order

so that each time we use **G[j]** to update **G[j + T[i]]** we know that the value in **G[j]** is the optimized value of using **j** minutes and the first **(i - 1)** questions only.

</details>
