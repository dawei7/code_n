# Magician versus Chef

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAGICHF |
| Difficulty Rating | 1088 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [MAGICHF](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/MAGICHF) |

---

## Problem Statement

When Chef was visiting a fair in Byteland, he met a magician. The magician had $N$ boxes (numbered $1$ through $N$) and a gold coin. He challenged Chef to play a game with him; if Chef won the game, he could have the coin, but if he lost, the magician would kidnap Chef.

At the beginning of the game, the magician places the gold coin into the $X$-th box. Then, he performs $S$ swaps. To win, Chef needs to correctly identify the position of the coin after all swaps.

In each swap, the magician chooses two boxes $A$ and $B$, moves the contents of box $A$ (before the swap) to box $B$ and the contents of box $B$ (before the swap) to box $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $X$ and $S$.
- $S$ lines follow. Each of these lines contains two space-separated integers $A$ and $B$ denoting a pair of swapped boxes.

### Output
For each test case, print a single line containing one integer — the number of the box containing the gold coin after all swaps are performed.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 10^5$
- $1 \le S \le 10^4$
- $1 \le X, A, B \le N$
- $A \neq B$
- the sum of $S$ for all test cases does not exceed $2*10^5$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
5 2 4
4 2
3 4
3 2
1 2
```

**Output**

```text
1
```

**Explanation**

**Example case 1:**
- after the first swap, the coin is in box $4$
- after the second swap, the coin is in box $3$
- after the third swap, the coin is in box $2$
- after the fourth swap, the coin is in box $1$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/SEPT18A/problems/MAGICHF)

[Div2](https://www.codechef.com/SEPT18B/problems/MAGICHF)

[Practice](https://www.codechef.com/problems/MAGICHF)

**Setter-**  [Shivam Gupta](https://www.codechef.com/users/shivam_g1470)

**Tester-**  [Teja Vardhan Reddy](https://www.codechef.com/users/teja349)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

[Looping, Conditionals Basic Coding](https://www.hackerrank.com/domains/tutorials/30-days-of-code) .

### PROBLEM:

There is a gold coin under box at index X. S swaps are performed where two boxes are exchanged. We need to tell that finally, i.e. after all swaps are done, which indexed box has gold coin under it.

### QUICK-EXPLANATION:

**Key to AC-** Having coded 5-6 problems from cakewalk question is enough to solve this problem. Looping, Conditionals and swapping of variables is needed.

We initially know that gold coin is under box X. For each swap, we know the indices (i,j) of the boxes which are being swapped. We form basic conditions of form-

- Let Curr hold the index of box under which coin is initially. By the question, Curr=X initially. Now, for every swap, the following holds-

- If i\neq Curr and j \neq Curr- Do nothing. We dont care about such swaps.

- If i==Curr, then it means that box i and j are swapped, and coin was initially in box i. Now, after swapping, it will be under box at index j. Hence, we assign Curr=j.

- If j==Curr then by same reasoning we assign Curr=i.

-
i==j==Curr , we need to do nothing. (I dont think this case exists in the question XD).

The final ans is in Curr. Please note I followed standard programming convention of = representing assignment operator and == representing “Check for Equality” operator.

### EXPLANATION:

This is one of the editorial where Quick Explanation more than sums up everything about the logic. Instead of making editorial unnecessarily lengthy by formulating the logic again, lets focus on implementation.

In case there is any doubt of logic under Quick Explanation, do ask. I kept it short as it was simply common sense. **The gist of the logic is, if the coin is currently under any one of the bowls, i or j, then it will be in the other bowl with which we swapped after the operation. Keep a track of which bowl the coin is CURRENTLY in.**

Taking the input is trivial, but with that being said, let me introduce you to Fast Input-Output methods. The rule of thumb says, if number of input is >10^5 or output >10^5, use fast input-output to save precious time. Else, many times correct solutions get TLE due to huge time wasted in IO operations.

Maintain a temporary variable to store answer. I used currAns. After this, implement the conditionals mentioned above. Remember that, for cases where (i \neq currAns \&\& j \neq currAns)  and (i==currAns \&\& j==currAns) we dont need to do nothing, hence we ignore them. We only handle the remaining 2 cases. Implementation in tab below-

Click to view
``   int currAns=x;
	    int a,b;
	    while(s--)
	    {
	        cin>>a>>b;//a corresponds to i, b corresponds to j. This line takes input
	        if(a==currAns)
	            currAns=b;//if (i==currAns) currAns=j;
	        else if(b==currAns)
	            currAns=a;//Same as above.
	    }
	    cout<<currAns<<endl;//Print
``

### SOLUTION

The code is pasted in tabs below for you guys to refer in case solution links dont work.

[Setter](http://www.codechef.com/download/Solutions/SEPT18/setter/MAGICHF.cpp)

[Tester](http://www.codechef.com/download/Solutions/SEPT18/tester/MAGICHF.cpp)

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

// used for storing contents of boxes.
int arr[123456];
int main(){
    std::ios::sync_with_stdio(false);
    int t;
    cin>>t;
    while(t--){
    	int n,x,s;
    	cin>>n>>x>>s;
    	int i,a,b;
        // initialising correct box
    	arr[x]=1;
        // performing swaps
    	rep(i,s){
    		cin>>a>>b;
    		swap(arr[a],arr[b]);
    	}

        // checking for answer box!!
    	rep(i,123456){
    		if(arr[i]){
    			arr[i]=0;
    			cout<<i<<endl;
    			break;
    		}
    	}

    }
    return 0;
}
``

[Editorialist](http://www.codechef.com/download/Solutions/SEPT18/editorialist/MAGICHF.cpp)

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
	while(t--)
	{
	    int n,x,s;
	    cin>>n>>x>>s;
	    int currAns=x;
	    int a,b;
	    while(s--)
	    {
	        cin>>a>>b;
	        if(a==currAns)
	            currAns=b;
	        else if(b==currAns)
	            currAns=a;
	    }
	    cout<<currAns<<endl;
	}
	return 0;
}
``

Time Complexity=O(S) per test case

Space Complexity=O(1)

### CHEF VIJJU’S CORNER

**1.** Swapping variables here and there kind of reminds me of the [std::swap](http://www.cplusplus.com/reference/algorithm/swap/) function of C++ STL. Its a nice function which comes in handy for beginners and professionals alike. It can swap variables, arrays, vectors, queues…you pretty much get it XD.

**2.** Why did Chef bother accepting Magicians challenge if he needs us to help him? -_-

**3.** Related Problems: Frankly, the entire [beginner](https://www.codechef.com/problems/school) section is filled to brim with such level problems. Solve any random problem from there, EXCEPT

- Rupsa and Game

- Chef and Weird Game.

- One more Weird Game.

List item

</details>
