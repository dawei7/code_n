# One-XOR Deletions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DELXORONE |
| Difficulty Rating | 1516 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [DELXORONE](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/DELXORONE) |

---

## Problem Statement

Chef has with him an array $A$ of length $N$. In one move, he can delete any element from $A$.

Find the minimum number of deletions Chef must make so that the following condition holds:
- Let $B$ denote the resulting array, and $M$ be the length of $B$.
- Then, $B_i \oplus B_j \leq 1$ for every $1 \leq i, j \leq M$.

Here, $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

For example, $[3, 3, 3]$ and $[6, 7, 6, 7]$ are valid final arrays, while $[1, 2]$ and $[6, 7, 8]$ are not (because $1 \oplus 2 = 3$ and $7\oplus 8 = 15$, respectively).

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, denoting the length of array $A$.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of array $A$.

---

## Output Format

For each test case, output on a new line the answer: the minimum number of deletions required so that the given condition is satisfied.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 3\cdot 10^5$
- $0 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
4
2 2 2 2
5
3 4 3 4 4
5
1 2 3 4 0
6
5 5 5 6 6 6
```

**Output**

```text
0
2
3
3
```

**Explanation**

**Test case $1$:** The given array already satisfies the condition, no deletions need to be done.

**Test case $2$:** Chef can delete both the $3$'s to make the array $[4, 4, 4]$, which satisfies the condition.

**Test case $3$:** Chef can use three moves as follows:
- Delete the $1$, the array is now $[2, 3, 4, 0]$.
- Delete the $4$, the array is now $[2, 3, 0]$.
- Delete the $0$, the array is now $[2, 3]$ which satisfies the condition.

It can be verified that using two or less deletions cannot give an array that satisfies the condition.

**Test case $4$:** Chef must either delete all the $5$'s or all the $6$'s.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
2 2 2 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5
3 4 3 4 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 4 0
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
6
5 5 5 6 6 6
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

[Practice](https://www.codechef.com/problems/DELXORONE)

[Contest: Division 1](https://www.codechef.com/START63A/problems/DELXORONE)

[Contest: Division 2](https://www.codechef.com/START63B/problems/DELXORONE)

[Contest: Division 3](https://www.codechef.com/START63C/problems/DELXORONE)

[Contest: Division 4](https://www.codechef.com/START63D/problems/DELXORONE)

***Author & Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

***Testers:*** [Takuki Kurokawa](https://www.codechef.com/users/tabr), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

#
[](#difficulty-2)DIFFICULTY:

1516

#
[](#prerequisites-3)PREREQUISITES:

Frequency arrays

#
[](#problem-4)PROBLEM:

Given an array A, find the minimum number of elements that need to be deleted from it so that the pairwise xor of any two elements in the resulting array is \leq 1.

#
[](#explanation-5)EXPLANATION:

For each 0 \leq x \leq N, let freq(x) denote the frequency of x in A, i.e, the number of times it occurs. We’ll use this later.

First, let’s find out what the final array can look like.

Suppose it contains two elements x and y. Then, the condition tells us that either x\oplus y = 0 or x\oplus y = 1.

- If x\oplus y = 0, then the only possibility is that y = x.

- If x\oplus y = 1, then the only possibility is that y = x \oplus 1.

So, if the final array contains x, the only elements it can contain are x and x\oplus 1.

Suppose we fix x. Then, our only option is to delete every element that is not x or x\oplus 1.

Recall the frequency array we initially constructed: it tells us that the number of such elements is exactly N - freq(x) - freq(x\oplus 1).

The final answer is hence simply the minimum value of (N - freq(x) - freq(x\oplus 1)) across all 0 \leq x \leq N, which can be easily found by just iterating across x once freq has been precomputed.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<int> freq(n+10);
		for (int i = 0; i < n; ++i) {
			int x; cin >> x;
			++freq[x];
		}
		int ans = n - 1;
		for (int i = 0; i <= n; ++i) {
			ans = min(ans, n - freq[i] - freq[i^1]);
		}
		cout << ans << '\n';
	}
}
``

</details>
