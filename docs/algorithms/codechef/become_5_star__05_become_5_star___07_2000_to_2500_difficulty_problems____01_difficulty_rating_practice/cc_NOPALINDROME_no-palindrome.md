# No Palindrome

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOPALINDROME |
| Difficulty Rating | 2054 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [NOPALINDROME](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/NOPALINDROME) |

---

## Problem Statement

Given positive integers $N$ and $K$, let $S$ denote the **smallest number** of $N$ digits (with no leading zeros) such that:
- No substring of $S$ having length **strictly greater** than $K$ is a [palindrome](https://en.wikipedia.org/wiki/Palindrome#Numbers).

Find the **sum of digits** of $S$.

Note:
- A substring of a number is obtained by deleting some (possibly zero) digits from the beginning of the number and some (possibly zero) digits from the end of the number. For example, some substrings of the number $3010$ are $3010, 301, 010, 01, 10$ and $0$.
- **Leading zeros** are **considered** in a substring. In the above example, $010$ and $01$ are **valid** substrings.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $K$ — as mentioned in the statement.

---

## Output Format

For each test case, output on a new line, the sum of digits of the smallest number of $N$ digits satisfying the given condition.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq K \lt N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
2 1
3 2
```

**Output**

```text
1
1
```

**Explanation**

**Test case $1$:** The smallest number of $2$ digits satisfying the condition is $10$. Here no substring of length greater than $1$ is a palindrome.

**Test case $2$:** The smallest number of $3$ digits satisfying the condition is $100$. The sum of its digits is $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 2
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NOPALINDROME)

[Contest: Division 1](https://www.codechef.com/START97A/problems/NOPALINDROME)

[Contest: Division 2](https://www.codechef.com/START97B/problems/NOPALINDROME)

[Contest: Division 3](https://www.codechef.com/START97C/problems/NOPALINDROME)

[Contest: Division 4](https://www.codechef.com/START97D/problems/NOPALINDROME)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [jay_1048576](https://www.codechef.com/users/jay_1048576)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

2054

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given N and K, find the sum of digits of S; where S denotes the smallest N-digit number such that it doesn’t contain a palindromic substring of length \gt K.

# [](#explanation-5)EXPLANATION:

Let’s try to greedily construct the smallest number we can that satisfies the palindrome property.

It’s best if the first digit is 1, since we can’t use 0.

After than, we can start using zeros - the next K digits can all be 0 without creating any palindromes of length \gt K.

However, the next character can’t be 0; and it also can’t be 1.

So, the best we can do is to place a 2.

Our number currently looks like

1\ \underbrace{000\ldots 000}_{K \text{ times}} \ 2

Now, once again we can start placing zeros.

However, this time we can only place \left \lfloor \frac{K-1}{2} \right\rfloor of them - otherwise we’d create a palindrome of the form 000\ldots 00200\ldots 000.

So, we now have the string

1\ \underbrace{000\ldots 000}_{K \text{ times}} \ 2 \ \underbrace{00\ldots 00}_{\left \lfloor \frac{K-1}{2} \right\rfloor \text{ times}}

After this, we can’t place any more zeros; so we must place a 1.

Then, the pattern repeats — so the final string will look like

1\ \underbrace{000\ldots 000}_{K \text{ times}} \ 2 \ \underbrace{00\ldots 00}_{\left \lfloor \frac{K-1}{2} \right\rfloor \text{ times}} \ 1\ \underbrace{000\ldots 000}_{K \text{ times}} \ 2 \ \underbrace{00\ldots 00}_{\left \lfloor \frac{K-1}{2} \right\rfloor \text{ times}} \ 100 \ldots

repeated upto length N.

Of course, what we’re really interested in is the sum of this string.

The zeros don’t contribute to it at all, so we just need to count the number of times 1 and 2 occur.

That’s not too hard.

The length of the pattern is L = 2 + K + \left \lfloor \frac{K-1}{2} \right\rfloor.

- The ones appear at positions 1, L+1, 2L+1, 3L+1, \ldots

So, if x ones are to appear in the string upto position N, we’d need (x-1)\cdot L + 1 \leq N.

Using this, you can find the largest valid x either with math or just binary search it.

- The twos appear at positions K+2, K+2+L, K+2+2L, \ldots

Similarly, for y twos to appear in the string, we’d need K+2+L\cdot (y-1) \leq N; so the largest valid y can be found quickly.

Once x and y are known from above, the answer is just x + 2y.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <cassert>
#define int long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;

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
    int n = readInt(2,1000000000,' ');
    int k = readInt(1,n-1,'\n');
    int q = k + 2 + (k-1)/2;
    int ans = 3*(n/q);
    if(n%q > k+1){
        ans += 3;
    } else if(n%q){
        ans += 1;
    }
    cout << ans;
}
int32_t main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,5000,'\n');
    while(T--){
        solve();
        cout<<'\n';
    }
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``/*...................................................................*
 *............___..................___.....____...______......___....*
 *.../|....../...\........./|...../...\...|.............|..../...\...*
 *../.|...../.....\......./.|....|.....|..|.............|.../........*
 *....|....|.......|...../..|....|.....|..|............/...|.........*
 *....|....|.......|..../...|.....\___/...|___......../....|..___....*
 *....|....|.......|.../....|...../...\.......\....../.....|./...\...*
 *....|....|.......|../_____|__..|.....|.......|..../......|/.....\..*
 *....|.....\...../.........|....|.....|.......|.../........\...../..*
 *..__|__....\___/..........|.....\___/...\___/.../..........\___/...*
 *...................................................................*
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define INF 1000000000000000000
#define MOD 1000000007

void solve(int tc)
{
    int n,k;
    cin >> n >> k;
    int l = (3*k+3)/2;
    int ans = 3*(n/l);
    n%=l;
    if(n>k+1)
        ans+=3;
    else if(n>0)
        ans++;
    cout << ans << '\n';
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int tc=1;
    cin >> tc;
    for(int ttc=1;ttc<=tc;ttc++)
        solve(ttc);
    return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    L = 2 + k + ((k-1)//2)

    # (x-1)L + 1 <= N
    # (x-1)L <= N-1
    # x <= (N-1)/L + 1
    x = (n-1)//L + 1

    # k+2+(y-1)L <= N
    # y <= (N-k-2)/L + 1
    y = 0
    if n >= k+2: y = (n-k-2)//L + 1

    print(x + 2*y)
``

</details>
