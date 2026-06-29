# Difference Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATDIF |
| Difficulty Rating | 1377 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MATDIF](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MATDIF) |

---

## Problem Statement

You are given an integer $N$. You need to find an $N\times N$ matrix such that:
- Each element of the matrix is an integer from $1$ to $N^2$;
- All elements of the matrix are **unique**;
- The absolute difference between elements in neighbouring cells is **strictly greater** than $1$.

It can be shown that there is at least one matrix that satisfies the given conditions. If multiple matrices satisfy the given conditions, print any.

Note that two cells are considered to be neighbours if they have a common side **or** a common vertex (i.e. a cell can have at most $8$ neighbouring cells).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains a single line of input, an integer $N$, denoting the number of rows and columns in the required matrix.

---

## Output Format

For each test case, output $N$ lines, where the $i^{th}$ line contains $N$ space-separated integers, denoting the elements of the $i^{th}$ row.

---

## Constraints

- $1 \leq T \leq 1000$
- $4 \leq N \leq 1000$
- The sum of $N^2$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
1
4
```

**Output**

```text
12  10  6   14
3   8   4   1
5   15  11  9
2   7   13  16
```

**Explanation**

**Test case $1$:** The given matrix satisfies all the conditions.

Note that all elements are unique and in the range $[1, N^2]$. Also, the absolute difference between any two neighbouring cells is greater than $1$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MATDIF)

[Contest: Division 1](https://www.codechef.com/START82A/problems/MATDIF)

[Contest: Division 2](https://www.codechef.com/START82B/problems/MATDIF)

[Contest: Division 3](https://www.codechef.com/START82C/problems/MATDIF)

[Contest: Division 4](https://www.codechef.com/START82D/problems/MATDIF)

***Authors:*** [shubham_grg](https://www.codechef.com/users/shubham_grg)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N \geq 4, find any N\times N matrix that consists of distinct integers from 1 to N^2, such that no two adjacent cells contain elements that differ by 1.

Two cells are adjacent if they touch horizontally, vertically, or diagonally.

#
[](#explanation-5)EXPLANATION:

Notice that it’d be nice if we could surround even integers with other even integers, and odd integers with other odd integers.

This is because any two distinct integers of the same parity differ by at least 2.

In fact, doing this greedily is enough to construct a valid matrix.

Let’s fill the matrix first with increasing even numbers, then with increasing odd numbers.

For example, for N = 4 we obtain

\begin{bmatrix}
2 & 4 & 6 & 8 \\
10 & 12 & 14 & 16 \\
1 & 3 & 5 & 7 \\
9 & 11 & 13 & 15
\end{bmatrix}

and for N = 5 we obtain

\begin{bmatrix}
2 & 4 & 6 & 8 & 10 \\
12 & 14 & 16 & 18 & 20 \\
22 & 24 & 1 & 3 & 5 \\
7 & 9 & 11 & 13 & 15 \\
17 & 19 & 21 & 23 & 25
\end{bmatrix}

It’s not hard to see that this matrix works, because when N \geq 4, there is at least one row separating any two integers whose difference is 1 (for example, for N = 4, 5 is in the third row while 4 and 6 are both in the first), so they’ll never be adjacent in the matrix.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N^2) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <iostream>

using namespace std;

void ANS(int n)
{
   int curr=2;
   for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {
            if(curr>n*n) curr=1;
            cout<<curr<<" ";
            curr+=2;
        }
        cout<<endl;
    }
}

int main() {
	// your code goes here

	int t; cin>>t;
	while(t--)
	{
	    int n; cin>>n;
	    ANS(n);
	}

	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(range(1, n*n + 1))
    a.sort(key = lambda x: (x%2)* (10**9) + x)
    for i in range(n): print(*a[i*n:i*n+n])
``

</details>
