# Maximise Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXIMISESUM |
| Difficulty Rating | 1715 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MAXIMISESUM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MAXIMISESUM) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ positive integers.

You are allowed to do the following operation any number of times:

- Select two integers $l$ and $r$ such that $1 \leq l < r \leq N$;
- Change $A_i$ to $\min(A_l, A_r)$ for all $l < i < r$.

Find the **maximum** value of $\sum_{i=1}^{N} A_i$ that you can achieve after any (possibly zero) number of operations.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

---

## Output Format

For each test case, output on a new line, the maximum sum that you can achieve after any (possibly zero) number of operations.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
2 3
3
5 1 7
4
5 5 5 5
```

**Output**

```text
5
17
20
```

**Explanation**

**Test case $1$:** The only possible value of $(l, r)$ can be $(1, 2)$ but that does not impact any $A_i$. Thus, the maximum sum we can achieve is $2+3=5$.

**Test case $2$:** Select $(l, r)$ as $(1, 3)$ and change $A_2=\min(A_1, A_3) = 5$. Thus, the array becomes $[5, 5, 7]$ with sum $5+5+7 = 17$.

**Test case $3$:** Since all elements of the array are same, we cannot change any $A_i$ using an operation. Thus, the maximum sum we can achieve is $5+5+5+5=20$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 3
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
3
5 1 7
```

**Output for this case**

```text
17
```



#### Test case 3

**Input for this case**

```text
4
5 5 5 5
```

**Output for this case**

```text
20
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXIMISESUM)

[Contest: Division 1](https://www.codechef.com/START104A/problems/MAXIMISESUM)

[Contest: Division 2](https://www.codechef.com/START104B/problems/MAXIMISESUM)

[Contest: Division 3](https://www.codechef.com/START104C/problems/MAXIMISESUM)

[Contest: Division 4](https://www.codechef.com/START104D/problems/MAXIMISESUM)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1715

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You have an array A.

In one move, you can pick indices 1 \leq i \lt j \leq N and set A_k:=\min(A_i, A_j) for each i \lt k \lt j.

Find the maximum possible sum of the final array obtained after performing some operations.

# [](#explanation-5)EXPLANATION:

Let’s analyze what the final array might look like.

Intuitively, if we have indices  i \lt k \lt j such that A_k \lt \min(A_i, A_j), then we should be able to bring A_k up to \min(A_i, A_j) by performing the operation.

Of course, this operation also affects other elements inbetween (and might reduce some of them, which isn’t what we want).

Let’s call a move (i, j) a *good move* if there’s no index i \lt k \lt j such that A_k \gt \min(A_i, A_j).

That is, a *good move* is one that only increases the elements it affects.

It’d be nice if we could use only good moves - in fact ,we can!

***Claim:*** The final array will be such that for any three indices i \lt k \lt j, we’ll have A_k \geq \min(A_i, A_j); and further, this can be achieved by using only *good* moves.

Proof

Suppose there are indices  i \lt k \lt j such that A_k \lt \min(A_i, A_j).

Let x be the index of the *maximum* element of the segment [i, k-1]. We definitely have A_x \geq A_i (if there are multiple, choose the rightmost).

Similarly, let y be the index of the leftmost maximum of segment [k+1, j]. Once again, we know A_y \geq A_j.

Without loss of generality, let’s say A_x \geq A_y, i.e, A_y = \min(A_x, A_y).

Let z be the largest index in [x, k-1] such that A_z \geq A_y.

Notice that the operation (z ,y) is a *good* operation, because we’ve chosen our indices in such a way that A_y is the second maximum in range [z, y].

Further, this range includes index k as well.

So, we can perform good operation (z ,y), which increases A_k to reach A_y.

Since A_y \geq A_j, we have A_k \geq\min(A_i, A_j), as we wanted!

This way, we can keep on performing good operations to increase elements till no further is possible.

It’s not hard to see that the process will terminate after finitely many steps.

Now that we know this, let’s see what it actually means for A.

Let M be the *index* of the maximum element of A.

Then, the above claim tells us that the final array must have:

- A_1 \leq A_2 \leq A_3 \leq\ldots\leq A_M

- A_M \geq A_{M+1}\geq\ldots\geq A_N

That is, the array will look like a pyramid.

So, we just need to find out what the prefix of the array till M will look like in the end.

It’s not too hard to see that:

- Let M_1 be the maximum element of the range [1, M-1] (if there are multiple occurrences, choose the leftmost).

Then, we can set A_{M_1} = A_{M_1+1} = A_{M_1+1} = \ldots = A_{M-1} all to this maximum, by performing the operation (M_1, M).

- Again, let M_2 be the index of the leftmost maximum element of [1, M_1-1]. Everything from M_2 till M_1-1 can be set to A_{M_2}.

- Repeat this process for [1, M_2-1], and so on till all the elements are set.

Of course, we can’t implement this process in \mathcal{O}(N^2) time, that’d be too slow.

To speed it up, note that the indices M_1, M_2, M_3, \ldots we found are in fact exactly the *prefix maximums* of the array A.

That is whenever there’s a new prefix maximum, that’s one of the M_i.

This way, all the M_i can be found in \mathcal{O}(N) time, after which finding the final values of all the elements is easy.

The suffix after M can be solved similarly by finding suffix maximums.

Once the entire array is known, just output its sum.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

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
    ll n; cin>>n;
    ll ans=0;
    vector<ll> a(n+5);
    for(ll i=1;i<=n;i++){
        cin>>a[i];
    }
    vector<ll> pref(n+5,0),suff(n+5,0);
    for(ll i=1;i<=n;i++){
        pref[i]=max(pref[i-1],a[i]);
    }
    for(ll i=n;i>=1;i--){
        suff[i]=max(suff[i+1],a[i]);
    }
    for(ll i=2;i<n;i++){
        a[i]=max(a[i],min(pref[i-1],suff[i+1]));
    }
    for(ll i=1;i<=n;i++){
        ans+=a[i];
    }
    cout<<ans<<nline;
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
    int T = input.readInt(1, (int)1e5); input.readEoln();
    int sum_N = 0;
    while(T-- > 0) {
        int n = input.readInt(1, (int)1e5);    input.readEoln();
        sum_N += n;
        vector<int> a = input.readInts(n, 1, (int)1e9);  input.readEoln();

        int pos = max_element(a.begin(), a.end()) - a.begin();
        int mx = 0;
        for(int i = 0 ; i < pos ; i++) {
            mx = max(mx, a[i]);
            a[i] = mx;
        }
        mx = 0;
        for(int i = n - 1 ; i > pos ; i--) {
            mx = max(mx, a[i]);
            a[i] = mx;
        }

        cout << accumulate(a.begin(), a.end(), 0ll) << '\n';
    }
    input.readEof();
    assert(sum_N <= (int)5e5);

    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = max(a)
    ans, mx = 0, 0
    lo, hi = 0, 0
    for i in range(n):
        x = a[i]
        if x == m:
            lo = i
            break
        mx = max(mx, x)
        ans += mx
    mx = 0
    for i in reversed(range(n)):
        x = a[i]
        if x == m:
            hi = i
            break
        mx = max(mx, x)
        ans += mx
    ans += m*(hi-lo+1)
    print(ans)
``

</details>
