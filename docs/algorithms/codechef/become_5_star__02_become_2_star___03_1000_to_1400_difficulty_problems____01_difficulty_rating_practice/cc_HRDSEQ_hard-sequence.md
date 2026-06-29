# Hard Sequence

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HRDSEQ |
| Difficulty Rating | 1278 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [HRDSEQ](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/HRDSEQ) |

---

## Problem Statement

Chef decided to write an infinite sequence. Initially, he wrote $0$, and then he started repeating the following process:
- Look at the last element written so far (the $l$-th element if the sequence has length $l$ so far); let's denote it by $x$.
- If $x$ does not occur anywhere earlier in the sequence, the next element in the sequence is $0$.
- Otherwise, look at the previous occurrence of $x$ in the sequence, i.e. the $k$-th element, where $k \lt l$, this element is equal to $x$ and all elements between the $k+1$-th and $l-1$-th are different from $x$. The next element is $l-k$, i.e. the distance between the last two occurrences of $x$.

The resulting sequence is $(0, 0, 1, 0, 2, 0, 2, 2, 1, \ldots)$: the second element is $0$ since $0$ occurs only once in the sequence $(0)$, the third element is $1$ since the distance between the two occurrences of $0$ in the sequence $(0, 0)$ is $1$, the fourth element is $0$ since $1$ occurs only once in the sequence $(0, 0, 1)$, and so on.

Chef has given you a task to perform. Consider the $N$-th element of the sequence (denoted by $x$) and the first $N$ elements of the sequence. Find the number of occurrences of $x$ among these $N$ elements.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
For each test case, print a single line containing one integer ― the number of occurrences of the $N$-th element.

### Constraints
- $1 \le T \le 128$
- $1 \le N \le 128$

### Subtasks
**Subtask #1 (30 points):** $1 \le N \le 16$

**Subtask #2 (70 points):** $1 \le N \le 128$

---

## Examples

**Example 1**

**Input**

```text
1
2
```

**Output**

```text
2
```

**Explanation**

**Example case 1:** The $2$-nd element is $0$. It occurs twice among the first two elements, since the first two elements are both $0$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HRDSEQ)

[Div-2 Contest](https://www.codechef.com/NOV19B/problems/HRDSEQ)

***Author:***  [Mayank Padia](https://www.codechef.com/users/vladprog)

***Tester:***  [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

***Editorialist:***  [Michael Nematollahi](https://www.codechef.com/users/watcher)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

NONE

# QUICK EXPLANATION:

Generate the described sequence and count the number of occurrences of A[N] in the first N elements.

# EXPLANATION:

To solve this problem, we’re going to simulate the process of generating the sequence.

First of all, note that the maximum number in the sequence is non-negative and does not exceed the length of the sequence. This is because each number is the result of i - j where i and j are two indices of the sequence where 0 \le j < i.

Hence, we can keep an array lst, where lst[x] stores the index of the last occurrence of the number x in the sequence so far before the last element. By convention, we assume that if lst[x] = -1, it means that x has not occurred in the sequence before the last element.

Taking this all into account, the code to generate the sequence goes like this:

Expand to view
``for (int i = 0; i + 1 < N; i++){
    if (lst[a[i]] == -1)
        a[i+1] = 0;
    else
        a[i+1] = i - lst[a[i]];
    lst[a[i]] = i;
}
``

After generating the sequence, all that’s left to do is to loop through the sequence and count the number of occurrences of the last number.

The time complexity of this solution is O(N) per test case.

To view an implementation of the described solution, refer to the editorialist’s solution. Note that in this implementation, the sequence is generated only once before processing the test cases.

# SOLUTIONS:

Setter's Solution
``/**
*        __    _____ _____ ____  _____ _____ _____
*       |  |  |     |  _  |    \|     |   | |   __|
*       |  |__|  |  |     |  |  |-   -| | | |  |  |_ _ _
*       |_____|_____|__|__|____/|_____|_|___|_____|_|_|_|
**/
#include<bits/stdc++.h>
typedef long long ll;
typedef double ld;
#define vll vector<ll>
#define vvll vector< vll >
#define vld vector< ld >
#define vvld vector< vld >
#define pll pair<ll ,ll >
#define vllp vector< pll >
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define endl "\n"
#define test ll t;cin>>t;while(t--)
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define F first
#define S second

#define forn(i,n) for(ll (i) = 0 ; (i) < (n) ; ++(i))
#define for1(i,n) for(ll (i) = 1 ; (i) <= (n) ; ++(i))
#define forr(i,n) for(ll (i) = (n)-1 ; (i)>=0 ; --(i))
#define forab(i,a,b,c) for(ll (i) = a ; (i) <= (b) ; (i)+=(c))
#define MAX 1000000007
using namespace std;

vll sieve;
void Sieve(int N){
 const ll maxn = N;
 sieve.resize(maxn);
 forn(i,maxn) sieve[i] = i;
 sieve[1] = -1;
 sieve[0] = -1;
 forab(i,2,maxn,1) if(i == sieve[i]) for(ll j = 2*i ; j < maxn ; j+=i) if(sieve[j] == j) sieve[j] = i;
}
ll extended_GCD(ll a , ll b , ll &x , ll &y){
 if(a == 0){
     x = 0;
     y = 1;
     return b;
 }
 ll x1 , y1;
 ll gcd = extended_GCD(b%a , a , x1 , y1);
 x = y1 - (b/a)*x1;
 y = x1;
 return gcd;
}
ll power(ll a, ll b, ll m = MOD) {
    a %= m;
    ll res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
ll modinv(ll a , ll mod = MOD){
 ll x , y;
 extended_GCD(a , mod , x , y);
 if(x < 0) x += mod;
 return x;
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void solve(){
 ll n;
    cin>>n;
    map<ll,ll> m,m1,m2;
    ll a[n]={0};
    if(n==1||n==2)
    {
     cout<<n<<endl;
     return;
    }
    m[0]=2;
    m1[0]=1;
    m2[0]=0;
    a[2]=1;
    for (int i = 2; i < n; ++i)
    {
     if(m[a[i-1]]>1)
     {
         a[i]=m1[a[i-1]]-m2[a[i-1]];
         m[a[i]]++;
         m2[a[i]]=m1[a[i]];
         m1[a[i]]=i;
     }
     else
     {
         a[i]=0;
         m[0]++;
         m2[a[i]]=m1[a[i]];
         m1[0]=i;
     }
    }
 cout<<m[a[n-1]]<<endl;

 }
int main(){
     #ifndef ONLINE_JUDGE
         freopen("input.txt","r",stdin);
         freopen("output.txt","w",stdout);
     #endif
    ios::sync_with_stdio(0); cin.tie(0);
 int t=1;
    cin>>t;
    while(t--){
        solve();
    }
return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif

#define rep(i, n)    for(int i = 0; i < (n); ++i)
#define repA(i, a, n)  for(int i = a; i <= (n); ++i)
#define repD(i, a, n)  for(int i = a; i >= (n); --i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
#define fill(a)  memset(a, 0, sizeof (a))
#define fst first
#define snd second
#define mp make_pair
#define pb push_back
typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

void pre(){

}

void solve(){
	int n;
	scanf("%d\n",&n);
	assert(n>=1&&n<=128);
	vi v(2,0);
	while(sz(v)<=n){
		int ans = 0;
		repD(i,sz(v)-2,0){
			if(v[i]==v.back()){
				ans = sz(v)-1-i;
				break;
			}
		}
		v.pb(ans);
	}
	int cnt = 0;
	rep(i,n) if(v[i]==v[n-1]) cnt++;
	cout<<cnt<<'\n';
}

int main() {
	cin.sync_with_stdio(0); cin.tie(0);
	cin.exceptions(cin.failbit);
	pre();
	int n;
	scanf("%d\n",&n);
	assert(n>=1&&n<=128);
	rep(i,n) solve();
	return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define F first
#define S second

const int MAXN = 128 + 10;

int n, a[MAXN], lst[MAXN];

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	memset(lst, -1, sizeof(lst));
	a[0] = 0;
	for (int i = 0; i + 1 < MAXN; i++){
		if (lst[a[i]] == -1)
			a[i+1] = 0;
		else
			a[i+1] = i - lst[a[i]];
		lst[a[i]] = i;
	}

	int te;	cin >> te;
	while (te--){
		int n; cin >> n;
		int ans = 0;
		for (int i = 0; i < n; i++)
			ans += a[i] == a[n-1];
		cout << ans << "\n";
	}
	return 0;
}
``

</details>
