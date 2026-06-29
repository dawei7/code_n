# GCD Queries

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GCD_QUERIES |
| Difficulty Rating | 2422 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [GCD_QUERIES](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/GCD_QUERIES) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ integers along with $Q$ queries.

For each query:
- $X$ : Given an integer $X$, print and **remove** the **minimum** element in the array $k$, such that $\texttt{gcd} (X, k) \gt 1$, where $\texttt{gcd}$ denotes the [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).
If no value present in the array satisfies the condition, print and remove the **minimum** element of the array.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case consists of a single integer $N$ — the number of elements in the array.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ — the elements of the array $A$.
    - The third line contains one integer $Q$, denoting the number of queries.
    - The next line contains $Q$ space-separated integers, where the $i^{th}$ integer is $X_i$, denoting the $i^{th}$ query.

---

## Output Format

For each test case, print $Q$ space-separated integers denoting the answer to each query.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq Q \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i, X_i \leq 10^6$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.
- The sum of $Q$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
1
5
2 9 3 15 10
4
2 2 3 7
```

**Output**

```text
2 10 3 9
```

**Explanation**

**Test case $1$:** The given array is $[2, 9, 3, 15, 10]$ and there are $4$ queries:
- Query $1$: Given $X = 2$. The elements $2$ and $10$ satisfy the condition. Since $2$ is smaller, we print and remove $2$ from array. The array becomes $A = [9, 3, 15, 10]$.
- Query $2$: Given $X = 2$. The element $10$ satisfies the condition. We print and remove $10$ from array. The array becomes $A = [9, 3, 15]$.
- Query $3$: Given $X = 3$. The elements $3$ and $9$ satisfy the condition. Since $3$ is smaller, we print and remove $3$ from array. The array becomes $A = [9, 15]$.
- Query $4$: Given $X = 7$. No element satisfies the condition, so we have to select $9$ since it is the smallest element present. We print and remove $9$ from array. The array becomes $A = [15]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GCD_QUERIES)

[Contest: Division 1](https://www.codechef.com/START85A/problems/GCD_QUERIES)

[Contest: Division 2](https://www.codechef.com/START85B/problems/GCD_QUERIES)

[Contest: Division 3](https://www.codechef.com/START85C/problems/GCD_QUERIES)

[Contest: Division 4](https://www.codechef.com/START85D/problems/GCD_QUERIES)

***Authors:*** [d_k_7386](https://www.codechef.com/users/d_k_7386)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

2422

#
[](#prerequisites-3)PREREQUISITES:

[Sieve of Eratosthenes](https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html)

#
[](#problem-4)PROBLEM:

You’re given an array of N integers, each between 1 and 10^6.

Answer Q queries of the following form on this array:

- Given an integer x, find the smallest integer y present in A such that \gcd(x, y) \gt 1, print it, and delete it from A.

- If no such y exists, then print and delete the smallest element of A instead.

#
[](#explanation-5)EXPLANATION:

The main observation required to solve this problem is the fact that, if \gcd(x, y) \gt 1, then there must exist a *prime number* p such that p divides both x and y.

So, to answer a given query x, we can do the following:

- Quickly all prime factors of x, say they’re p_1, p_2, \ldots, p_k.

- For each p_i, find the smallest element of the array that’s divisible by p_i, say y_i.

- The answer is then simply \min(y_1, y_2, \ldots, y_k).

- Of course, if none of the y_i exist simply take the smallest element of the array.

The main hurdle is now how we would do this quickly. Prime factorization in \mathcal{O}(\sqrt{x}) each time is almost certainly too slow, since we need to factorize several numbers (all the array elements and the queries).

Notice the constraint A_i \leq 10^6, which we’ll use to our advantage.

Prime factorizing small numbers fast

Notice that for this problem, we don’t really need all the factors of a number: we only need its *prime* factors.

In particular, a number x can only have \leq \log{x} distinct prime factors, since 2^{\log x} = x.

This gives us hope that maybe we can find them all quickly.

Since A_i \leq 10^6, let’s do some preprocessing.

Using a (slightly modified) sieve of Eratosthenes, one can find, for each 1 \leq x \leq 10^6, a list of all its prime factors.

This can be done in \mathcal{O}(M\log\log M), where M = 10^6 here.

Once these lists are stored, prime factorizing a number is simple: just iterate through the list!

Now that we’re done with the prime factorization, let’s move on to answering queries.

We need to support the following:

- For a given prime p, find the smallest element of A that’s divisible by p.

- Delete an element from A, which also requires us to update the information of all primes it’s divisible by.

So, we need a data structure that supports quick insertion/deletion, and quickly finding the minimum.

The easiest way to achieve this is by using `std::set`/`std::multiset` in C++ or `TreeSet` in Java. Coding in Python will require you to be a bit more clever, though it’s still doable — see the editorialist’s code linked below.

At any rate, pick your data structure of choice, and assign one to each prime, using say a map.

Then,

- For each i, quickly prime factorize A_i using the approach discussed above. For each prime p that divides A_i, insert A_i into its corresponding set.

- Notice that this uses \mathcal{O}(N\log{10^6}) memory, since each A_i has \leq \log{A_i} prime factors and so will only be present in that many lists.

- Then, for each query x,

- Prime factorize x as discussed.

- For each prime factor, find the smallest remaining element; after which you’ll know which value needs to be deleted from the array

- To delete an element, simply reverse the insertion process: find each prime factor, and delete A_i from the appropriate list.

Each element is inserted into at most \log{A_i} lists and deleted at most once from each, so the complexity of this part is \mathcal{O}(N\log{10^6}\log N); perhaps with an extra \log depending on implementation.

Each query requires us to iterate through \leq \log x lists; and query each one for the minimum which can be done in \mathcal{O}(1). So, the complexity of this part is \mathcal{O}(Q\log{10^6}), again with maybe an extra \log from a map.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(M\log\log M) precomputation, followed by \mathcal{O}((N+Q)\log N\log M) per test case, where M = 10^6.

#
[](#code-7)CODE:

Setter's code (C++)
``#define ll long long int
#include<bits/stdc++.h>
#define loop(i,a,b) for(ll i=a;i<b;++i)
#define rloop(i,a,b) for(ll i=a;i>=b;i--)
#define in(a,n) for(ll i=0;i<n;++i) cin>>a[i];
#define pb push_back
#define mk make_pair
#define all(v) v.begin(),v.end()
#define dis(v) for(auto i:v)cout<<i<<" ";cout<<endl;
#define display(arr,n) for(int i=0; i<n; i++)cout<<arr[i]<<" ";cout<<endl;
#define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);srand(time(NULL));
#define l(a) a.length()
#define s(a) (ll)a.size()
#define fr first
#define sc second
#define mod 1000000007
#define endl '\n'
#define yes cout<<"Yes"<<endl;
#define no cout<<"No"<<endl;
using namespace std;
#define debug(x) cerr << #x<<" "; _print(x); cerr << endl;
void _print(ll t) {cerr << t;}
void _print(int t) {cerr << t;}
void _print(string t) {cerr << t;}
void _print(char t) {cerr << t;}
void _print(double t) {cerr << t;}
template <class T, class V> void _print(pair <T, V> p);
template <class T> void _print(vector <T> v);
template <class T> void _print(set <T> v);
template <class T, class V> void _print(map <T, V> v);
template <class T> void _print(multiset <T> v);
template <class T, class V> void _print(pair <T, V> p) {cerr << "{"; _print(p.fr); cerr << ","; _print(p.sc); cerr << "}";}
template <class T> void _print(vector <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(set <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T> void _print(multiset <T> v) {cerr << "[ "; for (T i : v) {_print(i); cerr << " ";} cerr << "]";}
template <class T, class V> void _print(map <T, V> v) {cerr << "[ "; for (auto i : v) {_print(i); cerr << " ";} cerr << "]";}

ll add(ll x,ll y)  {ll ans = x+y; return (ans>=mod ? ans - mod : ans);}
ll sub(ll x,ll y)  {ll ans = x-y; return (ans<0 ? ans + mod : ans);}
ll mul(ll x,ll y)  {ll ans = x*y; return (ans>=mod ? ans % mod : ans);}
vector<multiset<ll>> present(1e6+1);
vector<ll> spf;
void fn(){
    spf.assign(1e6+1,0);
    loop(i,0,1e6+1) spf[i] = i;
    loop(i,2,1e6+1){
        if(spf[i] == i) {
            for(int j = i;j<=1e6;j+=i)  spf[j] = min(spf[j],i);
        }
    }
}

vector<ll> prime_fact(ll n){
    vector<ll> ans;
    while(n>1)  {
        int j = spf[n];
        while(n%j == 0) n/=j;
        ans.pb(j);
    }
    return ans;
}

void solve(){
    ll n;   cin>>n;
    vector<ll> v(n);    in(v,n);
    present[1].clear();
    set<ll> used;
    loop(i,0,n){
        present[1].insert(v[i]);
        vector<ll> fact = prime_fact(v[i]);
        for(auto j:fact)    {
            present[j].insert(v[i]);
            used.insert(j);
        }
    }
    ll q;   cin>>q;
    while(q--){
        ll x;   cin>>x;
        vector<ll> fact = prime_fact(x);
        ll mi = INT_MAX;
        for(auto i:fact)
            if(present[i].size() > 0)    mi = min(mi,*present[i].begin());
        if(mi == INT_MAX){
            mi = *present[1].begin();
        }
        fact = prime_fact(mi);
        present[1].erase(present[1].find(mi));
        for(auto i:fact)    {
            present[i].erase(present[i].find(mi));
        }
        cout<<mi<<' ';
    }
    cout<<endl;
    for(auto i:used)    present[i].clear();
}

int main()
{
    fast
    fn();
    int t; cin>>t;
    while(t--) solve();
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
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

    string readOne() {
        assert(pos < (int) buffer.size());
        string res;
        while (pos < (int) buffer.size() && buffer[pos] != ' ' && buffer[pos] != '\n') {
            res += buffer[pos];
            pos++;
        }
        return res;
    }

    string readString(int min_len, int max_len, const string& pattern = "") {
        assert(min_len <= max_len);
        string res = readOne();
        assert(min_len <= (int) res.size());
        assert((int) res.size() <= max_len);
        for (int i = 0; i < (int) res.size(); i++) {
            assert(pattern.empty() || pattern.find(res[i]) != string::npos);
        }
        return res;
    }

    int readInt(int min_val, int max_val) {
        assert(min_val <= max_val);
        int res = stoi(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    long long readLong(long long min_val, long long max_val) {
        assert(min_val <= max_val);
        long long res = stoll(readOne());
        assert(min_val <= res);
        assert(res <= max_val);
        return res;
    }

    vector<int> readInts(int size, int min_val, int max_val) {
        assert(min_val <= max_val);
        vector<int> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readInt(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
    }

    vector<long long> readLongs(int size, long long min_val, long long max_val) {
        assert(min_val <= max_val);
        vector<long long> res(size);
        for (int i = 0; i < size; i++) {
            res[i] = readLong(min_val, max_val);
            if (i != size - 1) {
                readSpace();
            }
        }
        return res;
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

int main() {
    input_checker in;
    const int N = 1e6 + 10;
    vector<vector<int>> f(N);
    vector<bool> ip(N, true);
    for (int i = 2; i < N; i++) {
        if (ip[i]) {
            for (int j = i; j < N; j += i) {
                f[j].emplace_back(i);
                ip[j] = false;
            }
        }
    }
    vector<multiset<int>> st(N);
    int tt = in.readInt(1, 100000);
    in.readEoln();
    int sn = 0;
    while (tt--) {
        int n = in.readInt(1, 2e5);
        in.readEoln();
        auto a = in.readInts(n, 1, 1e6);
        in.readEoln();
        int q = in.readInt(1, n);
        in.readEoln();
        auto b = in.readInts(q, 1, 1e6);
        in.readEoln();
        for (int i = 0; i < n; i++) {
            st[1].emplace(a[i]);
            for (int t : f[a[i]]) {
                st[t].emplace(a[i]);
            }
        }
        for (int x : b) {
            int y = N;
            for (int t : f[x]) {
                if (!st[t].empty()) {
                    y = min(y, *st[t].begin());
                }
            }
            if (y == N) {
                y = *st[1].begin();
            }
            st[1].erase(st[1].find(y));
            cout << y << '\n';
            for (int t : f[y]) {
                st[t].erase(st[t].find(y));
            }
        }
        for (int i = 0; i < n; i++) {
            st[1].clear();
            for (int t : f[a[i]]) {
                st[t].clear();
            }
        }
    }
    assert(sn <= 2e5);
    in.readEof();
    return 0;
}
``

Editorialist's code (Python)
``maxn = 10**6 + 10
prf = [0] * maxn
for i in range(2, maxn):
	if prf[i] > 0: continue
	for j in range(i, maxn, i):
		prf[j] = i

for _ in range(int(input())):
	n = int(input())
	mapper = {}
	id = 0
	a = list(map(int, input().split()))
	vals = [ ]
	mark = [0]*n
	for i in range(n):
		x = a[i]
		while x > 1:
			p = prf[x]
			if p not in mapper:
				mapper[p] = id
				vals.append([ ])
				id += 1
			vals[mapper[p]].append(i)

			while x%p == 0: x //= p
	for i in range(id):
		vals[i].sort(key = lambda x: -a[x])

	ord = list(range(n))
	ord.sort(key= lambda x: -a[x])

	q = int(input())
	queries = list(map(int, input().split()))

	for x in queries:
		primes = []
		while x > 1:
			p = prf[x]
			while x%p == 0: x //= p
			primes.append(p)

		choice = -1
		for p in primes:
			if p not in mapper: continue
			loc = mapper[p]
			while vals[loc]:
				if mark[vals[loc][-1]]: vals[loc].pop()
				else:
					who = vals[loc][-1]
					if choice == -1 or a[who] < a[choice]: choice = who
					break
		if choice == -1:
			while mark[ord[-1]] == 1: ord.pop()
			choice = ord[-1]

		print(a[choice], end = ' ')
		mark[choice] = 1
``

</details>
