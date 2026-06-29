# Guessing Game

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GUESS |
| Difficulty Rating | 1410 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [GUESS](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/GUESS) |

---

## Problem Statement

Alice and Bob, both have to drink water. But they both don't want to go, so they will play a game to decide who will fetch water for both of them. Alice will choose a number randomly between **1** and **N** (both inclusive) and Bob will choose a number randomly between **1** and **M** (both inclusive). Both will write their numbers on a slip of paper. If sum of numbers choosen by both is **odd**, then Alice will go, else Bob will go.

What is probability that Alice will go?

### Input

First line contains, **T**, the number of testcases. Each testcase consists of **N** and **M** in one line, separated by a space.

### Output

For each test case, output a single line containing probability as an [irreducible fraction](http://en.wikipedia.org/wiki/Irreducible_fraction).

### Constraints

- **1** ≤ **T** ≤ **105**

- **1** ≤ **N,M** ≤ **109**

---

## Examples

**Example 1**

**Input**

```text
3
1 1
1 2
2 3
```

**Output**

```text
0/1
1/2
1/2
```

**Explanation**

#test1: The only way is when Alice and Bob both choose 1. So, Alice won't have to go because sum is even.

#test2: The different ways are (1,1) and (1,2), where first term denotes the number choosen by Alice. So of all possible cases (ie. 2) in only 1 case Alice has to go. Therefore, probability is 1/2.

#test3: The different ways are (1,1), (1,2), (1,3), (2,1), (2,2), (2,3) where first term denotes the number choosen by Alice. So of all possible cases (ie. 6) in only 3 cases Alice has to go. Therefore, probability is 1/2.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0/1
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
1/2
```



#### Test case 3

**Input for this case**

```text
2 3
```

**Output for this case**

```text
1/2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/GUESS)

[Contest](http://www.codechef.com/JUNE14/problems/GUESS)

**Author:** [Lalit Kundu](http://www.codechef.com/users/darkshadows/)

**Tester:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

Simple

### PREREQUISITES:

ad hoc, simple combinatorics.

### PROBLEM:

You are selecting two numbers x and y such that 1 <= x <= N and 1 <= y <= M. How many (x, y) pairs satisfy the condition that x + y is odd.

### QUICK EXPLANATION

-

Use the fact that Number of even numbers from 1 to N are floor(N / 2) and number of odd numbers from 1 to N are ceiling(N / 2).

-

Answer will be (floor(N / 2) * ceiling(N / 2)) / (N * M).

-

For representing the fraction in lowest terms, divide both the numerator and denominator by gcd of both.

### EXPLANATION

Notice the following simple facts.

-

Sum of an even and an odd number is odd.

ie

Even + Odd = Odd.

Odd + Even = Odd.

-

Number of even numbers from 1 to N are floor(N / 2).

Number of odd numbers from 1 to N are ceiling(N / 2).

Fact number 1 is very easy to prove.

Let us prove fact 2, first part.

**Claim** Number of even numbers from 1 to N are floor(N / 2).

**Proof:**

We will prove this fact by using induction over N.

*Base Case:*

For N = 1, floor(1 / 2) = 0. Hence LHS = 0

As number of even numbers are 0 too from 1 to 1. Hence RHS = 0

So LHS = RHS

*Induction Hypothesis:*

Let us assume that formula is true up to N such that N is **even**, then we need to prove the formula for N + 1.

Notice that N + 1 will be odd. Hence number of even numbers won’t increase and will remain equal to floor(N / 2).

As we know if N is even, then floor(N / 2) = floor((N + 1)/ 2). Hence we are done for this case.

Now Let us assume that formula is true up to N such that N is **odd**, then we need to prove the formula for N + 1.

Notice that N + 1 will be even. Hence number of even numbers increase by 1, hence they will be equal to floor(N / 2) + 1.

As we know if N is odd, then floor(N / 2) + 1 = floor((N + 1)/ 2). Hence we are done for this case too.

Note that instead of proving it formally, you can just see the above observation by observing the pattern for small numbers.

Proof of second part of fact 2 (Number of odd numbers from 1 to N are ceiling(N / 2).) will also go exactly along the same lines.

So finally our answer will be (floor(N / 2) * ceiling(N / 2)) / (N * M). We need to print this fraction in its irreducible form, so we have to divide both

the numerator and denominator by their gcd.

- Computing floor(N / 2) can be done by using simply integer division N / 2.

- Computing ceiling(N / 2) can be done by using simply integer divide (N + 1) / 2.

**Complexity**

O(log(N * M)), in the computation of gcd.

**Things to Take Care**

- Beware of the overflow of the product N * M, So use long long for storing product N * M.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Author’s solution](http://www.codechef.com/download/Solutions/2014/June/Setter/GUESS.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/2014/June/Tester/GUESS.cpp)

</details>
