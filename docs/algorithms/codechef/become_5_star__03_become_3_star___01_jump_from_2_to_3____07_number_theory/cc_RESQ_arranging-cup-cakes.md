# Arranging Cup-cakes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RESQ |
| Difficulty Rating | 1322 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [RESQ](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/RESQ) |

---

## Problem Statement

Our Chef is catering for a big corporate office party and is busy preparing different mouth watering dishes. The host has insisted that he serves his delicious cupcakes for dessert.

 On the day of the party, the Chef was over-seeing all the food arrangements as well, ensuring that every item was in its designated position. The host was satisfied with everything except the cupcakes. He noticed they were arranged neatly in the shape of a rectangle. He asks the Chef to make it as square-like as possible.

 The Chef is in no mood to waste his cupcakes by transforming it into a perfect square arrangement. Instead, to fool the host, he asks you to arrange the **N** cupcakes as a rectangle so that the **difference** between the length and the width is minimized.

### Input

The first line of the input file contains an integer **T**, the number of test cases. Each of the following **T** lines contains a single integer **N** denoting the number of cupcakes.

### Output

Output **T** lines, each indicating the minimum possible difference between the length and the width in a rectangular arrangement of the cupcakes.

### Constraints

1 ≤ **T** ≤ 100

1 ≤ **N** ≤ 108

---

## Examples

**Example 1**

**Input**

```text
4
20
13
8
4
```

**Output**

```text
1
12
2
0
```

**Explanation**

**Test case $1$:** $20$ cupcakes can be arranged in a rectange in $6$ possible ways -  $1 \times 20, 2 \times 10, 4 \times 5, 5 \times 4, 10 \times 2$ and $20 \times 1$.
The corresponding differences between the length and the width for each of these rectangles are $ |1-20| = 19, |2-10| = 8, |4-5| = 1, |5-4| = 1, |10-2| = 8$ and $|20-1| = 19$ respectively. Hence, $1$ is the smallest difference between length and width among all possible combinations.

**Test case $2$:** $13$ cupcakes can be arranged in $2$ ways only. These are $13 \times 1$ and $1 \times 13$. In both cases, the difference between width and length is $12$.

**Test case $3$:** $8$ cupcakes can be arranged in $4$ ways. These are: $8\times 1, 4\times 2, 2\times 4$ and $1\times 8$. The minimum difference between length and width is $2$ which is in the cases $4\times 2 $ and $2\times 4$.

**Test case $4$:** $4$ cupcakes can be arranged as $2\times 2$. The difference between the length and the width, in this case, is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
20
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
13
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
8
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## PROBLEM LINKS:

[Practice](http://www.codechef.com/problems/RESQ)

[Contest](http://www.codechef.com/JUNE12/problems/RESQ)

## DIFFICULTY:

Simple

## PREREQUISITES:

Math, [Prime Factorization](http://en.wikipedia.org/wiki/Prime_factor)

## PROBLEM:

The aim is to find two numbers **x** and **y** such that **x * y = N** and **|y – x|** is as small as possible.

## EXPLANATION:

This looks like a simple factorization problem, doesn’t it?

``ans = INF
for x = 1 to N:
	if N mod x = 0:
		y = N / x is integer
		ans = min(ans, abs(y – x))
``

However, the program written by the above logic will get TLE. The reason being, **N** can be as large as **108**. It is safe to assume that a loop over **108** numbers will not take less than **1** second on the CodeChef judge. And considering that the test data will have up to 100 such numbers, we cannot pass the time limit with the above solution.

The important trick here is to notice that when we consider some **x** in the above loop that is greater than **[sqrt(N)]** (the largest integer that is not greater than square root of **N**) then **y** will be less than **[sqrt(N)]** and it means that we have considered pair **(y, x)** earlier in this loop. Also for this pair we have the same absolute value of difference as for current pair **(x, y)** and hence we can simply skip values of **x** that are greater than **[sqrt(N)]** which transforms our program to the following one

``ans = INF
for x = 1 to [sqrt(N)]:
	if N mod x = 0:
		y = N / x is integer
		ans = min(ans, y – x)
``

This solution has complexity **O(sqrt(N))** for each test and since we have **T <= 100** tests in each test file it safely fits in the time limit. Note the we get rid of **abs** since **y** now is always not less than **x**.

Also, as **x** reaches closer to **[sqrt(N)]** on the number line, **y = N / x** also reaches closer to **[sqrt(N)]** from the other side, i.e. as **x** increases, **y** decreases. This means that the difference between **x** and **y** is decreasing as we continue through the loop. Hence, the answer will be the difference between **x** and **N / x** where **x** is the largest factor of **N** which is not greater than **[sqrt(N)]**. The solution can be further optimised as:

``ans = INF
for x = [sqrt(N)] downto 1:
	if N mod x = 0:
		y = N / x
		ans = y – x
		break;
``

## SETTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/June/Setter/RESQ.cpp).

### APPROACH:

The problem setter used the above approach to solve the problem.

## TESTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/June/Tester/RESQ.cpp).

### APPROACH:

Here, the problem tester used the above approach to solve the problem.

## ALTERNATE TESTER’S SOLUTION:

Can be found [here](http://www.codechef.com/download/Solutions/2012/June/Tester/RESQ1.cpp).

### APPROACH:

This approach uses the [Sieve of Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) algorithm for finding prime numbers. Using this, we find all the primes till sqrt(N) once and store them in an array. Since the maximum value of N is 108, it is enough to find the primes till sqrt(108) = 104.

Now, for every given N, we find all its prime factors and store them in an array. This can be done by looping over the prime numbers that we generated earlier and checking if each of it is a factor of N. We check for only those numbers which are not greater than sqrt(N). If any of those prime numbers is a factor, we calculate the degree of that factor. By degree of a factor we mean the number of times the factor divides the number. For example, 24 = 23.31. Here 2 (the prime factor) has a degree of 3 and 3(the next prime factor) has a degree of 1.

Next we try to generate all the divisors of N using the above information that we gathered. Initially our divisors array will have 1 in it (1 is a divisor of every number ). We can do this by going through each prime factor x, and multiply each element in the existing divisors array by xi where 0<=i<=degree[x]. For example, let N = 84.

84 can be written as 22.31.71

*Divisors*: 1 *Prime Factor*: 2 *New*

*Divisors*: 2x1 , 22x1

*Divisors*: 1, 2, 4 *Prime Factor*: 3 *New*

*Divisors*: 1, 2, 4, 3, 6, 12

*Divisors*: 1, 2, 4, 3, 6, 12 *Prime*

*Factor*: 7 *New Divisors*: 1, 2, 4, 3, 6,

12, 7, 14, 28, 21, 42, 84

So we finally have the array of the entire divisors. Note that we do not have these divisors in the sorted order. So we will have to check for every divisor d, and check for the minimum difference of **|d – N/d|**.

This approach is asymptotically better than the previous approach. Let’s look at the complexity of this solution. Generating the primes using the sieve has **O(sqrt(N) * log log N)** complexity. And on an average, getting all the prime factors and generating the divisors of a number will take **O(sqrt(N)/log(N))** time. So the overall complexity is **O(sqrt(N) * log log N + T * sqrt(N) / log(N))** .

</details>
