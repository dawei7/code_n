# Pyramid Traversal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PYRAMIDMOVES |
| Difficulty Rating | 2194 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [PYRAMIDMOVES](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/PYRAMIDMOVES) |

---

## Problem Statement

You are given a pyramid of the following form with an infinite number of rows:
    $$1$$
   $$2\ 3$$
  $$4\ 5\  6$$
 $$7\ 8\ 9\ 10$$
$$...........$$

From a cell, you can move to either the bottom-left cell or the bottom-right cell directly in contact with the current one (For example, you can make the following moves: $1 \rightarrow 2, 1 \rightarrow 3, 6 \rightarrow 9, 6 \rightarrow 10$, while you **cannot** make moves $2\to 6$ or $2\rightarrow 7$).

You are given a starting cell $s$ and an ending cell $e$. Starting at cell $s$, find the number of ways to reach cell $e$. This number can be large, so print the answer modulo $10^9 + 7$.

Two ways are said to be different if there exists at least one cell which was visited in one of the ways but not the other one.

---

## Input Format

- The first line of input contains a single integer $T$, the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $s$ and $e$, denoting the starting and the ending cell respectively.

---

## Output Format

For each test case, output a single line containing one integer: the number of ways to go from $s$ to $e$ modulo $10^9 + 7$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq s, e\leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2 7
1 5
5 3
```

**Output**

```text
1
2
0
```

**Explanation**

In the first test case, there exists only $1$ way to move from $2$ to $7$, which is:
- $2 \rightarrow 4 \rightarrow 7$

In the second test case, there exist $2$ ways to move from $1$ to $5$, which are:
- $1 \rightarrow 2 \rightarrow 5$
- $1 \rightarrow 3 \rightarrow 5$

In the third test case, it is not possible to move from $5$ to $3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 7
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 5
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
5 3
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

[Contest Division 1](https://www.codechef.com/DEC21A/problems/PYRAMIDMOVES)

[Contest Division 2](https://www.codechef.com/DEC21B/problems/PYRAMIDMOVES)

[Contest Division 3](https://www.codechef.com/DEC21C/problems/PYRAMIDMOVES)

[Practice](https://www.codechef.com/problems/PYRAMIDMOVES)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Pascal’s Triangle

#
[](#problem-4)PROBLEM

You are given a pyramid of the following form with an infinite number of rows:

1

2\ 3

4\ 5\  6

7\ 8\ 9\ 10

...........

From a cell, you can move to either the bottom-left cell or the bottom-right cell directly in contact with the current one (For example, you can make the following moves: 1 \rightarrow 2, 1 \rightarrow 3, 6 \rightarrow 9, 6 \rightarrow 10, while you **cannot** make moves 2\to 6 or 2\rightarrow 7).

You are given a starting cell s and an ending cell e. Starting at cell s, find the number of ways to reach cell e. This number can be large, so print the answer modulo 10^9 + 7.

Two ways are said to be different if there exists at least one cell which was visited in one of the ways but not the other one.

#
[](#quick-explanation-5)QUICK EXPLANATION

- After left aligning the triangle, the first move translates to move moving down, and the second move corresponds to moving down-right cell. We need to count the number of ways to reach from cell (r_1, c_1) to (r_2, c_2).

- There would be r_2 - r_1 moves, and the number of ways would be \displaystyle ^{r_2-r_1}C_{c_2-c_1}

#
[](#explanation-6)EXPLANATION

First of all, the positions in this triangle are hard to represent. Let’s left align it.

``1
2 3
4 5 6
7 8 9 10 ...
``

Now, the effect of this translation is

- The move to the bottom-left position became moving immediately towards the bottom. For example 5 to 8.

- The move to the bottom-right position became moving to cell one step down and once step right. For example, from 5 to 9.

Hence, after this translation, each move moves you one step to the bottom, and we can choose whether to move one step to the right or not, by choosing between the first and second options.

In order to solve this, we first need to find the position in terms of rows and columns from numbering.

###
[](#find-the-row-and-column-of-the-specific-numbered-position-7)Find the row and column of the specific numbered position

If the number x is written on position (r, c), row r and column c, then we can see that x = (r-1)*r/2 + c. The numbers used up in first r-1 rows are (r-1)*r/2 and c numbers in current row.

We can find the largest r such that r*(r-1)/2 \lt x by linear or binary search. Additionally, we can prove that for x \leq 10^9, the row never exceeds 10^5.

###
[](#given-positions-computing-the-number-of-ways-8)Given positions, computing the number of ways

Assuming we have to reach position (r_2, c_2) from (r_1, c_1), we can see that each move moves us one step down, and we need to move exactly r_2-r_1 steps down, Hence the total number of moves is r_2 - r_1. In each of these moves, we can either stay in the same column or move to the next column. We have to move right c_2-c_1 times out of r_2 - r_1 times.

The problem is to choose c_2 - c_1 positions out of r_2 - r_1 positions, which can be done in ^{r_2-r_1} C _ {c_2 - c_1} ways.

The problem becomes to computing ^NC_R \bmod P. The easiest way would be to precompute factorials and their modular inverses and multiply them. Some detailed discussion on computing this can be found [here](https://discuss.codechef.com/t/best-known-algos-for-calculating-ncr-m/896/2).

#
[](#time-complexity-9)TIME COMPLEXITY

The time complexity is O(MX + T) per test case.

#
[](#solutions-10)SOLUTIONS

Setter's Solution
``#ifdef WTSH
    #include "wtsh.h"
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(Z...)
#endif

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const int N = 1e5 + 5, mod = 1e9 + 7;

int fac[N], invfac[N];

int power(int a, int b, int m)
{
    int res = 1;
    a %= m;
    while (b > 0)
    {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}

int modinv(int k)
{
    return power(k, mod-2, mod);
}

void precompute()
{
    fac[0] = fac[1] = 1;
    for(int i = 2; i < N; i++)
    {
        fac[i] = fac[i-1] * i;
        fac[i] %= mod;
    }
    invfac[N-1] = modinv(fac[N-1]);
    for(int i = N-2; i >= 0; i--)
    {
        invfac[i] = invfac[i+1] * (i+1);
        invfac[i] %= mod;
    }
}

int nCr(int n, int r)
{
    if(n < 0 or r < 0 or n < r)
        return 0;
    return (fac[n] * invfac[r] % mod) * invfac[n-r] % mod;
}

pii find_coord(int x)
{
    int lo = 0, hi = 1e5;
    while(lo <= hi)
    {
        int mid = (lo + hi) / 2;
        int done = mid * (mid + 1) / 2;
        if(done < x)
            lo = mid + 1;
        else
            hi = mid - 1;
    }
    swap(lo, hi);
    int row = hi;
    int col = x - lo * (lo + 1) / 2;
    return pii{row, col};
}

void solve()
{
    int s, e; cin >> s >> e;
    pii S = find_coord(s);
    pii E = find_coord(e);
    cout << nCr(E.first - S.first, E.second - S.second) << endl;
}

int32_t main()
{
    IOS;
    precompute();
    int T; cin >> T;
    while(T--)
    {
        solve();
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

/*
------------------------Input Checker----------------------------------
*/

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
            if(is_neg){
                x= -x;
            }

            if(!(l <= x && x <= r))
            {
                cerr << l << ' ' << r << ' ' << x << '\n';
                assert(1 == 0);
            }

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

/*
------------------------Main code starts here----------------------------------
*/

const int MAX_T = 1000;
const int MAX_N = 1e6+5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll MX=200000;
ll fac[MX], ifac[MX];

const ll mod = 1000000007;

ll po(ll x, ll n ){
    ll ans=1;
     while(n>0){
        if(n&1) ans=(ans*x)%mod;
        x=(x*x)%mod;
        n/=2;
     }
     return ans;
}

void pre(){
 fac[0]=1;
 for(int i=1; i<MX; i++) fac[i]= (i*fac[i-1])%mod;
 for(int i=0; i<MX; i++) ifac[i]= po(fac[i], mod-2);
}

ll ncr(ll n, ll r){
 if(r>n || r<0 || n<0) return 0;
 return (fac[n]*((ifac[r]*ifac[n-r])%mod))%mod;
}

pair<ll,ll> find_pos(ll z){
    ll l=0, r=100000;

    while(l<r){
        ll m = (l+r+1)>>1;
        if((m*m+m)/2 >= z) r = m-1;
        else l = m;
    }

    pair<ll,ll> ret;
    ret.first = l+1;

    z -= (l*l+l)/2;
    z -= (l+2)/2;

    if(l&1) z = 2*z-1;
    else z = z*2;

    ret.second = z;
    return ret;
}

void solve()
{
    ll s,e;
    s = readIntSp(1, 1e9);
    e = readIntLn(1, 1e9);

    pair<ll,ll> p1, p2;
    p1 = find_pos(s);
    p2 = find_pos(e);

    ll dis = abs(p1.second-p2.second);
    ll steps = p2.first-p1.first;

    if(dis>steps || (dis&1)!=(steps&1)){
        cout<<0<<"\n";
        return;
    }

    ll a = dis+(steps-dis)/2;
    ll b = steps-a;

    cout<<ncr(a+b,a)<<"\n";
    return;
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,MAX_T);
    pre();

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    //cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class PYRAMIDMOVES{
    //SOLUTION BEGIN
    int MOD = (int)1e9+7;
    long[][] fif = fif(100000);
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int s = ni(), e = ni();
        int[] p1 = pos(s), p2 = pos(e);
        int N = p2[0]-p1[0], R = p2[1]-p1[1];
        if(N < R || R < 0)pn(0);
        else pn(C(N, R));
    }
    int[] pos(int num){
        int r = 0;
        while(((r+2)*(r+1))/2 < num)r++;
        return new int[]{r+1, num-(r*(r+1))/2};
    }
    long[][] fif(int mx){
        mx++;
        long[] F = new long[mx], IF = new long[mx];
        F[0] = 1;
        for(int i = 1; i< mx; i++)F[i] = (F[i-1]*i)%MOD;
        //GFG
        long M = MOD;
        long y = 0, x = 1;
        long a = F[mx-1];
        while(a> 1){
            long q = a/M;
            long t = M;
            M = a%M;
            a = t;
            t = y;
            y = x-q*y;
            x = t;
        }
        if(x<0)x+=MOD;
        IF[mx-1] = x;
        for(int i = mx-2; i>= 0; i--)IF[i] = (IF[i+1]*(i+1))%MOD;
        return new long[][]{F, IF};
    }
    long C(int n, int r){
        if(n<r || r<0)return 0;
        return (fif[0][n]*((fif[1][r]*fif[1][n-r])%MOD))%MOD;
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
        new PYRAMIDMOVES().run();
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
