# Alternating String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ALTSTR |
| Difficulty Rating | 1116 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ALTSTR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ALTSTR) |

---

## Problem Statement

A binary string is called *alternating* if no two adjacent characters of the string are equal. Formally, a binary string $T$ of length $M$ is called alternating if $T_i \neq T_{i +1}$ for each $1 \leq i \lt M$.

For example, `0`, `1`, `01`, `10`, `101`, `010`, `1010` are alternating strings while `11`, `001`, `1110` are not.

You are given a binary string $S$ of length $N$. You would like to rearrange the characters of $S$ such that the length of the **longest alternating substring** of $S$ is **maximum**. Find this maximum value.

A binary string is a string that consists of characters `0` and `1`. A string $a$ is a [substring](https://en.wikipedia.org/wiki/Substring) of a string $b$ if $a$ can be obtained from $b$ by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first line of each test case contains an integer $N$.
- The second line of each test case contains the binary string $S$.

---

## Output Format

For each test case, output the maximum possible length of the longest alternating substring of $S$ after rearrangement.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $S$ contains only the characters `0` and `1`.
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3
110
4
1010
4
0000
7
1101101
```

**Output**

```text
3
4
1
5
```

**Explanation**

**Test case $1$:** Swapping the second and third characters makes $S=101$. Hence the length of the longest alternating substring is $3$ (choosing the entire string as a substring).

**Test case $2$:** The given string $S=1010$ is an alternating string of length $4$.

**Test case $3$:** The length of the longest alternating substring is $1$ for any rearrangement of  $S=0000$.

**Test case $4$:** One possible rearrangement of $S$ is $1\underline{10101}1$, which has an alternating substring of length $5$ (the substring starting at index $2$ and ending at index $6$).

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
110
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1010
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
4
0000
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
7
1101101
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START31A/problems/ALTSTR)

[Contest Division 2](https://www.codechef.com/START31B/problems/ALTSTR)

[Contest Division 3](https://www.codechef.com/START31C/problems/ALTSTR)

[Contest Division 4](https://www.codechef.com/START31D/problems/ALTSTR)

Setter: [ Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

Tester: [ Aryan](https://www.codechef.com/users/aryanc403), [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk/Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A binary string is called alternating if no two adjacent characters of the string are equal. Formally, a binary string T of length M is called alternating if Ti?Ti+1 for each 1?i<M.

For example, 0, 1, 01, 10, 101, 010, 1010 are alternating strings while 11, 001, 1110 are not.

You are given a binary string S of length N. You would like to rearrange the characters of S such that the length of the longest alternating substring of S is maximum. Find this maximum value.

A binary string is a string that consists of characters 0 and 1. A string a is a substring of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.

#
[](#explanation-5)EXPLANATION:

To form the given string of maximum length, we calculate the number of 1’s and 0’s in the original string.

Let n_1, n_0 be the counts respectively.

**Case1: n_0 = n_1**

(Keeping either ‘0’ or ‘1’ in the beginning and alternating)

\implies ans = 2*n_1

**Case2: n_0 < n_1**

(Keeping ‘1’ in the beginning and alternating)

\implies ans = 2*n_0+1

**Case3: n_0 > n_1**

(Keeping ‘0’ in the beginning and alternating)

\implies ans = 2*n_1+1

The above three cases can be mathematically combined in a single equation as:

 ans = 2*min(n_0,n_1) + (n_1!=n_0)

#
[](#time-complexity-6)TIME COMPLEXITY:

The above calculation can be done in constant time. However, calculating n_1 and n_0 requires a complete iteration of the string. Hence, the solution has a time complexity of O(N).

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://pastebin.com/B1ax30u3)

[Setter’s Solution](http://p.ip.fi/tzNE)

[Tester-1’s Solution](http://p.ip.fi/AHvT)

[Tester-2’s Solution](http://p.ip.fi/AGeh)

</details>
