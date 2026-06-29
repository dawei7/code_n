# Chess Time

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHESSTIME |
| Difficulty Rating | 337 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CHESSTIME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CHESSTIME) |

---

## Problem Statement

Chef has recently started playing chess, and wants to play as many games as possible.

He calculated that playing one game of chess takes at least $20$ minutes of his time.

Chef has $N$ **hours** of free time. What is the maximum number of **complete** chess games he can play in that time?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing a single integer, $N$.

---

## Output Format

For each test case, output on a new line the maximum number of complete chess games Chef can play in $N$ hours.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
1
10
7
3
```

**Output**

```text
3
30
21
9
```

**Explanation**

**Test case $1$:** If every game Chef plays takes $20$ minutes, he can play $3$ games in one hour.

**Test case $2$:** If every game Chef plays takes $20$ minutes, he can play $30$ games in $10$ hours.

**Test case $3$:** If every game Chef plays takes $20$ minutes, he can play $21$ games in $7$ hours.

**Test case $4$:** If every game Chef plays takes $20$ minutes, he can play $9$ games in $3$ hours.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
10
```

**Output for this case**

```text
30
```



#### Test case 3

**Input for this case**

```text
7
```

**Output for this case**

```text
21
```



#### Test case 4

**Input for this case**

```text
3
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/START47/)

[Practice](https://www.codechef.com/problems/CHESSTIME)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Tester: [ Abhinav Sharma](https://www.codechef.com/users/inov_360), [ Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Kiran](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

337

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has recently started playing chess, and wants to play as many games as possible. Chef takes at least 20 minutes to play one game. Our objective is to find what is the maximum number of complete chess games he can play if he has got N hours of free time.

#
[](#explanation-5)EXPLANATION:

-

Here we take an input to variable N representing the available free time in Hours.

-

Given that the Chef takes at least 20 minutes to finish a game, we need to calculate the available free time in minutes.

-

Comparing the available free time with the time taken for a single game, we get the maximum number of games chef can play.

-

Solution:

-

N hours = N*60 minutes of free time

-

Maximum number of games chef can play = (N*60)/20

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1)

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	    int n;
	    cin>>n;
	    cout<<(n*60)/20<<"\n";
	}
``

</details>
