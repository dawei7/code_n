# Levy Conjecture

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEVY |
| Difficulty Rating | 1510 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [LEVY](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/LEVY) |

---

## Problem Statement

### Problem Statement

**Levy's conjecture**, named after **Hyman Levy**, states that all odd integers greater than **5** can be represented as the sum of an odd prime number and an even semiprime. To put it algebraically, **2n + 1 = p + 2q** always has a solution in primes **p** and **q** (not necessary to be distinct) for **n > 2**. *(Source: [Wikipedia](http://en.wikipedia.org/wiki/Lemoine's_conjecture))*

In this problem, given a positive integer **N** (not necessary to be odd integer greater than **5**). Your task is to calculate how many distinct ordered pairs **(p, q)** such that **N = p + 2q**, where **p** and **q** are primes.

### Input

The first line of input contains an integer **T**, denoting the number of test cases. Then **T** test cases follow.

Each test case consists of exactly one line containing an integer **N**.

### Constraints

- **1** ≤ **T** ≤ **100000 (105)**

- **1** ≤ **N** ≤ **10000 (104)**

### Output

For each test case, output the number of ordered pairs **(p, q)** of primes such that **N = p + 2q**.

---

## Examples

**Example 1**

**Input**

```text
3
2
7
11
```

**Output**

```text
0
1
2
```

**Explanation**

**Case #1:** There are no ordered pairs **(p, q)** such that **p + 2q = 2**.

**Case #2:** There is only one ordered pair **(p, q) = (3, 2)** such that **p + 2q = 7**.

**Case #3:** There are two ordered pairs **(p, q) = (7, 2), (5, 3)** such that **p + 2q = 11**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
7
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
11
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/LEVY)

[Contest](http://www.codechef.com/APRIL13/problems/LEVY)

**Author:** [Kaushik Iska](http://www.codechef.com/users/kaushik_iska)

**Tester:** [Hiroto Sekido](http://www.codechef.com/users/laycurse)

**Editorialist:** [Anton Lunyov](http://www.codechef.com/users/anton_lunyov)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

[Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes)

### PROBLEM:

For the given positive integer **n ? N := 10000** you need to find the number of pairs **(p, q)** such that **p + 2 * q = n** and **p**, **q** are both primes. You should be able to answer up to **100000** test cases in a second.

### QUICK EXPLANATION:

The following solution works fine even when **N = 400000**. At first let’s find all prime numbers up to **N** using sieve of Eratosthenes. Then we fill array `cnt[]` of size **N** such that `cnt[n]` denotes the number of required pairs of primes for **n**. Initially it is filled by zeros. Then we iterate over pairs of primes **(p, q)** in a simple double loop over array of found primes and increase `cnt[p + 2 * q]` by 1 for each such pair. Moreover, if **p + 2 * q > N** we break from the inner cycle over **q**. Clearly after this double loop array `cnt[]` will be filled correctly. So after such precomputation we can answer each query in **O(1)** time. The complexity of such approach is **O(N * log log N + (N / log N)2 + T)**. Here **N * log log N** is the complexity of sieve and **N / log N** is a approximate number of primes up to **N**.

Some contestants were curious about the case of even **n**. Let **n = 2 * k**. Then from **p + 2 * q = n** we have **p = 2 * (k ? q)**. So **p** is even prime and hence equal to **2**. Then **q = k ? 1**. So for even **n** answer is **1** if **n/2 ? 1** is prime and **0** otherwise.

### EXPLANATION:

Here we discuss implementation details of the above solution.

To find all primes the following pseudo-code could be used:

``for p = 1 to N do
   isPrime[p] = true
for p = 2 to N do
   if isPrime[p] then
      add p to the list of primes
      for n = p * p to N with step p do
         isPrime[n] = false
``

Let `primes` denotes the list of found primes.

To fill the array `cnt[]` the following pseudo-code could be used

``for n = 1 to N do
   cnt[n] = 0
for p in primes do
   for q in primes do
      if (p + 2 * q > N) then break
      increase cnt[p + 2 * q] by 1
``

### ALTERNATIVE SOLUTION:

The low limit on **N** allows to use the following dirty trick. Let’s find array `cnt[]` using any algorithm that possibly could get TLE and print it to some file as a comma separated list of integers. Then copy this list to the program as an initialization of the actual array `cnt[]`. Now the program is ready to answer each query in **O(1)** time. Note also that source limit for this problem is **50000** bytes. So your program should not exceed **50000** characters. But since **N** is only **10000**, hack with initialization of `cnt[]` would cost only about **26Kb** of code which is far from the limit.

The most easiest and straightforward way to perform this hack is the following:

``for n = 1 to N do
   cnt = 0
   for q = 1 to n/2 do
      p = n - 2 * q
      if (isPrime(p) and isPrime(q)) then
         cnt = cnt + 1
   print cnt, ","
``

where `isPrime(n)` returns whether **n** is prime and could implemented as follows:

``isPrime(n)
   if n < 2 return false
   for d = 2 to sqrt(n) do
      if (n mod d = 0) return false
   return true
``

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be provided soon.

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/2013/April/Tester/LEVY.cpp).

### RELATED PROBLEMS:

[UVA - 543 - Goldbach’s Conjecture](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=7&page=show_problem&problem=484)

</details>
