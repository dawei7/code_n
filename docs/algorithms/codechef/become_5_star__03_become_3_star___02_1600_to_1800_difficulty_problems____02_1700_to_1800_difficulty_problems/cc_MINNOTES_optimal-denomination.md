# Optimal Denomination

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINNOTES |
| Difficulty Rating | 1759 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MINNOTES](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MINNOTES) |

---

## Problem Statement

You are the owner of a big company. You are so rich, that the government has allowed you to print as many notes as you want of any single value that you like. You also have peculiar behavioral traits and you often do things that look weird to a third person.

You have $N$ employees, where the $i$-th employee has salary $A_i$. You want to pay them using a denomination that you create. You are also eco-friendly and wish to save paper. So, you wish to pay them using as few notes as possible. Find out the minimum number of notes required if you can alter the salary of at most one employee to any **positive integer** that you like, and choose the positive integer value that each note is worth (called its denomination).

Each employee must receive the exact value of his/her salary and no more.

### Subtasks
**Subtask #1 (100 points):** Original constraints

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$, where $A_i$ is the salary of the $i$-th employee.

---

## Output Format

For each test case, output in a single line the answer to the problem.

---

## Constraints

- $1 \leq T \leq 12\cdot 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases is at most $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
3
1 2 3
3
8 4 2
2
2 2
```

**Output**

```text
4
4
2
```

**Explanation**

**Test Case $1$:** We can change the salary of the third person to $1$ and use $1$ as the denomination. So in total we need $\frac{1}{1} + \frac{2}{1} + \frac{1}{1}$ = $1 + 2 + 1$ = $4$ notes.

**Test Case $2$:** We can change the salary of the first person to $2$ and use $2$ as the denomination. So in total we need $1 + 2 + 1$ = $4$ notes.

**Test Case $3$:** We can use $2$ as the denomination and we need not change the salary of any person. So in total we need $1 + 1$ = $2$ notes.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
8 4 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
2
2 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JULY21A/problems/MINNOTES)

[Contest Division 2](https://www.codechef.com/JULY21B/problems/MINNOTES)

[Contest Division 3](https://www.codechef.com/JULY21C/problems/MINNOTES)

[Practice](https://www.codechef.com/problems/MINNOTES)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm) and [Akash Bhalotia](https://www.codechef.com/users/akashbhalotia)

**Tester:** [Aryan](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy

# PREREQUISITES

[Prefix/Suffix Sum Arrays](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/)

# PROBLEM

Given an array A containing N positive integers, representing salaries of N employees. You are allowed to change at most 1 integer to any value. After changing, you need to choose a denomination x such that all the employees can be paid with notes of denomination x and the number of notes used is the minimum possible.

Find the minimum number of notes used with optimal choice of changing integer, and optimal choice of denomination.

# QUICK EXPLANATION

- For a fixed array A, choosing the denomination to be the gcd of all elements of A is optimal.

- So, we need to consider changing each element, and for each element, choosing the denomination to be the gcd of all remaining elements is the optimal choice. That way, we determine the number of nodes required if the i-th element is changed.

- The computation of gcd of all except 1 element can be computed quickly by computing prefix gcd and suffix gcd.

# EXPLANATION

### Array with No updates

Let’s consider a simpler problem where you are not allowed to change the array at all. You just can choose the denomination value and you need to determine the minimum number of notes.

For denomination value x, the number of notes required are \displaystyle \sum_{i = 1}^N \frac{A_i}{x} = \frac{\sum_{i = 1}^N A_i}{x}.

So, we need

- All A_i to be divisible by x

-
x should be the maximum possible.

So we need x to be the largest number dividing all A_i, which is satisfied by gcd of all elements of A. So we choose x = gcd(A_i) and compute minimum number of notes as \displaystyle\frac{\sum_{i = 1}^N A_i}{x}

### Solving original problem slowly

So, we know how to solve it if no changes are to be made. Now, we are allowed to change one element. Let’s say we decide that i-th element must be changed, and the denomination x is chosen. It is in our best interest to change i-th element to x so that the number of notes required increases by 1 only.

Hence, let’s iterate over all elements, and assume the current element is the one that is changed, compute GCD of all other elements, and compute the minimum number of notes required, and take minimum for all chosen elements.

The following code represents the above idea in practice.

Code
``ans = INF
for i in range(0, N):
    gcd, sum = 0, 0
    for j in range (0, N):
        if i != j:
            gcd = gcd(gcd, A[i])
            sum += A[i]
    ans = min(ans, 1+(sum/gcd))
``

As the above code has time complexity O(N^2*log(max(A_i))), this shall TLE

### Optimizing above solution

Let us try to remove the inner loop to compute sum and gcd excluding i-th element. We can see that the required gcd is GCD(A_1, A_2 \ldots A_{i-1}, A_{i+1} \ldots A_N). We can write it as GCD(GCD(A_1, A_2 \ldots A_{i-1}), GCD(A_{i+1} \ldots A_N)). The inner two terms are GCD of prefix up to A_{i-1}, and suffix starting from A_{i+1}

Let’s compute prefix GCD array and suffix GCD array for the given A.

Specifically, compute P_i = GCD(P_{i-1}, A_i) P_0 = 0 and S_i = GCD(S_{i+1}, A_i), S_{N+1} = 0. Both of these can be done in time O(N*log(max(A_i))).

Now, we can see that GCD(A_1, A_2 \ldots A_{i-1}) = P_{i-1} and GCD(A_{i+1} \ldots A_N) = S_{i+1}. So, the GCD of all elements except i is GCD(P_{i-1}, S_{i+1}). Computing sum excluding i-th element is trivial.

### Edge Case

Handle N = 1 separately, as for i = 1, both P_0 = S_2 = 0, so GCD(P_0, S_2) evaluates to zero, leading to divide by zero. Since there’s only one element, we can choose denomination same as A_1, requiring only one note.

# TIME COMPLEXITY

The time complexity is O(N*log(max(A_i))) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 118369, maxn = 1e5, maxtn = 1e6, maxv = 1e9;
const string newln = "\n", space = " ";
ll a[maxn + 10];
ll dp[maxn + 10][2], sum[maxn + 10][2];
int main()
{
    int t, n; cin >> t; int tn = 0;
    while(t--){
        cin >> n; tn += n;
        for(int i = 1; i <= n; i++)cin >> a[i];
        for(int i = 1; i <= n; i++){
            sum[i][0] = sum[i - 1][0] + a[i];
            sum[n - i + 1][1] = sum[n - i + 2][1] + a[n - i + 1];
            dp[i][0] = __gcd(dp[i - 1][0], a[i]);
            dp[n - i + 1][1] = __gcd(dp[n - i + 2][1], a[n - i + 1]);
        }
        ll ans = 1e18;
        for(int i = 1; i <= n; i++){
            ll g = __gcd(dp[i - 1][0], dp[i + 1][1]);
            ans = min(ans, (g == 0 ? 0 : (sum[i - 1][0] + sum[i + 1][1]) / g) + 1);
        }
        cout << ans << endl;
        for(int i = 0; i <= n + 2; i++){
            a[i] = 0;
            sum[i][0] = sum[i][1] = 0;
            dp[i][0] = dp[i][1] = 0;
        }
    }
    assert(tn <= maxtn);
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
T=readIntLn(1,12e4);
lli sumN=0;
while(T--)
{

    n=readIntLn(1,1e5);
    sumN+=n;
    a=readVectorInt(n,1,1e9);
    if(n==1){
        cout<<1<<endl;
        continue;
    }
    lli sum=0;
    for(auto &x:a)
        sum+=x;
    vi pref(n+1),suf(n+1);
    lli ans=INF;
    for(lli i=0;i<n;++i){
        pref[i+1]=__gcd(pref[i],a[i]);
    }

    for(lli i=n-1;i>=0;--i){
        suf[i]=__gcd(suf[i+1],a[i]);
    }

    ans=min(ans,sum/pref[n]);
    fo(i,n){
        lli g=__gcd(pref[i],suf[i+1]);
        ans=min(ans,1+(sum-a[i])/g);
    }
    cout<<ans<<endl;
}
    assert(sumN<=1e6);
    aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MINNOTES{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        long[] A = new long[2+N], pre = new long[2+N], suf = new long[2+N];
        long sum = 0;
        for(int i = 1; i<= N; i++){
            A[i] = nl();
            sum += A[i];
        }
        if(N == 1){
            pn(1);
            return;
        }
        for(int i = 1; i<= N; i++)pre[i] = gcd(pre[i-1], A[i]);
        for(int i = N; i>= 1; i--)suf[i] = gcd(suf[i+1], A[i]);
        long ans = Long.MAX_VALUE;
        for(int i = 1; i<= N; i++){
            long gcd = gcd(pre[i-1], suf[i+1]);
            long total = sum-A[i];
            long notes = total/gcd + 1;
            ans = Math.min(ans, notes);
        }
        pn(ans);
    }
    long gcd(long a, long b){return b == 0?a:gcd(b, a%b);}
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
        new MINNOTES().run();
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
