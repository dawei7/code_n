# Utkarsh and Placement tests

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UTKPLC |
| Difficulty Rating | 886 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [UTKPLC](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/UTKPLC) |

---

## Problem Statement

Utkarsh is currently sitting for placements. He has applied to three companies named $A, B$, and $C$.

You know Utkarsh's order of preference among these $3$ companies, given to you as characters `first`, `second`, and `third` respectively (where `first` is the company he prefers most).

You also know that Utkarsh has received offers from exactly two of these three companies, given you as characters $x$ and $y$.

Utkarsh will always accept the offer from whichever company is highest on his preference list. Which company will he join?

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains three different space-separated characters: `first`, `second`, and `third`, denoting Utkarsh's order of preference among the three companies.
- The second line of each test case contains two space-separated characters $x$ and $y$, the companies from which Utkarsh has received offers.

---

## Output Format

For each test case, print one line containing a single character, the company whose offer Utkarsh will accept.

The output is not case sensitive, so if the answer is $A$, both $a$ and $A$ will be accepted.

---

## Constraints

- $1 \leq T \leq 36$
- `first`, `second` and `third` are three different characters among $\{A, B, C\}$.
- $x$ and $y$ are two different characters among $\{A, B, C\}$.

---

## Examples

**Example 1**

**Input**

```text
2
A B C
A B
B C A
A C
```

**Output**

```text
A
C
```

**Explanation**

**Test Case 1.** Utkarsh has received offers from $A$ and $B$. Of these two, he prefers company $A$ (first preference) over $B$ (second preference). Therefore Utkarsh will accept the offer of company $A$.

**Test Case 2.** Utkarsh has received offers from $A$ and $C$, where company $C$ is his second preference and company $A$ is his third preference. Utkarsh will accept the offer of company $C$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
A B C
A B
```

**Output for this case**

```text
A
```



#### Test case 2

**Input for this case**

```text
B C A
A C
```

**Output for this case**

```text
C
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/DEC21A/problems/UTKPLC)

[Contest Division 2](https://www.codechef.com/DEC21B/problems/UTKPLC)

[Contest Division 3](https://www.codechef.com/DEC21C/problems/UTKPLC)

[Practice](https://www.codechef.com/problems/UTKPLC)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

**Tester:** [Lavish Gupta](https://www.codechef.com/users/lavish315)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Utkarsh is currently sitting for placements. He has applied to three companies named A, B, and C.

You know Utkarsh’s order of preference among these 3 companies, given to you as characters `first`, `second`, and `third` respectively (where `first` is the company he prefers most).

You also know that Utkarsh has received offers from exactly two of these three companies, given you as characters x and y.

Utkarsh will always accept the offer from whichever company is highest on his preference list. Which company will he join?

#
[](#quick-explanation-5)QUICK EXPLANATION

If Utkarsh received the offer from his first preference, then He’d join his first preference. Otherwise, he’d join his second preference.

#
[](#explanation-6)EXPLANATION

In this problem, we just need to implement the problem statement. The focus is on our ability to translate the problem statement into functioning error-free code.

We can check companies one by one in the order of preference if Utkarsh received an offer from that company. On finding the first company, from which he did receive an offer, we need to print that company name.

So, one basic implementation (in python) would be

``T = int(input())
for _ in range(T):
    first, second, third = input().split(" ")
    X, Y = input().split(" ")

    for company in (first, second, third):
        if company == X or company == Y:
            print(company)
            break
``

**Follow up:**

Prove that the third preference of Utkarsh would never be the company Utkarsh joins.

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
    char a,b,c;
    cin>>a>>b>>c;
    int vis[200]={0};
    char ch;
    cin>>ch;
    vis[ch]=1;
    cin>>ch;
    vis[ch]=1;
    if(vis[a]==1)
        cout<<a<<'\n';
    else
        cout<<b<<'\n';
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

const int MAX_T = 36;
const int MAX_N = 1e6+5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

// int sum_len = 0;
// int max_n = 0;
// int yess = 0;
// int nos = 0;
// int total_ops = 0;

// int n;

void solve()
{

    string p[3] ;
    p[0] = readStringSp(1 , 1);
    p[1] = readStringSp(1 , 1);
    p[2] = readStringLn(1 , 1);

    string s[2] ;
    s[0] = readStringSp(1 , 1);
    s[1] = readStringLn(1 , 1);

    for(int i = 0 ; i < 3 ; i++)
    {
        for(int j = 0 ; j < 2 ; j++)
        {
            if(s[j] == p[i])
            {
                cout << p[i] << endl ;
                return ;
            }
        }
    }
    return ;
}

signed main()
{
    fast;
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
       solve() ;
    }

    assert(getchar() == -1);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    //cerr<<"Sum of lengths : " << sum_len << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class UTKPLC{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        char[] pref = new char[]{n().charAt(0), n().charAt(0), n().charAt(0)};
        char[] offer = new char[]{n().charAt(0), n().charAt(0)};

        if(pref[0] == offer[0] || pref[0] == offer[1])pn(pref[0]);
        else pn(pref[1]);
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
        new UTKPLC().run();
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
