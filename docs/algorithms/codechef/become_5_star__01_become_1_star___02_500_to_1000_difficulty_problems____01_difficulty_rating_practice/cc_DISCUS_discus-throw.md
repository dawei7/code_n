# Discus Throw

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISCUS |
| Difficulty Rating | 622 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [DISCUS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DISCUS) |

---

## Problem Statement

In discus throw, a player is given $3$ throws and the throw with the **longest distance** is regarded as their final score.

You are given the distances for all $3$ throws of a player. Determine the final score of the player.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $A, B,$ and $C$ denoting the distances in each throw.

---

## Output Format

For each test case, output the final score of the player.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A,B,C \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
10 15 8
32 32 32
82 45 54
```

**Output**

```text
15
32
82
```

**Explanation**

**Test Case $1$:** The longest distance is achieved in the second throw, which is equal to $15$ units. Thus, the answer is $15$.

**Test Case $2$:** In all throws, the distance is $32$ units. Thus, the final score is $32$.

**Test Case $3$:** The longest distance is achieved in the first throw which is equal to $82$ units. Thus, the answer is $82$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 15 8
```

**Output for this case**

```text
15
```



#### Test case 2

**Input for this case**

```text
32 32 32
```

**Output for this case**

```text
32
```



#### Test case 3

**Input for this case**

```text
82 45 54
```

**Output for this case**

```text
82
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH221A/problems/DISCUS)

[Contest Division 2](https://www.codechef.com/MARCH221B/problems/DISCUS)

[Contest Division 3](https://www.codechef.com/MARCH221C/problems/DISCUS)

[Contest Division 4](https://www.codechef.com/MARCH221D/problems/DISCUS)

[Practice](https://www.codechef.com/problems/DISCUS)

**Setter:** [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

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

In discus throw, a player is given 3 throws and the throw with the **longest distance** is regarded as their final score.

You are given the distances for all 3 throws of a player. Determine the final score of the player.

#
[](#quick-explanation-5)QUICK EXPLANATION

The final score of the player is the maximum of scores of all three throws.

#
[](#explanation-6)EXPLANATION

This problem is intended to test the ability to implement a basic program. Given three numbers, find the maximum value.

There are multiple ways to implement this.

**By using function max**

``read A, B, C
print max(A, max(B, C))
``

**By nested conditional statements**

``read A, B, C
if A > B:
    if A > C: print A
    else print C
else:
    if B > C: print B
    else print C
``

The actual implementation can be seen in the solutions below.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
``#include <iostream>
using namespace std;

int main() {
    // your code goes here

    int t,a,b,c;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>a>>b>>c;
        cout<<max(a,max(b,c))<<"\n";;
    }

    return 0;
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

const int MAX_T = 100;
const int MAX_ABC = 100;

#define ll long long int
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

long long int sum_len=0;

void solve()
{
    int a = readIntSp(1, MAX_ABC);
    int b = readIntSp(1, MAX_ABC);
    int c = readIntLn(1, MAX_ABC);
    cout << max(a,max(b, c)) << "\n";
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
    int a[3];
    rep(i,2) a[i] = readIntSp(1, 100);
    a[2] = readIntLn(1, 100);
    sort(a,a+3);
    cout<<a[2]<<'\n';
}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,100);

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
class DISCUS{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        long A = nl(), B = nl(), C = nl();
        pn(Math.max(A, Math.max(B, C)));
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
        new DISCUS().run();
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
