# Mystical Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORGAND |
| Difficulty Rating | 1702 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [XORGAND](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/XORGAND) |

---

## Problem Statement

A number $M$ is said to be a *Mystical Number* with respect to a number $X$ if $(M \oplus X) \gt (M \& X)$.

You are given an array $A$ of size $N$. You are also given $Q$ queries. Each query consists of three integers $L$, $R$, and $X$.

For each query, find the count of *Mystical Numbers* in the subarray $A[L:R]$ with respect to the number $X$.

**Notes:**
- $\oplus$ represents the [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation and $\&$ represents the [Bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operation.
- $A[L:R]$ denotes the subarray $A[L], A[L+1], \ldots, A[R]$.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.
- The third line of each test case contains an integer $Q$ - denoting the number of queries.
- The $i^{th}$ of the next $Q$ lines contains three space-separated integers $L$ , $R$ and $X$.

---

## Output Format

For each testcase,
- For each query, print in a new line, the count of *Mystical Numbers* among $A[L], A[L+1], \ldots, A[R]$ with respect to the number $X$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 2 \cdot 10^5$
- $0 \leq A_i \lt 2^{31}$
- $1 \leq Q \leq 2 \cdot 10^5$
- $1 \leq L \leq R \leq N$
- $0 \leq X \lt 2^{31}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- Sum of $Q$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
1
5
1 2 3 4 5
2
1 5 4
2 5 2
```

**Output**

```text
3
2
```

**Explanation**

**Test case $1$**:
- Query $1$: $L = 1 , R = 5 , X = 4$.
    - $A_1 \oplus X = 5, A_1 \& X = 0$.
    - $A_2 \oplus X = 6, A_2 \& X = 0$.
    - $A_3 \oplus X = 7, A_3 \& X = 0$.
    - $A_4 \oplus X = 0, A_4 \& X = 4$.
    - $A_5 \oplus X = 1, A_5 \& X = 4$.

Mystical numbers are $A_1 , A_2,$ and $A_3$ with respect to $4$. Therefore, the answer to this query is $3$.
- Query $2$: $L = 2 , R = 5 , X = 2$.
    - $A_2 \oplus X = 0, A_2 \& X = 2$.
    - $A_3 \oplus X = 1, A_3 \& X = 2$.
    - $A_4 \oplus X = 6, A_4 \& X = 0$.
    - $A_5 \oplus X = 7, A_5 \& X = 0$.

Mystical numbers are $A_4$ and $A_5$ with respect to $2$. Therefore , the answer to this query is $2$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/XORGAND)

[Contest: Division 1](https://www.codechef.com/MAY221A/problems/XORGAND)

[Contest: Division 2](https://www.codechef.com/MAY221B/problems/XORGAND)

[Contest: Division 3](https://www.codechef.com/MAY221C/problems/XORGAND)

[Contest: Division 4](https://www.codechef.com/MAY221D/problems/XORGAND)

***Author:*** [Ankush Chhabra](https://www.codechef.com/users/mystic_ankush)

***Testers:*** [Satyam](https://www.codechef.com/users/satyam_343), [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

Bitwise operations, [prefix sums](https://usaco.guide/silver/prefix-sums?lang=cpp)

#
[](#problem-4)PROBLEM:

Given an array A of N integers and Q queries of the form (L, R, X), find for each query the number of indices L \leq i \leq R such that (A_i \oplus X) \gt (A_i \& X)

#
[](#explanation-5)EXPLANATION:

Hint 1

Look at the highest set bit of A_i and X — what does this tell you about A_i \oplus X and A_i \& X?

Hint 2

Now use prefix sums!

Full solution

Of course, checking for every query if each A_i with L \leq i \leq R satisfies the condition is \mathcal{O}(QN), which is too slow. As is always the case with such problems, we need to observe some structure to make this faster.

The key idea here is to look at the *highest set bit* of a number, i.e, the highest integer k such that 2^k occurs in the binary representation of that number. For example, the highest set bit of 4 is 2 (since 4 = 100_2), and the highest set bit of 21 is 4 (since 21 = 10101_2).

For convenience, I’ll denote the highest set bit of an integer y > 0 as h(y). Note that h(y) is not defined when y = 0, since there are no set bits, so we consider it separately.

Now let’s look at the given operation in terms of the highest set bit. There are a few cases to consider.

Cases

- Suppose X = 0. Then, A_i \& X = A_i \& 0 is always zero, so A_i \oplus X > A_i \& X is always going to be satisfied as long as A_i \oplus X > 0. But A_i \oplus X = A_i \oplus  0 = A_i, so we just need to count the number of elements in range that are positive, i.e, non-zero.

- Suppose X > 0. Now,

- If A_i = 0 the condition is always satisfied, with the same logic as above.

- What happens when h(X) = h(A_i)? Notice that X \& A_i will then have this highest bit set, but X \oplus A_i will not. No higher bits of X \oplus A_i will be set either, which means that X \oplus A_i < X \& A_i always.

- Finally, what if h(X)  \neq h(A_i)? Then, the highest set bit of X \oplus A_i is \max(h(X), h(A_i), whereas the highest set bit of X \& A_i is always **strictly** less than \max(h(X), h(A_i). In other words, X\oplus A_i > X \& A_i always!

With our cases in hand, it’s easy to see that the problem reduces to the following:

- If X = 0, count the number of integers in range that are **not** zero

- If X > 0, count the number of integers A_i in range such that h(X)  \neq h(A_i)

Doing this fast is a simple application of prefix sums, as follows:

For each 0 \leq b \lt 31 and each 1 \leq i \leq N, let P_{b, i} denote the number of indices j such that 1 \leq j \leq i, and h(A_j) = b. P_{b, i} is easily computed from P_{b, i-1} by knowing the value of h(A_i) (add 1 if h(A_i) = b, add 0 otherwise), so this entire array can be computed in \mathcal{O}(31 \cdot N).

Notice that this is essentially 31 separate prefix sum arrays, one corresponding to each bit. Similarly, create a prefix sum array corresponding to the value 0, since it doesn’t come under any of these.

With these arrays in hand, the answer to a query (L, R, X) is simply R-L+1 - (P_{b, R} - P_{b, L-1}), where b = h(X) (and of course, treating the X = 0 case similarly).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(Q + 31\cdot N) per test.

#
[](#code-7)CODE:

Author (C++)
``#include<bits/stdc++.h>
#define ll long long int
#define pb push_back
#define ff first
#define ss second
#define ii insert
#define mem(l,r) memset(l,r,sizeof(l))
#define sorta(a,n) sort(a+1,a+1+n)
#define sortv(v) sort(v.begin(),v.end())
#define revs(s) reverse(s.begin(),s.end())
#define reva(a,n) reverse(a+1,a+1+n)
#define fastio ios::sync_with_stdio(false), cin.tie(NULL) ,cout.tie(NULL);
const int N=1e5+5;
const int mod=1e9+7;
const ll int_max=1e18;
const ll int_min=-1e18;
#define rep(i,j,k) for(ll i=j;i<=k;i++)
#define repr(i,j,k) for(ll i=j;i>=k;i--)
const long double PI = acos(-1);
using namespace std;
ll sumn=0,sumq=0;
void solve(ll t,ll finalt)
{
 	ll n;
 	cin>>n;
	sumn+=n;
    assert(n>=1 && n<=200000);
 	ll a[n+2];
 	rep(i,1,n)
 	cin>>a[i];
	vector<ll>zeroes(n+2,0);
 	rep(i,1,n)
 	{
        assert(a[i]>=0 && a[i]<pow(2,31));
		zeroes[i]+=zeroes[i-1];
		zeroes[i]+=(a[i]==0);
		if(a[i]==0){
			a[i]=-1;
			continue;
		}
 		a[i]=log2(a[i]);
 	}
 	vector<vector<ll>>prefix(n+2,vector<ll>(31,0));
 	rep(i,0,30)
 	{
 		prefix[1][i]=(a[1]==i);
 		rep(j,2,n)
 		{
 			prefix[j][i]=prefix[j-1][i]+(a[j]==i);
 		}
 	}
 	ll q;
 	cin>>q;
	sumq+=q;
    assert(q>=1 && q<=200000);
 	rep(i,1,q)
 	{
 		ll l,r,x;
 		cin>>l>>r>>x;
		assert(l>=1 && l<=n);
		assert(r>=1 && r<=n);
        assert(l<=r);
        assert(x>=0 && x<pow(2,31));
		ll ans=0;
		if(x==0)
		{
			ans+=(r-l+1)-(zeroes[r]-zeroes[l]+(a[l]==-1));
		}
		else
		{
			ll high=log2(x);
			repr(i,30,0)
			{
				if(high!=i)
				{
					ans+=prefix[r][i]-prefix[l][i]+(a[l]==i);
				}
			}
			ans+=(zeroes[r]-zeroes[l]+(a[l]==-1));
		}
 		cout<<ans<<'\n';
 	}
}
int main() {
    fastio
    //freopen("input15.txt","r",stdin);
    //freopen("output15.txt","w",stdout);
    int t;
    cin>>t;
    assert(t>=1 && t<=100);
    rep(i,1,t)
    {
       solve(i,t);
    }
	assert(sumn>=1 && sumn<=200000);
	assert(sumq>=1 && sumq<=200000);
}
``

Tester (inov_360, C++)
``#include <bits/stdc++.h>
using namespace std;

/*
------------------------Input Checker----------------------------------
*/

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

/*
------------------------Main code starts here----------------------------------
*/

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define pb push_back

int sum_n = 0, sum_m = 0, sum = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll INF = 1e18;
ll mod = 1000000007;
using ii = pair<ll,ll>;

void solve()
{

    int n = readIntLn(1,2e5);
    sum_n+=n;
    int a[n];
    rep(i,n){
        if(i<n-1) a[i] = readIntSp(0,(1ll<<31)-1);
        else a[i] = readIntLn(0, (1ll<<31)-1);
    }

    vector<vector<int> > v(n, vector<int>(32,0));
    rep(i,n){
        if(i){
            rep(j,32) v[i][j]=v[i-1][j];
        }
        if(a[i]==0){
            v[i][0]++;
            continue;
        }

        rev(j,30){
            if(a[i]&(1<<j)){
                v[i][j+1]++;
                break;
            }
        }
    }

    int q = readIntLn(1,2e5);
    sum_m+=q;

    int l,r,x;
    rep(i,q){
        l = readIntSp(1,n);
        r = readIntSp(1,n);
        r--, l--;
        x = readIntLn(0,(1ll<<31)-1);

        int msb=0;
        // if(x==0) msb = 0;
        // else{
            rev(j,30){
                if(x&(1<<j)){
                    msb = j+1;
                    break;
                }
            }

        //}

            cout<<r-l+1-v[r][msb]+(l>0?v[l-1][msb]:0)<<'\n';
    }

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,100);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_n<=2e5 and sum_m<=2e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<" "<<sum_m<<'\n';
    // cerr<<"Maximum length : " << max_n <<'\n';
    // // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester (satyam_343, C++)
``#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast,unroll-loops")
#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif
#define ll long long

/*
------------------------Input Checker----------------------------------
*/

long long readInt(long long l,long long r,char endd){
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true){
        char g=getchar();
        if(g=='-'){
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g && g<='9'){
            x*=10;
            x+=g-'0';
            if(cnt==0){
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd){
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l,int r,char endd){
    string ret="";
    int cnt=0;
    while(true){
        char g=getchar();
        assert(g!=-1);
        if(g==endd){
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt && cnt<=r);
    return ret;
}
long long readIntSp(long long l,long long r){
    return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
    return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
    return readString(l,r,'\n');
}
string readStringSp(int l,int r){
    return readString(l,r,' ');
}

/*
------------------------Main code starts here----------------------------------
*/
ll MAX=100000;
vector<ll> readv(ll n){
    vector<ll> a;
    ll x,y=1LL<<31; y--;
    for(ll i=1;i<n;i++){
        x=readIntSp(0,y);
        a.push_back(x);
    }
    x=readIntLn(0,y);
    a.push_back(x);
    return a;
}
ll sum_n=0,sum_q=0;
void solve(){
    ll n=readIntLn(1,2e5);
    sum_n+=n;
    vector<ll> a=readv(n);
    vector<vector<ll>> freq(32,vector<ll>(n+5,0));
    vector<ll> zro(n+5,0);
    for(ll i=0;i<n;i++){
        for(ll j=30;j>=0;j--){
            if(a[i]&(1<<j)){
                freq[j][i+1]++;
                break;
            }
        }
        zro[i+1]=(a[i]==0)+zro[i];
    }
    for(ll i=0;i<31;i++){
        for(ll j=1;j<=n;j++){
            freq[i][j]+=freq[i][j-1];
        }
    }
    ll q=readIntLn(1,2e5);
    sum_q+=q;
    while(q--){
        ll l=readIntSp(1,n); ll r=readIntSp(l,n); ll x=readIntLn(0,(1LL<<31)-1);
        ll ans=0;
        if(x!=0){
            ans+=zro[r]-zro[l-1];
        }
        for(ll j=31;j>=0;j--){
            if(x&(1LL<<j)){
                x=0;
                continue;
            }
            ans+=freq[j][r]-freq[j][l-1];
        }
        cout<<ans<<"\n";
    }
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    ll test_cases=readIntLn(1,1e2);
    while(test_cases--){
        solve();
    }
    assert(getchar()==-1);
    assert(sum_n<=(2e5));
    assert(sum_q<=(2e5));
    return 0;
}
``

Editorialist (C++)
``#include "bits/stdc++.h"
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	auto get_hsb = [] (ll x) {
		for (int bit = 31; bit >= 0; --bit) {
			if (x & (1LL<<bit)) return bit;
		}
		return 32;
	};

	int t; cin >> t;
	while (t--) {
		int n; cin >> n;
		vector<ll> a(n);
		for (ll &x : a) cin >> x;
		vector<array<ll, 33>> pref_hsb(n);
		for (int i = 0; i < n; ++i) {
			if (i) pref_hsb[i] = pref_hsb[i-1];
			++pref_hsb[i][get_hsb(a[i])];
		}
		auto get = [&] (int L, int R, int b) {
			int ret = pref_hsb[R][b];
			if (L) ret -= pref_hsb[L-1][b];
			return ret;
		};

		int q; cin >> q;
		while (q--) {
			int L, R, x; cin >> L >> R >> x;
			cout << R-L+1 - get(L-1, R-1, get_hsb(x)) << '\n';
		}
	}
}
``

</details>
