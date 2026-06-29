# Eugene and function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KFUNC |
| Difficulty Rating | 1746 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [KFUNC](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/KFUNC) |

---

## Problem Statement

Eugene loves sequences, especially [arithmetic progressions](https://en.wikipedia.org/wiki/Arithmetic_progression). One day he was asked to solve a difficult problem.

If a sequence of numbers **A1**, **A2**, ... , **AN** form an arithmetic progression **A**, he was asked to calculate sum of **F(Ai)**, for **L** ≤ **i** ≤ **R**.

**F(X)** is defined as:

If **X** < 10 then **F(X)** = **X**.

Else **F(X)** = **F(**sum_of_digits**(X))**.

Example:

**F(**1378**)** =
**F(**1+3+7+8**)** =
**F(**19**)** =
**F(**1 + 9**)** =
**F(**10**)** =
**F(**1+0**)** =
**F(**1**)** = 1

### Input

- The first line of the input contains an integer **T** denoting the number of test cases.

- Each test case is described in one line containing four integers: **A1** denoting the first element of the arithmetic progression **A**, **D** denoting the common difference between successive members of **A**, and **L** and **R** as described in the problem statement.

### Output

- For each test case, output a single line containing one integer denoting sum of **F(Ai)**.

### Constraints

- **1** ≤ **T** ≤ **105**

- **1** ≤ **A1** ≤ **109**

- **0** ≤ **D** ≤ **10**9

- **1** ≤ **R** ≤ **1018**

- **1** ≤ **L** ≤ **R**

### Subtasks

- **Subtask 1:**  0 ≤ **D** ≤ 100, 1 ≤ **A1** ≤ 109, 1 ≤ **R** ≤ 100  - **15 points**

- **Subtask 2:**  0 ≤ **D** ≤ 109, 1 ≤ **A1** ≤ 109, 1 ≤ **R** ≤ 106  - **25 points**

- **Subtask 3:** Original constraints -** 60 points**

---

## Examples

**Example 1**

**Input**

```text
2
1 1 1 3
14 7 2 4
```

**Output**

```text
6
12
```

**Explanation**

**Example case 1.**

**A** = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...}

**A1** = 1

**A2** = 2

**A3** = 3

**F(A1)** = 1

**F(A2)** = 2

**F(A3)** = 3

**1+2+3=6**

**Example case 2.**

**A** = {14, 21, 28, 35, 42, 49, 56, 63, 70, 77,  ...}

**A2** = 21

**A3** = 28

**A4** = 35

**F(A2)** = 3

**F(A3)** = 1

**F(A4)** = 8

**3+1+8=12**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 3
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
14 7 2 4
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/KFUNC)

[Contest](http://www.codechef.com/NOV15/problems/KFUNC)

**Author:** [Eugene Kazmin](http://www.codechef.com/users/aangairbender)

**Tester:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Xellos](http://www.codechef.com/users/xellos0)

### DIFFICULTY:

CAKEWALK

### PREREQUISITES:

none

### PROBLEM:

You’re given a function F(n) and many queries of the form: find \sum_{k=L}^{R} F(A_1+kD). Answer the queries.

### QUICK EXPLANATION:

Notice that F(n)=n%9. That means you only need the sum of any 9 consecutive terms and at most 9 other terms of the given arithmetic sequence to compute the answer.

### EXPLANATION:

We can split the sum for a range [L,R] into sums for 2 ranges [L,M] and [M+1,R] for any M between L and R.

In order to solve this problem, we need one simple observation: F(x+9)=F(x). Yes, the function F is periodic with period 9, even though it’s defined in a complicated way! It’s actually quite easy to notice if you implement F(x) as described in the statement and print its values for some small ranges of consecutive numbers. When you have trouble solving a problem and 10 days to spend, it’s not a bad idea to play with it, print some values and try to see some useful property in them.

Note that the sum of digits of a number n can be computed in O(\log{n}) time and is usually much smaller than n, so there won’t be many iterations n \rightarrow digit\_sum(n) and even this implementation by definition is really fast. Still, since F(x)=x for x < 10 and F(x) is periodic, we can find a formula for it: F(x)=(x-1)\% 9 +1. This allows us to compute F(x) in O(1) time.

How to use periodicity in our problem, then? The key is that if we have 9 terms in our arithmetic sequence (R-L+1=9), then the answer is always the same for the same A_1,D (since the sum of a range [L+1,L+9] differs from the sum of the range [L,L+8] by F(A_1+D(L+9))-F(A_1+DL)=F(A_1+DL+9D)-F(A_1+DL)=0) and can be computed easily. Let’s denote this answer for a given A_1,D by ans_0. If R-L+1 is divisible by 9, then the answer is ans_0\frac{R+1-L}{9} - we split the range [L,R] into \frac{R+1-L}{9} ranges of 9 consecutive elements and the answer for each of them is the same. If R-L+1 < 9, we can simply bruteforce the answer. And if it’s not divisible by 9, but large enough, then we can split the range [L,R] into ranges [L,R-m] and [R-m+1,R] for m=(R+1-L)\% 9; the first range has the number of elements divisible by 9, so we know how to calculate the answer for it, and the second one has just m elements, so the answer for it can be bruteforced as well.

This means we can compute the answer in O(1) time and memory.

How large can the answers get? If D=0, A_1=9, L=1, R=10^{18}, then it’s 9\cdot 10^{18}, which fits into 64-bit signed integer types; since F(n) \le 9, that’s also the maximum. However, any relevant A_k can easily exceed this type’s range if D and L are large. Therefore, we have to carefully use modulos - or just stick to Python with its arbitrarily large integers (of course, with this size of data, we need fast I/O).

One more thing: we haven’t proved why F(x)=(x-1)\% 9+1. Let’s use mathematical induction. Let’s suppose that it holds for x < a; at the beginning, we know that it’s true for a=10. Now we want to prove it for x=a. It’s well-known that the sum of digits of a gives the same remainder mod 9 as a, since 10^j\% 9=1 \% 9 for any j and so

a \% 9 = \sum \left(d_j 10^j \% 9\right) =\left( \sum (d_j\% 9)\cdot(10^j \% 9)\right)\% 9 = \left(\sum d_j\right) \% 9

(d_j are the digits of a). If a \ge 10, we know that its sum of digits s is < a, so F(s)=(s-1)\% 9+1 and F(a)=F(s)=(s-1)\% 9 +1= (a-1)\% 9+1. Now we know that F(x)=(x-1)\% 9+1 holds for x \le a, so by induction, it holds for any x.

### AUTHOR’S AND TESTER’S SOLUTIONS:

The author’s solution can be found [here](https://www.codechef.com/download/Solutions/NOV15/Setter/KFUNC.cpp).

The tester’s solution can be found [here](https://www.codechef.com/download/Solutions/NOV15/Tester/KFUNC.cpp).

The editorialist’s solution can be found [here](https://www.codechef.com/download/Solutions/NOV15/Editorialist/KFUNC.py).

### RELATED PROBLEMS:

</details>
