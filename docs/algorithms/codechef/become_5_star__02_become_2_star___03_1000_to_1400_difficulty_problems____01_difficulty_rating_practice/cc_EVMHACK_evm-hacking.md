# EVM Hacking

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EVMHACK |
| Difficulty Rating | 1223 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [EVMHACK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/EVMHACK) |

---

## Problem Statement

There are three cities and thus three EVMs. An insider told Chef that his party got $A, B, C$ votes respectively in these three cities according to the EVMs. Also, the total number of votes cast are $P, Q, R$ respectively for the three cities.

Chef, being the party leader, can hack **at most** one EVM so that his party wins. On hacking a particular EVM all the votes cast in that EVM are counted in favor of Chef's party.

A party must secure **strictly more than half** of the total number of votes cast in order to be considered the winner. Can Chef achieve his objective of winning by hacking at most one EVM?

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing six space-separated integers — in order, $A, B, C, P, Q, R$.

---

## Output Format

For each test case, output in a single line the answer — `"YES"`, if Chef can win the election after hacking **at most** one EVM and `"NO"` if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 5 \cdot 10^3$
- $0 \leq A \lt P \leq 100$
- $0 \leq B \lt Q \leq 100$
- $0 \leq C \lt R \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 3 3 3
49 1 49 50 100 50
0 0 0 1 1 1
```

**Output**

```text
YES
YES
NO
```

**Explanation**

**Test case $1$:** Chef can hack any EVM, thus getting a total of $3 + 1 + 1 = 5$ votes which is more than $\frac{3 + 3 + 3}{2} = 4.5$ votes.

**Test case $2$:** Only hacking the second EVM works, getting a total of $49 + 100 + 49 = 198$ votes which is more than $\frac{50 + 100 + 50}{2} = 100$ votes.

**Test case $3$:** None of the EVM's can help Chef in winning the election, since maximum number of votes he can secure by doing so is $1 + 0 + 0 = 1$ which is less than $\frac{1 + 1 + 1}{2} = 1.5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 3 3 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
49 1 49 50 100 50
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
0 0 0 1 1 1
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[https://www.codechef.com/START24C/problems/EVMHACK](https://www.codechef.com/START24C/problems/EVMHACK)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec) + [Daanish](https://www.codechef.com/users/daanish_adm)

Tester: [Aryan Chaudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Rishabh Gupta](https://www.codechef.com/users/rishabhdevil)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are three cities and thus three EVMs. An insider told Chef that his party got A,B,C votes in these three cities according to the EVMs. Also, the total number of votes cast are P,Q,R respectively for the three cities.

Chef, being the party leader, can hack **at most** one EVM so that his party wins. On hacking a particular EVM all the votes cast in that EVM are counted in favor of Chef’s party.

A party must secure **strictly more than half** of the total number of votes cast in order to be considered the winner. Can Chef achieve his objective of winning by hacking at most one EVM?

#
[](#explanation-5)EXPLANATION:

Which EVM should he hack?

Chef would want to hack the EVM that would gain him the maximum new votes.

So his new vote count would increase to a+b+c+ max(p-a,q-b,r-c). Now we can answer yes or no depending on the new vote count.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

 Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define rb pop_back
#define ti tuple<int, int, int>
#define pii pair<int, int>
#define pli pair<ll, int>
#define pll pair<ll, ll>
#define mp make_pair
#define mt make_tuple
#define F first
#define S second
using namespace std;

const string newln = "\n", space = " ";
const int maxt = 5e3, maxv = 100;

int main()
{
    int t; cin >> t;
    int a, b, c, p, q, r;
    int cnt = 0;
    while(t--){
    	cin >> a >> b >> c;

        cin >> p >> q >> r;

    	bool ans = max({p + b + c, a + q + c, a + b + r}) > (p + q + r) / 2;
        cout << (ans ? "YEs" : "No") << endl;
        cnt += ans;
    }
}
``

 Editorialist''s Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define dd double
#define endl "\n"
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define fi first
#define se second
#define vll vector<ll>
#define pll pair<ll,ll>
#define fo(i,n) for(int i=0;i<n;i++)
#define fo1(i,n) for(int i=1;i<=n;i++)
ll mod=1000000007;
ll n,k,t,m,q,flag=0;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(a) -- no. of elements strictly less than a
// s.find_by_order(i) -- itertor to ith element (0 indexed)
ll min(ll a,ll b){if(a>b)return b;else return a;}
ll max(ll a,ll b){if(a>b)return a;else return b;}
ll gcd(ll a , ll b){ if(b > a) return gcd(b , a) ; if(b == 0) return a ; return gcd(b , a%b) ;}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifdef NOOBxCODER
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #else
    #define NOOBxCODER 0
    #endif
    cin>>t;
    //t=1;
    while(t--){
        ll a,b,c,p,q,r;
        cin>>a>>b>>c>>p>>q>>r;
        int s = a+b+c,tot= p+q+r;
        int val= max(p-a,q-b);val =max(val , r-c);
        if(s+val +s+val > p+q+r )cout<<"YES"<<endl;
        else cout<<"NO"<<endl;

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}

``

</details>
