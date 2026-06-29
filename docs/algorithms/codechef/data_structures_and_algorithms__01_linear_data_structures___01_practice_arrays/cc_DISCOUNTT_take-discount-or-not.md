# Take discount or Not

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISCOUNTT |
| Difficulty Rating | 700 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [DISCOUNTT](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/DISCOUNTT) |

---

## Problem Statement

There are $n$ items in a shop. You know that the price of the $i$-th item is $A_i$. Chef wants to buy all the $n$ items.

There is also a discount coupon that costs $x$ rupees and reduces the cost of every item by $y$ rupees. If the price of an item was initially $\leq y$, it becomes free, i.e, costs $0$.

Determine whether Chef should buy the discount coupon or not. Chef will buy the discount coupon if and only if the total price he pays after buying the discount coupon is **strictly less** than the price he pays without buying the discount coupon.

---

### **Function Declaration**

**Function Name** :

$checkCoupon$ – This function determines whether a coupon can be applied based on given conditions and item prices, and returns the result as a string.

### **Parameters**

$n$: An integer representing the number of items.

$x$: An integer representing the minimum number of items required to apply the coupon.

$y$: An integer representing the minimum total price required to apply the coupon.

$prices$: A 1D array of integers where each element represents the price of an item.

### **Return Value**

Returns a string indicating whether the coupon is applicable or not based on the given constraints.

---

**The input and output formats given below are only if you want to test using custom inputs.**

### Constraint:
- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $1 \leq X, Y \leq 10^5$
- $1 \leq A_i \leq 10^5$

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of two lines of input.
    - The first line of the test case contains three space-separated integers — $n$, $x$, and $y$.
    - The second line contains $n$ space-separated integers — $A_1, A_2, \ldots, A_N$.

---

## Output Format

- For each test case, output `COUPON` if Chef should buy the discount coupon, and `NO COUPON` otherwise.

Each letter of the output may be printed in either lowercase or uppercase. For example, the strings `coupon`, `CouPoN`, and `COUPON` will all be treated as equivalent.

---

## Examples

**Example 1**

**Input**

```text
5
4 30 10
15 8 22 6
4 40 10
15 8 22 6
4 34 10
15 8 22 6
2 10 100
60 80
3 30 5
50 60 50
```

**Output**

```text
COUPON
NO COUPON
NO COUPON
COUPON
NO COUPON
```

**Explanation**

**Test case $1$:** The original cost of the items is $15 + 8 + 22 + 6 = 51$. Buying the coupon costs $30$, and after buying it the cost of buying all the items is $5 + 0 + 12 + 0 = 17$. The total cost of buying everything with the coupon is $30 + 17 = 47$, which is strictly less than $51$. So, Chef will buy the coupon.

**Test case $2$:** The original cost of the items is $15 + 8 + 22 + 6 = 51$. Buying the coupon costs $40$, and after buying it the cost of buying all the items is $5 + 0 + 12 + 0 = 17$. The total cost of buying everything with the coupon is $40 + 17 = 57$, which is more than $51$. So, Chef will not buy the coupon.

**Test case $3$:** The original cost of the items is $51$. Buying the coupon costs $34$, and the cost of buying all the items after using it is $17$, making the total cost $34 + 17 = 51$. Since this is not strictly less than the original cost, Chef won't buy the coupon.

**Test case $4$:** The original cost of the items is $140$, the coupon costs $10$, and the cost of buying everything after using the coupon is $0$. Since $10 + 0 \lt 140$, Chef will buy the coupon.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 30 10
15 8 22 6
```

**Output for this case**

```text
COUPON
```



#### Test case 2

**Input for this case**

```text
4 40 10
15 8 22 6
```

**Output for this case**

```text
NO COUPON
```



#### Test case 3

**Input for this case**

```text
4 34 10
15 8 22 6
```

**Output for this case**

```text
NO COUPON
```



#### Test case 4

**Input for this case**

```text
2 10 100
60 80
```

**Output for this case**

```text
COUPON
```



#### Test case 5

**Input for this case**

```text
3 30 5
50 60 50
```

**Output for this case**

```text
NO COUPON
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START40A/problems/DISCOUNTT)

[Contest Division 2](https://www.codechef.com/START40B/problems/DISCOUNTT)

[Contest Division 3](https://www.codechef.com/START40C/problems/DISCOUNTT)

[Contest Division 4](https://www.codechef.com/START40D/problems/DISCOUNTT)

Setter: [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [ Satyam](https://www.codechef.com/users/satyam_343), [ Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

To be calculated

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are N items in a shop. You know that price of i^{th} item is A_i. You want to buy all the N items.

There is also a discount coupon which costs X Rs and reduces Y Rs from every item (If price of any item is \leq Y, then it becomes free).

Determine whether he should buy the discount coupon or Not.

Chef will buy discount coupon if and only if Total price he pays after buying the discount coupon is **strictly less** than the price he pays without buying discount coupon.

#
[](#explanation-5)EXPLANATION:

Let sum1 represent the sum of all N items in the shop. Let sum2 represent the cost of all the items reduced by Y (If price of any item is \leq Y, it’s cost becomes 0).

\therefore sum2= \sum_{i=1}^{N}  max(0, cost\: of\: i^{th}\: item-Y)

A discount coupon costs X Rs. Chef should buy a discount coupon if sum2+X< sum1 otherwise he should not buy a coupon.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) or for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
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
void solve()
{
    int n=readInt(1,100,' ');
    int X=readInt(1,100000,' ');
    int Y=readInt(1,100000,'\n');
    int A[n+1]={0};
    int withoutdisc=0,withdisc=X;
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(1,100000,'\n');
        else
            A[i]=readInt(1,100000,' ');
        withoutdisc+=A[i];
        withdisc+=(max(A[i]-Y,0));
    }
    if(withdisc<withoutdisc)
        cout<<"COUPON\n";
    else
        cout<<"NO COUPON\n";
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
}
``

Editorialist's Solution
``#include "bits/stdc++.h"
using namespace std;
#define ll long long
#define pb push_back
#define all(_obj) _obj.begin(), _obj.end()
#define F first
#define S second
#define pll pair<ll, ll>
#define vll vector<ll>
ll INF = 1e18;
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n, sum1 = 0, sum2 = 0, x, y;
    cin >> n >> x >> y;
    vll v(n);
    for (int i = 0; i < n; i++)
    {
        cin >> v[i], sum1 += v[i];
        sum2 += max(0, v[i] - y);
    }
    if (sum1 > sum2 + x)
        cout << "COUPON\n";
    else
        cout << "NO COUPON\n";
    return;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL), cout.tie(NULL);
    int test = 1;
    cin >> test;
    while (test--)
        sol();
}

``

</details>
