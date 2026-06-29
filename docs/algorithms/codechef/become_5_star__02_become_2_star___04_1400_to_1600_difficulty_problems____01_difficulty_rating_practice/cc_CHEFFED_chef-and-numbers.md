# Chef and Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFFED |
| Difficulty Rating | 1477 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHEFFED](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHEFFED) |

---

## Problem Statement

Chef likes problems related to numbers a lot. He is generally quite good at solving these kinds of problems, but today he got stuck at one number theory problem, and so he asks your help to solve it.

Given a positive integer **N**, find out how many positive integers **X** satisfy the equation **X** + S(**X**) + S(S(**X**)) = **N**, where S(**X**) denoting sum of digits of **X** in decimal (base 10) representation.

### Input

The only line of the input contains one integer number - **N**.

### Output

Output single integer in a line denoting the count of number of positive integers **X** satisfying the above given equation.

### Constraints

- **1** ≤ **N** ≤ **109**

---

## Examples

**Example 1**

**Input**

```text
6
```

**Output**

```text
1
```

**Explanation**

**Example 1**. Only one positive integer **X = 2** satisfies the equation **X + S(X) + S(S(X)) = 6**, as **X + S(X) + S(S(X)) = 2 + 2 + 2 = 6**.

**Example 2**

**Input**

```text
9939
```

**Output**

```text
4
```

**Explanation**

**Example 2**.**X** can be 9898, 9907, 9910 and 9913.

9898 + S(9898) + S(S(9898)) = 9898 + 34 + 7 = 9939

9907 + S(9907) + S(S(9907)) = 9907 + 25 + 7 = 9939

9910 + S(9910) + S(S(9910)) = 9910 + 19 + 10 = 9939

9913 + S(9913) + S(S(9913)) = 9913 + 22 + 4 = 9939

You can verify that there is not other positive value of **X** satisfying the given equation.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/CHEFFED)

[Contest](http://www.codechef.com/COOK72/problems/CHEFFED)

**Author:** [Misha Chorniy](https://www.codechef.com/users/mgch)

**Tester:** [Karan Aggarwal](https://www.codechef.com/users/karanaggarwal)

**Editorialist:** [Pushkar Mishra](https://www.codechef.com/users/pushkarmishra)

### DIFFICULTY:

Easy

### PREREQUISITES:

None

### PROBLEM:

Given a number N, find the number of integers X such that X + S(X) + S(S(X)) = N. Here, S(k) denotes sum of digits of integer K.

### EXPLANATION:

The first thing to note is that no number strictly greater than N can satisfy the equation. So we only care about numbers less than or equal to N.

The next thing to note is that we are given the constraint that N \leq 10^9. This means S(X) can at maximum be 81 for any X \leq N. This is because the largest number below 10^9 is 999999999 whose digits add up to 81. The digits of 10^9 add up to 1 anyway. So, S(X) \leq 81, and we have that S(S(X)) \leq 16 (maximum case is for 79). Summing the two inequalities, we have that S(X) + S(S(X)) \leq 97.

This gives us an efficient algorithm to calculate the number of integers that satisfy the equation. Since, S(X) + S(S(X)) \leq 97, we just need to iterate from X = N-97 to N and check which integers satisfy the equation because no integer smaller than N-97 can satisfy the equation and neither can any integer greater than N.

Please see editorialist’s/setter’s program for implementation details.

### COMPLEXITY:

\mathcal{O}(97)

### SAMPLE SOLUTIONS:

[Author](http://www.codechef.com/download/Solutions/COOK72/Setter/CHEFFED.cpp)

[Tester](http://www.codechef.com/download/Solutions/COOK72/Tester/CHEFFED.cpp)

[Editorialist](http://www.codechef.com/download/Solutions/COOK72/Editorialist/CHEFFED.cpp)

[Admin](http://www.codechef.com/download/Solutions/COOK72/Admin/CHEFFED.cpp)

</details>
