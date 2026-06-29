# Chef and Pepperoni Pizza

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PEPPERON |
| Difficulty Rating | 1810 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [PEPPERON](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/PEPPERON) |

---

## Problem Statement

Chef has a pepperoni pizza in the shape of a $N \times N$ grid; both its rows and columns are numbered $1$ through $N$. Some cells of this grid have pepperoni on them, while some do not. Chef wants to cut the pizza vertically in half and give the two halves to two of his friends. Formally, one friend should get everything in the columns $1$ through $N/2$ and the other friend should get everything in the columns $N/2+1$ through $N$.

Before doing that, if Chef wants to, he may choose one row of the grid and reverse it, i.e. swap the contents of the cells in the $i$-th and $N+1-i$-th column in this row for each $i$ ($1 \le i \le N/2$).

After the pizza is cut, let's denote the number of cells containing pepperonis in one half by $p_1$ and their number in the other half by $p_2$. Chef wants to minimise their absolute difference. What is the minimum value of $|p_1-p_2|$?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains a string with length $N$ describing the $i$-th row of the grid; this string contains only characters '1' (denoting a cell with pepperonis) and '0' (denoting a cell without pepperonis).

### Output
For each test case, print a single line containing one integer — the minimum absolute difference between the number of cells with pepperonis in the half-pizzas given to Chef's friends.

### Constraints
- $1 \le T \le 1,000$
- $2 \le N \le 1,000$
- $N$ is even
- the sum of $N \cdot N$ over all test cases does not exceed $2 \cdot 10^6$

---

## Examples

**Example 1**

**Input**

```text
2
6
100000
100000
100000
100000
010010
001100
4
0011
1100
1110
0001
```

**Output**

```text
2
0
```

**Explanation**

**Example case 1:** Initially, $|p_1-p_2| = 4$, but if Chef reverses any one of the first four rows from "100000" to "000001", $|p_1-p_2|$ becomes $2$.

**Example case 2:** Initially, $|p_1-p_2| = 0$. We cannot make that smaller by reversing any row.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
100000
100000
100000
100000
010010
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
001100
4
0011
1100
1110
0001
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PEPPERON)

[Contest: Division 1](https://www.codechef.com/COOK109A/problems/PEPPERON)

[Contest: Division 2](https://www.codechef.com/COOK109B/problems/PEPPERON)

**Setter:** [Erfan Alimohammadi](https://www.codechef.com/users/erfaniaa), [Rami](https://www.codechef.com/users/i_love_islam)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Simple

# PREREQUISITES:

Basic Inclusion-exclusion.

# PROBLEM:

Given a square matrix of size N consisting of zeroes and ones only. You are allowed to reverse at most one row of the matrix. You want to minimize the difference between the number of ones in the left half and the right half of the matrix.

# EXPLANATION

Let’s assume we cannot reverse any row, and compute the answer.

Let’s compute for each row, the number of ones in the left half of current row and right half of current row, and Let leftSum be the sum of the number of ones in left halves, and rightSum be the number of ones in the right halves.

It is easy to see that the answer to this subproblem is |leftSum - rightSum|.

Now, coming back to the original problem, we are allowed to reverse only one row. Let’s see what impact it has on the final answer.

If for some row, there are x ones in left half and y ones in right half, then leftSum already contains x and rightSum already contains y. Reversing this row means there are y ones in left half now and x ones in the right half.

This leads to the number of ones in the left half being leftSum-x+y and in the right half being rightSum-y+x. So, by reversing this row, we get the difference between the number of ones in left and right half as |(leftSum-x+y) - (rightSum-y+x)|.

We can simply repeat this process for all rows and take the minimum difference obtained. Do make sure to consider case where no row is reversed.

Problem solved.

# TIME COMPLEXITY

Time complexity is O(N^2) per test case.

# SOLUTIONS:

Setter 1 Solution
``#include <bits/stdc++.h>
using namespace std;

const int max_n = 1100;
int a[max_n];

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
		int n;
		cin >> n;
		for(int i=0;i<n;i++)
		{
			a[i] = 0;
			string str;
			cin >> str;
			for(int j=0;j<n;j++)
			{
				if(str[j] == '0') continue;
				if((j)/(n/2))
					a[i]--;
				else a[i]++;
			}
		}
		int sum = 0;
		for(int i=0;i<n;i++)
			sum+=a[i];
		int ans = abs(sum);
		for(int i=0;i<n;i++)
		{
			ans = min(ans , abs(sum - 2*a[i]));
		}
		cout << ans << endl;
	}

	return 0;
}
``

Setter 2 Solution
``#include <bits/stdc++.h>
#define ll long long
using namespace std;

char s[1010][1010];
int dp[1010][1010];

int main() {
	int t;
	cin>>t;
	int n;
	while(t--){
	    scanf("%d",&n);
	    for(int i=1 ;i <=n ;i++){
	        scanf("%s",s[i]+1);
	    }

	    for(int i=1 ;i <=n ; i++){
	        for(int j=1 ;j <=n; j++){
	            dp[i][j] = dp[i][j-1] + s[i][j]-'0';
	        }
	    }
	    int r1 = 0;
	    int r2 = 0;
	    for(int i=1 ;i <=n ;i ++){
	        r1 += dp[i][n/2];
	        r2 += dp[i][n]-dp[i][n/2];
	    }

	    int mn = abs(r1-r2);
	    for(int i=1 ;i <=n ;i ++){
	        mn = min(mn,abs(r1 - 4*dp[i][n/2] +2*dp[i][n]-r2 ));
	    }
	    printf("%d\n",mn);
	}
	return 0;
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

string s[1234];

int main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		int i,j;
		rep(i,n){
			cin>>s[i];
		}
		int ans=0,val,mini=inf;
		rep(i,n){
			rep(j,n/2){
				if(s[i][j]=='1')
					ans++;
			}
		}
		rep(i,n){
			f(j,n/2,n){
				if(s[i][j]=='1')
					ans--;
			}
		}
		mini=abs(ans);
		rep(i,n){
			val=0;
			rep(j,n/2){
				if(s[i][j]=='1')
					val++;
			}
			f(j,n/2,n){
				if(s[i][j]=='1')
					val--;
			}
			ans-=val;
			val*=-1;
			ans+=val;
			mini=min(abs(ans),mini);
			ans-=val;
			val*=-1;
			ans+=val;

		}
		cout<<mini<<endl;
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class PEPPERON{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int n = ni();
	    int[][] c = new int[n][2];
	    int leftSum = 0, rightSum = 0;
	    for(int i = 0; i< n; i++){
	        String s = n();
	        for(int j = 0; j< n; j++)c[i][j/(n/2)] += s.charAt(j)-'0';
	        leftSum += c[i][0];
	        rightSum += c[i][1];
	    }
	    int ans = Math.abs(leftSum-rightSum);
	    for(int i = 0; i< n; i++){
	        ans = Math.min(ans, Math.abs(leftSum-c[i][0]+c[i][1] - rightSum+c[i][1]-c[i][0]));
	    }
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
	    new PEPPERON().run();
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
