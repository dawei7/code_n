# Building Race

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BUILDINGRACE |
| Difficulty Rating | 739 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [BUILDINGRACE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BUILDINGRACE) |

---

## Problem Statement

Two friends Chef and Chefina are currently on floors $A$ and $B$ respectively. They hear an announcement that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.

Chef can climb down $X$ floors per minute while Chefina can climb down $Y$ floors per minute. Determine who will reach the ground floor first (ie. floor number 0). In case both reach the ground floor together, print `Both`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains four space-separated integers $A$, $B$, $X$, and $Y$ — the current floor of Chef, the current floor of Chefina, speed of Chef and speed of Chefina in floors per minute respectively.

---

## Output Format

For each test case, output on a new line:
- `Chef` if Chef reaches the ground floor first.
- `Chefina` if she reaches the ground floor first.
- `Both` if both reach the ground floor at the same time.

You may print each character of the string in uppercase or lowercase. For example, the strings `CHEF`, `chef`, `Chef`, and `chEF` are all considered the same.

---

## Constraints

- $1 \leq T \leq 2500$
- $1 \leq A, B \leq 100$
- $1 \leq X, Y \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
2 2 2 2
4 2 1 5
3 2 4 1
3 2 2 1
```

**Output**

```text
Both
Chefina
Chef
Chef
```

**Explanation**

**Test case $1$:** Chef is on the second floor and has a speed of $2$ floors per minute. Thus, Chef takes $1$ minute to reach the ground floor. Chefina is on the second floor and and has a speed of $2$ floors per minute. Thus, Chefina takes $1$ minute to reach the ground floor. Both Chef and Chefina reach the ground floor at the same time.

**Test case $2$:** Chef is on the fourth floor and has a speed of $1$ floor per minute. Thus, Chef takes $4$ minute to reach the ground floor. Chefina is on the second floor and and has a speed of $5$ floors per minute. Thus, Chefina takes $0.4$ minutes to reach the ground floor. Chefina reaches the ground floor first.

**Test case $3$:** Chef is on the third floor and has a speed of $4$ floors per minute. Thus, Chef takes $0.75$ minutes to reach the ground floor. Chefina is on the second floor and and has a speed of $1$ floor per minute. Thus, Chefina takes $2$ minutes to reach the ground floor. Chef reaches the ground floor first.

**Test case $4$:** Chef is on the third floor and has a speed of $2$ floors per minute. Thus, Chef takes $1.5$ minutes to reach the ground floor. Chefina is on the second floor and and has a speed of $1$ floor per minute. Thus, Chefina takes $2$ minutes to reach the ground floor. Chef reaches the ground floor first.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 2 2
```

**Output for this case**

```text
Both
```



#### Test case 2

**Input for this case**

```text
4 2 1 5
```

**Output for this case**

```text
Chefina
```



#### Test case 3

**Input for this case**

```text
3 2 4 1
```

**Output for this case**

```text
Chef
```



#### Test case 4

**Input for this case**

```text
3 2 2 1
```

**Output for this case**

```text
Chef
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BUILDINGRACE)

[Contest: Division 1](https://www.codechef.com/OCT221A/problems/BUILDINGRACE)

[Contest: Division 2](https://www.codechef.com/OCT221B/problems/BUILDINGRACE)

[Contest: Division 3](https://www.codechef.com/OCT221C/problems/BUILDINGRACE)

[Contest: Division 4](https://www.codechef.com/OCT221D/problems/BUILDINGRACE)

***Author:*** [Pratiyush MIshra](https://www.codechef.com/users/foxy7)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is on floor A and can run down X floors a minute. Chefina is on floor B and can run down Y floors a minute. Who reaches the ground floor faster?

#
[](#explanation-5)EXPLANATION:

The time taken equals distance divided by speed.

So,

- Chef takes \frac{A}{X} minutes to reach the ground floor.

- Chefina takes \frac{B}{Y} minutes to reach the ground floor.

Compute these two values, and then compare them.

- If they are equal, the answer is “Both”.

- If \frac{A}{X} is smaller, the answer is “Chef”

- Otherwise, the answer is Chefina.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    if a*y == b*x:
        print('Both')
    elif a*y > b*x:
        print('Chefina')
    else:
        print('Chef')
``

</details>
