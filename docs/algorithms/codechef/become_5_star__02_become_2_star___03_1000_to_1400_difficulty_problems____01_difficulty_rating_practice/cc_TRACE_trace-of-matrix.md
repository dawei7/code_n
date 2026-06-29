# Trace of Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TRACE |
| Difficulty Rating | 1198 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [TRACE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/TRACE) |

---

## Problem Statement

Chef is learning linear algebra. Recently, he learnt that for a square matrix $M$, $\mathop{\rm trace}(M)$ is defined as the sum of all elements on the main diagonal of $M$ (an element lies on the main diagonal if its row index and column index are equal).

Now, Chef wants to solve some excercises related to this new quantity, so he wrote down a square matrix $A$ with size $N\times N$. A square *submatrix* of $A$ with size $l\times l$ is a contiguous block of $l\times l$ elements of $A$. Formally, if $B$ is a submatrix of $A$ with size $l\times l$, then there must be integers $r$ and $c$ ($1\le r, c \le N+1-l$) such that $B_{i,j} = A_{r+i-1, c+j-1}$ for each $1 \le i, j \le l$.

Help Chef find the maximum trace of a square submatrix of $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains $N$ space-separated integers $A_{i,1}, A_{i,2}, \dots, A_{i, N}$ denoting the $i$-th row of the matrix $A$.

### Output
For each test case, print a single line containing one integer — the maximum possible trace.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le A_{i,j} \le 100$ for each valid $i, j$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3
1 2 5
6 3 4
2 7 1
```

**Output**

```text
13
```

**Explanation**

**Example case 1:** The submatrix with the largest trace is
```
6 3
2 7
```
which has trace equal to $6 + 7 = 13$. (This submatrix is obtained for $r=2, c=1, l=2$.)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/LTIME60A/problems/TRACE)

[Div2](https://www.codechef.com/LTIME60B/problems/TRACE)

[Practice](https://www.codechef.com/problems/TRACE)

**Setter-** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester-** [Jakub Safin](https://www.codechef.com/users/xellos0)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

[2-D Matrix](https://www.cs.cmu.edu/~mrmiller/15-110/Handouts/arrays2D.pdf), Looping

### PROBLEM:

Given a 2-D matrix A, find the maximum trace possible for any possible sub-matrix

### QUICK EXPLANATION:

We can, of course, apply brute force to generate every possible sub-matrix and check its trace, and print the maximum trace we found.

There, also exists a linear time solution which will be prime focus of editorial.

### EXPLANATION:

This editorial will have 2 parts, the brute force (O({N}^{4})) solution of editorialist and the O({N}^{2}) solution by the setter, [@kingofnumbers](/u/kingofnumbers) .

**1. Editorialist’s approach-**

Refer to editorialist’s code for this. We will use 3 nested for-loops. The first loop will tell the row number from where our sub-matrix starts. The second loop gives the column number where the sub-matrix starts. The third loop is the length of sub-matrix.

In other words, we will iterate over every cell in the matrix, and check all possible square matrices which can be generated from that cell, and then move to next cell and so on. Every possible sub-matrix is checked, and the maximum trace found is stored in a variable. The code will loop like-

`for(i=0;i< n;i++)//Row number { 	 for(j=0;j< n;j++)//Column Number 	 { 	 for(k=0;i+k< n and j+k< n;k++)//Length of Sub-matrix 	 { 	 trace=max(trace,findTrace(i,j,k));//Check trace of every sub-matrix. Print the maximum one. 	 } 	 } }`

**2. Setter’s Approach-**

Recall that trace of a matrix is sum of all element son the main diagonal. Now, since all numbers are positive, just think how many cells do we have to *actually* check?

Note that, my solution checks all possible cells. However, we can prove that the maximum trace is obtained if we start our sub-matrix from either the topmost row or the leftmost column.  Can you try to derive/prove this mathematically? A hint will be that all elements are positive. Another hint is given in the image below

What he does is, that, he only finds trace of the 2n matrices, (my solution found trace of all {N}^{2} matrices). Checkint trace is straightforward looping, which can be seen in the reference solutions. Alternatively, you can, like setter, mathematically find which of the 2n matrix does each element belong to.  The setter starts from the top-right corner (whose trace is in mxxx[0] in his solution) and goes linearly to top-left, and from there down to bottom-left, adding values to corresponding traces, and finally printing the maximum one of them.

### SOLUTIONS:

For immediate availability of setter and tester’s solution, they are also pasted in the tabs below. This is for your reference, and you can copy code from there to wherever you are comfortable reading them. This is to prevent non-availability of solutions (which  hinders understanding of editorial) as [@admin](/u/admin) links the solutions.

[Setter](http://www.codechef.com/download/Solutions/LTIME60/setter/TRACE.cpp)

Click to view
``#include <iostream>
#include <algorithm>
#include <string>
#include <assert.h>
using namespace std;

long long readInt(long long l,long long r,char endd){
	long long x=0;
	int cnt=0;
	int fi=-1;
	bool is_neg=false;
	while(true){
		char g=getchar();
		if(g=='-'){
			assert(fi==-1);
			is_neg=true;
			continue;
		}
		if('0'<=g && g<='9'){
			x*=10;
			x+=g-'0';
			if(cnt==0){
				fi=g-'0';
			}
			cnt++;
			assert(fi!=0 || cnt==1);
			assert(fi!=0 || is_neg==false);

			assert(!(cnt>19 || ( cnt==19 && fi>1) ));
		} else if(g==endd){
			assert(cnt>0);
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
			return x;
		} else {
			assert(false);
		}
	}
}
string readString(int l,int r,char endd){
	string ret="";
	int cnt=0;
	while(true){
		char g=getchar();
		assert(g!=-1);
		if(g==endd){
			break;
		}
		cnt++;
		ret+=g;
	}
	assert(l<=cnt && cnt<=r);
	return ret;
}
long long readIntSp(long long l,long long r){
	return readInt(l,r,' ');
}
long long readIntLn(long long l,long long r){
	return readInt(l,r,'\n');
}
string readStringLn(int l,int r){
	return readString(l,r,'\n');
}
string readStringSp(int l,int r){
	return readString(l,r,' ');
}

int mxxx[1111];
int T;
int n;

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,100);
	while(T--){
		n=readIntLn(2,100);
		for(int i=0;i<2*n;i++){
			mxxx[i] = 0;
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				int h;
				if(j==n-1){
					h=readIntLn(1,100);
				} else {
					h=readIntSp(1,100);
				}
				mxxx[i-j+n-1]+= h;
			}
		}
		int sol=0;
		for(int i=0;i<2*n;i++){
			sol = max(sol,mxxx[i]);
		}
		cout<<sol<<endl;
	}
	assert(getchar()==-1);
}
``

[Tester](http://www.codechef.com/download/Solutions/LTIME60/tester/TRACE.cpp)

Click to view
``#include <bits/stdc++.h>
// iostream is too mainstream
#include <cstdio>
// bitch please
#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <iomanip>
#include <time.h>
#define dibs reserve
#define OVER9000 1234567890
#define ALL_THE(CAKE,LIE) for(auto LIE =CAKE.begin(); LIE != CAKE.end(); LIE++)
#define tisic 47
#define soclose 1e-8
#define chocolate win
// so much chocolate
#define patkan 9
#define ff first
#define ss second
#define abs(x) (((x) < 0)?-(x):(x))
#define uint unsigned int
#define dbl long double
#define pi 3.14159265358979323846
using namespace std;
// mylittledoge

using cat = long long;

#ifdef DONLINE_JUDGE
	// palindromic tree is better than splay tree!
	#define lld I64d
#endif

int main() {
	cin.sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(10);
	int T;
	cin >> T;
	for(int t = 0; t < T; t++) {
		int N;
		cin >> N;
		vector< vector<int> > A(N, vector<int>(N));
		for(int i = 0; i < N*N; i++) cin >> A[i/N][i%N];
		int maxsum = 0;
		for(int i = -N; i <= N; i++) {
			int sum = 0;
			for(int s = 0; s <= 2*N; s++) if((s+i)%2 == 0)
				if((s+i)/2 < N && s-i >= 0 && s+i >= 0 && (s-i)/2 < N)
					sum += A[(s+i)/2][(s-i)/2];
			maxsum = max(maxsum, sum);
		}
		cout << maxsum << "\n";
	}
	return 0;}

// look at my code
// my code is amazing
``

[Editorialst](http://www.codechef.com/download/Solutions/LTIME60/editorialist/TRACE.cpp)

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
int n;
int arr[110][110];

//Returns trace. Takes starting point, and length of square sub-matrix as input
int findTrace(int i,int j,int k)
{
    int trace=0,l;
    for(l=0;l<=k;l++)
    {
        trace+=arr[i+l][j+l];
    }
    return trace;
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
	int t;
	cin>>t;
	while(t--)
	{
	    //input
	    int i,j;
	    cin>>n;

	    for(int i=0;i<n;i++)
	    {
	        for(int j=0;j<n;j++)
	            cin>>arr[i][j];
	    }

	    int k,l,trace=0;
	    for(i=0;i<n;i++)
	    {
	        for(j=0;j<n;j++)
	        {
	            for(k=0;i+k<n and j+k<n;k++)
	            {
	                trace=max(trace,findTrace(i,j,k));//Check trace of every sub-matrix. Print the maximum one.
	            }
	        }
	    }
	    cout<<trace<<endl;
	}

	return 0;
}
``

### CHEF VIJJU’S CORNER

**1.** Proof of why only 2n matrices suffice-

Click to view

**The 2n matrices start from either the top-most row or the left-most column. Now, say, I start my sub-matrix from somewhere else, except these 2 locations. Lets call their trace T. Since the sub-matrix didnt start at the topmost row or the leftmost column, we can clearly say that there exists atleast one element A_{i,j} in diagonally, North-West direction. And they are all positive, so T< T+ \sum_{p=0}^{p=k} A_{i-p,j-p}. Hence, T can never be maximal. This, any sub-matrix not starting from either top-most row, or the leftmost column can never have maximal trace.**

**2.** Estimate the difficulty of problem if sub-matrix did *not* mean contiguous rows/columns? What if it meant a sub-set of rows and columns?

**3.** Estimate the difficulty if negative elements were allowed. Can we do better than O({N}^{4}) or O({N}^{3}) in that case? Note that our proof stated in point **1.** above will be invalid if elements can be negative.

**4.** - Pseudo code to calculate trace (editorialist’s solution)

Click to view
``int findTrace(int i,int j,int k)
{
    int trace=0,l;
    for(l=0;l<=k;l++)
    {
        trace+=arr[i+l][j+l];
    }
    return trace;
}
``

**5.** What lies at the end of this box?

Click to view

**Compiling…**

Click to view

**Compiling…**

Click to view

**Compiling…**

Click to view

**Compiling…**

Click to view

**Running…**

Click to view

**Running…**

Click to view

**Running…**

Click to view

**Running…**

Click to view

**Running…**

Click to view

**RE:SIGSEV**

**6.** Some problems for practicing 2-D Matrices-

- [Add Alternate Elements](https://www.hackerearth.com/practice/data-structures/arrays/multi-dimensional/practice-problems/algorithm/add-alternate-elements-of-2-dimensional-array/)

- [HourGlass Problem](https://www.hackerrank.com/challenges/2d-array/problem)

- [Spiral Array](https://www.hackerrank.com/contests/utsav/challenges/spiral-matrix/)

</details>
