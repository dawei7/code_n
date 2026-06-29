# Digit Operation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIGITOP |
| Difficulty Rating | 1798 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [DIGITOP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/DIGITOP) |

---

## Problem Statement

You are given arrays $A$ and $B$, each consisting of $N$ **strings**, and a positive integer $K$.
For all $1\le i \le N$, both $A_i$ and $B_i$ consist of characters from $0$ to $9$ (both inclusive).

You can perform the following types of operations on array $A$:
- Type $1$: Choose two indices $i$ and $j$ $(i\neq j)$ and swap any character of $A_i$ with any character of $A_j$. The cost of this operation is $0$.
- Type $2$: Choose an index $i$ and replace **one** character of $A_i$ with any character from $0$ to $9$ (both inclusive). The cost of this operation is $1$.

For example, let $A = [24, 30, 51]$. A valid sequence of operations can be:
- Swap $4$ in $A_1 = 24$ with $0$ in $A_2 = 30$ to obtain $[20, 34, 51]$.
- Swap $0$ in $A_1 = 20$ with $5$ in $A_3 = 51$ to obtain $[25, 34, 01]$.
- Replace $0$ in $A_3 = 01$ with $1$ to obtain $[25, 34, 11]$.
The cost of the above sequence of operations is $1$.

Find whether we can convert the array $A$ to array $B$ using **any** (possibly zero) number of operations with cost $\le K$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, the size of array and the maximum cost of operations.
    - The second line of each test case contains $N$ space-separated strings $A_1,A_2,\ldots,A_N$.
    - The third line of each test case contains $N$ space-separated strings $B_1,B_2,\ldots,B_N$.

---

## Output Format

For each test case, print `YES` if it is possible to convert array $A$ to $B$ using **any** (possibly zero) number of operations with cost $\le K$. Else, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq K \leq 10^{18}$
- $1 \leq |A_i|, |B_i| \leq 19$
- $A_i$ and $B_i$ consist of characters from $0$ to $9$ (both inclusive).
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 9
9 1
2 2
1 11
11 1
4 1
22 13 12 89
28 98 21 31
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$**: We can use one operation of type $1$ to swap $1$ in $A_1$ with $9$ in $A_2$. Thus, $A$ becomes $[9,1]$, which is equal to $B$. We are able to do this with $0$ cost, which is $\le 2$.

**Test case $2$:** It is impossible to convert $A$ to $B$ with at most $2$ cost.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
1 9
9 1
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 2
1 11
11 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 1
22 13 12 89
28 98 21 31
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIGITOP)

[Contest: Division 1](https://www.codechef.com/START84A/problems/DIGITOP)

[Contest: Division 2](https://www.codechef.com/START84B/problems/DIGITOP)

[Contest: Division 3](https://www.codechef.com/START84C/problems/DIGITOP)

[Contest: Division 4](https://www.codechef.com/START84D/problems/DIGITOP)

***Author:*** [grayhathacker](https://www.codechef.com/users/grayhathacker)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1798

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You’re given two integer arrays A and B of length N. In one move you can:

- Pick 1 \leq i \lt j \leq N, and swap one digit of A_i with one digit of A_j. This operation is free.

- Pick 1 \leq i \leq N, and replace some digit of A_i with some other digit. This operation has a cost of 1.

Find out whether you can make A = B with a cost of at most K.

#
[](#explanation-5)EXPLANATION:

First, note that neither operation allows us to change the length of a string.

So, if len(A_i) \neq len(B_i) for some 1 \leq i \leq N, then making them equal is obviously impossible.

Now, note that the first operation allows us to freely rearrange the digits in A as we like, so our aim should be to just make sure that A and B have the same multiset of digits.

So, let \text{ct}_A[d] be the number of times digit d appears in A, and \text{ct}_B[d] be the same for B.

Let S = \sum_{d=0}^9 \max(0, \text{ct}_A[d] - \text{ct}_B[d]), i.e, S is the number of ‘extra’ digits that A has compared to B.

We need one operation to get rid of each of these digits, so we definitely need at least S operations of type 2.

It’s also not hard to see that we need exactly S operations of type 2 to make the multisets equal.

Proof

Recall that we ensured that A_i and B_i have equal lengths, right at the start.

So, the total number of digits in A equals the total number of digits in B.

In particular, for each digit that A has extra of, there will be some digit that it has a deficit of.

So, in one replace operation, we can turn an extra digit into one that we require.

This allows us to use exactly S operations so that A and B have the same multisets of digits, as required.

So, once S is computed, the answer is `Yes` if S \leq K and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include<bits/stdc++.h>
using namespace std;

#define mod 1000000007
typedef set<string> ss;
typedef vector<int> vs;
typedef map<int, char> msi;
typedef pair<int, int> pa;
typedef long long int ll;

ll n, k, i, j, val, ca[10], cb[10];
string a[100005], b[100005];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
#ifndef ONLINE_JUDGE
	freopen("inputf.in", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;
	while (t--)
	{
		memset(ca, 0, sizeof(ca));
		memset(cb, 0, sizeof(cb));
		cin >> n >> k;
		for (i = 0; i < n; i++)
			cin >> a[i];
		for (i = 0; i < n; i++)
			cin >> b[i];
		for (i = 0; i < n; i++)
			if (a[i].length() != b[i].length())
				break;
		if (i != n)
			cout << "NO\n";
		else
		{
			for (i = 0; i < n; i++)
			{
				for (j = 0; j < a[i].length(); j++)
					ca[a[i][j] - '0']++;
				for (j = 0; j < b[i].length(); j++)
					cb[b[i][j] - '0']++;
			}
			val = 0;
			for (i = 0; i < 10; i++)
				val += max(0LL, cb[i] - ca[i]);
			if (val <= k)
				cout << "YES\n";
			else
				cout << "NO\n";
		}

	}

	return 0;
}
``

Tester's code (C++)
``

// Problem: Digit Operation
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
const long long N=200005, INF=1000000000000000000, inf = 2e9+5, lim=1e18;

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

	auto readIntVec(int n, int minv, int maxv) {
		assert(n >= 0);
		vector<int> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readInt(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
		}
		return v;
	}

	auto readLongVec(int n, long long minv, long long maxv) {
		assert(n >= 0);
		vector<long long> v(n);
		for (int i = 0; i < n; ++i) {
			v[i] = readLong(minv, maxv);
			if (i+1 < n) readSpace();
			else readEoln();
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

input_checker inp;

int32_t main()
{
    IOS;
    int sm=0;
		int T=inp.readInt(1, 1000);
		inp.readEoln();
		while(T--){
			int n=inp.readInt(2, 100000);
			inp.readSpace();
			int k=inp.readLong(1, INF);
			inp.readEoln();
			vector<int> a = inp.readLongVec(n, 1, INF);
			vector<int> b = inp.readLongVec(n, 1, INF);
			sm+=n;
			assert(sm<=100000);
			int f[10]={0};
			int ok=1;
			for(int i=0;i<n;i++){
				string s = to_string(a[i]);
				for(auto c: s){
					f[c-'0']--;
				}
				string ss = to_string(b[i]);
				for(auto c: ss){
					f[c-'0']++;
				}
				ok&=(s.size()==ss.size());
			}

			int cnt=0;
			for(int i=0;i<10;i++) cnt+=max(f[i], 0LL);
			ok&=(cnt<=k);
			print(ok);
		}

		inp.readEof();
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 'Yes'
    for i in range(n):
        if len(str(a[i])) != len(str(b[i])): ans = 'No'

    dif = [0]*10
    for x in a:
        for d in str(x): dif[ord(d) - ord('0')] += 1
    for x in b:
        for d in str(x): dif[ord(d) - ord('0')] -= 1
    reqd = sum(x for x in dif if x > 0)
    if reqd > k: ans = 'No'
    print(ans)
``

</details>
