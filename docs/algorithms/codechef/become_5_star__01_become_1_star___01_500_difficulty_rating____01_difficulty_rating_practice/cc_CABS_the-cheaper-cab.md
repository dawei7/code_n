# The Cheaper Cab

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CABS |
| Difficulty Rating | 399 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CABS](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CABS) |

---

## Problem Statement

Chef has to travel to another place. For this, he can avail any one of two cab services.
- The first cab service charges $X$ rupees.
- The second cab service charges $Y$ rupees.

Chef wants to spend the **minimum** amount of money. Which cab service should Chef take?

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $Y$ - the prices of first and second cab services respectively.

---

## Output Format

For each test case, output `FIRST` if the first cab service is cheaper, output `SECOND` if the second cab service is cheaper, output `ANY` if both cab services have the same price.

You may print each character of `FIRST`, `SECOND` and `ANY` in uppercase or lowercase (for example, `any`, `aNy`, `Any` will be considered identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
30 65
42 42
90 50
```

**Output**

```text
FIRST
ANY
SECOND
```

**Explanation**

**Test case $1$:** The first cab service is cheaper than the second cab service.

**Test case $2$:** Both the cab services have the same price.

**Test case $3$:** The second cab service is cheaper than the first cab service.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
30 65
```

**Output for this case**

```text
FIRST
```



#### Test case 2

**Input for this case**

```text
42 42
```

**Output for this case**

```text
ANY
```



#### Test case 3

**Input for this case**

```text
90 50
```

**Output for this case**

```text
SECOND
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START33A/problems/CABS)

[Contest Division 2](https://www.codechef.com/START33B/problems/CABS)

[Contest Division 3](https://www.codechef.com/START33C/problems/CABS)

[Contest Division 4](https://www.codechef.com/START33D/problems/CABS)

Setter: [Jeevan Mayur Koli](https://www.codechef.com/users/mayurkoli128)

Testers: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef  has to travel to another place. For this, he can avail any one of two cab services.

- The first cab service charges X rupees.

- The second cab service charges Y rupees.

Chef wants to spend the minimum amount of money. Which cab service should Chef take?

#
[](#explanation-5)EXPLANATION:

For each test case, we have to compare which of the cabs, first or the second incurs lesser charge.

This can be done by comparing the first cab and the second cab charges. If the first cab costs less we have to print **FIRST**, otherwise if the second cab costs less we have to print **SECOND** and in the case where both charge equally we have to print **ANY**.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/6wYR)

[Setter’s Solution](http://p.ip.fi/7itX)

[Tester 1’s Solution](http://p.ip.fi/5Zn6)

[Tester 2’s Solution](http://p.ip.fi/EPBI)

</details>
