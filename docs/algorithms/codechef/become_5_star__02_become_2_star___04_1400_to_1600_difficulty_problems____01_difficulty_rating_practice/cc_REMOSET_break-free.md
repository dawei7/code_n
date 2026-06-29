# Break Free

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMOSET |
| Difficulty Rating | 1612 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [REMOSET](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/REMOSET) |

---

## Problem Statement

*This is the part when I say I don't want ya \
I'm stronger than I've been before \
This is the part when I break free \
'Cause I can't resist it no more*

Chef has an array $A$ of length $N$.

Let $B$ denote the array obtained by removing any **non-empty** subset of **indices** from the array $A$.
The removal of subset of indices is said to be *good* if:
- Sum of the subarray $B[i, j]$ is divisible by $2$ for all pairs of indices $(1 \leq i \leq j \leq |B|)$.

Find the number of *good* removals. Since the answer can be huge, print it modulo $10^9 + 7$.

**Note:**
- The sum of an empty array is $0$, which is divisible by $2$.
- $B[i, j]$ denotes the subarray $[B_i, B_{i+1}, \ldots, B_j]$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$, the length of the array.
    - The next line contains $N$ space-separated integers, denoting the elements of the array.

---

## Output Format

For each test case, output on a new line, total number of *good* removals modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_{i} \leq 2 \cdot 10^5$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
3
2 1 4
3
1 2 3
```

**Output**

```text
4
2
```

**Explanation**

**Test case $1$:** There are $4$ *good* removals.
- Remove subset $\{2\}$. Final array: $[2,4]$.
- Remove subset $\{1,2,3\}$. Final array: $[]$.
- Remove subset $\{2,3\}$. Final array: $[2]$.
- Remove subset $\{1,2\}$. Final array: $[4]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 1 4
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REMOSET)

[Contest: Division 1](https://www.codechef.com/START93A/problems/REMOSET)

[Contest: Division 2](https://www.codechef.com/START93B/problems/REMOSET)

[Contest: Division 3](https://www.codechef.com/START93C/problems/REMOSET)

[Contest: Division 4](https://www.codechef.com/START93D/problems/REMOSET)

***Author:*** [likhon5](https://www.codechef.com/users/likhon5)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1612

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics

#
[](#problem-4)PROBLEM:

You’re given an array A. Find the number of non-empty subsets of indices whose removal results in every subarray having even sum.

#
[](#explanation-5)EXPLANATION:

Suppose we removed some indices, and the array satisfies the given condition, i.e, \displaystyle\sum_{k=i}^j A_k is even, for each 1 \leq i \leq j \leq |A|.

Then, in particular this holds for i = j, which means every element must itself be even.

Of course, if every element is even then every subarray sum is also even; so we’ve reduced our problem to counting the number of ways of removing indices such that all remaining elements are even.

That’s not too hard:

- First, *all* odd elements must be removed.

- Suppose this leaves K even elements. We can then choose any subset of them to remove, for 2^K possible ways.

There’s one edge case: since the statement asks for **non-empty** subsets, if K = N (i.e all elements of the original array are even), the answer is 2^N - 1; since we can’t choose the empty subset.

Since K \leq N, computing 2^K can be done by just repeated multiplication using a loop.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
#define endl '\n'
#define filein freopen("input20.in","r",stdin)
#define fileout freopen("output20.out","w",stdout)
#define fast ios_base::sync_with_stdio(false); cin.tie(NULL)
using namespace std;
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
const int mx=2e5+9;
const int mod=1e9+7;
int main()
{
    fast;
    int t; cin>>t;
    assert(t<=10000);
    int total=0;
    while(t--)
    {
        int n; cin>>n;
        total+=n;
        int odd=0,even=0;
        for(int i=0;i<n;i++)
        {
            int x; cin>>x;
            assert(x>=0 and x<=200000);
            if(x%2) odd++;
            else even++;
        }
        long long cnt=1;
        for(int i=1;i<=even;i++) cnt=(cnt*2)%mod;
        if(odd) cout<<cnt<<endl;
        else cout<<cnt-1<<endl;
    }
    assert(total<=200000);
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    evens = 0
    for x in a: evens += (x+1)%2
    ans = pow(2, evens, mod)
    if evens == n: ans -= 1
    print(ans%mod)
``

</details>
