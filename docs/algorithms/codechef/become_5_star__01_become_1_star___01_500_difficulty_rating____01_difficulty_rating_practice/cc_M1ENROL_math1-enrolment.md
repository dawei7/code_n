# MATH1 Enrolment

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | M1ENROL |
| Difficulty Rating | 349 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [M1ENROL](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/M1ENROL) |

---

## Problem Statement

For the upcoming semester, the admins of your university decided to keep a total of $X$ seats for the `MATH-1` course. A student interest survey was conducted by the admins and it was found that $Y$ students were interested in taking up the `MATH-1` course.

Find the **minimum** number of **extra** seats that the admins need to add into the `MATH-1` course to make sure that every student who is interested in taking the course would be able to do so.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two-space separated integers on a single line, $X$ and $Y$ — the current number of seats up for enrolment and the number of students interested in taking up the course in the upcoming semester, respectively.

---

## Output Format

For each test case, output on a new line the **minimum** number of seats required to be added.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
1 1
12 34
50 49
49 50
```

**Output**

```text
0
22
0
1
```

**Explanation**

**Test case $1$:** Exactly $1$ seat is available for enrolment, and exactly $1$ student is interested in taking up the course, hence addition of more seats is not required.

**Test case $2$:** $12$ seats are available for enrolment but $34$ students are interested in taking up the course, hence the admins would have to add $34-12=22$ more seats to make sure that every student interested in the course gets a seat.

**Test case $3$:** $50$ seats are available for enrolment and $49$ students are interested in taking up the course, hence addition of more seats is not required.

**Test case $4$:** $49$ seats are available for enrolment, but $50$ students are interested in taking up the course, hence the admins would have to add $50-49=1$ more seat to make sure that every student interested in the course gets a seat.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
12 34
```

**Output for this case**

```text
22
```



#### Test case 3

**Input for this case**

```text
50 49
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
49 50
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START46A/problems/M1ENROL)

[Contest Division 2](https://www.codechef.com/START46B/problems/M1ENROL)

[Contest Division 3](https://www.codechef.com/START46C/problems/M1ENROL)

[Contest Division 4](https://www.codechef.com/START46D/problems/M1ENROL)

[Practice](https://www.codechef.com/problems/M1ENROL)

**Setter:** [Anish Ashish Kasegaonkar](https://www.codechef.com/users/anish_ak)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Anish Ashish Kasegaonkar](https://www.codechef.com/users/anish_ak)

#
[](#difficulty-2)DIFFICULTY

349

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

There are a total of X seats available for enrolment for `MATH-1`, and there are Y students who are interested in taking up the course. You have to output the minimum number of seats that need to be added to make sure that every interested student gets a seat.

#
[](#explanation-5)EXPLANATION

The solution can be divided into two cases:

-
X\geq Y: In this case, there are more seats available than there are interested students (in the case of X=Y, there are exactly as many seats), hence no more seats need to be added. The answer for this case would be 0.

-
X<Y: In this case, there are lesser seats available than there are interested students. Hence we would need to add some more seats, and this number is given by the current number of seats subtracted from the required number of seats (number of interested students), i.e. the answer for this case would be Y-X.

This will simplify to simply printing max(0, Y-X).

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION

Editorialist's Solution
``// Anish Kasegaonkar
#include <bits/stdc++.h>
using namespace std;

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        int x, y;
        cin >> x >> y;
        cout << max(0, y - x) << '\n';
    }
    return 0;
}
``

</details>
