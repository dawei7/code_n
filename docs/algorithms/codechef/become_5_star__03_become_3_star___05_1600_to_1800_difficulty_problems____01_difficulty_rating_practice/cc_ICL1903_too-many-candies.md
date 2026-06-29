# Too Many Candies

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ICL1903 |
| Difficulty Rating | 1754 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [ICL1903](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/ICL1903) |

---

## Problem Statement

Luke, an intergalactic traveller went on a trip across the universe and got candies from the different planets he visited. He comes back with $N$ candies and decides to distribute them among his $M$ friends. However, Luke only wants a fair distribution of the candies as he loves everyone equally. (A fair distribution is one in which each of his friends receive an equal number of candies and each friend receives at least one candy.) If a fair distribution is not possible, he might throw away some candies and try to distribute the remaining candies in a similar manner.

If he can throw away exactly $K$ candies at a time (he can throw away candies multiple times), what is the minimum number of times he will need to throw away candies before achieving a fair distribution?

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers $N, M, K$.

###Output:
For each testcase, output a single integer denoting the minimum number of times he will need to throw away candies before achieving a fair distribution. If a fair distribution is not possible, print   -1.

###Constraints
- $1 \leq T \leq 10^5$
- $2 \leq N,M,K \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2     
28 6 2       
78 5 3
```

**Output**

```text
2
1
```

**Explanation**

Test case 1: There are 28 candies and 6 friends. He can distribute 24 candies fairly among his friends, each getting 4 candies. He then throws away the remaining 4 candies 2 at a time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
28 6 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
78 5 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**PROBLEM LINK:** [https://www.codechef.com/ICL2019/problems/ICL1903](https://www.codechef.com/ICL2019/problems/ICL1903)

**DIFFICULTY:** EASY

**PREREQUISITE:** Modular-Arithmetic

**PROBLEM**

There are N sweets that have to be distributed equally among M friends. You can remove K sweets from the N sweets and try to redistribute the sweets if needed. What is the minimum number of times you will have to remove K sweets such that the remaining sweets can be distributed equally among the M people?

**EXPLANATION**

We have N candies to distribute among M friends. Since we throw can throw K candies at a time, we can write -

 N = a*M + c*K  where a and c are positive integers

Let  GCD (M, K) = g .

If N mod g != 0, output -1 since no solutions for the given equation then.

Otherwise, divide the whole equation by g to remove any common factors.

Then say n=N/g, m=M/g, k=K/g

n = a*m + c*k (m and k are coprime)

Take modulo m both sides

n % m = (c*k) % m

Since m and k are coprime, inverse modulo of k exists. Therefore, multiply by k^{-1} both sides of the equation.

(n * k^{-1})%m = c % m

This means c = p*m + ((n * k^{-1})%m) where p is a positive integer

For minimum value of c, p=0.

c = (n * k^{-1}) % m

(Remember that since m is not necessarily prime, but m and k are coprime, we use the coprime algorithm for finding inverse modulo of k).

A simple check is needed at the end to make sure that N-c*K  is positive so that the remaining sweets are positive.

</details>
