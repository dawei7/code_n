# Digit Removal

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIGITREM |
| Difficulty Rating | 1754 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [DIGITREM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/DIGITREM) |

---

## Problem Statement

You are given an integer $N$ and a digit $D$. Find the minimum non-negetive integer you should add to $N$ such that the final value of $N$ does not contain the digit $D$.

---

## Input Format

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains two integers $N$ and $D$ on a single line denoting the original number and the digit you need to avoid.

---

## Output Format

For each test case, output on a single line the minimum non-negetive integer you should add to $N$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq D \leq 9$

---

## Examples

**Example 1**

**Input**

```text
5
21 5
8 8
100 0
5925 9
434356 3
```

**Output**

```text
0
1
11
75
5644
```

**Explanation**

**Test case $1$:** $N = 21$ does not contain the digit $D = 5$. Hence there is no need to add any integers to $N$.

**Test case $2$:** If $1$ is added to $N = 8$, it becomes equal to $9$, which does not contain the digit $D = 8$.

**Test case $3$:** The minimum integer you should add to $N = 100$ such that the final value of $N$ does not contain the digit $D = 0$ is $11$.

**Test case $5$:** The minimum integer which is greater than $434356$ and does not contain the digit $D = 3$ is $440000$. So we should add $440000 - 434356 = 5644$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
21 5
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
8 8
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
100 0
```

**Output for this case**

```text
11
```



#### Test case 4

**Input for this case**

```text
5925 9
```

**Output for this case**

```text
75
```



#### Test case 5

**Input for this case**

```text
434356 3
```

**Output for this case**

```text
5644
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/OCT21A/problems/DIGITREM)

[Contest Division 2](https://www.codechef.com/OCT21B/problems/DIGITREM)

[Contest Division 3](https://www.codechef.com/OCT21C/problems/DIGITREM)

[Practice](https://www.codechef.com/problems/DIGITREM)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Basic Math.

#
[](#problem-4)PROBLEM

You are given an integer N and a digit D. Find the minimum non-negetive integer you should add to N such that the final value of N does not contain the digit D.

#
[](#quick-explanation-5)QUICK EXPLANATION

- We need to find the smallest integer T \geq N such that D is not present in T. T-N is the required number of operations.

- Consider digits from right to left. If current digit is D, increase it to D+1 and make all digits to the right equal to 0 (or 1 if D = 0)

#
[](#explanation-6)EXPLANATION

For now, let’s ignore D = 0 case. Assuming 1 \leq D \leq 9.

Let’s say we get N = 5925 and D = 9. Third digit from the right is equal to D, so we need to change that digit. By adding anything less than 75, that digit remains unchanged.

We can observe that we need to increase 59XX to 60XX where each X may be replaced by any digit. Since we want to minimize T, it’d be optimal to choose T = 6000. The number of operation would be 100-XX, which in above case was 100-25 = 75.

So, we can see that as soon as we get a digit equal to D, we need to increase that by one and make all digits to its right equal to 0.

Now, we can consider digits either from left to right or right to left.

Consider N = 88888889 and D = 9. The smallest T here is 100000000. If we consider digits from left to right, as soon as we hit 9, we would again need to consider all digits to left of 9.

The reason this happened was due to carry forward. It is handled easier when considering digits from right to left, as addition happens from right to left.

Hence, considering digits from right to left, as soon as we hit a digit D, make that digit D+1 (If D = 9, make it 0 and increase digit to its immediate left by 1.

Specifically, starting from T = N, if x-th digit from right (numbered from 0) is equal to D, add 10^x - T \bmod 10^x. When we had N = 5925 and D = 9, we have x = 2, so we add 10^2 - (5925 \bmod 100) = 100-25 = 75 to T. Repeat this process till there’s no occurrence of D in T.

###
[](#when-d-0-7)When D = 0

In this case, we cannot make digits to the right 0. So the smallest choice we have is making digits to its right equal to 1.

Let’s say we get N = 5025 and D = 0, the smallest integer T is 5111.

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(log_{10} (N)) per test case.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;
template <class T> ostream &operator << (ostream & os, const vector<T> &p) { os << "["; for (auto&it : p) os << it << " "; return os << "]";}
template <class S, class T> ostream &operator << (ostream & os, const pair<S, T> &p) { return os << "(" << p.first << "," << p.second << ")";}
#ifndef ONLINE_JUDGE
#define deb(...) dbs(#__VA_ARGS__,__VA_ARGS__)
template <class T> void dbs(string str, T t) { cerr << str << ":" << t << "\n";}
template<class T, class...S> void dbs(string str, T t, S... s) { int idx = str.find(','); cerr << str.substr(0, idx) << ":" << t << ","; dbs(str.substr(idx + 1), s...);}
#else
#define deb(...){}
#endif
#define int long long
#define fi first
#define se second
#define pb push_back
#define sz(x) (int)x.size()
#define all(x) x.begin(), x.end()
#define ini(x, y) memset(x, y, sizeof(x))
#define pr(x) {cout << x << '\n'; return;}
#define nl cout<< '\n'
#define rep(i,n) for(int i = 0; i < n; i++)
#define re(i,n) for(int i = 1; i <= n; i++)
#define vi vector<int>
#define pii pair<int, int>
#define vii vector<pii>
template<class T> inline T Bit(T x, int i) { return (x >> i) & 1;}
template<class T> bool umin(T & a, T b) { return a > b ? (a = b, true) : false; }
template<class T> bool umax(T & a, T b) { return a < b ? (a = b, true) : false; }
const int N = 1e3 + 3; // check the limits

int greedy(int n, int d) {
  if (n == d) return 1;
  string s = to_string(n);
  int len = sz(s);
  int pos = n;
  int num = 1;
  for (int i = 0; i < len; i++) {
    if (s[i] == '0' + d) {
      if (d == 9 && i >= 1 && s[i - 1] == '8') {
        int p2 = i - 1;
        for (int j = i - 1; j >= 0; j--) {
          if (s[j] == '8') p2 = j;
          else break;
        }
        for (int j = p2; j < len; j++) {
          num *= 10;
        }
        int dig = 0;
        for (int j = p2; j < len; j++) {
          dig = dig * 10 + (s[j] - '0');
        }
        // deb(num, dig);
        return (num - dig);
        break;
      }
      if (d == 0) {
        for (int j = i + 1; j < len; j++) {
          num = num * 10 + 1;
        }
        int dig = 0;
        for (int j = i + 1; j < len; j++) {
          dig = dig * 10 + (s[j] - '0');
        }
        return (num - dig);
      }
      pos = i;
      for (int j = i + 1; j < len; j++) {
        num *= 10;
      }
      int dig = 0;
      for (int j = i + 1; j < len; j++) {
        dig = dig * 10 + (s[j] - '0');
      }
      return (num - dig);
      break;
    }
  }
  return 0;
}

void solve(int tc) {
  int n, d; cin >> n >> d;
  cout << greedy(n, d) << '\n';
}

signed main() {
  ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t = 1;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    solve(i);
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

vector<int> getDigits(int N)
{
    vector<int> res;
    while (N)
    {
	    res.push_back(N % 10);
	    N /= 10;
    }
    return res;
}

int calcDigits(const vector<int>& v)
{
    int res = 0;
    int mul = 1;
    for (const auto& vi : v)
    {
	    res += vi * mul;
	    mul *= 10;
    }
    return res;
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
    vector<int> w(10,1);
    fore(i, 1, w.size() - 1)
    {
	    w[i] = w[i - 1] * 10;
    }

    forn(tc, T)
    {
	    int N = readIntSp(1, 1'000'000'000);
	    int d = readIntLn(0, 9);
	    int NN = N;
	    while (true)
	    {
		    auto nd = getDigits(NN);
		    int fd = -1;
		    forn(i, nd.size())
		    {
			    if (nd[i] == d)
				    fd = i;
		    }
		    if (fd != -1)
		    {
			    forn(i, fd)
			    {
				    nd[i] = d == 0 ? 1 : 0;
			    }
		    }
		    else
			    break;
		    NN = calcDigits(nd);
		    if (fd != -1)
			    NN += w[fd];
	    }
	    printf("%d\n", NN - N);
    }
    assert(getchar() == -1);
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class DIGITREM{
    //SOLUTION BEGIN
    Random R = new Random();
    int MX = 10000;
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        long N = nl(), D = nl();
        pn(fast(N, D)-N);
    }
    long fast(long N, long D){
        long T = N;
        long add0 = 0;
        for(long pw10 = 1; pw10 <= 1000000000000000L; pw10 *= 10){
            if(T/pw10 == 0)break;
            long d = (T/pw10)%10;
            if(d == D){
                long num = (T/pw10+1)*pw10 + (D == 0?add0:0);
                T = num;
            }
            add0 += pw10;
        }
        return T;
    }
    boolean contains(long N, long d){

        while(N>0){
            if(N%10 == d)return true;
            N /= 10;
        }
        return false;
    }
    long brute(long N, long D){
        while(contains(N, D))N++;
        return N;
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
        new DIGITREM().run();
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
