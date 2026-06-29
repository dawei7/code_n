# Average Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGARR |
| Difficulty Rating | 1424 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [AVGARR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/AVGARR) |

---

## Problem Statement

You are given two integers $N$ and $X$. Output an array $A$ of length $N$ such that:
- $-1000 \le A_i \le 1000$ for all $1 \le i \le N$.
- All $A_i$ are **distinct**.
- $\texttt{mean}(A) = X$.

If there are multiple answers, print any. It is guaranteed that under the given constraints at least one array satisfying the given conditions exists.

As a reminder, the mean of an array $B$ of size $M$ is defined as: $\texttt{mean}(B) = \dfrac{\sum_{i = 1}^{M} B_i}{M}$.

For example, $\texttt{mean}([3, 1, 4, 8]) = \frac{3 + 1 + 4 + 8}{4} = \frac{16}{4} = 4$.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N$ and $X$ - the size of the array $A$ and the mean of the array $A$.

---

## Output Format

For each test case, output an array $A$ of length $N$ which satisfies the given conditions.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \le N \le 1000$
- $0 \le X \le 100$

---

## Examples

**Example 1**

**Input**

```text
3
3 7
5 1
1 10
```

**Output**

```text
5 10 6
1 2 3 4 -5
10
```

**Explanation**

**Test case 1:** $\texttt{mean}([5, 10, 6]) = \frac{5 + 10 + 6}{3} = \frac{21}{3} = 7$.

**Test case 2:** $\texttt{mean}([1, 2, 3, 4, -5]) = \frac{1 + 2 + 3 + 4 + (-5)}{5} = \frac{5}{5} = 1$.

**Test case 3:** $\texttt{mean}([10]) = \frac{10}{1} = 10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 7
```

**Output for this case**

```text
5 10 6
```



#### Test case 2

**Input for this case**

```text
5 1
```

**Output for this case**

```text
1 2 3 4 -5
```



#### Test case 3

**Input for this case**

```text
1 10
```

**Output for this case**

```text
10
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START34A/problems/AVGARR)

[Contest Division 2](https://www.codechef.com/START34B/problems/AVGARR)

[Contest Division 3](https://www.codechef.com/START34C/problems/AVGARR)

[Contest Division 4](https://www.codechef.com/START34D/problems/AVGARR)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

The mean of an array B of size M is defined as: \texttt{mean}(B) = \dfrac{\sum_{i = 1}^{M} B_i}{M}.

#
[](#problem-4)PROBLEM:

You are given two integers N and X. Output an array A of length N such that:

-
-1000 \le A_i \le 1000 for all 1 \le i \le N.

- All A_i are **distinct**.

-
\texttt{mean}(A) = X.

If there are multiple answers, print any. It is guaranteed that under the given constraints at least one array satisfying the given conditions exists.

As a reminder, the mean of an array B of size M is defined as: \texttt{mean}(B) = \dfrac{\sum_{i = 1}^{M} B_i}{M}.

For example, \texttt{mean}([3, 1, 4, 8]) = \frac{3 + 1 + 4 + 8}{4} = \frac{16}{4} = 4.

#
[](#explanation-5)EXPLANATION:

The problem can be divided into two cases:

\textbf{Case 1}: N is even. To achieve an average of X , the sum of all the values of array A must be N\cdot X. We simply create N/2 pairs such that their sum is 2\cdot X each. Total sum of these pairs would be 2\cdot X\cdot N/2 = N\cdot X

Therefore the average of these N values is (N\cdot X)/N = X . One possible way to create these pairs is to pair values around X i.e X-1\: and\: X+1 ,X-2\: and\: X+2 and so on.

To print the answer for this case run a loop from i=1 to i=N/2 and on each iteration print two values X-i and X+i.

\textbf{Case 1}: N is odd. To achieve an average of X , the sum of all the values of array A must be N\cdot X. We simply create (N-1)/2 pairs such that their sum is 2\cdot X each and append X to the end of the array. Total sum of these pairs would be 2\cdot X\cdot (N-1)/2 +X= N\cdot X - X +X= N\cdot X

Therefore the average of these N values is (N\cdot X)/N = X . One possible way to create these pairs is to pair values around X i.e X-1\: and\: X+1 ,X-2\: and\: X+2 and so on.

To print the answer for this case run a loop from i=1 to i=(N-1)/2 and on each iteration print two values X-i and X+i. Then print X in the end.

The value of A_i never exceeds 600 and never drops below -500 in this approach which satisfies the given constraints.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const long long INF = 1e18;

const int N = 1e6 + 5;

void solve()
{
    int n, x; cin >> n >> x;
    vector<int> a;
    for(int i = 1; i <= n / 2; i++)
        a.push_back(x - i), a.push_back(x + i);
    if(n % 2)
        a.push_back(x);
    for(int x: a)
        cout << x << " ";
    cout << endl;
}

int32_t main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        // cout << "Case #" << tc << ": ";
        solve();
    }
    return 0;
}
``

Tester-1's Solution(Python)
``for _ in range(int(input())):
	n, x = map(int, input().split())
	for i in range(n//2):
		print(x-i-1, x+i+1, end = ' ')
	if n%2 == 1:
		print(x)
	else:
		print('')
``

Tester-2's Solution
``#include <bits/stdc++.h>
using namespace std;
#ifndef ONLINE_JUDGE
#define debug(x) cerr<<#x<<" "; _print(x); cerr<<nline;
#else
#define debug(x);
#endif

/*
------------------------Input Checker----------------------------------
*/

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

/*
------------------------Main code starts here----------------------------------
*/
int MAX=100000;
void solve(){
    int n=readIntSp(1,1000);
    int x=readIntLn(0,100);
    if(n&1){
        cout<<x<<" "; n--;
    }
    int l=-5,r=2*x+5;
    for(int i=1;i<=n;i+=2){
        cout<<l--<<" "<<r++<<" ";
    }
    cout<<"\n";
    return;
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
    #endif
    int test_cases=readIntLn(1,100);
    while(test_cases--){
        solve();
    }
    assert(getchar()==-1);
    return 0;
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
const int N = 1e5 + 11, mod = 1e9 + 7;
ll max(ll a, ll b) { return ((a > b) ? a : b); }
ll min(ll a, ll b) { return ((a > b) ? b : a); }
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
void sol(void)
{
    int n, x;
    cin >> n >> x;
    if (n & 1)
    {
        cout << x << ' ';
        for (int i = 1; i <= (n / 2); i++)
            cout << x - i << ' ' << x + i << ' ';
        cout << '\n';
    }
    else
    {
        for (int i = 1; i <= (n / 2); i++)
            cout << x - i << ' ' << x + i << ' ';
        cout << '\n';
    }

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
