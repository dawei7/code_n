# Good Sequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GSEQ |
| Difficulty Rating | 2451 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [GSEQ](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/GSEQ) |

---

## Problem Statement

Suppose you have a **binary** array $B$ of length $N$.
A sequence $x_1, x_2, \ldots, x_k$ is called *good* with respect to $B$ if it satisfies the following conditions:
- $1 \leq x_1 \lt x_2 \lt \ldots \lt x_k \leq N+1$
- For *every* pair $(i, j)$ such that $1 \leq i \lt j \leq k$, the subarray $B[x_i: x_j-1]$ contains $(j-i)$ more ones than zeros.
    - That is, if $B[x_i : x_j-1]$ contains $c_1$ ones and $c_0$ zeros, then $c_1 - c_0 = j-i$ must hold.

Here, $B[L: R]$ denotes the subarray consisting of elements $[B_L, B_{L+1}, B_{L+2}, \ldots, B_R]$.
Note that in particular, a sequence of size $1$ is always *good*.

For example, suppose $B = [0,1,1,0,1,1]$. Then,
- The sequence $[1,4,7]$ is a *good* sequence. The subarrays that need to be checked are $B[1:3], B[1:6]$ and $B[4:6]$, which all satisfy the condition.
- The sequence $[1, 5]$ is not *good*, because $B[1:4] = [0, 1, 1, 0]$ contains an equal number of zeros and ones (when it should contain one extra $1$).

Alice gave Bob a binary array $A$ of size $N$ and asked him to find the **longest** sequence that is *good* with respect to $A$. Help Bob find one such sequence.
If multiple possible longest sequences exist, you may print **any** of them.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the binary array.
    - The second line contains $N$ space-separated numbers — $A_1 , A_2 , \ldots , A_N$.

---

## Output Format

Each test case requires two lines of output:
- First, print on a new line a single integer $K$ — the maximum length of a sequence that is good with respect to $A$
- On the next line, print $K$ space-separated integers in **increasing order**, denoting the indices of one such sequence.

If there are multiple possible good sequences with maximum size, output any of them.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 1$
- The sum of $N$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
6
0 1 1 0 1 1
5
0 1 0 1 0
4
1 1 1 1
3
1 0 0
```

**Output**

```text
4
2 5 6 7
2
4 5
5
1 2 3 4 5
2
1 2
```

**Explanation**

**Test case $1$:** We have $A = [0, 1, 1, 0, 1, 1]$. The sequence $[2, 5, 6, 7]$ requires us to check $6$ subarrays:
- $A[2:4] = [1, 1, 0]$ which has $c_1 - c_0 = 1$ and corresponds to $i = 1, j = 2$
- $A[2:5] = [1, 1, 0, 1]$ which has $c_1 - c_0 = 2$ and corresponds to $i = 1, j = 3$
- $A[2:6] = [1, 1, 0, 1, 1]$ which has $c_1 - c_0 = 3$ and corresponds to $i = 1, j = 4$
- $A[5:5] = [1]$, which has $c_1 - c_0 = 1$ and corresponds to $i = 2, j = 3$
- $A[5:6] = [1, 1]$, which has $c_1 - c_0 = 2$ and corresponds to $i = 2, j = 4$
- $A[6:6] = [1]$, which has $c_1 - c_0 = 1$ and corresponds to $i = 3, j = 4$

As you can see, all $6$ pairs satisfy the condition.

**Test case $2$:** The only subarray that needs to be checked is $A[4:4] = [1]$, which has $c_1 - c_0 = 1$ as needed. It can be verified that no good sequence of length greater than $2$ exists.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GSEQ)

[Contest: Division 1](https://www.codechef.com/START72A/problems/GSEQ)

[Contest: Division 2](https://www.codechef.com/START72B/problems/GSEQ)

[Contest: Division 3](https://www.codechef.com/START72C/problems/GSEQ)

[Contest: Division 4](https://www.codechef.com/START72D/problems/GSEQ)

***Authors:*** [still_me](https://www.codechef.com/users/still_me), [iceknight1093](https://www.codechef.com/users/IceKnight1093)

***Testers:*** [the_hyp0cr1t3](https://www.codechef.com/users/the_hyp0cr1t3), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Prefix sums, dynamic programming

#
[](#problem-4)PROBLEM:

Given a binary array A, find the longest *good* sequence x_1, x_2, \ldots, x_k such that it satisfies:

- 1 \leq x_1 \lt x_2 \lt \ldots \lt x_k \leq N+1

-
A[x_i:x_j-1] contains an equal number of zeros and ones for each i \lt j.

#
[](#explanation-5)EXPLANATION:

First, note that it’s enough to ensure that A[x_i:x_{i+1}-1] (i.e, the subarray between consecutive elements) satisfies the condition, i.e, contains an extra one.

Proof

This is not hard to see.

The subarray A[x_i:x_j-1] can be thought of as the concatenation of A[x_i:x_{i+1}-1], A[x_{i+1}:x_{i+2}-1], \ldots, A[x_{j-1}, x_j-1]. Note that there are j-i such subarrays.

If each of these contains an extra one, of course all together the number of extra ones will be exactly j-i.

Now, let’s use a small trick: replace every 0 in the array with -1. Let’s call the array obtained this way as B.

For example, if A = [0, 1, 1, 0, 1] then B = [-1, 1, 1, -1, 1].

Notice that "A[L:R] contains an extra one" translates to "B[L:R] has a sum of 1" in the new array, which is much easier to deal with!

Since we’re dealing with subarray sums, it’s natural to think of prefix sums.

So, let P_i = B_1 + B_2 + \ldots + B_i (with P_0 = 0) denote the prefix sum array of B.

Now, for B[L:R] to have a sum of 1, we must have P_R - P_{L-1} = 1, or P_R = P_{L-1} + 1.

Applying this to the definition of a good sequence, we see that we must have P_{x_{i+1}-1} = P_{x_i-1} + 1 for every 1 \leq i \lt k.

In other words, we need to choose a sequence of indices whose prefix sums are k, k+1, k+2, \ldots for some value of k.

The longest good sequence thus corresponds to the longest sequence of prefix sums of this form.

This can be computed using dynamic programming.

Let dp_i denote the length of the longest sequence of prefix sums ending at position i that satisfies the above condition.

Transitions for a given index are quite easy to compute in \mathcal{O}(N). We simply have dp_i = 1 + \max (dp_j) across all j \lt i such that P_j+1 = P_i.

However, doing this \mathcal{O}(N) computation for each index is too slow, we need to speed it up a bit.

This can be done by noting that we only care about those indices whose P_j values equal P_i - 1; in fact, we only care about the maximum dp_j value among these indices.

So, let’s keep another array \text{mx}, where \text{mx}[x] is the largest value of dp_i across all indices i such that P_i = x. Initially, initialize it to all zeros.

Then, for each i from 0 to N,

- dp_i = 1 + \text{mx}[P_i]

- \text{mx}[P_i] = \max(dp_i, \text{mx}[P_i])

The maximum element of dp is the final answer.

Reconstructing a valid sequence is not hard, when performing the dp keep a link to the previous element in the sequence, then follow these in reverse at the end.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (C++)
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
		vector<int> a(n);
		for (int i = 0; i < n; ++i) cin >> a[i];
		vector<int> difs = {0};
		for (int i = 0; i < n; ++i) {
			if (a[i] == 1) difs.push_back(difs[i] + 1);
			else difs.push_back(difs[i] - 1);
		}

		map<int, int> len, last;
		vector<int> link(n+1, -1), ending_at(n+1);
		for (int i = 0; i <= n; ++i) {
			int cur = len[difs[i]-1] + 1;
			ending_at[i] = cur;
			if (cur > 1) link[i] = last[difs[i] - 1];

			len[difs[i]] = cur;
			last[difs[i]] = i;
		}
		int ans = *max_element(begin(ending_at), end(ending_at));
		cout << ans << '\n';
		for (int i = n; i >= 0; --i) {
			if (ending_at[i] != ans) continue;
			vector<int> pos;
			int cur = i;
			while (1) {
				pos.push_back(cur);
				if (link[cur] == -1) break;
				cur = link[cur];
			}
			reverse(begin(pos), end(pos));
			for (int x : pos) cout << x+1 << ' ';
			cout << '\n';
			break;
		}
	}
}
``

</details>
