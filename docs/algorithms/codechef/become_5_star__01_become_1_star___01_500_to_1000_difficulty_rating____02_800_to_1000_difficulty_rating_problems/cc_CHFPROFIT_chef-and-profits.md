# Chef and Profits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFPROFIT |
| Difficulty Rating | 889 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CHFPROFIT](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CHFPROFIT) |

---

## Problem Statement

Some time ago, Chef bought $X$ stocks at the cost of Rs. $Y$ each. Today, Chef is going to sell **all** these $X$ stocks at Rs. $Z$ each. What is Chef's total profit after he sells them?

Chef's profit equals the total amount he received by selling the stocks, minus the total amount he spent buying them.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $X, Y$ and $Z$ — the number of stocks, the price they were bought at, and the price they can be sold at, respectively.

---

## Output Format

For each test case print on a new line a single integer — Chef's profit after selling all the stocks he has.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 10^4$
- $Y \leq Z \leq 10^4$

---

## Examples

**Example 1**

**Input**

```text
3
2 5 20
3 1 2
4 5 6
```

**Output**

```text
30
3
4
```

**Explanation**

**Test Case 1:** Chef bought $X = 2$ stocks for $Y = 5$ each, making the total amount **spent** by Chef $ = 2 \cdot 5 = 10$.

Chef can sell this stock today for $Z = 20$, making the total amount **received** by Chef $ =  2 \cdot 20 = 40$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $40 - 10 = 30$.

**Test Case 2:** Chef bought $X = 3$ stocks for $Y = 1$ each, making the total amount **spent** by Chef $ = 3 \cdot 1 = 3$.

Chef can sell this stock today for $Z = 2$, making the total amount **received** by Chef $ =  3 \cdot 2 = 6$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $6 - 3 = 3$.

**Test Case 3:** Chef bought $X = 4$ stocks for $Y = 5$ each, making the total amount **spent** by Chef $ = 4 \cdot 5 = 20$.

Chef can sell this stock today for $Z = 6$, making the total amount **received** by Chef $ =  4 \cdot 6 = 24$.

The total **profit** is then the amount **received** minus the amount **spent**, which equals $24 - 20 = 4$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 5 20
```

**Output for this case**

```text
30
```



#### Test case 2

**Input for this case**

```text
3 1 2
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 5 6
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

[Contest Division 1](https://www.codechef.com/START23A/problems/CHFPROFIT)

[Contest Division 2](https://www.codechef.com/START23B/problems/CHFPROFIT)

[Contest Division 3](https://www.codechef.com/START23C/problems/CHFPROFIT)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Some time ago, Chef bought X stocks at the cost of Rs. Y each. Today, Chef is going to sell **all** these X stocks at Rs. Z each. What is Chef’s total profit after he sells them?

Chef’s profit equals the total amount he received by selling the stocks, minus the total amount he spent buying them.

#
[](#explanation-5)EXPLANATION:

The Chef has bought X stocks at the cost of Rs. Y each, so the total amount of money spent is Rs X \cdot Y.  Now, the chef is going to sell **all** these X stocks at Rs. Z each, and therefore the total amount of money that chef will get will be Rs X \cdot Z

So, Chef’s profit = total amount that chef received - total amount that chef spent  = X\cdot Z - X \cdot Y = X \cdot (Z-Y).

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

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
    int x,y,z;
    cin>>x>>y>>z;
    cout<<(x*(z-y))<<'\n';
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
``#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int a, b, c;
    cin>>a>>b>>c;
    cout<<(c - b) * a<<"\n";
  }
  return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

const ll z = 1000000007 ;

void solve()
{
    int x , y , z ;
    cin >> x >> y >> z ;
    cout << max(0 , (z-y)*x) << endl ;
    return ;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t;
    cin >> t ;
    while(t--)
        solve() ;

    return 0;
}
``

</details>
