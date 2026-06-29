# Broken Life

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BRKNLIFE |
| Difficulty Rating | 1772 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [BRKNLIFE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/BRKNLIFE) |

---

## Problem Statement

You are given two strings $S$ and $A$ of lengths $N$ and $M$ respectively.
- String $S$ contains characters from the set $\texttt{\{?, a, b, c, d, e\}}$.
- String $A$ contains characters from the set $\texttt{\{a, b, c, d, e\}}$.

Let $S'$ denote the string formed by replacing **all** the $\texttt{?}$ in $S$ using the characters from the set $\texttt{\{a, b, c, d, e\}}$.
Construct $S'$ such that $A$ is **not** a [subsequence](https://en.wikipedia.org/wiki/Subsequence) of $S'$.

If multiple such $S'$ exist, output any. If no such $S'$ exists, print $-1$.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ - the lengths of strings $S$ and $A$ respectively.
- The second line of each test case contains string $S$.
- The third line of each test case contains string $A$.

---

## Output Format

For each test case, output any valid string $S'$. If no such string exists, print $-1$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,M \leq 10^5$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.
- Sum of $M$ over all test cases does not exceed $3 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
4 2
?ab?
ba
4 2
a??b
ab
```

**Output**

```text
aabe
-1
```

**Explanation**

**Test case $1$:** Replace the $\texttt{?}$ at indices $1$ and $4$ using characters $\texttt{a}$ and $\texttt{e}$ respectively. Both the characters belong to the set $\texttt{\{a, b, c, d, e\}}$.
The string $S' = \texttt{aabe}$. Note that no subsequence of $S'$ is equal to $\texttt{ba}$.

**Test case $2$:** There is no possible value of $S'$ such that $\texttt{ab}$ is not a subsequence of $S'$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 2
?ab?
ba
```

**Output for this case**

```text
aabe
```



#### Test case 2

**Input for this case**

```text
4 2
a??b
ab
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START33A/problems/BRKNLIFE)

[Contest Division 2](https://www.codechef.com/START33B/problems/BRKNLIFE)

[Contest Division 3](https://www.codechef.com/START33C/problems/BRKNLIFE)

[Contest Division 4](https://www.codechef.com/START33D/problems/BRKNLIFE)

Setter: [S.Manuj Nanthan](https://www.codechef.com/users/munch_01)

Testers: Abhinav Sharma[[inov_360 | CodeChef User Profile for Abhinav sharma | CodeChef](https://www.codechef.com/users/inov_360)], Nishank Suresh [[iceknight1093 | CodeChef User Profile for Nishank Suresh | CodeChef](https://www.codechef.com/users/iceknight1093)]

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given two strings S and A of lengths N and M respectively.

String S contains characters from the set {?, a, b, c, d, e}.

String A contains characters from the set {a, b, c, d, e}.

Let S? denote the string formed by replacing all the ? in S using the characters from the set {a, b, c, d, e}.

Construct S? such that A is not a subsequence of S?.

If multiple such S? exist, output any. If no such S? exists, print ?1.

#
[](#explanation-5)EXPLANATION:

It is obvious that if string A is already a subsequence of string S then there is no way to construct S’ so return -1.

For when it is not a subsequence of S, we keep a track of how much of prefix substring of A has been found as subsequence as we traverse the string. When we encounter a ‘?’ we place a character in S’ which is not same as the next index of the prefix substring. Thus avoiding replacing of a same characters as in string A. Continue this till all ‘?’ have been processed which results in S’ which does not have A as a subsequence.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(|S|) for each test case as we traverse the string once.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://paste-bin.xyz/48876)

[Tester1’s Solution](https://p.ip.fi/kZgr)

[Tester2’s Solution](https://p.ip.fi/7uvl)

</details>
