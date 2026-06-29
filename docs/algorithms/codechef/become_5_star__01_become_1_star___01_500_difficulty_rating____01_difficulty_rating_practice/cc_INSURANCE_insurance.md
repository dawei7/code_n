# Insurance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INSURANCE |
| Difficulty Rating | 475 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INSURANCE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INSURANCE) |

---

## Problem Statement

Chef bought car insurance. The policy of the insurance is:

- The **maximum** rebatable amount for any damage is Rs $X$ lakhs.
- If the amount required for repairing the damage is $\leq X$ lakhs, that amount is rebated in full.

Chef's car meets an accident and required Rs $Y$ lakhs for repairing.

Determine the amount that will be rebated by the insurance company.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.

---

## Output Format

For each test case, output the amount (in lakhs) that will be rebated by the insurance company.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 30$

---

## Examples

**Example 1**

**Input**

```text
4
5 3
5 8
4 4
15 12
```

**Output**

```text
3
5
4
12
```

**Explanation**

**Test case $1$:** The damages require only Rs $3$ lakh which is below the upper cap, so the entire Rs $3$ lakh will be rebated.

**Test case $2$:** The damages require Rs $8$ lakh which is above the upper cap, so only Rs $5$ lakh will be rebated.

**Test case $3$:** The damages require only Rs $4$ lakh which is equal to the upper cap, so the whole Rs $4$ lakh will be rebated.

**Test case $4$:** The damages require Rs $15$ lakh which is above the upper cap, so only Rs $12$ lakh will be rebated.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5 8
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
4 4
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
15 12
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/JULY222/)

[Practice](https://www.codechef.com/problems/INSURANCE)

**Setter:** [abhi_inav](https://www.codechef.com/users/abhi_inav)

**Testers:** [tejas10p](https://www.codechef.com/users/tejas10p), [rivalq](https://www.codechef.com/users/rivalq)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

475

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the maximum rebatable amount X and the amount for repairing as Y, our objective is to determine the amount that will be rebated by the insurance company.

#
[](#explanation-5)EXPLANATION:

There are only two cases :

a. The amount for repairing , Y \le X. Then the amount rebated by the insurance company will be Y.

b. The amount for repairing , Y > X. Then the amount rebated by the insurance company will be X.

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
	    cin >> x >> y;
	    if(y <= x) cout << y << endl;
	    else cout << x << endl;
	}
``

</details>
