# String Operations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STROPERS |
| Difficulty Rating | 2220 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [STROPERS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/STROPERS) |

---

## Problem Statement

Two strings $A$ and $B$ are *equivalent* (denoted by $A \sim B$) if they have the same lengths and $A$ can be transformed into $B$ by performing the following operation zero or more times: choose a substring of $A$ which contains '1' an even number of times and reverse this substring.

You are given a binary string $S$. Find the number of different equivalence classes of the substrings of this string. In other words, find the smallest possible size of a set $\mathcal{C}$ of binary strings with the following property: for each non-empty string $R$ which is a substring of $S$ (including $S$ itself), there is a string $X \in \mathcal{C}$ such that $R \sim X$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$ with length $N$.

### Output
For each test case, print a single line containing one integer ― the number of equivalence classes among the substrings of the given string.

### Constraints
- $1 \le T \le 10$
- $1 \le N \le 1,000$
- $S$ contains only characters '0' and '1'

### Subtasks
**Subtask #1 (10 points):** $N \le 10$

**Subtask #2 (90 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
10
00000
10001
10101
01111
11001
01101
10110
10010
10111
11001
```

**Output**

```text
5
11
8
9
12
10
10
11
11
12
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
00000
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
10001
```

**Output for this case**

```text
11
```



#### Test case 3

**Input for this case**

```text
10101
```

**Output for this case**

```text
8
```



#### Test case 4

**Input for this case**

```text
01111
```

**Output for this case**

```text
9
```



#### Test case 5

**Input for this case**

```text
11001
```

**Output for this case**

```text
12
```



#### Test case 6

**Input for this case**

```text
01101
```

**Output for this case**

```text
10
```



#### Test case 7

**Input for this case**

```text
10110
```

**Output for this case**

```text
10
```



#### Test case 8

**Input for this case**

```text
10010
```

**Output for this case**

```text
11
```



#### Test case 9

**Input for this case**

```text
10111
```

**Output for this case**

```text
11
```



#### Test case 10

**Input for this case**

```text
11001
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/STROPERS)

[Div1](https://www.codechef.com/DEC20A/problems/STROPERS)

[Div2](https://www.codechef.com/DEC20B/problems/STROPERS)

**Setter:**  [Anton Trygub](https://www.codechef.com/users/anton_trygub)

**Tester:**  [Alexander Morozov](https://www.codechef.com/users/scanhex)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

### DIFFICULTY:

MEDIUM

### PREREQUISITES:

Good observation skills

### PROBLEM:

In this problem, we deal with binary strings (i.e strings containing only  0's and 1's) .

Two strings A and B are said to be equivalent (i.e A \sim B) if their lengths are equal and A can be transformed to B by performing the given operation 0 or more times:

- Choose a substring of A containing even number of 1's and reverse it.

For a given binary string S, we need to find the total number of equivalence classes for all the substrings of S . In other words, we need to get the set of binary strings \mathcal{C} with smallest possible size such that for any substring R of S, there exists a string X \in \mathcal{C} such that R \sim X .

### QUICK EXPLANATION:

-

For every substring X of given S, store the following length(X), number\_of\_ones(X)  and the number of positions i (where 1 \leq i \leq length(X))  of X where

(X[1] +X[2]+... + X[i])  \bmod 2 = 1  .

-

The number of such unique triples is the answer. We can solve this easily in O(N^2*\log(N)) by using sets where N is the length of string S .

### EXPLANATION:

The first thing to note is that if for two strings A and B we have A \sim B, then A and B must belong to the same equivalence class. Now let us find some observations related to equivalent strings which help us solve the problem easily:

-

**Observation 1 : ** If A \sim B, then B \sim A

This must be clearly visible since if we can perform some operations to convert A to B, we can reverse those sequence of operations to convert B to A .

-

**Observation 2 : ** If A \sim B, then length(A) = length(B) and the number of 1's in A and B are same.

-

**Observation 3 : ** If A \sim B, then cnt_A = cnt_B where cnt_S for a string S is defined as follows:

cnt_S = \{ Number of positions i where 1 \leq i \leq length(S) and (\sum_{j = 1}^{i} S_j) \bmod 2 = 1 \}

The last observation is the most crucial observation. Let us prove it.

Proof

Since A \sim B, we must must have some sequence of k \ge 0 operations op_1, op_2, ..., op_k   to convert A to B. If we are able to prove that applying the operation once on any substring of A satisfying the given criteria leads to a string  X with cnt_A = cnt_X, the value of cnt_A will be preserved after applying every operation and hence we are done with the proof.

For proving this, let us consider some notations for a string S with length N :

-

pref_S[i]= (\sum_{j = 1}^{i} S_j) \bmod 2

-

sum_S(l, r) = (\sum_{j = l}^{r} S_j) \bmod 2

Let  us re-define cnt_S(l, r) = \{ Number of positions i where l \leq i \leq r and  pref[i]=1\}

Now suppose we have applied operation on substring of S from l to r where 1 \leq l \leq r \leq N to convert S to T . We need to prove cnt_S(1, N) = cnt_T(1, N).

Since there are even number of ones from l to r, sum_S(l, r)=sum_T(l, r)= 0 .

We have pref_S[i] = pref_T[i]  for 1 \leq i \lt l  since that portion of the string is unchanged. Thus, cnt_S(1,l-1) = cnt_T(1, l-1) .

**Note: All the additions done on arrays pref and sum are performed modulo 2** .

We also have pref_S[i] = pref_T[i] for r \lt i \leq N. This is because

pref_T[i] = pref_T[l-1] + sum_T(l,r) +sum_T(r+1,i)

\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = pref_S[l-1] + sum_T(l,r) +sum_S(r+1,i)

\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = pref_S[l-1] + 0 +sum_S(r+1,i)

\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = pref_S[l-1] + sum_S(l,r) +sum_S(r+1,i)

\ \ \ \ \ \ \ \ \ \ \ \ \ \ \  = pref_S[i]

Thus cnt_S(r+1, N) = cnt_T(r +1 , N) .

If we are able to prove cnt_S(l, r) = cnt_T(l, r) then

cnt_S(1, N) = cnt_S(1, l-1) + cnt_S(l, r) + cnt_S(r+1, N)

 \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \  \ \  = cnt_T(1, l-1) + cnt_T(l, r) + cnt_T(r+1, N)

 \ \ \ \ \ \ \ \ \ \ \  \ \ \ \ \ \  \ \  = cnt_T(1, N)

which is exactly what we want.

First, note that for any l \leq i \leq  r where S[i] = 0 and sum(l, r) = 0, we will definitely have

sum_S(l, i) = sum_S(i, r) .

Let the number of 1's from l to r be x.

Now, we will have exactly x/2 positions in l \leq i \leq r having S[i] = 1  and  pref_S[i] = 1 (think why this is true) . The same thing follows for string T also.

Also, for each position i from l to r where S[i] =0, we have

pref_S[i] = pref_S[l-1]+sum_S(l, i)

 \ \ \ \ \ \ \ \ \ \ \ \ \ \ =pref_T[l -1] + sum_S(i, r)

\ \ \ \ \ \ \ \ \ \ \ \ \ \ = pref_T[l -1] + sum_T(l, r-i+l) = pref_T[r-i+l].

This implies that for every position i in S where S[i]=0, we will have a unique position

j = r-i+l in T  such that T[j] = 0 and pref_S[i]=pref_T[j] .

Based on this observations, we can conclude cnt_S(l,r)=cnt_T(l, r) and

hence cnt_S(1,N)= cnt_T(1,N) .

**This completes the proof.**

Now, I claim that if two strings A and B satisfy length(A) = length(B), number\_of\_ones(A) = number\_of\_ones(B) and cnt_S = cnt_T, then A \sim B .

The first two conditions are obvious, but the third condition isn’t. Here is the proof for it.

Proof

The main idea of proving it is to show there exists a string S such that A \sim S and B \sim S. Then A \sim B .

Let the number of 1's in A and B be equal to x .

Do the following sequence of operations on A:

-

Start from i=1

-

If  A[i] = 1, then increment i

-

Else find an index j such that A[j]=1 and the number of 1's in A[l,...,r] is even and reverse that substring. If there is so such j, then stop the process.

Here is an example:

Suppose A= 01010110, we do the following :

**0101**0110 \to 1**01001**10 \to 11**00101**0 \to 11101000

After performing these series of operations, it is guaranteed that the resultant string say A' has x-1 ones at the positions from 1 to x-1 (beginning of the string) and the remaining 1 at such a position that cnt_A=cnt_{A'} (there could be only one such position) . Similarly, B is converted to B' by performing these series of operations on B . Also cnt_B=cnt_{B'} . SInce we have initially assumed that cnt_A = cnt_B, we get cnt_{A'} = cnt_{B'} and thus the last 1 will be at the same location in A' and B' . Hence A \sim B.

Therefore, given a binary string S, we can evaluate for each substring X of S the following 3 parameters length(S), number\_of\_ones(X), cnt_X and the number of these unique triples is the answer. We can evaluate this easily (for example by using a set) .

### TIME COMPLEXITY:

O(N^2 \cdot \log(N)) ( where N is the length of string S \ ) for each testcase if set is used (see solution code). This can be optimised to O(N^2) is we use hash set but that is not required.

### SOLUTION:

Editorialist's solution
``#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string s;
		cin >> s;
		int n = s.size();
		//length count_of_ones count_of_positions_of_odd_parity_sum
		set<tuple<int, int, int>> classes;
		for (int i = 0; i < n; i++)
		{
			int ones = 0;
			int cnt = 0;
			for (int j = i; j < n; j++)
			{
				if (s[j] == '1')
					ones++;
				if (ones & 1)
					cnt++;
				classes.insert(make_tuple(j - i + 1, ones, cnt));
			}
		}
		cout << classes.size() << endl;
	}
}
``

Setter's solution
``#include <cmath>
#include <functional>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <math.h>
#include <random>
#include <deque>
#include <queue>
#include <cassert>
#include <unordered_map>
#include <unordered_set>
#include <iomanip>
#include <bitset>
#include <sstream>
#include <chrono>
#include <cstring>

using namespace std;

typedef long long ll;

#ifdef iq
mt19937 rnd(228);
#else
mt19937 rnd(chrono::high_resolution_clock::now().time_since_epoch().count());
#endif

int main()
{
#ifdef iq
    freopen("a.in", "r", stdin);
#endif
    ios::sync_with_stdio(0);
    cin.tie(0);
    int _t;
    cin >> _t;
    while (_t--)
    {
        string s;
        cin >> s;
        set<pair<int, pair<int, int>>> q;
        for (int i = 0; i < (int)s.size(); i++)
        {
            string t = s.substr(i);
            int cnt = 0, sum = 0;
            for (int j = 0; j < (int)t.size(); j++)
            {
                if (t[j] == '1')
                {
                    cnt++;
                    sum = -sum + j;
                }
                q.insert({cnt, {sum, j}});
            }
        }
        cout << q.size() << '\n';
    }
}
``

# VIDEO EDITORIAL:

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
