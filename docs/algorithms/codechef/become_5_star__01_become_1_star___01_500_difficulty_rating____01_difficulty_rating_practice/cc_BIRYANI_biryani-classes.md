# Biryani classes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BIRYANI |
| Difficulty Rating | 257 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BIRYANI](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BIRYANI) |

---

## Problem Statement

According to a recent survey, Biryani is the most ordered food. Chef wants to learn how to make world-class Biryani from a MasterChef. Chef will be required to attend the MasterChef's classes for $X$ weeks, and the cost of classes per week is $Y$ coins. What is the total amount of money that Chef will have to pay?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output on a new line the total amount of money that Chef will have to pay.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
1 10
1 15
2 10
2 15
```

**Output**

```text
10
15
20
30
```

**Explanation**

**Test case $1$:** Chef will be required to attend the MasterChef's classes for $1$ week and the cost of classes per week is $10$ coins. Hence, Chef will have to pay $10$ coins in total.

**Test case $2$:** Chef will be required to attend the MasterChef's classes for $1$ week and the cost of classes per week is $15$ coins. Hence, Chef will have to pay $15$ coins in total.

**Test case $3$:** Chef will be required to attend the MasterChef's classes for $2$ weeks and the cost of classes per week is $10$ coins. Hence, Chef will have to pay $20$ coins in total.

**Test case $4$:** Chef will be required to attend the MasterChef's classes for $2$ weeks and the cost of classes per week is $15$ coins. Hence, Chef will have to pay $30$ coins in total.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 10
```

**Output for this case**

```text
10
```



#### Test case 2

**Input for this case**

```text
1 15
```

**Output for this case**

```text
15
```



#### Test case 3

**Input for this case**

```text
2 10
```

**Output for this case**

```text
20
```



#### Test case 4

**Input for this case**

```text
2 15
```

**Output for this case**

```text
30
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START44A/problems/BIRYANI)

[Contest Division 2](https://www.codechef.com/START44B/problems/BIRYANI)

[Contest Division 3](https://www.codechef.com/START44C/problems/BIRYANI)

[Contest Division 4](https://www.codechef.com/START44D/problems/BIRYANI)

**Setter:** [lavish_adm](https://www.codechef.com/users/lavish_adm)

**Testers:** [utkarsh_adm](https://www.codechef.com/users/utkarsh_adm), [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

257

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

**Chef wants to attend the Masterchef’s classes for X weeks. The cost of classes per week is Y coins. What is the total amount that the Chef will have to pay?**

#
[](#explanation-5)EXPLANATION:

The main objective of this problem is to test the user’s ability to read multiple inputs on different lines.

The total amount to be paid is = (Cost per week x Number of weeks) = X * Y

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``for _ in range(int(input())):
    x,y = map(int,input().split())
    print(x*y)
``

</details>
