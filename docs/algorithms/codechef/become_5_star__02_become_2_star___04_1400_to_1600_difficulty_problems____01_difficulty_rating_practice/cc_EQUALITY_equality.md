# Equality

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUALITY |
| Difficulty Rating | 1419 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [EQUALITY](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/EQUALITY) |

---

## Problem Statement

An *equation* is an equality containing one or more variables. Solving the equation consists of determining which values of the variables make the equality true. In this situation, variables are also known as unknowns and the values which satisfy the equality are known as solutions. An equation differs from an identity in that an equation is not necessarily true for all possible values of the variable.

There are many types of equations, and they are found in all areas of mathematics. For instance, a linear equation is an algebraic equation in which each term is either a constant or the product of a constant and (the first power of) a single variable.

In this problem we'll consider quite a special kind of systems of linear equations. To be more specific, you are given a system of **N** linear equations of the following form:

- **x2** + **x3** + ... + **xN - 1** + **xN** = **a1**

- **x1** + **x3** + ... + **xN - 1** + **xN** = **a2**

- ...

- **x1** + **x2** + ... + **xN - 2** + **xN** = **aN - 1**

- **x1** + **x2** + ... + **xN - 2** + **xN - 1** = **aN**

In other words, **i**'th equation of the system consists of the sum of all the variable **x1**, ..., **xN** except **xi** to the left of the equality sign and the constant **ai** to the right of the equality sign.

One can easily prove, that a system of linear equations as described above always have exactly one solution in case **N** is greater than one. Your task is to find the solution of the system(such a sequence **x1**, **x2**, ..., **xN**, that turns each of the equations into equality). It's guaranteed, that the solution of the system is a sequence consisting only of integers from the range [1, 108].

### Input

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of the test case description contains one integer **N** denoting the number of equations in the system.

The second line contains **N** integers **a1**, **a2**, ..., **aN** denoting the constants defining a system of linear equations, that you are asked to solve.

### Output

For each test case, output a single line containing **N** integers: a sequence **x1**, **x2**, ..., **xN**, which is the solution of the system.

### Constraints

- 1 ≤ **T** ≤ 25000

- 2 ≤ **N** ≤ 50000

- 1 ≤ **ai** ≤ 5 × 1012

- 1 ≤ **xi** ≤ 108

- The sum of all **N** in the input is not greater than 50000

---

## Examples

**Example 1**

**Input**

```text
2
3
9 6 5
4
13 11 10 8
```

**Output**

```text
1 4 5 
1 3 4 6
```

**Explanation**

In the first test case, we can simply replace the variables with the values from the correct output to make sure, that all the conditions are satisfied:

- **x2** + **x3** = 4 + 5 = 9 = **a1**

- **x1** + **x3** = 1 + 5 = 6 = **a2**

- **x1** + **x2** = 1 + 4 = 5 = **a3**

	In the second test case, we can repeat the same process to make sure, that all the conditions are satisfied:

- **x2** + **x3** + **x4** = 3 + 4 + 6 = 13 = **a1**

- **x1** + **x3** + **x4** = 1 + 4 + 6 = 11 = **a2**

- **x1** + **x2** + **x4** = 1 + 3 + 6 = 10 = **a3**

- **x1** + **x2** + **x3** = 1 + 3 + 4 = 8 = **a4**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
9 6 5
```

**Output for this case**

```text
1 4 5
```



#### Test case 2

**Input for this case**

```text
4
13 11 10 8
```

**Output for this case**

```text
1 3 4 6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/EQUALITY)

[Contest](http://www.codechef.com/COOK57/problems/EQUALITY)

**Author:** [Konstantsin Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

**Editorialist:** [Miguel Oliveira](http://www.codechef.com/users/mogers)

### DIFFICULTY:

Easy.

### PREREQUISITES:

Math, Linear Algebra.

### PROBLEM

We have a system of **N** equations on **N** variables. Equation *i* is of the form: x_1 + x_2 + ... + x_{i-1} + x_{i+1} + .. x_n = A_i. You can prove that solution of this system of equations will be unique. You have to solve this system of equations.

### QUICK EXPLANATION

- Write each equation in form of sum - x_i = A_i where sum denotes sum of all the variables i.e. sum = x_1 + x_2 + \dots + x_n. So, x_i = (sum - A_i)

- Now only thing that we have to do is to compute value of sum in terms of known values A_1, A_2, \dots A_n.

Let us add all the equations, we get N * sum - ( x_1 + x_2 + \dots + x_n) =  A_1 + A_2 + \dots + A_n.

As, sum =  x_1 + x_2 + \dots + x_n, we get sum = \frac{A_1 + A_2 + \dots + A_n}{N - 1}

- So finally, x_i = \frac{A_1 + A_2 + \dots + A_n}{N - 1} - A_i.

### EXPLANATION

The solution to a system of 2 variables is trivial:

\begin{cases} x_2 = A_1 \\ x_1 = A_2 \end{cases}

If we have 3 variables, the system is:

\begin{cases} x_2 + x_3 = A_1 \\ x_1 + x_3 = A_2 \\ x_1 + x_2 = A_3 \end{cases}

Each variable appears N-1 times. Let’s sum these equations. We get

\begin{array}{lcl} 2 * x_1 + 2 * x_2 +  2 * x_3 & = & A_1 + A_2 + A_3 \\
2 * (x_1 + x_2 + x_3) & = & A_1 + A_2 + A_3 \\
x_1 + x_2 + x_3 & = & \frac{A_1 + A_2 + A_3}{2} \end{array}

Now, to know the value of each variable, we can reuse the original equations. Then, to know the value of x1, we can use the fact that x_2 + x_3 = A_1. Let S = A_1 + A_2 + A_3, then x_1 + A_1 = \frac{S}{2} \Leftrightarrow x_1 = \frac{S}{2} - A_1.

In general, let S = A_1 + A_2 + ... + A_n. For each variable, x_i = \frac{S}{N-1} - A_i.

**Time Complexity**

We can compute the sum in linear time and calculate the answer in linear time as well for a O(N) solution.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/COOK57/Setter/EQUALITY.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/COOK57/Tester/EQUALITY.cpp)

</details>
