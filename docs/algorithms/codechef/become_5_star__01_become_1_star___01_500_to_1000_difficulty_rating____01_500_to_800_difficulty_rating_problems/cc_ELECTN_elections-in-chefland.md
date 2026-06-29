# Elections in Chefland

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ELECTN |
| Difficulty Rating | 604 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [ELECTN](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/ELECTN) |

---

## Problem Statement

Election season has started in Chefland and the election commission wants to know the count of eligible voters.

There are $N$ people in Chefland where the age of the $i^{th}$ person in $A_i$.
Given that a person needs to be **at least** $X$ years old to vote, find the number of eligible voters.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $X$ — the number of people in Chefland, and the minimum age required for a person to vote in Chefland.
    - The next line contains $N$ space-separated integers, where the $i^{th}$ integer denotes the age of the $i^{th}$ person.

---

## Output Format

For each test case, output on a new line, the number of eligible voters in Chefland.

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 100$
- $1 \leq A_i, X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
4 3
5 3 1 2
3 2
1 3 4
4 2
2 1 2 4
5 6
1 2 3 4 5
```

**Output**

```text
2
2
3
0
```

**Explanation**

**Test case $1$:** The minimum age to vote in Chefland is $3$ years. There are $2$ people with age greater than equal to $3$ and thus, there are $2$ eligible voters.

**Test case $2$:** The minimum age to vote in Chefland is $2$ years. There are $2$ people with age greater than equal to $2$ and thus, there are $2$ eligible voters.

**Test case $3$:** The minimum age to vote in Chefland is $2$ years. There are $3$ people with age greater than equal to $2$ and thus, there are $3$ eligible voters.

**Test case $4$:** The minimum age to vote in Chefland is $6$ years. There are no people with age greater than equal to $6$ and thus, there are no eligible voters.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3
5 3 1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 2
1 3 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 2
2 1 2 4
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
5 6
1 2 3 4 5
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ELECTN)

[Contest: Division 1](https://www.codechef.com/START84A/problems/ELECTN)

[Contest: Division 2](https://www.codechef.com/START84B/problems/ELECTN)

[Contest: Division 3](https://www.codechef.com/START84C/problems/ELECTN)

[Contest: Division 4](https://www.codechef.com/START84D/problems/ELECTN)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

604

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the ages of N people and the minimum age to vote X, find the number of people who can vote.

#
[](#explanation-5)EXPLANATION:

This is a straightforward application of loops and conditional statements.

Iterate through the given array, and each time you have A_i \geq X, add one to the answer.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(1 for y in a if y >= x))
``

</details>
