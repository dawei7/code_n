# Monthly Budget

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BUDGET_ |
| Difficulty Rating | 456 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BUDGET_](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BUDGET_) |

---

## Problem Statement

Akshat has $X$ rupees to spend in the current month. His daily expenditure is $Y$ rupees, i.e., he spends $Y$ rupees each day.

Given that the current month has $30$ days, find out if Akshat has enough money to meet his daily expenditures for this month.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$, $Y$ - the amount of money Akshat has for the current month and his daily expenditure respectively.

---

## Output Format

For each test case, output `YES` if Akshat has enough money to meet his daily expenditure for $30$ days of the month, otherwise output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1000 10
250 50
1500 50
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test Case $1$:** Akshat has $1000$ rupees and he wants to spend $30 \times 10 = 300$ rupees in the entire month. Therefore, he has enough money for the entire month.

**Test Case $2$:** Akshat has $250$ rupees and he wants to spend $30 \times 50 = 1500$ rupees in the entire month. Therefore, he does not have enough money for the entire month.

**Test Case $3$:** Akshat has $1500$ rupees and he wants to spend $30 \times 50 = 1500$ rupees in the entire month. Therefore, he has enough money for the entire month.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1000 10
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
250 50
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
1500 50
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START33A/problems/BUDGET_)

[Contest Division 2](https://www.codechef.com/START33B/problems/BUDGET_)

[Contest Division 3](https://www.codechef.com/START33C/problems/BUDGET_)

[Contest Division 4](https://www.codechef.com/START33D/problems/BUDGET_)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Akshat has X rupees to spend in the current month. His daily expenditure is Y rupees, i.e., he spends Y rupees each day.

Given that the current month has 30 days, find out if Akshat has enough money to meet his daily expenditures for this month.

#
[](#explanation-5)EXPLANATION:

For each test case, we are given two integer values X and Y which are the monthly budget and daily expenditure respectively.

Since Akshat will have enough money if the budget is greater than or equal to the monthly expenditure hence Akshat will have enough money if X \ge 30.Y else money will not be enough.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/i8_k)

[Setter’s Solution](http://p.ip.fi/sUeK)

[Tester-1’s Solution](http://p.ip.fi/rxUH)

[Tester-2’s Solution](http://p.ip.fi/EPBI)

</details>
