# Flip the String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FLIP |
| Difficulty Rating | 1538 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [FLIP](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/FLIP) |

---

## Problem Statement

You are given two binary strings $A$ and $B$ with the same length.

You may perform the following operation any number of times (including zero): pick a substring of $A$ with odd length and invert all the bits (change '0' to '1' or vice versa) at odd positions in this substring. For example, if we choose a substring "**0**1**0**1**1**", we can convert it to "**1**1**1**1**0**" (bits at odd positions are bold).

Determine the minimum number of operations required to change the string $A$ to the string $B$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single string $A$.
- The second line contains a single string $B$.

### Output
For each test case, print a single line containing one integer — the minimum number of operations required.

### Constraints
- $1 \le T \le 10^3$
- $1 \le |A| = |B| \le 10^5$
- $A$ and $B$ contain only characters '0' and '1'
- the sum of $|A|$ over all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
3
100001
110111
1010
1010
000
111
```

**Output**

```text
2
0
2
```

**Explanation**

**Example case 1:** Initially, $A$ is "100001". We choose the substring "**0**0**0**" between the $2$-nd and $4$-th character and convert it to "**1**0**1**".

Now $A$ becomes "110101". We choose the string "**0**" containing only the $5$-th character and convert it to "**1**".

Finally, $A$ becomes "110111", which is equal to $B$.

**Example case 2:** $A$ and $B$ are initially equal, so there is no need to perform any operation.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100001
110111
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
1010
1010
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
000
111
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FLIP)

[Contest: Division 1](https://www.codechef.com/COOK124A/problems/FLIP)

[Contest: Division 2](https://www.codechef.com/COOK124B/problems/FLIP)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

None

# PROBLEM

Given two binary strings A and B of same length, we need to determine the minimum number of operations to apply on A to convert A into B.

An operation involves picking an odd length substring of A and flipping all bits at odd position **within this substring**

# QUICK EXPLANATION

- Since each operation can affect positions of only same parity modulo 2, we can divide this into two simpler sub-problems, by splitting

- Dividing both A and B into two strings each, odd indexed positions in one string (A_o and B_o) and even indexed positions in other string (A_e and B_e).

- The operation now becomes to flip a consecutive segment, either in A_o or in A_e, in order to make A_o same as B_o and A_e same as B_e

- It can be solved by a single pass over each string, maintaining the number of flips needed to make prefix of A_o and B_o and extending at each step.

# EXPLANATION

Let’s consider an example of operation `A = 0101101011`, we apply operation at substring

A_{3,7} = `11010`, we get `0100111111`, as only bits at position 3, 5 and 7 are flipped in original string. Similarly, if operation is applied at A_{2,4}, we get `0111111011`  as only positions 2 and 4 are flipped.

**Crucial Observation**

It’s easy to prove that no matter which substring we choose, the operation only affects either odd positioned bits, or even positioned bits.

Let’s split A into two strings A_o containing odd positioned bits of A in original order, and A_e containing even positioned bits of A in original order. Let’s do same for B.

Since our operation always affected consecutive bits of same parity, the operation on A is equivalent to flipping a consecutive sub-string of A_o or A_e, and the goal becomes to make A_o same as B_o and A_e same as B_e

Since both sub-problems are same, Let’s just focus on making A_e same as B_e

Another thing we can prove is that in optimal case, no two operation sub-strings would overlap, since for the overlap interval, flipping it twice gives same sub-string.

Hence, for each position, we can determine whether it needs to be flipped or not (by taking XOR of A_o and A_e). Let’s call this C_o

It’s intuitive to prove that the number of flips needed is the number of blocks consisting of ones in C_o.

We can similarly find C_e and add the operations needed for both odd and even positioned bits separately to get required number of operations.

# TIME COMPLEXITY

Time complexity is O(N) per test case.

# SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define endl "\n"
#define int long long

const int N = 2e5 + 5;

int32_t main()
{
	IOS;
	int t;
	cin >> t;
	assert(t >= 1 && t <= 1000);
	int sumlen = 0;
	while(t--)
	{
		string a, b;
		cin >> a >> b;
		assert(a.size() == b.size());
		assert(a.size() >= 1 && a.size() <= 1e5);
		sumlen += a.size();
		assert(sumlen <= 1e5);
		int ans = 0;
		int n = a.size();
		for(int i = 0; i < n; i += 2)
		{
			if(a[i] == b[i])
				continue;
			while(i < n && a[i] != b[i])
				i += 2;
			ans++;
		}
		for(int i = 1; i < n; i += 2)
		{
			if(a[i] == b[i])
				continue;
			while(i < n && a[i] != b[i])
				i += 2;
			ans++;
		}
		cout << ans << endl;
	}
	return 0;
}
``

Tester's Solution
``#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/rope>
using namespace __gnu_pbds;
using namespace __gnu_cxx;
#ifndef rd
#define trace(...)
#define endl '\n'
#endif
#define pb push_back
#define fi first
#define se second
#define int long long
typedef long long ll;
typedef long double f80;
#define double long double
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sz(x) ((long long)x.size())
#define fr(a,b,c) for(int a=b; a<=c; a++)
#define rep(a,b,c) for(int a=b; a<c; a++)
#define trav(a,x) for(auto &a:x)
#define all(con) con.begin(),con.end()
const ll infl=0x3f3f3f3f3f3f3f3fLL;
const int infi=0x3f3f3f3f;
//const int mod=998244353;
const int mod=1000000007;
typedef vector<int> vi;
typedef vector<ll> vl;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> oset;
auto clk=clock();
mt19937_64 rang(chrono::high_resolution_clock::now().time_since_epoch().count());
int rng(int lim) {
	uniform_int_distribution<int> uid(0,lim-1);
	return uid(rang);
}
int powm(int a, int b) {
	int res=1;
	while(b) {
		if(b&1)
			res=(res*a)%mod;
		a=(a*a)%mod;
		b>>=1;
	}
	return res;
}

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

int sum_n=0;
int holve(string a, string b) {
	int d=0,an=0;
	for(int i=0; i<sz(a); i++) {
		if(d) {
			if(a[i]==b[i])
				d=0;
		} else {
			if(a[i]!=b[i]) {
				d=1;
				an++;
			}
		}
	}
	return an;
}
void solve() {
	string a=readStringLn(1,100000);
	string b=readStringLn(sz(a),sz(a));
	int n=sz(a);
	sum_n+=n;
	assert(sum_n<=100000);
	string pa,pb,ppa,ppb;
	for(int i=0; i<n; i++) {
		if(i&1) {
			pa+=a[i];
			pb+=b[i];
		} else {
			ppa+=a[i];
			ppb+=b[i];
		}
	}
	cout<<holve(pa,pb)+holve(ppa,ppb)<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(7);
	int t=readIntLn(1,1000);
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
//	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class FLIP{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
	String A = n(), B = n();
	StringBuilder[] a = new StringBuilder[]{new StringBuilder(), new StringBuilder()};
	StringBuilder[] b = new StringBuilder[]{new StringBuilder(), new StringBuilder()};
	int N = A.length();
	hold(A.length() == B.length());
	for(int i = 0; i< N; i++){
	    a[i%2].append(A.charAt(i));
	    b[i%2].append(B.charAt(i));
	}
	pn(calc(a[0].toString(), b[0].toString())+calc(a[1].toString(), b[1].toString()));
    }
    int calc(String A, String B) throws Exception{
	hold(A.length() == B.length());
	int flip = 0, ans = 0;
	for(int i = 0; i< A.length(); i++){
	    int d = (A.charAt(i)-'0')^(B.charAt(i)-'0');
	    if(d != flip){
	        ans++;
	        flip ^= 1;
	    }
	}
	return (ans+1)/2;
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
	new FLIP().run();
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

# VIDEO EDITORIAL (Hindi):

# VIDEO EDITORIAL (English):

Feel free to share your approach. Suggestions are welcomed as always.

</details>
