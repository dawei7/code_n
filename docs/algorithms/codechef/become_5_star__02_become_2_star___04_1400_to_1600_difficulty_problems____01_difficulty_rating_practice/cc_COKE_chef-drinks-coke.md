# Chef Drinks Coke

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COKE |
| Difficulty Rating | 1511 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [COKE](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/COKE) |

---

## Problem Statement

Chef went to the store in order to buy one can of coke. In the store, they offer $N$ cans of coke (numbered $1$ through $N$). For each valid $i$, the current temperature of the $i$-th can is $C_i$ and its price is $P_i$.

After buying a can of coke, Chef wants to immediately start walking home; when he arrives, he wants to immediately drink the whole can. It takes Chef $M$ minutes to get home from the store.

The ambient temperature outside is $K$. When a can of coke is outside, its temperature approaches the ambient temperature. Specifically, if its temperature is $t$ at some point in time:
- if $t \gt K+1$, then one minute later, its temperature will be $t-1$
- if $t \lt K-1$, then one minute later, its temperature will be $t+1$
- if $K-1 \le t \le K+1$, then one minute later, its temperature will be $K$

When Chef drinks coke from a can, he wants its temperature to be between $L$ and $R$ (inclusive). Find the cheapest can for which this condition is satisfied or determine that there is no such can.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains five space-separated integers $N$, $M$, $K$, $L$ and $R$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains two space-separated integers $C_i$ and $P_i$.

### Output
For each test case, print a single line containing one integer — the price of the can Chef should buy, or $-1$ if it is impossible to buy a can such that Chef's condition is satisfied.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $1 \le M \le 100$
- $|C_i| \le 50$ for each valid $i$
- $|K| \le 50$
- $-50 \le L \le R \le 50$
- $1 \le P_i \le 10^6$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
2
3 2 5 4 6
1 6
2 8
8 10
3 5 10 20 30
21 20
22 22
23 23
```

**Output**

```text
8
-1
```

**Explanation**

**Example case 1:** Chef should buy the second can (with price $8$), even though the first can is cheaper. If Chef bought the first can, its temperature would be $3$ when he got home, and that is outside the range $[4, 6]$.

**Example case 2:** No matter which can Chef buys, when he gets home, its temperature will be less than $20$, so there is no suitable can available in the store.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2 5 4 6
1 6
2 8
8 10
```

**Output for this case**

```text
8
```



#### Test case 2

**Input for this case**

```text
3 5 10 20 30
21 20
22 22
23 23
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COKE)

[Contest: Division 1](https://www.codechef.com/COOK109A/problems/COKE)

[Contest: Division 2](https://www.codechef.com/COOK109B/problems/COKE)

**Setter:** [Hasan](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Basic math

# PROBLEM:

Given temperatures and prices of N coke cans. You want to drink the cheapest coke which quenches your thirst. You know a coke shall quench your thirst if it’s temperature if within the range [L, R]. All these cokes lie at distance M and the normal temperature is K. For every second, if the current temperature of coke is x, it changes as follows.

- If x > K, x reduces by 1.

- If x < K, x increases by 1.

- If x == K, x remains same.

# EXPLANATION

It can be seen that we can consider each coke separately. For each coke, we need to determine whether after M seconds, whether it’s temperature is within the acceptable range, and for all cokes, we can take the one with minimum cost. If no coke satisfies, the answer is -1.

Now, what shall be the temperature of coke after M seconds. If Initial temperature is more than K, then every second, the temperature reduces, until it reaches K. Once it reaches K, it remains K. So, the final temperature can be written as max(K, C_i-M)

In other case, temperature increases every second till it reaches K. So, the final temperature can be written as min(K, C_i+M) (as we want to stop as soon as it reaches temperature K).

Hence, we can check for each code whether it is within the range [L, R] and take minimum cost.

# TIME COMPLEXITY

Time complexity is O(N) per test case.

# SOLUTIONS:

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
int n,m,k,l,r;

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,1000);
	while(T--){
		n=readIntSp(1,100);
		m=readIntSp(1,100);
		k=readIntSp(-50,50);
		l=readIntSp(-50,50);
		r=readIntLn(l,50);
		int best = 10000000;
		for(int i=0;i<n;i++){
			int c,p;
			c=readIntSp(-50,50);
			p=readIntLn(1,1000000);
			for(int j=0;j<m;j++){
				if(c > k){
					c--;
				} else if( c< k){
					c++;
				}
			}
			if(l <= c && c<= r){
				best=min(best,p);
			}
		}
		if(best == 10000000){
			cout<<-1<<endl;
		} else {
			cout<<best<<endl;
		}

	}
	assert(getchar()==-1);
}
``

Tester's Solution
``//teja349
#include <bits/stdc++.h>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <utility>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <iomanip>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
using namespace __gnu_pbds;

#define f(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) f(i,0,n)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define pb push_back
#define mp make_pair
#define vi vector< int >
#define vl vector< ll >
#define ss second
#define ff first
#define ll long long
#define pii pair< int,int >
#define pll pair< ll,ll >
#define sz(a) a.size()
#define inf (1000*1000*1000+5)
#define all(a) a.begin(),a.end()
#define tri pair<int,pii>
#define vii vector<pii>
#define vll vector<pll>
#define viii vector<tri>
#define mod (1000*1000*1000+7)
#define pqueue priority_queue< int >
#define pdqueue priority_queue< int,vi ,greater< int > >
#define flush fflush(stdout)
#define primeDEN 727999983
mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

// find_by_order()  // order_of_key
typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

int c[123456],p[123456];
int main(){
	//std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,m,k,l,r;
		cin>>n>>m>>k>>l>>r;
		int i;
		int mini=inf;
		rep(i,n){
			cin>>c[i]>>p[i];
			if(abs(c[i]-k)<=m){
				c[i]=k;
			}
			else if(c[i]>k){
				c[i]-=m;
			}
			else{
				c[i]+=m;
			}
			if(l<=c[i] && c[i]<=r){
				mini=min(mini,p[i]);
			}
		}
		if(mini==inf)
			mini=-1;
		cout<<mini<<endl;
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class COKE{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int n = ni(), m = ni(), k = ni(), l = ni(), r = ni();
	    int ans = (int)1e8;
	    for(int i = 0; i< n; i++){
	        int c = ni(), p = ni();
	        if(c > k)c = Math.max(c-m, k);
	        else if(c < k)c = Math.min(c+m, k);
	        if(l <= c && c <= r)ans = Math.min(ans, p);
	    }
	    if(ans > 1e7)ans = -1;
	    pn(ans);
	}
	//SOLUTION END
	void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
	DecimalFormat df = new DecimalFormat("0.00000000000");
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
	    new COKE().run();
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

Feel free to Share your approach, if you want to. (even if its same  ) . Suggestions are welcomed as always had been.

</details>
