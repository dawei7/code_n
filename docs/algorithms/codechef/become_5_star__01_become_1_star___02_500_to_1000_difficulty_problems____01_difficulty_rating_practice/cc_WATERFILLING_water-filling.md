# Water Filling

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATERFILLING |
| Difficulty Rating | 541 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [WATERFILLING](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WATERFILLING) |

---

## Problem Statement

Chef has three water bottles. At any point, if at least two of them are empty, she will fill them up. But if at most one bottle is empty, she will wait, and not fill them up now.

You are given three integers - $B_1, B_2,$ and $B_3$. \
If $B_1 = 1$, it means that the first bottle is full. \
If $B_1 = 0$, it means that the first bottle is empty. \
Similarly, $B_2$ denotes whether the second bottle is full or empty, and $B_3$ denotes it for the third bottle.

Output "Water filling time", if Chef has to fill the bottles now. If not, output "Not now".

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains three space-separated integers, $B_1, B_2, B_3$.

---

## Output Format

For each test case, output on a new line, either "Water filling time", or "Not now".

---

## Constraints

- $1 \leq T \leq 1000$
- $B_i$ is either $0$ or $1$

---

## Examples

**Example 1**

**Input**

```text
5
0 0 0
1 1 1
1 1 0
0 1 0
0 1 1
```

**Output**

```text
Water filling time
Not now
Not now
Water filling time
Not now
```

**Explanation**

**Testcase 1:** The inputs are $0, 0, 0$. So all three bottles are empty. Since at least two bottles are empty, it is "Water filling time".

**Testcase 2:** The inputs are $1, 1, 1$. So all three bottles are full. Since it is not the case that at least two bottles are empty, it is "Not now".

**Testcase 3:** The inputs are $1, 1, 0$. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".

**Testcase 4:** The inputs are $0, 1, 0$. So two bottles are empty. Since at least two bottles are empty, it is "Water filling time".

**Testcase 5:** The inputs are $0, 1, 1$. So only one bottle is empty. Since it is not the case that at least two bottles are empty, it is "Not now".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0 0 0
```

**Output for this case**

```text
Water filling time
```



#### Test case 2

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
Not now
```



#### Test case 3

**Input for this case**

```text
1 1 0
```

**Output for this case**

```text
Not now
```



#### Test case 4

**Input for this case**

```text
0 1 0
```

**Output for this case**

```text
Water filling time
```



#### Test case 5

**Input for this case**

```text
0 1 1
```

**Output for this case**

```text
Not now
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WATERFILLING)

[Contest: Division 1](https://www.codechef.com/START92A/problems/WATERFILLING)

[Contest: Division 2](https://www.codechef.com/START92B/problems/WATERFILLING)

[Contest: Division 3](https://www.codechef.com/START92C/problems/WATERFILLING)

[Contest: Division 4](https://www.codechef.com/START92D/problems/WATERFILLING)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

541

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has three water bottles, and will fill them up if at least two are empty.

Given the state of the three bottles B_1, B_2, B_3 (each being either 0 or 1 denoting full/empty), decide whether Chef will fill them up.

#
[](#explanation-5)EXPLANATION:

Check whether at least two of the bottles are empty.

This can be done using casework (check each pair of bottles); or simply check whether B_1+B_2+B_3 \leq 1.

After this check, print the answer appropriately.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    b1, b2, b3 = map(int, input().split())
    print('Water filling time' if b1+b2+b3 <= 1 else 'Not now')
``

</details>
