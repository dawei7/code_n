# Interesting Representation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INTREP |
| Difficulty Rating | 2251 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [INTREP](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/INTREP) |

---

## Problem Statement

Given a positive integer $N$, find two positive integers $A$ and $B$, such that $A - B = N$ and the number of **distinct** prime factors of $A$ and $B$ are equal. If there exist multiple pairs of values of $A$ and $B$ satisfying the given conditions, you can output any one of them.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, integer $N$.

---

## Output Format

For each testcase, output in a single line two space separated integers $A$ and $B$.
If there are multiple answers, you can output any one of them.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^{16}$
- $1 \leq A, B \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
3
1
8
135
```

**Output**

```text
3 2
97 89
1071 936
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
3 2
```



#### Test case 2

**Input for this case**

```text
8
```

**Output for this case**

```text
97 89
```



#### Test case 3

**Input for this case**

```text
135
```

**Output for this case**

```text
1071 936
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/LTIME100C/problems/INTREP)

[Contest - Division 2](https://www.codechef.com/LTIME100B/problems/INTREP)

[Contest - Division 1](https://www.codechef.com/LTIME100A/problems/INTREP)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#problem-3)PROBLEM:

Given a positive integer N, find positive integers A and B such that A-B=N and the number of distinct prime factors of A and of B are equal.

#
[](#explanation-4)EXPLANATION:

**Notation:** Let d(x) represent the number of distinct prime factors of x.

The trivial case of N\equiv0\pmod 2 is solved by A=2*N and B=N.

How?

Since N is even, it’s prime factorization includes the number 2. Thus, 2*N has the same number of distinct prime factors as N.

Therefore, d(A)=d(B), and A-B=N.

The solution for when N is not divisible by 2 is not so straightforward. But a little bit of experimenting (and extrapolating the trivial case above) gives the following idea.

**Claim:** There exists values k_1,k_2 such that A=Nk_1 and B=Nk_2 is a valid answer.

Intuition for the next step

This may sound absurd, but let’s assume the above claim is true and try to find some special properties of k_1 and k_2.

N = A-B = N(k_1-k_2) implies k_1=k_2+1.

Our Spidey intuitive sense guides us to experiment with k_1 as a prime number. Trial and error for several small N shows that the smallest odd prime k_1 not a factor of N always works.

This little conclusion gives rise to the ingenious solution presented below.

Let x be the smallest **odd** prime that doesn’t divide N. Then k_1=x and k_2=x-1 are valid values for A=Nk_1 and B=Nk_2 respectively.

Proof

A-B=Nk_1-Nk_2=N(k_1-k_2)=N completes the first part of the proof.

All we need to show now is d(Nk_1)=d(Nk_2).

Since k_1 is an odd prime that is not a factor of N, we have d(Nk_1)=1+d(N).

Now, k_2=k_1-1 is even (has 2 as a prime factor), and its prime factors are <x. Since by the definition of x, all **odd** primes <x are factors of N, it follows that the only prime factor of k_2 not a factor of N, is 2.

Thus, d(Nk_2)=1+d(N)=d(Nk_1) and we are done.

All that remains is to find the smallest odd prime x that doesn’t divide N. This can be done by hard coding an array of the first 20 primes (why are 20 sufficient?) and iterating over it to find the required value.

Then, A=Nx and B=N(x-1) is a valid solution.

#
[](#time-complexity-5)TIME COMPLEXITY:

Iterating over the constant size list of primes to determine the answer makes the time complexity

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51617755).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
