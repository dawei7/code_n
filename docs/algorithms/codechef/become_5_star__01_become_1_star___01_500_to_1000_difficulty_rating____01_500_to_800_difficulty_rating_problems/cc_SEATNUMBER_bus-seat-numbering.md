# Bus  Seat Numbering

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SEATNUMBER |
| Difficulty Rating | 613 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SEATNUMBER](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SEATNUMBER) |

---

## Problem Statement

There is a bus with 30 seats. The seats are numbered from 1 to 30, and the numbering is as depicted in this image.

As can be seen in the image, the bus is divided into two decks - The Lower deck, and the Upper deck, with 15 seats each. And some of the seats come as Single and some as Double. For example, Seats 1 and 2 are Double, whereas Seat 11 is a Single.

You will be given a Seat number, and your job is to classify it as one of these 4 types:
- Lower Single
- Lower Double
- Upper Single
- Upper Double

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input which contains a single integers $N$ — the seat number.

---

## Output Format

For each test case, output on a new line, the type of seat.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 30$

---

## Examples

**Example 1**

**Input**

```text
5
6
28
16
13
10
```

**Output**

```text
Lower Double
Upper Single
Upper Double
Lower Single
Lower Double
```

**Explanation**

**Testcase 1:** The seat number 6 is in the Lower deck, and it is a Double. Hence the output is "Lower Double".

**Testcase 2:** The seat number 28 is in the Upper deck, and it is a Single. Hence the output is "Upper Single".

**Testcase 3:** The seat number 16 is in the Upper deck, and it is a Double. Hence the output is "Upper Double".

**Testcase 4:** The seat number 13 is in the Lower deck, and it is a Single. Hence the output is "Lower Single".

**Testcase 5:** The seat number 10 is in the Lower deck, and it is a Double. Hence the output is "Lower Double".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
```

**Output for this case**

```text
Lower Double
```



#### Test case 2

**Input for this case**

```text
28
```

**Output for this case**

```text
Upper Single
```



#### Test case 3

**Input for this case**

```text
16
```

**Output for this case**

```text
Upper Double
```



#### Test case 4

**Input for this case**

```text
13
```

**Output for this case**

```text
Lower Single
```



#### Test case 5

**Input for this case**

```text
10
```

**Output for this case**

```text
Lower Double
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SEATNUMBER)

[Contest: Division 1](https://www.codechef.com/START91A/problems/SEATNUMBER)

[Contest: Division 2](https://www.codechef.com/START91B/problems/SEATNUMBER)

[Contest: Division 3](https://www.codechef.com/START91C/problems/SEATNUMBER)

[Contest: Division 4](https://www.codechef.com/START91D/problems/SEATNUMBER)

***Tester and Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

613

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the seat numbering plan of a bus and specific seat in it, output whether the set is in the upper or lower deck, and a single or double seat.

#
[](#explanation-5)EXPLANATION:

Looking at the seat plan, we can see that for seat number N:

- If 1 \leq N \leq 10, the seat is Lower Double

- If 11 \leq N \leq 15, the set is Lower Single

- If 16 \leq N \leq 25, the seat is Upper Double

- If 26 \leq N \leq 30, the seat is Upper Single

Check which one of the four conditions N satisfies, and output the appropriate type.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for test in range(int(input())):
    n = int(input())
    if n <= 10: print('Lower Double')
    elif n <= 15: print('Lower Single')
    elif n <= 25: print('Upper Double')
    else: print('Upper Single')
``

</details>
