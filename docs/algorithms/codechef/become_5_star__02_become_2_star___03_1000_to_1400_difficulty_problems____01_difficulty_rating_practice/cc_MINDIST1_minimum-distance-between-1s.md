# Minimum distance between 1s

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINDIST1 |
| Difficulty Rating | 1335 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MINDIST1](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MINDIST1) |

---

## Problem Statement

Chef has a **binary** string $S$ of size $N$. Chef can perform the following operation on the string:
- Select any substring of size $3$ and **reverse** it.

Find the **minimum** *distance* between **any two** $1$s Chef can achieve, by applying the above operation any (possibly zero) number of times.

Note:
- The *distance* between two characters $S_i$ and $S_j$ is defined as $abs(i-j)$.
- It is guaranteed that the string contains **at least** two occurrences of $1$.
- A substring is obtained by deleting some (possibly zero) elements from the beginning and some (possibly zero) elements from the end of the string.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of characters in the string.
    - The next line contains a binary string of length $N$.

---

## Output Format

For each test case, output on a new line, the **minimum** distance between **any two** $1$s Chef can achieve, by applying the above operation any (possibly zero) number of times.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $S_i$ contains $0$ and $1$ only.
- It is guaranteed that $S$ contains **at least** two occurrences of $1$.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
11
3
101
7
0100101
```

**Output**

```text
1
2
1
```

**Explanation**

**Test case $1$:** There are only two $1$s in the string. The distance between the $1$s is $2-1 = 1$.

**Test case $2$:** The distance between the given $1$s is $3-1 = 2$. It can be shown that we cannot achieve a distance smaller than $2$ by applying any number of operations.

**Test case $3$:** Chef can perform the following operation:
- Select the substring $S[2,4] = 100$ and reverse it. Thus, the string becomes $S = 0001101$. The minimum distance between the $1$s in the string is $5-4 = 1$.

It can be shown that we cannot achieve a distance smaller than $1$ by applying any number of operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
11
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
101
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
7
0100101
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINDIST1)

[Contest: Division 1](https://www.codechef.com/START70A/problems/MINDIST1)

[Contest: Division 2](https://www.codechef.com/START70B/problems/MINDIST1)

[Contest: Division 3](https://www.codechef.com/START70C/problems/MINDIST1)

[Contest: Division 4](https://www.codechef.com/START70D/problems/MINDIST1)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1335

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a binary string S, in one move you can reverse any substring of length 3. What’s the minimum distance between some pair of ones that you can achieve?

#
[](#explanation-5)EXPLANATION:

Suppose we reverse the substring consisting of indices [i, i+1, i+2]. Notice that this is essentially the same as swapping S_i and S_{i+2}.

In particular, if a `1` is on an even position, then after a move it will remain on an even position; and the same holds for odd positions.

However, among the even positions we can swap ‘adjacent’ elements, which means we can rearrange them as we like. This applies to the odd positions as well.

So,

- If there is a `1` on an even position and a `1` on an odd position, we can rearrange the string to make them adjacent, giving us an answer of 1 (which is obviously the minimum possible).

- If the above condition doesn’t hold, then all the ones are on positions of the same parity. In this case, we can make the distance between them 2.

So, all that needs to be done is to iterate across the string and check whether there are ones at both even and odd positions.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
	n = int(input())
	s = input()
	odd, even = 0, 0
	for i in range(n):
		if s[i] == '1':
			if i%2 == 0: even = 1
			else: odd = 1
	print(1 if odd > 0 and even > 0 else 2)
``

</details>
