# Gold Mining

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GOLMINE |
| Difficulty Rating | 2033 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [GOLMINE](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/GOLMINE) |

---

## Problem Statement

Chef and Chefu are working as gold miners. There are a total of $N$ gold mines, numbered $1$ through $N$. For each valid $i$, the $i$-th gold mine contains $G_i$ gold in total; if only Chef worked in it, it would take him $A_i$ days to completely mine it, while if only Chefu worked in it, it would take him $B_i$ days.

Each of our miners may only work in one mine at a time, but they may decide to start working in another mine at any time (even in the middle of some day), any number of times. They also choose the mines to work in independently from each other and they may work in the same mine at the same time. Mining gold is a continuous process, i.e. if a miner works for $t$ days (where $t$ is a real number) in a mine where this miner has mining speed $g$ gold per day, then he will mine $g \cdot t$ gold. Obviously, it is impossible to work in a mine after no gold remains in it. For example, if a gold mine contains $30$ gold and Chef needs $2$ days to completely mine it, but he spends $1$ day in it, then he will mine $15$ gold; if Chefu needs $1$ day to completely mine the same gold mine, and both Chef and Chefu start working in this mine at the same time, it will be empty after $2/3$ days ― Chefu will mine $20$ gold, while Chef will mine $10$ gold.

At each point of time, both Chef and Chefu know the gold mine in which the other miner is working. Each of them wants to gather the maximum amount of gold for himself. Find the amounts of gold the miners will have if they both act optimally.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains three space-separated integers $G_i$, $A_i$ and $B_i$.

### Output
For each test case, print a single line containing two space-separated real numbers ― the amount of gold mined by Chef and the amount of gold mined by Chefu. Your answer will be considered correct if the absolute or relative error of each amount of gold does not exceed $10^{-6}$.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 10^5$
- $1 \le G_i \le 10^5$ for each valid $i$
- $1 \le A_i \le 10^5$ for each valid $i$
- $1 \le B_i \le 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (50 points):** $N \le 2$

**Subtask #2 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
1
30 2 1
3
10 1 1
20 2 2
30 3 3
```

**Output**

```text
10.00000 20.00000
30.00000 30.00000
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
30 2 1
3
```

**Output for this case**

```text
10.00000 20.00000
```



#### Test case 2

**Input for this case**

```text
10 1 1
20 2 2
30 3 3
```

**Output for this case**

```text
30.00000 30.00000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/GOLMINE)

[Contest: Division 1](https://www.codechef.com/LTIME85A/problems/GOLMINE)

[Contest: Division 2](https://www.codechef.com/LTIME85B/problems/GOLMINE)

**Tester:** [Trung Nguyen](https://www.codechef.com/users/chemthan)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

Observations

# PROBLEM

Chef and Chefu work as gold miners. There are N gold mines numbered from 1 to N, i-th mine having G_i gold. If Chef alone works in mine numbered i, it’d take him A_i days to completely mine it. Similarly, if Chefu alone works in mine numbered i, it’d take him B_i days to completely mine it.

Find the maximum amount of gold each miner can mine if both mine optimally.

# QUICK EXPLANATION

- Both Chef and Chefu always work in the same gold mine till it is empty, so we can consider each gold mine independently and divide gold in ratio B_i: A_i among Chef and Chefu.

- We don’t even need to obtain the order of mining since this sum remains same for each order.

# EXPLANATION

Firstly, Let’s denote P_i = G_i/A_i and Q_i = G_i/B_i denote the amount of gold Chef and Chefu mines from i-th mine in a day.

Now, let’s assume X and Y denote the total gold Chef and Chefu respectively can collect if both of them work in same mine at all times.

**Lemma:** Chef and Chefu always work in the same mine at all times in the optimal choice of mines.

**Proof:** Suppose, at some time, Chef and Chefu are working in the different mine, and Let’s say Chef is about to get more than X gold (implying Chefu would get less than Y gold). Then Chefu can always switch to the mine Chef is working, to gain at least Y units of gold, which is the optimal choice for Chefu.

Similarly, if Chefu is about to get more than Y gold (implying Chef would get less than X gold), then Chef would immediately switch to mine the same as Chefu, to obtain X gold, which is the optimal choice for Chef.

Hence, we can see that in the optimal choice by both Chef and Chefu, they would always work in same mine, till it’s empty.

So, all we need to do is to calculate the values of X and Y, which shall be our required maximum amount of gold Chef and Chefu can mine.

For some mine i, in one day, P_i+Q_i gold is mined, Chef and Chefu works in this mine for \displaystyle \frac{G_i}{P_i+Q_i} days. Hence, Chef mines \displaystyle P_i*\frac{G_i}{P_i+Q_i} and Chefu mines \displaystyle Q_i*\frac{G_i}{P_i+Q_i} from i-th mine. So, we take this sum for all mines.

# TIME COMPLEXITY

The time complexity is O(N) per test case.

# SOLUTIONS

Setter's Solution
``#include <iostream>
#include <algorithm>
#include <string>
#include <assert.h>
using namespace std;

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
			assert(cnt>0);
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
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

int T;
long long G[100100];
long long A[100100],B[100100];
int n;

int main(){
	//freopen("02.txt","r",stdin);
	//freopen("02o.txt","w",stdout);
	cout.precision(13);
	cout<<fixed;
	T=readIntLn(1,10000);
	while(T--){
		n=readIntLn(1,100000);
		for(int i=0;i<n;i++){
			G[i] = readIntSp(1,100000);
			A[i]= readIntSp(1,100000);
			B[i] = readIntLn(1,100000);
		}
		long double a=0,b=0;
		for(int i=0;i<n;i++){
			a += G[i] * B[i] / (long double) ( A[i]+ B[i]);
			b += G[i] * A[i] / (long double) ( A[i]+ B[i]);
		}

		cout<<a<<" "<<b<<endl;
	}
	assert(getchar()==-1);
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
	int sumn = 0;
	while (test--) {
	    int n; cin >> n;
	    sumn += n;
	    assert(1 <= n && n <= 1e5);
	    assert(1 <= sumn && sumn <= 1e6);
	    double x = 0, y = 0;
	    FOR(i, 0, n) {
	        int g, a, b; cin >> g >> a >> b;
	        assert(1 <= g && g <= 1e5);
	        assert(1 <= a && a <= 1e5);
	        assert(1 <= b && b <= 1e5);
	        x += (double) g * b / (a + b);
	        y += (double) g * a / (a + b);
	    }
	    cout << prec(9) << x << " " << y << "\n";
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
import java.text.DecimalFormat;
class GOLMINE{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni();
	    double ans1 = 0.0, ans2 = 0.0;
	    for(int i = 0; i< N; i++){
	        double G = nl(), A = nl(), B = nl();
	        double sp = 1/A+1/B;
	        ans1 += (G/sp)*(1/A);
	        ans2 += (G/sp)*(1/B);
	    }
	    DecimalFormat df = new DecimalFormat("0.000000000");
	    pn(df.format(ans1)+" "+df.format(ans2));
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
	    new GOLMINE().run();
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
