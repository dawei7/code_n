# Array Equality

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARREQU |
| Difficulty Rating | 1281 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [ARREQU](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/ARREQU) |

---

## Problem Statement

Chef has an array of $N$ integers. Chef can rearrange this array in any manner.

Chef doesn’t like the array if any two **adjacent** elements are equal. Determine whether there exists a rearrangement of the array that Chef likes.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- First line of each test case contains a single integer $N$ - size of the array $A$.
- Second line of each test case contains $N$ space-separated integers - denoting the elements of array $A$.

---

## Output Format

For each test case, if Chef can like any rearrangement of the array print `YES`, otherwise print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yes`, `yEs`, `YeS`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
1 1 1 1 1
3
3 3 4
```

**Output**

```text
No
Yes
```

**Explanation**

**Test case $1$:** There exists no rearrangement of the array which Chef will like.

**Test case $2$:** A rearrangement of the array that Chef likes is $[3, 4, 3]$. Note that in this rearrangement, no two adjacent elements are equal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
No
```



#### Test case 2

**Input for this case**

```text
3
3 3 4
```

**Output for this case**

```text
Yes
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ARREQU)

[Contest: Division 1](https://www.codechef.com/LTIME111A/problems/ARREQU)

[Contest: Division 2](https://www.codechef.com/LTIME111B/problems/ARREQU)

[Contest: Division 3](https://www.codechef.com/LTIME111C/problems/ARREQU)

[Contest: Division 4](https://www.codechef.com/LTIME111D/problems/ARREQU)

***Author:*** [S. Manuj Nanthan](https://www.codechef.com/users/munch_01)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1281

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

Chef has an array A of length N. Can it be rearranged such that no two adjacent elements are equal?

#
[](#explanation-5)EXPLANATION:

Let the maximum frequency of an element in A be M. Then, the answer is “Yes” if and only if M \leq \left\lceil \frac{N}{2}\right\rceil, i.e, 2\cdot M \leq N+1.

Proof

- First, suppose that some element x appears strictly more than \left\lceil \frac{N}{2}\right\rceil times. Then clearly in any rearrangement, there will be two occurrences of x next to each other.

- Next, suppose that every element appears \leq \left\lceil \frac{N}{2}\right\rceil times. A valid rearrangement can be constructed recursively as follows:

- If N = 1 or N = 2, nothing needs to be done - any array is good.

- Otherwise, let x and y be the two elements with highest frequency in A. Remove one occurrence of x and y from A, and solve it for length N-2 recursively (note that since we are removing the elements with highest frequency, the condition on maximum frequency still holds). Now, append either [x, y] or [y, x] to the solution obtained from N-2: at least one of these will not cause a conflict and we are done.

This gives us a simple solution:

- Count the frequency of every element of A using some method (`map` in C++, `dict/collections.Counter` in python, sorting, etc)

- The answer is “Yes” if the maximum frequency is \leq \left\lceil \frac{N}{2}\right\rceil and “No” otherwise.

- To be safe and not have to deal with floating-point issues, check the condition 2\cdot M \leq N+1 instead of computing \left\lceil \frac{N}{2}\right\rceil.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) or \mathcal{O}(N\log N) per test case, depending on implementation.

#
[](#code-7)CODE:

Editorialist's code (Python)
``import collections
for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	freq = collections.Counter(a)
	print('yes' if 2*max(freq.values()) <= n+1 else 'no')
``

</details>
