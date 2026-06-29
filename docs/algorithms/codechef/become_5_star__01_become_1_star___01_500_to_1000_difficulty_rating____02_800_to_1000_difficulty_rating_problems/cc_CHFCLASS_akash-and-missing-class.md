# Akash and Missing Class

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFCLASS |
| Difficulty Rating | 931 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [CHFCLASS](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/CHFCLASS) |

---

## Problem Statement

Akash loves going to school, but not on weekends.

A week consists of $7$ days (Monday to Sunday). Akash takes a leave every **Saturday**.

If a month consists of $N$ days and the **first-day** of the month is **Monday**, find the number of days Akash would take a leave in the whole month.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, one integer $N$ - the number of days in the month.

---

## Output Format

For each test case, output in a single line, the number of days Akash would take a leave in the whole month.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
5
6
8
22
```

**Output**

```text
0
1
1
3
```

**Explanation**

**Test case $1$:** The month consists of $5$ days (Monday, Tuesday, Wednesday, Thursday, and Friday). Since there are no Saturdays, Akash would go to school every day. Thus, he takes a leave for $0$ days.

**Test case $2$:** The month consists of $6$ days (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday). Akash takes a leave only on Saturday. Thus, he takes a leave for $1$ day.

**Test case $3$:** The month consists of $8$ days (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday). Akash takes a leave only on Saturday. Thus, he takes a leave for $1$ day.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
8
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
22
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH221A/problems/CHFCLASS)

[Contest Division 2](https://www.codechef.com/MARCH221B/problems/CHFCLASS)

[Contest Division 3](https://www.codechef.com/MARCH221C/problems/CHFCLASS)

[Contest Division 4](https://www.codechef.com/MARCH221D/problems/CHFCLASS)

[Practice](https://www.codechef.com/problems/CHFCLASS)

**Setter:** [Akash Sharma](https://www.codechef.com/users/justfun21)

**Testers:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Cakewalk

#
[](#prerequisites-3)PREREQUISITES

Basic math

#
[](#problem-4)PROBLEM

Akash loves going to school, but not on weekends.

A week consists of 7 days (Monday to Sunday). Akash takes a leave every **Saturday**.

If a month consists of N days and the **first-day** of the month is **Monday**, find the number of days Akash would take a leave in the whole month.

#
[](#explanation-5)EXPLANATION

The N days include \displaystyle\left\lfloor \frac{N}{7} \right\rfloor complete weeks, and one incomplete week with N \bmod 7 days starting from Monday. Let’s handle the complete weeks and the last week separately.

- For a complete week, it will contain exactly one Saturday, leading to one leave per week.

- If the incomplete week includes Saturday, then it will contribute one more leave.

Since the week is starting from Monday, the only way an incomplete week includes Saturday when it ends on Saturday, which happens only if N \bmod 7 = 6.

So if we have N \bmod 7 = 6, then there would be \displaystyle\left\lfloor \frac{N}{7} \right\rfloor+1 leaves. Otherwise there would be \displaystyle\left\lfloor \frac{N}{7} \right\rfloor

**Bonus**

We can solve this problem without adding if condition for N \bmod 7 = 6.

Spoiler

Prove why \displaystyle\left\lfloor \frac{N+1}{7} \right\rfloor would give correct number of leaves for all N.

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``#pragma GCC optimize("Ofast")
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie();cout.tie();
    long long TT = 1;
    cin>>TT;
    for(long long TR = 1;TR <= TT;TR++){
        int n;
        cin>>n;
        int ans = n/7;
        if(n%7==6)ans++;
        // if(n>10000)ans = 0;
        cout<<ans<<'\n';
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
const int MAX_N = 1000000000;

#define ll long long int
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

long long int sum_len=0;

void solve()
{
    int n = readIntLn(1, MAX_N);
    cout << (n + 1)/7 << "\n";
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
ll mod = 998244353;

ll po(ll x, ll n){
    ll ans=1;
    while(n>0){ if(n&1) ans=(ans*x)%mod; x=(x*x)%mod; n/=2;}
    return ans;
}

void solve()
{
    int n = readIntLn(1, 1e9);
    max_n = max(max_n,n);
    cout<<(n+1)/7<<'\n';
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

    //assert(getchar() == -1);
    assert(sum_n<=1e6);

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
class CHFCLASS{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        pn((nl()+1)/7);
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
        new CHFCLASS().run();
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
