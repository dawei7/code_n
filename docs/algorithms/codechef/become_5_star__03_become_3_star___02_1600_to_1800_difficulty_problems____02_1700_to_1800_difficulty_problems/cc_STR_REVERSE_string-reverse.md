# String Reverse

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STR_REVERSE |
| Difficulty Rating | 1792 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [STR_REVERSE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/STR_REVERSE) |

---

## Problem Statement

Chef has a string $S$ consisting only of English lowercase letters (`a` - `z`). However, Hitesh does not like it and wants it to be reversed.

Hitesh wonders what is the minimum number of operations required to reverse the string $S$ using the following operation:
- Select any $i$ such that $1 \le i \le \lvert S \rvert$ and remove $S_i$ from its original position and append it to the end of the string (i.e. shift any character to the end of the string).

For e.g. if $S =$ `abcde` and we apply operation on $i = 2$, then $S$ becomes `acdeb`.

Help Hitesh find the minimum number of operations required to reverse $S$.

It is guaranteed that it is possible to reverse the string in a finite number of operations.

---

## Input Format

-   The first line of input contains a single integer  $T$, denoting the number of test cases. The description of  $T$  test cases follows.
-   Each test case consists of a single line containing the string S.

---

## Output Format

For each test case, output the minimum number of operations required to reverse the string $S$.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1  \leq \lvert S \rvert \leq 10^5$
- Sum of $\lvert S \rvert$ over all testcases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
abdeba
codechef
```

**Output**

```text
3
7
```

**Explanation**

- **Test case-1:** Following steps can be performed:
1.  $abdeba \to  abebad$
2.  $abebad \to abeadb$
3.  $abeadb \to  abedba$
- **Test case-2:** following steps can be performed:
1.  $codechef \to  codechfe$
2.  $codechfe \to codecfeh$
3.  $codecfeh \to codefehc$
4.  $codefehc \to  codfehce$
5.  $codfehce \to cofehced$
6.  $cofehced \to cfehcedo$
7.  $cfehcedo \to fehcedoc$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
abdeba
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
codechef
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START27A/problems/STR_REVERSE)

[Contest Division 2](https://www.codechef.com/START27B/problems/STR_REVERSE)

[Contest Division 3](https://www.codechef.com/START27C/problems/STR_REVERSE)

[Contest Division 4](https://www.codechef.com/START27D/problems/STR_REVERSE)

Setter: [Hitesh Jindal](https://www.codechef.com/users/hjindal)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a string S consisting only of English lowercase letters (`a` - `z`). However, Hitesh does not like it and wants it to be reversed.

Hitesh wonders what is the minimum number of operations required to reverse the string S using the following operation:

- Select any i such that 1 \le i \le \lvert S \rvert and remove S_i from its original position and append it to the end of the string (i.e. shift any character to the end of the string).

For e.g. if S = `abcde` and we apply operation on i = 2, then S becomes `acdeb`.

Help Hitesh find the minimum number of operations required to reverse S.

It is guaranteed that it is possible to reverse the string in a finite number of operations.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- In the optimal scenario, we will never remove the same character twice. In this sentence, we are treating each index element as a distinct character. So, in aba, the first and the third a are distinct for this sentence.

- Let S' denote the set of indices (in the original string) that we have removed and appended at the end, and let S denote the set of indices that we have not operated on. How will the string look after all the operations.

- Make the cardinality of S as large as possible.

#
[](#explanation-6)EXPLANATION:

The first observation is in the optimal scenario, we should never remove the same character twice. To see this, consider a sequence of operations O_1 in which the same character c is removed twice. Consider another sequence of operations O_2, where the first operation in which the character c was removes, is removed from O_1, and rest everything remains same. We can see that both O_1 and O_2 will lead to same string, with |O_2| < |O_1|.

Let S = \{i_1, i_2, ... , i_k\} be the set of indices which have not been operated on. Let us call the new string as new\_str. We have:

str = s_1s_2...s_n

rev\_str = s_ns_{n-1}...s_2s_1

new\_str = s_{i_1}s_{i_2}...s_{i_k} s_{i_1'}...,

Because rev\_str = new\_str, we have s_n = s_{i_1}, s_{n-1} = s_{i_2}, and so on. So to minimize the size of set S', we should maximize the size of set S, which is equal to k. In other words, we need to find out the longest prefix of rev\_str that appears as a subsequence in str.

We can find this prefix greedily, using the algorithm described [here](https://www.geeksforgeeks.org/maximum-length-prefix-one-string-occurs-subsequence-another/) in O(N) time.

#
[](#time-complexity-7)TIME COMPLEXITY:

O(N) per test case.

#
[](#solution-8)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll mod = 998244353;

ll po(ll x, ll n ){
    ll ans=1;
     while(n>0){
        if(n&1) ans=(ans*x)%mod;
        x=(x*x)%mod;
        n/=2;
     }
     return ans;
}

void solve()
{

    string s = readStringLn(1, 1e5);

    for(auto h:s) assert(h>='a' && h<='z');

    string t = s;
    reverse(t.begin(), t.end());

    int l=0;

    int n = s.length();
    sum_len += n;
    max_n = max(max_n, n);

    rep(i,n){
        if(s[i]==t[l]) l++;
    }

    cout<<n-l<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_len<=2e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}

``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll mod = 998244353;

ll po(ll x, ll n ){
    ll ans=1;
     while(n>0){
        if(n&1) ans=(ans*x)%mod;
        x=(x*x)%mod;
        n/=2;
     }
     return ans;
}

void solve()
{

    string s = readStringLn(1, 1e5);

    for(auto h:s) assert(h>='a' && h<='z');

    string t = s;
    reverse(t.begin(), t.end());

    int l=0;

    int n = s.length();
    sum_len += n;
    max_n = max(max_n, n);

    rep(i,n){
        if(s[i]==t[l]) l++;
    }

    cout<<n-l<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_len<=2e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}

``

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;
const ll z = 998244353 ;

void solve()
{
    string str , orig;
    cin >> orig ;
    str = orig ;

    reverse(str.begin() , str.end()) ;

    int cnt = 0, n = str.size() ;
    for(int i = 0 ; i < n ; i++)
    {
        if(orig[i] == str[cnt])
            cnt++ ;
    }
    cout << n-cnt << endl ;
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

    ll t;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    return 0;
}
``

</details>
