# Wordle

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WORDLE |
| Difficulty Rating | 804 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [WORDLE](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/WORDLE) |

---

## Problem Statement

Chef invented a modified wordle.

There is a hidden word $S$ and a guess word $T$, both of length $5$.

Chef defines a string $M$ to determine the correctness of the guess word. For the $i^{th}$ index:
- If the guess at the $i^{th}$ index is correct, the $i^{th}$ character of $M$ is $\texttt{G}$.
- If the guess at the $i^{th}$ index is wrong, the $i^{th}$ character of $M$ is $\texttt{B}$.

Given the hidden word $S$ and guess $T$, determine string $M$.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of two lines of input.
- First line contains the string $S$ - the hidden word.
- Second line contains the string $T$ - the guess word.

---

## Output Format

For each test case, print the value of string $M$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{BgBgB}$, $\texttt{BGBGB}$, $\texttt{bgbGB}$ and $\texttt{bgbgb}$ will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $|S| = |T| = 5$
- $S, T$ contain uppercase english alphabets only.

---

## Examples

**Example 1**

**Input**

```text
3
ABCDE
EDCBA
ROUND
RINGS
START
STUNT
```

**Output**

```text
BBGBB
GBBBB
GGBBG
```

**Explanation**

**Test Case $1$:** Given string $S = \texttt{ABCDE}$ and $T = \texttt{EDCBA}$. The string $M$ is:
- Comparing the first indices, $\texttt{A} \neq \texttt{E}$, thus, $M[1] = \texttt{B}$.
- Comparing the second indices, $\texttt{B} \neq \texttt{D}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{C} = \texttt{C}$, thus, $M[3] = \texttt{G}$.
- Comparing the fourth indices, $\texttt{D} \neq \texttt{B}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{E} \neq \texttt{A}$, thus, $M[5] = \texttt{B}$.
Thus, $M = \texttt{BBGBB}$.

**Test Case $2$:** Given string $S = \texttt{ROUND}$ and $T = \texttt{RINGS}$. The string $M$ is:
- Comparing the first indices, $\texttt{R} = \texttt{R}$, thus, $M[1] = \texttt{G}$.
- Comparing the second indices, $\texttt{O} \neq \texttt{I}$, thus, $M[2] = \texttt{B}$.
- Comparing the third indices, $\texttt{U} \neq \texttt{N}$, thus, $M[3] = \texttt{B}$.
- Comparing the fourth indices, $\texttt{N} \neq \texttt{G}$, thus, $M[4] = \texttt{B}$.
- Comparing the fifth indices, $\texttt{D} \neq \texttt{S}$, thus, $M[5] = \texttt{B}$.
Thus, $M = \texttt{GBBBB}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
ABCDE
EDCBA
```

**Output for this case**

```text
BBGBB
```



#### Test case 2

**Input for this case**

```text
ROUND
RINGS
```

**Output for this case**

```text
GBBBB
```



#### Test case 3

**Input for this case**

```text
START
STUNT
```

**Output for this case**

```text
GGBBG
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH221A/problems/WORDLE)

[Contest Division 2](https://www.codechef.com/MARCH221B/problems/WORDLE)

[Contest Division 3](https://www.codechef.com/MARCH221C/problems/WORDLE)

[Contest Division 4](https://www.codechef.com/MARCH221D/problems/WORDLE)

[Practice](https://www.codechef.com/problems/WORDLE)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Testers:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

None

#
[](#problem-4)PROBLEM

Chef invented a modified wordle.

There is a hidden word S and a guess word T, both of length 5.

Chef defines a string M to determine the correctness of the guess word. For the i^{th} index:

- If the guess at the i^{th} index is correct, the i^{th} character of M is \texttt{G}.

- If the guess at the i^{th} index is wrong, the i^{th} character of M is \texttt{B}.

Given the hidden word S and guess T, determine string M.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Each position is independent. If S_i equals T_i, then we have M_i = \texttt{G}, otherwise M_i = \texttt{B}

- So we can simply iterate over all 5 positions and check this.

#
[](#explanation-6)EXPLANATION

**Observation:** Characters at i-th position do not affect characters at any position j \neq i.

This means that we can simply consider S_i and T_i, compare them, and determine M_i based on that. Hence the intended solution is to consider all 5 positions one by one and calculate M_i for each i.

Since the length of string is small, we can implement this either by looping over the string, or by having 5 if-else conditions.

**For loop solution**

``Read S, T
M = ""
for i from 0 to N-1:
     if S[i] == T[i]:
          M += "G"
     else:
          M += "B"
print M
``

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(N) per test case, where N = 5 for this problem.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
``//Utkarsh.25dec
#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
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
void solve()
{
    string s=readStringLn(5,5);
    string t=readStringLn(5,5);
    for(int i=0;i<5;i++)
    {
        if(s[i]==t[i])
            cout<<'G';
        else
            cout<<'B';
    }
    cout<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution 1
``#include <bits/stdc++.h>
#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")
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
const int MAX_XY = 100;

#define ll long long int
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

long long int sum_len=0;

void solve()
{
    string a = readStringLn(5, 5);
    string b = readStringLn(5, 5);
    for(int i = 0; i < 5; i++)
        cout << (a[i] == b[i]?'G':'B');
    cout << "\n";
}

signed main()
{
    //fast;
    #ifndef ONLINE_JUDGE
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    #endif

    int t = readIntLn(1, MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve();
    }

    assert(getchar() == -1);
}
``

Tester's Solution 2
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

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int sum_n = 0, sum_m = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll mod = 1000000007;

ll po(ll x, ll n){
    ll ans=1;
    while(n>0){ if(n&1) ans=(ans*x)%mod; x=(x*x)%mod; n/=2;}
    return ans;
}

void solve()
{
    string s = readStringLn(5,5);
    string t = readStringLn(5,5);

    rep(i,5){
        cout<<(s[i]==t[i]?'G':'B');
    }
    cout<<'\n';
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,1000);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_n<=1e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<'\n';
    cerr<<"Maximum length : " << max_n <<'\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class Main{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        String A = n(), B = n();
        StringBuilder ans = new StringBuilder();
        int N = A.length();
        hold(N == B.length());
        for(int i = 0; i< N; i++)ans.append(A.charAt(i) == B.charAt(i)?"G":"B");
        pn(ans.toString());
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
        new Main().run();
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
