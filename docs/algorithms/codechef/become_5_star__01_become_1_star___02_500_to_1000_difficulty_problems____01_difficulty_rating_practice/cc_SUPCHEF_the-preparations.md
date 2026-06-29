# The Preparations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUPCHEF |
| Difficulty Rating | 823 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [SUPCHEF](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/SUPCHEF) |

---

## Problem Statement

Chef has an exam which will start exactly $M$ minutes from now. However, instead of preparing for his exam, Chef started watching Season-$1$ of Superchef. Season-$1$ has $N$ episodes, and the duration of **each** episode is $K$ minutes.

Will Chef be able to finish watching Season-$1$ **strictly before** the exam starts?

$\textbf{Note:}$ Please read the explanations of the sample test cases carefully.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases. $T$ test cases then follow.
- The first and only line of each test case contains $3$ space separated integers $M$, $N$ and $K$.

---

## Output Format

For each test case, output on one line YES if it is possible to finish Season-1 **strictly before** the exam starts, or NO if it is not possible to do so.

Output is case insensitive, which means that "yes", "Yes", "YEs", "no", "nO" - all such strings will be acceptable.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq M \leq 10^9$
- $1 \leq N, K \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
10 1 10
25 2 10
15 2 10
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Test Case $1$:** The duration of the only episode is $10$ minutes, and the exam starts exactly after $10$ minutes. So, Chef will **not** be able to finish watching Season-$1$ strictly before the exam starts.

**Test Case $2$:** There are two episodes in Season-$1$, each of duration $10$ minutes. Therefore, Chef will require $10 + 10 = 20$ minutes to finish watching Season-$1$. As the exam starts after $25$ minutes, Chef will be able to finish watching Season-$1$ strictly before the exam starts.

**Test Case $3$:** There are two episodes in Season-$1$, each of duration $10$ minutes. Therefore, Chef will require $10 + 10 = 20$ minutes to finish watchin Season-$1$. As the exam starts after $15$ minutes, Chef will **not** be able to finish watching Season-$1$ strictly before the exam starts.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 1 10
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
25 2 10
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
15 2 10
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

[Contest - Division 3](https://www.codechef.com/START13C/problems/SUPCHEF)

[Contest - Division 2](https://www.codechef.com/START13B/problems/SUPCHEF)

[Contest - Division 1](https://www.codechef.com/START13A/problems/SUPCHEF)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Chef’s exam will start M minutes from now. He wishes to watch a series of N episodes, each K minutes long.

Determine if it is possible for him to watch the entire series **strictly before** his exam begins.

#
[](#explanation-4)EXPLANATION:

Since each series is K minutes long, chef will require a total of N*K minutes to watch all N episodes of the series.

Therefore, it is only possible to watch the entire series before his exam begins if, the total time to watch the series is less than the time remaining for the commencement of the exam \implies N*K < M.

Output `YES` if the above equality holds, and `NO` otherwise.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51712376).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
