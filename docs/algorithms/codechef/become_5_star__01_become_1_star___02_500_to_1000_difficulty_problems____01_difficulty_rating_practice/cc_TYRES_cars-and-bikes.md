# Cars and Bikes

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TYRES |
| Difficulty Rating | 809 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [TYRES](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/TYRES) |

---

## Problem Statement

### Read problems statements in [Russian](https://www.codechef.com/download/translated/COOK133/russian/TYRES.pdf) and [Bengali](https://www.codechef.com/download/translated/COOK133/bengali/TYRES.pdf).

Chef opened a company which manufactures cars and bikes. Each car requires $4$ tyres while each bike requires $2$ tyres. Chef has a total of $N$ tyres ($N$ is even). He wants to manufacture maximum number of cars from these tyres and then manufacture bikes from the remaining tyres.

Chef's friend went to Chef to purchase a bike. If Chef's company has manufactured even a single bike then Chef's friend will be able to purchase it.

Determine whether he will be able to purchase the bike or not.

---

## Input Format

- The first line contains an integer $T$ denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains an integer $N$ denoting the number of tyres.

---

## Output Format

For each test case, output `YES` or `NO` depending on whether Chef's friend will be able to purchase the bike or not. Output is case insensitive.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 1000$
- $N$ is even

---

## Examples

**Example 1**

**Input**

```text
3
8
2
6
```

**Output**

```text
NO
YES
YES
```

**Explanation**

- For the first test case Chef, will manufacture $2$ cars and will thus use all the $8$ tyres and thus could not manufacture any bike.

- For the second test case, Chef cannot manufacture any car since there are not enough tyres and will thus manufacture only a single bike which will be purchased by Chef's friend.

- For the third test case, Chef will manufacture $1$ car and thus use $4$ tyres. From the remaining $2$ tyres, Chef can manufacture a single bike which will be purchased by Chef's friend.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
6
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

[Contest](https://www.codechef.com/COOK133C/problems/TYRES)

[Practice](https://www.codechef.com/problems/TYRES)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Tester:** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

**Editorialist:** [Keyur Jain](https://www.codechef.com/users/keyurjain0)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Modulo Operation

#
[](#problem-4)PROBLEM

Chef opened a company which manufactures cars and bikes. Each car requires 4 tyres while each bike requires 2 tyres. Chef has a total of N tyres (N is even). He wants to manufacture maximum number of cars from these tyres and then manufacture bikes from the remaining tyres.

Chef’s friend went to Chef to purchase a bike. If Chef’s company has manufactured even a single bike then Chef’s friend will be able to purchase it.

Determine whether he will be able to purchase the bike or not.

#
[](#explanation-5)EXPLANATION

Chef will be building the maximum possible cars. When he is finally unable to build a car, he will try to build bikes.

This can be translated to code in the following way :

``cars = 0, bikes = 0
while tyres >= 4:
    cars++
    tyres -= 4
while tyres >= 2:
    bikes++
    tyres -= 2

if bikes > 0:
    print('YES')
else:
    print('NO')
``

It is to be observed that we can build atmost 1 bike. If we could build >1 bike, then we could’ve discarded two bikes and built a car with the 4 tyres instead.

We can update the code to :

``cars = 0, bikes = 0
while tyres >= 4:
    cars++
    tyres -= 4

if tyres >= 2:
    print('YES')
else:
    print('NO')
``

Can we still make it more efficient? Yes!

The above snippet is just another way of finding the remainder when tyres is divided by 4. An operator that can find the remainder in O(1) is the MODULO (\%) operator.

Read more about the modulo operation [here](https://en.wikipedia.org/wiki/Modulo_operation).

Our final solution becomes

``if tyres % 4 >= 2:
    print('YES')
else
    print('NO')
``

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(1)

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#include <chrono>
#include <random>
#define ll long long int
#define ull unsigned long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
#define loop(i,a,b) for(ll i=a;i<=b;i++)
#define vi vector <int>
#define vs vector <string>
#define vc vector <char>
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
#define max3(a,b,c) max(max(a,b),c)
#define min3(a,b,c) min(min(a,b),c)
#define deb(x) cerr<<#x<<' '<<'='<<' '<<x<<'\n'
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(val)  no. of elements strictly less than val
// s.find_by_order(i)  itertor to ith element (0 indexed)
typedef vector<vector<ll>> matrix;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
void solve()
{
    ll n;
    cin>>n;
    if(n%4==2)
    {
        cout<<"YES\n";
    }
    else
        cout<<"NO\n";
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    cin>>T;
    int t=0;
    while(t++<T)
    {
        //cout<<"Case #"<<t<<":"<<' ';
        solve();
        //cout<<'\n';
    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std ;

#define ll              long long
#define pb              push_back
#define all(v)          v.begin(),v.end()
#define sz(a)           (ll)a.size()
#define F               first
#define S               second
#define INF             2000000000000000000
#define popcount(x)     __builtin_popcountll(x)
#define pll             pair<ll,ll>
#define pii             pair<int,int>
#define ld              long double

const int M = 1000000007;
const int MM = 998244353;

template<typename T, typename U> static inline void amin(T &x, U y){ if(y<x) x=y; }
template<typename T, typename U> static inline void amax(T &x, U y){ if(x<y) x=y; }

#ifdef LOCAL
#define debug(...) debug_out(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) 2351
#endif

int _runtimeTerror_()
{
    int N;
    cin >> N;
    cout << (N % 4 ? "Yes" : "No") << "\n";
    return 0;
}

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifdef runSieve
        sieve();
    #endif
    #ifdef NCR
        initialize();
    #endif
    int TESTS = 1;
    cin >> TESTS;
    while(TESTS--)
        _runtimeTerror_();
    return 0;
}
``

Editorialist's Solution
``public class CarsAndBikes {
    public void solve(int testNumber, InputReader in, OutputWriter out) {
        int n = in.readInt();
        out.printLine((n % 4 >= 2) ? "YES" : "NO");
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
