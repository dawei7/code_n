# Relativity

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RELATIVE |
| Difficulty Rating | 872 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [RELATIVE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/RELATIVE) |

---

## Problem Statement

In Chefland, the speed of light is $c\ \mathrm{m}/\mathrm{s}$, and acceleration due to gravity is $g\ \mathrm{m}/\mathrm{s}^2$.

Find the smallest height (in meters) from which Chef should jump such that during his journey down only under the effect of gravity and independent of any air resistance, he achieves the speed of light and verifies Einstein's theory of special relativity.

Assume he jumps at zero velocity and at any time, his velocity ($v$) and depth of descent ($H$) are related as
$$v^2 = 2 \cdot g \cdot H.$$

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $g$, $c$.

### Output
For each test case, output in a single line the answer to the problem. We can show that under the constraints, the answer is an integer.

---

## Constraints

$1 \leq T \leq 5\cdot 10^3$
- $1 \leq g \leq 10$
- $1000 \leq c \leq 3000$
- $2 \cdot g$ divides $c^2$.

---

## Examples

**Example 1**

**Input**

```text
3
7 1400
5 1000
10 1000
```

**Output**

```text
140000
100000
50000
```

**Explanation**

**Test Case $1$:** For Chef to achieve the speed of light, the minimum height required is $\frac{c^2}{2 \cdot g}$ = $\frac{1400 \cdot 1400}{14}$ = $140000$ meters.

**Test Case $3$:** For Chef to achieve the speed of light, the minimum height required is $\frac{c^2}{2 \cdot g}$ = $\frac{1000 \cdot 1000}{20}$ = $50000$ meters.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 1400
```

**Output for this case**

```text
140000
```



#### Test case 2

**Input for this case**

```text
5 1000
```

**Output for this case**

```text
100000
```



#### Test case 3

**Input for this case**

```text
10 1000
```

**Output for this case**

```text
50000
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JULY21A/problems/RELATIVE)

[Contest Division 2](https://www.codechef.com/JULY21B/problems/RELATIVE)

[Contest Division 3](https://www.codechef.com/JULY21C/problems/RELATIVE)

[Practice](https://www.codechef.com/problems/RELATIVE)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Aryan](https://www.codechef.com/users/aryanc403)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Given the intended velocity c to be achieved and the gravity g, find the minimum height H such that in descent from height H, speed c is achieved, where he jumped at zero velocity and depth H and v are related as v^2 = 2 \cdot g \cdot H

# QUICK EXPLANATION

\displaystyle H = \frac{c^2}{2 \cdot g} is the required minimum height.

# EXPLANATION

We want to achieve velocity c during the descent, and we know that g is nothing, but acceleration, a change in the rate of velocity. We can see that the velocity at the end of the jump shall be higher than any point during the jump.

Also, starting descent at zero velocity, velocity after descending H meters is v where v^2 = 2 \cdot g \cdot H

So, we want to find minimum H such that c^2 \leq 2 \cdot g \cdot H, which happens when \displaystyle H = \frac{c^2}{2 \cdot g}.

Since problem constraints mention that 2 \cdot g divides c^2, the final answer shall always be an integer.

### Bonus

Let’s assume you jump at velocity x m/s. Check if you can achieve velocity c by jumping, and if possible, find the minimum height. x, c and g are given in input.

# TIME COMPLEXITY

The time complexity is O(1) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxt = 5e3;
const string newln = "\n", space = " ";
int main()
{
    int t; cin >> t;
    while(t--){
        int g, v; cin >> g >> v;
        assert((v * v) % (2 * g) == 0);
        int ans = (v * v) / (2 * g);
        cout << ans << endl;
    }
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
T=readIntLn(1,5e3);
while(T--)
{
    const lli g = readIntSp(1,10);
    const lli v = readIntLn(1e3,3e3);
    assert(v*v%(2*g)==0);
    cout<<v*v/(2*g)<<endl;
}   aryanc403();
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class RELATIVE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int G = ni(), C = ni();
        pn((C*C)/(2*G));
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
        new RELATIVE().run();
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
