# Partition It

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PARPERM |
| Difficulty Rating | 2202 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [PARPERM](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/PARPERM) |

---

## Problem Statement

Chef has the $N$ numbers $1, 2, 3, \dots, N$. He wants to give exactly $K$ of these numbers to his friend and keep the rest with him.

He can choose any $K$ numbers such that the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of any number from Chef's set and any number from his friend's set is equal to $1$.

Formally, suppose Chef gives the set of numbers $A$ to his friend and keeps $B$ with himself (where $|A| = K$ and $|B| = N - K$). Then $A$ and $B$ must satisfy

$$
\gcd(a, b) = 1 \ \ \forall a\in A, b\in B
$$

Chef needs your help in choosing these $K$ numbers. Please find any valid set of $K$ numbers that will satisfy the condition, or tell him that no such set exists.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $K$.

---

## Output Format

For each test case first output a single line containing "YES" (without quotes) if a set of size $K$ satisfying Chef's condition exists; and "NO" if no such set exists. This line is not case-sensitive so "YeS", "nO", etc. are also acceptable.

Next, if the answer is "YES", print another line containing $K$ distinct space-separated integers from $1$ to $N$ denoting the numbers which Chef will give to his friend. The integers can be printed in any order.

If there are multiple solutions, you may print any of them.

---

## Constraints

- $1 \leq T \leq 10^4$
- $2 \leq N \leq 10^5$
- $1 \leq K \leq N - 1$
- Sum of $N$ over all test cases does not exceed $5*10^5$

---

## Examples

**Example 1**

**Input**

```text
3
4 1
4 2
6 3
```

**Output**

```text
Yes
3
Yes
4 2
No
```

**Explanation**

**Test case $1$:** Chef can give $[3]$ to his friend and keep $[1, 2, 4]$ for himself. $3$ is coprime with $1, 2$ and $4$ so the condition is satisfied. Another possible solution is Chef giving $[1]$ to his friend.

**Test case $2$:** Chef can give $[2, 4]$ and keep $[1, 3]$ (or vice versa). It can be seen that $\gcd(2, 1) = 1$, $\gcd(2, 3) = 1$, $\gcd(4, 1) = 1$, $\gcd(4, 3) = 1$ and so the condition is satisfied.

**Test case $3$:** There is no set of 3 numbers that can satisfy the given condition.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START17A/problems/PARPERM)

[Contest Division 2](https://www.codechef.com/START17B/problems/PARPERM)

[Contest Division 3](https://www.codechef.com/START17C/problems/PARPERM)

[Practice](https://www.codechef.com/problems/PARPERM)

**Setter:** [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Tester:** [Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

[Sieve of Eratosthenes](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

#
[](#problem-4)PROBLEM

Chef has the N numbers 1, 2, 3, \dots, N. He wants to give exactly K of these numbers to his friend and keep the rest with him.

He can choose any K numbers such that the [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) of any number from Chef’s set and any number from his friend’s set is equal to 1.

Formally, suppose Chef gives the set of numbers A to his friend and keeps B with himself (where |A| = K and |B| = N - K). Then A and B must satisfy

\gcd(a, b) = 1 \ \ \forall a\in A, b\in B

Chef needs your help in choosing these K numbers. Please find any valid set of K numbers that will satisfy the condition, or tell him that no such set exists.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Consider a set A containing an integer 1 and all prime numbers strictly greater than N/2. Let’s assume the size of this set is C.

- The rest of the elements must be in one set B only. So if both K and N-K are \lt N-C, there’s no possible way to divide.

- Otherwise, we can keep adding elements from set A to B until one of them is of size K. We can print the set with size K.

#
[](#explanation-6)EXPLANATION

###
[](#graph-formulation-7)Graph formulation

There shouldn’t exist any pair (a, b) such that gcd(a, b) \gt 1, a \in A, b \in B. Let’s consider a graph where for every pair (a, b), an edge is present if and only if gcd(a, b) \gt 1.

We cannot put any two vertices from the same connected component to the different sets.

For example, for N = 6, we have edges (2, 4), (2, 6), (4, 6), (3, 6). This way, we get connected components [(1), (2,3,4,6), (5)].

Assuming K = 4, we can print ` 2 3 4 6` as a valid set. for K = 2, `1 5` works.

So, assuming we can get the sizes of connected components, can we find to select some components having total node count equal to K. This seems like a knapsack problem. So we need to think more.

###
[](#number-theory-8)Number theory

Let’s focus on prime numbers since the gcd function works on primes independently of other primes.

Consider all primes p such that p*2 \leq N. Then we have edges (2, 2*p) and (p, 2*p). Hence, 2 and p must be in same component for all primes \leq N/2. Let’s add this to a set called S.

All non-prime integers shall also lie in the same set as their prime factors. So any integer \gt 1 which is not a prime shall also be added to this S.

We can claim that the elements present in S shall all be in either A or B.

For example, for N = 13, the primes less than 6.5 are 2,3,5, so the set S formed is [2,3,4,5,6,8,9,10,12].

Elements not present in this set are 1 and all primes greater than N/2. Let’s say there are C such elements. for N = 13, we have [1,7,11,13]. C = 4 here.

In the graph, the set S represents a single component, and the rest all appear as connected components of size 1 each.

###
[](#implementation-9)Implementation

So, if we can add elements from [1,7,11,13] to make a set of size K or size N-K, then it is possible to find such A and B.

It is only when we have either K \leq C or K \geq N-C that we can form set A and B.

Considering N = 13 and K = 11, set A = [2,3,4,5,6,8,9,10,12, 1, 7] is a valid answer. For K = 3, A = [1,11,13] is a valid answer.

The list of primes can be computed using the sieve of Eratosthenes.

#
[](#time-complexity-10)TIME COMPLEXITY

The time complexity is O(N*log(log(N))) per test case due to sieve.

#
[](#solutions-11)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
#define maxn 100007
using namespace std;

vector<int> primes;
bool isp[maxn];

void seive() {
    for(int i = 2; i < maxn; i++) {
        if(isp[i]) continue;
        primes.push_back(i);
        for(int j = i*2; j < maxn; j += i)
            isp[j] = 1;
    }
}

int main() {
    //freopen("wr2.txt", "w", stdout);
    //freopen("inp2.txt", "r", stdin);
    int t;
    cin >> t;
    seive();
    int sm = 0;
    while(t--) {
        int n, k;
        cin >> n >> k;
        sm += n;
        //assert(n > 0 && n <= 100000);
        //assert(k > 0 && k < n);
        int pr = 1;
        if(k > n/2)
            k = n - k, pr = 0;
        int first = upper_bound(primes.begin(), primes.end(), n/2) - primes.begin();
        int last = upper_bound(primes.begin(), primes.end(), n) - primes.begin();
        int count = last - first;
        //cout << count << "\n";
        if(k <= count + 1) {
            cout << "YES\n";
            int grp[n + 1];
            memset(grp, 0, sizeof(grp));
            k--;
            grp[1] = 1;
            while(k) {
                k--;
                grp[primes[first]] = 1;
                first++;
            }
            assert(first <= last + 1);
            for(int i = 1; i <= n; i++)
                if(grp[i] == pr)
                    cout << i << " ";
            cout << "\n";
        } else {
            cout << "NO\n";
        }
    }
    //assert(sm <= 5*100000);
}
``

Tester's Solution
``/* in the name of Anton */

/*
  Compete against Yourself.
  Author - Aryan (@aryanc403)
  Atcoder library - https://atcoder.github.io/ac-library/production/document_en/
*/

#include <algorithm>
#include <cassert>
#include <vector>

namespace atcoder {

struct dsu {
  public:
    dsu() : _n(0) {}
    explicit dsu(int n) : _n(n), parent_or_size(n, -1) {}

    int merge(int a, int b) {
        assert(0 <= a && a < _n);
        assert(0 <= b && b < _n);
        int x = leader(a), y = leader(b);
        if (x == y) return x;
        if (-parent_or_size[x] < -parent_or_size[y]) std::swap(x, y);
        parent_or_size[x] += parent_or_size[y];
        parent_or_size[y] = x;
        return x;
    }

    bool same(int a, int b) {
        assert(0 <= a && a < _n);
        assert(0 <= b && b < _n);
        return leader(a) == leader(b);
    }

    int leader(int a) {
        assert(0 <= a && a < _n);
        if (parent_or_size[a] < 0) return a;
        return parent_or_size[a] = leader(parent_or_size[a]);
    }

    int size(int a) {
        assert(0 <= a && a < _n);
        return -parent_or_size[leader(a)];
    }

    std::vector<std::vector<int>> groups() {
        std::vector<int> leader_buf(_n), group_size(_n);
        for (int i = 0; i < _n; i++) {
            leader_buf[i] = leader(i);
            group_size[leader_buf[i]]++;
        }
        std::vector<std::vector<int>> result(_n);
        for (int i = 0; i < _n; i++) {
            result[i].reserve(group_size[i]);
        }
        for (int i = 0; i < _n; i++) {
            result[leader_buf[i]].push_back(i);
        }
        result.erase(
            std::remove_if(result.begin(), result.end(),
                           [&](const std::vector<int>& v) { return v.empty(); }),
            result.end());
        return result;
    }

  private:
    int _n;
    std::vector<int> parent_or_size;
};

}  // namespace atcoder

#ifdef ARYANC403
    #include <header.h>
#else
    #pragma GCC optimize ("Ofast")
    #pragma GCC target ("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx")
    //#pragma GCC optimize ("-ffloat-store")
    #include<bits/stdc++.h>
    #define dbg(args...) 42;
#endif

// y_combinator from @neal template https://codeforces.com/contest/1553/submission/123849801
// http://www.open-std.org/jtc1/sc22/wg21/docs/papers/2016/p0200r0.html
template<class Fun> class y_combinator_result {
    Fun fun_;
public:
    template<class T> explicit y_combinator_result(T &&fun): fun_(std::forward<T>(fun)) {}
    template<class ...Args> decltype(auto) operator()(Args &&...args) { return fun_(std::ref(*this), std::forward<Args>(args)...); }
};
template<class Fun> decltype(auto) y_combinator(Fun &&fun) { return y_combinator_result<std::decay_t<Fun>>(std::forward<Fun>(fun)); }

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

// #include<atcoder/dsu>
// vector<vi> readTree(const int n){
//     vector<vi> e(n);
//     atcoder::dsu d(n);
//     for(lli i=1;i<n;++i){
//         const lli u=readIntSp(1,n)-1;
//         const lli v=readIntLn(1,n)-1;
//         e[u].pb(v);
//         e[v].pb(u);
//         d.merge(u,v);
//     }
//     assert(d.size(0)==n);
//     return e;
// }

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
T=readIntLn(1,1e4);
lli sumN = 5e5;
while(T--)
{

    const int n=readIntSp(1,min(100000LL,sumN)),k=readIntLn(1,n);
    sumN-=n;
    atcoder::dsu d(n);
    for(lli i=2;i<=n;++i)
        for(lli j=2*i;j<=n;j+=i)
            d.merge(i-1,j-1);
    const auto dg=d.groups();
    vector<int> largeComponent,sizeOneComponent;
    for(auto v:dg){
        if(sz(v)==1)
            sizeOneComponent.pb(v[0]);
        else
            largeComponent=v;
    }

    vector<int> a;
    if(sz(largeComponent)<=k)
        a=largeComponent;
    for(auto x:sizeOneComponent){
        if(sz(a)<k)
            a.pb(x);
    }
    if(sz(a)!=k){
        cout<<"nO"<<endl;
        continue;
    }
    cout<<"yEs"<<endl;
    for(auto x:a)
        cout<<x+1<<" ";
    cout<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class PARPERM{
    //SOLUTION BEGIN
    int MX = (int)1e5;
    boolean[] prime;
    void pre() throws Exception{
        prime = new boolean[1+MX];
        Arrays.fill(prime, true);
        prime[0] = prime[1] = false;
        for(int p = 2; p<= MX; p++)
            if(prime[p])
                for(int q = p+p; q<= MX; q += p)
                    prime[q] = false;
    }
    void solve(int TC) throws Exception{
        int N = ni(), K = ni();

        List<Integer> sp = new ArrayList<>();
        sp.add(1);
        boolean[] special = new boolean[1+N];
        special[1] = true;
        for(int i = (N)/2+1; i<= N; i++)if(prime[i]){
            sp.add(i);
            special[i] = true;
        }

        //All elements not in set must appear in one set.
        if(K <= sp.size()){
            pn("YES");
            for(int i = 0; i< K; i++)p(sp.get(i)+" ");
            pn("");
        }else if(K >= N-sp.size()){
            pn("YES");
            TreeSet<Integer> ans = new TreeSet<>();
            for(int i = 1; i<= N; i++)if(!special[i])ans.add(i);
            for(int i = 0; i< K-(N-sp.size()); i++)ans.add(sp.get(i));
            for(int x:ans)p(x+" ");
            pn("");
        }else pn("NO");
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
        new PARPERM().run();
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
