# Chef And The Hiring Event

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEARMY |
| Difficulty Rating | 1613 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHEARMY](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHEARMY) |

---

## Problem Statement

The Head Chef is receiving a lot of orders for cooking the best of the problems lately. For this, he organized an hiring event to hire some talented Chefs. He gave the following problem to test the skills of the participating Chefs. Can you solve this problem and be eligible for getting hired by Head Chef.

A non-negative number **n** is said to be *magical* if it satisfies the following property. Let **S** denote the multi-set of numbers corresponding to the non-empty subsequences of the digits of the number **n** in decimal representation. Please note that the numbers in the set **S** can have **leading zeros**. Let us take an element **s** of the multi-set **S**, **prod(s)** denotes the product of all the digits of number **s** in decimal representation.
The number **n** will be called magical if sum of **prod(s)** for all elements **s** in **S**, is even.

For example, consider a number 246, its all possible non-empty subsequence will be **S = {2, 4, 6, 24, 46, 26, 246}**. Products of digits of these subsequences will be **{prod(2) = 2, prod(4) = 4, prod(6) = 6, prod(24) = 8, prod(46) = 24, prod(26) = 12, prod(246) = 48**, i.e. **{2, 4, 6, 8, 24, 12, 48}**. Sum of all of these is 104, which is even. Hence 246 is a *magical* number.

Please note that multi-set **S** can contain repeated elements, e.g. if number is 55, then **S = {5, 5, 55}**. Products of digits of these subsequences will be **{prod(5) = 5, prod(5) = 5, prod(55) = 25}**, i.e. **{5, 5, 25}**. Sum of all of these is 35 which is odd. Hence 55 is not a
 *magical* number.

Consider a number 204, then **S = {2, 0, 4, 20, 04, 24, 204}**. Products of digits of these subsequences will be **{2, 0, 4, 0, 0, 8, 0}**. Sum of all these elements will be 14 which is even. So 204 is a *magical* number.

The task was to simply find the **Kth** *magical* number.

### Input

- First line of the input contains an integer **T** denoting the number of test cases.

- Each of the next **T** lines contains a single integer **K**.

### Output

For each test case, print a single integer corresponding to the **Kth** magical number.

### Constraints

- **1** ≤ **T** ≤ **105**

- **1** ≤ **K** ≤ **1012**.

### Subtasks

**Subtask #1 : (20 points)**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **K** ≤ **104**.

**Subtask 2 : (80 points) **
Original Constraints

---

## Examples

**Example 1**

**Input**

```text
2
2
5
```

**Output**

```text
2
8
```

**Explanation**

**Example case 1.**
2 is the 2nd magical number, since it satisfies the property of the magical number. The first magical number will be of course 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Contest](http://www.codechef.com/JUNE16/problems/CHEARMY)

[Practice](http://www.codechef.com/problems/CHEARMY)

**Author:** [Prateek Gupta](http://www.codechef.com/users/dpraveen)

**Testers:** [Istvan Nagy](http://www.codechef.com/users/iscsi)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Easy

### PREREQUISITES:

finding pattern, base 5 representation, simple maths

### PROBLEM:

A number n is called a *magical* number if the sum of product of individual digits (in base 10 representation) of each subsequence of digits is even. You have to find K-th *magical* number.

### QUICK EXPLANATION:

A number n will be *magical* number, iff all of its digits are even.  Represent K in base 5, and the corresponding number with each digit 0 \leq i < 5 being mapped to 2 * i will be the K-th *magical* number.

### EXPLANATION:

**Properties of a *magical* number**

**Lemma:** A number will be *magical* number, if all of its digits in decimal representation are even.

**Proof**: You can observe this property by finding a pattern by writing a bruteforce solution for small numbers. A more formal proof follows.

Note that the order of digits of n does not matter. Product of digits of  subsequence containing only even digits will be even. Similarly, a subsequence containing any even digit will be even. Now, all the subsequences that remain are the ones which consist of all odd digits. Sum of each such subsequence will be odd. Number of such subsequences will be 2^o - 1 where o denotes number of odd digits in n. Note that 2^o - 1 will be odd if o is non-zero. Hence if a number contains even a single odd digit, sum of product of digits of subsequences will be odd.

**Finding K-th number**

Note that you can view magical numbers in decimal representation as numbers written in base 5 representation, where a digit i in base 5 has the value of 2 * i (which will be an even number) in decimal, e.g. 2480 (decimal) can be thought 1240 (in base 5).

Finding K-th number in base 5, is same as representing K - 1 in base 5. You can find the corresponding magical number in decimal representation by replacing each digit i by 2 * i.

**Example**

Assume we have to find K = 10-th magical number.

Write K - 1 in base 5, K - 1 = 9 = (14)_5.

Now replace digit i, with 2 * i, i.e. (28)_{10}.

Therefor, 10-th magical number will be 28.

### Time Complexity:

\mathcal{O}(log_5^{K}) - Represent K in base 5.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter](http://www.codechef.com/download/Solutions/JUNE16/Setter/CHEARMY.cpp)

[Tester](http://www.codechef.com/download/Solutions/JUNE16/Tester/CHEARMY.cpp)

</details>
