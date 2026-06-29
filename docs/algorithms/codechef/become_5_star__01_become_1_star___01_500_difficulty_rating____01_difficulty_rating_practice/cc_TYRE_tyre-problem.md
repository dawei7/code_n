# Tyre problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TYRE |
| Difficulty Rating | 452 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TYRE](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TYRE) |

---

## Problem Statement

There are $N$ bikes and $M$ cars on the road.

- Each bike has $2$ tyres.
- Each car has $4$ tyres.

Find the total number of tyres on the road.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $N, M$.

---

## Output Format

For each test case, output in a single line,  the total number of tyres on the road.

---

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq N, M \leq 100$

---

## Examples

**Example 1**

**Input**

```text
2
2 1
3 0
```

**Output**

```text
8
6
```

**Explanation**

**Test Case $1$:** There are $2$ bikes and $1$ car. Each bike has $2$ tyres, so there are $2\cdot 2 = 4$ bike tyres. Similarly, each car has $4$ tyres, so there are $1\cdot 4 = 4$ car tyres. Adding the tyres of all vehicles, we get $4+4=8$ tyres in total.

**Test Case $2$:** There are $3$ bikes and $0$ cars. Each bike has $2$ tyres, so there are $3\cdot 2 = 6$ bike tyres. There are no cars, so there are $0\cdot 4 = 0$ car tyres. Adding the tyres of all vehicles, we get $6+0=6$ tyres in total.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3 0
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TYRE)

[Div-4 Contest](https://www.codechef.com/START29B/problems/TYRE)

***Author:*** [Arpit Kesharwani](https://www.codechef.com/users/anript)

***Tester:*** [Anshu Garg](https://www.codechef.com/users/anshugarg12)

#
[](#difficulty-2)DIFFICULTY:

CAKEWALK

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N bikes and M cars.

Each bike has 2 tyres.

Each car has 4 tyres.

Calculate total number of tyres.

#
[](#explanation-5)EXPLANATION:

Total number of tyres of bikes = 2 \cdot N.

Total number of tyres of cars = 4 \cdot M.

Total number of tyres = 2 \cdot N + 4 \cdot M.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solutions-7)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
#define ll long long int
using namespace std;

void solve()
{
        int n,m;
        cin>>n>>m;
        cout<<(2*n + 4 * m)<<"\n";
}

int main(){
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        int t;
        cin>>t;
        while(t--)solve();
        return 0;
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
    int T = readIntLn(1, 1000);
    for(int i=1;i<=T;++i) {
    	int N = readIntSp(0, 100);
    	int M = readIntLn(0, 100);
    	cout << 2 * N + 4 * M << "\n";
        cerr << N << " " << M << "\n";
        // assert(!(N == 0 && M == 0));
    }
    assert(getchar() == -1);
    return 0;
}

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
