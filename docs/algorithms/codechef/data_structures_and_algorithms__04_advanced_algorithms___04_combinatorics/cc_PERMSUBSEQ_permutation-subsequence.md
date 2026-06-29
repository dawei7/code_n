# Permutation Subsequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERMSUBSEQ |
| Difficulty Rating | 1519 |
| Difficulty Band | Combinatorics |
| Path | Data Structures and Algorithms |
| Lesson | Conceptual Problems |
| Official Link | [PERMSUBSEQ](https://www.codechef.com/learn/course/combinatorics/COMBI05/problems/PERMSUBSEQ) |

---

## Problem Statement

Chefina has an array $A$ consisting of $N$ positive integers.

A permutation subsequence of length $M$ is a subsequence that represents a permutation of length $M$.

Now, Chefina asks Chef to find the count of permutation subsequences in array $A$.
The count can be very large, so output it modulo $1000000007$ $(10^9 + 7)$.

As a reminder:
- A subsequence of an array is obtained by deleting some (possibly zero) elements from the array without changing the order of the remaining elements.
- A permutation of length $M$ is an array of length $M$ in which every element from $1$ to $M$ occurs exactly once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the length of array $A$.
    - The next line contains $N$ space-separated integers, the elements of the array $A$.

---

## Output Format

For each test case, output on a new line, the count of permutation subsequences in array $A$, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 2\cdot 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^9 $
- Sum of $N$ over all test cases does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5
1 2 3 2 4
6
1 3 5 8 9 8
```

**Output**

```text
7
1
```

**Explanation**

**Test case $1$:** Chef can get $7$ permutation subsequences:
$[1]$ , $[1, 2]$ , $[1, 2]$ , $[1, 2, 3]$ , $[1, 3, 2]$ , $[1, 2, 3, 4]$ , $[1, 3, 2, 4]$.

**Test case $2$:** Chef can get $1$ permutation subsequence:
$[1]$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 2 4
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
6
1 3 5 8 9 8
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

[Practice](https://www.codechef.com/problems/PERMSUBSEQ)

[Contest: Division 1](https://www.codechef.com/START80A/problems/PERMSUBSEQ)

[Contest: Division 2](https://www.codechef.com/START80B/problems/PERMSUBSEQ)

[Contest: Division 3](https://www.codechef.com/START80C/problems/PERMSUBSEQ)

[Contest: Division 4](https://www.codechef.com/START80D/problems/PERMSUBSEQ)

***Author:*** [anky_301](https://www.codechef.com/users/anky_301)

***Testers:*** [wuhudsm](https://www.codechef.com/users/wuhudsm), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A of size N, count the number of its subsequences that are permutations.

#
[](#explanation-5)EXPLANATION:

Let’s count permutations of length 1, 2, 3, \ldots, N separately and add them up.

For a permutation of length K, we need to:

- Choose exactly one 1

- Choose exactly one 2

- Choose exactly one 3

\vdots

- Choose exactly one K

There are no further restrictions, since the order of the chosen elements doesn’t matter.

In particular, if there are \text{freq}[i] occurrences of element i in the array, then the number of ways to do the above is simply \text{freq}[1] \times \text{freq}[2] \times \text{freq}[3] \times \ldots \times \text{freq}[K] = \prod_{i=1}^K \text{freq}[i].

Adding this up for all K, our final answer is thus

\sum_{K=1}^N \left(\prod_{i=1}^K \text{freq}[i]\right)

After computing the frequency array, this value is easy to compute in \mathcal{O}(N^2) time.

To optimize it, note that that we’re essentially taking prefix *products* of the \text{freq} array, and all of those can be computed in \mathcal{O}(N) time total once \text{freq} is known, thus solving the problem in \mathcal{O}(N).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (Python)
``for test_cases in range(int(input())):
    n = int(input())
    l = list(map(int , input().split()))
    m = 1000000007
    d = {}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    x = 1
    c = 0
    p = 1
    while (x in d) and d[x]>0:
        cur = ((p%m )*(d[x]%m))%m
        c += cur
        p = cur
        c = c%m
        x+=1
    print(c)
``

Tester's code (C++)
``#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
typedef double db;
typedef long long ll;
typedef unsigned long long ull;
const int N=1000010;
const int LOGN=28;
const ll  TMD=1000000007;
const ll  INF=2147483647;
int T,n;
ll  ans,cur;
int cnt[N];

int main()
{
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(int i=1;i<=n;i++) cnt[i]=0;
		for(int i=1;i<=n;i++)
		{
			int t;
			scanf("%d",&t);
			if(t<=n) cnt[t]++;
		}
		ans=0;cur=1;
		for(int i=1;i<=n;i++) cur=(cur*cnt[i])%TMD,ans=(ans+cur)%TMD;
		printf("%lld\n",ans);
	}

	return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    freq = [0]*(n+1)
    for x in map(int, input().split()):
        if x <= n: freq[x] += 1
    cur, ans = 1, 0
    for i in range(1, n+1):
        cur = (cur * freq[i]) % mod
        ans += cur
    print(ans % mod)
``

</details>
