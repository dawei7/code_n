# Chef in his Office

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OFFICE |
| Difficulty Rating | 532 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [OFFICE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/OFFICE) |

---

## Problem Statement

Recently Chef joined a new company. In this company, the employees have to work for $X$ hours each day from Monday to Thursday. Also, in this company, Friday is called Chill Day — employees only have to work for $Y$ hours $(Y \lt X)$ on Friday. Saturdays and Sundays are holidays.

Determine the total number of working hours in one week.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the number of working hours on each day from Monday to Thursday and the number of working hours on Friday respectively.

---

## Output Format

For each test case, output the total number of working hours in one week.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq X \leq 12$
- $1 \le Y \lt X$

---

## Examples

**Example 1**

**Input**

```text
3
10 5
12 2
8 7
```

**Output**

```text
45
50
39
```

**Explanation**

**Test case $1$:** The total number of working hours in a week are: $10 \texttt{(Monday)} + 10 \texttt{(Tuesday)} + 10 \texttt{(Wednesday)} + 10 \texttt{(Thursday)} + 5 \texttt{(Friday)} = 45$

**Test Case 2:** The total number of working hours in a week are: $12 \texttt{(Monday)} + 12 \texttt{(Tuesday)} + 12 \texttt{(Wednesday)} + 12 \texttt{(Thursday)} + 2 \texttt{(Friday)} = 50$

**Test Case 3:** The total number of working hours in a week are: $8 \texttt{(Monday)} + 8 \texttt{(Tuesday)} + 8 \texttt{(Wednesday)} + 8 \texttt{(Thursday)} + 7 \texttt{(Friday)} = 39$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 5
```

**Output for this case**

```text
45
```



#### Test case 2

**Input for this case**

```text
12 2
```

**Output for this case**

```text
50
```



#### Test case 3

**Input for this case**

```text
8 7
```

**Output for this case**

```text
39
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY222/)

[Practice](https://www.codechef.com/problems/OFFICE)

**Setter:** [jeevan_adm](https://www.codechef.com/users/jeevan_adm)

**Testers:** [tejas10p](https://www.codechef.com/users/tejas10p), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

532

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the working hours from Monday to Thursday as X hours per day and that of Friday being Y hours, our objective is to determine the total number of working hours in one week.

#
[](#explanation-5)EXPLANATION:

Total number of working hours from Monday - Thursday[4 days] = 4 \times X. And the working hours on a Friday is Y.

Thus the total number working hours in one week is - (4 \times X) + Y

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``int t;
	cin>>t;
	while(t--)
	{
	    int x,y;
	    cin>>x>>y;
	    cout<<4*x+y<<"\n";
	}
``

</details>
