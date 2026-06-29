# Triplets Min

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRIPLETMIN |
| Difficulty Rating | 1868 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [TRIPLETMIN](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/TRIPLETMIN) |

---

## Problem Statement

You are given an integer array $A$ of size $N$.
A *triplet array* is defined as the collection of $\min(A_i,A_j,A_k)$ for all triplets $(i,j,k)$, where $1\le i\lt j\lt k\le N$.

You are given $Q$ queries of the following type:
- Given an integer $K$, return the value of $K^{th}$ **smallest** element in the *triplet array*.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $Q$ — the size of array $A$ and the number of queries, respectively.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$.
    - The following $Q$ lines describe the queries. Each of these lines contain a single positive integer $K$.

---

## Output Format

For each query, print a single line containing the $K^{th}$ **smallest** element in the *triplet array*.

---

## Constraints

- $1 \leq T \leq 1000$
- $3 \leq N \leq 3\cdot 10^5$
- $1 \leq Q \leq 3\cdot 10^5$
- $-10^{9} \leq A_i \leq 10^{9}$
- $1 \leq K \leq \binom{N}{3}$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.
- The sum of $Q$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
6 2
3 3 3 3 3 3
18
1
4 4
2 4 2 1
1
2
3
4
```

**Output**

```text
3
3
1
1
1
2
```

**Explanation**

**Test case 1:** Here, all elements of triplet array are equal to $3$.

**Test case 2:** The sorted triplet array is $[1, 1, 1, 2]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TRIPLETMIN)

[Contest: Division 1](https://www.codechef.com/START97A/problems/TRIPLETMIN)

[Contest: Division 2](https://www.codechef.com/START97B/problems/TRIPLETMIN)

[Contest: Division 3](https://www.codechef.com/START97C/problems/TRIPLETMIN)

[Contest: Division 4](https://www.codechef.com/START97D/problems/TRIPLETMIN)

***Author:*** [grayhathacker](https://www.codechef.com/users/grayhathacker)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1868

# [](#prerequisites-3)PREREQUISITES:

Binary search, prefix sums

# [](#problem-4)PROBLEM:

For an array A of length N, the multiset S = \{\min(A_i, A_j, A_j) \mid 1 \leq i \lt j \lt k \leq N\}  is called its *triplet array*.

You’re given an array A and Q queries.

For each query, given an integer K, output the K-th smallest element of the triplet array of A.

# [](#explanation-5)EXPLANATION:

First, let’s attempt to answer a single query reasonably quickly.

Let’s sort A, so that A_1 \leq A_2 \leq \ldots \leq A_N. This doesn’t change the triplet array.

Then, we have the following:

- There are \binom{N-1}{2} pairs whose minimum value is A_1 (pick two distinct indices out of (2, 3, 4, \ldots, N).

- There are \binom{N-2}{2} pairs whose minimum value is A_2 (pick two distinct indices out of (3, 4, \ldots, N).

\vdots

- There are \binom{N-i}{2} pairs whose minimum value is A_i, for any i.

This already gives us an algorithm in \mathcal{O}(N) to solve for a single K: all we need to do is find the smallest i such that

\binom{N-1}{2} + \binom{N-2}{2} + \ldots + \binom{N-i}{2} \geq K

and we know that the answer is A_i.

To speed this up, we can use binary search and prefix sums.

In particular, let P_i = \binom{N-1}{2} + \binom{N-2}{2} + \ldots + \binom{N-i}{2} be the prefix sums of the counts we calculated above.

For a fixed K, we want to find the smallest i such that P_i \geq K.

Since P_i \lt P_{i+1} for all i, this can be done by just binary searching on the P array!

Now we’re able to answer a single query in \mathcal{O}(\log N) time with \mathcal{O}(N) precomputation.

Since the precomputation remains the same across all queries, this gives us a fairly simple solution in \mathcal{O}(N + Q\log N), which is enough to get AC.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N + Q\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int, char> msi;
typedef pair<int, int> pa;
typedef long long int ll;

ll n, q, i, a[300005], cnt[300005], k;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
#ifndef ONLINE_JUDGE
	freopen("inputf.in", "r", stdin);
	// freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;
	while (t--)
	{
		cin >> n >> q;
		for (i = 0; i < n; i++)
			cin >> a[i];
		sort(a, a + n);
		for (i = 0; i < n; i++)
		{
			cnt[i] = (n - i - 1) * (n - i - 2) / 2;
			if (i > 0)
				cnt[i] += cnt[i - 1];
		}
		while (q--)
		{
			cin >> k;
			cout << a[lower_bound(cnt, cnt + n, k) - cnt] << "\n";
		}
	}

	return 0;
}
``

Tester's code (C++)
``/*...................................................................*
 *............___..................___.....____...______......___....*
 *.../|....../...\........./|...../...\...|.............|..../...\...*
 *../.|...../.....\......./.|....|.....|..|.............|.../........*
 *....|....|.......|...../..|....|.....|..|............/...|.........*
 *....|....|.......|..../...|.....\___/...|___......../....|..___....*
 *....|....|.......|.../....|...../...\.......\....../.....|./...\...*
 *....|....|.......|../_____|__..|.....|.......|..../......|/.....\..*
 *....|.....\...../.........|....|.....|.......|.../........\...../..*
 *..__|__....\___/..........|.....\___/...\___/.../..........\___/...*
 *...................................................................*
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1000000000000000000
#define MOD 1000000007

void solve(int tc)
{
    int n,q;
    cin >> n >> q;
    int a[n];
    for(int i=0;i<n;i++)
        cin >> a[i];
    sort(a,a+n);
    int pre[n];
    for(int i=0;i<n;i++)
        pre[i]=(n-i-1)*(n-i-2)/2;
    for(int i=1;i<n;i++)
        pre[i]+=pre[i-1];
    while(q--)
    {
        int k;
        cin >> k;
        cout << a[lower_bound(pre,pre+n,k)-pre] << '\n';
    }
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc=1;
    cin >> tc;
    for(int ttc=1;ttc<=tc;ttc++)
        solve(ttc);
    return 0;
}
``

Editorialist's code (Python)
``from bisect import bisect_right
def C2(x):
    return x * (x-1) // 2

for _ in range(int(input())):
    n, q = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    counts = []
    for i in range(n): counts.append(C2(n-1-i))
    for i in range(1, n): counts[i] += counts[i-1]

    for i in range(q):
        k = int(input())
        pos = bisect_right(counts, k-1)
        print(a[pos])
``

</details>
