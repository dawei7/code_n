# Subarray XOR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUB_XOR |
| Difficulty Rating | 1757 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUB_XOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUB_XOR) |

---

## Problem Statement

Mary loves binary strings.
Given a binary string $S$, she defines the *beauty* of the string as the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of **decimal representations** of **all substrings** of $S$.

Find the *beauty* of string $S$. Since the answer can be huge, print it modulo $998244353$.

For example, the decimal representation of binary string $1101$ is $1\cdot 2^3 + 1\cdot 2^2 + 0\cdot 2^1 + 1\cdot 2^0 = 8 + 4 + 0+1 = 13$. Kindly refer sample explanation for more such examples.

A string $A$ is a substring of a string $B$ if $A$ can be obtained from $B$ by deleting several (possibly zero) characters from the beginning and several (possibly zero) characters from the end.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of test cases follow.
- First line of each test case contains one integer $N$ - the length of the binary string.
- Second line of each test case contains the binary string $S$.

---

## Output Format

For each test case, output in a single line, beauty of the string modulo $998244353$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
2
10
3
101
4
1111
```

**Output**

```text
3
6
12
```

**Explanation**

**Test Case $1$:** All substrings of the string $S = 10$ are $[1, 0, 10]$. The decimal representation of these substrings is denoted by the array $[1, 0, 2]$. Bitwise XOR of all these values is $1 \oplus 0 \oplus 2 = 3$.

**Test Case $2$:** All substrings of the string $S = 101$ are $[1, 0, 1, 10, 01, 101]$. The decimal representation of these substrings is denoted by the array $[1, 0, 1, 2, 1, 5]$. Bitwise XOR of all these values is: $1 \oplus 0 \oplus 1 \oplus 2 \oplus 1 \oplus 5 = 6$.

**Test Case $3$:** All substrings of the string $S = 1111$ are $[1, 1, 1, 1, 11, 11, 11, 111, 111, 1111]$. The decimal representation of these substrings is denoted by the array $[1, 1, 1, 1, 3, 3, 3, 7, 7, 15]$. Bitwise XOR of all these values is: $1 \oplus 1 \oplus 1 \oplus 1 \oplus 3 \oplus 3 \oplus 3 \oplus 7 \oplus 7 \oplus 15 = 12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
10
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
101
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
4
1111
```

**Output for this case**

```text
12
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/MARCH221A/problems/SUB_XOR)

[Contest Division 2](https://www.codechef.com/MARCH221B/problems/SUB_XOR)

[Contest Division 3](https://www.codechef.com/MARCH221C/problems/SUB_XOR)

[Contest Division 4](https://www.codechef.com/MARCH221D/problems/SUB_XOR)

[Practice](https://www.codechef.com/problems/SUB_XOR)

**Setter:** [Aryan Raj](https://www.codechef.com/users/rajaryan123)

**Testers:** [Tejas Pandey](https://www.codechef.com/users/tejas10p) and [Abhinav sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Bitwise operations, prefix sums, [Contribution trick](https://codeforces.com/blog/entry/62690)

#
[](#problem-4)PROBLEM

Given a binary string S of length N, find the beauty of string S, which is defined as the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of **decimal representations** of **all substrings** of S.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Consider each occurrence of 1 separately, and consider its contribution to XOR.

- For a 1 at position p (0-based) in S, it will be included in (1+p)*(|S|-p) substrings.

- This 1 will appear at 0-th position in (1+p) substrings, at 1-st position in (1+p) substrings, \ldots, at (|S|-p+1)-th position in (1+p) substrings.

- We can maintain the total number of substrings containing ON bit at position x for each x using the difference array, and compute its prefix sum.

- In the final XOR, only those bits would be ON, which have an odd number of substrings having ON bit at that position.

#
[](#explanation-6)EXPLANATION

Since XOR operation is applied on bits and the string is also in binary, we shall solve the whole problem in binary to find the binary representation of the answer and then finally compute its decimal value modulo 998244353.

For some 0 \leq p \leq N-1, p-th bit in final XOR would be ON if and only if there are an odd number of substrings having p-th bit ON. So, if we can compute for each p, the number of substrings of S having p-th bit ON, we get the binary representation of the answer.

###
[](#reduced-problem-7)Reduced problem

Now, the problem is to count the number of substrings of S, which have p-th bit on for all 0 \leq p \lt |S|. Let’s denote this count as cnt_p.

Now, let’s consider each ON bit in S, and find its contribution to cnt_p. Let’s assume we have position c with S_c = 1. Firstly, position c is included in exactly (1+c)*(|S|-c) substrings of S (We have (1+c) choices for left end, and (|S|-c) choices for right end).

For example, considering string `101000` and c = 2, there are 3 substrings where S_2 appears at lowest bit (right end at 2), 3-substrings with S_2 appearing at second lowest bit (right end at 3) and so on.

We can see that for position c and right end of substring r, it contributes (1+c) substrings to cnt_{r-c}. The right end r can take values c \leq r \lt |S|. Hence, if c-th character in S is ON, it shall contribute (1+c) substrings to all cnt_{r-c} for c \leq r \lt N.

But naively updating each cnt_{r-c} for all pairs (r, c) would take |S|^2 time, which would time out, we need something faster.

###
[](#standard-problem-8)Standard problem

We need to increase cnt_{x} for all 0 \leq x \lt |S|-c for a some set of positions, and then compute the final array cnt. We need to perform a range increment operation here.

We can use [difference arrays](https://www.geeksforgeeks.org/difference-array-range-update-query-o1/), supporting this operation in O(1), or segment tree supporting this in O(log_2(N)).

Taking the prefix/suffix sum (depending upon implementation) will recover the original cnt array, using which, the final answer can be computed.

If in doubt, refer to my solution with comments mentioning each step.

#
[](#time-complexity-9)TIME COMPLEXITY

The time complexity is O(|S|) per test case.

#
[](#solutions-10)SOLUTIONS

Setter's Solution
``// author: Aryan Raj
#include "bits/stdc++.h"
using namespace std;
#define int   long long int
#define mod   998244353

signed main()
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t, n;
  cin >> t;
  while (t--)
  {
    string s;
    cin >> n >> s;
    vector<int> cnt(n);
    for (int i = 0; i < n; ++i)
      if (s[i] == '1')cnt[n - i - 1] += (i + 1);

    for (int j = n - 2; j >= 0; --j)
      cnt[j] += cnt[j + 1];

    int ans = 0, cur = 1;
    for (int i = 0; i < n; ++i)
    {
      if (cnt[i] % 2)
        ans = (ans + cur) % mod;
      cur = (cur * 2) % mod;
    }
    cout << ans << "\n";
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
const int MAX_N = 100000;
const int MAX_SUM_N = 200000;
const int mod = 998244353;

#define ll long long int
#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

long long int sum_len=0;

ll mpow(ll a, ll b) {
    ll res = 1;
    while(b) {
        if(b&1) res *= a, res %= mod;
        a *= a;
        a %= mod;
        b >>= 1;
    }
    return res;
}

void solve()
{
    int n = readIntLn(1, MAX_N);
    sum_len += n;
    assert(sum_len <= MAX_SUM_N);
    string s = readStringLn(n, n);
    ll mv = mpow(2, n - 1), inv = mpow(2, mod - 2);
    ll cnt = 0, ans = 0;
    for(int i = 0; i < n; i+=2) {
        if(s[i] - '0') cnt ^= 1;
        if(cnt) {
            ans += mv;
            ans %= mod;
            mv *= inv;
            mv %= mod;
            if(i + 1 < n) {
                ans += mv;
                ans %= mod;
                mv *= inv;
                mv %= mod;
            }
        } else {
            mv *= inv;
            mv %= mod;
            mv *= inv;
            mv %= mod;
        }
    }
    cout << ans << "\n";
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

    int n = readIntLn(1,1e5);
    sum_n+=n;
    max_n = max(max_n, n);

    string s = readStringLn(n,n);
    for(auto h:s) assert(h=='0' || h=='1');

    ll df[n] = {0};

    rep(i,n){
        if(s[i]=='1'){
            df[n-1-i]+=i+1;
        }
    }

    rev(i,n-2) df[i]+=df[i+1];

    ll ans = 0;
    rep(i,n){
        if(df[i]&1) ans+=po(2,i);
    }

    ans%=mod;
    cout<<ans<<'\n';
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
    assert(sum_n<=2e5);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<'\n';
    cerr<<"Maximum length : " << max_n <<'\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution (with comments)
``import java.util.*;
import java.io.*;
class SUB_XOR{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        char[] C = n().toCharArray();
        long[] cnt = new long[N];
        for(int i = 0; i< N; i++)
            if(C[i] == '1')
                cnt[N-i-1] += (1+i);//Adding contribution of on bits

        for(int i = N-2; i>= 0; i--)cnt[i] += cnt[i+1]; // Taking suffix sum to recover cnt

        //Converting cnt to decimal number
        long ans = 0, f = 1, MOD = 998244353;
        for(int i = 0; i< N; i++){
            cnt[i] %= 2; // Only the parity of count matters
            ans += f*cnt[i]%MOD;
            if(ans >= MOD)ans -= MOD;
            f = (f*2)%MOD;
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
        new SUB_XOR().run();
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
