# Bitwise Equation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BITEQU |
| Difficulty Rating | 1679 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [BITEQU](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/BITEQU) |

---

## Problem Statement

Given an integer $N$, find four **positive** **distinct** integers $a$, $b$, $c$ and $d$ such that:
- $1 \leq a, b, c, d \leq 10^{18}$
- $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = N$

Here $\mathbin{\&}$, $\mathbin{|}$, and $\oplus$ represent [bitwise AND, OR and XOR](https://en.wikipedia.org/wiki/Bitwise_operation), respectively.

If there are multiple answers, print **any** of them. If no answer exists, print $-1$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of one line of input, containing a single integer $N$.

---

## Output Format

For each test case, output $-1$ if there is no way to find four distinct integers to satisfy the equation.

Otherwise, print on a new line **any** four space-separated integers $a$, $b$, $c$ and $d$ that satisfy the conditions.

---

## Constraints

- $1 \leq T \leq 10^4$
- $0 \leq N \lt 2^{32}$

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3221225472
```

**Output**

```text
1 4 3 2
2 4 3 1
920426639 955944413 754668683 4244364431
```

**Explanation**

**Test case $1$:** We have $a = 1$, $b = 4$, $c = 3$, $d = 2$ and $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = (0 \mathbin{|}3) \oplus 2 = 3 \oplus 2 = 1.$

**Test case $2$:** We have $a = 2$, $b = 4$, $c = 3$, $d = 1$ and $((a\mathbin{\&}b)\mathbin{|}c)\oplus d = (0 \mathbin{|}3) \oplus 1 = 3 \oplus 1 = 2.$

**Test case $3$:** Note that the value of $N$ might exceed the limit of signed a $32$-bit integer, use unsigned $32$-bit integers or $64$-bit integers instead.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1 4 3 2
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
2 4 3 1
```



#### Test case 3

**Input for this case**

```text
3221225472
```

**Output for this case**

```text
920426639 955944413 754668683 4244364431
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BITEQU)

[Contest: Division 1](https://www.codechef.com/START78A/problems/BITEQU)

[Contest: Division 2](https://www.codechef.com/START78B/problems/BITEQU)

[Contest: Division 3](https://www.codechef.com/START78C/problems/BITEQU)

[Contest: Division 4](https://www.codechef.com/START78D/problems/BITEQU)

***Author:*** [gudegude](https://www.codechef.com/users/gudegude)

***Testers:*** [tabr](https://www.codechef.com/users/tabr), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an integer N, find four distinct positive integers a, b, c, d such that (((a \ \& \ b)\mid c)\oplus d) = N.

#
[](#explanation-5)EXPLANATION:

There are several ways to solve this problem. Here are a few:

Author's solution (fix c)

Let’s fix c = 2^{32} - 1, i.e, the first 32 bits of c are set.

This will make (a\ \& \ b)\mid c) always equal 2^{32}-1, no matter what a and b are.

So, choose d = c\oplus N, and then arbitrary a and b that don’t equal c or d, and we’re done.

There are only a couple of edge cases here: when we get d = 0 or d = c.

- If d = 0, that means N = 2^{32}-1. Find any solution for this case by hand and print it separately.

- If d = c, that means N = 0. Again, find a solution to this case by hand.

There are other ways to do this too; for example, you can fix c = 1 and similarly solve all but a handful of cases.

Tester's solution (brute force lower bits)

Let’s solve the problem for N \lt 8 by brute force, while ensuring that a, b, c, d are all also \lt 8.

Simply brute-forcing all 8^4 possibilities here will tell you that this is possible.

To solve for N \geq 8,

- Set the first three bits of a, b, c, d to the solution for N\mod 8.

- Give all higher bits that are set in N to d.

Editorialist's solution (Random)

Choose a, b, c randomly between 1 and 10^{18}, and then choose d = N\oplus ((a\ \& \ b)\mid c).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    ll m = 4294967295;
    while (t--){
        ll n;
        cin >> n;
        if (n == 0) cout << 17 << " " << 1 << " " << 2 << " " << 3 << endl;
        else if (n == m) cout << 2 << " " << 4 << " " << m - 1 << " " << 1 << endl;
        else {
            ll d = bitset<32>(n).flip().to_ulong();
            if (d <= 2) cout << d + 1 << " " << d + 2 << " " << m << " " << d << endl;
            else cout << d - 2 << " " << d - 1 << " " << m << " "<< d << endl;
        }
    }
	return 0;
}
``

Tester's code (C++)
``//clear adj and visited vector declared globally after each test case
//check for long long overflow
//Mod wale question mein last mein if dalo ie. Ans<0 then ans+=mod;
//Incase of close mle change language to c++17 or c++14
//Check ans for n=1
// #pragma GCC target ("avx2")
// #pragma GCC optimize ("O3")
// #pragma GCC optimize ("unroll-loops")
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#define int long long
#define IOS std::ios::sync_with_stdio(false); cin.tie(NULL);cout.tie(NULL);cout.precision(dbl::max_digits10);
#define pb push_back
#define mod 1000000007ll //998244353ll
#define lld long double
#define mii map<int, int>
#define pii pair<int, int>
#define ll long long
#define ff first
#define ss second
#define all(x) (x).begin(), (x).end()
#define rep(i,x,y) for(int i=x; i<y; i++)
#define fill(a,b) memset(a, b, sizeof(a))
#define vi vector<int>
#define setbits(x) __builtin_popcountll(x)
#define print2d(dp,n,m) for(int i=0;i<=n;i++){for(int j=0;j<=m;j++)cout<<dp[i][j]<<" ";cout<<"\n";}
typedef std::numeric_limits< double > dbl;
using namespace __gnu_pbds;
using namespace std;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> indexed_set;
//member functions :
//1. order_of_key(k) : number of elements strictly lesser than k
//2. find_by_order(k) : k-th element in the set
const long long N=200005, INF=2000000000000000000;
const int inf=2e9 + 5;
lld pi=3.1415926535897932;
int lcm(int a, int b)
{
    int g=__gcd(a, b);
    return a/g*b;
}
int power(int a, int b, int p)
    {
        if(a==0)
        return 0;
        int res=1;
        a%=p;
        while(b>0)
        {
            if(b&1)
            res=(1ll*res*a)%p;
            b>>=1;
            a=(1ll*a*a)%p;
        }
        return res;
    }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

int getRand(int l, int r)
{
    uniform_int_distribution<int> uid(l, r);
    return uid(rng);
}

int32_t main()
{
    IOS;
    int t, mask=7;
    cin>>t;
    assert(t>=1 && t<=10000);
    vector <int> res[8];
    res[0] = {7, 4, 2, 6};
    res[1] = {7, 5, 3, 6};
    res[2] = {7, 6, 3, 5};
    res[3] = {7, 6, 5, 4};
    res[4] = {7, 6, 5, 3};
    res[5] = {7, 6, 5, 2};
    res[6] = {7, 6, 5, 1};
    res[7] = {7, 6, 4, 1};
    while(t--)
    {
        int n;
        cin>>n;
        assert(n>=0 && (n<(1ll << 32)));
        int cur_mask=(n&mask);
        cout<<res[cur_mask][0]<<" "<<res[cur_mask][1]<<" "<<res[cur_mask][2]<<" "<<(res[cur_mask][3]^n^cur_mask)<<"\n";
    }
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

	int t; cin >> t;
	const ll mx = 1e17;
	while (t--) {
		ll n; cin >> n;
		ll a, b, c, d;
		while (true) {
			a = uniform_int_distribution<ll>(1, mx)(rng);
			while (true) {
				b = uniform_int_distribution<ll>(1, mx)(rng);
				if (a == b) continue;
				else break;
			}
			while (true) {
				c = uniform_int_distribution<ll>(1, mx)(rng);
				if (a == c) continue;
				else if (b == c) continue;
				else break;
			}
			d = (a & b) | c;
			d ^= n;
			if (a == d or b == d or c == d or d == 0) continue;
			cout << a << ' ' << b << ' ' << c << ' ' << d << '\n';
			break;
		}
	}
}
``

</details>
