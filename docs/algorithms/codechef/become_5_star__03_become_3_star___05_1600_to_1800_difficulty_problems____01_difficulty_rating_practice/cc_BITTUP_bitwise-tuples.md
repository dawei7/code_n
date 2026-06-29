# Bitwise Tuples

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BITTUP |
| Difficulty Rating | 1634 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [BITTUP](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/BITTUP) |

---

## Problem Statement

Chef has two numbers $N$ and $M$. Help Chef to find number of integer $N$-tuples $(A_1, A_2, \ldots, A_N)$ such that $0 \leq A_1, A_2, \ldots, A_N \leq 2^M - 1$ and $A_1 \& A_2 \& \ldots \& A_N = 0$, where $\&$ denotes the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

Since the number of tuples can be large, output it modulo $10^9+7$.

### Input
- The first line contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $N$ and $M$.

### Output
For each test case, output in a single line the answer to the problem modulo $10^9+7$.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq N, M \leq 10^6$

###Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
1 2
2 2
4 2
8 4
```

**Output**

```text
1
9
225
228250597
```

**Explanation**

**Test Case $1$:** The only possible tuple is $(0)$.

**Test Case $2$:** The tuples are $(0, 0)$, $(0, 1)$, $(0, 2)$, $(0, 3)$, $(1, 0)$, $(2, 0)$, $(3, 0)$, $(1, 2)$, $(2, 1)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 2
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
4 2
```

**Output for this case**

```text
225
```



#### Test case 4

**Input for this case**

```text
8 4
```

**Output for this case**

```text
228250597
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE21A/problems/BITTUP)

[Contest Division 2](https://www.codechef.com/JUNE21B/problems/BITTUP)

[Contest Division 3](https://www.codechef.com/JUNE21C/problems/BITTUP)

[Practice](https://www.codechef.com/problems/BITTUP)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm) and [Souradeep](https://www.codechef.com/users/souradeep_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

Basic Maths

# PROBLEM

Chef has two numbers N and M. Help Chef to find number of integer N-tuples (A_1, A_2, \ldots, A_N) such that 0 \leq A_1, A_2, \ldots, A_N \leq 2^M - 1 and A_1 \& A_2 \& \ldots \& A_N = 0, where \& denotes the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

# QUICK EXPLANATION

- For each bit, we can choose a subset of given N integers, which shall have a current bit set. Only bad case is when all N integers have the current bit set. So there are 2^N-1 ways to choose a subset of positions having current bit set.

- Subsets of positions having ith bit on is independent of values of other bits. So for each bit, we have 2^N-1 ways, leading to (2^N-1)^M

# EXPLANATION

### Solving for M = 1

We have to choose N integers where each integer may be 0 or 1 such that the bitwise AND of these numbers is zero. There are total 2^N ways to select integers, since we have two choices for each of the N integers.

The only bad case, where bitwise AND of numbers is non-zero, is when all values are 1. Subtracting from 2^N, we can see that there are 2^N-1 ways to choose N integers such that their bitwise AND is zero.

Intuitively, this makes sense. Let’s assume S denotes the set of positions of 1s. There are 2^N such subsets. The only subset, which has non-zero AND is when all positions are included. There’s only 1 such subset. Hence, the number of subsets of positions with zero AND is 2^N-1

### Solving for M > 1

Let us try to extend our previous solution. What happens when M = 2?

We know from the definition of bitwise AND, that AND operation is applied individually on each bit. Hence, for each bit, we need to choose a subset of N positions with bitwise AND  to be 0. Hence, for each bit, there are 2^N-1 valid ways to choose subsets of positions with that bit on.

Since **each bit is independent of each other**, then by [Fundamental Rule of Counting](https://brilliant.org/wiki/fundamental-counting-principle/), we can see that the number of ways would be multiplied, resulting in \displaystyle \prod_{i = 1}^M (2^N-1) = (2^N-1)^M

### Implementation

Since we need to compute (2^N-1)^M \bmod MOD, we need to use binary exponentiation, as computing powers linearly will time out.

Article on Fundamental rule of counting [here](https://www.intmath.com/counting-probability/2-basic-principles-counting.php).

Some good resources explaining Binary Exponentiation are [this](https://cp-algorithms.com/algebra/binary-exp.html), [this](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) and [this](https://iq.opengenus.org/binary-exponentiation/)

# TIME COMPLEXITY

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;
const int maxn = 1e6 + 10, maxm = 1e6 + 10, mod = 1e9 + 7;
ll dp[maxn];
ll add(ll a, ll b){
    a += b;
    if(a >= mod)a -= mod;
    return a;
}
ll mul(ll a, ll b){
    a *= b;
    if(a >= mod)a %= mod;
    return a;
}
ll rpe(ll a, ll b){
    ll ans = 1;
    while(b != 0){
        if(b & 1)ans = mul(ans, a);
        a = mul(a, a); b >>= 1;
    }
    return ans;
}
int main()
{
    dp[0] = 1;
    for(int i = 1; i < maxn; i++)dp[i] = dp[i - 1] * 2 % mod;
    int t; cin >> t;
    int n, m;
    while(t--){
        cin >> n >> m;
        cout << rpe((dp[n] + mod - 1) % mod, m) << endl;
    }
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>

#ifdef HOME
    #include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
	    char g = getchar();
	    if (g == '-') {
		    assert(fi == -1);
		    is_neg = true;
		    continue;
	    }
	    if ('0' <= g && g <= '9') {
		    x *= 10;
		    x += g - '0';
		    if (cnt == 0) {
			    fi = g - '0';
		    }
		    cnt++;
		    assert(fi != 0 || cnt == 1);
		    assert(fi != 0 || is_neg == false);

		    assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
	    }
	    else if (g == endd) {
		    assert(cnt > 0);
		    if (is_neg) {
			    x = -x;
		    }
		    assert(l <= x && x <= r);
		    return x;
	    }
	    else {
		    //assert(false);
	    }
    }
}

string readString(int l, int r, char endd) {
    string ret = "";
    int cnt = 0;
    while (true) {
	    char g = getchar();
	    assert(g != -1);
	    if (g == endd) {
		    break;
	    }
	    cnt++;
	    ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
    return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
    return readString(l, r, ' ');
}

template<typename T>
T powMod(T a, T pw, T mod)
{
    T res(1);
    while (pw)
    {
	    if (pw & 1)
	    {
		    res = (res * a) % mod;
	    }
	    pw >>= 1;
	    a = (a * a) % mod;
    }
    return res;
}

int main(int argc, char** argv)
{
#ifdef HOME
    if(IsDebuggerPresent())
    {
	    freopen("../in.txt", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 100'000);
    const int64_t MOD = 1'000'000'007;
    forn(tc, T)
    {
	    int64_t N = readIntSp(1, 1'000'000);
	    int64_t M = readIntLn(1, 1'000'000);
	    int64_t a = powMod<int64_t>(2, N, MOD);
	    --a;//a cannot be zero, so we can subtract
	    int64_t r = powMod<int64_t>(a, M, MOD);
	    printf("%lld\n", r);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class BITTUP{
    //SOLUTION BEGIN
    final long MOD = (long)1e9+7;
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), M = ni();
        long candidates = (pow(2, N)+MOD-1)%MOD;
        long ways = pow(candidates, M);
        pn(ways);
    }
    long pow(long a, long p){
        long o = 1;
        while(p > 0){
            if(p%2 == 1)o = o*a%MOD;
            a = a*a%MOD;
            p /= 2;
        }
        return o;
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new BITTUP().run();
    }
    int bit(long n){return (n==0)?0:(1+bit(n&(n-1)));}
    void p(Object o){out.print(o);}
    void pn(Object o){out.println(o);}
    void pni(Object o){out.println(o);out.flush();}
    String n()throws Exception{return in.next();}
    String nln()throws Exception{return in.nextLine();}
    int ni()throws Exception{return Integer.parseInt(in.next());}
    long nl()throws Exception{return Long.parseLong(in.next());}
    double nd()throws Exception{return Double.parseDouble(in.next());}

    class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        public FastReader(String s) throws Exception{
            br = new BufferedReader(new FileReader(s));
        }

        String next() throws Exception{
            while (st == null || !st.hasMoreElements()){
                try{
                    st = new StringTokenizer(br.readLine());
                }catch (IOException  e){
                    throw new Exception(e.toString());
                }
            }
            return st.nextToken();
        }

        String nextLine() throws Exception{
            String str = "";
            try{
                str = br.readLine();
            }catch (IOException e){
                throw new Exception(e.toString());
            }
            return str;
        }
    }
}
``

Feel free to share your approach. Suggestions are welcomed as always.

</details>
