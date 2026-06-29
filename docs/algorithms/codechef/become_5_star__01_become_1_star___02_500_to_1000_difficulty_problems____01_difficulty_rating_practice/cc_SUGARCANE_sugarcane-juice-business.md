# Sugarcane Juice Business

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUGARCANE |
| Difficulty Rating | 563 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SUGARCANE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SUGARCANE) |

---

## Problem Statement

While Alice was drinking sugarcane juice, she started wondering about the following facts:
- The juicer sells each glass of sugarcane juice for $50$ coins.
- He spends $20\%$ of his total income on buying sugarcane.
- He spends $20\%$ of his total income on buying salt and mint leaves.
- He spends $30\%$ of his total income on shop rent.

Alice wonders, what is the juicer's profit (in coins) when he sells $N$ glasses of sugarcane juice?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$, as described in the problem statement.

---

## Output Format

For each test case, output on a new line the juicer's profit when he sells $N$ glasses of juice.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
4
2
4
5
10
```

**Output**

```text
30
60
75
150
```

**Explanation**

**Test case $1$**: The total income is $50\times 2 = 100$ coins. The juicer spends $20$ coins on sugarcane, $20$ coins on  salt and mint leaves and $30$ coins on rent. Thus, the profit is $100-(20+20+30) = 30$ coins.

**Test case $2$**: The total income is $50\times 4 = 200$ coins. The juicer spends $40$ coins on sugarcane, $40$ coins on  salt and mint leaves and $60$ coins on rent. Thus, the profit is $200-(40+40+60) = 60$ coins.

**Test case $3$**: The total income is $50\times 5 = 250$ coins. The juicer spends $50$ coins on sugarcane, $50$ coins on  salt and mint leaves and $75$ coins on rent. Thus, the profit is $250-(50+50+75) = 75$ coins.

**Test case $4$**: The total income is $50\times 10 = 500$ coins. The juicer spends $100$ coins on sugarcane, $100$ coins on  salt and mint leaves and $150$ coins on rent. Thus, the profit is $500-(100+100+150) = 150$ coins.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
30
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
60
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
75
```



#### Test case 4

**Input for this case**

```text
10
```

**Output for this case**

```text
150
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUGARCANE)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/SUGARCANE)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/SUGARCANE)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/SUGARCANE)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/SUGARCANE)

***Author:*** [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

Basic mathematical reasoning

#
[](#problem-4)PROBLEM:

A sugarcane juicer sells each glass of juice for 50 coins. 20\% of his income is spent on buying sugarcane, 20\% is spent on salt and mint leaves, and a further 30\% is spent on shop rent.

If he sells a total of N glasses of juice, what is his overall profit?

#
[](#explanation-5)EXPLANATION:

Let’s look at what happens when N = 1. The juicer sells one glass of juice for 50 coins. Then,

- He spends 20\% of 50 on sugarcane, which is 10 coins.

- Another 20\% is spent on salt and mint, which is another 10 coins.

-
30\% is spent on rent, which is 15 coins.

So, his total costs come out to be 10 + 10 + 15 = 35, and hence his profit is 50 - 35 = 15 coins.

Now note that the same calculation applies to every glass sold, so he earns a profit of 15 coins per glass sold. So, his final profit is 15\cdot N coins.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per test.

#
[](#code-7)CODE:

Python
``for _ in range(int(input())):
	print(15*int(input()))
``

</details>
