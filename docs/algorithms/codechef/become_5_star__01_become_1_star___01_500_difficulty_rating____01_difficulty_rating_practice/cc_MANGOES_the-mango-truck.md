# The Mango Truck

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MANGOES |
| Difficulty Rating | 482 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MANGOES](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MANGOES) |

---

## Problem Statement

You are given that a mango weighs $X$ kilograms and a truck weighs $Y$ kilograms.
You want to cross a bridge that can withstand a weight of $Z$ kilograms.

Find the **maximum** number of mangoes you can load in the truck so that you can cross the bridge safely.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, three integers $X, Y, Z$ - the weight of mango, the weight of truck and the weight the bridge can withstand respectively.

---

## Output Format

For each test case, output in a single line the **maximum** number of mangoes that you can load in the truck.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq Y \leq Z \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
2 5 11
4 10 20
1 1 1
6 40 90
```

**Output**

```text
3
2
0
8
```

**Explanation**

**Test case $1$:** You can load $3$ mangoes at maximum. The total weight is $ 3\times 2+5 = 11 \leq 11$. Thus, the truck can safely cross the bridge with $3$ mangoes. If you load $4$ mangoes, the total weight is $4\times 2+5 = 13 \gt 11$.

**Test case $2$:** You can load $2$ mangoes at maximum. The total weight is $ 2\times 4+10 = 18 \leq 20$. Thus, the truck can safely cross the bridge with $2$ mangoes.

**Test case $3$:** You can load $0$ mangoes at maximum. The total weight is $ 0\times 1+1 = 1 \leq 1$. Thus, the truck can safely cross the bridge only if there are $0$ mangoes.

**Test case $4$:** You can load $8$ mangoes at maximum. The total weight is $ 6\times 8+40 = 88 \leq 90$. Thus, the truck can safely cross the bridge with $8$ mangoes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 11
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 10 20
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1 1 1
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
6 40 90
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START37A/problems/MANGOES)

[Contest Division 2](https://www.codechef.com/START37B/problems/MANGOES)

[Contest Division 3](https://www.codechef.com/START37C/problems/MANGOES)

[Contest Division 4](https://www.codechef.com/START37D/problems/MANGOES)

Setter: [Yuvraj Garg](https://www.codechef.com/users/yjgarg)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

482

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given that a mango weighs X kilograms and a truck weighs Y kilograms.

You want to cross a bridge that can withstand a weight of Z kilograms.

Find the **maximum** number of mangoes you can load in the truck so that you can cross the bridge safely.

#
[](#explanation-5)EXPLANATION:

Given the maximum weight that the bridge can withstand is Z kilograms and the weight of truck is Y, so the maximum weight of mangoes that the truck can carry would be (Z-Y) kilograms. Now we need to check how many mangoes can be loaded in the truck when its limit is (Z-Y), which would be as follows:

answer = \lfloor \frac{Z-Y}{X} \rfloor

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1)  for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/hKUc)

[Setter’s Solution](http://p.ip.fi/4o5O)

[Tester1’s Solution](http://p.ip.fi/qbIG)

[Tester2’s Solution](http://p.ip.fi/GQtR)

</details>
