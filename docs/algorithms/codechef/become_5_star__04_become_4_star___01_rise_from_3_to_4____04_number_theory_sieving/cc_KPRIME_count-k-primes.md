# Count K-Primes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KPRIME |
| Difficulty Rating | 1549 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [KPRIME](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/KPRIME) |

---

## Problem Statement

Alice and Bob are studying for their class test together. The topic of the test is **Prime Numbers**. The preparation is getting too boring for their liking. To make it interesting, they turn it into a game. The winner will get an ice-cream treat from the other.

The game is called **Count K-Primes**. A number is a $K$-prime if it has exactly $K$ **distinct** prime factors. The game is quite simple. Alice will give three numbers $A$, $B$ & $K$ to Bob. Bob needs to tell Alice the number of $K$-prime numbers between $A$ & $B$ (both inclusive). If Bob gives the correct answer, he gets a point. If not, Alice gets a point. They play this game $T$ times.

Bob hasn't prepared so well. But he really wants to win the game. He wants you to tell him the correct answer.

### Input

- First line of input contains a single integer $T$, the number of times they play.
- Each game is described in a single line containing the three numbers $A$,$B$ & $K$.

### Output

For each game, output on a separate line the number of $K$-primes between $A$ & $B$.

### Constraints:

- $1 \le T \le 10000$
- $2 \le A \le B \le 100000$
- $1 \le K \le 5$

---

## Examples

**Example 1**

**Input**

```text
4
2 5 1
4 10 2
14 15 2
2 20 3
```

**Output**

```text
4
2
2
0
```

**Explanation**

**Test case $1$:** The range includes $4$ integers $\{2, 3, 4,5 \}$. We need to find the number of integers in this range having only $1$ distinct prime factor.
- For $2$, since it is prime, it has $1$ distinct prime factor.
- For $3$, since it is prime, it has $1$ distinct prime factor.
- For $4$, we can write it as $2\times 2$. Thus, it has $1$ distinct prime factor which is $2$.
- For $5$, since it is prime, it has $1$ distinct prime factor.

Thus, all $4$ integers in the given range are $1$-primes.

**Test case $2$:** The only *K-primes* in the given range are $6$ and $10$. This is because $6 = 2\times 3$ and $10 = 2\times 5$. Thus both these integers have $2$ distinct prime factors.

**Test case $3$:** The only *K-primes* in the given range are $14$ and $15$. This is because $14 = 2\times 7$ and $15 = 3\times 5$. Thus both these integers have $2$ distinct prime factors.

**Test case $4$:** There are no *K-primes* in the given range.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
4 10 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
14 15 2
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
2 20 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](http://www.codechef.com/problems/KPRIME)

[Contest](http://www.codechef.com/JULY13/problems/KPRIME)

### DIFFICULTY

SIMPLE

### PREREQUISITES

[Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

### PROBLEM

A number is called a **K-prime** if it has **K** distinct prime factors.

Find the number of **K-prime** numbers between some given **A** and **B**, inclusive.

### QUICK EXPLANATION

Let us look at a simple implementation of the **Sieve of Eratosthenes**.

`
isPrime[N] = { YES }
for i = 2 to N
    if isPrime[i] = YES
        j = 2
        while i*j ? N
            isPrime[i*j] = NO
            j += i
`

**Sieve of Eratosthenes** has the wonderful property of **iterating through all the multiples of a prime number, for each unique prime number below N**. This means that the number of times the algorithm above marks a number **not prime** is equal to the number of unique prime factors of the number!

### EXPLANATION

Let us maintain the number of times the Sieve of Erotosthenes algorithm would mark an item as **not prime**. This maintained in the array **marked**.

`
marked[N] = { 0 }
isPrime[N] = { YES }
for i = 2 to N
    if isPrime[i] = YES
        marked[i] = 1 // each prime is its own single factor
        j = 2
        while i*j ? N
            isPrime[i*j] = NO
            marked[i*j]++
            j += i
`

Now, for any given range **[A,B]** and value **k**, we can iterate through **marked**. If the value in marked is equal to **k** then we know that the number has exactly **k** distinct prime factors.

The complexity of **Sieve of Eratosthenes** is equivalent to the number of times the innermost statement is executed. This is equal to the sum of the number of distinct prime factors for each number below **N**. We know that a number cannot have more than **log N** prime factors. In fact, the complexity of **Sieve of Eratosthenes** is equal to **O(N log log N)**.

There is one problem in our solution though. We are iterating between **A** and **B** for each input. It is given that there might be as many as **10000** inputs to be processed within a single second.

You will notice that the limit on possible values of **k** is very small. This can be exploited. Even if there were no limits on **k**, the maximum possible value in marked would be **7**.

You can build a table to store the number of times some **k** occurs in **marked** before each position **i**, for each **k**.

`
table[5][N] = { 0 }
for i = 2 to N
    for j = 1 to 5
        table[j][i] = table[j][i-1]
    v = marked[i]
    if 1 ? v ? 5
        table[v][i]++
`

Now the answer for some range **[A,B]** and value **k** can be found in constant time form **table**.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/July/Setter/KPRIME.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/July/Tester/KPRIME.cpp).

</details>
