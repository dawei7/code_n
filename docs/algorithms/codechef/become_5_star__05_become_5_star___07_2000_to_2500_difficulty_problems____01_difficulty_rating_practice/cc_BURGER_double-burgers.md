# Double Burgers

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BURGER |
| Difficulty Rating | 2072 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [BURGER](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/BURGER) |

---

## Problem Statement

You have taken an eating challenge from Chef and now you have to eat exactly $Y$ burgers. You will eat in the following way:

- In the first minute you will eat exactly $X$ burgers and every minute after that you will eat exactly twice the number of burgers you ate in the previous minute.
- Since you can get tired of eating, Chef also allows you take a break from eating for exactly $1$ minute.
- When you start eating again after taking a break, your eating streak resets, i.e. in the first minute after the break you will eat exactly $X$ burgers and every minute after that you will eat exactly double the burgers you ate on the previous minute.

Let $a_1, a_2, ..., a_k$ be the lengths of your eating streaks in minutes. Chef requires that all $a_i$ are pairwise distinct.

Find the minimum number of minutes you need to eat exactly $Y$ burgers or determine it is impossible to do so.

###Input

- The first line contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.

###Output
For each test case, print a single line containing one integer — the minimum number of minutes you need to eat exactly $Y$ burgers, or $−1$ if it is impossible.

###Constraints
- $1\leq T\leq 10^5$
- $1\leq X,Y\leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
2
1 7
1 4
```

**Output**

```text
3
4
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 7
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
1 4
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK129A/problems/BURGER)

[Contest Division 2](https://www.codechef.com/COOK129B/problems/BURGER)

[Contest Division 3](https://www.codechef.com/COOK129C/problems/BURGER)

[Practice](https://www.codechef.com/problems/BURGER)

**Setter:** [Sunidhi Chandra](https://www.codechef.com/users/suni30102)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy-Medium

# PREREQUISITES

Greedy

# PROBLEM

You have taken an eating challenge from Chef, to eat exactly Y burgers. You will eat in the following way.

- In the first minute, you eat exactly X burgers, and in every minute after that, you will eat exactly twice the number of burgers you ate in the previous minute.

- You can take a break of exactly one minute.

- When you start eating again after the break, your eating streak resets, and you eat X burgers in that minute, and so on.

Additionally, let a_1, a_2 \ldots a_k denote the length of your eating streaks. Chef asks that all a_i are pairwise distinct.

Find the minimum number of minutes you need in order to eat exactly Y burgers or determine if it’s impossible to do so.

# QUICK EXPLANATION

- A streak of d minutes involves eating exactly X*(2^{d+1}-1) burgers, and takes d minutes eating, and 1 minute break.

- We can make a set of streaks possible, since the number of burgers eaten in a streak rises exponentially, we don’t need to store streaks of length more than log_2(Y/X).

- Now, considering these streaks in descending order of the number of burgers, while the number of burgers to be eaten is greater or equal to the number of burgers in a streak, it is optimal to include that streak in the set and update the number of burgers to be eaten.

- If, in the end, all burgers are not eaten, it is impossible to eat them all in this setting.

# EXPLANATION

Let us notice first that if X doesn’t divide Y, it’s not possible to eat Y burgers at all, since every minute, we eat burgers in multiples of X. So, if X doesn’t divide Y, it’s an impossible case.

Now assuming Y = T*X, so we need to eat T burgers if our streak starts with exactly 1 burger.

Let us see the number of burgers eaten in a streak of d days. We can see that number of burgers eaten are \displaystyle \sum_{i = 0}^{d-1} 2^i, which is a geometric progression, so the number of burgers eaten shall be 2^d-1.

Let us assume, in a streak, the last day, we take a break. Now, the number of burgers eaten in a streak of d days is 2^{d-1}-1. Also, d \geq 2, since in each streak, we have at least one day we eat, and the last day is spent on a break. **This way, the minute spent on break is already included, except for the last streak**.

### Redefined Goal

Our goal is to find a set A of pairwise integers greater than 1 such that \displaystyle \sum_{x \in A} (2^{x-1}-1) = T (The number of burgers eaten) and \displaystyle -1 + \sum_{x \in A} x is minimized (Sum of length of streaks).  One is subtracted since the last streak also includes one minute for a break, which can be skipped.

Since 2^{d-1}-1 \leq T for d \in A, So we have d-1 \leq log_2(T+1). Hence, we only need to consider positive integers d up to log_2(T+1)+1

Hence, considering first streaks of length up to log_2(T+1), we want to check if there’s a subset with burger count T, and if multiple subsets exist, find the one with minimum sum. The subset cannot contain duplicates.

Let’s consider the streaks now, their duration, and the number of burgers eaten

``duration               burgers eaten
2                                 1
3                                 3
4                                 7
5                                15
6                                31
...
``

### Why greedy selection work

**Claim:** Considering streaks in descending order, if 2^{d-1}-1 \leq T holds for current streak d, then if a valid subset exists, it shall include a streak of length d.

Proof

The number of burgers eaten in streak of length d is 2^{d-1}-1. Let’s assume current streak is not included. So the remaining streak must eat T burgers. The sum of number of burgers in remaining streaks is given by \displaystyle \sum_{x = 2}^{d-1} (2^{x-1}-1) = \sum_{x = 1}^{d-2} 2^x -(d-2). By GP sum, we have \displaystyle \sum_{x = 1}^{d-2} 2^x = 2^{d-1}-2.

Hence, by taking all remaining streaks, we manage to eat 2^{d-1}-d burgers.

But 2^{d-1}-d < 2^d-1 \leq T, so by skipping streak of length d, we can never eat all burgers while keeping the remaining streaks pairwise distinct.

Hence, if a streak of length d is possible, we must include it in our set of streaks.

The above claim allows us to greedily consider streaks from log_2(T) to 2 in decreasing order, check if we can include that streak in our subset. If we can, we must, and we update the number of burgers to be eaten. If at the end of the process, all burgers are not eaten, it means it is impossible to eat them all.

However, if we managed to eat streaks, one less than the sum of lengths of streaks shall give the minimum number of minutes, thus, solving the problem.

We can make the list of streaks beforehand. Refer to my implementation in the case facing any issues.

### Bonus

Prove that the minimum time taken to eat all burgers, if possible, is also the same as the maximum time possible under the problem constraints.

# TIME COMPLEXITY

The time complexity is O(log_2(Y/X)) per test case.

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define fastIO ios_base::sync_with_stdio(false); cin.tie(0)

int main()
{
    fastIO;
    int t=1;
    cin>>t;
    while(t--){
        ll x,y,ans=-1;
        cin>>x>>y;
        if((y%x)==0){
            y/=x;
            for(int k=1;k<60;k++){
                ll val=y+k;
                if(val%2)continue;
                int cnt=__builtin_popcountll(val);
                if(cnt==k){
                    int tmp=0;
                    for(int i=1;i<=60;i++){
                        if(val&(1LL<<i))tmp+=i;
                    }
                    tmp+=k-1;
                    ans=tmp;
                    break;
                }
            }
        }
        cout<<ans<<endl;
    }

return 0;
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
#include <limits>
#include <functional>

#ifdef HOME
    #define NOMINMAX
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

uint32_t lzCount(uint64_t v)
{
#ifdef WIN32
    return static_cast<uint32_t>(__lzcnt64(v));
#else
    return __builtin_clzll(v);
#endif
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
    int T = readIntLn(1, 100'000);

    forn(tc, T)
    {
	    int64_t X = readIntSp(1, 1'000'000'000'000'000'000ll);
	    int64_t Y = readIntLn(1, 1'000'000'000'000'000'000ll);
	    if (Y % X)
	    {
		    printf("-1\n");
		    continue;
	    }
	    Y /= X;
	    int64_t lv = numeric_limits<int64_t>::max();
	    int32_t res = 0;
	    while (Y)
	    {
		    uint32_t lzc = lzCount(Y);
		    int64_t val = (1ll << (64 - lzc)) - 1;
		    if (val > Y)
		    {
			    val = (1ll << (63 - lzc)) - 1;
			    res += 64 - lzc;
		    }
		    else
			    res += 65 - lzc;

		    if(lv == val)
		    {
			    res = 0;
			    break;
		    }
		    Y -= val;
		    lv = val;
	    }
	    --res;
	    printf("%d\n", res);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class BURGER{
    //SOLUTION BEGIN
    int MX = 62;
    long[] burgerCount, duration;
    void pre() throws Exception{
        burgerCount = new long[MX];
        duration = new long[MX];

        burgerCount[0] = 1;
        duration[0] = 2;
        for(int i = 1; i< MX; i++){
            burgerCount[i] = burgerCount[i-1]*2+1;
            duration[i] = duration[i-1]+1;
        }
    }
    void solve(int TC) throws Exception{
        long X = nl(), Y = nl();
        if(Y%X != 0){
            pn(-1);
            return;
        }
        long TotalBurgers = Y/X;
        long days = 0;
        for(int i = MX-1; i>= 0; i--){
            if(TotalBurgers >= burgerCount[i]){
                TotalBurgers -= burgerCount[i];
                days += duration[i];
            }
        }
        if(TotalBurgers == 0)pn(days-1);
        else pn(-1);
    }
    //SOLUTION END
    void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
    static boolean multipleTC = true;
    FastReader in;PrintWriter out;
    void run() throws Exception{
//        in = new FastReader("in.txt");
//        out = new PrintWriter("out.txt");
        in = new FastReader();
        out = new PrintWriter(System.out);
        //Solution Credits: Taranpreet Singh
        int T = (multipleTC)?ni():1;
        pre();for(int t = 1; t<= T; t++)solve(t);
        out.flush();
        out.close();
    }
    public static void main(String[] args) throws Exception{
        new BURGER().run();
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
