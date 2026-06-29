# Odd Divisors

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ODDDIV |
| Difficulty Rating | 1657 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [ODDDIV](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/ODDDIV) |

---

## Problem Statement

Little Egor likes to play with positive integers and their divisors. Bigger the number to play with, more the fun! The boy asked you to come up with an algorithm, that could play the following game:

Let's define **f(n)** as the sum of all odd divisors of **n**. I.e. **f(10) = 1 + 5 = 6** and **f(21) = 1 + 3 + 7 + 21 = 32**. The game is to calculate **f(l) + f(l + 1) + ... + f(r - 1) + f(r)** for the given integers **l** and **r**.

Have fun! But be careful, the integers might be quite big.

### Input

The first line of the input contains one integer **T** denoting the number of test cases.

The only line of the test case description contains two positive integers **l** and **r**.

### Output

For each test case, output the required sum on a separate line.

### Constraints

- **1 ≤ T ≤ 10**

- **1 ≤ l ≤ r ≤ 105**

---

## Examples

**Example 1**

**Input**

```text
2
1 10
42 42
```

**Output**

```text
45
32
```

**Explanation**

In the first example case, **f(1) + f(2) + ... + f(10) = 1 + 1 + 4 + 1 + 6 + 4 + 8 + 1 + 13 + 6 = 45**

In the second example case, **f(42) = 32**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
45
```



#### Test case 2

**Input for this case**

```text
42 42
```

**Output for this case**

```text
32
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/ODDDIV)

[Contest](http://www.codechef.com/COOK69/problems/ODDDIV)

**Author:** [Constantine Sokol](http://www.codechef.com/users/kostya_by)

**Tester:** [Pavel Sheftelevich](http://www.codechef.com/users/pavel1996)

**Editorialist:** [Praveen Dhinwa](http://www.codechef.com/users/dpraveen)

### DIFFICULTY:

simple

### PREREQUISITES:

finding sum of divisors of a number

### PROBLEM:

Let’s define f_n as the sum of all odd divisors of n. You are given at max 10 queries of following types to answer

- Given two (l, r), output value of f_l + f_{l + 1} + \dots+  f_{r - 1} + f_r. Range of l, r will be [1, 10^5].

### QUICK EXPLANATION:

- Precompute f_n for all n from 1 to 10^5 using sieve in \mathcal{O}(n \, log n) time. Now, for answering each query, you can answer in \mathcal{O}(r - l  + 1).

- Let n = 2^r * s such that s is odd. Let prime representation of s be p_1^{q_1} * p_2^{q_2} * \dots * p_r^{q_r}. Then value of f_n will be

\frac{(p_1^{q_1 + 1} - 1)}{p_1 - 1} \cdot \frac{(p_2^{q_2 + 1} - 1)}{p_2 - 1} \cdot \dots \cdot \frac{(p_r^{q_r + 1} - 1)}{p_r - 1}

### EXPLANATION:

Let M = 10^5.

### Sieve based solution

The problem is very similar to finding sum of all the divisors of a number, only change is that we should only consider odd divisors.

We will use a sieve to precompute sum of all divisors for number \leq M. So, we iterate over each odd i from 1 to M, then we iterate over each multiple d of i, s.t. d \leq M and add i to f_d as i is an odd divisor of d. See the following pseudo code for details.

``
for (int i = 1; i <= M; i += 2) {
    for (int d = i; d <= M; d += i) {
        f[d] += i
    }
}

``

Now, you might be thinking that its time complexity is \mathcal{O}(M^2). Not it’s not, in fact it is only \mathcal{O}(M \,  log M).

**Proof**

For each i, we iterate over all its multiples d such that d \leq M. Number of such d's can be at max \frac{M}{i}.

So, our time complexity will be

\begin{aligned}
\textbf{Time Complexity} & = \frac{M}{1} + \frac{M}{2} + \dots + \frac{M}{M} \\
&= M * (1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{M}) \\
& \leq M * (1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{M} + \dots + \text{ infinite terms}) \\
& \leq M * log M \\
& \text{ as } (1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{M} + ..) \text{ is harmonic series whose sum is bounded by log(number of terms)}.
\end{aligned}

### Prime representation of number based solution

Let us first remove all the factors of 2 from n, i.e. n = 2^r * s such that s is odd.

Now, say prime representation of s be p_1^{q_1} * p_2^{q_2} * \dots * p_r^{q_r}, then value of f_n will be

\frac{(p_1^{q_1 + 1} - 1)}{p_1 - 1} \cdot \frac{(p_2^{q_2 + 1} - 1)}{p_2 - 1} \cdot \dots \cdot \frac{(p_r^{q_r + 1} - 1)}{p_r - 1}

**Proof**

Consider the following product

\begin{equation}

(1 + p_1 + p_1^2 + \dots + p_1^{q_1}) \cdot (1 + p_2 + p_2^2 + \dots + p_2^{q_2}) \cdot \dots * (1 + p_r + p_r^2 + \dots + p_r^{q_r})

\end{equation}

Notice that upon expending this product, its each term will be a product of some powers of p_1, p_2, \dots p_r, i.e. each term will be a divisor of s.

Also, notice that each of the term in the expression will be unique, i.e. each divisor is added only once. Hence this expression represents sum of all divisors of s.

As we know the formula for sum of a geometric progression

\begin{aligned}
1 + p_1 + p_1^2 + .. p_1^{q_1} & = \frac{(p_1^{q_1 + 1} - 1)}{p_1 - 1} \\
i.e., \sum_{i = 1}^{q_1} {p_1}^i & =  \frac{(p_1^{q_1 + 1} - 1)}{p_1 - 1} \\
\end{aligned}

Thus follows the proof.

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK69/Setter/ODDDIV.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/COOK69/Tester/ODDDIV.cpp).

</details>
