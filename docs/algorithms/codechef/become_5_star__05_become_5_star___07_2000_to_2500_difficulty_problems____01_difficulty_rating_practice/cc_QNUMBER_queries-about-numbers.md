# Queries About Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | QNUMBER |
| Difficulty Rating | 2026 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [QNUMBER](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/QNUMBER) |

---

## Problem Statement

Chef loves number theory very much. Now it is time to solve a new kind of problem.

There is given a natural number **N**. Chef has to answer **Q** queries of the form **T K**.

Here **T** is the type of query and **K** is the natural number.

If **T=**1, Chef must find the number of natural numbers which is divisor of both **N** and **K**.

If **T=**2, Chef must find the number of natural numbers which is divisor of **N** and is divisible by **K**.

If **T=**3, Chef must find the number of natural numbers which is divisor of **N** and is not divisible by **K**.

Chef can solve all these queries, but you will be hungry for night if this happens, because Chef will not have free time to cook a meal. Therefore you compromise with him and decided that everyone must do his/her own job. You must program and Chef must cook.

### Input

There will be 2 numbers in the first line: **N** and **Q**.

**Q** lines follow with 2 numbers each: **T** and **K**

### Output

For each of the **Q** lines you must output the result for corresponding query in separat line.

### Constraints
1<=**N**<=1012
1<=**Q**<=5*105
1<=**T**<=3

1<=**K**<=1012

---

## Examples

**Example 1**

**Input**

```text
12 6
1 6
1 14
2 4
2 3
3 12
3 14
```

**Output**

```text
4
2
2
3
5
6
```

**Explanation**

Numbers for each query:

{1,2,3,6}

{1,2}

{4,12}

{3,6,12}

{1,2,3,4,6}

{1,2,3,4,6,12}

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](http://www.codechef.com/problems/QNUMBER)

[Contest](http://www.codechef.com/SEP12/problems/QNUMBER)

# DIFFICULTY

EASY-MEDIUM

# PREREQUISITES

Elementary Number Theory, Integer Factorization

# PROBLEM

You are given a number N. Answer for 3 types of queries

- Given K, find the numbers that are divisors to both N and K

- Given K, find the numbers that are divisors to N and divisible by K

- Given K, find the numbers that are divisors of N and not divisible by K

# QUICK EXPLANATION

We can factorize N into primes and store it with us.

Now for each query, we simply iterate through prime factors of N and find the power of the prime factor that occurs in K to answer each type of query. We know that there are O(log N) factors of either N or K. Thus, our algorithm will run in O(Q*(log N + log K)) time, which is sufficiently fast within the time limits.

# EXPLANATION

We can factorize N by [trial division](http://en.wikipedia.org/wiki/Trial_division) in O(?N) time.

Let the factorization of N be P1R1P2R2…PmRm, for m prime factors. m can be at most O(log N).

For each of the queries, given K, we need to find the largest power of each prime in the set P = { P1, P2 …, Pm}, that occurs in K. This can be done by trial division of K by each of the primes. K will be divided at most O(log K) times.

We will obtain a set S = { S1, S2 …, Sm}, the highest power of each prime in the set P.

This will execute in at most O(log N) + O(log K) time.

### Type 1 query

The result is the number of divisors of the number whose prime factorization over the set P is

T = { min(S1, R1), min(S2, R2) …, min(Sm, Rm)}.

This is equal to

?i=1 to m(Ti + 1).

### Type 2 query

If, for any i = 1 to m: Si > Ri, the answer is 0.

Otherwise the answer can be calculated by finding the number of divisors of the number whose prime factorization over the set P is

T = { R1 - S1, R2 - S2 …, Rm - Sm}.

This is equal to

?i=1 to m(Ti + 1).

### Type 3 query

The answer for this query is equal to the number of divisors of N - (the answer for the equivalent Type 2 query).

Thus if the query is not of type 1, we always find the answer to type 2 query and find the appropriate answer based on whether the query was of Type 2 or Type 3.

See the setters / testers solutions for implementation details.

# SETTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Setter/QNUMBER.cpp)

# TESTERS SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/September/Tester/QNUMBER.c)

</details>
