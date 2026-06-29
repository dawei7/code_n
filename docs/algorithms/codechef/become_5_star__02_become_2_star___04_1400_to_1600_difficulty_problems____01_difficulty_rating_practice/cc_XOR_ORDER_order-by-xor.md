# Order by XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XOR_ORDER |
| Difficulty Rating | 1476 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [XOR_ORDER](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/XOR_ORDER) |

---

## Problem Statement

You are given three **distinct** integers $A, B,$ and $C$.

Find **any** integer $X \ (0 \leq X < 2^{30})$ such that:
$(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$, where $\oplus$ denotes the [Bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

If no such $X$ exists, print $-1$ instead.

---

## Input Format

- The first line of the input contains a single integer $T$, the number of test cases.
- The first and only line of each test case contains three space-separated integers $A, B,$ and $C$.

---

## Output Format

For each test case, output a single integer on a new line, the value of $X$ that satisfies the above conditions or $-1$ if no such $X$ exists.

If multiple such $X$ satisfy the condition, you may print any.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B, C \lt 2^{30}$
- $A, B, C$ are **distinct**.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 3
3 1 2
3 2 1
```

**Output**

```text
4
-1
3
```

**Explanation**

**Test case $1$:** For $X = 4$,
- $A \oplus X = 1 \oplus 4 \ = 5$
- $B \oplus X = 2 \oplus 4 \ = 6$
- $C \oplus X = 3 \oplus 4 \ = 7$

Thus, $(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$.

**Test case $2$:** No $X \ (0 \leq X \lt 2^{30})$ exists that satisfies the above conditions.

**Test case $3$:** For $X = 3$,
- $A \oplus X = 3 \oplus 3 \ = 0$
- $B \oplus X = 2 \oplus 3 \ = 1$
- $C \oplus X = 1 \oplus 3 \ = 2$

Thus, $(A \oplus X) \lt (B \oplus X) \lt (C \oplus X)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 1 2
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
3 2 1
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/XOR_ORDER)

[Contest: Division 1](https://www.codechef.com/START83A/problems/XOR_ORDER)

[Contest: Division 2](https://www.codechef.com/START83B/problems/XOR_ORDER)

[Contest: Division 3](https://www.codechef.com/START83C/problems/XOR_ORDER)

[Contest: Division 4](https://www.codechef.com/START83D/problems/XOR_ORDER)

***Author:*** [youknow_who](https://www.codechef.com/users/youknow_who)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Bitwise operations

#
[](#problem-4)PROBLEM:

Given distinct integers A, B, C, find any 0 \leq X \lt 2^{30} such that

A\oplus X \lt B\oplus X \lt C\oplus X

or claim that none exist.

#
[](#explanation-5)EXPLANATION:

Let’s just look at A and B first.

Looking at their binary representations, let k be the *highest* bit where they differ.

For example, if A = 28 = 11100_2 and B = 26 = 11010_2, we’d have k =2, because the first time the binary representations differ is at 2^2 = 4.

Let a_k be the value of this bit in A, and b_k be the value of this bit in B.

The direction of inequality between A and B is completely defined by what a_k and b_k are; in particular, we want a_k = 0 and b_k = 1 to hold.

So,

- if a_k = 0 and b_k = 1, then the k-th bit of X *must* be 0

- if a_k = 1 and b_k = 0, then the k-th bit of X *must* be 1

This fixes one of the bits of X.

Do the same for the pairs (B, C) and (A, C) as well, giving us three conditions on the bits of X.

If any of these conditions conflict (for example, if (A, B) says that the 10-th bit must be 0 while (B, C) says that it must be 1), no answer is possible; so print -1.

Otherwise, fix these three bits of X, and the others can be left as zeros since there are no constraints on them; so this gives us a valid value of X.

The fact that at most three bits really matter also gives us a rather funny randomized solution: generate a random X between 0 and 2^{30} - 1 and check if it satisfies the condition; and if it doesn’t, continue generating X till you find a valid one.

If no valid X is found after several attempts (say, 100 attempts), the answer is -1.

Do you see why this works with high probability?

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``#include "bits/stdc++.h"
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

#define all(x)      x.begin(), x.end()
#define pb          push_back
#define sz(x)       (int)(x.size())
#define ll          long long
#define fi          first
#define se          second
#define lbd         lower_bound
#define ubd         upper_bound

template <typename T>
using ordered_set = tree<T, null_type,
      less<T>, rb_tree_tag,
      tree_order_statistics_node_update>;

const int MOD = 1e9 + 7;
const double eps = 1e-10;
const long long INF = 1e18;
const int N = 2e5 + 10;

void solve() {
	int a, b, c;
	cin >> a >> b >> c;

	int ans = 0, ok = 0;
	for (int i = 29; i >= 0; --i) {
		int x = (1 << i) ^ a;
		int y = (1 << i) ^ b;
		int z = (1 << i) ^ c;
		if (x < y && y < z) {
			a = x;
			b = y;
			c = z;
			ans ^= (1 << i);
			break;
		} else if (x < min(y, z) || max(x, y) < z) {
			a = x;
			b = y;
			c = z;
			ans ^= (1 << i);
		}
	}
	if (a < b && b < c) cout << ans;
	else cout << -1;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);

	int tt = 1;
	cin >> tt;
	while (tt--) {
		solve();
		cout << '\n';
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
// #define int long long
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
    int t;
    cin>>t;
    while(t--)
    {
        int a, b, c;
        cin>>a>>b>>c;
        if(a==b || c==a || b==c)
        {
            cout<<-1<<"\n";
            continue;
        }
        int f=-1;
        rep(i,0,500)
        {
            int x=getRand(0, (1 << 30) - 1);
            if((b^x)>(a^x) && (c^x)>(b^x))
            {
                f=x;
                break;
            }
        }
        cout<<f<<"\n";
    }
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x = 0
    for bit in reversed(range(30)):
        abit, bbit, cbit = (a >> bit) & 1, (b >> bit) & 1, (c >> bit) & 1

        flip = 0
        if a > b and abit > bbit: flip = 1
        if b > c and bbit > cbit: flip = 1
        if a > c and abit > cbit: flip = 1

        if flip == 1:
            a ^= 1 << bit
            b ^= 1 << bit
            c ^= 1 << bit
            x ^= 1 << bit

    print(x if a < b < c else -1)
``

</details>
