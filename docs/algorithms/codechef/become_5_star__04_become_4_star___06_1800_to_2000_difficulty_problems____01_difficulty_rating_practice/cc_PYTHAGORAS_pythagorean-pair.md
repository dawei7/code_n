# Pythagorean Pair

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PYTHAGORAS |
| Difficulty Rating | 1862 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [PYTHAGORAS](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/PYTHAGORAS) |

---

## Problem Statement

Chef has an integer $N$. It is known that the **largest** [odd](https://simple.wikipedia.org/wiki/Odd_number) [divisor](https://simple.wikipedia.org/wiki/Divisor) of $N$ does not exceed $10^5$.

Determine two **non-negative** integers $A$ and $B$ such that $A^2 + B^2 = N$, or report that no such pair exists.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$.

---

## Output Format

For each test case, output space-separated $A$ and $B$ such that $A^2 + B^2 = N$ or $-1$ if no such pair exists.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^{15}$
- Largest odd divisor of $N$ won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
100
6
13
4
```

**Output**

```text
8 6
-1
2 3
0 2
```

**Explanation**

**Test case $1$:** A possible pair $(A, B)$ such that $A^2 + B^2 = N$ is $(8, 6)$. Here, $8^2 + 6^2 = 64+36 = 100$.

**Test case $2$:** There is no pair $(A, B)$ such that $A^2 + B^2 = N$.

**Test case $3$:** A possible pair $(A, B)$ such that $A^2 + B^2 = N$ is $(2, 3)$. Here, $2^2 + 3^2 = 4+9 = 13$

**Test case $4$:** A possible pair $(A, B)$ such that $A^2 + B^2 = N$ is $(0, 2)$. Here, $0^2 + 2^2 = 0+4 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100
```

**Output for this case**

```text
8 6
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
13
```

**Output for this case**

```text
2 3
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
0 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PYTHAGORAS)

[Contest: Division 1](https://www.codechef.com/START62A/problems/PYTHAGORAS)

[Contest: Division 2](https://www.codechef.com/START62B/problems/PYTHAGORAS)

[Contest: Division 3](https://www.codechef.com/START62C/problems/PYTHAGORAS)

[Contest: Division 4](https://www.codechef.com/START62D/problems/PYTHAGORAS)

***Author:*** [Aryan](https://www.codechef.com/users/aryanc403)

***Preparer:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Takuki Kurokawa](https://www.codechef.com/users/tabr)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1862

#
[](#prerequisites-3)PREREQUISITES:

Algebraic manipulation

#
[](#problem-4)PROBLEM:

Given an integer N whose largest odd factor is at most 10^5, find two integers A and B such that A^2 + B^2 = N or claim that none exist.

#
[](#explanation-5)EXPLANATION:

There are several different constructions that can work in this task, so if you have an interesting one feel free to share it in the comments below.

The constraint on the largest odd factor is a bit weird, so let’s try to use that. Note that it immediately implies that any large N must be even.

So, if we were able to obtain a solution for N from a solution for N/2, we could potentially use that to build a solution.

It turns out that the relationship is a bit stronger: when N is even, there exists an integer pair (A_1, B_1) such that A_1^2 + B_1^2 = N *if and only if* there exists an integer pair (A_2, B_2) such that A_2^2 + B_2^2 = N/2.

Proof

Suppose A^2 + B^2 = N/2. Then, (A+B)^2 + (A-B)^2 = 2A^2 + 2B^2 = N gives us a solution for N.

Conversely, if A^2 + B^2 = N, turning the above construction around gives us

\left ( \frac{A+B}{2} \right )^2 + \left ( \frac{A-B}{2} \right )^2 = \frac{A^2}{2} + \frac{B^2}{2} = \frac{N}{2}

The interesting thing here is that (A+B)/2 and (A-B)/2 are both integers: if N is even, the only way A^2 + B^2 = N can have integer solutions is if both A and B have the same parity.

This tells us that it is enough to solve the problem for small N: we can reduce N to its largest odd factor, solve for this factor, then reconstruct the result for the original N using the method above.

Solving for N \leq 10^5 can be done with bruteforce: fix a value of A, then check if N - A^2 is itself a square integer.

We only need to check those A such that A^2 \leq N, giving us a \sqrt{10^5} solution, which is good enough.

There are also other constructions, though most use the same idea. One simple one is as follows:

Suppose we have a solution to A^2 + B^2 = N. Then, simply multiplying A and B by 2 gives us a solution to 4N.

So, we can simply divide N by 4 as long as possible, which will end with it being \leq 2\cdot 10^5. Use the bruteforce to solve for this, then reconstruct the answer for the original N by multiplying by 2 as many times as needed.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\sqrt{10^5} + \log N) per test case.

Spending 10^5 \cdot \sqrt{10^5} time on precomputation can bring this down to \mathcal{O}(\log N) per test case, but is unnecessary.

#
[](#code-7)CODE:

Preparer's code (C++)
``//Utkarsh.25dec
#include <bits/stdc++.h>
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
int avail[N];
pair<ll,ll> good[N];
int issq[N];
int sqrtval[N];
void solve()
{
    ll n=readInt(1,(ll)100000000*10000000,'\n');
    ll tmp=n;
    while(tmp%2==0)
        tmp/=2;
    assert(tmp<=100000);
    if(avail[tmp]==0)
        cout<<-1<<'\n';
    else
    {
        ll a=good[tmp].first;
        ll b=good[tmp].second;
        while(tmp!=n)
        {
            ll c=a+b;
            ll d=abs(a-b);
            a=c;
            b=d;
            tmp*=2;
        }
        cout<<a<<' '<<b<<'\n';
    }
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,100000,'\n');
    for(int i=0;i<400;i++)
    {
        issq[i*i]=1;
        sqrtval[i*i]=i;
    }
    for(int n=1;n<=100000;n++)
    {
        for(int a=0;a<=1000;a++)
        {
            if(a*a>n)
                break;
            if(issq[n-a*a]==1)
            {
                ll b=sqrtval[n-a*a];
                good[n]=mp(a,b);
                avail[n]=1;
                break;
            }
        }
    }
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;

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
        // cerr << res << endl;
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
    int tt = in.readInt(1, 1e5);
    in.readEoln();
    while (tt--) {
        long long n = in.readLong(1, 1e15);
        in.readEoln();
        long long m = 1;
        while (n % 2 == 0) {
            n /= 2;
            m *= 2;
        }
        assert(n <= 1e5);
        if (__builtin_ctzll(m) % 2 == 1) {
            m /= 2;
            n *= 2;
        }
        m = llround(sqrtl(m));
        int a = -1;
        for (int i = 0; i * i <= n; i++) {
            int j = (int) llround(sqrtl(n - i * i));
            if (i * i + j * j == n) {
                a = i;
                break;
            }
        }
        if (a == -1) {
            cout << -1 << '\n';
        } else {
            cout << a * m << " " << llround(sqrtl(n - a * a)) * m << '\n';
        }
    }
    in.readEof();
    return 0;
}
``

Editorialist's code (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	const int mx = 2e5 + 10;

	int t; cin >> t;
	while (t--) {
		ll n; cin >> n;
		ll mul = 1;
		while (n > mx) {
			n /= 4;
			mul *= 2;
		}
		bool done = false;
		for (int i = 0; i*i <= n; ++i) {
			int rem = n - i*i;
			int s = sqrtl(rem);
			while (s*s > rem) --s;
			while ((s+1)*(s+1) <= rem) ++s;
			if (s*s == rem) {
				cout << mul*i << ' ' << mul*s << '\n';
				done = true;
				break;
			}
		}
		if (!done) cout << -1 << '\n';
	}
}
``

</details>
