# Destroy Cells

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DESTCELL |
| Difficulty Rating | 2297 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [DESTCELL](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/DESTCELL) |

---

## Problem Statement

Anas is playing an amazing game on a grid with $N$ rows and $M$ columns. The rows are numbered $1$ through $N$ from top to bottom and the columns are numbered $1$ through $M$ from left to right.

Anas wants to destroy this grid. To do that, he wants to send two heroes from the top left cell to the bottom right cell:
- The first hero visits cells in row-major order: $(1,1) \rightarrow (1,2) \rightarrow \ldots \rightarrow (1,M) \rightarrow (2,1) \rightarrow (2,2) \rightarrow \ldots \rightarrow (2,M) \rightarrow \ldots \rightarrow (N,M)$.
- The second hero visits cells in column-major order: $(1,1) \rightarrow (2,1) \rightarrow \ldots \rightarrow (N,1) \rightarrow (1,2) \rightarrow (2,2) \rightarrow \ldots \rightarrow (N,2) \rightarrow \ldots \rightarrow (N,M)$.

We know that each hero destroys the first cell he visits, rests in the next $K$ cells he visits without destroying them, then destroys the next cell he visits, rests in the next $K$ cells, destroys the next cell, and so on until he reaches (and rests in or destroys) the last cell he visits.

Anas does not know the value of $K$. Therefore, for each value of $K$ between $0$ and $N \cdot M - 1$ inclusive, he wants to calculate the number of cells that will be destroyed by at least one hero. Can you help him?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $M$.

### Output
For each test case, print a single line containing $N \cdot M$ space-separated integers as described above.

### Constraints
- $1 \le T \le 100$
- $2 \le N, M \le 1,000$
- the sum of $N \cdot M$ over all test cases does not exceed $2 \cdot 10^6$

### Subtasks
**Subtask #1 (30 points):**
- $2 \le N, M \le 50$
- the sum of $N \cdot M$ over all test cases does not exceed $5,000$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
2 3
```

**Output**

```text
6 4 3 3 2 1
```

**Explanation**

**Example case 1:**
- $K = 0$: All cells will be destroyed by the heroes.
- $K = 1$: The first hero will destroy the cells $[(1,1), (1,3), (2,2)]$, while the second one will destroy the cells $[(1,1), (1,2), (1,3)]$.
- $K = 2$: The first hero will destroy the cells $[(1,1), (2,1)]$, while the second one will destroy the cells $[(1,1), (2,2)]$.
- $K = 3$: The first hero will destroy the cells $[(1,1), (2,2)]$, while the second one will destroy the cells $[(1,1), (1,3)]$.
- $K = 4$: The first hero will destroy the cells $[(1,1), (2,3)]$ and the second one will also destroy the cells $[(1,1), (2,3)]$.
- $K = 5$ : The first hero will destroy the cell $(1,1)$ and the second one will also destroy the cell $(1,1)$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DESTCELL)

[Contest: Division 1](https://www.codechef.com/LTIME75A/problems/DESTCELL)

[Contest: Division 2](https://www.codechef.com/LTIME75B/problems/DESTCELL)

**Setter:** [Rami](https://www.codechef.com/users/i_love_islam)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Easy

# PREREQUISITES:

[Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

# PROBLEM:

Given a grid with N rows and M columns, two heroes move from (1, 1) to (N, M), one moving row-wise, and other is moving column-wise. For each K \in [0, N*M-1], both heroes destroy the cell they are standing on, move K cells forward till the move outside the grid. Find the number of cells destroyed by at least one hero for each value of K. Grid is independent for each value of K.

# EXPLANATION

Let us consider each value of K separately.

For each K, let us simulate the process of both heroes and mark the cells visited.

If we simulate the process one-by-one cell, it would lead to time complexity O((N*M)^2) which is too much.

For both heroes, let’s directly jump directly to the next cell to be destroyed, since other cells remain unaffected. We can see, we visit exactly (N*M)/K cells. Summing over each K, it gives total N*M*\Big( \displaystyle\sum_{i = 1}^{K}\frac{1}{i}\Big) steps. The summation is approximately equal to ln(N*M) as mentioned [here](https://en.wikipedia.org/wiki/Harmonic_number#Calculation), so overall complexity is O(N*M*ln(N*M)).

So, we directly jump to the next cell to destroy, maintain a counter for the number of cells destroyed as well as marking the destroyed cells (to avoid double-counting). After calculating this for a specific K, we also need to reset visited array in the same manner.

Knowledge of Sieve of Eratosthenes would make the idea crystal clear.

# TIME COMPLEXITY

The time complexity is O(N*M*ln(N*M)) per test case.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
#define ll  long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define sc second
#define fr first
using namespace std;

const int NM = 1e6+10;
const int N = 1e3+10;
const int M = 1e3+10;

pii hero1[NM];
pii hero2[NM];
bool vis[N][M];

int main()  {
	int t;
	cin>>t;
	while(t--){
	    int n,m;
	    scanf("%d%d",&n,&m);

	    int k =0;
	    for(int i=0 ; i<n ;i ++){
	        for(int j=0 ;j <m ;j ++){
	            hero1[k++] = {i,j};
	        }
	    }
	    k =0;
	    for(int j=0 ; j<m ;j ++){
	        for(int i=0 ;i <n ;i ++){
	            hero2[k++] = {i,j};
	        }
	    }

	    for(int i=1;i <=n*m ; i++){
	        if(i-1)printf(" ");
	        int res =0;
	        for(int j=0; j <n*m ; j+= i){
	            vis[hero1[j].fr][hero1[j].sc] = 1;
	            res++;
	        }

	        for(int j=0; j <n*m ; j+= i){
	            if(!vis[hero2[j].fr][hero2[j].sc])
	                res++;
	        }

	        printf("%d",res);

	        for(int j=0; j <n*m ; j+= i){
	            vis[hero1[j].fr][hero1[j].sc] = 0;
	        }

	    }

	    printf("\n");
	}
	return 0;
}
``

Tester's Solution
``//raja1999

//#pragma comment(linker, "/stack:200000000")
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")

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
//setbase - cout << setbase (16)a; cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 <<endl;prints xxx77
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
#define int ll

typedef tree<
int,
null_type,
less<int>,
rb_tree_tag,
tree_order_statistics_node_update>
ordered_set;

//std::ios::sync_with_stdio(false);
vii a,b;
vii vec;
int vis[1005][1005];
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t,t1;
	cin>>t;
	t1=t;
	while(t--){
		int n,m,i,j,ans,id;
		a.clear();
		b.clear();
		cin>>n>>m;
		f(i,1,n+1){
			f(j,1,m+1){
				a.pb(mp(i,j));
			}
		}
		f(i,1,m+1){
			f(j,1,n+1){
				b.pb(mp(j,i));
			}
		}
		f(i,0,n*m){
			vec.clear();
			ans=0;
			id=0;
			while(id<n*m){
				vis[a[id].ff][a[id].ss]=1;
				vec.pb(a[id]);
				id+=i+1;
				ans++;
			}
			id=0;
			while(id<n*m){
				if(vis[b[id].ff][b[id].ss]==0){
					ans++;
				}
				id+=i+1;
			}
			rep(j,vec.size()){
				vis[vec[j].ff][vec[j].ss]=0;
			}
			cout<<ans<<" ";
		}
		cout<<endl;
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class DESTCELL{
	//SOLUTION BEGIN
	int[][] factors;
	void pre() throws Exception{factors = factors((int)1e6);}
	void solve(int TC) throws Exception{
	    int n = ni(), m = ni();
	    int[] ans = new int[1+n*m];
	    for(int i = 0; i< n; i++){
	        for(int j = 0; j< m; j++){
	            int x = i*m+j, y = i+j*n;
	            int g = gcd(x, y);
	            for(int v:factors[x])ans[v]++;
	            for(int v:factors[y])ans[v]++;
	            for(int v:factors[g])ans[v]--;
	        }
	    }
	    for(int i = 1; i<= n*m; i++)p(1+ans[i]+" ");pn("");
	}
	int[][] factors(int MAX){
	    MAX++;
	    int[][] fact = new int[MAX][];
	    fact[0] = new int[]{};
	    int[] spf = new int[MAX];
	    for(int i = 2; i<MAX; i++)if(spf[i]==0)for(int j = i; j< MAX; j+=i)if(spf[j]==0)spf[j] = i;
	    for(int i = 1; i< MAX; i++){
	        int cnt = 1, x = i;
	        while(x>1){
	            int p = spf[x],c= 1;
	            while(x%p==0){x/=p;c++;}
	            cnt*=c;
	        }
	        fact[i] = new int[cnt];
	        fact[i][0] = 1;int cur = 1;
	        x = i;
	        while(x>1){
	            int p = spf[x], c = 1;
	            while(x%p==0){x/=p;c++;}
	            for(int j = 0; j< cur; j++)for(int k = 1; k< c; k++)fact[i][k*cur+j] = fact[i][(k-1)*cur+j]*p;
	            cur*=c;
	        }
	    }
	    return fact;
	}
	int gcd(int x, int y){
	    return x == 0?y:gcd(y%x, x);
	}
	class Pair implements Comparable<Pair>{
	    int r, c;
	    public Pair(int R, int C){
	        r = R;c = C;
	    }
	    public int compareTo(Pair p){
	        if(r != p.r)return Integer.compare(r, p.r);
	        return Integer.compare(c, p.c);
	    }
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
	    new DESTCELL().run();
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

Feel free to share your approach, if you want to. (even if its same  ) . Suggestions are welcomed as always had been.

</details>
