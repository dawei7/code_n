# Chef and Magical Steps

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFMGXPRIME |
| Difficulty Rating | 2004 |
| Difficulty Band | Number theory |
| Path | Data Structures and Algorithms |
| Lesson | Sieve of Eratosthenes |
| Official Link | [CHEFMGXPRIME](https://www.codechef.com/learn/course/number-theory/LINTDSA09/problems/CHEFMGXPRIME) |

---

## Problem Statement

Chef has a new customer and he wants to prepare his order as soon as possible. While preparing, he sees that he is out of mint sauce. He has to run upstairs to get it from other kitchen. Chef is currently on the $X^{th}$ stair. He has to climb all the way up to the $Y^{th}$ stair in minimum number of steps. In one step, Chef can do one of the following things:

- Climb a single stair. ( i.e go from the $X^{th}$ stair to the $(X+1)^{th}$ stair. )
- Climb two stairs only if the final stair falls at a prime number position. ( i.e. go from the $X^{th}$ stair to the $(X+2)^{th}$ stair, only if $(X + 2$) is a prime number)

Help Chef reach the $Y^{th}$ stair from the $X^{th}$ stair in minimum number of steps.

$\textbf{See Explanation for more clarity.}$

**Note:** The input files are large. The use of Fast I/O is recommended.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains $X$ and $Y$ denoting the starting stair and ending stair respectively.

---

## Output Format

- Output a single integer representing minimum number of steps chef can take to reach from $X^{th}$ to $Y^{th}$ stair.

---

## Constraints

- $1 \leq T \leq 10^6$
- $1 \leq X \lt Y \leq 10^7$

---

## Examples

**Example 1**

**Input**

```text
4
2 10
5 12
34 43
57 63
```

**Output**

```text
6
5
6
4
```

**Explanation**

**Test case $1$**: Chef starts from $2^{nd}$, goes to $3^{rd}$ stair, then to $5^{th}$ stair as $5$ or $(3+2)$ is prime number. Now, from $5^{th}$ stair, Chef goes to $7^{th}$ stair as $7$ or $(5+2)$ is a prime number, then Chef goes to $8^{th}$ stair, then to $9^{th}$ stair and finally to $10^{th}$ stair. This approach takes a total of $6$ steps which is the minimum possible number of steps Chef can take to reach the $10^{th}$ stair starting from the $2^{nd}$ stair.

**Test case $3$**: Starting from the $34^{th}$ stair, Chef moves through the stairs as following. $34$ → $35$ → $37$ → $38$ → $39$ → $41$ → $43$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 10
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
5 12
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
34 43
```

**Output for this case**

```text
6
```



#### Test case 4

**Input for this case**

```text
57 63
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Chef and Magical Steps in Number theory](https://www.codechef.com/learn/course/number-theory/LINTDSA09/problems/CHEFMGXPRIME)

### [](#problem-statement-1)Problem Statement:

Chef needs to climb from the Xth stair to the Yth stair in the minimum number of steps. He can either climb one stair at a time or climb two stairs if the destination stair (X+2) is a prime number.

Help Chef reach the Yth stair from the Xth stair in minimum number of steps.

### [](#approach-2)Approach:

- Chef can move from stair X to stair Y in two ways:

- Climbing one stair at a time: Chef moves from i to i+1.

- Climbing two stairs at a time: Chef can only do this if the final stair position he lands on (i.e., X+2) is a prime number.

- To determine the minimum number of steps Chef can take to reach from stair X to stair Y, we need to understand how the ability to skip stairs (by climbing two at a time) influences the overall step count.

- Counting Non-Primes: By computing the number of non-prime stairs between X and Y, we can derive the minimum number of steps Chef must take.

**Why are we calculating non-primes:**

- Chef can only skip one stair if the resulting stair is prime. Thus, the number of non-prime stairs in the range directly affects how Chef can progress.

- If a stair is non-prime, Chef can only move to it by climbing one stair at a time.

- The more non-prime stairs there are, the fewer opportunities Chef has to jump by two stairs.

- The formula used to compute the minimum number of steps is:

**Steps** = Y − X − (count of primes between X+1 and Y)

- Y−X: Represents the total distance Chef needs to cover in terms of stairs.

- **(count of primes between X+1 and Y)**: Represents the maximum number of two-stair jumps Chef can make. Each prime number allows Chef to skip an additional stair, thus reducing the total number of steps he needs to take.

By subtracting the count of prime stairs from the total distance, we effectively compute the number of individual steps Chef must take due to the constraints imposed by non-prime stairs.

### [](#complexity-3)Complexity:

- **Time Complexity:** The Sieve of Eratosthenes runs in `O(n log ⁡log ⁡n)` for precomputation.

- **Space Complexity:** The space used is `O(n)` for computing prime numbers and total prime numbers in a given range.

</details>
