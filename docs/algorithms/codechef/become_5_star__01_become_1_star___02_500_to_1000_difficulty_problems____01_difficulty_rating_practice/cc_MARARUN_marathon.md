# Marathon

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MARARUN |
| Difficulty Rating | 955 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [MARARUN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/MARARUN) |

---

## Problem Statement

Chefland is holding a virtual marathon for the categories $10$ km, $21$ km and $42$ km having prizes $A, B, C$ ($A \lt B \lt C$) respectively to promote physical fitness. In order to claim the prize in a particular category the person must cover the total distance for that category within $D$ days. Also a single person **cannot** apply in multiple categories.

Given the maximum distance $d$ km that Chef can cover in a single day, find the maximum prize that Chef can win at the end of $D$ days. If Chef can't win any prize, print $0$.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, five integers $D, d, A, B, C$.

---

## Output Format

For each test case, output in a single line the answer to the problem.

---

## Constraints

- $1 \leq T \leq 50$
- $1 \leq D \leq 10$
- $1 \leq d \leq 5$
- $1 \leq A \lt B \lt C \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1 2 3
10 1 1 2 3
10 3 1 2 3
```

**Output**

```text
0
1
2
```

**Explanation**

**Test Case $1$:** The maximum distance covered by Chef is $1 \cdot 1 = 1$ km which is less than any of the available distance categories. Hence Chef won't be able to claim a prize in any of the categories.

**Test Case $2$:** The maximum distance covered by Chef is $10 \cdot 1 = 10$ km which is equal to distance of the first category. Hence Chef can claim the maximum prize of $1$ units.

**Test Case $3$:** The maximum distance covered by Chef is $10 \cdot 3 = 30$ km which is more than the distance of the second category but less than that of the third category. Hence Chef can claim the maximum prize of $2$ units.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1 1 2 3
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
10 1 1 2 3
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
10 3 1 2 3
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK129A/problems/MARARUN)

[Contest Division 2](https://www.codechef.com/COOK129B/problems/MARARUN)

[Contest Division 3](https://www.codechef.com/COOK129C/problems/MARARUN)

[Practice](https://www.codechef.com/problems/MARARUN)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Cakewalk

# PREREQUISITES

None

# PROBLEM

Given the distance covered per day in km and the number of days, determine the prize won by person, if a person can get prize A for covering at least 10 km, B for covering at least 21 km, and C for covering at least 42 km. Given A < B < C

# QUICK EXPLANATION

Compute T = d*D as the total distance covered, and compare T with 10, 21, and 42 to determine the category person can apply to, and find the maximum prize.

# EXPLANATION

Since person covers d km per day for D days, total distance covered is T = d*D. Now, the only thing we need to check is the largest prize category person can apply to.

Since we have 0 < A < B < C, we can see that

- If the distance covered is at least 42 km, a person can win prize C

- If the distance covered is between 21 km and 41 km, a person can win prize B

- If the distance covered is between 10 km and 20 km, a person can win prize A

- If the distance covered is less than 10 km, a person cannot win any prize.

We can write those as if conditions as represented by the following pseudocode.

``T = d*D
if T >= 42: print(C)
if T >= 21 and T < 42: print(B)
if T >= 10 and T < 21: print(A)
if T < 10:print(0)
``

We can also reduce the number of conditions by using an if-else ladder, as follows.

``T = d*D
if T >= 42: print(C)
else if T >= 21: print(B)
else if T >= 10: print(A)
else: print(0)
``

### Bonus problems

- What if we are not guaranteed A < B< C in above problem?

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
    int days, d, a, b, c;
    while(t--){
        cin >> days >> d >> a >> b >> c;
        int ans = 0;
        if(days * d >= 42)ans = c;
        else if(days * d >= 21)ans = b;
        else if(days * d >= 10)ans = a;
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

template<class T> bool umin(T& a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T& a, T b) { return a < b ? (a = b, true) : false; }

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
		    assert(false);
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
    int T = readIntLn(1, 50);
    forn(tc, T)
    {
	    int D = readIntSp(1, 10);
	    int d = readIntSp(1, 5);

	    int A = readIntSp(1, 100000);
	    int B = readIntSp(A+1, 100000);
	    int C = readIntLn(B+1, 100000);

	    int dist = d * D;
	    if (dist >= 42)
		    printf("%d\n", C);
	    else if (dist >= 21)
		    printf("%d\n", B);
	    else if (dist >= 10)
		    printf("%d\n", A);
	    else
		    printf("0\n");
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MARARUN{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int D = ni(), d = ni(), A = ni(), B = ni(), C = ni();
        int distance = D*d;
        if(distance >= 42)pn(C);
        else if(distance >= 21)pn(B);
        else if(distance >= 10)pn(A);
        else pn(0);
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
        new MARARUN().run();
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
