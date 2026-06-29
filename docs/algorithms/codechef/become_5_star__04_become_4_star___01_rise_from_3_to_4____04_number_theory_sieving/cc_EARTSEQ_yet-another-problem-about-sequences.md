# Yet Another Problem About Sequences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EARTSEQ |
| Difficulty Rating | 2011 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [EARTSEQ](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/EARTSEQ) |

---

## Problem Statement

For a set of positive integers $S$, let's define $\mathrm{gcd}(S)$ as the greatest integer which divides each element of $S$. If $\mathrm{gcd}(S) = 1$, the set $S$ is called *coprime*. For example, the set $\{7, 12, 15\}$ is coprime, but $\{6, 12, 15\}$ is not coprime, since every element of this set is divisible by $3$.

Your task is to find an integer sequence $A_0, A_1, \ldots, A_{N-1}$ such that:
- for each valid $i$, $1 \le A_i \le 10^9$
- $A_0, A_1, \ldots, A_{N-1}$ are pairwise distinct
- for each valid $i$, the set $\{A_i, A_{(i+1)\%N}\}$ is not coprime ($\%$ denotes the modulo operator)
- for each valid $i$, the set $\{A_i, A_{(i+1)\%N}, A_{(i+2)\%N}\}$ is coprime

It is possible that there is no solution. If there are multiple solutions, you may find any one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
For each test case:
- If there is no solution, print a single line containing the integer $-1$.
- Otherwise, print a single line containing $N$ space-separated integers $A_0, A_1, \ldots, A_{N-1}$.

### Constraints
- $1 \le T \le 1,000$
- $3 \le N \le 50,000$
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (19 points):** $3 \le N \le 3,333$

**Subtask #2 (81 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
3
4
```

**Output**

```text
6 10 15
374 595 1365 858
```

**Explanation**

**Example case 1:** Let's check the answer: $\mathrm{gcd}(6, 10) = 2$, $\mathrm{gcd}(10, 15) = 5$, $\mathrm{gcd}(15, 6) = 3$, $\mathrm{gcd}(6, 10, 15) = 1$. Every two cyclically consecutive numbers are not coprime, but every three cyclically consecutive numbers are coprime.

**Example case 2:**
- $\mathrm{gcd}(374, 595) = 17$, $\mathrm{gcd}(595, 1365) = 35$, $\mathrm{gcd}(1365, 868) = 39$, $\mathrm{gcd}(858, 374) = 22$
- $\mathrm{gcd}(374, 595, 1365) = 1$, $\mathrm{gcd}(595, 1365, 858) = 1$, $\mathrm{gcd}(1365, 858, 374) = 1$, $\mathrm{gcd}(858, 374, 595) = 1$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
6 10 15
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
374 595 1365 858
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/EARTSEQ)

[Contest: Division 1](https://www.codechef.com/JAN19A/problems/EARTSEQ)

[Contest: Division 2](https://www.codechef.com/JAN19B/problems/EARTSEQ)

**Setter:** [Evgeniy Artemov](https://www.codechef.com/users/eartemov)

**Tester:** [Xiuhan Wang](https://www.codechef.com/users/wxh010910)

**Editorialist:** [Taranpreet Singh](http://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Easy-Medium

### PREREQUISITES:

[Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), Number-Theory and Constructive Algorithms.

### PROBLEM:

Given an integer N \geq 3, find N distinct numbers such that every pair of consecutive numbers have a common factor  > 1 and all possible consecutive three elements have no common factor  > 1. Also, all numbers found should be between 1 and 10^9. First and Last elements are also considered adjacent here.

### SUPER QUICK EXPLANATION

- A simple way to generate N such distinct numbers is to take a prime and multiply two consecutive elements by this number. This way, the condition of co-primes is handled, but the numbers generated go beyond 10^9.

- A better way would be to reuse smaller primes while ensuring all the generated numbers are distinct.

### EXPLANATION

This is a constructive problem, and hence, have multiple solutions. Feel free to share your solution in comments.

**Note:** If we represent a number as the product of prime numbers, Prime factorization of a common factor of the pair of numbers is the common part of prime factorization. If we consider prime values or product of few primes, they have relatively lesser factors as compared to composite numbers. So, for most of the problems involving prime factors/factorization/divisibility, prime numbers bear special importance.

Let us try similar problems first.

Try solving the same problem assuming there’s no upper bound on maximum values. Now, we can just multiply a distinct prime number to every pair of consecutive numbers. This way, every two consecutive numbers are not co-prime while every three consecutive numbers are coprime.

The above solution is sufficient to solve the first subtask, but in the second subtask, the values exceed 10^9, so we need something better.

Try solving the same problem, assuming we are allowed repeated values. Here, we can choose prime numbers and multiplying each position by exactly two primes such that every two consecutive positions share prime factor while every three consecutive numbers do not share any prime factor, taking special care to choose a different prime number when reaching the end of the array.

Now, let us solve the **original problem**.

Think up and try to mix the above solutions so as to reduce the magnitude of generated numbers while keeping each number distinct.

The construction used in my solution is to reserve the first few primes and then multiply the first two positions by a non-reserved prime, next two positions by another prime and so on. Now, We can multiply Last and first position by a reserved prime, second and third position by different reserved prime, and so on. This way, we are guaranteed to have every pair of consecutive positions divisible by that particular prime number, and every three consecutive positions are coprime since no prime is multiplied to three consecutive positions.

**Implementation**

For this problem, we can preprocess and calculate a list of primes beforehand using the sieve of Eratosthenes and then for every test case, use primes from the list instead of recomputing.

**Interesting Fact**

This problem can also be approached as a challenge problem where we need to minimize the maximum value generated in sequence. Can you minimize? Say for N = 50000

### Time Complexity

Time complexity is O(MX*log(log(MX)) + \sum N) per test case where MX is the upper limit till primes are found. Finding primes up to 10^6 suffices for this problem.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](http://www.codechef.com/download/Solutions/JAN19/setter/EARTSEQ.cpp)

[Tester’s solution](http://www.codechef.com/download/Solutions/JAN19/tester/EARTSEQ.cpp)

[Editorialist’s solution](http://www.codechef.com/download/Solutions/JAN19/editorialist/EARTSEQ.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
