# Bomb the base

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BOMBTHEBASE |
| Difficulty Rating | 982 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [BOMBTHEBASE](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/BOMBTHEBASE) |

---

## Problem Statement

In Chefland, there are $N$ houses numbered from $1$ to $N$, $i^{th}$ house has a defence system having strength $A_i$.

Chef suspects a bomb drop on **one** of the houses very soon. A bomb with attack strength $X$ can destroy the $i^{th}$ house, if the defence system of the $i^{th}$ house $A_i$, is **strictly less** than $X$.

Also, when the $i^{th}$ house is destroyed due to the bomb, all houses with indices $j$ such that $1 \leq j < i$ get destroyed as well irrespective of their defence system.

Given **one** bomb with attack strength $X$, find the **maximum** number of houses that can get destroyed.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- First line of each test case contains $2$ integers $N , X$.
- Second line of test case contains $N$ space separated integers $A_1, A_2,\ldots ,A_N$.

---

## Output Format

For each test case, output in a single line the maximum number of houses that can get destroyed if the bomb can hit any house.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq X \leq 10^9$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
2
8 6
4 1 6 1 6 5 6 8
2 1
3 5
```

**Output**

```text
6
0
```

**Explanation**

**Test Case $1$:** The bomb can only destroy houses $1, 2, 4,$ and $6$.
- If it hits house $1$, only house $1$ is destroyed.
- If it hits house $2$, houses $1$ and $2$ are destroyed.
- If it hits house $4$, houses $1, 2, 3$ and $4$ are destroyed.
- If it hits house $6$, houses $1, 2, 3, 4, 5,$ and $6$ are destroyed.

The maximum number of destroyed houses is $6$.

**Test Case $2$:** The  bomb cannot destroy any of the houses as the defence system of each house is not lesser than attack power of bomb. Thus, the total number of destroyed houses is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
8 6
4 1 6 1 6 5 6 8
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
2 1
3 5
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Div-3 Contest](https://www.codechef.com/START29C/problems/BOMBTHEBASE)

[Div-4 Contest](https://www.codechef.com/START29D/problems/BOMBTHEBASE)

***Author:*** [Akshat Gupta](https://www.codechef.com/users/akshat468)

***Tester:*** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

***Editorialist:*** [Akshat Gupta](https://www.codechef.com/users/akshat468)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#problem-3)PROBLEM:

Given an Array A of length N and an integer X.

we need to find the farthest index such A_i < X

#
[](#explanation-4)EXPLANATION:

In the Problem it is given that if we destroy the i^{th} house all the bases before it get destroyed.

So we need to find maximum i such that A_i < X

For this we can simply iterate over the array and find the largest i which satisfies the given condition.

#
[](#solutions-5)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
    int n,x;cin>>n>>x;
    int ans=0;
    for(int i=0;i<n;i++){
        int a;cin>>a;
        if(a<x)ans=i+1;
    }
    cout<<ans<<endl;
}

int main()
{
    int t;
    cin>>t;
    while(t--)
        solve();
}
``
````

Tester's Solution
``#include<bits/stdc++.h>
using namespace std ;

#define ll              long long
#define pb              push_back
#define all(v)          v.begin(),v.end()
#define sz(a)           (ll)a.size()
#define F               first
#define S               second
#define INF             2000000000000000000
#define popcount(x)     __builtin_popcountll(x)
#define pll             pair<ll,ll>
#define pii             pair<int,int>
#define ld              long double

template<typename T, typename U> static inline void amin(T &x, U y){ if(y < x) x = y; }
template<typename T, typename U> static inline void amax(T &x, U y){ if(x < y) x = y; }

#ifdef LOCAL
#define debug(...) debug_out(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) 2401
#endif

long long readInt(long long l,long long r,char end){
    long long x = 0;
    int cnt = 0;
    int first =-1;
    bool is_neg = false;
    while(true) {
        char g = getchar();
        if(g == '-') {
            assert(first == -1);
            is_neg = true;
            continue;
        }
        if('0' <= g && g <= '9') {
            x *= 10;
            x += g - '0';
            if(cnt == 0) {
                first = g - '0';
            }
            ++cnt;
            assert(first != 0 || cnt == 1);
            assert(first != 0 || is_neg == false);

            assert(!(cnt > 19 || (cnt == 19 && first > 1)));
        }
        else if(g == end) {
            if(is_neg) {
                x = -x;
            }
            assert(l <= x && x <= r);
            return x;
        }
        else {
            assert(false);
        }
    }
}
string readString(int l,int r,char end){
    string ret = "";
    int cnt = 0;
    while(true) {
        char g = getchar();
        assert(g != -1);
        if(g == end) {
            break;
        }
        ++cnt;
        ret += g;
    }
    assert(l <= cnt && cnt <= r);
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

int _runtimeTerror_()
{
    int T = readIntLn(1, 100);
    int mx_N = 0, mn_N = 1e6, sum_N = 0;
    for(int i=1;i<=T;++i) {
    	int N = readIntSp(1, 1e5), X = readIntLn(1, 1e9);
    	amax(mx_N, N);
    	amin(mn_N, N);
    	sum_N += N;
    	cerr << N << " " << X << "\n";
    	vector<int> a(N);
    	for(int i=0;i<N-1;++i) {
    		a[i] = readIntSp(1, 1e9);
    	}
    	a[N - 1] = readIntLn(1, 1e9);
    	int ans = 0;
    	for(int i=N-1;i>=0;--i) {
    		if(a[i] < X) {
    			ans = i + 1;
    			break;
    		}
    	}
    	cout << ans << "\n";
    }

    cerr << T << "\n";
    cerr << mn_N << " " << mx_N << " " << sum_N << "\n";
    assert(sum_N <= 1e5);
    assert(getchar() == -1);
    return 0;
}

// <= X instead of < X
// constraints on sum_N, and mx_N should be 1e5 in one case atleast

int main()
{
    // ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
    #ifdef runSieve
        sieve();
    #endif
    #ifdef NCR
        initncr();
    #endif
    int TESTS = 1;
    //cin >> TESTS;
    while(TESTS--) {
        _runtimeTerror_();
    }
    return 0;
}
``
````

</details>
