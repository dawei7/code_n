# Sleep deprivation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLEEP |
| Difficulty Rating | 348 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [SLEEP](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/SLEEP) |

---

## Problem Statement

A person is said to be sleep deprived if he slept **strictly less than** $7$ hours in a day.

Chef was only able to sleep $X$ hours yesterday. Determine if he is sleep deprived or not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ — the number of hours Chef slept.

---

## Output Format

For each test case, output `YES` if Chef is sleep-deprived. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 20$
- $1 \le X \le 15$

---

## Examples

**Example 1**

**Input**

```text
3
4
7
10
```

**Output**

```text
YES
NO
NO
```

**Explanation**

**Test Case 1:** Since $4 \lt 7$, Chef is sleep deprived.

**Test Case 2:** Since $7 \ge 7$, Chef is not sleep deprived.

**Test Case 3:** Since $10 \ge 7$, Chef is not sleep deprived.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
7
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
10
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

[Practice](https://www.codechef.com/problems/SLEEP)

[Contest: Division 1](https://www.codechef.com/LTIME112A/problems/SLEEP)

[Contest: Division 2](https://www.codechef.com/LTIME112B/problems/SLEEP)

[Contest: Division 3](https://www.codechef.com/LTIME112C/problems/SLEEP)

[Contest: Division 4](https://www.codechef.com/LTIME112D/problems/SLEEP)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Tester:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

348

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A person is said to be sleep-deprived if he sleeps strictly less than 7 hours in a day.

Given that someone sleeps for X hours, is he sleep-deprived?

#
[](#explanation-5)EXPLANATION:

Simply implement what the statement says using an if condition:

- If X \lt 7, then the person is sleep-deprived, so print “Yes”

- Otherwise, print “No”

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('Yes' if int(input()) < 7 else 'No')
``

</details>
