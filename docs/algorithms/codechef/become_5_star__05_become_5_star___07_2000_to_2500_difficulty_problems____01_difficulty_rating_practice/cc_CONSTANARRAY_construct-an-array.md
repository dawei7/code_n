# Construct An Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CONSTANARRAY |
| Difficulty Rating | 2419 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CONSTANARRAY](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CONSTANARRAY) |

---

## Problem Statement

You are given a positive integer $M$ and an array $A \ (1 \leq A_i \leq M)$ consisting of $N$ positive integers.

Construct an array $B$ of length $N$ such that:
- $1 \leq B_i \leq M$ for all $1 \leq i \leq N$;
- For all $1 \leq i \leq N$, there does not exist an index $1 \leq j \leq i$ such that the frequency of $B_j$ is more than that of $A_i$ in the subarray $[B_1, B_2, \ldots, B_i]$

It can be proved that at least one such array $B$ exists for any array $A$.
If there are multiple valid arrays, you can print any one.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space separated integers $N$ and $M$ — the length of the array $A$ and upper bound on $A_i$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

---

## Output Format

For each test case, output on a new line, $N$ space-separated integers representing a valid array $B$.

It can be proved that at least one such array $B$ exists for any array $A$.
If there are multiple valid arrays, you can print any one.

---

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 2000$
- $1 \leq M \leq N$
- $1 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $2000$.

---

## Examples

**Example 1**

**Input**

```text
4
1 1
1
3 2
1 1 1
3 2
1 1 1
4 4
1 2 3 4
```

**Output**

```text
1
1 1 1
1 2 1
1 2 3 4
```

**Explanation**

**Test case $1$:** Consider the array $B = [1]$. The only subarray is $[1]$ where the frequency of $B_1$ is less than equal to that of $A_1$.

**Test case $2$:** Consider the array $B = [1, 1, 1]$.
- For $i=1$: The frequency of both $A_1$ and $B_1$ in subarray $[B_1]$ is $1$.
- For $i=2$: The frequency of $A_2$ is same as that of $B_1, B_2$ in subarray $[B_1, B_2]$.
- For $i=3$: The frequency of $A_3$ is same as that of $B_1, B_2, B_3$ in subarray $[B_1, B_2, B_3]$.

**Test case $3$:** Consider the array $B = [1, 2, 1]$.
- For $i=1$: The frequency of both $A_1$ and $B_1$ in subarray $[B_1]$ is $1$.
- For $i=2$: The frequency of $A_2$ is same as that of $B_1$ and $B_2$ in subarray $[B_1, B_2]$.
- For $i=3$: The frequency of $A_3$ is same as that of $B_1, B_3$ and higher than $B_2$ in subarray $[B_1, B_2, B_3]$.

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
3 2
1 1 1
```

**Output for this case**

```text
1 1 1
```



#### Test case 3

**Input for this case**

```text
3 2
1 1 1
```

**Output for this case**

```text
1 2 1
```



#### Test case 4

**Input for this case**

```text
4 4
1 2 3 4
```

**Output for this case**

```text
1 2 3 4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CONSTANARRAY)

[Contest: Division 1](https://www.codechef.com/START104A/problems/CONSTANARRAY)

[Contest: Division 2](https://www.codechef.com/START104B/problems/CONSTANARRAY)

[Contest: Division 3](https://www.codechef.com/START104C/problems/CONSTANARRAY)

[Contest: Division 4](https://www.codechef.com/START104D/problems/CONSTANARRAY)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2419

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given an array A of length N and integer M \leq N, construct any array B of length equal to A such that:

- 1 \leq B_i \leq M

- For each i, A_i has the highest frequency among [B_1, B_2, \ldots, B_i].

# [](#explanation-5)EXPLANATION:

Let’s solve a restricted case first: N = M.

While it seems quite hard to ensure the given condition for each index, there’s a surprisingly simple idea: just make every element occur once!

That is, consider what happens if B is chosen to be a permutation of [1, 2, 3, \ldots, M].

Then, for each i, we only need to ensure that A_i appears as one of B_1, B_2, \ldots, B_i — once it does, the condition is automatically satisfied, since no other element appears strictly more than once.

To do this is, for each x = 1, 2, 3, \ldots, M, find the *first* occurrence of x in A (call it \text{pos}[x]), and set B_{\text{pos}[x]} to x.

Now, any remaining elements can be distributed to the remaining positions arbitrarily, as long as you end up with a permutation.

Next, we’ll generalize this to any M \leq N.

Of course, it’s no longer possible to form a permutation, but we can use a similar idea: make everything occur an equal number of times.

That is, take the first M positions; and solve them using the algorithm for M = N as above.

Then, take the next M positions, and solve them separately, and so on.

Repeat this process and you’ll get a valid array!

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Setter's code (C++)
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
    vector<ll> a(n);
    for(auto &it:a){
        cin>>it;
    }
    while(!a.empty()){
        vector<ll> visited(n+5,0);
        ll freq=0;
        for(auto it:a){
            if(!visited[it]){
                cout<<it<<" ";
                freq++;
            }
            visited[it]=1;
        }
        while(freq--){
            a.erase(a.begin());
        }
    }
    cout<<nline;
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
    int T = input.readInt(1, 2000); input.readEoln();
    int sum_N = 0;
    while(T-- > 0) {
        int n = input.readInt(1, 2000); input.readSpace();
        int m = input.readInt(1, n); input.readEoln();
        sum_N += n;
        vector<int> a(n), b(n), vis(m + 1);

        for(int i = 0 ; i < n ; i++) {
            a[i] = input.readInt(1, m);
            if(i < n - 1)   input.readSpace();
            else    input.readEoln();
        }

        for(int i = 0 ; i < n ; i += m) {
            int end = min(i + m, n), ptr = 1;
            for(int j = i ; j < end ; j++) {
                vis[a[j]] = 1;
            }
            for(int j = i ; j < end ; ++j) {
                if(vis[a[j]] == 1) {
                    vis[a[j]] = -1;
                    b[j] = a[j];    continue;
                }
                while(ptr <= m && vis[ptr]) ptr++;
                assert(ptr <= m);
                vis[ptr] = -1;
                b[j] = ptr;
            }
            fill(vis.begin(), vis.end(), 0);
        }

        for(int i = 0 ; i < n ; i++)    cout << b[i] << " \n"[i == n - 1];
    }
    input.readEof();
    assert(sum_N <= 2000);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0]*n
    for i in range(0, n, m):
        mark = [0]*(m+1)
        for j in range(i, min(n, i+m)):
            if mark[a[j]] == 1: continue
            ans[j] = a[j]
            mark[a[j]] = 1
        for j in range(i, min(i+m, n)):
            if ans[j] > 0: continue
            while mark[len(mark)-1] == 1: mark.pop()
            ans[j] = len(mark) - 1
            mark.pop()
    print(*ans)
``

</details>
