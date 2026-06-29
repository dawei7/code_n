# Profit Increment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PROINC |
| Difficulty Rating | 414 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [PROINC](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/PROINC) |

---

## Problem Statement

Chef recently started selling a special fruit.
He has been selling the fruit for $X$ rupees ($X$ is a multiple of $100$). He earns a profit of $Y$ rupees on selling the fruit currently.

Chef decided to increase the selling price by $10\%$. Please help him calculate his new profit after the increase in selling price.

Note that only the selling price has been increased and the buying price is same.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$ denoting the initial selling price and the profit respectively.

---

## Output Format

For each test case, output a single integer, denoting the new profit.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 1000$
- $1 \leq Y \leq 100$
- $X$ is a multiple of $100$.

---

## Examples

**Example 1**

**Input**

```text
4
100 10
200 5
500 10
100 7
```

**Output**

```text
20
25
60
17
```

**Explanation**

**Test case $1$:** The buying price of the item is the difference of selling price and profit, which is $90$. The new selling price is $10\%$ more than the initial selling price. Thus, the new profit is $110-90 = 20$.

**Test case $2$:** The buying price of the item is the difference of selling price and profit, which is $195$. The new selling price is $10\%$ more than the initial selling price. Thus, the new profit is $220-195 = 25$.

**Test case $3$:** The buying price of the item is the difference of selling price and profit, which is $490$. The new selling price is $10\%$ more than the initial selling price. Thus, the new profit is $550-490 = 60$.

**Test case $4$:** The buying price of the item is the difference of selling price and profit, which is $93$. The new selling price is $10\%$ more than the initial selling price. Thus, the new profit is $110-93 = 17$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 10
```

**Output for this case**

```text
20
```



#### Test case 2

**Input for this case**

```text
200 5
```

**Output for this case**

```text
25
```



#### Test case 3

**Input for this case**

```text
500 10
```

**Output for this case**

```text
60
```



#### Test case 4

**Input for this case**

```text
100 7
```

**Output for this case**

```text
17
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PROINC)

[Contest: Division 1](https://www.codechef.com/START75A/problems/PROINC)

[Contest: Division 2](https://www.codechef.com/START75B/problems/PROINC)

[Contest: Division 3](https://www.codechef.com/START75C/problems/PROINC)

[Contest: Division 4](https://www.codechef.com/START75D/problems/PROINC)

***Author:*** [tejas10p](https://www.codechef.com/users/tejas10p)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef sells a fruit for rupees X, and earns a profit of rupees Y.

If he increases the price of the fruit by 10\%, what’s his new profit?

#
[](#explanation-5)EXPLANATION:

The new price of the fruit is X increased by 10\%, i.e, X + \frac{X}{10}.

The increase in price is \frac{X}{10}, and so Chef’s profit will also increase by exactly this amount.

So, the total profit is now

Y + \frac{X}{10}

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y + x//10)
``

</details>
