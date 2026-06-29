# Lexicographically Largest 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LEXILARGEST |
| Difficulty Rating | 2151 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [LEXILARGEST](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/LEXILARGEST) |

---

## Problem Statement

You are given a positive integer $M$ and an array $A \ (1\leq A_i \leq M)$ consisting of $N$ positive integers.

Find the **lexicographically largest** array $B$ such that:
- $|B|=N$;
- $1 \leq B_i \leq M$ for all $1 \leq i \leq N$;
- $A_i = \gcd(B_1, B_2, \ldots, B_i)$, where $\gcd$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).

Note that the input $A$ guarantees that $B$ always exists.
For two arrays $X$ and $Y$, both of size $N$, the array $X$ is said to be lexicographically larger than array $Y$, if, in the first position where $X$ and $Y$ differ, $X_i \gt Y_i$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space separated integers $N$ and $M$ — the  length of array $A$ and upper bound on array elements.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ representing the array $A$.

---

## Output Format

For each test case, output on a new line, the lexicographically largest array $B$, satisfying the given conditions.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^4$
- $1 \leq M \leq 10^9$
- $1 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^4$.

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1
2 2
2 1
4 3
2 2 2 2
4 5
2 2 2 2
```

**Output**

```text
1
2 1
2 2 2 2
2 4 4 4
```

**Explanation**

**Test case $1$:** The only possible array is $B = [1]$ which satisfies the given conditions.

**Test case $2$:** The only possible array is $B = [2, 1]$ which satisfies the given conditions.
Here $A_1 = B_1 = 2$, and $A_2 = \gcd(B_1, B_2) = 1$.

**Test case $4$:** The lexicographically largest valid array is $B = [2, 4, 4, 4]$. Some other arrays that are valid include $[2, 2, 2, 2], [2, 2, 4, 2], [2, 2, 4, 4]$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 2
2 1
```

**Output for this case**

```text
2 1
```



#### Test case 3

**Input for this case**

```text
4 3
2 2 2 2
```

**Output for this case**

```text
2 2 2 2
```



#### Test case 4

**Input for this case**

```text
4 5
2 2 2 2
```

**Output for this case**

```text
2 4 4 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/LEXILARGEST)

[Contest: Division 1](https://www.codechef.com/START104A/problems/LEXILARGEST)

[Contest: Division 2](https://www.codechef.com/START104B/problems/LEXILARGEST)

[Contest: Division 3](https://www.codechef.com/START104C/problems/LEXILARGEST)

[Contest: Division 4](https://www.codechef.com/START104D/problems/LEXILARGEST)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2151

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given an array A and an integer M, find the lexicographically largest array B whose elements are between 1 and M, and A_i = \gcd(B_1, B_2, B_3, \ldots, B_i) for every i.

It’s guaranteed that a solution exists for every given input.

# [](#explanation-5)EXPLANATION:

First, recall that \gcd(B_1, B_2, B_3, \ldots, B_i) is always a multiple of \gcd(B_1, B_2, B_3, \ldots, B_i, B_{i+1}).

In other words, we know that input is such that A_i is a multiple of A_{i+1} for each i, since we’re told the answer exists. Keep this fact in mind.

Note that we have no choice for B_1: it must always be A_1 itself, since that’s the only way the condition on prefix gcd can be satisfied for the first index.

Now, let’s try to find the remaining elements.

We want the lexicographically maximum array, so it’s best to make a greedy choice at each step.

Suppose we’ve found the values of B_1, B_2, \ldots B_{i-1}, and we want to find B_i.

B_i should be chosen such that \gcd(B_1, B_2, \ldots, B_i) = A_i.

However, we already know that \gcd(B_1, B_2, \ldots, B_{i-1}) = A_{i-1}, since that’s how we constructed the first i-1 elements.

So, we just want to choose B_i such that \gcd(A_{i-1}, B_i) = A_i. In particular, B_i should be a multiple of A_i.

Recall that we already know that A_{i-1} is a multiple of A_i, so we just need to choose B_i to be a multiple of A_i that’s as large as possible; yet also shares no other factors with A_{i-1} than A_i.

Clearly, the absolute best we can do is to choose A_i\cdot \left\lfloor\frac{M}{A_i}\right\rfloor, i.e, the largest multiple of A_i that’s \leq M.

However, this might not always work - we might have its GCD with A_{i-1} be some larger multiple of A_i.

In such a case, we can just bruteforce to find the next best thing!

That is, while \gcd(B_i, A_{i-1}) \neq A_i, keep reducing B_i by A_i.

This is clearly a correct solution, the only concern is speed.

And indeed, this is fast enough - very fast, actually.

Proof

Let A_{i-1} = x\cdot A_i and B_i = y\cdot A_i.

Then, \gcd(A_{i-1}, B_i) = A_i\cdot \gcd(x, y), so our objective is to ensure that \gcd(x, y) = 1.

Suppose we take K steps to find an answer.

That would mean that \gcd(x, y-i) \gt 1 for all 0 \leq i \lt K; in particular, x must share a prime factor with every integer in that range.

Now, x \leq 10^9 means it has at most 9 distinct prime factors.

Further, till 10^9, the gap between consecutive primes is at most about 300.

So, after 300\cdot 10 = 3000 steps, we’ll surely find a prime number that’s not a factor of x and be done.

In practice, the number of steps required will be far far less than 3000 because primes just aren’t that spaced out (also, large prime gaps only happen for larger primes, and x can’t have many large primes in its factorization) - I would expect the actual number of steps to be of the order \mathcal{O}(\log{10^9}).

The 3000 upper bound is good enough though, because we don’t actually trigger it at each index - it’s only done when A_i \neq A_{i-1} which happens \log( A_1) times at most, since the element (at least) halves each time we move to a strictly smaller one.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N + 3000) GCD operations per testcase (in practice, the 3000 is far smaller and more like 50).

# [](#code-7)CODE:

Author's code (C++)
``#pragma GCC optimod_intze("O3,unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
using namespace std;
#define ll long long
const ll INF_MUL=1e15;
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
const ll MOD=998244353;
const ll MAX=500500;
void solve(){
    ll n,m; cin>>n>>m;
    vector<ll> a(n+5,0);
    for(ll i=1;i<=n;i++){
        cin>>a[i];
        assert((a[i-1]%a[i])==0);
    }
    vector<ll> ans(n+5,0);
    ans[1]=a[1];
    for(ll i=2;i<=n;i++){
        ans[i]=(m/a[i])*a[i];
        ll ops=0;
        while(__gcd(ans[i],a[i-1])!=a[i]){
            ans[i]-=a[i];
        }
    }
    ll use=0;
    for(ll i=1;i<=n;i++){
        use=__gcd(use,ans[i]);
        assert(use==a[i]);
        cout<<ans[i]<<" \n"[i==n];
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

Tester's code (C++)
``#ifndef LOCAL
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx,avx2,sse,sse2,sse3,sse4,popcnt,fma")
#endif

#include <bits/stdc++.h>
using namespace std;

#ifdef LOCAL
#include "../debug.h"
#else
#define dbg(...) "11-111"
#endif

struct input_checker {
	string buffer;
	int pos;

	const string all = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	const string number = "0123456789";
	const string upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	const string lower = "abcdefghijklmnopqrstuvwxyz";

	input_checker() {
		pos = 0;
		while (true) {
			int c = cin.get();
			if (c == -1) {
				break;
			}
			buffer.push_back((char) c);
		}
	}

	int nextDelimiter() {
		int now = pos;
		while (now < (int) buffer.size() && buffer[now] != ' ' && buffer[now] != '\n') {
			now++;
		}
		return now;
	}

	string readOne() {
		assert(pos < (int) buffer.size());
		int nxt = nextDelimiter();
		string res;
		while (pos < nxt) {
			res += buffer[pos];
			pos++;
		}
		return res;
	}

	string readString(int minl, int maxl, const string &pattern = "") {
		assert(minl <= maxl);
		string res = readOne();
		assert(minl <= (int) res.size());
		assert((int) res.size() <= maxl);
		for (int i = 0; i < (int) res.size(); i++) {
			assert(pattern.empty() || pattern.find(res[i]) != string::npos);
		}
		return res;
	}

	int readInt(int minv, int maxv) {
		assert(minv <= maxv);
		int res = stoi(readOne());
		assert(minv <= res);
		assert(res <= maxv);
		return res;
	}

	long long readLong(long long minv, long long maxv) {
		assert(minv <= maxv);
		long long res = stoll(readOne());
		assert(minv <= res);
		assert(res <= maxv);
		return res;
	}

	auto readInts(int n, int minv, int maxv) {
		assert(n >= 0);
		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readInt(minv, maxv);
			if (i+1 < n) readSpace();
		}
		return v;
	}

	auto readLongs(int n, long long minv, long long maxv) {
		assert(n >= 0);
		vector<long long> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readLong(minv, maxv);
			if (i+1 < n) readSpace();
		}
		return v;
	}

	void readSpace() {
		assert((int) buffer.size() > pos);
		assert(buffer[pos] == ' ');
		pos++;
	}

	void readEoln() {
		assert((int) buffer.size() > pos);
		assert(buffer[pos] == '\n');
		pos++;
	}

	void readEof() {
		assert((int) buffer.size() == pos);
	}
};

int32_t main() {
    ios_base::sync_with_stdio(0);   cin.tie(0);

    input_checker input;
    int T = input.readInt(1, (int)1e4); input.readEoln();
    int sum_N = 0;
    while(T-- > 0) {
        int n = input.readInt(1, (int)1e4); input.readSpace();
        int m = input.readInt(1, (int)1e9); input.readEoln();
        vector<int> a = input.readInts(n, 1, m); input.readEoln();
        auto b = a;
        for(int i = 1 ; i < n ; i++) {
            b[i] = (m / a[i]) * a[i];
            while(__gcd(a[i - 1], b[i]) > a[i])
                b[i] -= a[i];
        }

        for(int i = 0 ; i < n ; i++)
            cout << b[i] << " \n"[i == n - 1];
    }
    input.readEof();
    assert(sum_N <= (int)5e4);

    return 0;
}
``

Editorialist's code (Python)
``from math import gcd
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0]*n
    ans[0] = a[0]
    for i in range(1, n):
        ans[i] = a[i]*(m//a[i])
        while gcd(ans[i], a[i-1]) != a[i]: ans[i] -= a[i]
    print(*ans)
``

</details>
