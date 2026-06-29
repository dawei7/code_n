# Air Blimp

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BLIMP |
| Difficulty Rating | 1831 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [BLIMP](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/BLIMP) |

---

## Problem Statement

There are $N$ cities in a row. The $i$-th city from the left has a sadness of $A_i$.

In an attempt to reduce the sadness of the cities, you can send [blimps](https://en.wikipedia.org/wiki/Blimp) from the left of city $1$ that move rightwards (i.e, a blimp crosses cities $1, 2, \ldots$ in order)

You are given two integers $X$ and $Y$. For each blimp sent, you can make one of the following choices:
- Let the blimp fly over every city, in which case the sadness of **every city** will decrease by $Y$, or,
- Choose a city $i$ $(1 \leq i \leq N)$, and shower confetti over city $i$. In this case, the sadness of cities $1, 2, \ldots, i-1$ will decrease by $Y$, the sadness of city $i$ will decrease by $X$, and cities $i+1, \ldots, N$ see no change in sadness.

Find the **minimum** number of blimps needed such that, by making the above choice optimally for each blimp, you can ensure that no city is sad (i.e, in the end every city has sadness $\leq 0$).

---

## Input Format

- The first line of input contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains three space-separated integers $N, X, Y$ — the size of the array, and the parameters mentioned in the statement.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$, denoting the sadness of the $N$ cities.

---

## Output Format

For each test case, output on a new line the minimum number of blimps needed such that no city is sad.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 3\cdot10^5$
- $1 \leq X,Y \leq 10^9$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $3\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
3
4 4 4
1 5 4 4
5 4 3
1 4 3 3 5
4 3 1
3 1 3 9
```

**Output**

```text
2
2
3
```

**Explanation**

**Test case $1$:** One way of using two blimps is as follows:
- Initially, $A = [1, 5, 4, 4]$
- Shower confetti on city $2$. Now, $A = [-3, 1, 4, 4]$.
- Shower confetti on city $4$. Now, $A = [-7, -3, 0, 0]$ and we are done.

**Test case $2$:** One way of using two blimps is as follows:
- Initially, $A = [1, 4, 3, 3, 5]$
- Let a blimp fly over every city. Now, $A = [-2, 1, 0, 0, 2]$.
- Shower confetti on city $5$. Now, $A = [-5, -2, -3, -3, -2]$, and we are done.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 4 4
1 5 4 4
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 4 3
1 4 3 3 5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 3 1
3 1 3 9
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START50A/problems/BLIMP)

[Contest Division 2](https://www.codechef.com/START50B/problems/BLIMP)

[Contest Division 3](https://www.codechef.com/START50C/problems/BLIMP)

[Contest Division 4](https://www.codechef.com/START50D/problems/BLIMP)

Setter: [Ashish Gangwar](https://www.codechef.com/users/kryptonix171)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1831

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N cities in a row. The i-th city from the left has a sadness of A_i.

In an attempt to reduce the sadness of the cities, you can send [blimps](https://en.wikipedia.org/wiki/Blimp) from the left of city 1 that move rightwards (i.e, a blimp crosses cities 1, 2, \ldots in order)

You are given two integers X and Y. For each blimp sent, you can make one of the following choices:

- Let the blimp fly over every city, in which case the sadness of **every city** will decrease by Y, or,

- Choose a city i (1 \leq i \leq N), and shower confetti over city i. In this case, the sadness of cities 1, 2, \ldots, i-1 will decrease by Y, the sadness of city i will decrease by X, and cities i+1, \ldots, N see no change in sadness.

Find the **minimum** number of blimps needed such that, by making the above choice optimally for each blimp, you can ensure that no city is sad (i.e, in the end every city has sadness \leq 0).

#
[](#explanation-5)EXPLANATION:

Case \;1: X \leq Y: In this case, since X is always smaller than Y, so it won’t make sense to shower confetti over any city so we would just let the blimp pass over each city and thus for each blimp the sadness of all cities would reduce by Y. Thus our answer would be

ans = \lceil \frac{A_{max}}{Y} \rceil
\\
where \; A_{max} = max(A_i), 1 \leq i \leq N

Case \;2: In this case it would be most efficient to show confetti to the farthest right city that has a positive value. This way all the cities before that would have their sadness reduced by Y and the last city would have its sadness reduced by X. Showering confetti before the last city with positive sadness won’t make sense since then the cities after that won’t have any sadness reduced.

In this case we would loop from end to start to calculate and for each say, the i_{th} city, we would calculate its current value, which would be the total number of blimps passed through it before the blimp started showering confetti on it. Let us assume total number of blimps passed as total\_blimps, and the sadness levels of the i_{th} city as A[i]

A[i] = max(0,A[i] - total\_blimps \times y)
\\
total\_blimps = total\_blimps + \lceil \frac{A[i]}{X}  \rceil

Our final answer would be total\_blimps at the end of the loop.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/yhqd)

[Setter’s Solution](http://p.ip.fi/UUmK)

[Tester1’s Solution](http://p.ip.fi/q0fx)

[Tester2’s Solution](http://p.ip.fi/FdxH)

</details>
