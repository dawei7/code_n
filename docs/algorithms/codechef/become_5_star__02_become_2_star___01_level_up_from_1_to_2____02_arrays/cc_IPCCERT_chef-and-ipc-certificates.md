# Chef and IPC Certificates

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | IPCCERT |
| Difficulty Rating | 922 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Arrays |
| Official Link | [IPCCERT](https://www.codechef.com/practice/course/1to2stars/LP1TO202/problems/IPCCERT) |

---

## Problem Statement

There were $N$ students (numbered $1$ through $N$) participating in the Indian Programming Camp (IPC) and they watched a total of $K$ lectures (numbered $1$ through $K$). For each student $i$ and each lecture $j$, the $i$-th student watched the $j$-th lecture for $T_{i, j}$ minutes.

Additionally, for each student $i$, we know that this student asked the question, "What is the criteria for getting a certificate?" $Q_i$ times.

The criteria for getting a certificate is that a student must have watched at least $M$ minutes of lectures in total and they must have asked the question no more than $10$ times.

Find out how many participants are eligible for a certificate.

### Input
- The first line of the input contains three space-separated integers $N$, $M$ and $K$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains $K+1$ space-separated integers $T_{i, 1}, T_{i, 2}, \ldots, T_{i, K}, Q_i$.

### Output
Print a single line containing one integer — the number of participants eligible for a certificate.

###Constraints
- $1 \le N, K \le 1,000$
- $1 \le M \le 10^6$
- $1 \le Q_i \le 10^6$ for each valid $i$
- $1 \le T_{i, j} \le 1,000$ for each valid $i$ and $j$

---

## Examples

**Example 1**

**Input**

```text
4 8 4
1 2 1 2 5
3 5 1 3 4
1 2 4 5 11
1 1 1 3 12
```

**Output**

```text
1
```

**Explanation**

- Participant $1$ watched $1 + 2 + 1 + 2 = 6$ minutes of lectures and asked the question $5$ times. Since $6 \lt M$, this participant does not receive a certificate.
- Participant $2$ watched $3 + 5 + 1 + 3 = 12$ minutes of lectures and asked the question $4$ times. Since $12 \ge M$ and $4 \le 10$, this participant receives a certificate.
- Participant $3$ watched $1 + 2 + 4 + 5 = 12$ minutes of lectures and asked the question $11$ times. Since $12 \ge M$ but $11 \gt 10$, this participant does not receive a certificate.
- Participant $4$ watched $1 + 1 + 1 + 3 = 6$ minutes of lectures and asked the question $12$ times. Since $6 \lt M$ and $12 \gt 10$, this participant does not receive a certificate.

Only participant $2$ receives a certificate.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/IPCCERT)

[Contest: Division 1](https://www.codechef.com/COOK124A/problems/IPCCERT)

[Contest: Division 2](https://www.codechef.com/COOK124B/problems/IPCCERT)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Rahul Dugar](https://www.codechef.com/users/rahuldugar)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Given the time spent by each of the N students on all K lectures, and the number of times student asked about certificates, determine the number of students who’ll receive certificates based on following criteria.

Total time spent across all lectures is at least M, and the number of times student has asked the question is up to 10.

# QUICK EXPLANATION

- We just take total of time spent over all lectures for each student and check both conditions.

# EXPLANATION

The problem statement mostly describes what to do. All we need to do is to check two conditions

- Total time spent \geq M

AND

- Number of questions asked \leq 10

We can consider each student separately, take sum of time spent over all K lectures and check above conditions. If and only if both conditions are satisfied that the student gets a certificate.

We also do not need to store times in arrays at all, since we can take total while reading input, solving problem in constant space.

# TIME COMPLEXITY

The time complexity is O(N*K) per test case. Memory complexity O(1)

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n, m, k;
	cin >> n >> m >> k;
	int a[n][k], i, j;
	int q[n];
	int ans = 0;
	for (i = 0; i < n; i++) {
		int sum = 0;
		for (j = 0; j < k; j++) {
			cin >> a[i][j];
			sum += a[i][j];
		}
		cin >> q[i];
		if (q[i] <= 10 && sum >= m)
			ans++;
	}
	cout << ans << "\n";

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
const int mod=998244353;
//const int mod=1000000007;
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

void solve() {
	int n,m,k;
//	cin>>n>>m>>k;
	n=readIntSp(1,1000);
	m=readIntSp(1,1000000);
	k=readIntLn(1,1000);
	int ans=0;
	fr(i,1,n) {
		int te=0,te2;
		fr(j,1,k) {
			te2=readIntSp(1,1000);
			te+=te2;
		}
		te2=readIntLn(1,1000000);
		if(te2<=10&&te>=m)
			ans++;
	}
	cout<<ans<<endl;
}

signed main() {
	ios_base::sync_with_stdio(0),cin.tie(0);
	srand(chrono::high_resolution_clock::now().time_since_epoch().count());
	cout<<fixed<<setprecision(7);
	int t=1;
//	cin>>t;
	fr(i,1,t)
		solve();
	assert(getchar()==EOF);
#ifdef rd
	cerr<<endl<<endl<<endl<<"Time Elapsed: "<<((double)(clock()-clk))/CLOCKS_PER_SEC<<endl;
#endif
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class IPCCERT{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni(), M = ni(), K = ni();
	    int certificates = 0;
	    for(int i = 0; i< N; i++){
	        int timeSpent = 0;
	        for(int j = 0; j< K; j++)
	            timeSpent += ni();
	        int questionAsked = ni();
	        if(timeSpent >= M && questionAsked <= 10)certificates++;
	    }
	    pn(certificates);
	}
	//SOLUTION END
	void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
	static boolean multipleTC = false;
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
	    new IPCCERT().run();
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
