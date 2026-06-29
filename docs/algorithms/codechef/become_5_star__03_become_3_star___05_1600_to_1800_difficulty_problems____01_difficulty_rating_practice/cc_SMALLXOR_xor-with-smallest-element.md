# XOR with smallest element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SMALLXOR |
| Difficulty Rating | 1635 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [SMALLXOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/SMALLXOR) |

---

## Problem Statement

Chef has an array $A$ of length $N$ and an integer $X$.

In one operation, Chef does the following:
- Find the smallest element in the current array. Let this be $S$.
- Next, pick any **one** index $i$ such that $A_i = S$
- Finally, replace $A_i$ with $A_i \oplus X$

Here $\oplus$ denotes the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) operation.

For example, if $A = [1, 1, 2]$ and $X = 4$, then in one move Chef can turn the array into either $[5, 1, 2]$ or $[1, 5, 2]$.

Chef performs this operation **exactly** $Y$ times. Let $B$ be final array obtained.

Output the array $B$ in sorted order. Note that under this restriction, the output is unique.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains three space-separated integers $N$, $X$, and $Y$.
    - The second line contains $N$ space-separated integers denoting the array $A$.

---

## Output Format

For each test case, output array $B$ in sorted order.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq Y \leq 10^9$
- $1 \leq A_i , X \leq 2^{30}$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1 6 99
9
3 7 44
1 2 3
5 20 6
5 10 15 20 25
```

**Output**

```text
15 
3 5 6 
5 20 25 27 30
```

**Explanation**

**Test case $1$:** The array is initially $[9]$. Since there is only one element, it will be modified in each step. So,
- After the first operation, the array is $[15]$ (since $9 \oplus 6 = 15$)
- After the second operation, the array is $[9]$ (since $15 \oplus 6 = 9$)
- Continuing the above, it can be verified that after $99$ steps, the array is $[15]$.

**Test case $3$:** The sequence of steps is as follows:
- Initially, the array is $[5, 10, 15, 20, 25]$
- After operation $1$, it is $[17, 10, 15, 20, 25]$
- After operation $2$, it is $[17, 30, 15, 20, 25]$
- After operation $3$, it is $[17, 30, 27, 20, 25]$
- After operation $4$, it is $[5, 30, 27, 20, 25]$
- After operation $5$, it is $[17, 30, 27, 20, 25]$
- After operation $6$, it is $[5, 30, 27, 20, 25]$

Remember to print the output in sorted order.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 6 99
9
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
3 7 44
1 2 3
```

**Output for this case**

```text
3 5 6
```



#### Test case 3

**Input for this case**

```text
5 20 6
5 10 15 20 25
```

**Output for this case**

```text
5 20 25 27 30
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SMALLXOR)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/SMALLXOR)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/SMALLXOR)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/SMALLXOR)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/SMALLXOR)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1635

#
[](#prerequisites-3)PREREQUISITES:

Multisets

#
[](#problem-4)PROBLEM:

Given an array A and integer X, Chef does the following exactly Y times:

- Pick one instance of the smallest element in A, and replace it with its bitwise xor with X

Print the final array, in sorted order.

#
[](#explanation-5)EXPLANATION:

Suppose we simply simulated the process. How would we be able to do this fast?

Answer

Keep all the elements of A in a multiset or equivalent data structure (`std::multiset` in C++). The smallest element can be found in \mathcal{O}(1), and removing it and inserting a new element can both be done in \mathcal{O}(\log N).

This allows us to solve the problem in \mathcal{O}(Y \log N). However, Y is large so this is too slow.

Let’s analyze the operation instead. Suppose, at the current step, the minimum element is m.

- If (m \oplus X) \gt m, we can’t say anything about the minimum in the next step — it might be some other element.

- If (m \oplus X) \lt m, then the minimum in the next step is definitely going to be (m \oplus X), because it’s smaller than m which is already not larger than any other element of the array.

However, note that (m \oplus X) \oplus X = m, so the only change from this point onwards is to keep replacing m with m\oplus X and vice versa.

This gives us an idea to optimize the solution. Suppose we simulate the process upto the point when our minimum m satisfies the condition (m \oplus X) \lt m. Once we reach this point, we can stop the simulation, since the other elements of A are never going to change again. Whether the final array contains m or m\oplus X can be determined by the parity of the number of moves remaining, since the values simply alternate between each other.

Is this fast enough? Turns out it is!

Proof

Within the first N+1 moves, we are guaranteed to find an element whose xor with X is less than itself.

This follows from the fact that if (m \oplus X) \gt m, then m \oplus X gets added to the array, and ((m\oplus X) \oplus X) = m \lt (m \oplus X).

Thus, if any index is picked as the minimum twice, it is guaranteed to satisfy the condition at one of those choices.

Now, by the pigeonhole principle, after N+1 moves, some index has been picked as the minimum twice or more. So, our simulation will stop after at most N+1 moves, hence making the time complexity \mathcal{O}(N\log N).

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N\log N) per test case.

#
[](#code-7)CODE:

Setter's Code (C++)
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
    int n=readInt(1,100000,' ');
    sumN+=n;
    assert(sumN<=100000);
    int x=readInt(1,(1<<30),' ');
    int y=readInt(1,1000000000,'\n');
    int A[n+1]={0};
    multiset <ll> s;
    for(int i=1;i<=n;i++)
    {
        if(i==n)
            A[i]=readInt(1,(1<<30),'\n');
        else
            A[i]=readInt(1,(1<<30),' ');
        s.insert(A[i]);
    }
    int oper=0;
    while(true)
    {
        auto it=s.begin();
        ll ele=(*it);
        ll now=(ele^x);
        s.erase(it);
        s.insert(now);
        oper++;
        if(oper==y)
            break;
        if(now<ele)
            break;
    }
    ll req=y-oper;
    req%=2;
    if(req==1)
    {
        auto it=s.begin();
        ll ele=(*it);
        ll now=(ele^x);
        s.erase(it);
        s.insert(now);
    }
    for(auto it:s)
        cout<<it<<' ';
    cout<<'\n';
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

Tester's Code (C++)
``/*
   - Check file formatting
   - Assert every constraint
   - Analyze testdata
*/

#include <bits/stdc++.h>
using namespace std;

/*
---------Input Checker(ref : https://pastebin.com/Vk8tczPu )-----------
*/

long long readInt(long long l, long long r, char endd)
{
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true)
    {
        char g = getchar();
        if (g == '-')
        {
            assert(fi == -1);
            is_neg = true;
            continue;
        }
        if ('0' <= g && g <= '9')
        {
            x *= 10;
            x += g - '0';
            if (cnt == 0)
            {
                fi = g - '0';
            }
            cnt++;
            assert(fi != 0 || cnt == 1);
            assert(fi != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
        }
        else if (g == endd)
        {
            if (is_neg)
            {
                x = -x;
            }

            if (!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

            return x;
        }
        else
        {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd)
{
    string ret = "";
    int cnt = 0;
    while (true)
    {
        char g = getchar();
        assert(g != -1);
        if (g == endd)
        {
            break;
        }
        cnt++;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r)
{
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r)
{
    return readInt(l, r, '\n');
}

/*
-------------Main code starts here------------------------
*/

// Note here all the constants from constraints
const int MAX_T = 1e4;
const int MAX_N = 1e5;
const int MAX_Y = 1e9;
const int MAX_A = (1 << 30);
const int SUM_N = 1e5;

// Variables to measure some parameters on test-data
int max_n = 0;
int sum_n = 0;
int max_y = 0;
int max_useful_ops = 0;
int sum_useful_ops = 0;

void solve()
{
    int n, x, y;
    n = readIntSp(1, MAX_N);
    x = readIntSp(1, MAX_A);
    y = readIntLn(1, MAX_Y);

    max_n = max(max_n, n);
    sum_n += n;

    assert(sum_n <= SUM_N);

    max_y = max(max_y, y);

    vector<int> A(n);

    for (int i = 0; i < n; i++)
    {
        if (i != n - 1)
        {
            A[i] = readIntSp(1, MAX_A);
        }
        else
        {
            A[i] = readIntLn(1, MAX_A);
        }
    }

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

    for (int i = 0; i < n; i++)
    {
        pq.push((pair<int, int>){A[i], i});
    }

    int last_index = -1;

    int useful_ops = 0;

    while (y > 0)
    {
        y--;
        useful_ops++;

        auto min_element = pq.top();
        pq.pop();

        if (last_index == min_element.second)
        {
            if (y % 2 == 0)
            {
                min_element.first ^= x;
            }

            pq.push(min_element);
            y = 0;
        }
        else
        {
            min_element.first ^= x;
            pq.push(min_element);
        }

        last_index = min_element.second;
    }

    while (!pq.empty())
    {
        cout << pq.top().first << ' ';
        pq.pop();
    }

    cout << '\n';

    sum_useful_ops += useful_ops;
    max_useful_ops = max(max_useful_ops, useful_ops);
}

signed main()
{
    int t;
    t = readIntLn(1, MAX_T);

    for (int i = 1; i <= t; i++)
    {
        solve();
    }

    // Make sure there are no extra characters at the end of input
    assert(getchar() == -1);
    cerr << "SUCCESS\n";

    // Some important parameters which can help identify weakness in testdata
    cerr << "Tests : " << t << '\n';
    cerr << "Maximum N : " << max_n << '\n';
    cerr << "Sum of N : " << sum_n << '\n';
    cerr << "Maximum useful operations : " << max_useful_ops << '\n';
    cerr << "Sum of useful operations : " << sum_useful_ops << '\n';
}
``

Editorialist's Code (C++)
``#include "bits/stdc++.h"
// #pragma GCC optimize("O3,unroll-loops")
// #pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
using namespace std;
using ll = long long int;
mt19937_64 rng(chrono::high_resolution_clock::now().time_since_epoch().count());

int main()
{
	ios::sync_with_stdio(false); cin.tie(0);

	int t; cin >> t;
	while (t--) {
		int n, x, y; cin >> n >> x >> y;
		multiset<int> s;
		for (int i = 0; i < n; ++i) {
			int a; cin >> a;
			assert(a < (1 << 30));
			s.insert(a);
		}
		while (y > 0) {
			int u = *s.begin();
			int v = u^x;
			if (v < u) break;
			--y;
			s.erase(s.begin());
			s.insert(v);
		}
		if (y%2 == 1) {
			int u = *s.begin();
			int v = u^x;
			s.erase(s.find(u));
			s.insert(v);
		}
		for (int u : s) cout << u << ' ';
		cout << '\n';
	}
}
``

</details>
