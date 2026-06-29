# Maximise the Tastiness

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXTASTE |
| Difficulty Rating | 627 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MAXTASTE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MAXTASTE) |

---

## Problem Statement

Chef is making a dish that consists of exactly two ingredients. He has four ingredients $A, B, C$ and $D$ with tastiness $a, b, c,$ and $d$ respectively. He can use either $A$ or $B$ as the first ingredient and either $C$ or $D$ as the second ingredient.

The tastiness of a dish is the sum of tastiness of its ingredients. Find the **maximum** possible tastiness of the dish that the chef can prepare.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains four space-separated integers $a, b, c,$ and $d$ — the tastiness of the four ingredients.

---

## Output Format

For each test case, output on a new line the maximum possible tastiness of the dish that chef can prepare.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq a, b, c, d \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
3 5 6 2
16 15 5 4
```

**Output**

```text
11
21
```

**Explanation**

**Test case $1$:** Chef can prepare a dish with ingredients $B$ and $C$ with a tastiness of $5+6=11$.

**Test case $2$:** Chef can prepare a dish with ingredients $A$ and $C$ with a tastiness of $16+5=21$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 5 6 2
```

**Output for this case**

```text
11
```



#### Test case 2

**Input for this case**

```text
16 15 5 4
```

**Output for this case**

```text
21
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START49/)

[Practice](https://www.codechef.com/problems/MAXTASTE)

**Setter:** [inov_360 ](https://www.codechef.com/users/inov_360)

**Testers:** [iceknight1093 ](https://www.codechef.com/users/iceknight1093), [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

627

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has four ingredients A, B, C and D with tastiness a, b, c, and d respectively. He can use either A or B as the first ingredient and either C or D as the second ingredient. The tastiness of a dish is the sum of tastiness of its ingredients. Find the **maximum** possible tastiness of the dish that the chef can prepare.

#
[](#explanation-5)EXPLANATION:

Given, the testiness of the dish is the sum of the testiness of the ingredients. Also, out of 4 ingredients only two are used at a time. That is either A or B is used  as the first ingredient and C or D is used as the second ingredient.

Thus the testiness of the dish is: Testiness of (A or B) + Testiness of (C or D).

Our objective is to find the maximum testiness, thus our desired output is:

Max(A or B) + Max (C or D).

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
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;

	    cout<<max(a,b)+max(c,d)<<"\n";
	}

``

</details>
