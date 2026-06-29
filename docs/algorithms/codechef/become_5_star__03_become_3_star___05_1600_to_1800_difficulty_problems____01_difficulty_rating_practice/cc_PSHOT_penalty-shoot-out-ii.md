# Penalty Shoot-Out II

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PSHOT |
| Difficulty Rating | 1735 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [PSHOT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/PSHOT) |

---

## Problem Statement

Teams $A$ and $B$ are having a penalty shoot-out to decide the winner of their football match. Each team gets to take a shot $N$ times, and the team with the higher number of scored goals at the end wins. If the number of goals scored during the shoot-out by each team turns out to be the same even after all $2N$ shots, then they stop and agree that the result is a draw.

The two teams take shots alternately — team $A$ shoots first, then team $B$ shoots, then team $A$ and so on until team $B$ takes its $N$-th shot (at which point each team has taken exactly $N$ shots). Even though all $2N$ shots are taken, the result of the shoot-out is often known earlier — e.g. if team $A$ has already scored $N-1$ goals and team $B$ has missed at least two shots, team $A$ is definitely the winner.

For each shot, you know whether it was a goal or a miss. You need to find the earliest moment when the winner is known — the smallest $s$ ($0 \le s \le 2N$) such that after $s$ shots, the result of the shoot-out (whether team $A$ won, team $B$ won or the match is drawn) would be known even if we did not know the results of the remaining $2N-s$ shots.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains a string $S$ with length $2 \cdot N$, where for each valid $i$, the $i$-th character is '0' if the $i$-th shot was a miss or '1' if it was a goal.

### Output
For each test case, print a single line containing one integer — the smallest $s$ such that after $s$ shots, the result of the shoot-out is known.

### Constraints
- $1 \le T \le 10^5$
- $1 \le N \le 10^5$
- $S$ contains only characters '0' and '1'
- the sum of $N$ over all test cases does not exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
3
101011
3
100001
```

**Output**

```text
4
6
```

**Explanation**

**Example case 1:** After four shots, team $A$ has scored $2$ goals and team $B$ has scored $0$ goals. Whatever happens afterwards, team $A$ is guaranteed to win, since even if team $B$ scored their last (and only) goal and team $A$ did not score their last goal, team $A$ would still win by $1$ goal.

**Example case 2:** Team $A$ scores the first goal and after that, neither team scores any goals until the last shot. Up till then, there is always a possibility that the match could end in a draw if team $B$ scored a goal with its last shot, or in the victory of team $A$ if it was a miss. We can only guarantee the result after the last shot.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
101011
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
100001
```

**Output for this case**

```text
6
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/PSHOT)

[Contest](https://www.codechef.com/COOK115B/problems/PSHOT)

**Author:** [Jatin Nagpal](https://www.codechef.com/users/nagpaljatin141)

**Tester:** [Raja Vardhan Reddy](https://www.codechef.com/users/raja1999)

**Editorialist:** [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

### DIFFICULTY:

Cakewalk

### PREREQUISITES:

None

### PROBLEM:

A penalty shoot-out between two teams, A and B, taking N shots each, alternating in between shots, in which the result of each shot is known. A goes first. Find the earliest shot, after which the result of the shoot-out can be determined, irrespective of the results of the remaining shots.

### HINTS:

Not the full solution. Just some hints to help you if you are stuck at some point. As soon as you encounter a hint that you had not thought of, go back to solving the problem.

Hint 1:

There can be three possible results:

-
A is the winner, or

-
B is the winner, or

- It’s a draw.

Is it possible to determine a drawn state before all the 2*N shots have been taken?

Hint 2:

If A has scored, say, 5 goals after a particular number of shots, and B has scored 2 goals after the same number of shots, and both have, say, 2 shots remaining, is it still possible for B to catch up to and defeat A?

### QUICK EXPLANATION:

show

The result of the shoot-out can be known as soon as one of the teams has a score which is greater than - the score of the other team + the number of shots remaining for the other team. If all turns are over without a clear winner, it will be a draw. We can only know be sure of a draw after all 2N shots have been taken.

### EXPLANATION

show

Consider the following states in the shoot-out, where:

X is the number of goals scored by A till now,

Y is the number of goals scored by B till now,

LeftA is the number of shots still left for A to take, and

LeftB is the number of shots still left for B to take.

N is the total number of shots to be taken, per team.

**State 1:**

X > (Y+LeftB)

**State 2:**

Y > (X+LeftA)

**State 3:**

X \leq (Y+LeftB)  and  Y \le (X+LeftA) and total number of shots taken <2*N

**State 4:**

(LeftA=LeftB=0)

Let’s consider the above states one by one.

In **state 1**, as X > (Y+LeftB), this implies that X>Y, so A is clearly ahead of B right now. But is it still possible for B to catch up to A and beat it? In the best case scenario for B, A shall miss all their remaining shots, and B shall score in all of them. But since B has only LeftB shots remaining, the maximum score it can achieve is (Y+LeftB), which is < X. Thus, it is not possible to defeat A if such a state is reached.

In **state 2**, as Y > (X+LeftA), this implies that Y>X, so B is clearly ahead of A right now. But is it still possible for A to catch up to B and beat it? In the best case scenario for A, B shall miss all their remaining shots, and A shall score in all of them. But since A has only LeftA shots remaining, the maximum score it can achieve is (X+LeftA), which is < Y. Thus, it is not possible to defeat B if such a state is reached.

In **state 3**, irrespective of whether X<Y or Y<X or X=Y, the teams have enough shots left to catch up to or defeat the other team. Thus, we need to wait for the results of more shots, before we can determine who’s going to win the shoot-out.

In **state 4**, the teams have no more shots left. Thus, we’ll be able to determine the result of the shoot-out, based on their current scores. If, right now, X>Y, then A is the winner, if Y>X, then B is the winner, and if X=Y, then it’s a draw. In every case, we can be sure of the result now, as no more shots are left.

Thus, if the result of the shoot-out is one of the teams winning, it can be known as soon as **one of the teams has a score which is greater than : the score of the other team + the number of shots remaining for the other team.** This is because the other team won’t be able to catch up with the former team even if it manages to score in all its remaining turns and the former team misses in all its remaining turns.

While, if the result of the shoot-out is a draw, it can only be known after all the 2*N shots have been taken. This is because in a draw, the scores are equal. This implies that if A scored in it’s N^{th} shot, and the score of B was equal to the score of A before A's final shot, we’ll only be sure of the result after B's final shot, i.e., whether it will be able to equalise the score or not. On the other hand, if A misses its final shot, B still has a chance to win the game, if it scores in its final shot.

Thus, to solve the problem:

- Iterate through the shots one by one, maintaining X, Y, LeftA and LeftB,

- If after any shot, X > (Y+LeftB) or Y > (X+LeftA), we now know that one of the teams can no longer be defeated, irrespective of the results of the remaining shots. Thus, the result of the shoot-out can be known after this shot.

- If we couldn’t predict the result even after 2*N-1 shots, we can be sure of it after the 2*N^{th} shot, as no more shots are remaining for either of the teams. Thus, whatever is the score after the 2*N^{th} shot, will be the final result.

### SOLUTIONS:

Setter
``#include <bits/stdc++.h>
using namespace std;
int si(int a)
{
	if(a==0)
		return 0;
	if(a<0)
		return -1;
	return 1;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	//freopen("input.doc","r",stdin);
	//freopen("output.doc","w",stdout);
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		string s;
		cin>>n>>s;
		int a[2]={0,0};
		int b[2]={n,n};
		int ans=2*n;
		for(int i=0;i<2*n;i++)
		{
			int j=i%2;
			if(s[i]=='1')
			{
				a[j]++;
			}
			b[j]--;
			int sig[2]={si((a[0]+b[0])-(a[1]) ),si( (a[0])-(a[1]+b[1]) )};
			if(sig[0]==sig[1] && sig[0]!=0)
			{
				ans=i+1;
				break;
			}
		}
		cout<<ans<<'\n';
	}
}
``

Tester
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
	//t=1;
	while(t--){
		int n,a=0,b=0,i,rema,remb;
		string s;
		cin>>n;
		cin>>s;
		rema=n;
		remb=n;
		rep(i,s.length()){
			if(s[i]=='1'){
				if(i%2==0){
					a++;
				}
				else{
					b++;
				}
			}
			if(i%2==0){
				rema--;
			}
			else{
				remb--;
			}
			if(a>remb+b){
				cout<<i+1<<endl;
				break;
			}
			if(b>rema+a){
				cout<<i+1<<endl;
				break;
			}
			if(a==b&&remb==0){
				cout<<i+1<<endl;
				break;
			}
		}

	}
	return 0;
}
``

Editorialist

[https://www.codechef.com/viewsolution/29880426](https://www.codechef.com/viewsolution/29880426)

``//created by Whiplash99
import java.io.*;
import java.util.*;
class A
{
	public static void main(String[] args) throws IOException
	{
	    BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

	    int i,N,scA,scB,leftA,leftB;

	    int T=Integer.parseInt(br.readLine().trim());
	    StringBuilder sb=new StringBuilder();

	    while(T-->0)
	    {
	        N=Integer.parseInt(br.readLine().trim());

	        String s[]=br.readLine().trim().split("");
	        int a[]=new int[2*N+1];
	        for(i=0;i<2*N;i++)
	            a[i+1]=Integer.parseInt(s[i]);

	        scA=scB=0; //scores of both the teams
	        leftA=leftB=N; //number of turns left per team

	        for(i=1;i<=2*N;i++) //turns
	        {
	            if(i%2==1)
	            {
	                scA+=a[i];
	                leftA--;
	            }
	            else
	            {
	                scB+=a[i];
	                leftB--;
	            }

	            // Is it no longer possible to beat A?
	            // Is it no longer possible to beat B?
	            // Can no team win now (draw)?
	            if((scA>scB+leftB)||(scB>scA+leftA)||(scA==scB&&i==2*N))
	                break;
	        }
	        sb.append(i).append("\n");
	    }
	    System.out.println(sb);
	}
}
``

Feel free to share your approach if it differs. **You can ask your doubts below. Please let me know if something’s unclear.** I would LOVE to hear suggestions

</details>
