# Joining Date

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JOINING |
| Difficulty Rating | 970 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [JOINING](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/JOINING) |

---

## Problem Statement

$N$ candidates (numbered from $1$ to $N$) join Chef's firm. The first $5$ candidates join on the first day, and then, on every subsequent day, the next $5$ candidates join in.
For example, if there are $12$ candidates, candidates numbered $1$ to $5$ will join on day $1$, candidates numbered $6$ to $10$ on day $2$ and the remaining $2$ candidates will join on day $3$.

Candidate numbered $K$ decided to turn down his offer and thus, Chef adjusts the position by shifting up all the higher numbered candidates. This leads to a change in the joining day of some of the candidates.

Help Chef determine the number of candidates who will join on a different day than expected.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two space-separated integers $N$ and $K$ denoting the number of candidates and the candidate who turned down the offer.

---

## Output Format

For each test case, output a single integer denoting the number of candidates whose joining day will be changed.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$
- $1 \leq K \leq N$

---

## Examples

**Example 1**

**Input**

```text
4
7 3
6 6
2 1
14 2
```

**Output**

```text
1
0
0
2
```

**Explanation**

**Test case $1$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2, 2]$ but as candidate $3$ turns down his offer, the new joining days are now $[1, 1, NA, 1, 1, 1, 2]$. Candidate numbered $6$ is the only one to have his joining day changed.

**Test case $2$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2]$ but as candidate $6$ turns down his offer, the new joining days are now $[1, 1, 1, 1, 1, NA]$. No candidate got his joining day changed.

**Test case $3$:** The original joining day of each candidate is given as $[1, 1]$ but as candidate $1$ turns down his offer, the new joining days are now $[NA, 1]$. No candidate got his joining day changed.

**Test case $4$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]$ but as candidate $2$ turns down his offer, the new joining days are now $[1, NA, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]$. Candidate numbered $6$ and $11$ are the only ones to have their joining days changed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
6 6
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
2 1
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
14 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START43A/problems/JOINING)

[Contest Division 2](https://www.codechef.com/START43B/problems/JOINING)

[Contest Division 3](https://www.codechef.com/START43C/problems/JOINING)

[Contest Division 4](https://www.codechef.com/START43D/problems/JOINING)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

To be Calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

N candidates (numbered from 1 to N) join Chef’s firm. The first 5 candidates join on the first day, and then, on every subsequent day, the next 5 candidates join in.

For example, if there are 12 candidates, candidates numbered 1 to 5 will join on day 1, candidates numbered 6 to 10 on day 2 and the remaining 2 candidates will join on day 3.

Candidate numbered K decided to turn down his offer and thus, Chef adjusts the position by shifting up all the higher numbered candidates. This leads to a change in the joining day of some of the candidates.

Help Chef determine the number of candidates who will join on a different day than expected.

#
[](#explanation-5)EXPLANATION:

Total number of groups of 5 would be:

total = \lfloor \frac{n+4}{5} \rfloor

Total number of groups that won’t be affected:

unaffected = \lfloor \frac{k+4}{5} \rfloor

All the groups that are after the group containing the k_{th} candidate will have 1 person whose joining date will change since he will be shifted to one previous group.

Thus

affected = total - unaffected

which is our answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/_1ka)

[Setter’s Solution](http://p.ip.fi/ln4w)

[Tester1’s Solution](http://p.ip.fi/2Yc4)

[Tester2’s Solution](http://p.ip.fi/QsVp)

</details>
