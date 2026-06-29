# Longest AND Subarray

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ANDSUBAR |
| Difficulty Rating | 1502 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [ANDSUBAR](https://www.codechef.com/learn/course/bit-manipulation/BITM05/problems/ANDSUBAR) |

---

## Problem Statement

You are given an integer $N$. Consider the sequence containing the integers $1, 2, \dots, N$ in increasing order (each exactly once). Find the length of the longest subarray in this sequence such that the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of all elements in the subarray is **positive**.

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains a single integer $N$ on a single line.

---

## Output Format

For each test case, output on a single line the length of the longest subarray that satisfy the given property.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5
1
2
3
4
7
```

**Output**

```text
1
1
2
2
4
```

**Explanation**

**Test case $1$**: The only possible subarray we can choose is $[1]$.

**Test case $2$**: We can't take the entire sequence $[1, 2]$ as a subarray because the bitwise AND of $1$ and $2$ is zero. We can take either $[1]$ or $[2]$ as a subarray.

**Test case $4$**: It is optimal to take the subarray $[2, 3]$ and the bitwise AND of $2$ and $3$ is $2$.

**Test case $5$**: It is optimal to take the subarray $[4, 5, 6, 7]$ and the bitwise AND of all integers in this subarray is $4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
4
```

**Output for this case**

```text
2
```



#### Test case 5

**Input for this case**

```text
7
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

[Contest Division 1](https://www.codechef.com/OCT21A/problems/ANDSUBAR)

[Contest Division 2](https://www.codechef.com/OCT21B/problems/ANDSUBAR)

[Contest Division 3](https://www.codechef.com/OCT21C/problems/ANDSUBAR)

[Practice](https://www.codechef.com/problems/ANDSUBAR)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Bitwise Operators

#
[](#problem-4)PROBLEM

You are given an integer N. Consider the sequence containing the integers 1, 2, \dots, N in increasing order (each exactly once). Find the length of the longest subarray in this sequence such that the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) of all elements in the subarray is **positive**.

#
[](#quick-explanation-5)QUICK EXPLANATION

- All elements in the chosen subarray shall have at least one common bit set.

- The most significant bit is the one changing least frequently.

- Split the range [1, N] by the most significant bit. The largest partition is the required subarray.

#
[](#explanation-6)EXPLANATION

Since we want bitwise AND to be positive, we need to choose subarray [L, R] such that all integers in the range L and R have at least one common bit set.

Consider each bit one by one. For some bit, what is the largest range such that all integers in that range have b-th bit set. (The bits are numbered from least significant bit (LSB) to most significant bit (MSB) starting from 0).

**Observation 1**: We can see that integers in the range [0, 2^b-1] don’t have b-th bit set, then all integers in the range [2^b, 2^b + 2^b-1] have b-th bit set and so on.

Specifically, for b = 0, 0 don’t have b-th bit set, then 1 has 0-th bit set, then 2 don’t.

For b = 1, integers in range [0, 1] don’t have 1-th bit set, then [2, 3] has that bit set, then [4,5] don’t and so on.

**Observation 2**: As we move from LSB to MSB, the length of the range having that bit set becomes double.

0-th bit has ranges of length 2^0 = 1

1-th bit has ranges of length 2^1 = 2

2-th bit has ranges of length 2^2 = 4

and so on.

So, it is worthwhile to check only the largest bit in each integer and check the largest subarrays formed, as the length of the subarray would be greater.

For example, we can split range [1, 15] into [1,1], [2,3], [4,7],[8,15] as for each partition, all integers in the same partition have the same largest bit set. Hence, all sub-partitions have non-zero AND. We can simply print the size of the largest sub-partition. For N = 15, we found subarray [8, 15], Hence 8 is the required answer.

For N = 11, partitions are [1,1],[2,3],[4,7], [8,11]. Size of largest sub-partition is 4, so the required subarray length is 4.

We can also see that we cannot extend any of the range without making AND 0, so we cannot have any larger subarray.

**Bonus**

Solve each test case in O(1) if i-th test case has N = i. Specifically, focus on how the answer changes as we solve for N+1 after solving for N.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(log(N)) per test case.

#
[](#solutions-8)SOLUTIONS

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
#define int long long
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
template<class T> inline T Bit(T x, int i) { return (x >> i) & 1;}

void solve() {
    int n = readIntLn(1, 1000000000);
    int ans = 0;
    for (int i = 29; i >= 0; i--) {
	    if (Bit(n, i)) {
		    ans = n - (1LL << i) + 1;
		    if (i >= 1) {
			    ans = max(ans, (1LL << (i - 1)));
		    }
		    break;
	    }
    }
    cout << ans << '\n';
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
	    int N = readIntLn(1, 1'000'000'000);
	    int res = 1;
	    forn(i, 30)
	    {
		    uint32_t a = 1 << i;
		    uint32_t b = min<uint32_t>((1 << (i+1))-1, N);
		    if (a <= N)
		    {
			    res = max<int>(res, b - a + 1);
		    }
	    }
	    printf("%d\n", res);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class ANDSUBAR{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        long N = nl();
        long ans = 0;
        for(long size = 1, upto = 0; upto < N; upto += size, size *= 2){
            long sz = Math.min(size, N-upto);
            ans = Math.max(ans, sz);
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
        new ANDSUBAR().run();
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
