# Frequency Array Retrieval

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FREQARRRET |
| Difficulty Rating | 1654 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [FREQARRRET](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/FREQARRRET) |

---

## Problem Statement

Consider an array $A$ consisting of $N$ positive elements. The *frequency array* of $A$ is the array $B$ of size $N$ such that $B_i =$ *frequency* of element $A_i$ in $A$.

For example, if $A = [4, 7, 4, 11, 2, 7, 7]$, the *frequency array* $B = [2, 3, 2, 1, 1, 3, 3]$.

You have lost the array $A$, but fortunately you have the array $B$.
Your task is to construct the **lexicographically smallest** array $A$ such that:
- $1\le A_i \le 10^5$;
- The frequency array of $A$ is equal to $B$.

If no such array $A$ exists, print $-1$.

Note: Array $X$ is lexicographically smaller than array $Y$, if $X_i \lt Y_i$, where $i$ is the first index where $X$ and $Y$ differ.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the array.
    - The next line contains $N$ space-separated integers - $B_1, B_2, \ldots, B_N$, the frequency array.

---

## Output Format

For each test case, output on a new line, $N$ space separated integers - $A_1, A_2, \ldots, A_N$, the **lexicographically smallest** array $A$. If no such array $A$ exists, print $-1$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
5
5
2 3 3 3 2
5
1 1 1 1 1
5
5 5 5 5 5
3
1 2 4
8
1 3 2 3 2 2 2 3
```

**Output**

```text
1 2 2 2 1
1 2 3 4 5
1 1 1 1 1
-1
1 2 3 2 3 4 4 2
```

**Explanation**

**Test case $1$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 2, 2, 2, 1]$. The element $A_1$ and $A_5$ have frequency $2$ while $A_2, A_3,$ and $A_4$ have frequency $3$.

**Test case $2$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 2, 3, 4, 5]$. Each element in $A$ has frequency $1$.

**Test case $3$:** The lexicographically smallest array $A$ having the given frequency array $B$ is $A = [1, 1, 1, 1, 1]$. Each element in $A$ has frequency $5$.

**Test case $4$:** No possible array $A$ exists having the given frequency array.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
2 3 3 3 2
```

**Output for this case**

```text
1 2 2 2 1
```



#### Test case 2

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
1 2 3 4 5
```



#### Test case 3

**Input for this case**

```text
5
5 5 5 5 5
```

**Output for this case**

```text
1 1 1 1 1
```



#### Test case 4

**Input for this case**

```text
3
1 2 4
```

**Output for this case**

```text
-1
```



#### Test case 5

**Input for this case**

```text
8
1 3 2 3 2 2 2 3
```

**Output for this case**

```text
1 2 3 2 3 4 4 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FREQARRRET)

[Contest: Division 1](https://www.codechef.com/START70A/problems/FREQARRRET)

[Contest: Division 2](https://www.codechef.com/START70B/problems/FREQARRRET)

[Contest: Division 3](https://www.codechef.com/START70C/problems/FREQARRRET)

[Contest: Division 4](https://www.codechef.com/START70D/problems/FREQARRRET)

***Author:*** [munch_01](https://www.codechef.com/users/munch_01)

***Preparer:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1654

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given an array B. Find the lexicographically smallest array A such that B_i equals the frequency of A_i for every i; or report that no such array exists.

#
[](#explanation-5)EXPLANATION:

As with most tasks that require lexicographic minimization, this one can be solved greedily.

Let’s try to place the 1's, then the 2's, then the 3's, and so on.

Note that we can always set A_1 = 1.

Now, suppose B_1 = x. Then, there are exactly x-1 more 1's in A, and to minimize the final array, we must place them at the leftmost x-1 positions j such that B_j = x.

Then, we can find the first position \gt 1 that is unfilled, place a 2 there, and repeat the same process.

Note that at any step if we are unable to find enough positions to place elements, the answer is immediately -1.

In particular, any x must occur k\cdot x times in B (for some k \geq 0) for the answer to not be -1.

All that needs to be done is to implement this quickly.

Here’s one simple way to do this.

First, build the frequency table of B; let this be freq.

If freq[x] is not a multiple of x for some x, the answer is immediately -1; otherwise we’ll construct a valid array.

Also keep:

- A variable nxt. Initially, nxt = 1. This denotes the next smallest we are going to use.

- A second map, say cur, where cur[x] denotes the current value we’re placing that has frequency x.

Let’s iterate i from 1 to N. Suppose A_i = x. Then,

- If freq[x] is a multiple of x, we must start placing a new element. So, set cur[x] = nxt then increase nxt by 1.

- Then, set A_i = cur[x] and decrement freq[x] by 1.

It’s easy to see that the array constructed this way is the same one we discussed initially, since we increase cur[x] after placing exactly x instances of the previous value; and this is of course optimal.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) or \mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <iostream>
#include <map>

using namespace std;

map<int,int> F;
pair<int, int> M[100010];
int q, n, B[100010], poss, prev1;

int main()
{
	cin>>q;

	while(q--)
	{
		F.clear();
		poss = 1;
		prev1 = 0;
		cin>>n;
		int cnt = 0;
		for(int i=1;i<=n;i++)
		{
			cin>>B[i];
			F[B[i]]++;
			M[B[i]].first = 0;
			M[B[i]].second = 0;
		}

		for(auto it = F.begin(); it != F.end(); it++)
		{
			if( ((it->second)%(it->first))!=0 )
			{
				poss = 0;
				break;
			}
		}
		if(poss==0)
		{
			cout<<-1<<"\n";
			continue;
		}

		for(int i=1;i<=n;i++)
		{
			if( (M[B[i]].first == 0) || (M[B[i]].second == B[i]) )
			{
				prev1++;
				M[B[i]].first = prev1;
				M[B[i]].second = 1;
			}
			else
				M[B[i]].second++;
			cout<<M[B[i]].first;
			if(i<n)
				cout<<" ";
			else
				cout<<"\n";
		}
	}
}
``

Tester's code (C++)
``#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast,unroll-loops")

#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
const ll INF_MUL=1e13;
const ll INF_ADD=1e18;
#define pb push_back
#define mp make_pair
#define nline "\n"
#define f first
#define s second
#define pll pair<ll,ll>
#define all(x) x.begin(),x.end()
#define vl vector<ll>
#define vvl vector<vector<ll>>
#define vvvl vector<vector<vector<ll>>>
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
void _print(ll x){cerr<<x;}
void _print(char x){cerr<<x;}
void _print(string x){cerr<<x;}
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
template<class T,class V> void _print(pair<T,V> p) {cerr<<"{"; _print(p.first);cerr<<","; _print(p.second);cerr<<"}";}
template<class T>void _print(vector<T> v) {cerr<<" [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T>void _print(set<T> v) {cerr<<" [ "; for (T i:v){_print(i); cerr<<" ";}cerr<<"]";}
template<class T>void _print(multiset<T> v) {cerr<< " [ "; for (T i:v){_print(i);cerr<<" ";}cerr<<"]";}
template<class T,class V>void _print(map<T, V> v) {cerr<<" [ "; for(auto i:v) {_print(i);cerr<<" ";} cerr<<"]";}
typedef tree<ll, null_type, less<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
typedef tree<ll, null_type, less_equal<ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_multiset;
typedef tree<pair<ll,ll>, null_type, less<pair<ll,ll>>, rb_tree_tag, tree_order_statistics_node_update> ordered_pset;
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
const ll MOD=1e9+7;
const ll MAX=500500;
void solve(){
    ll n; cin>>n;

    map<ll,vector<ll>> track;
    vector<ll> b(n+5);
    for(ll i=1;i<=n;i++){
        cin>>b[i];
    }
    for(ll i=n;i>=1;i--){
        track[b[i]].push_back(i);
    }
    vector<ll> a(n+5,-1);
    ll cur=1;
    for(ll i=1;i<=n;i++){
        if(a[i]==-1){
            ll need=b[i];
            while(need--){
                if(track[b[i]].empty()){
                    cout<<"-1\n";
                    return;
                }
                auto it=track[b[i]].back();
                a[it]=cur;
                track[b[i]].pop_back();
            }
            cur++;
        }
    }
    for(ll i=1;i<=n;i++){
        cout<<a[i]<<" \n"[i==n];
    }
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=1;
    cin>>test_cases;
    while(test_cases--){
        solve();
    }
    cout<<fixed<<setprecision(10);
    cerr<<"Time:"<<1000*((double)clock())/(double)CLOCKS_PER_SEC<<"ms\n";
}
``

Editorialist's code (Python)
``import collections
for _ in range(int(input())):
	n = int(input())
	b = list(map(int, input().split()))
	freq = collections.Counter(b)
	curval = {}
	nxt = 1
	a = [-1]*n
	for i in range(n):
		if freq[b[i]]%b[i] == 0:
			curval[b[i]] = nxt
			nxt += 1
		if b[i] not in curval: break
		freq[b[i]] -= 1
		a[i] = curval[b[i]]
	if min(a) == -1: print(-1)
	else: print(*a)
``

</details>
