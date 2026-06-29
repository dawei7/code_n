# Bath in Winters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BATH |
| Difficulty Rating | 643 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [BATH](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BATH) |

---

## Problem Statement

A geyser has a capacity of $X$ litres of water and a bucket has a capacity of $Y$ litres of water.

One person requires **exactly** $2$ buckets of water to take a bath. Find the **maximum** number of people that can take bath using water from **one completely filled** geyser..

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, two integers $X, Y$.

---

## Output Format

For each test case, output the **maximum** number of people that can take bath.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
10 6
25 1
100 10
30 40
```

**Output**

```text
0
12
5
0
```

**Explanation**

**Test Case $1$:** One bucket has a capacity of $6$ litres. This means that one person requires $2\cdot 6 = 12$ litres of water to take a bath. Since this is less than the total water present in geyser, $0$ people can take bath.

**Test Case $2$:** One bucket has a capacity of $1$ litre. This means that one person requires $2\cdot 1 = 2$ litres of water to take a bath. The total amount of water present in geyser is $25$ litres. Thus, $12$ people can take bath. Note that $1$ litre water would remain unused in the geyser.

**Test Case $3$:** One bucket has a capacity of $10$ litres. This means that one person requires $2\cdot 10 = 20$ litres of water to take a bath. The total amount of water present in geyser is $100$ litres. Thus, $5$ people can take bath. Note that $0$ litres of water would remain unused in the geyser after this.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 6
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
25 1
```

**Output for this case**

```text
12
```



#### Test case 3

**Input for this case**

```text
100 10
```

**Output for this case**

```text
5
```



#### Test case 4

**Input for this case**

```text
30 40
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

``# PROBLEM LINK:
``

[Contest Division 1](https://www.codechef.com/MARCH221A/problems/BATH)

[Contest Division 2](https://www.codechef.com/MARCH221B/problems/BATH)

[Contest Division 3](https://www.codechef.com/MARCH221C/problems/BATH)

[Contest Division 4](https://www.codechef.com/MARCH221D/problems/BATH)

[Practice](https://www.codechef.com/problems/BATH)

**Setter:** [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

**Testers:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-1)DIFFICULTY

Cakewalk

#
[](#prerequisites-2)PREREQUISITES

None

#
[](#problem-3)PROBLEM

A geyser has a capacity of X liters of water and a bucket has a capacity of Y liters of water.

One person requires **exactly** 2 buckets of water to take a bath. Find the **maximum** number of people that can take bath using water from **one completely filled** geyser.

#
[](#quick-explanation-4)QUICK EXPLANATION

The number of people that can take bath is \displaystyle\left\lfloor \frac{X}{2*Y} \right\rfloor.

#
[](#explanation-5)EXPLANATION

There are the following ways to approach this problem.

**Simulation**

Let’s try simulating what the problem statement says. While there are at least 2*Y liters of water available, a person takes bath, which increases the count of people by one, and decreases water left by 2*Y. At end of this process, the number of people who could bathe is the maximum possible.

It’d be something like this

``read X, Y
waterLeft = X
peopleCount = 0
while (X >= 2*Y):
    waterLeft -= 2*X
    peopleCount++

print(peopleCount)
``

The time complexity of this approach is O(X)

**By basic math**

It is easy to observe that in the above process, we can replace repeated subtraction with a single division. If we divide the water left (X) by the water required per person (2*Y), we get the number of people who can take bath. Since X may or may not be divisible by 2*Y, the number of people can be in fractional form. In that case, floor value needs to be taken.

So the required number of people is \displaystyle\left\lfloor \frac{X}{2*Y} \right\rfloor.

#
[](#time-complexity-6)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-7)SOLUTIONS

Setter's Solution
``#include <iostream>
using namespace std;

int t,x,y;

int main() {
    // your code goes here

    cin>>t;

    while(t--)
    {
        cin>>x>>y;
        cout<<x/(2*y)<<"\n";
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

const int MAX_T = 1000;
const int MAX_XY = 100;

#define ll long long int
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

long long int sum_len=0;

void solve()
{
    int x = readIntSp(1, MAX_XY);
    int y = readIntLn(1, MAX_XY);
    cout << x/(2*y) << "\n";
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
    int x = readIntSp(1, 100);
    int y = readIntLn(1, 100);

    cout<<x/(2*y)<<'\n';
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
class BATH{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        pn(ni()/(2*ni()));
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
        new BATH().run();
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
