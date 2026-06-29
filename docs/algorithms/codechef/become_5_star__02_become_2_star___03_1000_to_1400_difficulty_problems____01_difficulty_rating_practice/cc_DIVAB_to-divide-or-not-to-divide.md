# To Divide or Not To Divide

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVAB |
| Difficulty Rating | 1224 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DIVAB](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DIVAB) |

---

## Problem Statement

Alice likes all the numbers which are divisible by $A$. Bob does **not** like the numbers which are divisible by $B$ and likes all the remaining numbers. Determine the smallest number **greater than or equal to** $N$ which is liked by both Alice and Bob. Output $-1$ if no such number exists.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains three space-separated integers $A$, $B$ and $N$ — the parameters mentioned in the problem statment.

---

## Output Format

For each test case, output the smallest number $\ge$ $N$ which is divisible by $A$ and is **not** divisible by $B$. Output $-1$ if no such number exists.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
5 2 11
4 3 24
7 7 100
```

**Output**

```text
15
28
-1
```

**Explanation**

**Test case $1$:** $15$ is the smallest number $\ge$ $11$ which is divisible by $5$ and is not divisible by $2$.

**Test case $2$:** $28$ is the smallest number $\ge$ $24$ which is divisible by $4$ and is not divisible by $3$.

**Test case $3$:** There does not exist any number which is divisible by $A = 7$ and is not divisible by $B = 7$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 11
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
4 3 24
```

**Output for this case**

```text
28
```



#### Test case 3

**Input for this case**

```text
7 7 100
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY222/)

[Practice](https://www.codechef.com/problems/DIVAB)

**Setter:** [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Testers:** [tejas10p](https://www.codechef.com/users/tejas10p), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [hrishik85](https://www.codechef.com/users/hrishik85)

#
[](#difficulty-2)DIFFICULTY:

1224

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Determine the smallest number **greater than or equal to** N which is divisible by A but not divisible by B. Output -1 if no such number exists.

#
[](#explanation-5)EXPLANATION:

We will output -1 when A \mod B = 0 because in this scenario ? there can never be a number which is divisible by A but not by B

For all other cases, we need to find the number larger than N which is divisble by A ?

N_{new} =(A \times math.ceil(N \div A))

- If this number is not divisible by B, we output N

- If this number is divisible by B, then we replace N = N + A and keep repeating these 2 steps till we find an N which is not divisible by B

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``t=int(input())
for _ in range(t):
    A, B, N = map(int,input().split())
    if A%B==0:
        print(-1)
    else:
        if N%A!=0:
            N = (N//A + 1) * A
        while N%B==0:
            N = N + A
        print(N)
``

</details>
