# Bull or Bear

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BULLBEAR |
| Difficulty Rating | 300 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BULLBEAR](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BULLBEAR) |

---

## Problem Statement

Chef is on his way to become the new big bull of the stock market but is a bit weak at calculating whether he made a profit or a loss on his deal.

Given that Chef bought the stock at value $X$ and sold it at value $Y$. Help him calculate whether he made a profit, loss, or was it a neutral deal.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing two space-separated integers $X$ and $Y$, denoting the value at which Chef bought and sold the stock respectively.

---

## Output Format

For each test case, output `PROFIT` if Chef made a profit on the deal, `LOSS` if Chef incurred a loss on the deal, and `NEUTRAL` otherwise.

The checker is case-insensitive so answers like `pROfiT`, `profit`, and `PROFIT` would be considered the same.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
4 2
8 8
3 4
2 1
```

**Output**

```text
LOSS
NEUTRAL
PROFIT
LOSS
```

**Explanation**

**Test case $1$:** Since the cost price is greater than the selling price, Chef made a loss in the deal.

**Test case $2$:** Since the cost price is equal to the selling price, the deal was neutral.

**Test case $3$:** Since the cost price is less than the selling price, Chef made a profit in the deal.

**Test case $4$:** Since the cost price is greater than the selling price, Chef made a loss in the deal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
```

**Output for this case**

```text
LOSS
```



#### Test case 2

**Input for this case**

```text
8 8
```

**Output for this case**

```text
NEUTRAL
```



#### Test case 3

**Input for this case**

```text
3 4
```

**Output for this case**

```text
PROFIT
```



#### Test case 4

**Input for this case**

```text
2 1
```

**Output for this case**

```text
LOSS
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BULLBEAR)

[Contest: Division 1](https://www.codechef.com/START68A/problems/BULLBEAR)

[Contest: Division 2](https://www.codechef.com/START68B/problems/BULLBEAR)

[Contest: Division 3](https://www.codechef.com/START68C/problems/BULLBEAR)

[Contest: Division 4](https://www.codechef.com/START68D/problems/BULLBEAR)

***Author:*** [tejas10p](https://www.codechef.com/users/tejas10p)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

300

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef bought a stock at value X and sold it at value Y. Did he make a profit, loss, or neither?

#
[](#explanation-5)EXPLANATION:

This task is solved by simple case analysis:

- If X \gt Y, Chef spent more than he gained, so he made a loss.

- If X \lt Y, Chef spent less than he gained, so he made a profit.

- If X = Y, Chef’s spending equals his gains, so it was a neutral deal.

Check all three cases using `if` conditions and print the appropriate answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Profit' if x < y else 'Loss' if x > y else 'Neutral')
``

</details>
