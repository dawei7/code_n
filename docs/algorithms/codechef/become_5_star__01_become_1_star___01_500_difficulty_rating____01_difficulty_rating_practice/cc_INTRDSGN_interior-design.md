# Interior Design

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INTRDSGN |
| Difficulty Rating | 373 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [INTRDSGN](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/INTRDSGN) |

---

## Problem Statement

Chef decided to redecorate his house, and now needs to decide between two different styles of interior design.

For the first style, tiling the floor will cost $X_1$ rupees and painting the walls will cost $Y_1$ rupees.

For the second style, tiling the floor will cost $X_2$ rupees and painting the walls will cost $Y_2$ rupees.

Chef will choose whichever style has the lower total cost. How much will Chef pay for his interior design?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input, containing $4$ space-separated integers $X_1, Y_1, X_2, Y_2$ as described in the statement.

---

## Output Format

For each test case, output on a new line the amount Chef will pay for interior design.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X_1, Y_1, X_2, Y_2 \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
10 20 9 25
10 20 9 20
10 20 20 10
100 43 85 61
```

**Output**

```text
30
29
30
143
```

**Explanation**

**Test case $1$:** The first style costs $10 + 20 = 30$ rupees, and the second costs $9 + 25 = 34$ rupees. The first is cheaper, so Chef will pay $30$ rupees.

**Test case $2$:** The first style costs $10 + 20 = 30$ rupees, and the second costs $9 + 20 = 29$ rupees. The second is cheaper, so Chef will pay $29$ rupees.

**Test case $3$:** The first style costs $10 + 20 = 30$ rupees, and the second costs $20 + 10 = 30$ rupees. Both styles cost the same, so Chef is always going to pay $30$ rupees.

**Test case $4$:** The first style costs $100 + 43 = 143$ rupees, and the second costs $85 + 61 = 146$ rupees. The first is cheaper, so Chef will pay $143$ rupees.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20 9 25
```

**Output for this case**

```text
30
```



#### Test case 2

**Input for this case**

```text
10 20 9 20
```

**Output for this case**

```text
29
```



#### Test case 3

**Input for this case**

```text
10 20 20 10
```

**Output for this case**

```text
30
```



#### Test case 4

**Input for this case**

```text
100 43 85 61
```

**Output for this case**

```text
143
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/LTIME110/)

[Practice](https://www.codechef.com/problems/INTRDSGN)

**Setter:** [iceknight1093](https://www.codechef.com/users/iceknight1093)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

**Editorialist:** [kiran8268](https://www.codechef.com/users/kiran8268)

#
[](#difficulty-2)DIFFICULTY:

373

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef decided to redecorate his house, and now he has two available styles. He’ll choose whichever style has the lower total cost. Our objective is to find how much will Chef pay for his interior design?

#
[](#explanation-5)EXPLANATION:

-

For the first style, tiling the floor will cost X_1 rupees and painting the walls will cost Y_1 rupees.

-

For the second style, tiling the floor will cost X_2 rupees and painting the walls will cost Y_2 rupees.

-

The total cost of first style is X_1+Y_1 and that of second style is X_2+Y_2.

-

Our objective is to find the minimum among the  cost of style 1 and style 2 and output the minimum cost.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(1).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``	int t;
	cin>>t;
	while(t--)
	{
	    int a,b,c,d;
	    cin>>a>>b>>c>>d;
	    cout<<min((a+b),(c+d))<<"\n";
	}
``

</details>
