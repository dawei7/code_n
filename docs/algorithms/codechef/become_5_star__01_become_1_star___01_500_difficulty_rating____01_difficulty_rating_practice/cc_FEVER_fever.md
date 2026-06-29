# Fever

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FEVER |
| Difficulty Rating | 348 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [FEVER](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/FEVER) |

---

## Problem Statement

Chef is not feeling well today. He measured his body temperature using a thermometer and it came out to be $X$ °F.

A person is said to have fever if his body temperature is **strictly greater** than $98$ °F.

Determine if Chef has fever or not.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ - the body temperature of Chef in °F.

---

## Output Format

For each test case, output `YES` if Chef has fever. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \le T \le 10$
- $94 \le X \le 103$

---

## Examples

**Example 1**

**Input**

```text
3
98
100
96
```

**Output**

```text
NO
YES
NO
```

**Explanation**

**Test Case 1**: Since $X = 98$ is not greater than $98$, Chef does not have fever.

**Test Case 2**: Since $X = 100$ is greater than $98$, Chef has fever.

**Test Case 3**: Since $X = 96$ is not greater than $98$, Chef does not have fever.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
98
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
100
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
96
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

[Practice](https://www.codechef.com/problems/FEVER)

[Contest: Division 1](https://www.codechef.com/START55A/problems/FEVER)

[Contest: Division 2](https://www.codechef.com/START55B/problems/FEVER)

[Contest: Division 3](https://www.codechef.com/START55C/problems/FEVER)

[Contest: Division 4](https://www.codechef.com/START55D/problems/FEVER)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/JeevanJyot)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

348

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s temperature is X °F. A person has a fever if their temperature is strictly more than 98 °F. Does Chef have a fever?

#
[](#explanation-5)EXPLANATION:

Do what the problem states: print “Yes” if X \gt 98 and “No” otherwise.

Checking if X \gt 98 can be done with the help of an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    print('yes' if int(input()) > 98 else 'no')
``

</details>
