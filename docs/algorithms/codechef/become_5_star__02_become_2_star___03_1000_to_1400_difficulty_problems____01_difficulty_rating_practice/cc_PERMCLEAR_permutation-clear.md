# Permutation Clear

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMCLEAR |
| Difficulty Rating | 1308 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [PERMCLEAR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/PERMCLEAR) |

---

## Problem Statement

Alice has an array $A$ of length $N$ which is initially a *permutation*. She dislikes $K$ numbers which are $B_1, B_2, \ldots, B_K$ all of which are **distinct**. Therefore, she removes all the occurrences of these numbers from $A$. The order of the remaining elements of the $A$ does **not** change.

Can you find out the resulting array $A$?

Note: A *permutation* of length $N$ is an array where every integer from $1$ to $N$ occurs exactly once.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ integers $A_1, A_2, \ldots, A_N$ denoting the array $A$.
- The third line of each test case contains an integer $K$ — the size of the array $B$.
- The fourth line of each test case contains $K$ integers $B_1, B_2, \ldots, B_K$ denoting the numbers which Alice dislikes.

---

## Output Format

For each test case, output the resulting array $A$ after the removal of all occurrences of $B_1, B_2, \ldots B_K$.

It is guaranteed that there will be at least one element in the resulting array.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq K \lt N \leq 10^5$
- $1 \le A_i, B_i \le N$
- $A$ is initially a *permutation*.
- $B_i \ne B_j$ when $(i \ne j)$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
4 1 3 2
2
3 1
9
5 2 9 1 8 6 4 3 7
3
5 8 9
5
3 4 5 1 2
2
2 3
```

**Output**

```text
4 2
2 1 6 4 3 7
4 5 1
```

**Explanation**

**Test Case 1:** Here $A = [4, 1, 3, 2]$ and $B = [3, 1]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[4, 2]$.

Note that here $[2, 4]$ is an incorrect answer since the order of elements should be the same as in the original array.

**Test Case 2:** Here $A = [5, 2, 9, 1, 8, 6, 4, 3, 7]$ and $B = [5, 8, 9]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[2, 1, 6, 4, 3, 7]$.

**Test Case 3:** Here $A = [3, 4, 5, 1, 2]$ and $B = [2, 3]$. The resulting array $A$ after removing all the numbers which Alice dislikes is $[4, 5, 1]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
4 1 3 2
2
3 1
```

**Output for this case**

```text
4 2
```



#### Test case 2

**Input for this case**

```text
9
5 2 9 1 8 6 4 3 7
3
5 8 9
```

**Output for this case**

```text
2 1 6 4 3 7
```



#### Test case 3

**Input for this case**

```text
5
3 4 5 1 2
2
2 3
```

**Output for this case**

```text
4 5 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PERMCLEAR)

[Contest: Division 1](https://www.codechef.com/START55A/problems/PERMCLEAR)

[Contest: Division 2](https://www.codechef.com/START55B/problems/PERMCLEAR)

[Contest: Division 3](https://www.codechef.com/START55C/problems/PERMCLEAR)

[Contest: Division 4](https://www.codechef.com/START55D/problems/PERMCLEAR)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/JeevanJyot)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1308

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice has a permutation of \{1, 2, \ldots, N\}. She dislikes K of these numbers B_1, \ldots, B_K. Can you print the permutation with these numbers removed?

#
[](#explanation-5)EXPLANATION:

This is an implementation problem more than anything else — it is enough to do exactly what is asked for.

Iterate across the values of A. Say we are currently at A_i, and we want to know whether to print it or not.

All that we really need to know is whether A_i is one of the elements of B, and to check this faster than \mathcal{O}(N) (since the constraints are such that \mathcal{O}(N^2) algorithms will TLE).

This check can be done in \mathcal{O}(\log N) or even \mathcal{O}(1), in several ways:

- The easiest way is to use the `set` data structure present in most languages. Insert all the elements of B into a set S, then simply check if A_i is in S. This check is \mathcal{O}(\log N) in C++ `set` and Java `TreeSet`, and \mathcal{O}(1) in python `set` and Java `HashSet`.

- Alternately, we can use an array. Note that all the elements are from 1 to N, so we can create an array mark of length N, such that mark_i is 1 if i is present in B and 0 otherwise. Now, we only need to look at mark_{A_i} to decide if A_i is in B, which takes \mathcal{O}(1) time.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = int(input())
	b = set(map(int, input().split()))
	for x in a:
		if x not in b:
			print(x, end = ' ')
	print('')
``

</details>
