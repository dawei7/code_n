# New Piece

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NEWPIECE |
| Difficulty Rating | 1216 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [NEWPIECE](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/NEWPIECE) |

---

## Problem Statement

Chef's favorite game is chess. Today, he invented a new piece and wants to see its strengths.

From a cell $(X, Y)$, the new piece can move to any cell of the chessboard such that its color is different from that of $(X, Y)$.

The new piece is currently located at cell $(A, B)$. Chef wants to calculate the minimum number of steps required to move it to $(P, Q)$.

**Note:** A chessboard is an $8 \times 8$ square board, where the cell at the intersection of the $i$-th row and $j$-th column is denoted $(i, j)$. Cell $(i, j)$ is colored white if $i+j$ is even and black if $i+j$ is odd.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of the test cases follows.
- Each test case consists of a single line of input, containing four space-separated integers $A, B, P, Q$.

---

## Output Format

For each test case, output a single line containing one integer - the minimum number of moves taken by the new piece to reach $(P, Q)$ from $(A, B)$.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq A,B,P,Q \leq 8$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 8 8
5 7 5 8
3 3 3 3
```

**Output**

```text
2
1
0
```

**Explanation**

**Test Case $1$:** $(1,1)$ and $(8,8)$ have the same color, so Chef cannot move the new piece in $1$ move. Chef can first move the piece from $(1,1)$ to $(8,1)$ and then from $(8,1)$ to $(8,8)$, thus taking $2$ moves.

**Test Case $2$:** $(5,7)$ and $(5,8)$ have different colors, so Chef can move the piece from $(5,7)$ to $(5,8)$ in $1$ move.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 8 8
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5 7 5 8
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3 3 3 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START17A/problems/NEWPIECE)

[Contest Division 2](https://www.codechef.com/START17B/problems/NEWPIECE)

[Contest Division 3](https://www.codechef.com/START17C/problems/NEWPIECE)

[Practice](https://www.codechef.com/problems/NEWPIECE)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Chef’s favorite game is chess. Today, he invented a new piece and wants to see its strengths.

From a cell (X, Y), the new piece can move to any cell of the chessboard such that its color is different from that of (X, Y).

The new piece is currently located at cell (A, B). Chef wants to calculate the minimum number of steps required to move it to (P, Q).

**Note:** A chessboard is an 8 \times 8 square board, where the cell at the intersection of the i-th row and j-th column is denoted (i, j). Cell (i, j) is colored white if i+j is even and black if i+j is odd.

#
[](#quick-explanation-5)QUICK EXPLANATION

- If Chef is already at the target cell (P, Q), then 0 moves are required.

- Otherwise, if cells (A, B) and (P, Q) have different colors, then in one move, Chef can move directly from (A, B) to (P, Q).

- Otherwise, It requires the chef two moves, first to get to any opposite-colored cell, from which the chef can go to cell (P, Q)

#
[](#explanation-6)EXPLANATION

The trivial case is when Chef is already at the target position, which happens when (A, B) = (P, Q). No moves are required in this case.

Otherwise, at least one move is required. In one move, Chef can reach any cell with a color different from the color of cell (A, B). So if (P, Q) has a different color from cell (A, B), then Chef can reach the target in his first move.

Lastly, if the cell (P, Q) is of the same color as cell (A, B), the chef can in the first move, move to any cell with different color, from where the chef can move to (P, Q)

The following snippet covers the model solution.

``read A, B, P, Q
if A == P and B == Q: print(0)
else if (A+B)%2 != (P+Q)%2: print(1)
else print(2)
``

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#include <chrono>
#include <random>
#define ll long long int
#define ull unsigned long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define rep(i,n) for(ll i=0;i<n;i++)
#define loop(i,a,b) for(ll i=a;i<=b;i++)
#define vi vector <int>
#define vs vector <string>
#define vc vector <char>
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
#define max3(a,b,c) max(max(a,b),c)
#define min3(a,b,c) min(min(a,b),c)
#define deb(x) cerr<<#x<<' '<<'='<<' '<<x<<'\n'
using namespace std;
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(val)  no. of elements strictly less than val
// s.find_by_order(i)  itertor to ith element (0 indexed)
typedef vector<vector<ll>> matrix;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
void solve()
{
    ll a,b,p,q;
    cin>>a>>b>>p>>q;
    if(a==p && b==q)
    {
        cout<<0<<'\n';
        return;
    }
    if(((a+b)%2)!=((p+q)%2))
    {
        cout<<1<<'\n';
    }
    else
        cout<<2<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int T=1;
    cin>>T;
    int t=0;
    while(t++<T)
    {
        //cout<<"Case #"<<t<<":"<<' ';
        solve();
        //cout<<'\n';
    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution
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

vi readVectorInt(int n,lli l,lli r){
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

int main(void) {
    ios_base::sync_with_stdio(false);cin.tie(NULL);
    // freopen("txt.in", "r", stdin);
    // freopen("txt.out", "w", stdout);
// cout<<std::fixed<<std::setprecision(35);
T=readIntLn(1,5000);
while(T--)
{
    const int a=readIntSp(1,8),b=readIntSp(1,8),x=readIntSp(1,8),y=readIntLn(1,8);
    if(a==x&&b==y){
        cout<<0<<endl;
        continue;
    }
    if((a+b+x+y)&1){
        cout<<1<<endl;
        continue;
    }
    cout<<2<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class NEWPIECE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int A = ni(), B = ni(), P = ni(), Q = ni();
        if(A == P && B == Q)pn(0);
        else if((A+B)%2 != (P+Q)%2)pn(1);
        else pn(2);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
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
        new NEWPIECE().run();
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
