# Number of Factors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUMFACT |
| Difficulty Rating | 1710 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [NUMFACT](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/NUMFACT) |

---

## Problem Statement

Alice has learnt factorization recently. Bob doesn't think she has learnt it properly and hence he has decided to quiz her. Bob gives Alice a very large number and asks her to find out the number of factors of that number. To make it a little easier for her, he represents the number as a product of **N** numbers. Alice is frightened of big numbers and hence is asking you for help. Your task is simple. Given **N** numbers, you need to tell the number of distinct factors of the product of these **N** numbers.

### Input:
First line of input contains a single integer **T**, the number of test cases.

Each test starts with a line containing a single integer **N**.
 The next line consists of **N** space separated integers (**Ai**).

### Output:
For each test case, output on a separate line the total number of factors of the product of given numbers.

### Constraints:
`
1 ≤ **T** ≤ 100
1 ≤ **N** ≤ 10
2 ≤ **Ai** ≤ 1000000

`

### Scoring:
You will be awarded **40** points for correctly solving for **Ai** ≤ 100.

You will be awarded another **30** points for correctly solving for **Ai** ≤ 10000.

The remaining **30** points will be awarded for correctly solving for **Ai** ≤ 1000000.

---

## Examples

**Example 1**

**Input**

```text
3
3
3 5 7
3
2 4 6
2
5 5
```

**Output**

```text
8
10
3
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 5 7
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3
2 4 6
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
2
5 5
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Author: **Vamsi Kavala**

Tester: **Roman Rubanenko**

Editorialist: **Bruno Oliveira**

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/NUMFACT)

[Contest](http://www.codechef.com/LTIME01/problems/NUMFACT)

# DIFFICULTY

Cakewalk

# PRE-REQUISITES

Simple Math, Integer Factorization

## Problem:

You are given a very large number represented as a product of **N** numbers.

Given this number representation, you need to find the number of distinct factors of the original number which is formed by the product of given N numbers.

## Quick Explanation:

We can factorize each one of the N given numbers into its prime factors. Then we find the number of occurrences of each prime factor, say they are a1, a2,…aK, if we have K distinct prime factors. Our answer is simply: (a1+1)*(a2+1)*(…)*(aK+1).

## Detailed Explanation:

This problem relies on some knowledge of divisor function. Divisor functions returns the number of positive and distinct divisors of a number. Let’s call it d(x).

-

Some properties of the divisor function:

We now look into some important properties of the divisor function:

For a prime number p, we have d§ = 2, as there are only two numbers which divide a prime 	number:1 and itself.

Now, it’s a known fact that this function is multiplicative but not completely multiplicative. This means that if two numbers, say, a and b are there such that gcd(a, b) = 1, then the following holds:

`` `d(a*b) = d(a)*d(b).`

This allows us to deduce the important relationship, that is the key of solving this problem:

For a prime number, p, we have: d(p^n) = n+1.

Now, it’s easy to understand that all we need to do is to factorize all the **N** given numbers into its prime factors, and, for each prime factor we also need to count how many times it appears (that is, we need to know the exponent of each prime factor).

Once we have this count with us (which can be done using integer factorization and for example, the **set** and **map** data structures, one to guarantee uniqueness of the factors and the other to save the number of occurences for each unique prime factor), all we need to do is to multiply all these numbers plus one together and we will obtain our answer.

As an example, consider the number:

504 = 2^**3** * 3^**2** * 7^**1**

The number of distinct divisors of 504 is then (3+1) * (2+1) * (1+1) = 24.

Applying this process to all numbers yields the answer to the problem

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/LTIME01/Setter/NUMFACT.cpp).

### TESTER’S SOLUTION

Tester’s solution will be uploaded soon.

### ***Useful Links***

[What is a multiplicative function?](http://en.wikipedia.org/wiki/Multiplicative_function)

[More information on the divisor function](http://en.wikipedia.org/wiki/Divisor_function)

</details>
