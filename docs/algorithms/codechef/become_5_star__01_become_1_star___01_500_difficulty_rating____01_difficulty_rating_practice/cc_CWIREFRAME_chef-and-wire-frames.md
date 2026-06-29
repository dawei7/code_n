# Chef and Wire Frames

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CWIREFRAME |
| Difficulty Rating | 383 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CWIREFRAME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWIREFRAME) |

---

## Problem Statement

Chef has a rectangular plate of length  $N cm$  and width $M cm$. He wants to make a wireframe around the plate. The wireframe costs $X$ rupees per cm.

Determine the cost Chef needs to incur to buy the wireframe.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing three space-separated integers $N,M,$ and $X$ — the length of the plate, width of the plate, and the cost of frame per cm.

---

## Output Format

For each test case, output in a single line, the price Chef needs to pay for the wireframe.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,M,X \leq 1000 $

---

## Examples

**Example 1**

**Input**

```text
3
10 10 10
23 3 12
1000 1000 1000
```

**Output**

```text
400
624
4000000
```

**Explanation**

**Test case $1$:** The total length of the frame is $2\cdot 10 + 2\cdot 10 = 40$ cms. Since the cost is $10$ per cm, the total cost would be $10 \cdot 40 = 400$.

**Test case $2$:** The total length of the frame is $2\cdot 23 + 2\cdot 3 = 52$ cms. Since the cost is $12$ per cm, the total cost would be $52 \cdot 12 = 624$.

**Test case $3$:** The total length of the frame is $2\cdot 1000 + 2\cdot 1000 = 4000$ cms. Since the cost is $1000$ per cm, the total cost would be $4000 \cdot 1000 = 4000000$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 10 10
```

**Output for this case**

```text
400
```



#### Test case 2

**Input for this case**

```text
23 3 12
```

**Output for this case**

```text
624
```



#### Test case 3

**Input for this case**

```text
1000 1000 1000
```

**Output for this case**

```text
4000000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CWIREFRAME)

[Contest: Division 1](https://www.codechef.com/SEP221A/problems/CWIREFRAME)

[Contest: Division 2](https://www.codechef.com/SEP221B/problems/CWIREFRAME)

[Contest: Division 3](https://www.codechef.com/SEP221C/problems/CWIREFRAME)

[Contest: Division 4](https://www.codechef.com/SEP221D/problems/CWIREFRAME)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Preparer:*** [Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

383

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a rectangular plate of length N\ cm and width M\ cm. He wants to make a wireframe around the plate that costs X rupees per cm. What will the total cost be?

#
[](#explanation-5)EXPLANATION:

The perimeter of the plate is 2\cdot(N+M) \ cm. Each centimeter of this costs rupees X, so the final cost is X\cdot 2\cdot(N+M) rupees.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m, x = map(int, input().split())
    print(2*x*(n+m))
``

</details>
