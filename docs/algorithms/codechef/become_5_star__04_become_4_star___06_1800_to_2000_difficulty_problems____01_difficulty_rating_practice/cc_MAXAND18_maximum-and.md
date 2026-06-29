# Maximum AND

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXAND18 |
| Difficulty Rating | 1908 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [MAXAND18](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/MAXAND18) |

---

## Problem Statement

Chef's good friend Shubham has an assignment to complete, but he is too lazy to do it, so he asked Chef to help him. On the other hand, Chef was busy in the kitchen, so he in turn asked you to help Shubham.

You are given a sequence of positive integers $A_1, A_2, \ldots, A_N$ and an integer $K$. For any positive integer $X$ such that exactly $K$ bits in the binary representation of $X$ are equal to $1$, consider the sum $S = \sum_{i=1}^N (X \wedge A_i)$; here, $\wedge$ denotes bitwise AND. You should choose $X$ in such a way that $S$ is maximum possible. If there is more than one such value of $X$, you should find the smallest one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the smallest possible value of $X$.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $1 \le K \le 30$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

### Subtasks
**Subtask #1 (50 points):** $K \le 2$

**Subtask #2 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
4 1
3 4 5 1
```

**Output**

```text
4
```

**Explanation**

**Example case 1:** Exactly one bit in $X$ should be $1$. Our options are:
- If $X = 1$, $S = 1+0+1+1 = 3$.
- If $X = 2$, $S = 2+0+0+0 = 2$.
- If $X = 4$, $S = 0+4+4+0 = 8$.
- For any greater valid $X$, $S = 0$.

The maximum value of $S$ is $8$, so the answer is the only value of $X$ where we get $S = 8$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXAND18)

[Contest: Division 1](https://www.codechef.com/LTIME85A/problems/MAXAND18)

[Contest: Division 2](https://www.codechef.com/LTIME85B/problems/MAXAND18)

**Setter:** [SHUBHAM KHANDELWAL](https://www.codechef.com/users/dean_student)

**Tester:** [Trung Nguyen](https://www.codechef.com/users/chemthan)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

Greedy

# PROBLEM

Given a sequence A of N integers, you must choose an integer X such that X has exactly K bits set and \displaystyle\sum_{i = 1}^N A_i \wedge X is maximized where \wedge denotes bitwise AND. Among all such X, you must find the minimum possible value of X.

# QUICK EXPLANATION

- We can write the above expression in terms of the contribution of each bit individually. If there are C_b integers with b-th bit on, b-th bit can contribute C_b*2^b to the answer.

- We find contribution for each bit and sort, first in decreasing order of value and then by increasing order of the bits (to minimize X) and select first K bits.

# EXPLANATION

Let’s notice how AND function behaves. Suppose X has x-th and y-th bit ON and rest all bits OFF. We can see that we can write the sum as \displaystyle\sum_{i = 1}^N A_i \wedge 2^x + \sum_{i = 1}^N A_i \wedge 2^y since AND operation works independently for each bit.

This allows us to separate the contribution of each bit into the final sum for some X. Formally, if some bit b is set in X, we add 2^b exactly C_b times, where C_b is the number of integers in A having b-th bit ON.

Hence, for each bit, we can calculate C_b beforehand. Now b-th bit, if set in X, contributes 2^b*C_b to final sum. Hence, we need to select K bits among these, to maximize sum and then minimize X for maximum sum.

Hence, we can sort these (bit, gain) pairs, first in non-increasing order of gain and then in increasing order of bit (to minimize X) and choose first K bits in this sorting. This allows us to reconstruct optimum value of X.

**Bonus:**

Maximize \displaystyle\sum_{i = 1}^N A_i \vee X where vee denotes bitwise OR, by choosing some X with K bits set.

# TIME COMPLEXITY

The time complexity is O(N*B) where B = 30 denotes the number of bits.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define FIO ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define mod 1000000007
#define test ll tx; cin>>tx; while(tx--)
typedef long long int ll;
int main() {
	FIO;
	ll power[31];
	ll i;
	power[0]=1;
	for(i=1;i<=30;i++){
	    power[i]=2*power[i-1];
	}
	test{
	    ll n,k,x,i,j;
	    cin>>n>>k;
	    ll a[n];
	    for(i=0;i<n;i++){
	        cin>>a[i];
	    }
	    ll count[31];
	    for(i=0;i<31;i++){
	        count[i]=0;
	    }
	    for(i=0;i<n;i++){
	        x=a[i];
	        j=0;
	        while(x!=0){
	            if(x%2==1){
	                count[j]++;
	            }
	            x/=2;
	            j++;
	        }
	    }
	    vector<pair<ll,ll>>res;
	    x=1;
	    for(i=0;i<=30;i++){
	        res.push_back(make_pair(count[i]*x,50-i));
	        x*=2;
	    }
	    sort(res.begin(),res.end());
	    ll ans=0;
	    for(i=30;i>30-k;i--){
	        ans+=power[50-res[i].second];
	    }
	    cout<<ans<<endl;
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
	assert(1 <= test && test <= 1e3);
	while (test--) {
	    int n, k; cin >> n >> k;
	    assert(1 <= n && n <= 1e5);
	    assert(1 <= k && k <= 30);
	    vi a(n);
	    vi f(30);
	    FOR(i, 0, n) {
	        cin >> a[i];
	        assert(1 <= a[i] && a[i] <= 1e9);
	        FOR(j, 0, 30) {
	            f[j] += bit(a[i], j);
	        }
	    }
	    vector<pair<long long, int>> vals;
	    FOR(j, 0, 30) {
	        vals.pb({f[j] * (1LL << j), -j});
	    }
	    sort(all(vals)), reverse(all(vals));
	    vals.resize(k);
	    int res = 0;
	    FOR(i, 0, k) res |= 1 << -vals[i].se;
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
class MAXAND18{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni(), K = ni(), B = 30;
	    int[] A = new int[N];
	    for(int i = 0; i< N; i++)A[i] = ni();
	    //Computing gain for each bit
	    long[][] gain = new long[B][2];
	    for(int b = 0; b< B; b++)gain[b] = new long[]{b, 0L};
	    for(int i = 0; i< N; i++)
	        for(int b = 0; b< B; b++)
	            gain[b][1] += A[i]&(1L<<b);
	    Arrays.sort(gain, (long[] l1, long[] l2) -> {
	        if(l1[1] != l2[1])return Long.compare(l2[1], l1[1]);//Sorting in non-increasing order of gain
	        return Long.compare(l1[0], l2[0]);//Choosing smallest bit among all bits having same gain
	    });
	    long X = 0;
	    for(int b = 0; b< K; b++)X |= 1<<gain[b][0];
	    pn(X);
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
	    new MAXAND18().run();
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
