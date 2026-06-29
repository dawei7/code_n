# Maximum Value

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MVALUE |
| Difficulty Rating | 1738 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [MVALUE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/MVALUE) |

---

## Problem Statement

Given an array $A$ of size $N$. Find the maximum value of the expression $a * b + a - b$ where $a$ and $b$ are $2$ distinct elements of the array.

###Input:

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line will contain $N$, number of elements of the array.
- Second line contains $N$ space separated integers, elements of the array $A$.

###Output:
For each testcase, output in a single line answer to the problem.

###Constraints
- $1 \leq T \leq 20$
- $2 \leq N \leq 10^5$
- $-10^9 \leq A_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
2   
2 2
3
5 3 2
```

**Output**

```text
4
17
```

**Explanation**

**Case 1:** Only possible pair is $[2, 2]$ for which answer = $2 * 2 + 2 - 2$ = $4$.

**Case 2:** There are six possible pairs.

For pairs $[2, 3]$ and $[3, 2]$, answer = $2 * 3 + max(2 - 3, 3 - 2)$ = $7$

For pairs $[3, 5]$ and $[5, 3]$ answer = $5 * 3 + max(3 - 5, 5 - 3)$ = $17$ and

For the pairs $[2, 5]$ and $[5, 2]$, answer = $2 * 5 + max(2 - 5, 5 - 2)$ = $13$.

So final answer is maximum of $\{7, 17, 13\}$ = $17$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 2
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3
5 3 2
```

**Output for this case**

```text
17
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START1A/problems/)

[Contest Division 2](https://www.codechef.com/START1B/problems/)

[Contest Division 3](https://www.codechef.com/START1C/problems/)

[Practice](https://www.codechef.com/problems/)

**Setter:** [](https://www.codechef.com/users/)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Easy-medium

# PREREQUISITES

Observation

# PROBLEM

Given an array A containing N integers, find the maximum value of a*b+a-b where a, b are distinct elements of array.

# QUICK EXPLANATION

- Rewriting a*b+a-b = (a-1)*(b+1) +1, we can fix a and see that for b, we only need to consider either minimum or maximum of all elements of array excluding element a.

- It can be done by computing the minimum, second minimum, maximum and second maximum element of array, or just by simply sorting the array.

# EXPLANATION

As mentioned in quick explanation, we can rewrite the expression.

a*b+a-b = a*(b+1) - (b+1)+1 = (a-1)*(b+1)

Hence, we need to maximise (a-1)*(b+1) where a and b are two distinct elements of array.

Now, a naive way to do this would be to try all pairs of numbers, and taking maximum of value resulted by any pair.

Here, if the elements of array were positive, Just taking the last two elements would have been sufficient. But there are negative elements too, and the product of two negative element can also lead to a higher positive product.

So we try to fix a. We can see that once a is fixed, it is optimal to choose b which would maximise value of (a-1)*(b+1)+1. So

- if (a-1) > 0, we’d aim to select the largest element in array, so that the value of b+1 can be maximised, therefore (a-1)*(b+1)+1 is maximised.

- if (a-1) < 0, we’d aim to select the smallest element in array, so that the value of b+1 can be minimised, therefore (a-1)*(b+1)+1 is maximised.

- if (a-1) < 0, then answer is atleast zero.

Hence, all we need to do is to sort the array, fix a to be each element one by one, and choose most optimum b. Taking maximum over all these candidates gives the maximum value of a*b+a-b

### Bonus

Write a solution for above problem which checks minimum number of pairs.

# TIME COMPLEXITY

The time complexity can be O(N) or O(N*log(N)) depending upon implementation, per test case.

The memory complexity is O(N) per test case, can be reduced to O(1).

# SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>

using namespace std;

const int maxt = 10;
const int maxn = 1e5;
const int maxv = 1e9;

int main()
{
    int t; cin >> t;
    vector<long long> v;
    while(t--){
        v.clear();
        int n; cin >> n;
        for(int i = 0; i < n; i++){
            int x; cin >> x;
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        long long ans = LLONG_MIN;
        ans = max(ans, (v[0] + 1) * (v[1] - 1) + 1);
        ans = max(ans, (v[n - 2] + 1) * (v[n - 1] - 1) + 1);
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
#include <limits>

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
	    // 		if(g == '\r')
	    // 			continue;

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
	    freopen("../MVALUE_0.in", "rb", stdin);
	    freopen("../out.txt", "wb", stdout);
    }
#endif
    int T = readIntLn(1, 10);
    forn(tc, T)
    {
	    int N = readIntLn(2, 100'000);
	    vector<int64_t> A(N);
	    forn(i, N)
	    {
		    if (i + 1 == N)
			    A[i] = readIntLn(-1'000'000'000, 1'000'000'000);
		    else
			    A[i] = readIntSp(-1'000'000'000, 1'000'000'000);
	    }
	    sort(A.begin(), A.end());
	    int64_t res = numeric_limits<int64_t>::min();
	    forn(i, N - 1)
	    {
		    int64_t act1 = A[i] * A[i + 1] + A[i] - A[i + 1];
		    int64_t act2 = A[i+1] * A[i] + A[i+1] - A[i];
		    res = max<int64_t>(res, max<int64_t>(act1, act2));
	    }
	    printf("%lld\n", res);
    }

    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MVALUE{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        long[] A = new long[N];
        for(int i = 0; i< N; i++)A[i] = nl();
        Arrays.sort(A);
        long ans = Long.MIN_VALUE;
        for(int i = 0; i< N; i++){
            int lo = 0, hi = N-1;
            if(i == lo)lo++;
            if(i == hi)hi--;
            if(A[i]-1 < 0)ans = Math.max(ans, (A[i]-1)*(A[lo]+1)+1);
            if(A[i]-1 > 0)ans = Math.max(ans, (A[i]-1)*(A[hi]+1)+1);
            if(A[i]-1 == 0)ans = Math.max(ans, 0);
        }
        pn(ans);
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
        new MVALUE().run();
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

# VIDEO EDITORIAL:

Feel free to share your approach. Suggestions are welcomed as always.

</details>
