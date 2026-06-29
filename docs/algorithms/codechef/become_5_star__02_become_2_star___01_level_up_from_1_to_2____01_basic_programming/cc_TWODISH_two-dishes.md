# Two Dishes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWODISH |
| Difficulty Rating | 1140 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [TWODISH](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TWODISH) |

---

## Problem Statement

Chef will have $N$ guests in his house today. He wants to serve at least one dish to each of the $N$ guests. Chef can make two types of dishes. He needs one fruit and one vegetable to make the first type of dish and one vegetable and one fish to make the second type of dish. Now Chef has $A$ fruits, $B$ vegetables, and $C$ fishes in his house. Can he prepare at least $N$ dishes in total?

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, four integers $N, A, B, C$.

---

## Output Format

For each test case, print "YES" if Chef can prepare at least $N$ dishes, otherwise print "NO". Print the output without quotes.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, A, B, C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
2 1 2 1
3 2 2 2
4 2 6 3
3 1 3 1
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$**: Chef prepares one dish of the first type using one fruit and one vegetable and another dish of the second type using one vegetable and one fish.

**Test case $2$**: Chef prepares two dishes of the first type using two fruit and two vegetable. Now all the vegetables are exhausted, hence he can't prepare any other dishes.

**Test case $3$**: Chef can prepare a total of $5$ dishes, two dishes of the first type and three dishes of the second type.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1 2 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 2 2 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 2 6 3
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3 1 3 1
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

[Contest - Division 3](https://www.codechef.com/LTIME100C/problems/TWODISH)

[Contest - Division 2](https://www.codechef.com/LTIME100B/problems/TWODISH)

[Contest - Division 1](https://www.codechef.com/LTIME100A/problems/TWODISH)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

You have A fruits, B vegetables and C fishes. You can make a single meal using 1 fruit and 1 vegetable or using 1 vegetable and 1 fish.

Determine if you can make at least N meals.

#
[](#explanation-4)EXPLANATION:

The number of meals that can be prepared can not exceed B, since each meal requires 1 vegetable (and there are only B vegetables).

Also, the number of meals can not exceed A+C, since each meal also requires either a fruit or a fish (and there are a total of A+C fruits and fishes).

Therefore, the number of meals that can be prepared is clearly the lower of the two constraints \implies \min (B, A+C).

Then, output `YES` if the value is \ge N and `NO` otherwise.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51617926).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
