# Vaccine Dates 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | VDATES |
| Difficulty Rating | 938 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [VDATES](https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/VDATES) |

---

## Problem Statement

Chef has taken his first dose of vaccine $D$ days ago. He may take the second dose no less than $L$ days and no more than $R$ days since his first dose.

Determine if Chef is too early, too late, or in the correct range for taking his second dose.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers $D, L, R$.

---

## Output Format

For each test case, print a single line containing one string - "Too Early" (without quotes) if it's too early to take the vaccine, "Too Late" (without quotes) if it's too late to take the vaccine, "Take second dose now" (without quotes) if it's the correct time to take the vaccine.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq D \leq 10^9$
- $1 \leq L \leq R \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
10 8 12 
14 2 10
4444 5555 6666 
8 8 12
```

**Output**

```text
Take second dose now
Too Late
Too Early
Take second dose now
```

**Explanation**

**Test case $1$:** The second dose needs to be taken within $8$ to $12$ days and since the Day $10$ lies in this range, we can take the second dose now.

**Test case $2$:** The second dose needs to be taken within $2$ to $10$ days since Day $14$ lies after this range, it is too late now.

**Test case $3$:** The second dose needs to be taken within $5555$ to $6666$ days and since the Day $4444$ lies prior to this range, it is too early now.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 8 12
```

**Output for this case**

```text
Take second dose now
```



#### Test case 2

**Input for this case**

```text
14 2 10
```

**Output for this case**

```text
Too Late
```



#### Test case 3

**Input for this case**

```text
4444 5555 6666
```

**Output for this case**

```text
Too Early
```



#### Test case 4

**Input for this case**

```text
8 8 12
```

**Output for this case**

```text
Take second dose now
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/LTIME100C/problems/VDATES)

[Contest - Division 2](https://www.codechef.com/LTIME100B/problems/VDATES)

[Contest - Division 1](https://www.codechef.com/LTIME100A/problems/VDATES)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Chef has taken his first vaccine D days ago. He may take the booster dose no less than L days and no more than R days since his first dose.

Determine if chef can take the vaccine or not.

#
[](#explanation-4)EXPLANATION:

Do just as the problem says.

- If D < L, then he is `too early`

- else if R < D, then he is `too late`

- else (the only remaining case is L\le D\le R), he can `take the second dose now`

#
[](#time-complexity-5)TIME COMPLEXITY:

O(1)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51617981).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
