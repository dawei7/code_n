# Pass or Fail

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PASSORFAIL |
| Difficulty Rating | 730 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [PASSORFAIL](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/PASSORFAIL) |

---

## Problem Statement

Chef is struggling to pass a certain college course.

The test has a total of $N$ questions, each question carries $3$ marks for a correct answer and $-1$ for an incorrect answer. Chef is a risk-averse person so he decided to attempt all the questions. It is known that Chef got $X$ questions correct and the rest of them incorrect. For Chef to pass the course he must score at least $P$ marks.

Will Chef be able to pass the exam or not?

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers $N, X, P$.

---

## Output Format

For each test case output `"PASS"` if Chef passes the exam and `"FAIL"` if Chef fails the exam.

You may print each character of the string in uppercase or lowercase (for example, the strings "pASs", "pass", "Pass" and "PASS" will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $0 \leq X \leq N$
- $0 \leq P \leq 3\cdot N$

---

## Examples

**Example 1**

**Input**

```text
3
5 2 3
5 2 4
4 0 0
```

**Output**

```text
PASS
FAIL
FAIL
```

**Explanation**

**Test case $1$:** Chef gets $2$ questions correct giving him $6$ marks and since he got $3$ questions incorrect so he faces a penalty of $-3$. So Chef's final score is $3$ and the passing marks are also $3$, so he passes the exam :)

**Test case $2$:** Chef's total marks are $3$ and since the passing marks are $4$, Chef fails the test :(

**Test case $3$:** Chef got all the problems wrong and thus his total score is $-4$. Since the passing marks are $0$, Chef fails the exam :(

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 3
```

**Output for this case**

```text
PASS
```



#### Test case 2

**Input for this case**

```text
5 2 4
```

**Output for this case**

```text
FAIL
```



#### Test case 3

**Input for this case**

```text
4 0 0
```

**Output for this case**

```text
FAIL
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PASSORFAIL)

[Div1](https://www.codechef.com/START16A/problems/PASSORFAIL)

[Div2](https://www.codechef.com/START16B/problems/PASSORFAIL)

[Div3](https://www.codechef.com/START16C/problems/PASSORFAIL)

**Setter:**  [Utkasrsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:**  [ Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

##
[](#difficulty-2)DIFFICULTY:

CAKEWALK

##
[](#prerequisites-3)PREREQUISITES:

None

##
[](#problem-4)PROBLEM:

Chef writes and exam consisting of N questions. Chef gets 3 marks for every correct answer and -1 marks for every incorrect answer.The passing marks is P for this course. Chef has answered X questions correct and the remaining questions incorrect. We need to find whether chef will pass the exam or not.

##
[](#explanation-5)EXPLANATION:

-

Number of questions answered correctly is X. Therefore, number of questions answered incorrectly is N-X.

-

The number of marks the chef will get will then be 3\cdot X - (N-X).

-

Since the passing marks is P, chef needs atleast P marks to pass.

-

Therefore, if 3\cdot X - (N-X) \geq P we ouput PASS, else we output FAIL.

##
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each testcase.

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
          int n, x, p;
          cin >> n >> x >> p;

          if (3 * x - (n - x) >= p)
               cout << "PASS" << endl;
          else
               cout << "FAIL" << endl;
     }
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
    ll n,x,p;
    cin>>n>>x>>p;
    assert(n>=1 && n<=100);
    assert(x>=0 && x<=n);
    assert(p>=0 && p<=3*n);
    ll marks=3*x-(n-x);
    if(marks>=p)
        cout<<"PASS\n";
    else
        cout<<"FAIL\n";
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
    assert(T>=1 && T<=1000);
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
    int n,x,p;
    cin>>n>>x>>p;
    if(p <= 4 * x - n){
      cout<<"PASS\n";
    }else{
      cout<<"FAIL\n";
    }
  }
  return 0;
}

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
