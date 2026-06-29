# XxOoRr

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XXOORR |
| Difficulty Rating | 1551 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1500 to 1600 difficulty problems |
| Official Link | [XXOORR](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1600/problems/XXOORR) |

---

## Problem Statement

Given an array $A_1, A_2 \ldots A_N$, find the minimum number of operations (possibly zero) required to convert all integers in $A$ to $0$.

In one operation, you
- choose a non-negative integer $p$ ($p \geq 0$),
- select at most $K$ indices in the array $A$, and
- for each selected index $i$, replace $A_i$ with $A_i\oplus 2^p$. Here, $\oplus$ denotes bitwise XOR.

### Subtasks
- **Subtask #1 (100 points)**: Original Constraints

---

## Input Format

- The first line contains an integer $T$ - the number of test cases. Then $T$ test cases follow.
- The first line of each test case contains two integers $N$, $K$ - the size of the array and the maximum number of elements you can select in an operation.
- The second line of each test case contains $N$ integers $A_1, A_2 \ldots A_N$.

---

## Output Format

For each test case, output the minimum number of operations to make all elements of the array $0$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, K \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases does not exceed $2\cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
1
3 2
3 6 10
```

**Output**

```text
5
```

**Explanation**

Here is one way to achieve $[0, 0, 0]$ from $[3, 6, 10]$ in $5$ operations:
1. Choose $p = 0$ and indices $\{1\}$. Now $A$ becomes $[2, 6, 10]$.
2. Choose $p = 1$ and indices $\{1,2\}$. Now $A$ becomes $[0, 4, 10]$.
3. Choose $p = 1$ and indices $\{3\}$. Now $A$ becomes $[0, 4, 8]$.
4. Choose $p = 2$ and indices $\{2\}$. Now $A$ becomes $[0, 0, 8]$.
5. Choose $p = 3$ and indices $\{3\}$. Now $A$ becomes $[0, 0, 0]$.

It can be shown that at least $5$ operations are required.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JULY21A/problems/XXOORR)

[Contest Division 2](https://www.codechef.com/JULY21B/problems/XXOORR)

[Contest Division 3](https://www.codechef.com/JULY21C/problems/XXOORR)

[Practice](https://www.codechef.com/problems/XXOORR)

**Setter:** [Bharat Singla](https://www.codechef.com/users/singlabharat)

**Tester:** [Aryan](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

Bitwise Operations

# PROBLEM

Given an array, A containing N elements and an integer K, find the minimum number of operations required to convert all integers into 0.

An operation is performed as follows

- Choose a non-negative integer p (p \geq 0)

- Select at most K indices in array A

- For each selected index i, replace A_i with A_i \oplus 2^p, where \oplus denote bitwise XOR operation.

# QUICK EXPLANATION

- In each operation, only the p-th bit of values in array changes, so the number of operations is the sum of the minimum number of operations needed to turn pth bit of all numbers 0 for each p

- For one p, we can count the number of elements in A having p-th bit on, say c, then we need \displaystyle \Big\lceil \frac{c}{K} \Big\rceil operations for p-th bit.

# EXPLANATION

### Observation 1

Let us notice that in one operation, all indices in the subset are XORed with 2^p, which has the effect of flipping only p-th bit in the binary representation of values of selected indices.

By the above logic, we can see that operations affecting different bits are independent of each other. Hence, we can consider each bit one by one, and find the minimum number of operations needed to make p-th bit of all numbers 0.

### Observation 2

**Claim:** We never include any index i in any operation for some p, if A_i has p-th bit off.

**Proof:** Since we aim to make all elements zero, flipping a bit of some number from off to on is actually a step in the opposite direction since some later operation shall have to turn that bit off. The combined effect of these two operations shall be no effect, just wasting two slots in operations. So, it is better not to apply operation at index i for some p, if A_i doesn’t have p-th bit on.

### Implication of Observation 2

Let’s say we have c elements having p-th bit on. In one operation, we can turn K of them off. So, by basic math, we can see that we need at least \displaystyle \Big\lceil \frac{c}{K} \Big\rceil operations.

### Implementation

For each bit, count the number of elements in A having that bit on. Say C_i denotes the number of elements having I-th bit on. So \displaystyle \sum_i \Big\lceil \frac{C_i}{K} \Big\rceil is the required answer

``C = [0,0,0,...]
for x in A:
    for b in range(0, 30):
        if x & (1<<b) > 0:
            C[b]++
ans = 0
for c in C:
    ans += ceil(c/K)
``

# TIME COMPLEXITY

The time complexity is O(N*log(max(A_i))) per test case, since we only need to consider log(max(A_i)) bits.

# SOLUTIONS

Setter's Solution
``import sys
# sys.stdin = open("Input.txt", "r")
# sys.stdout = open("Output.txt", "w")
import math as mt
# from collections import Counter, deque
# from itertools import permutations
# from functools import reduce
# from heapq import heapify, heappop, heappush, heapreplace

def getInput(): return sys.stdin.readline().strip()
def getInt(): return int(getInput())
def getInts(): return map(int, getInput().split())
def getArray(): return list(getInts())

# sys.setrecursionlimit(10**7)
# INF = float('inf')
# MOD1, MOD2 = 10**9+7, 998244353

tc = 1
tc = getInt()

for _ in range(tc):

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    bit_cnt = [0]*32
    for i in a:
        bit_pos = 0
        while (i > 0):
            if (i & 1):
                bit_cnt[bit_pos] += 1
            i >>= 1
            bit_pos += 1

    ans = 0
    for i in bit_cnt:
        ans += mt.ceil(i / k)

    print(ans)
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
T=readIntLn(1,1e5);
lli sumN = 0;
while(T--)
{
    n=readIntSp(1,1e5);
    sumN+=n;
    k=readIntLn(1,1e5);
    a=readVectorInt(n,0,1e9);
    lli fl=1,ans=0;
    while(fl){
        fl=0;
        lli cnt=0;
        for(auto &x:a){
            cnt+=x&1;
            x/=2;
            fl|=x;
        }
        ans+=(cnt+k-1)/k;
    }
    cout<<ans<<endl;
}
    assert(sumN<=2e5);
    aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class XXOORR{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), K = ni();
        int B = 30;
        int[] cnt = new int[B];
        for(int i = 0; i< N; i++){
            int x = ni();
            for(int b = 0; b< B; b++)if((x & (1<<b)) > 0)cnt[b]++;
        }
        int op = 0;
        for(int i = 0; i< B; i++)op += (cnt[i]+K-1)/K;
        pn(op);
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
        new XXOORR().run();
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
