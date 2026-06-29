# Array Filling

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRFILL |
| Difficulty Rating | 1887 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [ARRFILL](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/ARRFILL) |

---

## Problem Statement

You are given an array $A$ of size $N$. Initially, the array is filled with $0$-s.

There are $M$ types of operations that you can perform on array $A$. The $i^{th}$ operation can be described by two integers $(x_i, y_i)$. In this operation, you choose a set of indices $S$ such that

- $1 \leq j \leq N$,
- $(j \bmod y_i) \neq 0$,
- $A_j = 0$,

, then you set $A_j = x_i$ for all $j \in S$.

You can perform the operations in any order, but one type of operation can't be done more than once. What is the maximum sum of integers of the array $A$ you obtain if you perform the $M$ operations optimally?

For example, consider the array $A = [0, 0, 0, 0]$.
- Suppose $x = 3, y = 2$. Here you can choose indices $1$ and $3$ and set $A_1 = A_3 = 3$. So the array A becomes $[3, 0, 3, 0]$. In this operation you can't choose the indices $2$ and $4$ because $(2 \bmod 2) = 0$, $(4 \bmod 2) = 0$.
- Suppose $x = 5, y = 3$ and you set $A_2 = 5$. So the array $A$ becomes $[3, 5, 3, 0]$. Here you can't choose index $1$ because $A_1 \gt 0$ and index $3$ because $(3 \bmod 3) = 0$ and $A_3 \gt 0$. However, you could also set $A_4 = 5$.

- Suppose $x = 4, y = 4$. Now you can't choose any index because $A_j \gt 0$  for all $1 \leq j \leq 3$ and $(4 \bmod 4) = 0$. So the array remains same.

**Note:** Since input-output is large, prefer using fast input-output methods.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each testcase contains $M + 1$ lines of input.
- The first line of each test case contains two space-separated integers $N, M$.
- $M$ lines follow. For each valid $i$, the $i^{th}$ of these lines contains two space-separated integers $x_i, y_i$ - parameters of the $i^{th}$ operation.

---

## Output Format

For each test case, output in a single line the maximum sum of integers of the array $A$ after $M$ operations.

---

## Constraints

- $1 \leq T \leq 12600$
- $1 \leq N \leq 10^9$
- $1 \leq M \leq 10^5$
- $1 \leq x_i \leq 10^9$
- $2 \leq y_i \leq 10^9$
- The sum of $M$ over all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
3
10 1
5 2
8 2
5 2
6 3
3 2
2 2
1 3
```

**Output**

```text
25
41
5
```

**Explanation**

**Test case $1$:** Optimal filling is $[5, 0, 5, 0, 5, 0, 5, 0, 5, 0]$.

**Test case $2$:** Optimal filling is $[6, 6, 5, 6, 6, 0, 6, 6]$.

**Test case $3$:** Optimal filling is $[2, 1, 2]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/AUG21A/problems/ARRFILL)

[Contest Division 2](https://www.codechef.com/AUG21B/problems/ARRFILL)

[Contest Division 3](https://www.codechef.com/AUG21C/problems/ARRFILL)

[Practice](https://www.codechef.com/problems/ARRFILL)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Basic Number Theory

#
[](#problem-4)PROBLEM

Given an array A of length N filled with 0, you can apply given M operations in any order so as to maximize the sum of integers in the array A after all operations are applied.

An operation is described by two integers (x_i, y_i). In one operation, choose a subset of indices S such that

- 1 \leq j \leq N

- j \bmod y_i \neq 0

-
A_j = 0

Then update A_j = x_i for all j \in S

#
[](#quick-explanation-5)QUICK EXPLANATION

- Apply operations in non-increasing order of x_i, so that if a position can be chosen, it should be chosen immediately.

- After each operation, the set of positions j such that A_j = 0 are multiples of a constant value.

- If multiples of C are the positions containing 0 and we apply operation (x_i, y_i), then after this operations, multiples of lcm(C, y_i) would be the positions containing 0

#
[](#explanation-6)EXPLANATION

Since we need to maximize the sum of operations, It would be optimal to apply operations at all positions where it is possible.

###
[](#only-two-operations-7)Only two operations

Let’s assume M = 2 for now. The two operations are (x_1, y_1) and (x_2, y_2). A position p such that 1 \leq p \leq N shall fall into only one of the following cases

-
p \bmod y_1 = 0 and p \bmod y_2 = 0: Neither operation can cover position p, So A_p = 0 after operations

-
p \bmod y_1 = 0 and p \bmod y_2 \neq 0: Second operation can cover position p, So A_p = x_2 after operations

-
p \bmod y_1 \neq 0 and p \bmod y_2 = 0: First operation can cover position p, So A_p = x_1 after operations

-
p \bmod y_1 \neq 0 and p \bmod y_2 \neq 0: Both operations can cover position p, So, we shall apply operation with higher x first, leading to A_p = max(x_1, x_2) after operations

Assuming x_1 \geq x2, last two cases lead to A_p = x_1. So, we can merge the two cases, just checking if p \bmod y_1 \neq 0.

This way, assuming x_1 \geq x_2, we divide positions into three groups

- p \bmod y_1 \neq 0

-
p \bmod y_1 = 0 and p \bmod y_2 \neq 0

-
p \bmod y_1 = 0 and p \bmod y_2 = 0 which implies p \bmod lcm(y_1, y_2) = 0

###
[](#original-problem-8)Original Problem

Now we have many operations, but we can generalize the whole thing.

Let’s consider the operations in non-increasing order of x. This way, we can see that if we can pick position p in some earlier operation, we must pick it in an earlier operation.

Specifically, for position p, if operation q is the first operation where position p can be picked, then we can see that p \bmod y_q \neq 0 and p \bmod y_r = 0 for all r \lt q. Second condition can be written as p \bmod \text{lcm}_{r \lt q}{ y_r } = 0.

If we want to write cases like M = 2 case, we can divide it into M+1 cases, after sorting operations by x

-
p \bmod y_1 \neq 0 leads to A_p = x_1

-
p \bmod y_1 = 0 and p \bmod y_2 \neq 0 leads to A_p = x_2

-
p \bmod lcm(y_1, y_2) = 0 and p \bmod y_3 \neq 0 leads to A_p = x_3

…

-
p \bmod \text{lcm}_{r \lt M}{y_r} = 0 and p \bmod y_M \neq 0 leads to A_p = x_M

-
p \bmod \text{lcm}_{r \lt M}{y_r} = 0 leads to A_p = 0

**Observation:** After each operation, the set of empty positions shall be positions p such that p \bmod z_i = 0, if \displaystyle z_i = \text{lcm}_{j < i} (y_j)

**Example**

Consider N = 10 and operations (5,2), (6,3)

Initially [0,0,0,0,0,0,0,0,0,0]

After operation (6, 3), array becomes [6,6,0,6,6,0,6,6,0,6]. All empty positions are multiples of 3

After operation (5,2), array becomes [6,6,5,6,6,0,6,6,5,6]. All empty positions are multiples of 6 = lcm(3, 2) = 6

Hence, after each operation, we can represent all empty positions in A as multiples of a constant value.

###
[](#computing-the-sum-of-array-9)Computing the sum of array

Now we know the order of operations. We also know that before some operation (x, y), only the positions which are multiples of z are empty for some z. We want to figure out how many positions the current operation is applied to.

Before current operation, \displaystyle \left \lfloor \frac{N}{z} \right \rfloor positions are empty. After current operation, \displaystyle \left \lfloor \frac{N}{lcm(z, y)} \right \rfloor positions are empty. Hence, current operation is applied at \displaystyle \left \lfloor \frac{N}{z} \right \rfloor - \left \lfloor \frac{N}{lcm(z, y)} \right \rfloor positions, contributing sum \displaystyle \left( \left\lfloor \frac{N}{z} \right \rfloor - \left \lfloor \frac{N}{lcm(z, y)} \right \rfloor \right ) * x.

Hence, if we maintain LCM after each operation, we have solved the problem. To make sure lcm doesn’t overflow, we can see that as soon as z \gt N, all positions in the array are filled, so we can stop applying operations.

#
[](#time-complexity-10)TIME COMPLEXITY

The time complexity is O(M*log(M)) per test case.

#
[](#solutions-11)SOLUTIONS

Setter's Solution
``#include<bits/stdc++.h>
# define pb push_back
#define pii pair<int, int>
#define mp make_pair
# define ll long long int

using namespace std;

const int maxm = 1e5, maxtm = 1e6, maxx = 1e9, maxy = 1e9, maxn = 1e9;
vector<pii> v;
int main()
{
    ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    int t; cin >> t;
    int tm = 0;
    int maxitr = 0;
    ll n; int m;
    int x, y;
    while(t--){
        v.clear();
        cin >> n >> m;
        tm += m;
        for(int i = 0; i < m; i++){
            cin >> x >> y;
            v.pb({x, y});
        }
        sort(v.begin(), v.end(), greater<pii>());
        int itr = 0;
        ll d = 1, ans = 0, S = n;
        for(pii p : v){
            if(d <= n)d = (d * p.second) / __gcd(d, (ll)p.second);
            ans += p.first * (S - n / d); S = n / d;
            itr++;
            if(S == 0)break;
        }
        maxitr = max(maxitr, itr);
        cout << ans << endl;
    }
    assert(tm <= maxtm);
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

uint32_t gcd(uint32_t a, uint32_t b)
{
    return b ? gcd(b, a % b) : a;
}

uint64_t lcm(uint32_t a, uint32_t b)
{
    return static_cast<uint64_t>(a) * b / gcd(a,b);
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
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    forn(tc, T)
    {
	    uint32_t N, M;
	    cin >> N >> M;
	    vector<pair<uint32_t, uint32_t>> V(M);
	    for (auto& vi : V)
	    {
		    cin >> vi.first >> vi.second;
	    }
	    sort(V.begin(), V.end());
	    reverse(V.begin(), V.end());
	    uint64_t res = 0;
	    uint64_t g = 1;
	    for(const auto & vi: V)
	    {
		    const auto x = vi.first;
		    const auto y = vi.second;
		    if (g <= N)
		    {
			    const auto prevG = g;
			    g = lcm(g, y);
			    res += x * (N / prevG - N / g);
		    }
	    }
	    cout << res << endl;
    }
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class ARRFILL{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), M = ni();
        int[][] op = new int[M][];
        for(int i = 0; i< M; i++)op[i] = new int[]{ni(), ni()};
        //Sorting operations by x
        Arrays.sort(op, (int[] i1, int[] i2) -> Integer.compare(i2[0], i1[0]));
        long lcm = 1;
        long ans = 0;
        for(int[] o:op){
            long nlcm = lcm(lcm, o[1]);
            ans += o[0]* (N/lcm - N/nlcm);
            lcm = nlcm;
            if(nlcm > N)break;
        }
        pn(ans);
    }
    long gcd(long a, long b){return b == 0?a:gcd(b, a%b);}
    long lcm(long a, long b){return a * (b/gcd(a, b));}
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
        new ARRFILL().run();
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
