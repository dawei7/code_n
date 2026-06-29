# Make it Divisible

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAKEDIV3 |
| Difficulty Rating | 1379 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [MAKEDIV3](https://www.codechef.com/practice/course/2to3stars/LP2TO301/problems/MAKEDIV3) |

---

## Problem Statement

Given an integer $N$, help Chef in finding an $N$-digit $\textbf{odd positive integer}$ $X$ such that $X$ is divisible by $3$ but not by $9$.

$\textbf{Note}:$ There should not be any leading zeroes in $X$. In other words, $003$ is not a valid $3$-digit odd positive integer.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of the $T$ testcases follows.
- The first and only line of each test case contains a single integer $N$, denoting the number of digits in $X$.

---

## Output Format

For each testcase, output a single line containing an $N$-digit odd positive integer $X$ in decimal number system, such that $X$ is divisible by $3$ but not by $9$.

---

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N \leq 10^4$
- The sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
3
15
123
```

**Explanation**

**Test Case $1$:** $3$ is the only $1$-digit odd positive integer which is divisible by $3$ but not by $9$.

**Test Case $2$:** $15$ is a $2$-digit odd positive integer which is divisible by $3$ but not by $9$. $21$ is also a valid answer, among others. Note that $03$ is not a valid answer as there should not be any leading zeroes in the output.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
15
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
123
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAKEDIV3)

[Div1](https://www.codechef.com/START12A/problems/MAKEDIV3)

[Div2](https://www.codechef.com/START12B/problems/MAKEDIV3)

[Div3](https://www.codechef.com/START12C/problems/MAKEDIV3)

**Setter:**  [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:**  [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

##
[](#difficulty-2)DIFFICULTY:

CAKEWALK

##
[](#prerequisites-3)PREREQUISITES:

Divisibility rules

##
[](#problem-4)PROBLEM:

We need to print an N digit odd number which is divisible by 3 but not divisibility by 9.

##
[](#quick-explanation-5)QUICK EXPLANATION:

- If N=1 we ouput 3 else we output 30000\dots03 where the total zeros are N-2.

##
[](#explanation-6)EXPLANATION:

Recall that a number is divisible by 3 if the sum of the digits is divisible by 3 and a number is divisible by 9 if the sum of the digits is divisible by 9.

Now, to construct the number, there are many ways to go about it. One such way is as follows:

-

If N=1, we just output 3.

-

if N \gt 1, we can print a number where the first and last digits equal to 3 and the rest of the digits are equal to 0. The number constructed will be 3000\dots003 . Clearly this number is odd. Also the sum of the digits is 3+3=6 which is divisible by 3 but not divisible by 9. Hence, this number satisifies the required conditions.

##
[](#time-complexity-7)TIME COMPLEXITY:

O(N) for each testcase.

##
[](#solution-8)SOLUTION:

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
          for (int i = 1; i <= n; i++)
          {
               if (i == 1 || i == n)
                    cout << 3;
               else
                    cout << 0;
          }
          cout << endl;
     }
     return 0;
}
``

Setter's solution
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
    int n;
    cin>>n;
    string s="";
    int sum=0;
    for(int i=1;i<=n;i++)
    {
        sum+=3;
        s+='3';
    }
    if(sum%9==0)
        s[0]='9';
    cout<<s<<'\n';
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

Tester's solution
``#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int n;
    cin>>n;
    for(int i = 0; i < n; i++){
      if(i == 0 || i == n - 1){
        cout<<3;
      }else{
        cout<<0;
      }
    }
    cout<<"\n";
  }
  return 0;
}
``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
