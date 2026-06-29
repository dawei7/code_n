# Airlines

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPCP2 |
| Difficulty Rating | 712 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SPCP2](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SPCP2) |

---

## Problem Statement

An airline operates $X$ aircraft every day. Each aircraft can carry up to $100$ passengers.
One day, $N$ passengers would like to travel to the same destination. What is the minimum number of new planes that the airline must buy to carry all $N$ passengers?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers $X$ and $N$ — the number of aircraft the airline owns and the number of passengers travelling, respectively.

---

## Output Format

- For each test case, output the minimum number of planes the airline needs to purchase.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 10^6$
- $1 \leq N \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
4 600
3 523
8 245
```

**Output**

```text
2
3
0
```

**Explanation**

**Test case $1$:** The airline needs at least $6$ planes to carry $600$ passengers. They already have $4$, so they must purchase $2$ more.

**Test case $2$:** The airline needs at least $6$ planes to carry $523$ passengers. They already have $3$, so they must purchase $3$ more.

**Test case $3$:** The airline needs at least $3$ planes to carry $245$ passengers. They already have $8$, so there's no need to purchase any more.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 600
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 523
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
8 245
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SPCP2)

[Contest: Division 1](https://www.codechef.com/START110A/problems/SPCP2)

[Contest: Division 2](https://www.codechef.com/START110B/problems/SPCP2)

[Contest: Division 3](https://www.codechef.com/START110C/problems/SPCP2)

[Contest: Division 4](https://www.codechef.com/START110D/problems/SPCP2)

***Author:*** [kg_26,](https://www.codechef.com/users/kg_26) [alpha_ashwin](https://www.codechef.com/users/alpha_ashwin)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

An airline has X flights, each of which can carry 100 people.

How many more do they need to carry N people in total?

# [](#explanation-5)EXPLANATION:

Each flight can hold 100 people, so initially the airline can carry 100\cdot X people.

So, if 100\cdot X \geq N, no more aircraft are needed and the answer is 0.

Otherwise, N - 100\cdot X people are remaining.

Since 100 of them can be placed on a single flight, the minimum number of flights needed is

\left\lceil \frac{N-100\cdot X}{100} \right\rceil

where \left\lceil \ \  \right\rceil denotes the [ceiling](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions) function.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``from math import ceil
for _ in range(int(input())):
    x, n = map(int, input().split())
    print(max(0, ceil((n - 100*x)/100)))
``

</details>
