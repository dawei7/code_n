# Three Numbers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | THREENUMBERS |
| Difficulty Rating | 1675 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [THREENUMBERS](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/THREENUMBERS) |

---

## Problem Statement

Chef has three numbers $A, B,$ and $C$.

He can do the following type of operation:
- Select two numbers amongst $A, B,$ and $C$;
- Add $1$ to the selected numbers;
- Subtract $1$ from the remaining number.

Determine whether Chef can make all the three numbers **equal** after applying the above operation any number of times.
If yes, output the **minimum** number of operations required by Chef.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line containing $3$ space-separated integers $A, B,$ and $C$.

---

## Output Format

For each test case, output $-1$ if the numbers cannot be made equal, else output the **minimum** number of operations required to make them equal.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B, C \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
1 1 2
3 7 3
4 4 4
1 2 3
```

**Output**

```text
-1
2
0
-1
```

**Explanation**

**Test case $1$:** It can be proven that we cannot make the numbers equal using any number of operations.

**Test case $2$:** We require a minimum of $2$ operations to make the numbers equal:
- Operation $1$: Select the numbers $A$ and $C$. Thus, $A$ and $C$ become $3+1 = 4$ and $3+1 = 4$ respectively. Also, $B$ becomes $7-1 = 6$.
- Operation $2$: Select the numbers $A$ and $C$. Thus, $A$ and $C$ become $4+1 = 5$ and $4+1 = 5$ respectively. Also, $C$ becomes $6-1 = 5$.

Thus, all $3$ numbers are equal after $2$ operations.

**Test case $3$:** Since all $3$ numbers are already equal, we require no operations.

**Test case $4$:** It can be proven that we cannot make the numbers equal using any number of operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 2
```

**Output for this case**

```text
-1
```



#### Test case 2

**Input for this case**

```text
3 7 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 4 4
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
1 2 3
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/THREENUMBERS)

[Contest: Division 1](https://www.codechef.com/START77A/problems/THREENUMBERS)

[Contest: Division 2](https://www.codechef.com/START77B/problems/THREENUMBERS)

[Contest: Division 3](https://www.codechef.com/START77C/problems/THREENUMBERS)

[Contest: Division 4](https://www.codechef.com/START77D/problems/THREENUMBERS)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

You have three numbers A, B, C. In one move, you can increase two of them by 1 and decrease the third by 1.

Find the minimum number of moves needed to make all three equal, or decide that it’s impossible.

#
[](#explanation-5)EXPLANATION:

First, notice that the given operation always flips the parity of *all* three numbers since each one changes by +1 or -1.

If they’re to be equal in the end, all three will have the same parity.

So, if all three don’t have the same parity initially, it’s immediately possible to say that making them equal is impossible.

Now let’s look at what we can do with our moves.

Notice that any move increases the sum (A+B+C) by exactly 1.

In particular, this means if we make them all equal to x in the end, the number of moves used will be exactly 3x - A - B - C (that is, the difference between the final sum and the initial sum).

Minimizing this is thus the same as minimizing x, so let’s attempt to do that.

Suppose A \leq B \leq C.

It’s not hard to see that if we make everything equal to x, then x \geq \frac{B+C}{2}

Why?

Let d be the *initial* value of B+C.

Look at the value of B+C as we perform operations.

Any move does one of two things:

- Increases B+C by 2; or

- Doesn’t change B+C.

Either way, the value of B+C cannot decrease as we perform operations.

In particular, if we end up with B = C = x, then x+x =2x \geq d, which proves our claim.

In fact, we can always achieve x = \frac{B+C}{2}

Here’s how:

- Let k = \frac{B+C}{2} be the target value.

- Recall that B and C have the same parity, so let C-B = 2y where y \geq 0.

- Perform y moves that decrease C and increase the other two.

- Now we have B = C = k, and A \leq k

- Next, alternate moves that decrease C with moves that decrease B. This way, after two moves A will increase by 2 while B and C will remain unchanged.

- The parity condition ensures that A will reach k after an even number of moves, and we’re done!

So, when A \leq B \leq C and the parity condition is satisfied, the answer is simply

3\cdot\frac{B+C}{2} - A - B - C

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Setter's code (C++)
``//Utkarsh.25dec
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <queue>
#include <ctime>
#include <cassert>
#include <complex>
#include <string>
#include <cstring>
#include <chrono>
#include <random>
#include <bitset>
#include <array>
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
    int A, B, C;
    A=readInt(1,1000000000,' ');
    B=readInt(1,1000000000,' ');
    C=readInt(1,1000000000,'\n');
    if((A%2 == B%2) && (B%2 == C%2))
    {
        int d=A+B+C-min({A,B,C});
        d/=2;
        cout<<(3*d-A-B-C)<<'\n';
    }
    else
        cout<<-1<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,10000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    if a%2 == b%2 and a%2 == c%2:
        print(b-a + (c-b)//2)
    else:
        print(-1)
``

</details>
