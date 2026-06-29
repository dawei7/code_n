# Four Tickets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FOURTICKETS |
| Difficulty Rating | 302 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FOURTICKETS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FOURTICKETS) |

---

## Problem Statement

Four friends want to attend a concert. Each ticket costs $X$ rupees.
They have decided to go to the concert if and only if the total cost of the tickets does **not exceed** $1000$ rupees.

Determine whether they will be going to the concert or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $X$, the cost of each ticket.

---

## Output Format

For each test case, output `YES` if they will be going to the concert, `NO` otherwise.

You can print each character in uppercase or lowercase. For example, the strings `YES`, `yes`, `Yes`, and `yES`, are all considered identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
100
500
250
1000
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** The total cost of all tickets is $100\cdot 4 = 400$ which is $\le 1000$. Thus, they will go to the concert.

**Test case $2$:** The total cost of all tickets is $500\cdot 4 = 2000$ which is $\gt 1000$. Thus, they will not go to the concert.

**Test case $3$:** The total cost of all tickets is $250\cdot 4 = 1000$ which is $\le 1000$. Thus, they will go to the concert.

**Test case $4$:** The total cost of all tickets is $1000\cdot 4 = 4000$ which is $\gt 1000$. Thus, they will not go to the concert.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
500
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
250
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
1000
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FOURTICKETS)

[Contest: Division 1](https://www.codechef.com/START87A/problems/FOURTICKETS)

[Contest: Division 2](https://www.codechef.com/START87B/problems/FOURTICKETS)

[Contest: Division 3](https://www.codechef.com/START87C/problems/FOURTICKETS)

[Contest: Division 4](https://www.codechef.com/START87D/problems/FOURTICKETS)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

302

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Four friends want to attend a concert, each ticket of which costs X rupees.

However, they will only attend if the total cost doesn’t attend 1000 rupees.

Will they attend the concert?

#
[](#explanation-5)EXPLANATION:

Since each ticket costs X rupees and there are 4 friends, the total cost of the tickets is 4\cdot X rupees.

So, the answer is `Yes` if 4\cdot X \leq 1000 and `No` otherwise.

Note that this is the same thing as X \leq 250, so checking for that is a valid condition too.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x = int(input())
    print('Yes' if x <= 250 else 'No')
``

</details>
