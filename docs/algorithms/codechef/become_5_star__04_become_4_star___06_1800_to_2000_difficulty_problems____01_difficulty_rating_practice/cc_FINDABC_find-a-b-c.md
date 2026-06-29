# Find A, B, C

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FINDABC |
| Difficulty Rating | 1843 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [FINDABC](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/FINDABC) |

---

## Problem Statement

Chef has $3$ hidden numbers $A, B,$ and $C$ such that $0 \leq A, B, C \leq N$.

Let $f$ be a function such that $f(i) = (A \oplus i) + (B \oplus i) + (C \oplus i)$. Here $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

Given the values of $f(0), f(1), \dots, f(N)$, determine the values of $A, B,$ and $C$.

It is guaranteed that **at least** one tuple exists for the given input. If there are multiple valid tuples of $A, B, C$, print any one.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ denoting the upper bound on the values of $A, B, C$.
    - Next line contains $N+1$ space-separated integers denoting $f(0), f(1), \dots, f(N)$.

---

## Output Format

For each test case, output on a new line, three space-separated integers, the values of $A, B,$ and $C$. If there are multiple valid tuples of $A, B, C$, print any one.

---

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
0 3 6
2
4 7 2
5
9 6 11 8 13 10
```

**Output**

```text
0 0 0
2 0 2
1 3 5
```

**Explanation**

**Test case $1$:** The tuple $A = 0, B=0, C=0$ satisfies as:
- $f(0)= 0\oplus 0 + 0\oplus 0 + 0\oplus 0 = 0$.
- $f(1)= 0\oplus 1 + 0\oplus 1 + 0\oplus 1 = 3$.
- $f(2)= 0\oplus 2 + 0\oplus 2 + 0\oplus 2 = 6$.

**Test case $2$:** The tuple $A = 2, B=0, C=2$ satisfies as:
- $f(0)= 2\oplus 0 + 0\oplus 0 + 2\oplus 0 = 4$.
- $f(1)= 2\oplus 1 + 0\oplus 1 + 2\oplus 1 = 7$.
- $f(2)= 2\oplus 2 + 0\oplus 2 + 2\oplus 2 = 2$.

**Test case $3$:** The tuple $A = 1, B=3, C=5$ satisfies as:
- $f(0)= 1\oplus 0 + 3\oplus 0 + 5\oplus 0 = 9$.
- $f(1)= 1\oplus 1 + 3\oplus 1 + 5\oplus 1 = 6$.
- $f(2)= 1\oplus 2 + 3\oplus 2 + 5\oplus 2 = 11$.
- $f(3)= 1\oplus 3 + 3\oplus 3 + 5\oplus 3 = 8$.
- $f(4)= 1\oplus 4 + 3\oplus 4 + 5\oplus 4 = 13$.
- $f(5)= 1\oplus 5 + 3\oplus 5 + 5\oplus 5 = 10$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
0 3 6
```

**Output for this case**

```text
0 0 0
```



#### Test case 2

**Input for this case**

```text
2
4 7 2
```

**Output for this case**

```text
2 0 2
```



#### Test case 3

**Input for this case**

```text
5
9 6 11 8 13 10
```

**Output for this case**

```text
1 3 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JULY221A/problems/FINDABC)

[Contest Division 2](https://www.codechef.com/JULY221B/problems/FINDABC)

[Contest Division 3](https://www.codechef.com/JULY221C/problems/FINDABC)

[Contest Division 4](https://www.codechef.com/JULY221D/problems/FINDABC)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Tester: [ Satyam](https://www.codechef.com/users/satyam_343), [Jatin Garg](https://www.codechef.com/users/rivalq)

Editorialist: [Devendra Singh](https://www.codechef.com/users/devendra7700)

#
[](#difficulty-2)DIFFICULTY:

1843

#
[](#prerequisites-3)PREREQUISITES:

Greedy algorithms, [Bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#:~:text=A%20bitwise%20XOR%20is%20a,0%20or%20both%20are%201.)

#
[](#problem-4)PROBLEM:

Chef has 3 hidden numbers A, B, and C such that 0 \leq A, B, C \leq N.

Let f be a function such that f(i) = (A \oplus i) + (B \oplus i) + (C \oplus i). Here \oplus denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

Given the values of f(0), f(1), \dots, f(N), determine the values of A, B, and C.

It is guaranteed that **at least** one tuple exists for the given input. If there are multiple valid tuples of A, B, C, print any one.

#
[](#explanation-5)EXPLANATION:

A, B, C \leq N\leq 10^5 \implies only first 18 bits can be set to 1 in A, B\: and\: C.

Also as only the sum f(i) = (A \oplus i) + (B \oplus i) + (C \oplus i) is taken into consideration for each bit from 0^{th}(least significant) bit to the 17^{th} bit only the number of set bits is important.

 only the number of set bits is important.

Let countset_j represent the count of numbers in which the j^{th} bit is set to 1.

f[i] = \sum_{j=0}^{17} 2^{j}*((i & 2^j)?(3-countset_j):countset_j). Thus only the number of set bits for each bit is important to calculate the answer.

Let set be the number of integers in which i^{th} bit is set to 1 and unset be the number of integers in which i^{th} bit is set to 0.

Then set+unset=3 and set-unset= \frac{f[0] - f[2^i]}{2^i}

The number of set bits for each bit i (2^i<=N) can be calculated as  \frac{(3+\frac{f[0] - f[2^i]} {2^i})}{2}.

Initialize A, B and C as 0. Now iterate over bits from most significant to least significant bit and maintain the order of elements (ascending or descending), calculate the number of set bits for each bit using the above formula, add them to the the numbers in ascending order. For example if number of set bits for a bit is 1 add it to the smallest number, if it is 2 add it to the two smaller values and so on.  This greedy approach produces one of the correct answers.

This greedy approach produces one of the correct answers.

Let i^{th} bit from right be the first bit which is not same in all A,B\: and\: C. If it is present in only one number, set it in A and then whenever we have a choice of setting the bits i.e. set bit count is 1 or 2 we set them in B and C as they can never exceed A. Since an answer always exists this produces a correct answer.

If it is present in two numbers set it in A and B and then whenever we have a choice of setting the bit in one number i.e. set bit count is 1, we set it in C as it can never exceed A. When we get a choice of setting a bit in two numbers for the first time we set it in A and C and later every time in B and C

Thus, this greedy approach always produces one of the correct answers.

For details of implementation please refer to the attached solutions.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

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
int sumN=0;
void solve()
{
    int n=readInt(2,100000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    int A=0,B=0,C=0;
    int f[n+1]={0};
    for(int i=0;i<=n;i++)
    {
        if(i!=n)
            f[i]=readInt(0,100000000,' ');
        else
            f[i]=readInt(0,100000000,'\n');
    }
    for(int i=0;i<20;i++)
    {
        if((1<<i)>n)
            break;
        ll x=f[0];
        ll y=f[(1<<i)];
        ll diff=y-x;
        diff/=(1<<i);
        if(diff==3)
        {

        }
        else if(diff==-3)
        {
            A|=(1<<i);
            B|=(1<<i);
            C|=(1<<i);
        }
        else if(diff==1)
        {
            A|=(1<<i);
        }
        else if(diff==-1)
        {
            A|=(1<<i);
            B|=(1<<i);
        }
        else
        {
            assert(false);
        }
    }
    if(A>n)
    {
        int rec=20;
        for(int i=20;i>=0;i--)
        {
            if((A&B&C&(1<<i))!=0)
                continue;
            if((A&(1<<i))==0)
                continue;
            A^=(1<<i);
            C^=(1<<i);
            rec=i;
            break;
        }
        if(B>n)
        {
            for(int i=rec-1;i>=0;i--)
            {
                if((A&B&C&(1<<i))!=0)
                    continue;
                if((B&(1<<i))==0)
                    continue;
                B^=(1<<i);
                if((A&(1<<i))==0)
                    A^=(1<<i);
                else
                {
                    C^=(1<<i);
                    if(C>n)
                    {
                        C^=(1<<i);
                        B^=(1<<i);
                        continue;
                    }
                }
                break;
            }
        }
    }
    cout<<A<<' '<<B<<' '<<C<<'\n';
    assert(max({A,B,C})<=n);
    for(int i=0;i<=n;i++)
        assert(f[i]==((A^i)+(B^i)+(C^i)));
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,20000,'\n');
    while(T--)
        solve();
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
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
    int n;
    vector<int> a(3, 0);
    cin >> n;
    int f[n + 1];
    for (int i = 0; i <= n; i++)
        cin >> f[i];
    for (int i = 18; i >= 0; i--)
    {
        if ((1 << i) > n)
            continue;
        sort(all(a));
        int diff = (f[1 << i] - f[0]) / (1 << i);
        if (diff == -3)
        {
            a[0] ^= (1 << i);
            a[1] ^= (1 << i);
            a[2] ^= (1 << i);
        }
        else if (diff == 1)
        {
            a[0] ^= (1 << i);
        }
        else if (diff == -1)
        {
            a[0] ^= (1 << i);
            a[1] ^= (1 << i);
        }
    }

    cout << a[0] << ' ' << a[1] << ' ' << a[2] << '\n';
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
