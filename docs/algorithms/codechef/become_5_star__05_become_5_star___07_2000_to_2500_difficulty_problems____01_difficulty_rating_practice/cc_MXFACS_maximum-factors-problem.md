# Maximum Factors Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MXFACS |
| Difficulty Rating | 2006 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MXFACS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MXFACS) |

---

## Problem Statement

You are given an integer $N$. Let $K$ be a divisor of $N$ **of your choice** such that $K > 1$, and let $M = \frac{N}{K}$. You need to find the **smallest** $K$ such that $M$ has as many divisors as possible.

**Note**: $U$ is a divisor of $V$ if $V$ is divisible by $U$.

---

## Input Format

- The first line of the input contains an integer $T$ - the number of test cases. The test cases then follow.
- The only line of each test case contains an integer $N$.

---

## Output Format

For each test case, output in a single line minimum value of $K$ such that $M$ has as many divisors as possible.

---

## Constraints

- $1 \leq T \leq 3000$
- $2 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
3
4
6
```

**Output**

```text
3
2
2
```

**Explanation**

- **Test case $1$**: The only possible value for $K$ is $3$, and that is the answer.
- **Test case $2$**: There are two cases:
    - $K = 2$. Then $M = \frac{4}{2} = 2$, which has $2$ divisors ($1$ and $2$).
    - $K = 4$. Then $M = \frac{4}{4} = 1$, which has $1$ divisor ($1$).

Therefore the answer is $2$.
- **Test case $3$**: There are three cases:
    - $K = 2$. Then $M = \frac{6}{2} = 3$, which has $2$ divisors ($1$ and $3$).
    - $K = 3$. Then $M = \frac{6}{3} = 2$, which has $2$ divisors ($1$ and $2$).
    - $K = 6$. Then $M = \frac{6}{6} = 1$, which has $1$ divisor ($1$).

Therefore the answer is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Maximum Factors Problem:

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MXFACS)

[Code Drive Contest Division 1](https://www.codechef.com/CDRV21A/problems/MXFACS)

[Code Drive Contest Division 2](https://www.codechef.com/CDRV21B/problems/MXFACS)

[Code Drive Contest Division 3](https://www.codechef.com/CDRV21C/problems/MXFACS)

***Author:*** [Sobhagya Singh Dewal](https://www.codechef.com/users/manoj_vajpeyi)

***Tester:*** [Lavish Gupta](https://www.codechef.com/users/lavish315) , [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#prerequisites-3)PREREQUISITES:

Greedy, Math

#
[](#problem-4)PROBLEM:

You are given an integer N. Let K be a divisor of N **of your choice** such that K > 1, and let M = \frac{N}{K}. You need to find the smallest K such that M has as many divisors as possible.

**Note**: U is a divisor of V if V is divisible by U.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Find prime factorization of the number N, the smallest prime with maximum frequency will be the answer.

For example let’s say prime factorization of N is P_{1}^{X_{1}}*P_{2}^{X_{2}}......P_{i}^{X_{i}}

Minimum P with Maximum X value will be the answer.

#
[](#explanation-6)EXPLANATION:

We know that N can be written in the form

N=P_{1}^{X_{1}}*P_{2}^{X_{2}}......P_{i}^{X_{i}}

where P_{1},P_{2}....P_{i} are primes and

X_{1},X_{2}....X_{i} are their respective exponents.

Now, the number of factors of N will be

(X_{1}+1)*(X_{2}+1)*....(X_{i}+1).

We want to divide N by it’s one of the factor such that remaining number has maximum number of factors so it is always optimal to reduce maximum X_{i} by one, means we will divide N by one of it’s factor which have maximum exponent, so first we will find the maximum exponent and then will choose minimum prime with maximum exponent.

Time Complexity: O(\sqrt N) for each testcase.

#
[](#solutions-7)SOLUTIONS:

Setter’s Solution
``#include <bits/stdc++.h>
#define int long long int
using namespace std;

int f(int n)
{
  int cur = 0, ans = n;
  int cnt = 0;
  while (n % 2 == 0)
  {
    n /= 2;
    cnt++;
  }
  if (cnt > cur)
  {
    ans = 2;
    cur = cnt;
  }
  for (int i = 3; i * i <= n; i += 2)
  {
    cnt = 0;
    while (n % i == 0)
    {
      n /= i;
      cnt++;
    }
    if (cnt > cur)
    {
      ans = i;
      cur = cnt;
    }
  }
  if (n > 1)
  {
    if (1 > cur)
    {
      ans = n;
      cur = 1;
    }
  }
  return ans;
}
void myfun()
{
  int n;
  cin >> n;
  cout << f(n) << "\n";
}

signed main()
{
  int t = 1;
  cin >> t;
  for (int tt = 1; tt <= t; tt++)
  {
    myfun();
  }
  return 0;
}
``

Tester's (Lavish Gupta) Solution
``// O(N^1/2 * T)
#include <bits/stdc++.h>
using namespace std;
#define ll long long

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

const int MAX_T = 3000;
const int MAX_N = 1000000000;
const int MAX_SUM_N = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll z = 1000000007;
ll sum_nk = 0 ;

int get_facts(int n)
{
    ll cnt = 0 ;
    // cout << "n = " << n << endl ;
    for(ll i = 1 ; i*i <= n ; i++)
    {
        if(n%i == 0)
        {
            cnt++ ;
            if(n != i*i)
                cnt++ ;
        }
    }
    return cnt ;
}

void solve()
{
    int n = readIntLn(1 , MAX_N) ;
    ll a = n ;
    int ans = n , facts = 0 ;
    vector<pair<int , int> > v ;
    int max_cnt = 0 ;

    for(int i = 2 ; i*i <= n ; i++)
    {
        if(n%i == 0)
        {
            int cnt = 0 ;
            while(n%i == 0)
            {
                cnt++ ;
                n /= i ;
            }
            v.push_back({i , cnt}) ;
            max_cnt = max(max_cnt , cnt) ;
        }
    }
    if(n > 1)
    {
        max_cnt = max(max_cnt , 1) ;
        v.push_back({n , 1}) ;
    }

    for(int i = 0 ; i < v.size() ; i++)
        if(v[i].second == max_cnt)
            ans = min(ans , v[i].first) ;

    cout << ans << '\n' ;
    return ;
}

signed main()
{
    //fast;
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve() ;
    }

    assert(getchar() == -1);
    // assert(sum_n <= MAX_SUM_N);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    // cerr<<"Sum of lengths : " << sum_n << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr << "Sum of product : " << sum_nk << '\n' ;
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Tester's (Takuki Kurokawa) Solution
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    while (tt--) {
        int n;
        cin >> n;
        vector<pair<int, int>> f;
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                f.emplace_back(i, 0);
                while (n % i == 0) {
                    n /= i;
                    f.back().second++;
                }
            }
        }
        if (n) {
            f.emplace_back(n, 1);
        }
        sort(f.begin(), f.end(), [&](auto x, auto y) {
            if (x.second == y.second) {
                return x.first < y.first;
            }
            return x.second > y.second;
        });
        cout << f[0].first << '\n';
    }
    return 0;
}
``

</details>
