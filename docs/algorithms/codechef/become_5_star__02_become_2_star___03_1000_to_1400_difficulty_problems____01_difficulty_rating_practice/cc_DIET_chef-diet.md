# Chef Diet

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIET |
| Difficulty Rating | 1025 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [DIET](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DIET) |

---

## Problem Statement

Chef decided to go on a diet during the following $N$ days (numbered $1$ through $N$). Part of the diet plan is to eat $K$ grams of protein during each day. For each valid $i$, Chef wants to buy $A_i$ grams of protein in the morning of the $i$-th day and then eat $K$ grams of protein as part of his dinner. If he has any protein remaining, he can store it and use it in later dinners. Initially, Chef is storing $0$ grams of protein.

Determine whether Chef will have enough protein all the time during his diet. In case he will not have enough, find the first day on which Chef will be unable to eat $K$ grams of protein.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case:
- If Chef will have enough protein during his diet, print a single line containing the string `"YES"`.
- Otherwise, print a single line containing the string `"NO"`, followed by a space and one integer — the first day when Chef will be unable to eat $K$ grams of protein.

### Constraints
- $1 \le T \le 200$
- $1 \le N \le 100$
- $1 \le K \le 10^6$
- $1 \le A_i \le 10^6$ for each valid $i$

---

## Examples

**Example 1**

**Input**

```text
3
4 5
7 3 6 5
3 4
3 10 10
3 4
8 1 1
```

**Output**

```text
YES
NO 1
NO 3
```

**Explanation**

**Example case 1:** On the first day, Chef buys $7$ grams, eats $5$ and stores $2$ grams for later. On the second day, he buys $3$ grams, so he has $5$ grams, which is just enough for the dinner on this day. On the third day, he buys $6$ grams, eats $5$ and stores $1$, and on the fourth day, he buys $5$ grams, so he has $6$ grams — enough for dinner. In the end, he had enough protein to eat during all four dinners.

**Example case 2:** Chef needs to eat $4$ grams of protein on the first day, but he only has $3$ grams, so he does not have a sufficient amount of protein already for the first dinner.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 5
7 3 6 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 4
3 10 10
```

**Output for this case**

```text
NO 1
```



#### Test case 3

**Input for this case**

```text
3 4
8 1 1
```

**Output for this case**

```text
NO 3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIET)

[Contest: Division 1](https://www.codechef.com/COOK112A/problems/DIET)

[Contest: Division 2](https://www.codechef.com/COOK112B/problems/DIET)

**Setter:** [Hasan](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# [](#difficulty-2)DIFFICULTY:

Cakewalk

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Chef decided to go on a diet during the following N days (numbered 1 through N). Part of the diet plan is to eat K grams of protein each day. For each valid i, Chef wants to buy A_i grams of protein in the morning of the i-th day and then eat K grams of protein as part of his dinner. If he has any protein remaining, he can store it and use it in later dinners. Initially, Chef is storing 0 grams of protein.

Determine whether Chef will have enough protein all the time during his diet. In case he will not have enough, find the first day on which Chef will be unable to eat K grams of protein.

# [](#quick-explanation-5)QUICK EXPLANATION

- We can keep a single variable S denoting the number of grams of protein yet not consumed. Every day, we increase S by A_i and check if sufficient protein is available for that day or not.

- If it is available for all days, the answer is YES, otherwise the answer is NO, and we print the first day when there’s not enough protein.

# [](#explanation-6)EXPLANATION

Let us denote the number of grams of proteins available, yet not consumed by S. We can see that now, buying proteins is simply increasing S by A_i and consuming K grams of proteins is represented by reducing S by K.

The condition of the availability of sufficient protein represents that S must be non-negative at all times.

Hence, our problem becomes, Given an array A of length N and K and we have S = 0 (No previous supplies of protein)

So, we can simulate the process for N days, first adding A_i and then subtracting K while making sure S remains non-negative. If it becomes negative, the first day it becomes negative is our answer.

# [](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per test case.

# [](#solutions-8)SOLUTIONS:

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

int a[1234];
int main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,k;
		cin>>n>>k;
		int i;
		int val,ans=0;
		rep(i,n){
			cin>>a[i];
		}
		rep(i,n){
			ans+=a[i];
			ans-=k;
			if(ans<0){
				break;
			}
		}
		if(i==n){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<" "<<i+1<<endl;
		}
		int j;
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class DIET{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int n = ni(), k = ni();
	    long[] a = new long[1+n];
	    for(int i = 1; i<= n; i++)a[i] = ni()+a[i-1];
	    int ans = n+1;
	    for(int i = 1; i<= n; i++){
	        if(a[i] < i*k){ans = i;break;}
	    }
	    if(ans == n+1)pn("YES");
	    else pn("NO "+ans);
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
	    new DIET().run();
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
