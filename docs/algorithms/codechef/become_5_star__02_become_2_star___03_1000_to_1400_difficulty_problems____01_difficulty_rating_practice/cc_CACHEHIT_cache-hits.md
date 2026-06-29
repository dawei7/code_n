# Cache Hits

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CACHEHIT |
| Difficulty Rating | 1320 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CACHEHIT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CACHEHIT) |

---

## Problem Statement

Chef has a memory machine. It has one layer for data storage and another layer for cache. Chef has stored an array with length $N$ in the first layer; let's denote its elements by $A_0, A_1, \ldots, A_{N-1}$. Now he wants to load some elements of this array into the cache.

The machine loads the array in blocks with size $B$: $A_0, A_1, \ldots, A_{B-1}$ form a block, $A_B, A_{B+1}, \ldots, A_{2B-1}$ form another block, and so on. The last block may contain less than $B$ elements of Chef's array. The cache may only contain at most one block at a time. Whenever Chef tries to access an element $A_i$, the machine checks if the block where $A_i$ is located is already in the cache, and if it is not, loads this block into the cache layer, so that it can quickly access any data in it. However, as soon as Chef tries to access any element that is outside the block currently loaded in the cache, the block that was previously loaded into the cache is removed from the cache, since the machine loads a new block containing the element that is being accessed.

Chef has a sequence of elements $A_{x_1}, A_{x_2}, \ldots, A_{x_M}$ which he wants to access, in this order. Initially, the cache is empty. Chef is wondering how many times the machine will need to load a block into the cache layer. Can you help him calculate this number?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $B$ and $M$.
- The second line contains $M$ space-separated integers $x_1, x_2, \ldots, x_M$.

### Output
For each test case, print a single line containing one integer ― the number of times the machine loads a block into the cache.

### Constraints
- $1 \le T \le 100$
- $1 \le N, B, M \le 5,000$
- $0 \le x_i \lt N$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
1
5 3 3
0 3 4
```

**Output**

```text
2
```

**Explanation**

**Example case 1:** The machine stores elements $[A_0, A_1, A_2]$ in one block and $[A_3, A_4]$ in another block. When accessing $A_0$, the block $[A_0, A_1, A_2]$ is loaded. Then, accessing $A_3$ removes the previous block from the cache and loads the block $[A_3, A_4]$. Finally, when Chef accesses $A_4$, a new block is not loaded, since the block containing $A_4$ is currently loaded in the cache.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CACHEHIT)

[Contest: Division 1](https://www.codechef.com/COOK119A/problems/CACHEHIT)

[Contest: Division 2](https://www.codechef.com/COOK119B/problems/CACHEHIT)

**Setter:** [Rezwan Arefin](https://www.codechef.com/users/rezwanarefin01)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Basic Math

# PROBLEM:

Chef has a memory machine divided into N units numbered from 0 to N-1. Each B memory units are grouped together, that is, that is A_0,\ldots, A_{B-1} is stored in a block, A_B,\ldots, A_{2B-1} in another block and so on. The last block may contain less than B array elements.

Whenever the chef accesses an element, the whole block gets loaded into cache, if not already loaded.

Chef access memory M times, accessing memory unit i_j in j-th access. Find the number of times the cache is reloaded.

# QUICK EXPLANATION

- For first access, the block containing the first accessed element shall always be loaded.

- After that, only when the block of the previously accessed element is different from the block of the current element, we load the new block into the cache.

# EXPLANATION

First of all, how to find the block of a memory position x?

Here's how

 \displaystyle\bigg\lfloor \frac{x}{B} \bigg\rfloor  gives us the block number of memory position x

Now, the first access element’s block shall be loaded.

After that, we keep track of the current loaded block. If the next element also lies in the same block, then we don’t need to reload. Otherwise, we have to reload. We also update the current block.

pseudocode

``current := -1 //Denoting empty cache
count = 0
for x in access:
      if x/B != current:
            cur := x/B
            count++
``

**Bonus:**

You have a cache that can store at most K values. Every time you access some element, if it is not present in the cache, the least recently used element is removed from the cache if the cache is full and the accessed element is added.

Find the contents of the cache after M access operations.

# TIME COMPLEXITY

The time complexity is O(M) per test case.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

const int N = 1e5 + 5;
int n, t, b, m;

int main() {
  scanf("%d", &t);
  while(t--) {
	scanf("%d %d %d", &n, &b, &m);
	int prev = 1e9, i, ans = 0;
	while(m--) {
	  scanf("%d", &i);
	  ans += (i / b) != (prev / b);
	  prev = i;
	}
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

main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,m,b,pos,prev,ans=0,i;
		cin>>n>>b>>m;
		prev=-1;
		for(i=0;i<m;i++){
			cin>>pos;
			if(pos/b != prev){
				ans++;
			}
			prev=pos/b;
		}
		cout<<ans<<endl;
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class CACHEHIT{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int N = ni(), B = ni(), M = ni();
	    int prev = -1, ans = 0;
	    //prev is the block currently loaded into memory
	    for(int i = 0; i< M; i++){
	        int bl = ni()/B;//block of current element
	        if(prev != bl)ans++;
	        prev = bl;
	    }
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
	    new CACHEHIT().run();
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
