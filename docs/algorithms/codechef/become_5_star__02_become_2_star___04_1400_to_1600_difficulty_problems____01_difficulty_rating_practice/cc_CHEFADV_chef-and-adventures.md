# Chef and Adventures

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFADV |
| Difficulty Rating | 1462 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHEFADV](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHEFADV) |

---

## Problem Statement

Mysterious Chefland... Recently, Chef realised that Discuss, the educational system of Chefland, is out of date. Therefore, he is trying to find ways to update the infrastructure in the country. One possible way is to move all materials from Discuss to Discourse.

Chef will have access to Discourse if his *knowledge* and *power* become exactly equal to $N$ and $M$ respectively. Initially, he has power $1$ and knowledge $1$.

Chef can perform actions of the following types to improve his skills:
- solve a problem — increase his knowledge by $X$
- do a push-up — increase his power by $Y$
- install ShareChat to keep in touch with friends — increase both knowledge and power by $1$

Chef can only install ShareChat at most once. The remaining actions may be performed any number of times and the actions may be performed in any order.

Help Chef find out whether it is possible to move from Discuss to Discourse.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $N$, $M$, $X$ and $Y$.

### Output
For each test case, print a single line containing the string `"Chefirnemo"` if it is possible to reach the required knowledge and power or `"Pofik"` if it is impossible.

### Constraints
- $1 \le T \le 1,000$
- $1 \le N, M, X, Y \le 10^9$

### Subtasks
**Subtask #1 (30 points):** $1 \le N, M, X, Y \le 100$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
5
2 2 1 2
11 10 5 9
11 11 5 9
12 11 5 9
1 2 1 100
```

**Output**

```text
Chefirnemo
Chefirnemo
Pofik
Chefirnemo
Pofik
```

**Explanation**

**Example case 2:** We add $Y=9$ once to the power to get power $10$. We add $X=5$ twice to the knowledge to get knowledge $11$.

**Example case 3:** We can see that it is impossible to reach power $M=11$ no matter which or how many operations we do. Note that the ShareChat operation will increase both knowledge and power by $1$, and hence it will still be impossible to attain the given values of knowledge and power at the same time.

**Example case 4:** We can reach knowledge $11$ and power $10$ like in example case 2, the only difference is that we also use the ShareChat operation to increase both by $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2 1 2
```

**Output for this case**

```text
Chefirnemo
```



#### Test case 2

**Input for this case**

```text
11 10 5 9
```

**Output for this case**

```text
Chefirnemo
```



#### Test case 3

**Input for this case**

```text
11 11 5 9
```

**Output for this case**

```text
Pofik
```



#### Test case 4

**Input for this case**

```text
12 11 5 9
```

**Output for this case**

```text
Chefirnemo
```



#### Test case 5

**Input for this case**

```text
1 2 1 100
```

**Output for this case**

```text
Pofik
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/SEPT18A/problems/CHEFADV)

[Div2](https://www.codechef.com/SEPT18B/problems/CHEFADV)

[Practice](https://www.codechef.com/problems/CHEFADV)

**Setter-**  [Misha Chorniy](https://www.codechef.com/users/mgch)

**Tester-**  [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK/SIMPLE

### PRE-REQUISITES:

[Modulo Operator](https://en.wikipedia.org/wiki/Modulo_operation) (%), Basic Maths of Addition, Logic

### PROBLEM:

Let me denote knowledge by A and power by B. Now, as given in the question, we initially have A=1 and B=1. Tell if its possible for you to reach A=N AND B=M using following operations-

- Increase A by X

- Increase B by Y

- Increase A and B by 1. We can only do it once.

### QUICK-EXPLANATION:

**Key to AC-** Modulo along with careful checking for corner case (N=1 or M=1) fetched AC in first try.

The problem clearly asks if you can find two integers k and l such that either (1+X*k=N \&\& 1+Y*l=M) OR (1+X*k=N-1 \&\& 1+Y*l=M-1). Move the 1 in LHS to RHS to get equations in form (X*k=N-1 \&\& Y*l=M-1) OR (X*k=N-2 \&\& Y*l=M-2). Lets consider one equation for example, say X*k=N-1. Clearly, LHS can move **only in steps of X**. This means, X*k can **never** be equal to N-1 (for all possible integers k) if N-1 is not a multiple of X, or in other words, if N-1 is not divisible by X. Similar analogy holds in other 3 equations.

### EXPLANATION:

The problem is quite simple, hence we will have only a single section in editorial. We will discuss editorialist’s solution in those. I might sound over-explanative in the explanation below, and perhaps you may ask “Why is he now considering case only for Knowledge and not considering Power right now?” &etc. I want you, the reader, to patiently read it. I have tried to picture the thought process which should be on your mind when typically solving such easy problems, so please try to grasp it if possible.

**Editorialist’s Solution-**

For sake of formality, lets discuss the **first subtask’s solution** first. We can brute force for task 1. The idea is, keep increasing Knowledge by X as long as its less than N, and keep increasing power by Y as long as its less than M. At last, check if **Knowledge**==N \&\& **Power**==M. If not, subtract X from Knowledge and Y from Power and check **Knowledge**==N-1 \&\& **Power**==M-1.

The above fails, or gets time limit exceeded, if number of steps for Knowledge and Power to reach N and M are large.

For the full solution, first ask yourself what *exactly* do we have to check?

Let me denote knowledge by A and power by B. Now, we initially start with A=1, B=1 and have to see if we can reach A=N, B=M. At each step, we can add X to A, Y to B, or use the special operation 1 to both A and B . The special operation can be done only once.

Think on the special operation. It increases A and B by 1. When will it exactly be useful to us? It can help us reach A=N and B=M if, and only if we can reach A=N-1 and B=M-1 first. If we reach there, then we can use this special operation to reach A=N and B=M (Recall that it will increase A and B both by 1).

Now the problem reduces to, checking if we can reach (A=N \&\& B=M) OR (A=N-1 \&\& B=M-1) by moving in steps of X (for A) and Y (for B). Lets talk about A for now, the exact same thing will be later applied to B.

We initially have A=1, we can increase it in steps of X in normal operations. Say, I apply the operation k times, then my A will be -

A=1+X*k

Forget about everything else now. Just see that we have A=1+X*k, and we have to reach an integer N. When will it be possible? We see that we need-

1+X*k=N

\implies X*k=N-1

Stop there. See the LHS, i.e. X*k. k must be an integer, as number of operations is a whole number. Hence, this means LHS will **always** be a multiple of X. Also, since k can be **any** whole number, we can see that, LHS can reach any multiple of X. But can we reach numbers which are not multiples of X? No! Because if we could, then it will contradict the fact that k is a whole number (and not a fraction r decimal).

This means, all we need to check is to see if N-1 is a multiple of X or not! If it is, we can reach it, if its not, then we cannot reach it. And since we used **no special property** (i.e. no property which was only available only to A and is not available to B), we can repeat the above steps and arrive at Y*l=M-1, where l is number of times operation is done. Then, using arguments above, we conclude we can reach M iff and only if M-1 is divisible by Y!

Now lets bring the special operation into the picture. So far, we know how to check if we can reach a given number N or M from A=1 and B=1. What change does the special operation bring? See above, it just has the effect of **"If I can reach N-1 and M-1, I can then use special operation to reach N and M"**

Hence, our conditions reduce to checking-

- Check if we can reach N for knowledge and M for Power. If yes, print “Chefirnemo” else below.

- Check if we can reach N-1 for knowledge and M-1 for Power. If yes, print “Chefirnemo” else below.

- Conclude that we cannot reach A=N for knowledge and B=M for power. Wail out loud, cry, bang your head on wall and sobbingly print “Pofik”

The main aim of this editorial was not to merely explain solution of the problem, but to plant the *thought-process* which should go on your mind, as these are the common techniques, methods and tricks which will ultimately help you ace out as a programmer.

On a side note, beware of the corner case N=1 or M=1. We can prove that **special operation cannot be used if N=1 or M=1.** (Proof in bonus section.)

Try to frame the conditions in your coding language now. An implementation in C++ is given below for reference :).

Click to view
``int n,m,x,y;
	    cin>>n>>m>>x>>y;
	    assert(1<=n and n<=1000000000);
	    assert(1<=m and m<=1000000000);
	    assert(1<=x and x<=1000000000);
	    assert(1<=y and y<=1000000000);
	    n--;
	    m--;
	    if(n%x==0 and m%y==0)cout<<"Chefirnemo\n";
	    else if((n-1)%x==0 and (m-1)%y==0 and min(n,m)>0)cout<<"Chefirnemo\n";
	    else cout<<"Pofik\n";
``

### SOLUTION

The respective codes are also pasted in tabs below in case the links do not work. This is for convenience of readers, so that they can copy paste it to whichever IDE or editor they are comfortable reading it in and immediately have access to the codes.

[Setter](http://www.codechef.com/download/Solutions/SEPT18/setter/CHEFADV.cpp)

[Tester](http://www.codechef.com/download/Solutions/SEPT18/setter/CHEFADV.cpp)

Click to view
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
vii vec,vec1;
int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--){
    	int n,m,x,y;
    	cin>>n>>m>>x>>y;
    	int i;
    	vec.clear();
    	vec1.clear();
        // initial state
    	vec.pb(mp(1,1));
        // all possible states after installing Sharechat
    	rep(i,vec.size()){
    		vec1.pb(mp(vec[i].ff+1,vec[i].ss+1));
    	}

        // total possible states with possibility of installing Sharechat
    	rep(i,vec1.size()){
    		vec.pb(vec1[i]);
    	}

        // checking if required solution can be reached using states we are reachable from
    	int flag=0,val;
    	rep(i,vec.size()){
    		val=n-vec[i].ff;
    		if(val>=0 && val%x==0){
    			val=m-vec[i].ss;
    			if(val>=0 && val%y==0){
    				flag=1;
    			}
    		}

    	}

    	if(flag){
    		cout<<"Chefirnemo"<<endl;
    	}
    	else{
    		cout<<"Pofik"<<endl;
    	}
    }
    return 0;
}
``

[Editorialist](http://www.codechef.com/download/Solutions/SEPT18/editorialist/CHEFADV.cpp)

Click to view
``/*
 *
 ********************************************************************************************
 * AUTHOR : Vijju123                                                                        *
 * Language: C++14                                                                          *
 * Purpose: -                                                                               *
 * IDE used: Codechef IDE.                                                                  *
 ********************************************************************************************
 *
 Comments will be included in practice problems if it helps ^^
 */

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int mod=pow(10,9)+7;
int fastExpo(long long a,long long n, int mod)
{
    a%=mod;
    if(n==2)return a*a%mod;
    if(n==1)return a;
    if(n&1)return a*fastExpo(fastExpo(a,n>>1,mod),2,mod)%mod;
    else return fastExpo(fastExpo(a,n>>1,mod),2,mod);
}
inline void add(vector<vector<int> > &a,vector<vector<int> > &b,int mod)
{
    for(int i=0;i<a.size();i++)for(int j=0;j<a[0].size();j++)b[i][j]=(b[i][j]+a[i][j])%mod;
}

void multiply(vector<vector<int> > &a, vector<vector<int> > &b,int mod,vector<vector<int> > &temp)
{
    assert(a[0].size()==b.size());
    int i,j;
    for(i=0;i<a.size();i++)
    {
        for(j=0;j<b[0].size();j++)
        {
            temp[i][j]=0;
            for(int p=0;p<a[0].size();p++)
            {
                temp[i][j]=(temp[i][j]+1LL*a[i][p]*b[p][j])%mod;
            }
        }
    }
}

void MatExpo(vector<vector<int> > &arr,int power,int mod)
{
    int i,j,k;
    vector<vector<int> >temp,temp2,temp3;
    vector<int> init(arr[0].size());
    for(i=0;i<arr.size();i++){temp.push_back(init);}
    temp3=temp;
    temp2=temp;
    for(i=0;i<arr.size();i++)temp3[i][i]=1;
    while(power>0)
    {
        if(power&1)
        {
            multiply(arr,temp3,mod,temp);
            swap(temp3,temp);
        }
        multiply(arr,arr,mod,temp2);
        swap(arr,temp2);
        power>>=1;
    }
    swap(arr,temp3);
}

vector<int> primes;
int isComposite[1000001]={1,1};
void sieve()
{
    int i,j;
    for(i=2;i<=1000000;i++)
    {
        if(!isComposite[i])
        {
            primes.push_back(i);
            isComposite[i]=i;
        }
        for(j=0;j<primes.size() and i*primes[j]<=1000000;j++)
        {
            isComposite[primes[j]*i]=i;
            if(i%primes[j]==0)break;
        }
    }
}

int main() {
	// your code goes here
	#ifdef JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #endif
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	srand(time(NULL));
	int t;
	cin>>t;
	assert(1<=t and t<=1000);
	while(t--)
	{
	    int n,m,x,y;
	    cin>>n>>m>>x>>y;
	    assert(1<=n and n<=1000000000);
	    assert(1<=m and m<=1000000000);
	    assert(1<=x and x<=1000000000);
	    assert(1<=y and y<=1000000000);
	    n--;
	    m--;
	    if(n%x==0 and m%y==0)cout<<"Chefirnemo\n";
	    else if((n-1)%x==0 and (m-1)%y==0 and min(n,m)>0)cout<<"Chefirnemo\n";
	    else cout<<"Pofik\n";
	}
	return 0;
}
``

Time Complexity=O(1) per test case

Space Complexity=O(1) per test case

### CHEF VIJJU’S CORNER

**1.** Proof that we cannot apply special operation of ShareChat if N=1 or M=1.

Click to view

**The operation will increase BOTH N and M by 1. Once a value is increased, then it cannot be decreased by our operations!! In other words, say N=1 and we use special operation, then N will become 2 and can never be made equal to 1!! Similar argument holds for M as well.**

**2.** Solve the below 2 questions based on variants of - “Say, instead of special operation increasing A and B by 1, it did following-”

- Increase EITHER A OR B.

- Increase A and B by k instead of 1 (k can be negative)

- Is same as that in question, but can be use as many times as possible

**3.** A LOT of you guys made a silly error which got you WA in both the subtasks. It is generally known that (a-b)\%m=a\%m -b\%m if b\le a. And we can also write it as (a-b)\%m=a\%m -b\%m=a\%m -b if b<m and b<a\%m . So lot of you guys did (N-1)\% X ==0\implies N\% X==1 and similarly for M and Y. Ask yourself, is this step correct? Well, it is for 998 out of 1000 inputs, but at cases where X=1 and/or Y=1, this fails miserably, because that case b \% m= 1 \% 1=0!! Be very, very careful when doing such manipulations under modulo, and always check if they are allowed or not!

**4.** Related Problems-

-
[GIVCANDY](https://www.codechef.com/problems/GIVCANDY) - This problem is at least 2 levels higher than our current problem. Make sure to read about [Berzout’s Identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity) and [GCD](https://brilliant.org/wiki/greatest-common-divisor/) before attempting :).

</details>
