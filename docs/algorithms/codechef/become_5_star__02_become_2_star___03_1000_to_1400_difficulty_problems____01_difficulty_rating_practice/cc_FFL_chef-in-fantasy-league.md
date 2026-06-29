# Chef in Fantasy League

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FFL |
| Difficulty Rating | 1225 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [FFL](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/FFL) |

---

## Problem Statement

Chef is going to start playing Fantasy Football League (FFL) this season. In FFL, each team consists of exactly $15$ players: $2$ *goalkeepers*, $5$ *defenders*, $5$ *midfielders* and $3$ *forwards*. Chef has already bought $13$ players; he is only missing one defender and one forward.

There are $N$ available players (numbered $1$ through $N$). For each valid $i$, the $i$-th player is either a defender or a forward and has a price $P_i$. The sum of prices of all players in a team must not exceed $100$ dollars and the players Chef bought already cost him $S$ dollars.

Can you help Chef determine if he can complete the team by buying one defender and one forward in such a way that he does not exceed the total price limit?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $S$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.
- The last line contains $N$ space-separated integers. For each valid $i$, the $i$-th of these integers is $0$ if the $i$-th player is a defender or $1$ if the $i$-th player is a forward.

### Output
For each test case, print a single line containing the string `"yes"` if it is possible to build a complete team or `"no"` otherwise (without quotes).

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 100$
- $13 \le S \le 100$
- $1 \le P_i \le 100$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
2
4 90
3 8 6 5
0 1 1 0
4 90
5 7 6 5
0 1 1 0
```

**Output**

```text
yes
no
```

**Explanation**

**Example case 1:** If Chef buys the $1$-st and $3$-rd player, the total price of his team is $90 + 9 = 99$, which is perfectly fine. There is no other valid way to pick two players.

**Example case 2:** Chef cannot buy two players in such a way that all conditions are satisfied.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 90
3 8 6 5
0 1 1 0
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
4 90
5 7 6 5
0 1 1 0
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FFL)

[Contest: Division 1](https://www.codechef.com/LTIME83A/problems/FFL)

[Contest: Division 2](https://www.codechef.com/LTIME83B/problems/FFL)

**Setter:** [Shahadat Hossain Shahin](https://www.codechef.com/users/s_h_shahin)

**Tester:** [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

Greedy

# PROBLEM:

Given N available players, each of which is either a defender or a forward player, i-th player having price P_i, find whether Chef can complete his team by buying one defender and one forward player, with only 100 dollars out of which he has already spent S dollars.

# QUICK EXPLANATION

- The dollars available with Chef for defender and forward player is 100-S

- The minimum price to buy a defender is the minimum of the price of all defender players (let’s say min_D), and similarly, the minimum price to buy a forward player is minimum of price among all forward players (let’s say min_F).

- If min_D+min_F \leq 100-S, we have sufficient dollars to buy both a defender and a forward player.

# EXPLANATION

The quick explanation says it all.

First of all, we can check if there is any defender player present among N players. If there isn’t, we can never complete our team. Otherwise, we can find the minimum cost to buy a defender player. Let’s say it’s min_D

Similarly, we can check if there is any forward player present among N players. If there isn’t, we can never complete our team. Otherwise, we can find the minimum cost to buy a forward player. Let’s say it’s min_F

It is easy to see that buying player with minimum cost is optimal, as we need to minimize min_D+min_F

The number of available dollars is 100-S since out of 100, we have only 100-S dollars left.

So, if min_D+min_D \leq 100-S, we have enough dollars to complete the team, the answer is “yes”, otherwise the answer is “no”.

Bonus Problem

Suppose in the above problem, you want to minimize the number of remaining dollars after buying a froward player and a defender, and N \leq 10^5. Can you find the minimum remaining dollars?

Hint

Dynamic Programming

Even bigger Hint

[Knapsack DP](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/)

# TIME COMPLEXITY

The time complexity is O(N) per test case.

# SOLUTIONS:

Setter's Solution
``#include <bits/stdc++.h>

using namespace std;

const int MAX = 105;

int price[MAX], role[MAX];

int main() {
	// freopen("0.in", "r", stdin);
	// freopen("0.out", "w", stdout);
	int T;
	cin >> T;
	for(int t=1;t<=T;t++) {
	    int n, s;
	    cin >> n >> s;
	    for(int i=1;i<=n;i++) cin >> price[i];
	    for(int i=1;i<=n;i++) cin >> role[i];
	    string ans = "no";
	    for(int i=1;i<=n;i++) {
	        for(int j=i+1;j<=n;j++) {
	            if(role[i] == role[j]) continue;
	            if((price[i] + price[j]) <= (100 - s)) ans = "yes";
	        }
	    }
	    cout << ans << '\n';
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
//setbase - cout << setbase (16); cout << 100 << endl; Prints 64
//setfill -   cout << setfill ('x') << setw (5); cout << 77 << endl; prints xxx77
//setprecision - cout << setprecision (14) << f << endl; Prints x.xxxx
//cout.precision(x)  cout<<fixed<<val;  // prints x digits after decimal in val

using namespace std;
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

int p[1234];
signed main(){
	std::ios::sync_with_stdio(false); cin.tie(NULL);
	int t;
	cin>>t;
	while(t--){
		int n,s;
		cin>>n>>s;
		int i;
		rep(i,n){
			cin>>p[i];
		}
		int min1=1234,min2=1234,val;
		rep(i,n){
			cin>>val;
			if(val==0){
				min1=min(min1,p[i]);
			}
			else{
				min2=min(min2,p[i]);
			}
		}
		s+=min1+min2;
		if(s>100){
			cout<<"no"<<endl;
		}
		else{
			cout<<"yes"<<endl;
		}
	}

}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class FFL{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int n = ni();int remaining = 100-ni();
	    int minD = 100, minF = 100;
	    int[] price = new int[n];
	    for(int i = 0; i< n; i++)price[i] = ni();
	    for(int i = 0; i< n; i++){
	        int type = ni();
	        if(type == 0)minD = Math.min(minD, price[i]);
	        else minF = Math.min(minF, price[i]);
	    }
	    if(minF+minD <= remaining)pn("yes");
	    else pn("no");
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
	    new FFL().run();
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
