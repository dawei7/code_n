# Roller Coaster

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINHEIGHT |
| Difficulty Rating | 285 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MINHEIGHT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MINHEIGHT) |

---

## Problem Statement

Chef's son wants to go on a roller coaster ride. The height of Chef's son is $X$ inches while the **minimum** height required to go on the ride is $H$ inches. Determine whether he can go on the ride or not.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $X$ and $H$ - the height of Chef's son and the minimum height required for the ride respectively.

---

## Output Format

For each test case, output in a single line, `YES` if Chef's son can go on the ride. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical)

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, H \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
15 20
50 48
32 32
38 39
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test case 1:** Chef's son can not go on the ride as his height $\lt$ the minimum required height.

**Test case 2:** Chef's son can go on the ride as his height $\ge$ the minimum required height.

**Test case 3:** Chef's son can go on the ride as his height $\ge$ the minimum required height.

**Test case 4:** Chef's son can not go on the ride as his height $\lt$ the minimum required height.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15 20
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
50 48
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
32 32
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
38 39
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

[Contest Division 1](https://www.codechef.com/START37A/problems/MINHEIGHT)

[Contest Division 2](https://www.codechef.com/START37B/problems/MINHEIGHT)

[Contest Division 3](https://www.codechef.com/START37C/problems/MINHEIGHT)

[Contest Division 4](https://www.codechef.com/START37D/problems/MINHEIGHT)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

285

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s son wants to go on a roller coaster ride. The height of Chef’s son is X inches while the **minimum** height required to go on the ride is H inches. Determine whether he can go on the ride or not.

#
[](#explanation-5)EXPLANATION:

Here we are given the minimum height to go on the ride is H inches. Thus we just need to check if Chef’s son has a height greater than or equal to H inches.

Thus if X is greater than or equal to H then he can go on a ride else he can’t.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/4Rbu)

[Setter’s Solution](http://p.ip.fi/zi7O)

[Tester1’s Solution](http://p.ip.fi/OlIx)

[Tester2’s Solution](http://p.ip.fi/oG01)

</details>
