# DNA Storage

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DNASTORAGE |
| Difficulty Rating | 801 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [DNASTORAGE](https://www.codechef.com/practice/course/strings/STRINGS/problems/DNASTORAGE) |

---

## Problem Statement

For encoding an even-length binary string into a sequence of `A`, `T`, `C`, and `G`, we iterate from **left to right** and replace the characters as follows:
- `00` is replaced with `A`
- `01` is replaced with `T`
- `10` is replaced with `C`
- `11` is replaced with `G`

Given a binary string $S$ of length $N$ ($N$ is even), find the encoded sequence.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains two lines of input.
- First line contains a single integer $N$, the length of the sequence.
- Second line contains binary string $S$ of length $N$.

---

## Output Format

For each test case, output in a single line the encoded sequence.

**Note:** Output is **case-sensitive**.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10^3$
- $N$ is even.
- Sum of $N$ over all test cases is at most $10^3$.
- $S$ contains only characters `0` and `1`.

---

## Examples

**Example 1**

**Input**

```text
4
2
00
4
0011
6
101010
4
1001
```

**Output**

```text
A
AG
CCC
CT
```

**Explanation**

**Test case $1$:** Based on the rules `00` is replaced with `A`.

**Test case $2$:** Based on the rules `00` is replaced with `A`. Similarly, `11` is replaced with `G`. Thus, the encoded sequence is `AG`.

**Test case $3$:** The first two characters are `10` which is encoded as `C`. Similarly, the next two characters `10` are encoded as `C` and the last two characters `10` are encoded as `C`. Thus, the encoded string is `CCC`.

**Test case $4$:** The first two characters are `10` which is encoded as `C`. Similarly, the next two characters `01` are encoded as `T`. Thus, the encoded string is `CT`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
00
```

**Output for this case**

```text
A
```



#### Test case 2

**Input for this case**

```text
4
0011
```

**Output for this case**

```text
AG
```



#### Test case 3

**Input for this case**

```text
6
101010
```

**Output for this case**

```text
CCC
```



#### Test case 4

**Input for this case**

```text
4
1001
```

**Output for this case**

```text
CT
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START43A/problems/DNASTORAGE)

[Contest Division 2](https://www.codechef.com/START43B/problems/DNASTORAGE)

[Contest Division 3](https://www.codechef.com/START43C/problems/DNASTORAGE)

[Contest Division 4](https://www.codechef.com/START43D/problems/DNASTORAGE)

Setter: [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

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

For encoding an even-length binary string into a sequence of `A`, `T`, `C`, and `G`, we iterate from **left to right** and replace the characters as follows:

-
`00` is replaced with `A`

-
`01` is replaced with `T`

-
`10` is replaced with `C`

-
`11` is replaced with `G`

Given a binary string S of length N (N is even), find the encoded sequence.

#
[](#explanation-5)EXPLANATION:

This is a simple implementation problem. We can run a for loop with an increment of 2 and for each two characters we can compare and output result as follows:

Suppose we are at the i_{th} pointer, then

if \; s[i] = 0 \; and \; s[i+1] = 0, \; output \; A
\\
if \; s[i] = 0 \; and \; s[i+1] = 1, \; output \; T
\\
if \; s[i] = 1 \; and \; s[i+1] = 0, \; output \; C
\\
if \; s[i] = 1 \; and \; s[i+1] = 1, \; output \; G

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/K8d2)

[Setter’s Solution](http://p.ip.fi/Mim6)

[Tester1’s Solution](http://p.ip.fi/h6Af)

[Tester2’s Solution](http://p.ip.fi/qYf-)

</details>
