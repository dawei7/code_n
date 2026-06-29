# Make Money

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEMONEY |
| Difficulty Rating | 1101 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MAKEMONEY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAKEMONEY) |

---

## Problem Statement

Chef has $N$ bags and an integer $X$. The $i^{th}$ bag contains $A_i$ coins such that $A_i \leq X$.

In one operation, Chef can:
- Pick any bag and increase its coins to $X$. Formally, if he choses the $i^{th}$ bag, he can set $A_i = X$.

Given that the cost of performing **each** operation is $C$ $(C \leq X)$ coins and Chef can perform the above operation any (possibly zero) number of times, determine the **maximum** value of

$(\sum_{i=1}^N A_i)$ $-$ (total cost paid by Chef),

if Chef performs the operations optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains three space-separated integers $N$, $X$, and $C$ — the number of bags, maximum limit of coins on each bag and cost of each operation respectively.
    - The next line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ - denoting the number of coins in each bag.

---

## Output Format

For each test case, output the maximum value of $\sum_{i=1}^N A_i$ $-$ total cost paid by Chef.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq C \leq X \leq 100$
- $1 \leq A_i \leq X$

---

## Examples

**Example 1**

**Input**

```text
3
5 5 2
1 2 3 4 5
3 4 4
1 1 1
5 3 2
3 2 3 1 1
```

**Output**

```text
18
3
10
```

**Explanation**

**Test case $1$:** It is optimal for Chef to perform $2$ operations:
- Operation $1$: Choose $i = 1$ and set $A_1 = 5$ by using $2$ coins.
- Operation $2$: Choose $i = 2$ and set $A_2 = 5$ by using $2$ coins.

The final array is $A = [5, 5, 3, 4, 5]$ and the total cost is $2+2 = 4$. Thus, the value of $\sum_{i=1}^N A_i$ $-$ total cost is $(5+5+3+4+5) - 4 = 22-4 = 18$.

**Test case $2$:** It is optimal for Chef to perform $0$ operations. Thus, the final array remains $[1, 1, 1]$ and the cost is $0$. The value of $\sum_{i=1}^N A_i$ $-$ total cost is $(1+1+1) - 0 = 3$.

**Test case $3$:** It is optimal for Chef to perform $0$ operations. Thus, the final array remains $[3, 2, 3, 1, 1]$ and the cost is $0$. The value of $\sum_{i=1}^N A_i$ $-$ total cost is $(3+2+3+1+1) - 0 = 10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5 2
1 2 3 4 5
```

**Output for this case**

```text
18
```



#### Test case 2

**Input for this case**

```text
3 4 4
1 1 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
5 3 2
3 2 3 1 1
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAKEMONEY)

[Contest: Division 1](https://www.codechef.com/START68A/problems/MAKEMONEY)

[Contest: Division 2](https://www.codechef.com/START68B/problems/MAKEMONEY)

[Contest: Division 3](https://www.codechef.com/START68C/problems/MAKEMONEY)

[Contest: Division 4](https://www.codechef.com/START68D/problems/MAKEMONEY)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1101

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has N bags, the i-th with A_i \leq X coins. He can pay C coins to increase the number of coins in the i-th bag to X.

Find the maximum possible value of \sum A_i - cost, where cost is the number of coins paid by Chef when performing operations.

#
[](#explanation-5)EXPLANATION:

Let’s look at the i-th bag. We can either increase the coins in it or choose not to.

- If we don’t do anything, this bag gives us A_i coins.

- If we increase it, this bag gives us X coins but also a cost of C, for a total of X-C.

Since we’re free to perform operations as many times as we want to, we can simply take the maximum of the above two values; and then repeat this for every index.

That is, the final answer is

\sum_{i=1}^N \max(A_i, X-C)

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x, c = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum(max(y, x-c) for y in a))
``

</details>
