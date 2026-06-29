# Water Requirement

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WATERREQ |
| Difficulty Rating | 351 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [WATERREQ](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/WATERREQ) |

---

## Problem Statement

Finally, after purchasing a water cooler during the April long challenge, Chef noticed that his water cooler requires $2$ liters of water to cool for **one** hour.

How much water (in liters) would be required by the cooler to cool for $N$ hours?

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$, as described in the problem statement.

---

## Output Format

For each test case, output the number of liters of water required by the water cooler to cool for $N$ hours.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
2
1
2
```

**Output**

```text
2
4
```

**Explanation**

**Test case $1$**: As mentioned in the problem statement, $2$ liters of water is required by the water cooler to cool for $1$ hour.

**Test case $2$**: $4$ liters of water is required by the water cooler to cool for $2$ hours.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START35A/problems/WATERREQ)

[Contest Division 2](https://www.codechef.com/START35B/problems/WATERREQ)

[Contest Division 3](https://www.codechef.com/START35C/problems/WATERREQ)

[Contest Division 4](https://www.codechef.com/START35D/problems/WATERREQ)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [Felipe Mota](https://www.codechef.com/users/fmota), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

351

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Finally, after purchasing a water cooler during the April long challenge, Chef noticed that his water cooler requires 2 liters of water to cool for **one** hour.

How much water (in liters) would be required by the cooler to cool for N hours?

#
[](#explanation-5)EXPLANATION:

Since it is given that it requires 2 litres to cool for 1 hour, therefore we can say that for N hours it would take 2N litres of water.

Thus,

answer = 2 \times N

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/VCPS)

[Setter’s Solution](http://p.ip.fi/DQPd)

[Tester1’s Solution](http://p.ip.fi/Et9-)

[Tester2’s Solution](http://p.ip.fi/rwc0)

</details>
