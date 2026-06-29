# Max Mex

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXMEX |
| Difficulty Rating | 1714 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MAXMEX](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MAXMEX) |

---

## Problem Statement

Chef has a sequence of positive integers $A_1, A_2, \ldots, A_N$. He wants to choose some elements of this sequence (possibly none or all of them) and compute their MEX, i.e. the smallest positive integer which does not occur among the chosen elements. For example, the MEX of $[1, 2, 4]$ is $3$.

Help Chef find the largest number of elements of the sequence $A$ which he can choose such that their MEX is equal to $M$, or determine that it is impossible.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the maximum number of elements Chef can choose, or $-1$ if he cannot choose elements in such a way that their MEX is $M$.

### Constraints
- $1 \le T \le 100$
- $2 \le M \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
1
3 3
1 2 4
```

**Output**

```text
3
```

**Explanation**

**Example case 1:** The MEX of whole array is 3. Hence, we can choose all the elements.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MAXMEX)

[Contest: Division 1](https://www.codechef.com/COOK119A/problems/MAXMEX)

[Contest: Division 2](https://www.codechef.com/COOK119B/problems/MAXMEX)

**Setter:** [Rezwan Arefin](https://www.codechef.com/users/rezwanarefin01)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Simple

# PREREQUISITES:

None

# PROBLEM:

Given a sequence A of N integers, select the largest number of elements of A such that the MEX of the chosen sequence of selected elements is M, or determine that it’s impossible.

MEX of a sequence is the smallest positive integer not present in the sequence.

# QUICK EXPLANATION

- If the MEX of A is already less than M, it is impossible to make the MEX of any subset of A exactly M, hence it’s impossible to select a subset of A with MEX M

- Otherwise, we can remove all occurrences of M in A. The remaining elements shall form the largest subset we can select which have MEX M.

# EXPLANATION

We can view selecting a subset of A as the process of deleting the remaining elements. Let us assume the MEX of the sequence A is X.

Three cases arise

-
X = M

The given array A already has MEX M, hence it is the largest subset which is the required answer.

-
X < M

In this case, we actually need to add elements into A in order to make MEX equal to M. But, since we are not allowed to add new elements, it is impossible to make MEX M.

-
X > M

In this case, we know that all elements in the range [1, X-1] appear at least once and M \in [1, X-1]. If we delete all occurrences of M from A, the MEX of A shall become M, since all elements in the range [1, M-1] are still present, but M is not. Hence, in this case, the required subset size is N less the frequency of M in A.

**Bonus**

Given a sequence A with N elements, find the minimum number of operations to make MEX exactly M if the following operations are allowed.

- Add an element

- Remove an element

- Change the value of an element

# TIME COMPLEXITY

The time complexity is O(N) or O(N*log(N)) per test case, depending upon implementation.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = 1e5 + 5;
int t, n, m, a[N];

int main() {
  scanf("%d", &t);
  while(t--) {
	scanf("%d %d", &n, &m);

	set<int> st;
	int ans = 0, x;
	for(int i = 0; i < n; ++i) {
	  scanf("%d", &x);
	  if(x != m) st.insert(x), ++ans;
	}

	int mex = 1;
	while(st.count(mex)) ++mex;

	if(mex != m) ans = -1;
	printf("%d\n", ans);
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
int a[100005],cnt[100005];
main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,m,i;
		cin>>n>>m;
		rep(i,n){
			cin>>a[i];
			if(a[i]<=m){
				cnt[a[i]]+=1;
			}
		}
		f(i,1,m){
			if(cnt[i]==0){
				break;
			}
		}
		if(i!=m){
			// not possible to choose
			cout<<-1<<endl;
		}
		else{
			// n-occ(m) elements
			cout<<n-cnt[m]<<endl;
		}

		// clearing cnt
		rep(i,n){
			if(a[i]<=m){
				cnt[a[i]]--;
			}
		}
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MAXMEX{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni(), M = ni();
	    int mex = 1;
	    TreeSet<Integer> set = new TreeSet<>();
	    int cnt = 0;
	    for(int i = 0; i< N; i++){
	        int x = ni();
	        if(x == M)continue;
	        cnt++;
	        set.add(x);
	        while(set.contains(mex))mex++;
	    }
	    if(mex == M)pn(cnt);
	    else pn(-1);
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
	    new MAXMEX().run();
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
