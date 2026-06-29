# MEX-OR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEXOR |
| Difficulty Rating | 1650 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [MEXOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/MEXOR) |

---

## Problem Statement

The *MEX* (minimum excluded) of an array is the smallest non-negative integer that does not belong to the array. For instance:

- The MEX of $[2, 2, 1]$ is $0$, because $0$ does not belong to the array.
- The MEX of $[3, 1, 0, 1]$ is $2$, because $0$ and $1$ belong to the array, but $2$ does not.
- The MEX of $[0, 3, 1, 2]$ is 4 because $0, 1, 2$ and $3$ belong to the array, but $4$ does not.

Find the maximum possible MEX of an array of non-negative integers such that the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the elements in the array does not exceed $X$.

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains a single integer $X$ on a single line.

---

## Output Format

For each test case, output on a single line the maximum possible MEX of the array satisfying the given property.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
0
1
2
5
```

**Output**

```text
1
2
2
4
```

**Explanation**

**Test case $1$:** The array could be $[0]$.

**Test case $2$:** The array could be $[0, 1]$. Here the bitwise OR of $0$ and $1$ is $1$ and the MEX of the array is $2$ as both $0$ and $1$ belongs to the array.

**Test case $4$:** The array could be $[1, 0, 3, 2]$. Here the bitwise OR of all integers in the array is $3$ and the MEX of the array is $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/OCT21A/problems/MEXOR)

[Contest Division 2](https://www.codechef.com/OCT21B/problems/MEXOR)

[Contest Division 3](https://www.codechef.com/OCT21C/problems/MEXOR)

[Practice](https://www.codechef.com/problems/MEXOR)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Bitwise Operators

#
[](#problem-4)PROBLEM

The *MEX* (minimum excluded) of an array is the smallest non-negative integer that does not belong to the array. For instance:

- The MEX of [2, 2, 1] is 0 because 0 does not belong to the array.

- The MEX of [3, 1, 0, 1] is 2, because 0 and 1 belong to the array, but 2 does not.

- The MEX of [0, 3, 1, 2] is 4 because 0, 1, 2 and 3 belong to the array, but 4 does not.

Find the maximum possible MEX of an array of non-negative integers such that the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the elements in the array does not exceed X.

#
[](#quick-explanation-5)QUICK EXPLANATION

- If the maximum possible MEX is M, then the chosen array would be [0, M-1] and have bitwise OR not exceeding X, but array [0, M] would have bitwise OR exceeding X.

- The bitwise OR changes only at powers of 2.

- The maximum possible MEX is the largest power of 2 not exceeding X+1.

#
[](#explanation-6)EXPLANATION

**Observation 1**: In order to have MEX M, the array needs to contain elements in the range [0, M-1]. It doesn’t help to add any values larger than M, as they do not contribute to increasing MEX.

Hence, if the maximum possible MEX is M, then the array would be [0, M-1]. We need to find the largest M such that bitwise OR of range [0, M-1] does not exceed X.

**Observation 2**: The bitwise OR of range [0, N-1] is not equal to the bitwise OR of range [0, N] only when N is the power of 2.

**Proof**: Let’s assume N is not a power of 2. We can write N as sum of powers of 2. For example, N = 13 can be written as 8+4+1. Now, since 1,4,8 \lt 13, all these elements are already included in range [0, N-1] = [0, 12], So adding 13 to array doesn’t change bitwise OR.

Hence, bitwise OR changes only when a power of 2 is added to the array.

So, consider the powers of 2 in increasing order. You would not need to consider more than log_2(X)+1 powers of 2. Find the smallest power of 2 which would raise the bitwise OR  above X. This power of 2 is the required answer since we cannot add it to the array.

For example, if we have X = 6, we can add 1 and 2 into the array getting OR 3, but we cannot add 4 making OR 7 which exceeds 6. Hence, 4 is the required answer.

###
[](#alternate-implementation-7)Alternate implementation

You can also run a binary search in the range [0, X] and write a helper function, which finds bitwise OR of first N integers. My solution uses this implementation. The time complexity of this approach is O(log^2(X)) per test case.

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(log_2(X)) per test case.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
template <class T> ostream &operator << (ostream &os, const vector<T> &p) { os << "["; for (auto&it : p) os << it << " "; return os << "]";}
template <class S, class T> ostream &operator << (ostream &os, const pair<S, T> &p) { return os << "(" << p.first << "," << p.second << ")";}
#ifndef ONLINE_JUDGE
#define deb(...) dbs(#__VA_ARGS__,__VA_ARGS__)
template <class T> void dbs(string str, T t) { cerr << str << ":" << t << "\n";}
template<class T, class...S> void dbs(string str, T t, S... s) { int idx = str.find(','); cerr << str.substr(0, idx) << ":" << t << ","; dbs(str.substr(idx + 1), s...);}
#else
#define deb(...){}
#endif

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

      assert(!(cnt > 19 || ( cnt == 19 && fi > 1) ));
    } else if (g == endd) {
      if (is_neg) {
        x = -x;
      }
      // deb(l, r, x);
      assert(l <= x && x <= r);
      // deb(l, r, x);
      return x;
    } else {
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
///////////////////////////////////////////////////////////////////////

#define int long long
template<class T> inline T Bit(T x, int i) { return (x >> i) & 1;}
bool pow2(int i) { return i && (i & -i) == i;}

void solve() {
  int n = readIntLn(0, 1000000000);
    for (int i = 29; i >= 0; i--) {
      if (Bit(n + 1, i)) {
        cout << (1LL << i) << '\n';
        break;
      }
    }
}

signed main() {
  ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t = readIntLn(1, 100000);
  while (t--) {
    solve();
  }
  assert(getchar() == -1);
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
    int T = readIntLn(1, 100'000);
    forn(tc, T)
    {
	    int x = readIntLn(0, 1'000'000'000);
	    fore(i,1, 30)
	    {
		    int cand = (1 << i) - 1;
		    if (cand > x)
		    {
			    int res = (1 << (i-1));
			    printf("%d\n", res);
			    break;
		    }
	    }
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class MEXOR{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        long X = nl();
        long lo = 0, hi = X;
        while(lo < hi){
            long mid = lo+(hi-lo+1)/2;
            long OR = computeOR(mid);
            if(OR <= X)lo = mid;
            else hi = mid-1;
        }
        pn(lo+1);
    }
    //Computes bitwise OR of all integers in range [0, N]
    long computeOR(long n){
        long OR = 0;
        for(long p = 1; p <= n; p *= 2)OR |= p;
        return OR;
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
        new MEXOR().run();
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
