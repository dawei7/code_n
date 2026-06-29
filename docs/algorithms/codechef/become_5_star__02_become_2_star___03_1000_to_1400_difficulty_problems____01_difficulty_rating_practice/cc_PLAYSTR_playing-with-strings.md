# Playing with Strings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PLAYSTR |
| Difficulty Rating | 1108 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PLAYSTR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PLAYSTR) |

---

## Problem Statement

Chef usually likes to play cricket, but now, he is bored of playing it too much, so he is trying new games with strings. Chef's friend Dustin gave him binary strings $S$ and $R$, each with length $N$, and told him to make them identical. However, unlike Dustin, Chef does not have any superpower and Dustin lets Chef perform only operations of one type: choose any pair of integers $(i, j)$ such that $1 \le i, j \le N$ and swap the $i$-th and $j$-th character of $S$. He may perform any number of operations (including zero).

For Chef, this is much harder than cricket and he is asking for your help. Tell him whether it is possible to change the string $S$ to the target string $R$ only using operations of the given type.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a binary string $S$.
- The third line contains a binary string $R$.

### Output
For each test case, print a single line containing the string `"YES"` if it is possible to change $S$ to $R$ or `"NO"` if it is impossible (without quotes).

### Constraints
- $1 \le T \le 400$
- $1 \le N \le 100$
- $|S| = |R| = N$
- $S$ and $R$ will consist of only '1' and '0'

---

## Examples

**Example 1**

**Input**

```text
2
5
11000
01001
3
110
001
```

**Output**

```text
YES
NO
```

**Explanation**

**Example case 1:** Chef can perform one operation with $(i, j) = (1, 5)$. Then, $S$ will be "01001", which is equal to $R$.

**Example case 2:** There is no sequence of operations which would make $S$ equal to $R$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
11000
01001
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3
110
001
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PLAYSTR)

[Contest: Division 1](https://www.codechef.com/COOK108A/problems/PLAYSTR)

[Contest: Division 2](https://www.codechef.com/COOK108B/problems/PLAYSTR)

**Setter:** [Anik Sarker](https://www.codechef.com/users/imanik),  [Ezio Auditore](https://www.codechef.com/users/ezio_26)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

# PREREQUISITES:

Basic Math.

# PROBLEM:

Given two binary strings S and R, determine if it’s possible to convert string S to string R if you are allowed to swap any pair of characters in the string S any number of times (including zero times).

# EXPLANATION

Since we can make any number of swaps, we can get all possible orderings of the characters of string S. So, we need to find whether string R is one of the ordering of string S. Hence, the only condition here is that if a character is present in string R but not in string S, then no ordering of string S is same as string R, and hence the answer is NO.

Similarly, Let us suppose some character appears x times in string S and y times in string R, then a valid ordering of string S can exist if and only if x equals y. It can be proven that it is sufficient condition for the existence of the required ordering of string S.

So, in conclusion, we just need the frequency of each character to be same among both strings. This can be easily checked by maintaining the frequency of each character.

**Bonus 1:** Find out the minimum number of swaps needed to make S and R equal.

**Bonus 2:** Find out the minimum number of swaps needed to make S and R equal, if both S and R contain lowercase English characters.

**Bonus 3:** Find out the minimum number of swaps needed to make S and R equal, if only swaps among adjacent positions are allowed.

# TIME COMPLEXITY

Time complexity is O(N) per test case.

# SOLUTIONS:

Setter 1 Solution
``#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	scanf("%d",&T);

	for(int cs=1;cs<=T;cs++){
	    int N;
	    scanf("%d",&N);

	    string a,b;
	    cin>>a>>b;

	    sort(a.begin(),a.end());
	    sort(b.begin(),b.end());
	    cout<< ((a==b) ? "YES" : "NO") <<endl;
	}
}
``

Setter 2 Solution
``#include<bits/stdc++.h>
using namespace std;
int t, cs = 1, n;

string s1, s2;
int main()
{
//    freopen("input00.txt", "r", stdin);
//    freopen("output00.txt", "w", stdout);
	cin >> t;
	if(t < 1 || t > 400) assert(false);

	while(t--){

	    cin >> n >> s1 >> s2;
	    if(s1.size() != n || s2.size() != n) assert(false);
	    if(n < 1 || n > 100) assert(false);

	    int cnt0 = 0, cnt1 = 0;

	    for(int i = 0; i < n; i++){
	        if(s1[i] == '0') cnt0++;
	        else if(s1[i] == '1') cnt1++;
	        else{
	            assert(false);
	        }

	        if(s2[i] == '0') cnt0--;
	        else if(s2[i] == '1') cnt1--;
	        else{
	            assert(false);
	        }

	    }

	    if(cnt0 == 0 && cnt1 == 0) printf("YES\n");
	    else printf("NO\n");

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

int main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n;
		cin>>n;
		string s,t;
		cin>>s>>t;
		int i;
		int cnt=0;
		rep(i,n){
			if(s[i]=='1')
				cnt++;
			if(t[i]=='1')
				cnt--;
		}
		if(cnt==0){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}

	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class PLAYSTR{
	//SOLUTION BEGIN
	//Into the Hardware Mode
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int n = ni();
	    char[] c1 = n().toCharArray(), c2 = n().toCharArray();
	    int[] f = new int[2];
	    for(char c:c1)f[c-'0']++;
	    for(char c:c2)f[c-'0']--;
	    pn((f[0]==0 && f[1] == 0)?"YES":"NO");
	}
	//SOLUTION END
	void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
	long IINF = (long)1e18, mod = (long)1e9+7;
	final int INF = (int)1e9, MX = (int)2e5+5;
	DecimalFormat df = new DecimalFormat("0.00000000000");
	double PI = 3.141592653589793238462643383279502884197169399, eps = 1e-6;
	static boolean multipleTC = true, memory = false, fileIO = false;
	FastReader in;PrintWriter out;
	void run() throws Exception{
	    if(fileIO){
	        in = new FastReader("input.txt");
	        out = new PrintWriter("output.txt");
	    }else {
	        in = new FastReader();
	        out = new PrintWriter(System.out);
	    }
	    //Solution Credits: Taranpreet Singh
	    int T = (multipleTC)?ni():1;
	    pre();for(int t = 1; t<= T; t++)solve(t);
	    out.flush();
	    out.close();
	}
	public static void main(String[] args) throws Exception{
	    if(memory)new Thread(null, new Runnable() {public void run(){try{new PLAYSTR().run();}catch(Exception e){e.printStackTrace();}}}, "1", 1 << 28).start();
	    else new PLAYSTR().run();
	}
	long gcd(long a, long b){return (b==0)?a:gcd(b,a%b);}
	int gcd(int a, int b){return (b==0)?a:gcd(b,a%b);}
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
