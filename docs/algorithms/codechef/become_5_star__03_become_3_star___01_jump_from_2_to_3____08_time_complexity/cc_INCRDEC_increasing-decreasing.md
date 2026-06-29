# Increasing Decreasing

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INCRDEC |
| Difficulty Rating | 1557 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [INCRDEC](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/INCRDEC) |

---

## Problem Statement

Chef received a new sequence $A_1, A_2, \ldots, A_N$. He does not like arbitrarily ordered sequences, so he wants to permute the elements of $A$ in such a way that it would satisfy the following condition: there is an integer $p$ ($1 \le p \le N$) such that the first $p$ elements of the new (permuted) sequence are strictly increasing and the last $N-p+1$ elements are strictly decreasing.

Help Chef and find a permutation of the given sequence which satisfies this condition or determine that no such permutation exists. If there are multiple solutions, you may find any one.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case:
- If there is no permutation of $A$ that satisfies the given condition, print a single line containing the string `"NO"` (without quotes).
- Otherwise, print two lines.
- The first of these lines should contain the string `"YES"` (without quotes).
- The second line should contain $N$ space-separated integers ― the elements of your permuted sequence.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^5$
- $1 \le A_i \le 2 \cdot 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (50 points):**
- $N \le 10^3$
- $A_i \le 2 \cdot 10^3$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^4$

**Subtask #2 (50 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5
4
1 3 2 4
4
1 3 2 4
6
1 10 10 10 20 15
5
1 1 2 2 3
4
1 2 3 3
```

**Output**

```text
YES
1 2 3 4
YES
4 3 2 1
NO
YES
1 2 3 2 1
NO
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/INCRDEC)

[Contest: Division 1](https://www.codechef.com/LTIME85A/problems/INCRDEC)

[Contest: Division 2](https://www.codechef.com/LTIME85B/problems/INCRDEC)

**Tester:** [Trung Nguyen](https://www.codechef.com/users/chemthan)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

None

# PROBLEM

Given a sequence A of N integers. Reorder A into an increasing-decreasing sequence or determine if it is impossible to do so.

An increasing-decreasing sequence of integers is a sequence, which for some integer p (1 \leq p \leq N) have first p integers sorted in strictly increasing order and last N-p+1 elements sorted in strictly decreasing order.

# QUICK EXPLANATION

- It is possible to reorder if and only if each element appears at most twice, and the maximum element appears at most once.

- To obtain a valid increasing-decreasing order, first, print all distinct elements in increasing order and then print the remaining integers in decreasing order.

# EXPLANATION

Let’s focus on p-th element. On positions to its left as well as it’s right, all the elements are strictly smaller than this element. So, on p-th position, the maximum value must be fixed. But if the maximum value appears more than once, we cannot fit all occurrences of maximum into a valid increasing-decreasing sequence.

Hence, we need the maximum element to appear exactly once. (Think why maximum element cannot appear zero times  )

Now, having fixed the maximum element, we can add remaining values into either side of p-th element.

Since both left and right part is in strictly increasing/decreasing order, each distinct value may appear at most once in each part.

This constrains us to at most two occurrences of each distinct value. Hence, if an element appears more than twice, then also, it is impossible to reorder A into an increasing-decreasing sequence.

These impossible conditions give us the way to construct a valid sequence. Firstly, sort the given sequence A and print each distinct value present in A in sorted order. Then print the remaining elements in decreasing order.

Since each element appears at most twice and maximum element appears at most once, the generated sequence shall be a valid increasing-decreasing sequence.

**Bonus:**

Now, you are given position p in the input itself. You need to generate an increasing-decreasing sequence such that the maximum element appears at position p.

# TIME COMPLEXITY

The time complexity is O(N*log(N)) per test case (due to sorting).

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
int n;
int rep[200200];

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,100);
	while(T--){
		n=readIntLn(1,100000);
		int mx=0;
		bool ok=true;
		for(int i=0;i<n;i++){
			int x;
			if(i==n-1){
				x=readIntLn(1,200000);
			} else {
				x=readIntSp(1,200000);
			}
			rep[x]++;
			mx=max(mx,x);
			if(rep[x]> 2){
				ok=false;
			}
		}
		if(rep[mx] > 1){
			ok=false;
		}
		if(!ok){
			cout<<"NO"<<endl;
			for(int i=0;i<=200000;i++){
				rep[i]=0;
			}
			continue;
		}
		cout<<"YES"<<endl;
		for(int i=0;i<=200000;i++){
			if(rep[i]){
				cout<<i<<" ";
				rep[i]--;
			}
		}
		for(int i=200000;i>=0;i--){
			if(rep[i]){
				cout<<i<<" ";
				rep[i]--;
			}
		}
		cout<<endl;
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
	assert(1 <= test && test <= 1e2);
	int sumn = 0;
	while (test--) {
	    int n; cin >> n;
	    sumn += n;
	    assert(1 <= n && n <= 1e5);
	    assert(1 <= sumn && sumn <= 1e6);
	    vi a(n);
	    FOR(i, 0, n) cin >> a[i];
	    if (n == 1) {
	        cout << "YES\n";
	        cout << a[0] << "\n";
	        continue;
	    }
	    sort(all(a));
	    if (a[n - 2] == a[n - 1]) {
	        cout << "NO\n";
	        continue;
	    }
	    vi v1, v2;
	    FOR(i, 0, n - 1) {
	        if (!i || a[i] != a[i - 1]) {
	            v1.pb(a[i]);
	        }
	        else {
	            v2.pb(a[i]);
	        }
	    }
	    int found = 0;
	    FOR(i, 0, sz(v2) - 1) {
	        if (v2[i] == v2[i + 1]) {
	            found = 1;
	        }
	    }
	    reverse(all(v2));
	    if (found) {
	        cout << "NO\n";
	        continue;
	    }
	    cout << "YES\n";
	    FOR(i, 0, sz(v1)) cout << v1[i] << " ";
	    cout << a[n - 1] << " ";
	    FOR(i, 0, sz(v2)) cout << v2[i] << " ";
	    cout << "\n";
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
class INCRDEC{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni();
	    int[] A = new int[N];
	    for(int i = 0; i< N; i++)A[i] = ni();
	    Arrays.sort(A);
	    boolean[] vis = new boolean[N];
	    int[] ans = new int[N];
	    int c = 0;
	    for(int i = 0; i< N; i++)if(i == 0 || A[i] != A[i-1]){
	        ans[c++] = A[i];
	        vis[i] = true;
	    }
	    boolean possible = true;
	    for(int i = N-1; i>= 0; i--){
	        if(vis[i])continue;
	        possible &= A[i] < ans[c-1];//It'll become false in case of duplicates
	        ans[c++] = A[i];
	    }
	    if(possible){
	        pn("YES");
	        for(int i:ans)p(i+" ");pn("");
	    }else pn("NO");
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
	    new INCRDEC().run();
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
