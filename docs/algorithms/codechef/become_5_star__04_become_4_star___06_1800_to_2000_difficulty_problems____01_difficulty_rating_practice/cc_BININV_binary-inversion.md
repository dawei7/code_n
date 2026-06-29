# Binary Inversion

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BININV |
| Difficulty Rating | 1865 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [BININV](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/BININV) |

---

## Problem Statement

You are given $N$ binary strings $S_1, S_2, \dots, S_N$, each of length $M$. You want to concatenate **all** the $N$ strings in some order to form a single large string of length $N \cdot M$. Find the minimum possible number of inversions the resulting string can have.

A binary string is defined as a string consisting only of '$0$' and '$1$'.

An *inversion* in a binary string $S$ is a pair of indices $(i, j)$ such that $i \lt j$ and $S_i$ = '$1$', $S_j$ = '$0$'. For example, the string $S =$ "$01010$" contains $3$ inversions : $(2, 3)$, $(2, 5),$ $(4, 5)$.

Note that you are not allowed to change the order of characters within any of the strings $S_i$ - you are only allowed to concatenate the strings themselves in whatever order you choose. For example, if you have "$00$" and "$10$" you can form "$0010$" and "$1000$", but not "$0001$".

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N, M$.
- $N$ lines follow, the $i^{th}$ of which contains the string $S_i$ of length $M$.

---

## Output Format

For each test case, print a single line containing one integer - the minimum possible number of inversions in the resulting string.

---

## Constraints

- $1 \leq T \leq 10^3$
- $2 \leq N \leq 10^5$
- $1 \leq M \leq 10^5$
- $2 \leq N \cdot M \leq 2\cdot 10^5$
- $\lvert S_i \rvert = M$
- $S_i$ contains only characters '$0$' and '$1$'.
- Sum of $N \cdot M$ over all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
2 1
0
1
3 2
10
00
01
2 4
0010
1011
3 4
1011
1101
0101
```

**Output**

```text
0
2
3
11
```

**Explanation**

**Test case $1$:** Two strings can be formed : $S_1 + S_2 = $"$01$", $S_2 + S_1 $= "$10$". The first string does not have any inversion while the second has one inversion : $(1, 2)$.

**Test case $2$:**  Both $S_2 + S_1 + S_3 = $"$001001$", $S_2 + S_3 + S_1 = $"$000110$" contain $2$ inversions. It can be verified that no other order results in fewer inversions.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START17A/problems/BININV)

[Contest Division 2](https://www.codechef.com/START17B/problems/BININV)

[Contest Division 3](https://www.codechef.com/START17C/problems/BININV)

[Practice](https://www.codechef.com/problems/BININV)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Observations.

#
[](#problem-4)PROBLEM

Given N binary strings, each of length M. Concatenate all N strings in some order in a single string T of length N*M, aiming to minimize the number of inversions in T.

#
[](#quick-explanation-5)QUICK EXPLANATION

- The optimal order would be sorting the strings in nondecreasing order of number of ones present in S

- We can first build the string and then calculate the number of inversions on the concatenated string.

#
[](#explanation-6)EXPLANATION

###
[](#solving-for-n-2-7)Solving for N = 2

Let’s say we have two strings A and B, which we need to concatenate while minimizing the number of inversions. We can try both AB and BA and pick the one with fewer inversions.

Let’s denote C_{S,c} denote the number of occurrences of character c in S and the number of inversions in S by f(S).

We can denote f(A+B) = f(A)+f(B) + C_{A, 1}*C_{B, 0} and f(B+A) = f(B)+f(A) + C_{B, 1}*C_{A, 0}

###
[](#types-of-inversions-8)Types of inversions

Let’s call inversion pair (x, y) if 1 appears at position x and 0 appears at position y and x \lt y.

We can divide inversions into two categories

-
**Inversions within the same string**

This includes inversions where both x and y lie on the same string. Irrespective of where this string is concatenated, this pair shall always exist as an inversion. We cannot change the number of inversions within a string.

-
**Inversions across strings**

When solving for N = 2, when we concatenated AB, there must be some pairs where 1 appeared in A and 0 appeared in B, forming an inversion in concatenated string. These inversions are dependent on the order of strings we choose.

Our aim is to reduce the inversions of the second type since the first type of inversion never changes with the order of strings.

###
[](#deciding-the-order-of-a-pair-of-strings-9)Deciding the order of a pair of strings.

Let’s say we have already chosen the order of strings to be concatenated, and we are only allowed to swap adjacent strings. For some i, we need to decide whether swapping S_i and S_{i+1} is beneficial or not.

**Observation:** Only the number of inversion between strings S_i and S_{i+1} is affected by this swap.

**Proof:** Considering string S_j for j \lt i, both S_i and S_{i+1} appear to the right of string S_j, so no 0 or 1 from right to left of S_j, leaving the number of inversions arising from string S_j unaffected.

Similarly, if we have string S_j where j \gt i+1, then also, S_{j+1} is to the right of both S_i and S_{i+1}. So the number of inversions arising from S_j are also unaffected by the swap.

Hence, we can decide which one of S_i or S_{i+1} should come first sorely based on the number of inversions in string S_i + S_{i+1} and string S_{i+1}+S_i.

**Observation:** In the optimal order of strings, there doesn’t exist any beneficial swap, as beneficial swap reduces the inversions, but our string is already optimal.

###
[](#choosing-the-order-of-strings-10)Choosing the order of strings

Now, for an adjacent pair, we know whether the swap would be beneficial. So we can actually simulate bubble sort since bubble sort swaps elements until the array is sorted. We can sort the strings by defining a comparator function, accepting two strings A and B, and comparing f(A) + f(B) +C_{A, 1}*C_{B, 0}  with f(A)+f(B) + C_{B, 1}*C_{A, 0} to decide which string should appear before which.

Since bubble sort is slow, we can use sort algorithms like merge sort to sort them efficiently.

###
[](#computing-the-number-of-inversions-11)Computing the number of inversions

Now that we have the computed binary string, we need to count inversions. Counting inversions in an array is a well-known problem, but for binary strings, it can be solved even faster.

Let’s say we iterate on string S from left to right. We have two variables, ans, and cnt_1, denoting the number of inversions found yet, and the number of 1.

- If the current character is 0, this position shall form an inversion pair with all occurrences of 1 before the current position.  It can be written as ans = ans + cnt_1

- If the current character is 1, the number of $1$s should be incremented. which implies cnt_1 increases.

#
[](#time-complexity-12)TIME COMPLEXITY

The time complexity is O(M*N*log(N)) per test case due to sorting.

#
[](#solutions-13)SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
void solve() {
  int n, m;
  cin >> n >> m;
  vector<string> s(n);
  vector<pair<int, int>> v;
  for (int i = 0; i < n; i++) {
    cin >> s[i];
    int ones = count(s[i].begin(), s[i].end(), '1');
    v.push_back({ones, i});
  }
  sort(v.begin(), v.end());
  string cur;
  for (int i = 0; i < n; i++) {
    for (auto u : s[v[i].second]) {
      cur.push_back(u);
    }
  }
  int ones = 0;
  long long ans = 0;
  for (int i = 0; i < n * m; i++) {
    if (cur[i] == '1') ones++;
    else ans += ones;
  }
  cout << ans << '\n';
}

signed main() {
  int t = 1;
  cin >> t;
  for (int i = 1; i <= t; i++) solve();
  return 0;
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

void assertBinaryString(const string s){
    for(auto x:s)
        assert('0'<=x&&x<='1');
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
T=readIntLn(1,1e3);
lli sumNM = 1e6;
while(T--)
{

    const lli n=readIntSp(1,min(sumNM,100000LL)),m=readIntLn(1,min(sumNM/n,100000LL));
    sumNM-=n*m;
    vector<string> a(n);
    vii values;
    for(auto &s:a){
        s=readStringLn(m,m);
        assertBinaryString(s);
        ii cnt={0,0};
        for(auto x:s){
            if(x=='0')
                cnt.X++;
            else
                cnt.Y++;
        }
        values.pb(cnt);
    }

    vi b(n);
    iota(all(b),0);
    sort(all(b),[&](const int x,const int y){
        return values[x].Y*values[y].X<values[x].X*values[y].Y;
    });
    dbg(b);
    lli ans=0,cnt1=0;
    for(auto idx:b)
        for(auto x:a[idx]){
            if(x=='1')
                cnt1++;
            else
                ans+=cnt1;
        }
    cout<<ans<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class BININV{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), M = ni();
        String[] S = new String[N];
        for(int i = 0; i< N; i++)S[i] = n();
        Arrays.sort(S, (String s1, String s2) -> {
            int[] c1 = count(s1), c2 = count(s2);
            long inv1 = c1[1]*(long)c2[0], inv2 = c1[0]*(long)c2[1];
            if(inv1 == inv2)return 0;
            if(inv1 < inv2)return -1;
            return 1;
        });
        long inv = 0, onesCount = 0;
        for(int i = 0; i< N*M; i++){
            char ch = S[i/M].charAt(i%M);
            if(ch == '0')inv += onesCount;
            else onesCount++;
        }
        pn(inv);
    }
    int[] count(String S){
        int[] c = new int[2];
        for(int i = 0; i< S.length(); i++)c[S.charAt(i)-'0']++;
        return c;
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
        new BININV().run();
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
