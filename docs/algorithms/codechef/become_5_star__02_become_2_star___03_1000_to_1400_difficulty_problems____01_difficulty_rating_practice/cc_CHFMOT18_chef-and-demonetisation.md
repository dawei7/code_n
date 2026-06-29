# Chef and Demonetisation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFMOT18 |
| Difficulty Rating | 1250 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHFMOT18](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHFMOT18) |

---

## Problem Statement

In a country called Chef Land, there was a lot of monetary fraud, so Chefu, the head of the country, decided to choose new denominations of the local currency ― all even-valued coins up to an integer $N$ should exist. After a few days, a citizen complained that there was no way to create an odd value, so Chefu decided that he should also introduce coins with value $1$. Formally, you are given an integer $N$; for $v = 1$ and each even positive integer $v \le N$, coins with value $v$ exist.

You are also given an integer $S$. To handle transactions quickly, find the minimum number of coins needed to pay a price $S$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $S$ and $N$.

### Output
For each test case, print a single line containing one integer ― the minimum number of coins.

### Constraints
- $1 \le T \le 10,000$
- $1 \le S \le 10^9$
- $2 \le N \le 10^9$
- $N$ is even

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
4
2 2
1 14
30 10
31 4
```

**Output**

```text
1
1
3
9
```

**Explanation**

**Example case 1:** One coin with value $2$ is sufficient.

**Example case 2:** We need to use one coin with value $1$.

**Example case 3:** We need $3$ coins, each with value $10$.

**Example case 4:** We can use seven coins with value $4$, one coin with value $2$ and one coin with value $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 14
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
30 10
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
31 4
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHFMOT18)

[Contest: Division 1](https://www.codechef.com/LTIME85A/problems/CHFMOT18)

[Contest: Division 2](https://www.codechef.com/LTIME85B/problems/CHFMOT18)

**Setter:** [SHUBHAM KHANDELWAL](https://www.codechef.com/users/dean_student)

**Tester:** [Trung Nguyen](https://www.codechef.com/users/chemthan)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

Basic Math

# PROBLEM

You have currency coins for all even values up to N and coins valued 1, find the minimum number of coins required to pay price S.

# QUICK EXPLANATION

- If S is odd, then 1 value coin would be used.

- While we have S > N, we can greedily use N-valued coin.

- If there’s still some remaining price to pay, it must be even and up to N, so we can pay using 1 even-valued coin.

# EXPLANATION

Firstly, since all coins except coin valued 1 are even-valued, so if S is odd, we have to use 1-value coin at least once.

Also, since we want to minimize the number of coins used, we can see that using 2 1-valued coins is worse than using one 2-value coin. So, we can see, we use 1-value coin if and only if S is odd.

So, now we can assume S is even. Now, let’s divide all even-valued coins and S by 2, The problem becomes

Find the minimum number of coins to pay price S/2, using coins with values between 1 to N/2.

It is not hard to see that we can repeatedly choose largest valued coin, till we have paid at least S. Then we can replace the last coin with an appropriately valued coin to make sum exactly S.

The minimum number of coins needed to pay at least S is given by X = \displaystyle \Big\lceil \frac{S}{N} \Big\rceil since X*N \geq S and (X-1)*N < S

So, the final answer is \displaystyle \Big\lceil \frac{S-(S \bmod 2)}{N} \Big\rceil + (S\bmod 2)

Also, during implementation, we actually do not need to divide by 2. It was just for the ease of understanding. S-(S \bmod 2)  is basically subtracting 1 if S is odd.

**Bonus:**

What if we were given all odd valued coins and have to pay price S in minimum number of coins?

# TIME COMPLEXITY

The time complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mod 1000000007
#define test ll t; cin>>t; while(t--)
typedef long long int ll;
int main() {
	FIO;
	test{
	    ll s,n,ans=0,x;
	    cin>>s>>n;
	    if(s<=n){
	        if(s==1){
	            ans=1;
	        }
	        else if(s&1){
	            ans=2;
	        }
	        else{
	            ans=1;
	        }
	    }
	    else{
	        if(s&1){
	            ans++;
	            s--;
	        }
	        if(s%n==0){
	            ans+=(s/n);
	        }
	        else{
	            ans+=(s/n);
	            ans++;
	        }
	    }
	    printf("%lld\n",ans);
	}
	return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")

#define ms(s, n) memset(s, n, sizeof(s))
#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define FORd(i, a, b) for (int i = (a) - 1; i >= (b); --i)
#define FORall(it, a) for (__typeof((a).begin()) it = (a).begin(); it != (a).end(); it++)
#define sz(a) int((a).size())
#define present(t, x) (t.find(x) != t.end())
#define all(a) (a).begin(), (a).end()
#define uni(a) (a).erase(unique(all(a)), (a).end())
#define pb push_back
#define pf push_front
#define mp make_pair
#define fi first
#define se second
#define prec(n) fixed<<setprecision(n)
#define bit(n, i) (((n) >> (i)) & 1)
#define bitcount(n) __builtin_popcountll(n)
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vii;
const int MOD = (int) 1e9 + 7;
const int FFTMOD = 119 << 23 | 1;
const int INF = (int) 1e9 + 23111992;
const ll LINF = (ll) 1e18 + 23111992;
const ld PI = acos((ld) -1);
const ld EPS = 1e-9;
inline ll gcd(ll a, ll b) {ll r; while (b) {r = a % b; a = b; b = r;} return a;}
inline ll lcm(ll a, ll b) {return a / gcd(a, b) * b;}
inline ll fpow(ll n, ll k, int p = MOD) {ll r = 1; for (; k; k >>= 1) {if (k & 1) r = r * n % p; n = n * n % p;} return r;}
template<class T> inline int chkmin(T& a, const T& val) {return val < a ? a = val, 1 : 0;}
template<class T> inline int chkmax(T& a, const T& val) {return a < val ? a = val, 1 : 0;}
inline ull isqrt(ull k) {ull r = sqrt(k) + 1; while (r * r > k) r--; return r;}
inline ll icbrt(ll k) {ll r = cbrt(k) + 1; while (r * r * r > k) r--; return r;}
inline void addmod(int& a, int val, int p = MOD) {if ((a = (a + val)) >= p) a -= p;}
inline void submod(int& a, int val, int p = MOD) {if ((a = (a - val)) < 0) a += p;}
inline int mult(int a, int b, int p = MOD) {return (ll) a * b % p;}
inline int inv(int a, int p = MOD) {return fpow(a, p - 2, p);}
inline int sign(ld x) {return x < -EPS ? -1 : x > +EPS;}
inline int sign(ld x, ld y) {return sign(x - y);}
mt19937 mt(chrono::high_resolution_clock::now().time_since_epoch().count());
inline int mrand() {return abs((int) mt());}
inline int mrand(int k) {return abs((int) mt()) % k;}
#define db(x) cerr << "[" << #x << ": " << (x) << "] ";
#define endln cerr << "\n";

void chemthan() {
	int test; cin >> test;
	assert(1 <= test && test <= 1e4);
	while (test--) {
	    int s, n; cin >> s >> n;
	    assert(1 <= s && s <= 1e9);
	    assert(2 <= n && n <= 1e9 && n % 2 == 0);
	    int res = 0;
	    if (s & 1) {
	        res++;
	        s--;
	    }
	    if (s) {
	        res += s / min(n, s);
	        if (s % min(n, s)) {
	            res++;
	        }
	    }
	    cout << res << "\n";
	}
}

int main(int argc, char* argv[]) {
	ios_base::sync_with_stdio(0), cin.tie(0);
	if (argc > 1) {
	    assert(freopen(argv[1], "r", stdin));
	}
	if (argc > 2) {
	    assert(freopen(argv[2], "wb", stdout));
	}
	chemthan();
	cerr << "\nTime elapsed: " << 1000 * clock() / CLOCKS_PER_SEC << "ms\n";
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class CHFMOT18{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    long S = nl(), N = nl();
	    long ans = 0;

	    ans += S/N;
	    S %= N;
	    //Check 1
	    if(S%2 == 1){
	        S--;
	        ans++;
	    }
	    //Check 2
	    if(S > 0)ans++;
	    //Make sure this check 2 doesn't come before check 1, or you'll fail at cases like S = N+1
	    pn(ans);
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
	    new CHFMOT18().run();
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
