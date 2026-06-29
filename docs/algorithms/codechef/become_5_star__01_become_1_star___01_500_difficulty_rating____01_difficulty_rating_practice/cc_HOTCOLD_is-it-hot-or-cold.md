# Is it hot or cold

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HOTCOLD |
| Difficulty Rating | 410 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [HOTCOLD](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HOTCOLD) |

---

## Problem Statement

Chef considers the climate `HOT` if the temperature is **above** $20$, otherwise he considers it `COLD`. You are given the temperature $C$, find whether the climate is `HOT` or `COLD`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains a single integer, the temperature $C$.

---

## Output Format

For each test case, print on a new line whether the climate is `HOT` or `COLD`.

You may print each character of the string in either uppercase or lowercase (for example, the strings `hOt`, `hot`, `Hot`, and `HOT` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 50$
- $0 \leq C \leq 40$

---

## Examples

**Example 1**

**Input**

```text
2
21
16
```

**Output**

```text
HOT
COLD
```

**Explanation**

**Test case $1$:** The temperature is $21$, which is more than $20$. So, Chef considers the climate `HOT`.

**Test case $2$:** The temperature is $16$, which is not more than $20$. So, Chef considers the climate `COLD`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
21
```

**Output for this case**

```text
HOT
```



#### Test case 2

**Input for this case**

```text
16
```

**Output for this case**

```text
COLD
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START49/)

[Practice](https://www.codechef.com/problems/HOTCOLD)

**Setter:** [inov_360 ](https://www.codechef.com/users/inov_360)

**Testers:** [iceknight1093 ](https://www.codechef.com/users/iceknight1093), [jeevanjyot](https://www.codechef.com/users/jeevanjyot)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

410

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef considers the climate HOT if the temperature is above 20, otherwise he considers it COLD. You are given the temperature C, find whether the climate is HOT or COLD.

#
[](#explanation-5)EXPLANATION:

The objective is to input a value C and compare it with 20.

If its below 20 output COLD else output HOT

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
	    int c;
	    cin>>c;
	    if(c>20)
	    cout<<"HOT"<<"\n";
	    else
	    cout<<"COLD"<<"\n";
	}
``

</details>
