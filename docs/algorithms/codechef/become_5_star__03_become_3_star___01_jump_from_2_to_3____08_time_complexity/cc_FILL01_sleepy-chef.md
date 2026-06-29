# Sleepy Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FILL01 |
| Difficulty Rating | 1445 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [FILL01](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/FILL01) |

---

## Problem Statement

Chef has to work on a project for the next $N$ hours. He is given a work plan to do this, which is given to you as a binary string $S$ of length $N$. $S_i = 1$ if Chef has to work on the project during the $i$-th hour, and $S_i = 0$ if Chef is free during the $i$-th hour.

Chef would like to use some of his free time to take naps. He needs a minimum of $K$ consecutive hours of free time to take a nap. What is the maximum number of naps that Chef can take during the next $N$ hours?

Note that it is allowed for one nap to immediately follow another, i.e, Chef can wake up from one nap and then immediately take another one (if he has enough free time to do so), and these will be counted as different naps.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$ respectively.
- The second line of each test case contains a binary string $S$ of length $N$ denoting Chef's work plan.

---

## Output Format

- For each test case, print a single line containing one integer — the maximum number of naps that Chef can take.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N$
- Sum of $N$ over all test cases doesn't exceed $2 \cdot 10^5$
- $S$ is a binary string, i.e, each character of $S$ is either `0` or `1`.

---

## Examples

**Example 1**

**Input**

```text
3
4 1
1010
4 2
0100
11 3
00100000001
```

**Output**

```text
2
1
2
```

**Explanation**

**Test Case 1:** Chef can take two naps starting from the $2^{nd}$ and $4^{th}$ hours respectively.

**Test Case 2:** Chef can take a nap starting from the $3^{rd}$ hour.

**Test Case 3:** Chef can take one nap starting from the $5^{th}$ hour and another starting from the $8^{th}$ hour.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1
1010
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 2
0100
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
11 3
00100000001
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FILL01)

[Contest: Division 1](https://www.codechef.com/START19A/problems/FILL01)

[Contest: Division 2](https://www.codechef.com/START19B/problems/FILL01)

[Contest: Division 3](https://www.codechef.com/START19C/problems/FILL01)

***Authors:*** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360) and [Lavish Gupta](https://www.codechef.com/users/lavish315)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a work plan for the next N hours, and for each hour he knows if he must work or can take a break. He can take a nap if there are at least K consecutive hours of break time. What is the maximum number of naps he can take?

#
[](#explanation-5)EXPLANATION:

Suppose there are x hours of consecutive break time. Chef needs at least K hours to take a nap, so in x hours, he can take at most \lfloor \frac{x}{K} \rfloor naps, where \lfloor a \rfloor denotes the floor of a, i.e, the largest integer less than or equal to a.

So, the maximum number of naps Chef can take can be computed as follows:

- Let the (maximal) segments of break time in Chef’s schedule have lengths x_1, x_2, \ldots, x_m (a segment is said to be maximal if it is not contained in another segment of break time which has strictly larger length).

- The maximum number of naps is then \lfloor \frac{x_1}{K} \rfloor + \lfloor \frac{x_2}{K} \rfloor + \ldots + \lfloor \frac{x_m}{K} \rfloor

For example, if Chef’s schedule is `'0010110001110000'` and K = 2, the maximal segments of free time have lengths 2, 1, 3, 4 from left to right. The maximum number of naps is then \lfloor \frac{2}{2} \rfloor + \lfloor \frac{1}{2} \rfloor + \lfloor \frac{3}{2} \rfloor + \lfloor \frac{4}{2} \rfloor = 1 + 0 + 1 + 2 = 4.

In most languages, computing \lfloor \frac{x}{K} \rfloor can be done by **integer division**, that is, just `x / K`. Note that python users need to use `x // K` instead.

Finding the maximal segments of break time can be done in \mathcal{O}(|S|) by iterating over the string and keeping a variable denoting the length of the current segment, as in the following pseudocode:

``cur = 0
for i from 1 to N
    if S[i] = '0'
        cur += 1
    else
        // cur is now the length of a maximal segment, do whatever you want with it
        // ...

        // reset the length to 0
        cur = 0
end
// at the end of the loop, cur holds the length of the maximal segment of break time which is a suffix of S
``

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per test case.

#
[](#solutions-7)SOLUTIONS:

Tester's Solution (C++)
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

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll MX=200000;
ll fac[MX], ifac[MX];

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

    ll n,x;
    n = readIntSp(1,MAX_N);
    x = readIntLn(1,n);

    string s;
    s = readStringLn(1,MAX_N);

    int cur = 0, ans = 0;
    for(auto h:s){
    	assert(h=='0' || h=='1');
      if(h=='0') cur++;
      else cur = 0;

      if(cur == x){
        ans++;
        cur = 0;
      }
    }

    cout<<ans<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input() + '1'
    cur, ans = 0, 0
    for c in s:
        if c == '1':
            ans += cur//k
            cur = 0
        else:
            cur += 1
    print(ans)
``

</details>
