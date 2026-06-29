# Find the Direction

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FACEDIR |
| Difficulty Rating | 880 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [FACEDIR](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/FACEDIR) |

---

## Problem Statement

Chef is currently facing the north direction. Each second he rotates exactly $90$ degrees in clockwise direction. Find the direction in which Chef is facing after exactly $X$ seconds.

$\textbf{Note}:$ There are only 4 directions: North, East, South, West (in clockwise order).

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single integer $X$.

---

## Output Format

For each testcase, output the direction in which Chef is facing after exactly $X$ seconds.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1
3
6
```

**Output**

```text
East
West
South
```

**Explanation**

Chef is facing North in the starting.

**Test Case $1$:** After $1$ second he turns $90$ degrees clockwise and now faces the east direction.

**Test Case $2$:**
Direction after $1$ second- east

Direction after $2$ seconds- south

Direction after $3$ seconds- west

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
East
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
West
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
South
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START11A/problems/FACEDIR)

[Contest Division 2](https://www.codechef.com/START11B/problems/FACEDIR)

[Contest Division 3](https://www.codechef.com/START11C/problems/FACEDIR)

[Practice](https://www.codechef.com/problems/FACEDIR)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Samarth Gupta](https://www.codechef.com/users/samarth2017)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

The chef is standing facing North. For the next X second, he rotates exactly 90 degrees in the clockwise direction. Find the direction of Chef after X seconds where 1 \leq X \leq 100

Note: There are only 4 directions: North, East, South, West (in clockwise order).

#
[](#quick-explanation-5)QUICK EXPLANATION

- After every 4 rotation, the Chef faces the same direction as before. So let’s group all rotations in buckets of 4. The last bucket may be unfilled.

- All buckets containing 4 rotations do not change the direction. We only care about the last bucket, which may have less than 4 rotations.

- We can simulate the last three rotations or write cases to identify the final direction.

#
[](#explanation-6)EXPLANATION

Since the constraints of this problem are small, a simulation-based solution is acceptable along the following lines.

``dir = 'N'
repeat X times:
    if(dir == 'N')dir = 'E'
    else if(dir == 'E')dir = 'S'
    else if(dir == 'S')dir = 'W'
    else if(dir == 'W')dir = 'N'
``

The final value stored in dir represents the final direction. This solution takes O(X) time.

We can also solve it in O(1) as well, by noticing that rotating 4 times is equivalent to not rotating at all.

So we can say that doing X rotation gets same direction as doing X - 4 rotations, X-8 rotations … and (X - 4*C) for some C where X-4*C \geq 0. We can choose C = \lfloor X/4 \rfloor, which makes X-4*C = X \bmod 4.

Hence, we only need to perform up to 3 rotations, as we can replace X with X \bmod 4. We can use the above simulation or write cases to find out the final direction.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(X) or O(1) per test case.

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
    ll n;
    cin>>n;
    n%=4;
    if(n==0)
        cout<<"North\n";
    else if(n==1)
        cout<<"East\n";
    else if(n==2)
        cout<<"South\n";
    else if(n==3)
        cout<<"West\n";
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
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
``#include <bits/stdc++.h>
using namespace std;

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

int main() {
    // your code goes here
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int t;
    t = readIntLn(1, 100);
    int sum = 0;
    while(t--){
        int n;
        n = readIntLn(1, 1000);
        if(n%4 == 0)
            cout << "North\n";
        else if(n%4 == 1)
            cout << "East\n";
        else if(n%4 == 2)
            cout << "South\n";
        else
            cout << "West\n";
    }
    readEOF();
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class FACEDIR{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        String[] D = new String[]{"North", "East", "South", "West"};
        int dir = ni()%4;
        pn(D[dir]);
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
        new FACEDIR().run();
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
