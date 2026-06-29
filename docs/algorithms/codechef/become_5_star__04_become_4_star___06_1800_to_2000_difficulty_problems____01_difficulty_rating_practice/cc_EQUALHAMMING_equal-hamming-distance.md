# Equal Hamming Distance

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQUALHAMMING |
| Difficulty Rating | 1873 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [EQUALHAMMING](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/EQUALHAMMING) |

---

## Problem Statement

Chef is given two binary strings $A$ and $B$, each having length $N$.

Chef wants to find the number of binary strings $C$, of length $N$, such that $H(A, C) = H(B, C)$, where $H(X, Y)$ denotes the *hamming distance* between the strings $X$ and $Y$.

Since the answer can be large, output it modulo $10^9+7$.

Note: [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) between two strings of equal length is the number of positions at which the corresponding characters are different.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$, the length of the strings.
    - The second line contains the binary string $A$.
    - The third line contains the binary string $B$.

---

## Output Format

For each test case, output in a new line, the number of binary strings $C$ which satisfy the given conditions modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $A$ and $B$ consist of $0$ and $1$ only.
- Sum of $N$ over all test cases do not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
11
00
5
10101
10101
3
101
011
```

**Output**

```text
2
32
4
```

**Explanation**

**Test case $1$:** The number of strings $C$, of length $2$, such that $H(A, C) = H(B, C)$ is $2$. The strings are:
- $C = 10$: Here, $H(11, 10) = H(00, 10) = 1$, as there is only one position where the corresponding characters are different.
- $C = 01$: Here, $H(11, 01) = H(00, 01) = 1$.

**Test case $3$:** The number of strings $C$, of length $3$, such that $H(A, C) = H(B, C)$ is $4$. The strings are:
- $C = 000$: Here, $H(101, 000) = H(011, 000) = 2$, as there are two positions where the corresponding characters are different.
- $C = 111$: Here, $H(101, 111) = H(011, 111) = 1$, as there is only one position where the corresponding characters are different.
- $C = 001$: Here, $H(101, 001) = H(011, 001) = 1$, as there is only one position where the corresponding characters are different.
- $C = 110$: Here, $H(101, 110) = H(011, 110) = 2$, as there are two positions where the corresponding characters are different.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
11
00
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
10101
10101
```

**Output for this case**

```text
32
```



#### Test case 3

**Input for this case**

```text
3
101
011
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EQUALHAMMING)

[Contest: Division 1](https://www.codechef.com/START75A/problems/EQUALHAMMING)

[Contest: Division 2](https://www.codechef.com/START75B/problems/EQUALHAMMING)

[Contest: Division 3](https://www.codechef.com/START75C/problems/EQUALHAMMING)

[Contest: Division 4](https://www.codechef.com/START75D/problems/EQUALHAMMING)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Basic combinatorics

#
[](#problem-4)PROBLEM:

Given two binary strings A and B of length N, count the number of binary strings C of length N such that \text{dist}(A, C) = \text{dist}(B, C).

\text{dist}(A, C) denotes the hamming distance between A and C.

#
[](#explanation-5)EXPLANATION:

Hamming distance is computed as the sum of N individual terms; one corresponding to each index. So, let’s see how each index affects the equality.

Consider an index i.

- If A_i = B_i, then this index either contributes 0 to both \text{dist}(A, C) and \text{dist}(B, C) (if C_i = A_i); or contributes 1 to both (if C_i \neq A_i).

In other words, it doesn’t affect the equality at all, so we can freely choose C_i = 0 or C_i = 1 here.

- If A_i \neq B_i, then depending on our choice of C_i, this index either contributes 1 to \text{dist}(A, C) and 0 to \text{dist}(B, C); or vice versa.

Clearly, we must choose \text{dist}(A, C) and \text{dist}(B, C) an equal number of times for the equality to hold in the end.

So, suppose there are K positions such that A_i \neq B_i; and N - K positions where they’re equal.

If K is odd, the answer is immediately 0, since as we noted we need to split these K positions equally. Let’s deal with even K now.

At \frac{K}{2} of the unequal positions, we must fix C_i to ensure that C_i \neq A_i.

At the other \frac{K}{2} of the unequal positions, we must fix C_i to ensure that C_i \neq B_i.

The remaining N-K positions are ‘free’, and each have two options.

There are \binom{K}{K/2} ways to choose K/2 positions out of K, and then the values at these K positions are fixed.

The other positions have 2^{N-K} options in total.

Multiplying everything together, the final answer is

\binom{K}{K/2} \times 2^{N-K}

Computing binomial coefficients under modulo requires the use of modular division: you can see how [here](https://cp-algorithms.com/combinatorics/binomial-coefficients.html).

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``//Utkarsh.25dec
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
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
int sumN=0;
ll fact[N];
ll invfact[N];
ll inv[N];
void factorialsComputation()
{
    inv[0]=inv[1]=1;
    fact[0]=fact[1]=1;
    invfact[0]=invfact[1]=1;
    for(int i=2;i<N;i++)
    {
        inv[i]=(inv[mod%i]*(mod-mod/i))%mod;
        fact[i]=(fact[i-1]*i)%mod;
        invfact[i]=(invfact[i-1]*inv[i])%mod;
    }
}
ll ncr(ll n,ll r)
{
    ll ans=fact[n]*invfact[r];
    ans%=mod;
    ans*=invfact[n-r];
    ans%=mod;
    return ans;
}
void solve()
{
    int n=readInt(1,200000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    string A=readString(n,n,'\n');
    string B=readString(n,n,'\n');
    int good=0,bad=0;
    for(int i=0;i<n;i++)
    {
        assert(A[i]=='0' || A[i]=='1');
        assert(B[i]=='0' || B[i]=='1');
        if(A[i]==B[i])
            good++;
        else
            bad++;
    }
    if(bad%2==1)
    {
        cout<<0<<'\n';
        return;
    }
    ll ans=power(2,good)*ncr(bad,bad/2);
    ans%=mod;
    cout<<ans<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    factorialsComputation();
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``// Jai Shree Ram

#include<bits/stdc++.h>
using namespace std;

#define rep(i,a,n)     for(int i=a;i<n;i++)
#define ll             long long
#define int            long long
#define pb             push_back
#define all(v)         v.begin(),v.end()
#define endl           "\n"
#define x              first
#define y              second
#define gcd(a,b)       __gcd(a,b)
#define mem1(a)        memset(a,-1,sizeof(a))
#define mem0(a)        memset(a,0,sizeof(a))
#define sz(a)          (int)a.size()
#define pii            pair<int,int>
#define hell           1000000007
#define elasped_time   1.0 * clock() / CLOCKS_PER_SEC

template<typename T1,typename T2>istream& operator>>(istream& in,pair<T1,T2> &a){in>>a.x>>a.y;return in;}
template<typename T1,typename T2>ostream& operator<<(ostream& out,pair<T1,T2> a){out<<a.x<<" "<<a.y;return out;}
template<typename T,typename T1>T maxs(T &a,T1 b){if(b>a)a=b;return a;}
template<typename T,typename T1>T mins(T &a,T1 b){if(b<a)a=b;return a;}

// -------------------- Input Checker Start --------------------

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0, fi = -1;
    bool is_neg = false;
    while(true)
    {
        char g = getchar();
        if(g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if(cnt == 0)
                fi = g - '0';
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);
            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if(g == endd)
        {
            if(is_neg)
                x = -x;
            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(false);
            }
            return x;
        }
        else
        {
            assert(false);
        }
    }
}

string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while(true)
    {
        char g = getchar();
        assert(g != -1);
        if(g == endd)
            break;
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}

long long readIntSp(long long l, long long r) { return readInt(l, r, ' '); }
long long readIntLn(long long l, long long r) { return readInt(l, r, '\n'); }
string readStringLn(int l, int r) { return readString(l, r, '\n'); }
string readStringSp(int l, int r) { return readString(l, r, ' '); }
void readEOF() { assert(getchar() == EOF); }

vector<int> readVectorInt(int n, long long l, long long r)
{
    vector<int> a(n);
    for(int i = 0; i < n - 1; i++)
        a[i] = readIntSp(l, r);
    a[n - 1] = readIntLn(l, r);
    return a;
}

// -------------------- Input Checker End --------------------

const int MOD = hell;

struct mod_int {
    int val;

    mod_int(long long v = 0) {
        if (v < 0)
            v = v % MOD + MOD;

        if (v >= MOD)
            v %= MOD;

        val = v;
    }

    static int mod_inv(int a, int m = MOD) {
        int g = m, r = a, x = 0, y = 1;

        while (r != 0) {
            int q = g / r;
            g %= r; swap(g, r);
            x -= q * y; swap(x, y);
        }

        return x < 0 ? x + m : x;
    }

    explicit operator int() const {
        return val;
    }

    mod_int& operator+=(const mod_int &other) {
        val += other.val;
        if (val >= MOD) val -= MOD;
        return *this;
    }

    mod_int& operator-=(const mod_int &other) {
        val -= other.val;
        if (val < 0) val += MOD;
        return *this;
    }

    static unsigned fast_mod(uint64_t x, unsigned m = MOD) {
           #if !defined(_WIN32) || defined(_WIN64)
                return x % m;
           #endif
           unsigned x_high = x >> 32, x_low = (unsigned) x;
           unsigned quot, rem;
           asm("divl %4\n"
            : "=a" (quot), "=d" (rem)
            : "d" (x_high), "a" (x_low), "r" (m));
           return rem;
    }

    mod_int& operator*=(const mod_int &other) {
        val = fast_mod((uint64_t) val * other.val);
        return *this;
    }

    mod_int& operator/=(const mod_int &other) {
        return *this *= other.inv();
    }

    friend mod_int operator+(const mod_int &a, const mod_int &b) { return mod_int(a) += b; }
    friend mod_int operator-(const mod_int &a, const mod_int &b) { return mod_int(a) -= b; }
    friend mod_int operator*(const mod_int &a, const mod_int &b) { return mod_int(a) *= b; }
    friend mod_int operator/(const mod_int &a, const mod_int &b) { return mod_int(a) /= b; }

    mod_int& operator++() {
        val = val == MOD - 1 ? 0 : val + 1;
        return *this;
    }

    mod_int& operator--() {
        val = val == 0 ? MOD - 1 : val - 1;
        return *this;
    }

    mod_int operator++(int32_t) { mod_int before = *this; ++*this; return before; }
    mod_int operator--(int32_t) { mod_int before = *this; --*this; return before; }

    mod_int operator-() const {
        return val == 0 ? 0 : MOD - val;
    }

    bool operator==(const mod_int &other) const { return val == other.val; }
    bool operator!=(const mod_int &other) const { return val != other.val; }

    mod_int inv() const {
        return mod_inv(val);
    }

    mod_int pow(long long p) const {
        assert(p >= 0);
        mod_int a = *this, result = 1;

        while (p > 0) {
            if (p & 1)
                result *= a;

            a *= a;
            p >>= 1;
        }

        return result;
    }

    friend ostream& operator<<(ostream &stream, const mod_int &m) {
        return stream << m.val;
    }
    friend istream& operator >> (istream &stream, mod_int &m) {
        return stream>>m.val;
    }
};
#define NCR
const int N=1e6;
mod_int fact[N],inv[N];
void init(int n=N){
	fact[0]=inv[0]=inv[1]=1;
	rep(i,1,N)fact[i]=i*fact[i-1];
	rep(i,2,N)inv[i]=fact[i].inv();
}
mod_int C(int n,int r){
	if(r>n || r<0)return 0;
	return fact[n]*inv[n-r]*inv[r];
}

int solve(){

               int n = readIntLn(1, 2e5);
               static int sum_n = 0;
               sum_n += n;

               assert(sum_n <= 2e5);

               string a = readStringLn(n, n);
               string b = readStringLn(n,n);
               for(auto &i: a){
                        assert(i == '0' or i == '1');
               }
               for(auto &i: b){
                        assert(i == '1' or i == '0');
               }
               int cnt = 0;

               for(int i = 0; i < n; i++){
               		cnt += a[i] != b[i];
               }
               if(cnt & 1){
               		cout << "0" << endl;
               		return 0;
               }
               cout << mod_int(2).pow(n - cnt) * C(cnt, cnt / 2) << endl;

 return 0;
}
signed main(){
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    #ifdef SIEVE
    sieve();
    #endif
    #ifdef NCR
    init();
    #endif
    int t = readIntLn(1, 1000);
    while(t--){
        solve();
    }
    return 0;
}
``

Editorialist's code (Python)
``mod = 10**9 + 7
def C(n, r):
    ret = 1
    for i in range(1, r+1):
        ret = ret * (n-i+1) * pow(i, mod-2, mod)
        ret %= mod
    return ret
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    differ = 0
    for i in range(n):
        differ += a[i] != b[i]
    if differ%2 == 1: print(0)
    else: print(pow(2, n - differ, mod) * C(differ, differ//2) % mod)
``

</details>
