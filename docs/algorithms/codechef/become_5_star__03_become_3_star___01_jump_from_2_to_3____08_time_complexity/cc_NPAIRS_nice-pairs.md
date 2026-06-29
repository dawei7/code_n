# Nice Pairs 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NPAIRS |
| Difficulty Rating | 1564 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [NPAIRS](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/NPAIRS) |

---

## Problem Statement

Given a string $S$ of length $N$ containing only numeric characters, find the number of **Nice Pairs**.

A **Nice Pair** is a pair of indices - $(i, j)$ such that $1 \leq i \lt j \leq N$ and $j - i = |S_j - S_i|$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each testcase contains a single integer, $N$, the length of the string
- The second line of each testcase contains a string $S$ of length $N$. The string contains only numeric characters $[0-9]$

---

## Output Format

For each testcase, output a single integer - the number of nice pairs in the given string.

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- String $S$ contains only numeric characters
- The sum of $N$ over all test cases does not exceed $2\cdot10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3
123
5
13492
8
94241234
```

**Output**

```text
3
2
9
```

**Explanation**

**Test Case $1$:** There are $3$ nice pairs in the given string - $(1,2) , (1,3) , (2,3)$

**Test Case $2$:** There are $2$ nice pairs in the given string - $(2,3) , (3,5)$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
123
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
13492
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
8
94241234
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NPAIRS)

[Div1](https://www.codechef.com/START15A/problems/NPAIRS)

[Div2](https://www.codechef.com/START15B/problems/NPAIRS)

[Div3](https://www.codechef.com/START15C/problems/NPAIRS)

**Setter:**  [ Mradul Bhatnagar](https://www.codechef.com/users/mradul_adm)

**Tester:**  [ Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

##
[](#difficulty-2)DIFFICULTY:

SIMPLE

##
[](#prerequisites-3)PREREQUISITES:

None

##
[](#problem-4)PROBLEM:

We are given a string of length N consisting of only numeric characters. We need to find the number of pairs i, j where 1 \leq i \lt j \leq N and j-i = \mid S_j - S_i \mid.

##
[](#explanation-5)EXPLANATION:

-

The main observation in this problem is to find the maximum possible value of \mid S_j - S_i \mid. The maximum possible value is 9 when S_i =0, S_j=9 or S_i = 9, S_j=0.

-

So, it is enough that we check for pairs i, j where i \lt j and j-i \leq 9.

-

We can theerefore iterate over i from 1 to N, and iterate over j from i+1 to \min (i+9, N) and check the condition j-i = \mid S_j - S_i \mid holds true or not. If it is true, we increment our answer.

-

We will also fit our solution in the time limit because the number of pairs we are considering is O(9 \cdot N) which takes linear amount of time to run.

##
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each testcase.

##
[](#solution-7)SOLUTION:

Editorialist's solution
``#include <bits/stdc++.h>
using namespace std;

int main()
{
     int tests;
     cin >> tests;
     while (tests--)
     {
          int n;
          cin >> n;
          string s;
          cin >> s;

          int ans = 0;

          for (int i = 0; i < n; i++)
          {
               for (int j = i + 1; j <= min(i + 9, n - 1); j++)
               {
                    if (abs(s[j] - s[i]) == j - i)
                         ans++;
               }
          }

          cout << ans << endl;
     }
     return 0;
}

``

Setter's solution
``
#include <bits/stdc++.h>
//#include <ext/pb_ds/assoc_container.hpp>
//#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
//#pragma GCC optimize("Ofast,no-stack-protector,unroll-loops,fast-math,O3")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
//using namespace __gnu_pbds;
#define fastio() ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define pb  push_back
#define show(x) cout<<(#x)<<" : "<<x<<endl;
#define ll  long long
#define ld  long double
#define fill(a,val) memset(a,val,sizeof(a))
#define mp  make_pair
#define ff  first
#define ss  second
#define pii pair<ll,ll>
#define sq(x) ((x)*(x))
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define endl "\n"
#define int long long
#define printclock cerr<<"Time : "<<1000*(ld)clock()/(ld)CLOCKS_PER_SEC<<"ms\n";
const ll MOD     = 1000*1000*1000+7;
const ll INF     = 1ll*1000*1000*1000*1000*1000*1000 + 7;
const ll MOD2    = 998244353;
const ll N       = 1000*100 + 10;
const ll N2      = 70;
const ld PI  = 3.141592653589793;
//template<class T> using oset=tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
ll gcd(ll a, ll b){if(!b)return a;return gcd(b, a % b);}
ll power(ll x,ll y,ll p ){ll res=1;x%=p;while(y>0){if(y&1)res=(res*x)%p;y=y>>1;x=(x*x)%p;}return res;}
ll lcm(ll a , ll b){return (a*b)/gcd(a,b);}

signed main()
{
    fastio();
    //cout<<fixed<<setprecision(20);
    //CHECK for LONG LONG and LONG DOUBLE
    //*comment for all except cc/cf
    #ifndef ONLINE_JUDGE
           freopen("input.txt","r",stdin);
           freopen("output.txt","w",stdout);
    #endif//*/
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        int ans = 0;
        for (int j = 0; j < n; ++j)
        {
        	for(int k = 1 ; k < 10 ; k++)
        	{
        		int i = j-k;
        		if(i < 0) break;

        		if(k == (abs(s[i]-s[j])) )
        		{
        			ans++;
        		}

        	}
        }

        cout<<ans<<endl;

    }
    printclock;
    return 0;
}

``

Tester's solution
``#include <bits/stdc++.h>
using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

int main() {
	// your code goes here
	int t = readIntLn(1, 1000);
	int sum = 0;
	while(t--){
	    int n;
	    cin >> n;
	    sum += n;
	    assert(sum <= 2e5);
	    string s;
	    cin >> s;
	    for(auto j : s)
	        assert('0' <= j && j <= '9');
	    int ans = 0;
	    for(int i = 0; i < n ; i++)
	        for(int j = i + 1 ; j < min(i + 10, n) ; j++)
	            if(j - i == abs(s[j] - s[i]))
	                ans++;
	    cout << ans << '\n';
	}
    //readEOF();
	return 0;
}

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
