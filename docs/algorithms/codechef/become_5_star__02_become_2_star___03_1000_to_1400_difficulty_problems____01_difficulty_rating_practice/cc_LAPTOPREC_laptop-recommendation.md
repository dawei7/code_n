# Laptop Recommendation 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LAPTOPREC |
| Difficulty Rating | 1104 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [LAPTOPREC](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/LAPTOPREC) |

---

## Problem Statement

Chef wants to buy a new laptop. However, he is confused about which laptop to buy out of $10$ different laptops. He asks his $N$ friends for their recommendation. The $i^{th}$ friend recommends the Chef to buy the ${A_i}^{th}$ laptop $(1 \le A_i \le 10)$.

Chef will buy the laptop which is recommended by **maximum** number of friends. Determine which laptop Chef buys.
Print `CONFUSED` if there are multiple laptops having maximum number of recommendations.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the number of Chef's friends.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ where $A_i$ denotes the recommendation of the $i^{th}$ friend.

---

## Output Format

For each test case, output in a single line, the laptop which has the **maximum** number of recommendations. Print `CONFUSED` if there are multiple laptops having maximum number of recommendations.

You may print each character of `CONFUSED` in uppercase or lowercase (for example, `Confused`, `coNFused`, `CONFused` will be considered identical).

---

## Constraints

- $1 \leq T \leq 200$
- $1 \leq N \leq 1000$
- $1 \le A_i \le 10$

---

## Examples

**Example 1**

**Input**

```text
4
5
4 4 4 2 1
7
1 2 3 4 5 6 6
6
2 2 3 3 10 8
4
7 7 8 8
```

**Output**

```text
4
6
CONFUSED
CONFUSED
```

**Explanation**

**Test case 1:** Laptop $4$ has the maximum number of recommendations. Therefore, Chef will buy the $4^{th}$ laptop.

**Test case 2:** Laptop $6$ has the maximum number of recommendations. Therefore, Chef will buy the $6^{th}$ laptop.

**Test case 3:** Laptops $2$, $3$ have the maximum number of recommendations. Therefore, Chef will still be `CONFUSED`.

**Test case 4:** Laptops $7$, $8$ have the maximum number of recommendations. Therefore, Chef will still be `CONFUSED`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
4 4 4 2 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
7
1 2 3 4 5 6 6
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
6
2 2 3 3 10 8
```

**Output for this case**

```text
CONFUSED
```



#### Test case 4

**Input for this case**

```text
4
7 7 8 8
```

**Output for this case**

```text
CONFUSED
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START37A/problems/LAPTOPREC)

[Contest Division 2](https://www.codechef.com/START37B/problems/LAPTOPREC)

[Contest Division 3](https://www.codechef.com/START37C/problems/LAPTOPREC)

[Contest Division 4](https://www.codechef.com/START37D/problems/LAPTOPREC)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1104

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to buy a new laptop. However, he is confused about which laptop to buy out of 10 different laptops. He asks his N friends for their recommendation. The i^{th} friend recommends the Chef to buy the ${A_i}^{th}laptop (1 \le A_i \le 10)$.

Chef will buy the laptop which is recommended by **maximum** number of friends. Determine which laptop Chef buys.

Print `CONFUSED` if there are multiple laptops having maximum number of recommendations.

#
[](#explanation-5)EXPLANATION:

Here we can use an unordered map or an array of length 10 to keep count of number of recommendations for each laptop. Once we have the count, we can easily determine which laptop has the maximum recommendations which would be our answer.

Also we have to do one additional check to see if there are more than one laptop with maximum recommendations in which case the answer would be CONFUSED.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/8lcx)

[Setter’s Solution](http://p.ip.fi/3sS7)

[Tester1’s Solution](http://p.ip.fi/6hdL)

[Tester2’s Solution](http://p.ip.fi/R0yv)

</details>
