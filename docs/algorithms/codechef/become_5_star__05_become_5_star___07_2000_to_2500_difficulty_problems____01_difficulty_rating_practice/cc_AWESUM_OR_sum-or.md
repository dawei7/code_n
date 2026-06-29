# SUM OR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AWESUM_OR |
| Difficulty Rating | 2152 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [AWESUM_OR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/AWESUM_OR) |

---

## Problem Statement

You are given a positive integer $N$.
Find the number of triples $(X, Y, Z)$ such that:
- $0\lt X, Y, Z \lt N$;
- $X+Y+Z=N$;
- $X$ $|$ $Y$ $|$ $Z=N,$ where $|$ represents the [bitwise OR operation](https://en.wikipedia.org/wiki/Bitwise_operation#OR).

Since the number of triples can be huge, print them modulo $10^9+7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$, as mentioned in the statement.

---

## Output Format

For each test case, output on a new line, the number of triples satisfying the condition, modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le N \lt 2^{60}$

---

## Examples

**Example 1**

**Input**

```text
2
3
7
```

**Output**

```text
0
6
```

**Explanation**

**Test case $1$:** There are no triples $(X, Y, Z)$ satisfying the given conditions.

**Test case $2$:** The following $6$ tuples satisfy the conditions: $\{(1, 2, 4), (1, 4, 2), (2, 1, 4), (2, 4, 1), (4, 1, 2), (4, 2, 1)\}$.

For example, in the tuple $(1, 2, 4)$, $1+2+4 = 7$ and $1$ $|$ $2$ $|$ $4 = 7$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
7
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AWESUM_OR)

[Contest: Division 1](https://www.codechef.com/START84A/problems/AWESUM_OR)

[Contest: Division 2](https://www.codechef.com/START84B/problems/AWESUM_OR)

[Contest: Division 3](https://www.codechef.com/START84C/problems/AWESUM_OR)

[Contest: Division 4](https://www.codechef.com/START84D/problems/AWESUM_OR)

***Author:*** [shauryabhalla0](https://www.codechef.com/users/shauryabhalla0)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2152

#
[](#prerequisites-3)PREREQUISITES:

Combinatorics or dynamic programming

#
[](#problem-4)PROBLEM:

Given an integer N, find the number of triplets X, Y, Z such that

- 0 \lt X, Y, Z \lt N

- X+Y+Z = X\mid Y\mid Z = N

#
[](#explanation-5)EXPLANATION:

For any integers X and Y, it’s not hard to see that X\mid Y \leq X+Y, with equality holding if and only if X and Y don’t share any bits in their binary representations.

This extends to three integers as well: X\mid Y\mid Z \leq X+Y+Z, and equality holds if and only if X, Y, Z all have distinct bits set.

Now, we know that X\mid Y\mid Z = N. This means that

- If a bit b is not set in N, then it can’t be set in *any* of X, Y, Z

- If a bit b is set in N, then it should be set in at least one of X, Y, Z.

Our earlier discussion further tells us that it can’t be set in two or more of them, so it must be set in *exactly* one of them.

So, each set bit in N must be distributed to one of X, Y, or Z; while ensuring that each of them gets at least one set bit; our objective is to count the number of ways to do this.

There are several ways to do this, here are a couple.

Direct math

The number of ways can be calculated directly, using the inclusion-exclusion principle.

First, let’s ignore the “each value gets at least one bit” condition, i.e, allow zeros.

Counting the number of ways here is simple: each set bit in N has exactly 3 choices, for whether it’s given to X, Y, or Z.

So, if N has K set bits, the number of ways is 3^K.

Now, let’s remove the cases when some of the values are 0.

If X = 0 in the end, all the bits were distributed to Y and Z, i.e, 2 options for each bit for 2^K in total.

By symmetry, this is also the number of ways in which Y = 0, or Z = 0.

So, the total number of ways here is 3\cdot 2^K.

Finally, we need to add in the number of ways where two or more of X, Y, Z are zero, since those would have been removed multiple times.

It’s easy to see that there are only three ways here: (N, 0, 0), (0, N, 0), (0, 0, N).

So, the answer is simply

3^K - 3\cdot 2^K + 3

Dynamic programming

Suppose N has K set bits.

As our observations showed, only this number K matters; which bits were set doesn’t matter at all.

Our aim is to find out the number of ways to split K bits into three non-empty subsets.

Since K is quite small (N \lt 2^{60}, so K \leq 60), this can be done using dynamic programming.

Let dp_i be the number of ways to split i bits into three non-empty subsets.

Then, if we fix the size of the first subset j (1 \leq j \lt i), we have:

-
\binom{i}{j} ways to choose which bits go into this subset.

-
2^{i-j}-2 ways to distribute the remaining bits into two non-empty subsets.

So, we have

dp_i = \sum_{j=1}^{i-1} \binom{i}{j} \left ( 2^{i-j} - 2 \right )

which can easily be precomputed for all K \leq 60 in \mathcal{O}(K^2) or \mathcal{O}(K^3), after which answering queries is easy.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\log N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;
#define int long long

const int mod=1e9+7;
vector<int> pcom(61, 0);

int binexp(int a, int b, int mod){
    assert(b>=0);
    a=a%mod;
    int ans = 1;
    while(b){
        if(b&1){
            ans=ans*a%mod;
        }
        a=a*a%mod;
        b/=2;
    }
    return ans;
}

void solve(){
    int n;
    cin>>n;

    int x = __builtin_popcountll(n);
    cout<<pcom[x]*6%mod<<'\n';
    // cout<<((binexp(3, x, mod)-3*binexp(2, x, mod)%mod+mod)%mod+3)%mod<<'\n';
}

signed main(){

    ios::sync_with_stdio(false);
    cin.tie(0);  cout.tie(0);

    for(int a=3; a<=60; a++){
        int sum = 0;
        for(int b = a-1; b>0; b--){
            for(int c = b-1; c>0; c--){
                sum = (sum + binexp(2, b-c-1, mod)*binexp(3, c-1, mod)%mod)%mod;
            }
        }
        pcom[a] = sum;
    }

    int tt;
    cin>>tt;

    while(tt--) solve();
}
``

Tester's code (C++)
``// Problem: SUM OR
// Contest: CodeChef - STR84TST
// Memory Limit: 256 MB
// Time Limit: 1000 ms
// Author: abhidot

// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define int long long
#define ll long long
#define IOS std::ios::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);
#define pb push_back
#define mod 1000000007
#define mod2 998244353
#define lld long double
#define pii pair<int, int>
#define ff first
#define ss second
#define all(x) (x).begin(), (x).end()
#define uniq(v) (v).erase(unique(all(v)),(v).end())
#define rep(i,x,y) for(int i=x; i<y; i++)
#define fill(a,b) memset(a, b, sizeof(a))
#define vi vector<int>
#define V vector
#define setbits(x) __builtin_popcountll(x)
#define w(x)  int x; cin>>x; while(x--)
using namespace std;
using namespace __gnu_pbds;
template <typename num_t> using ordered_set = tree<num_t, null_type, less<num_t>, rb_tree_tag, tree_order_statistics_node_update>;
const long long N=200005, INF=2000000000000000000, inf = 2e9+5;

int power(int a, int b, int p){
	if(a==0)
	return 0;
	int res=1;
	a%=p;
	while(b>0)
	{
		if(b&1)
		res=(res*a)%p;
		b>>=1;
		a=(a*a)%p;
	}
	return res;
}

void print(bool n){
    if(n){
        cout<<"YES\n";
    }else{
        cout<<"NO\n";
    }
}

int f[100], in[100];

int ncr(int n, int r){
	return f[n]*in[r]%mod*in[n-r]%mod;
}

int32_t main()
{
    IOS;
    f[0]=1, in[0]=1;
    for(int i=1;i<100;i++){
    	f[i]=i*f[i-1]%mod;
    	in[i]=power(f[i], mod-2, mod);
    }
		int ans[61]={0};
		for(int x=1;x<=60;x++){
			for(int y=1;x+y<=60;y++){
				for(int z=1;x+y+z<=60;z++){
					int s = x+y+z;
					if(s>60) continue;
					ans[s]+=(ncr(s, x)*ncr(s-x, y)%mod);
					ans[s]%=mod;
				}
			}
		}

		w(T){
			int n;
			cin>>n;
			cout<<ans[setbits(n)]<<"\n";
		}
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    bits = bin(n).count('1')
    ans = pow(3, bits, mod) - 3*pow(2, bits, mod) + 3
    print(ans % mod)
``

</details>
