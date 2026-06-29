# Distinct Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISPAL |
| Difficulty Rating | 1304 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DISPAL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DISPAL) |

---

## Problem Statement

Given integers $N$ and $X$, generate a [palindrome](https://en.wikipedia.org/wiki/Palindrome) of length $N$ consisting of **lowercase English alphabets** such that the number of **distinct** characters in the palindrome is **exactly** $X$.
If it is impossible to do so, print $-1$ instead.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $N, X$, as mentioned in the statement.

---

## Output Format

For each test case, output in a single line, a palindrome of length $N$ consisting of **lowercase English alphabet** such that the number of distinct characters in the palindrome is $X$. If it is not possible to do so, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq X \leq min(N, 26)$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
1 1
2 1
3 3
4 2
```

**Output**

```text
z
aa
-1
xyyx
```

**Explanation**

**Test case $1$:** A possible palindrome of length $1$ having $1$ distinct character is `z`.

**Test case $2$:** A possible palindrome of length $2$ having $1$ distinct character is `aa`.

**Test case $3$:** It can be proven that there exists no possible palindrome of length $3$ having $3$ distinct characters.

**Test case $4$:** The palindrome `xyyx` has length $4$ and contains $2$ distinct characters namely `x` and `y`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
z
```



#### Test case 2

**Input for this case**

```text
2 1
```

**Output for this case**

```text
aa
```



#### Test case 3

**Input for this case**

```text
3 3
```

**Output for this case**

```text
-1
```



#### Test case 4

**Input for this case**

```text
4 2
```

**Output for this case**

```text
xyyx
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START43A/problems/DISPAL)

[Contest Division 2](https://www.codechef.com/START43B/problems/DISPAL)

[Contest Division 3](https://www.codechef.com/START43C/problems/DISPAL)

[Contest Division 4](https://www.codechef.com/START43D/problems/DISPAL)

Setter: [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

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

Given integers N and X, generate a [palindrome](https://en.wikipedia.org/wiki/Palindrome) of length N consisting of **lowercase English alphabets** such that the number of **distinct** characters in the palindrome is **exactly** X.

If it is impossible to do so, print -1 instead.

#
[](#explanation-5)EXPLANATION:

Lets tackle this problem case by case:

- Case 1: When N = 1:

Here the answer can be any character, example ‘a’.

- Case 2: When N\lt(2 \times X) - 1:

Here it won’t be possible to construct the required string, since for X distinct characters we need to use at least (2 \times X - 1) characters.

- Case 3: When N = (2 \times X) -1:

Assuming s to be a string of length X having all distinct characters, we can construct the following string as our answer:

s_1s_2...s_{x-1}s_xs_{x-1}s_{x-2}....s_1

- Case 4: When N  \gt  (2 \times X) - 1:

Assuming s to be a string of length X having all distinct characters, we can have three parts as:

left = s
	\\
	mid = A \;string \;of \;length \;(N - 2 \times X) \; having\; all\; characters\; as\; s_1
	\\
	right = reverse(s)

Thus our final answer for this case would then be:

ans = left + mid + right

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/aaSH)

[Setter’s Solution](http://p.ip.fi/p2bD)

[Tester1’s Solution](http://p.ip.fi/zRu7)

[Tester2’s Solution](http://p.ip.fi/boFN)

</details>
