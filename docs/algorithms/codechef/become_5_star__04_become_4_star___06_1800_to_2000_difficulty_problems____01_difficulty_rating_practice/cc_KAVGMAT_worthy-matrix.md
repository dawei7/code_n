# Worthy Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KAVGMAT |
| Difficulty Rating | 1817 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [KAVGMAT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/KAVGMAT) |

---

## Problem Statement

Chef found a matrix $A$ with $N$ rows (numbered $1$ through $N$) and $M$ columns (numbered $1$ through $M$), where for each row $r$ and column $c$, the cell in row $r$ and column $c$ (denoted by $(r,c)$) contains an integer $A_{r,c}$.

This matrix has two interesting properties:
- The integers in each row form a non-decreasing sequence, i.e. for each valid $i$, $A_{i,1} \leq A_{i,2} \leq \ldots \leq A_{i,M}$.
- The integers in each column also form a non-decreasing sequence, i.e. for each valid $j$, $A_{1,j} \leq A_{2,j} \leq \ldots \leq A_{N,j}$.

A $K$-worthy [submatrix](https://mathworld.wolfram.com/Submatrix.html) is a square submatrix of $A$, i.e. a submatrix with $l$ rows and $l$ columns, for any integer $l$, such that the average of all the integers in this submatrix is $\geq K$.

Chef wants you to find the number of $K$-worthy submatrices of $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three space-separated integers $N$, $M$ and $K$.
- $N$ lines follow. For each valid $i$, the $i$-th of these lines contains $M$ space-separated integers $A_{i,1}, A_{i,2}, A_{i,3}, \ldots, A_{i,M}$.

### Output
For each test case, print a single line containing one integer ― the number of $K$-worthy submatrices of $A$.

### Constraints
- $1 \leq T \leq 10$
- $1 \leq N \cdot M \leq 10^6$
- $N \leq M$
- $0 \leq K \leq 10^9$
- $0 \leq A_{r,c} \leq 10^9$ for each valid $r,c$
- the sum of $N \cdot M$ over all test cases does not exceed $10^6$

### Subtasks
**Subtask #1 (15 points):** the sum of $N \cdot M$ over all test cases does not exceed $10^3$

**Subtask #2 (25 points):** the sum of $N \cdot M$ over all test cases does not exceed $4 \cdot 10^5$

**Subtask #3 (60 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
3 3 4
2 2 3
3 4 5
4 5 5
```

**Output**

```text
7
```

**Explanation**

**Example case 1:** The following are the seven $4$-worthy submatrices:
- $
\begin{bmatrix}
3 & 4 \\
4 & 5 \\
\end{bmatrix}
$
with average $4$; this matrix occurs only once
- $
\begin{bmatrix}
4 & 5 \\
5 & 5 \\
\end{bmatrix}
$
with average $4.75$; this matrix also occurs only once
- $
\begin{bmatrix}
4 \\
\end{bmatrix}
$
with average $4$; we find this matrix twice in $A$
- $
\begin{bmatrix}
5 \\
\end{bmatrix}
$
with average $5$; we find this matrix $3$ times in $A$

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KAVGMAT)

[Div-2 Contest](https://www.codechef.com/APRIL21B/problems/KAVGMAT)

[Div-1 Contest](https://www.codechef.com/APRIL21A/problems/KAVGMAT)

*Author:* [Sayantan Jana](https://www.codechef.com/users/shaanknight)

*Tester:* [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

*Editorialist:* [Sayantan Jana](https://www.codechef.com/users/shaanknight)

# DIFFICULTY:

Easy

# PREREQUISITES:

Binary Search, 2 pointers technique

# PROBLEM:

Given an integer K and a matrix A of dimensions N*M with integer elements, such that the elements are non decreasing along the row as well as column, find the number of square [submatrices](https://mathworld.wolfram.com/Submatrix.html) such the average of the elements in the square submatrix is \geq K.

# QUICK EXPLANATION:

- For each cell (x,y) as the top left corner, we try to find the square submatrix with minimum length, such that average of the elements in the matrix is \geq K, i.e., we find minimum l such that f(x,y,l) = \frac{\sum_{i=x}^{i=x+l-1} \sum_{j=y}^{j=y+l-1} A_{i,j}}{l*l} \geq K. So if we get minimum l such that  f(x,y,l) \geq K, we can count number of square submatrices with top left corner at (x,y) and average \geq K .

-
f(x,y,l) can be computed in O(1) using prefix sum.

- Now there are 2 approaches to solve this problem.

-
\textbf{Binary Search : } We find that the function f(x,y,l) increases with increase in l. So for each cell (x,y), we binary search for l and find the count number of square submatrices with top left corner at (x,y) and average \geq K .

-
\textbf{2 pointers technique : } We also find that the function f(x,y,l) increases with increase in y. So fixing x, we find the minimum l_j for each (x,j), 1 \leq j \leq M such that f(x,j,l_j) \geq K in O(N+M) using 2 pointers technique.

# EXPLANATION:

Notice that a square submatrix can be described by 3 variables, (x,y,l), (x,y) being the coordinates of the top left corner and l being the length of the square submatrix, i.e., the other 3 corners are (x+l-1,y), (x,y+l-1) and (x+l-1,y+l-1).

Similarly a general submatrix can be described by 4 variables, (x,y,l,r), (x,y) being the coordinates of the top left corner and l*r being the dimensions of the submatrix.

Let us define 2 terms :

-
f(x,y,l) such that 1 \leq x \leq N, 1 \leq y \leq M, 1 \leq l \leq min(N-x+1,M-y+1) : average of the square submatrix with top left corner at (x,y) and length l. Similarly we can define f(x,y,l,r).

-
r(x,y) : minimum length such that the square submatrix with top left corner at (x,y) has average \geq K, i.e., minimum l such that f(x,y,k) \geq K.

**Monotonicity of f(x,y,l)**

Consider the following submatrices :

-
(x,y,l,l) : l*l submatrix with top left corner at (x,y).

-
(x,y+l,l,1) : l*1 submatrix with top left corner at (x,y+l).

-
(x+l,y,1,l) : 1*l submatrix with top left corner at (x+l,y).

Since the elements are increasing along the row, f(x,y+l,l,1) \geq f(x,y,l,l).

SInce the elements are increasing along the column,  f(x+l,y,1,l) \geq f(x,y,l,l).

Also notice that the maximum of all the elements in the square submatrix (x,y,l) can be at most A_{x+l,y+l}. Hence we show that f(x,y,l+1) = \frac{l*l*f(x,y,l) + l*f(x+l,y,1,l) + l*f(x,y+l,l,1) + A_{x+l,y+l}}{(l+l)*(l+1)} \geq f(x,y,l).

We show that f(x,y,l) increases with increase in l. Similarly we can show that f(x,y,l) increase with increase in x as well as with increase in y, even independently.

**O(N^2 M) solution**

If we find prefix sums for the matrix A such that P_{i,j} tells the sum of elements in the submatrix (1,1,i-1,j-1), we can find f(x,y,l) in O(1) using matrix P.

So, fixing a cell as the top left corner, we want to count number of square submatrices with average \geq K . If we find r(x,y), the number of required submatrices would be min(N-(x+r(x,y)-1)+1,M-(y+r(x,y)-1)+1). We can find r(x,y) by iterating over 1 \leq l \leq min(N-x+1,M-y+1).

**O(N M log(min(N,M)) solution**

Instead of iterating over 1 \leq l \leq min(N-x+1,M-y+1), we can binary search on the length of submatrix, l, as we have shown before f(x,y,l) is increasing (not necessarily strictly though) over l.

**O(N M) solution**

As we have already talked about the monotonicity of f(), we can also find that r(x,y) is decreasing  (not necessarily strictly) over y, i.e., r(x,y) \geq r(x,y+1).

Thus instead of fixing (x,y), if we just fix x, we can use 2 pointers technique to solve the problem. We solve as follows :

- We fix x and find r(x,1), we can either use binary search for the same or simply iterate on l, i.e., we keep left pointer at 1 and move the right pointer to get r(x,1).

- Now as we know r(x,1) \geq r(x,2), we move the left pointer by 1 and the right pointer by 1 stepwise as long as the submatrix has average \geq K to get r(x,2).

- Likewise step 2, we keep on moving the left pointer exactly by 1 as we increase y and have a gradual drop of the right pointer for getting corresponding r(x,y).

Fixing the row number x, we hence find r(x,y) for the entire row in O(N+M). Once we know r(x,y) for a cell, we have already discussed how to count number of square submatrices with average \geq K .

Note that in the above solution, left pointer denotes moving on y and right pointer on l, it isn’t necessary that the value of left pointer is always lesser than the value of right pointer.

# SOLUTIONS:

Setter's Solution - 2 pointer solution
``#include<bits/stdc++.h>
using namespace std;

const int M = (1<<20)+5;
const int md = 1e9+7;

vector<int> mat[M];
vector<long long> prefix_sum[M];

int get_avg(int i,int j,int x,int y)
{
	if(x<i || y<j) return -1;
	return (prefix_sum[x][y]-prefix_sum[x][j-1]-prefix_sum[i-1][y]+prefix_sum[i-1][j-1])/(1ll*(x-i+1)*(y-j+1));
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int testcases;
	cin >> testcases;
	while(testcases--)
	{
		int n,m,k;
		cin >> n >> m >> k;
		long long ans = 0;
		for(int i=1;i<=n;++i)
		{
			mat[i].clear();
			mat[i].push_back(0);
			prefix_sum[i].clear();
			prefix_sum[i].push_back(0);
		}
		mat[0].resize(m+1,0);
		prefix_sum[0].resize(m+1,0);
		for(int i=1;i<=n;++i)
		{
			for(int j=1;j<=m;++j)
			{
				int t;
				cin >> t;
				mat[i].push_back(t);
				prefix_sum[i].push_back(prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + mat[i][j]);
			}
		}
		for(int i=1;i<=n;++i)
		{
			int j;
			for(j=1;j<=m && i+j-1<=n;++j)
				if(get_avg(i,1,i+j-1,j)>=k)
					break;
			int b = j;
			if(b<=m && i+b-1<=n)
				ans += min(m-b+1,n-i-b+2);
			if(b>m)
				b--;
			for(j=2;j<=m;++j)
			{
				while(1)
				{
					if(get_avg(i,j,i+b-j,b)>=k)
						b--;
					else
					{
						b++;
						break;
					}
				}
				if(b<=m && i+b-j<=n)
					ans += min(m-b+1,n-i-b+j+1);
				if(b>m)
					b--;
			}
		}
		cout << ans << "\n";
	}
}
``

Tester's Solution - Binary Search Solution
``/* in the name of Anton */

/*
  Compete against Yourself.
  Author - Aryan (@aryanc403)
  Atcoder library - https://atcoder.github.io/ac-library/production/document_en/
*/

#ifdef ARYANC403
    #include <header.h>
#else
    #pragma GCC optimize ("Ofast")
    #pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
    //#pragma GCC optimize ("-ffloat-store")
    #include<bits/stdc++.h>
    #define dbg(args...) 42;
#endif

using namespace std;
#define fo(i,n)   for(i=0;i<(n);++i)
#define repA(i,j,n)   for(i=(j);i<=(n);++i)
#define repD(i,j,n)   for(i=(j);i>=(n);--i)
#define all(x) begin(x), end(x)
#define sz(x) ((lli)(x).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define endl "\n"

typedef long long int lli;
typedef long double mytype;
typedef pair<lli,lli> ii;
typedef vector<ii> vii;
typedef vector<lli> vi;

const auto start_time = std::chrono::high_resolution_clock::now();
void aryanc403()
{
#ifdef ARYANC403
auto end_time = std::chrono::high_resolution_clock::now();
std::chrono::duration<double> diff = end_time-start_time;
    cerr<<"Time Taken : "<<diff.count()<<"\n";
#endif
}

long long readInt(long long l, long long r, char endd) {
    long long x=0;
    int cnt=0;
    int fi=-1;
    bool is_neg=false;
    while(true) {
        char g=getchar();
        if(g=='-') {
            assert(fi==-1);
            is_neg=true;
            continue;
        }
        if('0'<=g&&g<='9') {
            x*=10;
            x+=g-'0';
            if(cnt==0) {
                fi=g-'0';
            }
            cnt++;
            assert(fi!=0 || cnt==1);
            assert(fi!=0 || is_neg==false);

            assert(!(cnt>19 || ( cnt==19 && fi>1) ));
        } else if(g==endd) {
            if(is_neg) {
                x=-x;
            }
            assert(l<=x&&x<=r);
            return x;
        } else {
            assert(false);
        }
    }
}
string readString(int l, int r, char endd) {
    string ret="";
    int cnt=0;
    while(true) {
        char g=getchar();
        assert(g!=-1);
        if(g==endd) {
            break;
        }
        cnt++;
        ret+=g;
    }
    assert(l<=cnt&&cnt<=r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l,r,' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l,r,'\n');
}
string readStringLn(int l, int r) {
    return readString(l,r,'\n');
}
string readStringSp(int l, int r) {
    return readString(l,r,' ');
}

void readEOF(){
    assert(getchar()==EOF);
}

vi readVectorInt(lli l,lli r,int n){
    vi a(n);
    for(int i=0;i<n-1;++i)
        a[i]=readIntSp(l,r);
    a[n-1]=readIntLn(l,r);
    return a;
}

const lli INF = 0xFFFFFFFFFFFFFFFL;

lli seed;
mt19937 rng(seed=chrono::steady_clock::now().time_since_epoch().count());
inline lli rnd(lli l=0,lli r=INF)
{return uniform_int_distribution<lli>(l,r)(rng);}

class CMP
{public:
bool operator()(ii a , ii b) //For min priority_queue .
{    return ! ( a.X < b.X || ( a.X==b.X && a.Y <= b.Y ));   }};

void add( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt==m.end())         m.insert({x,cnt});
    else                    jt->Y+=cnt;
}

void del( map<lli,lli> &m, lli x,lli cnt=1)
{
    auto jt=m.find(x);
    if(jt->Y<=cnt)            m.erase(jt);
    else                      jt->Y-=cnt;
}

bool cmp(const ii &a,const ii &b)
{
    return a.X<b.X||(a.X==b.X&&a.Y<b.Y);
}

const lli mod = 1000000007L;
// const lli maxN = 1000000007L;

    lli T,n,i,j,k,in,cnt,l,r,u,v,x,y;
    lli m;
    string s;
    vi a;
    //priority_queue < ii , vector < ii > , CMP > pq;// min priority_queue .

void checkIfStrictlyIncreasing(const vector<vi> &a)
{
    const int n=sz(a),m=sz(a[0]);
    for(int i=0;i+1<n;++i)
    for(int j=0;j<m;++j)
        assert(a[i][j]<=a[i+1][j]);
    for(int i=0;i<n;++i)
    for(int j=0;j+1<m;++j)
        assert(a[i][j]<=a[i][j+1]);
}

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
lli nmsum=1e6;
T=readIntLn(1,10);
while(T--)
{
    n=readIntSp(1,1e6);
    m=readIntSp(1,1e6);
    k=readIntLn(1,1e9);
    nmsum-=n*m;
    assert(nmsum>=0);
    vector<vi> a(n);
    for(auto &v:a)
        v=readVectorInt(0,1e9,m);
    checkIfStrictlyIncreasing(a);

    vector<vi> b(n+1,vi(m+1));
    fo(i,n) fo(j,m)     b[i+1][j+1]=a[i][j]-k;

    repA(i,1,n)     repA(j,1,m)     b[i][j]+=b[i-1][j]+b[i][j-1]-b[i-1][j-1];
    auto check=[&](lli r,lli c,lli len){
        return b[r+len][c+len]+b[r][c]-b[r][c+len]-b[r+len][c]>=0;
    };
    lli ans=0;
    for(int r=0;r<n;++r)
    for(int c=0;c<m;++c)
    {
        const lli MX=min(n-r,m-c);
        lli L=0,R=MX+1;
        while(R-L>1)
        {
            lli M=(L+R)/2;
            if(check(r,c,M))
                R=M;
            else
                L=M;
        }
        // dbg(r,c,MX,L,R);
        ans+=MX-L;
    }
    cout<<ans<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

</details>
