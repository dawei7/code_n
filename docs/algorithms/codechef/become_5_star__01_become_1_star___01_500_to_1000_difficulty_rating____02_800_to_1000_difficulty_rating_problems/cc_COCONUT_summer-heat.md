# Summer Heat

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COCONUT |
| Difficulty Rating | 852 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [COCONUT](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/COCONUT) |

---

## Problem Statement

### Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/COCONUT.pdf),

Chefland has $2$ different types of coconut, type $A$ and type $B$. Type $A$ contains only $x_a$ milliliters of coconut water and type $B$ contains only $x_b$ grams of coconut pulp. Chef's nutritionist has advised him to consume $X_a$ milliliters of coconut water and $X_b$ grams of coconut pulp every week in the summer. Find the total number of coconuts (type $A$ + type $B$) that Chef should buy each week to keep himself active in the hot weather.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, four integers $x_a$, $x_b$, $X_a$, $X_b$.

---

## Output Format

For each test case, output in a single line the answer to the problem.

---

## Constraints

- $1 \leq T \leq 15000$
- $100 \leq x_a \leq 200$
- $400 \leq x_b \leq 500$
- $1000 \leq X_a \leq 1200$
- $1000 \leq X_b \leq 1500$
- $x_a$ divides $X_a$.
- $x_b$ divides $X_b$.

---

## Examples

**Example 1**

**Input**

```text
3
100 400 1000 1200
100 450 1000 1350
150 400 1200 1200
```

**Output**

```text
13
13
11
```

**Explanation**

**TestCase $1$:**
Number of coconuts of Type $A$ required = $\frac{1000}{100} = 10$ and number of coconuts of Type $B$ required = $\frac{1200}{400} = 3$.  So the total number of coconuts required is $10 + 3 = 13$.

**TestCase $2$:**
Number of coconuts of Type $A$ required = $\frac{1000}{100} = 10$ and number of coconuts of Type $B$ required = $\frac{1350}{450} = 3$.  So the total number of coconuts required is $10 + 3 = 13$.

**TestCase $3$:**
Number of coconuts of Type $A$ required = $\frac{1200}{150} = 8$ and number of coconuts of Type $B$ required = $\frac{1200}{400} = 3$.  So the total number of coconuts required is $8 + 3 = 11$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 400 1000 1200
```

**Output for this case**

```text
13
```



#### Test case 2

**Input for this case**

```text
100 450 1000 1350
```

**Output for this case**

```text
13
```



#### Test case 3

**Input for this case**

```text
150 400 1200 1200
```

**Output for this case**

```text
11
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE21A/problems/COCONUT)

[Contest Division 2](https://www.codechef.com/JUNE21B/problems/COCONUT)

[Contest Division 3](https://www.codechef.com/JUNE21C/problems/COCONUT)

[Practice](https://www.codechef.com/problems/COCONUT)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Chefland has 2 different types of coconut, type A and type B. Type A contains only x_a milliliters of coconut water and type B contains only x_b grams of coconut pulp. Chef’s nutritionist has advised him to consume X_a milliliters of coconut water and X_b grams of coconut pulp every week in the summer. Find the total number of coconuts (type A + type B) that the Chef should buy each week to keep himself active in the hot weather.

# QUICK EXPLANATION

Chef must eat X_a/x_a coconuts of type A and X_b/x_b coconuts of type B.

# EXPLANATION

Chef gets x_a milliliters of coconut water from coconuts of type A, and he needs X_a milliliters of coconut water, then how many coconuts of type A does the chef need?

Since 1 coconut provides x_a milliliters of coconut water, P coconuts would provide P*x_a milliliters. Chef need P such that P*x_a = X_a, which implies P = X_a / x_a. Hence, Chef  consume P coconuts of type A.

By similar reasoning, we can see that Chef consumes Q = X_b/x_b coconuts of type B.

This way, the total number of coconuts consumed is P+Q = X_a/x_a + X_b/x_b.

Following C++ code depicts the above idea

``    int T;
    cin>>T;
    while(T-->0){
        int Xa, xa, Xb, xb;
        cin>>xa>>xb>>Xa>>Xb;
        int count = Xa/xa + Xb/xb;
        cout<<count<<"\n";
    }
``

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

int main()
{
    int t; cin >> t;
    int a, b, c, d;
    while(t--){
        cin >> a >> b >> c >> d;
        int ans = c / a + d / b;
        cout << ans << endl;
    }
}
``

Tester's Solution
``#include <iostream>
#include <cassert>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <random>

#ifdef HOME
    #include <windows.h>
#endif

#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define for1(i, n) for (int i = 1; i <= (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for (int i = (int)(a); i <= (int)(b); ++i)

template<class T> bool umin(T &a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T &a, T b) { return a < b ? (a = b, true) : false; }

using namespace std;

long long readInt(long long l, long long r, char endd) {
    long long x = 0;
    int cnt = 0;
    int fi = -1;
    bool is_neg = false;
    while (true) {
	    char g = getchar();
	    if (g == '-') {
		    assert(fi == -1);
		    is_neg = true;
		    continue;
	    }
	    if ('0' <= g && g <= '9') {
		    x *= 10;
		    x += g - '0';
		    if (cnt == 0) {
			    fi = g - '0';
		    }
		    cnt++;
		    assert(fi != 0 || cnt == 1);
		    assert(fi != 0 || is_neg == false);

		    assert(!(cnt > 19 || (cnt == 19 && fi > 1)));
	    }
	    else if (g == endd) {
		    assert(cnt > 0);
		    if (is_neg) {
			    x = -x;
		    }
		    assert(l <= x && x <= r);
		    return x;
	    }
	    else {
		    //assert(false);
	    }
    }
}

string readString(int l, int r, char endd) {
    string ret = "";
    int cnt = 0;
    while (true) {
	    char g = getchar();
	    assert(g != -1);
	    if (g == endd) {
		    break;
	    }
	    cnt++;
	    ret += g;
    }
    assert(l <= cnt && cnt <= r);
    return ret;
}
long long readIntSp(long long l, long long r) {
    return readInt(l, r, ' ');
}
long long readIntLn(long long l, long long r) {
    return readInt(l, r, '\n');
}
string readStringLn(int l, int r) {
    return readString(l, r, '\n');
}
string readStringSp(int l, int r) {
    return readString(l, r, ' ');
}

int main(int argc, char** argv)
{
#ifdef HOME
    if(IsDebuggerPresent())
    {
	    freopen("../in.txt", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 15'000);
    forn(tc, T)
    {
	    int xa = readIntSp(100, 200);
	    int xb = readIntSp(400, 500);

	    int Xa = readIntSp(1'000, 1'200);
	    int Xb = readIntLn(1'000, 1'500);
	    assert(Xa % xa == 0);
	    assert(Xb % xb == 0);
	    printf("%d\n", Xa / xa + Xb / xb);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class COCONUT{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int xa = ni(), xb = ni(), Xa = ni(), Xb = ni();
        pn(Xa/xa + Xb/xb);
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
        new COCONUT().run();
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
