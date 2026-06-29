# Ada King

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ADAKNG |
| Difficulty Rating | 1581 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Basic Graph Theory - Trees, DFS, BFS |
| Official Link | [ADAKNG](https://www.codechef.com/practice/course/3to4stars/LP3TO401/problems/ADAKNG) |

---

## Problem Statement

Chef Ada is training to defend her title of World Chess Champion.

To train her calculation skills, Ada placed a [king] on a chessboard. Remember that a chessboard has $8$ rows and $8$ columns (for the purposes of this problem, both the rows and the columns are numbered $1$ through $8$); let's denote the square in row $r$ and column $c$ by $(r, c)$. A king on a square $(r, c)$ can move to another square $(r', c')$ if and only if $(r'-r)^2+(c'-c)^2 \le 2$.

Ada placed her king on the square $(R, C)$. Now, she is counting the number of squares that can be visited (reached) by the king in at most $K$ moves. Help Ada verify her answers.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $R$, $C$ and $K$.

### Output
For each test case, print a single line containing one integer — the number of squares the king can visit.

### Constraints
- $1 \le T \le 512$
- $1 \le R, C, K \le 8$

---

## Examples

**Example 1**

**Input**

```text
1
1 3 1
```

**Output**

```text
6
```

**Explanation**

**Example case 1:** The king can stay on its original square or move to one of the squares circled in the following figure.

![](https://codechef_shared.s3.amazonaws.com/download/Images/CK102TST/ADAKNG/ADAKNG.png)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/COOK102A/problems/ADAKNG)

[Div2](https://www.codechef.com/COOK102B/problems/ADAKNG)

[Practice](https://www.codechef.com/problems/ADAKNG)

**Setter-**  [Alei Reyes](https://www.codechef.com/users/alei)

**Tester-**  [Pranjal Jain](https://www.codechef.com/users/praran26)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

Cakewalk

### PRE-REQUISITES:

[Basic Looping](https://www.tutorialspoint.com/cplusplus/cpp_loop_types.htm), 2-D [arrays](https://www.geeksforgeeks.org/multidimensional-arrays-c-cpp/), [Conditionals](https://www.tutorialspoint.com/cplusplus/cpp_if_else_statement.htm), [Greedy](https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/tutorial/)

### PROBLEM:

A king is placed at cell (r,c) - r being the row and c being the column number. How many cells can it visit in **at most** K moves?

### QUICK-EXPLANATION:

**Key to AC-** Realize **either** of the 3 things below-

- Lets say we want to go at a cell at distance (k_1,k_2). The optimal strategy is going diagonally until either k_1 or k_2 becomes 0, and then moving  horizontally or vertically (as we reached the same row/column now) until the cell is reached. Number of moves traversed are max(k_1,k_2) .

- This question is a standard BFS on matrix question.

- The possible cells king can visit will form a square (or rectangle, depending on where he is placed). The area of this figure is the answer.

The quickest and most intuitive way to solve the problem is to realize that to go to a cell at distance of (k_1,k_2) from our starting cell, we need max(k_1,k_2) moves, for example, to visit cell (X,Y) we get k_1=|X-r| and k_2=|Y-c|. If the max of these if \leq K, we can visit this cell. Check this for every cell and print the answer.

### EXPLANATION:

Most of the interesting stuff is there in quick explanation itself. We will simply expand some of the points, see the reasoning of why they occur and derive intuitions to solve such problems in the main explanation. However, the quick explanation section itself is self sufficient :).

**1. A cell (X,Y) can be visited if max(|X-r|,|Y-c|) \leq K**

Lets say that the cell we’re checking is (X,Y). Let the distance of this cell from (r,c) be defined as earlier, (k_1,k_2). What happens when you move diagonally? You subtract 1 from **both** k_1 and k_2. Had you moved horizontally, only one of them would have reduced, but because we moved diagonally, we came **closer** to the cell than we would have come by moving horizontally or vertically.

It is intuitive to see that, Greedy will hold. (Formally, it will hold true because there is no way we can come to a cell in lesser moves by visiting more cells). Hence, we move diagonally as long as we can. Without loss of generality, lets say k_1 > k_2. After moving diagonally for k_2 moves, the distance left to cover is now (k_1-k_2,0).

Hence, total moves taken = \underbrace{k_2}_ \text{Diagonally} + \underbrace{(k_1-k_2)} _ \text{Horizontally/Vertically}=k_1 where k_1 was maximum of the two.

As an exercise - Repeat this proof taking k_2 as maximum and come to the same result.

**2. Standard BFS on Matrix -**

Who cares for observation when you can write a quick, bugless code for this algorithm within seconds? Well…technically you should care for observations because they make work quicker.

Anyways, theres nothing to tell here in this section, the exact standard algorithm is used. The reason I listed this out here is, because we all want some trivial problems on the algorithm after newly learning it. Mark this question as a good question for practice after learning this algorithm, even if it does seem like an overkill right now. The reason is, if you get a WA or RE in this question, then the fault will be in your BFS part - because thats the only part in this question. You’d hence save some time debugging while you discover an optimal way to implement the algo

**3. Cells that king can visit will form a square/rectangle-**

**Setter’s solution uses this**

Say king is at middle of the chessboard. Refer to image below and observe the pattern-

-
k=0- Only the cell he is lying on is visited.

-
k=1- He can visit all cells immediately next to him. This is the yellow square in the picture Seems trivial till now?

-
k=2- He can visit all cells on yellow square in 1 move. We can see from picture that, he can visit all cells of orange square, from yellow square, in additional 1 move. Hence, he can visit the cells in orange square in 2 moves.

What about k=3? We can do a similar reasoning that, with 1 more move we can visit all cells of green square from orange square.

From the picture, can we derive some formula for the length of this square? Yes!!

The king, in k moves, can visit cells with column number from [r-k,r+k] and row numbers between [c-k,c+k]. However, we also need to check that he does not fall off the board while doing so! (Eg- what if r=1 and k=5?). We see that, on adding the condition of not falling off the board, some rows/columns get removed from square and it becomes a rectangle.

Hence, our expression becomes-

dx=min(c+k,8)-max(c-k,1)+1 and dy=min(r+k,8)-max(r-k,1)+1 where dx and dy are length of horizontal and vertical sides of rectangle. The +1 in the formula is to account for the row/column the king is standing it.

The area, i.e. dx*dy is the answer.

### SOLUTION

[Setter](http://campus.codechef.com/CK102TST/viewsolution/22518499/) - Used approach 3.

Click to view
``#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
int rint(char nxt){
  char ch=getchar();
  int v=0;
  int sgn=1;
  if(ch=='-')sgn=-1;
  else{
    assert('0'<=ch&&ch<='9');
    v=ch-'0';
  }
  while(true){
    ch=getchar();
    if('0'<=ch && ch<='9')v=v*10+ch-'0';
    else{
      assert(ch==nxt);
      break;
    }
  }
  return v*sgn;
}
int main(){
//  freopen("secret/0.in","r",stdin);
//  freopen("secret/0.out","w",stdout);
  int t=rint('\n');
  assert(1<=t&&t<=512);
  while(t--){
    int r=rint(' ');
    assert(1<=r&&r<=8);
    int c=rint(' ');
    assert(1<=c&&c<=8);
    int k=rint('\n');
    assert(1<=k&&k<=8);
    int dx=min(c+k,8)-max(c-k,1)+1;
    int dy=min(r+k,8)-max(r-k,1)+1;
    cout<<dx*dy<<endl;
  }
  assert(getchar()==EOF);
  return 0;
}
``

[Tester](http://campus.codechef.com/CK102TST/viewsolution/22511054/) - Used approach 1.

Click to view
``#ifndef _GLIBCXX_NO_ASSERT
#include <cassert>
#endif
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif

#define ll          long long
#define pb          push_back
#define mp          make_pair
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define sz(x)       (int)x.size()
#define hell        1000000007
#define endl        '\n'
#define rep(i,a,b)  for(int i=a;i<b;i++)
using namespace std;

string to_string(string s) {
	return '"' + s + '"';
}

string to_string(const char* s) {
	return to_string((string) s);
}

string to_string(bool b) {
	return (b ? "true" : "false");
}

string to_string(char ch) {
	return string("'")+ch+string("'");
}

template <typename A, typename B>
string to_string(pair<A, B> p) {
	return "(" + to_string(p.first) + ", " + to_string(p.second) + ")";
}

template <class InputIterator>
string to_string (InputIterator first, InputIterator last) {
  bool start = true;
  string res = "{";
  while (first!=last) {
  	if (!start) {
  		res += ", ";
  	}
  	start = false;
  	res += to_string(*first);
    ++first;
  }
  res += "}";
  return res;
}

template <typename A>
string to_string(A v) {
	bool first = true;
	string res = "{";
	for (const auto &x : v) {
		if (!first) {
			res += ", ";
		}
		first = false;
		res += to_string(x);
	}
	res += "}";
	return res;
}

void debug_out() { cerr << endl; }

template <typename Head, typename... Tail>
void debug_out(Head H, Tail... T) {
	cerr << " " << to_string(H);
	debug_out(T...);
}

template <typename A, typename B>
istream& operator>>(istream& input,pair<A,B>& x){
	input>>x.F>>x.S;
	return input;
}

template <typename A>
istream& operator>>(istream& input,vector<A>& x){
	for(auto& i:x)
		input>>i;
	return input;
}

#ifdef PRINTERS
#define debug(...) cerr << "[" << #__VA_ARGS__ << "]:", debug_out(__VA_ARGS__)
#else
#define debug(...) 42
#endif

void solve(){
	int r,c,k;
	cin>>r>>c>>k;
	int ans=0;
	for(int i=1;i<=8;i++){
		for(int j=1;j<=8;j++){
			if(max(abs(i-r),abs(j-c))<=k)ans++;
		}
	}
	cout<<ans<<endl;
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int t=1;
	cin>>t;
	assert(1<=t and t<=512);
	while(t--){
		solve();
	}
	return 0;
}
``

[Editorialist](http://campus.codechef.com/CK102TST/viewsolution/22514059/) - Used BFS

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
struct cell{
    int r,c,k;
};
int dx[]={1,1,1,0,0,-1,-1,-1};
int dy[]={1,0,-1,1,-1,1,0,-1};

bool check(int r,int c)
{
    return 1<=r and r<=8 and 1<=c and c<=8;
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
	mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
	int t;
	cin>>t;
	while(t--)
	{
	    int r,c,k;
	    int visited[10][15];
	    memset(visited,-1,sizeof(visited));
	    cin>>r>>c>>k;
	    queue<cell>q;
	    cell temp1,temp2;
	    temp1.r=r;
	    temp1.c=c;
	    temp1.k=k;
	    q.push(temp1);
	    while(!q.empty())
	    {
	        temp1=q.front();
	        q.pop();
	        if(visited[temp1.r][temp1.c]>temp1.k)continue;
	        visited[temp1.r][temp1.c]=temp1.k;
	        for(int i=0;i<8;i++)
	        {
	            int r=temp1.r+dx[i];
	            int c=temp1.c+dy[i];
	            if(check(r,c) and visited[r][c]<=temp1.k-1)
	            {

	                temp2.r=r;
	                temp2.c=c;
	                temp2.k=temp1.k-1;

	                if(temp2.k>=0)
	                    q.push(temp2);
	            }
	        }
	    }
	    int ct=0;
	    for(int i=1;i<=8;i++)
	    {
	        for(int j=1;j<=8;j++)
	        {
	            if(visited[i][j]>=0)
	            {
	                ++ct;
	            }
	            //cout<<visited[i][j]<<" ";
	        }
	        //cout<<endl;
	    }
	    cout<<ct<<endl;
	}
	return 0;
}
``

Time Complexity=O(1) **for Setter -O(N*N) for tester and editorialist where $N=$length of board**

Space Complexity=O(1) **for setter and tester -O(N*N) for editorialist**

### CHEF VIJJU’S CORNER

**1.**Analyze how the question would be different if we replaced king with other chess pieces, say queen, rook, knight etc.

**2.**Give an algorithm to solve the modified version of the problem-

Instead of 8 \times 8, the chessboard is of **infinite** size. You need to tell how many cells can be visited within K moves (1 \leq K \leq 10^9) if the piece we have is a-

- King

- Queen

- Rook

- Queen (If one of the dimension is finite)

- Rook (If one of the dimension is finite)

- Bishop (If one of the dimensions is finite)

Last three are difficult (in fact, you can find a question on the bishop case already). Just try to analyze for the king part and give your answer.

**3.Related Problems-**

- [Little Elephant and Chess](https://codeforces.com/problemset/problem/259/A)

- [Anton And Chess](https://codeforces.com/problemset/problem/734/D)

</details>
