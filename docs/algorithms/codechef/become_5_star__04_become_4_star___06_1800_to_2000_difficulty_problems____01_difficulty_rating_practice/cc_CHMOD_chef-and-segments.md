# Chef and Segments

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHMOD |
| Difficulty Rating | 1939 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [CHMOD](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/CHMOD) |

---

## Problem Statement

Chef likes toys. His favourite toy is an array of length **N**. This array contains only integers. He plays with this array every day. His favourite game with this array is **Segment Multiplication**. In this game, the second player tells the **left** and **right** side of a segment and some **modulo**. The first player should find **the multiplication of all the integers in this segment of the array modulo the given modulus**. Chef is playing this game. Of course, he is the first player and wants to win all the games. To win any game he should write the correct answer for each segment. Although Chef is very clever, he has no time to play games. Hence he asks you to help him. Write the program that solves this problem.

### Input

The first line of the input contains an integer **N** denoting the number of elements in the given array. Next line contains **N** integers **Ai** separated with spaces. The third line contains the number of games **T**. Each of the next T lines contain 3 integers **Li, Ri and Mi**, the left side of the segment, the right side of segment and the modulo.

### Output

For each game, output a single line containing the answer for the respective segment.

### Constrdaints

- **1 ≤ N ≤ 100,000**

- **1 ≤ Ai ≤ 100**

- **1 ≤ T ≤ 100,000**

- **1 ≤ Li ≤ Ri ≤ N**

- **1 ≤ Mi ≤ 109**

---

## Examples

**Example 1**

**Input**

```text
5
1 2 3 4 5
4
1 2 3
2 3 4
1 1 1
1 5 1000000000
```

**Output**

```text
2
2
0
120
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/CHMOD)

[Contest](http://www.codechef.com/AUG13/problems/CHMOD)

### DIFFICULTY

EASY

### PREREQUISITES

Simple Math, Repeated Squaring

### PROBLEM

You are given a list of N integers.

Each value in the list is between 1 and 100.

You have to respond to T queries of the following type

- Given L and R

- Find the product of all integers in the given list between L and R, inclusive

- Find the above product modulo some M, which is also given

### EXPLANATION

For each query, iterating through the list between **L and R** to maintain the **modular products** is too slow.

Of course, we use the fact that each value is between **1 and 100** to our advantage.

- There are **25 prime numbers between 1 and 100**

Each number has a unique prime factorization. The product of a set of numbers can also be simulated by adding up the frequencies of each prime in all numbers in the set.

For example, suppose we have to multiply 36 and 45.

`
36 = 2232
45 = 325

36 * 45 = 22345
`

Thus, we can maintain a table of **cumulative frequencies for each of the 25 primes between 1 to 100** for the given list of numbers.

When processing a query

- consider each of the 25 primes

- find the **frquency of the prime between L and R**. This can be done in O(1) using **pre-calculation of cumulative frequencies**

- calculate **primefrquency** for each prime and multiply these values

- maintain the result **modulo M**

These ideas are best presented in the pseudo code below.

### PSEUDO CODE
`
Given:
	N, the number of numbers
	L[N], the list of numbers
	P[25], primes between [1, 100]
	CF[N,25], cumulative frquency for each prime

for each query
	Given Query: left, right, M
	answer = 1
	for i = 1 to 25
		r = CF[right,i] - CF[left-1,i]
		v = P[i]r % M, use repeated squaring
		answer = (answer * v) % M

`

The complexity of answering each query would be **O(25 log N)**.

Cumulative Frequencies can be calculated in **O(25 * N)**.

### CODING COMMENTARY

You can either calculate the primes in thr porgram or hard code the array of primes by calculating it offline.

The repeated squaring should take care of the fact that the exponent can be 0. **a0** should return 1 for any **a**.

Calculating the cumulative frequencies table should be done carefully. The frequencies of the primes for each number between **1 and 100** can be **pre-calculated**. Use these frequencies to build the cumulative frequencies table.

### SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/August/Setter/CHMOD.cpp).

### TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2013/August/Tester/CHMOD.cpp).

</details>
