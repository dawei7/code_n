# Chef in Vaccination Queue

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VACCINQ |
| Difficulty Rating | 1016 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [VACCINQ](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/VACCINQ) |

---

## Problem Statement

There are $N$ people in the vaccination queue, Chef is standing on the $P^{th}$ position from the front of the queue. It takes $X$ minutes to vaccinate a child and $Y$ minutes to vaccinate an elderly person. Assume Chef is an elderly person.

You are given a binary array $A_1, A_2, \dots, A_N$ of length $N$, where $A_i = 1$ denotes there is an elderly person standing on the $i^{th}$ position of the queue, $A_i = 0$ denotes there is a child standing on the $i^{th}$ position of the queue. You are also given the three integers $P, X, Y$. Find the number of minutes after which Chef's vaccination will be completed.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains four space-separated integers $N, P, X, Y$.
- The second line of each test case contains $N$ space-separated integer $A_1, A_2,\dots, A_N$.

---

## Output Format

For each testcase, output in a single line the number of minutes after which Chef's vaccination will be completed.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq P \leq N$
- $1 \leq X, Y \leq 10$
- $0 \leq A_i \leq 1$
- $A_P = 1$

---

## Examples

**Example 1**

**Input**

```text
3
4 2 3 2
0 1 0 1
3 1 2 3
1 0 1
3 3 2 2
1 1 1
```

**Output**

```text
5
3
6
```

**Explanation**

**Test case $1$**: The person standing at the front of the queue is a child and the next person is Chef. So it takes a total of $3 + 2 = 5$ minutes to complete Chef's vaccination.

**Test case $2$**: Chef is standing at the front of the queue. So his vaccination is completed after $3$ minutes.

**Test case $3$**: Chef is standing at the rear of the queue. So it takes a total of $2 + 2 + 2 = 6$ minutes to complete Chef's vaccination.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2 3 2
0 1 0 1
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
3 1 2 3
1 0 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
3 3 2 2
1 1 1
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START13C/problems/VACCINQ)

[Contest - Division 2](https://www.codechef.com/START13B/problems/VACCINQ)

[Contest - Division 1](https://www.codechef.com/START13A/problems/VACCINQ)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Chef is standing for the vaccine in a queue, at the P^{th} position from the front of the line. Given the status of all people in the queue (child/elderly person), and that it takes X and Y minutes to vaccinate a child and elder, respectively.

Determine the number of minutes until Chef finishes getting his vaccination.

#
[](#explanation-4)EXPLANATION:

Since Chef is vaccinated only after the P-1 people in front of him are vaccinated, the total time for the completion of Chef’s vaccination is equal to the time it takes to vaccinate the first P people in the queue.

Therefore, for each person i\space(1\le i\le P) from the front of the queue, add the time it takes to vaccinate him/her (X for a child, Y for an adult) to get the final answer.

#
[](#time-complexity-5)TIME COMPLEXITY:

Since we iterate over the first P people in the queue (adding their vaccination time to the answer), the time complexity is

O(P)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51712264).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
