# Expected Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EXPECTEDSUM |
| Difficulty Rating | 2495 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [EXPECTEDSUM](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/EXPECTEDSUM) |

---

## Problem Statement

There are $N$ chits, out of which, $A$ chits have $1$ written on them and $B$ $(A+B = N)$ chits have $0$ written on them.

Chef and Chefina are taking alternate turns. They both have a personal score which is initially set to $0$. Chef starts first. On their turn, a player will:
- Pick a random chit among the available chits;
- Add the number written on the chit to their personal score;
- Remove the chit that was picked.

Determine the [expected](https://en.wikipedia.org/wiki/Expected_value) score of Chef after all chits have been picked.

The expected score can be written in the form of $\frac{P}{Q}$ such that $Q$ is not divisible by $998244353$ and its guaranteed that for testcases that $Q$ is not a multiple of $998244353$. Output the value of $P \cdot Q^{-1}$ mod $998244353$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $A$ and $B$, the number of chits having $1$ and $0$ respectively.

---

## Output Format

For each test case, output the expected score of Chef.
The expected score can be written in the form of $\frac{P}{Q}$. Output the value of $P \cdot Q^{-1}$ mod $998244353$.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A, B \leq 10^9$
- $1 \leq A+B \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1 1
0 5
3 4
```

**Output**

```text
499122177
0
285212674
```

**Explanation**

**Test case $1$:** There is one chit with $1$ written on it and $1$ chit with $0$ written on it. Consider all possible cases as follows:
- Chef picks the chit with $1$ on his turn. Thus, Chefina picks the chit with $0$. The final score of Chef is $1$.
- Chef picks the chit with $0$ on his turn. Thus, Chefina picks the chit with $1$. The final score of Chef is $0$.

The expected score of Chef is $\frac {1}{2} \cdot 1 + \frac {1}{2} \cdot 0 = \frac {1}{2}$. This is equivalent to $1\cdot 2^{-1} = 499122177$.

**Test case $2$:** All chits have $0$ written on them. Thus, in any case, the final score would be $0$. Thus, the expected score of Chef is also $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
499122177
```



#### Test case 2

**Input for this case**

```text
0 5
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
3 4
```

**Output for this case**

```text
285212674
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/EXPECTEDSUM)

[Contest: Division 1](https://www.codechef.com/START71A/problems/EXPECTEDSUM)

[Contest: Division 2](https://www.codechef.com/START71B/problems/EXPECTEDSUM)

[Contest: Division 3](https://www.codechef.com/START71C/problems/EXPECTEDSUM)

[Contest: Division 4](https://www.codechef.com/START71D/problems/EXPECTEDSUM)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

2495

#
[](#prerequisites-3)PREREQUISITES:

[Linearity of expectation](https://brilliant.org/wiki/linearity-of-expectation/), [Modular multiplicative inverse](https://cp-algorithms.com/algebra/module-inverse.html), basic combinatorics

#
[](#problem-4)PROBLEM:

There are A ones and B zeros.

Alice and Bob alternate turns; with Alice moving first.

On their turn, a player chooses (uniformly at random) one of the remaining elements, adds it to their score, and then discards that value.

What is Alice’s expected final score?

#
[](#explanation-5)EXPLANATION:

If you’re familiar with linearity of expectation, this is a rather straightforward task.

Each 1 contributes independently to the answer, so let’s find the probability that Alice chooses a specific 1 and then multiply this by A: this will be the final answer.

Note that Alice will choose exactly k = \left \lceil \frac{N}{2} \right\rceil of the N = A+B elements available. Since each choice is fully random, each set of size k is equally likely to be chosen.

So, there are \binom{N}{k} choices of what the final set can be.

Of these, we’d like to count the number of sets that include a specific 1.

This is not hard: if a 1 is fixed, the other k-1 elements of Alice’s set must be chosen from the remaining N-1 elements, giving us \binom{N-1}{k-1} possible choices; again, each one is equally likely.

So, the required probability is \displaystyle \frac{\binom{N-1}{k-1}}{\binom{N}{k}}.

Expanding this in terms of factorials and cancelling out will reduce this to just \frac{k}{N}.

The final answer is thus simply A\cdot \frac{k}{N}, where k = \left \lceil \frac{N}{2} \right\rceil.

This can be computed in \mathcal{O}(\log{MOD}), since all that needs to be done is to invert N with respect to MOD.

If you don’t know how to compute inverses, a tutorial is linked in the prerequisites above.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(\log {MOD}) per testcase.

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
#define mod 998244353
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
void solve()
{
    ll A, B;
    A=readInt(0,1000000000,' ');
    B=readInt(0,1000000000,'\n');
    assert(A+B>=1 && A+B<=1000000000);
    ll totalSum=A;
    if(A%2 == B%2)
    {
        ll ans=totalSum*modInverse(2);
        ans%=mod;
        cout<<ans<<'\n';
        return;
    }
    if(A==0)
    {
        cout<<0<<'\n';
        return;
    }
    if(B==0)
    {
        cout<<(A+1)/2<<'\n';
        return;
    }
    ll l=1+(A-1)*modInverse(2);
    l%=mod;
    l*=A;
    l%=mod;
    l+=((B*A)%mod*modInverse(2));
    l%=mod;
    l*=modInverse(A+B);
    l%=mod;
    cout<<l<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
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

const int MOD = 998244353;

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

int solve(){
 		int a = readIntSp(0,1e9);
 		int b = readIntLn(0,1e9);
 		assert(a + b >= 1 and a + b <= 1e9);
 		int n = a + b;
 		int x = a*(n/2 + n % 2);
 		mod_int ans = x * mod_int(n).inv();
 		cout << ans << endl;
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
    int t = readIntLn(1,1000);
    while(t--){
        solve();
    }
    return 0;
}
``

Editorialist's code (Python)
``mod = 998244353
for _ in range(int(input())):
    a, b = map(int, input().split())
    ans = (a+b+1)//2 * pow(a+b, mod-2, mod)
    print((ans * a)%mod)
``

</details>
