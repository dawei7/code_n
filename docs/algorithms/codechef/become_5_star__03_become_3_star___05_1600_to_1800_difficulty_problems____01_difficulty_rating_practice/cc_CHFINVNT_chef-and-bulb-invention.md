# Chef and Bulb Invention

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFINVNT |
| Difficulty Rating | 1607 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [CHFINVNT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/CHFINVNT) |

---

## Problem Statement

Chef is trying to invent the light bulb that can run at room temperature without electricity. So he has $N$ gases numbered from $0$ to $N - 1$ that he can use and he doesn't know which one of the $N$ gases will work but we do know it.

Now Chef has worked on multiple search algorithms to optimize search. For this project, he uses a modulo-based search algorithm that he invented himself. So first he chooses an integer $K$ and selects all indices $i$ in increasing order such that $i \bmod K = 0$ and test the gases on such indices, then all indices $i$ in increasing order such that $i \bmod K = 1$, and test the gases on such indices, and so on.

Given $N$, the index of the gas $p$ that will work, and $K$, find after how much time will he be able to give Chefland a new invention assuming that testing $1$ gas takes $1$ day.

For example, consider $N = 5, p = 2$ and $K = 3$.
- On the $1^{st}$ day, Chef tests gas numbered $0$ because $0 \bmod 3 = 0$.
- On the $2^{nd}$ day, Chef tests gas numbered $3$ because $3 \bmod 3 = 0$.
- On the $3^{rd}$ day, Chef tests gas numbered $1$ because $1 \bmod 3 = 1$.
- On the $4^{th}$ day, Chef tests gas numbered $4$ because $4 \bmod 3 = 1$.
- On the $5^{th}$ day, Chef tests gas numbered $2$ because $2 \bmod 3 = 2$.

So after $5$ days, Chef will be able to give Chefland a new invention

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains three space-separated integers $N$, $p$, and $K$.

---

## Output Format

For each test case, print a single line containing one integer — after how much time Chef will be able to give Chefland a new invention assuming that testing $1$ gas takes $1$ day.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, K \leq 10^9$
- $0 \leq p < N$

---

## Examples

**Example 1**

**Input**

```text
4
10 5 5
10 6 5
10 4 5
10 8 5
```

**Output**

```text
2
4
9
8
```

**Explanation**

**Test case $1$:** On the day $1$ Chef will test gas numbered $0$ and on the day $2$ Chef will test gas numbered $5$.

**Test case $2$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, and on the day $4$ Chef will test gas numbered $6$.

**Test case $3$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, on the day $4$ Chef will test gas numbered $6$, on the day $5$ Chef will test gas numbered $2$, on the day $6$ Chef will test gas numbered $7$, on the day $7$ Chef will test gas numbered $3$, on the day $8$ Chef will test gas numbered $8$, and on the day $9$ Chef will test gas numbered $4$.

**Test case $4$:** On the day $1$ Chef will test gas numbered $0$, on the day $2$ Chef will test gas numbered $5$, on the day $3$ Chef will test gas numbered $1$, on the day $4$ Chef will test gas numbered $6$, on the day $5$ Chef will test gas numbered $2$, on the day $6$ Chef will test gas numbered $7$, on the day $7$ Chef will test gas numbered $3$, and on the day $8$ Chef will test gas numbered $8$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 5 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
10 6 5
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
10 4 5
```

**Output for this case**

```text
9
```



#### Test case 4

**Input for this case**

```text
10 8 5
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/AUG21A/problems/CHFINVNT)

[Contest Division 2](https://www.codechef.com/AUG21B/problems/CHFINVNT)

[Contest Division 3](https://www.codechef.com/AUG21C/problems/CHFINVNT)

[Practice](https://www.codechef.com/problems/CHFINVNT)

**Setter:** [Souradeep Paul](https://www.codechef.com/users/souradeep1999) and [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Simple

#
[](#prerequisites-3)PREREQUISITES

Basic Math

#
[](#problem-4)PROBLEM

Given N, K and p, there are N gases numbered from 0 to N-1. Chef tries all gases one by one, first trying all gases x with x \bmod K = 0 in increasing order, then all gases with x \bmod K = 1 and so on, trying one gas on each day.

Given an integer p, determine the day on with gas numbered p shall be tried.

#
[](#quick-explanation-5)QUICK EXPLANATION

- Grouping gases x having the same value of x \bmod K, we get K groups, where groups are processed one by one.

- We can find the group in which p is present simply by computing p \bmod K.

- First N \bmod K groups shall have \frac{N}{K}+1 elements, and rest K - N \bmod K groups shall have \frac{N}{K} elements

- We need to count all elements in the first p \bmod K groups and then count the number of gases in the group same as p which are tried before p.

#
[](#explanation-6)EXPLANATION

Let’s consider an example first. Say we have N = 27, K = 5. The gases would be processed in following order

` 0 5 10 15 20 25 1 6 11 16 21 26 2 7 12 17 22 3 8 13 18 23 4 9 14 19 24`

We can divide above into groups bases on x \bmod K. We have

``0: 0 5 10 15 20 25
1: 1 6 11 16 21 26
2: 2 7 12 17 22
3: 3 8 13 18 23
4: 4 9 14 19 24
``

We can see that before processing any element in row r, all elements in rows before r are processed.

Let’s assume given p is in row r. So we need to find the number of elements in rows before row indexed r.

**Observation:** First N \bmod K rows contain \frac{N}{K}+1 elements, and rest K - N \bmod K rows contain \frac{N}{K} elements.

It is intuitive to see it this way. Let’s find C as the largest multiple of K such that C \leq N. In above example, C = 25 = K *\lfloor \frac{N}{K}\rfloor. We can see that dividing the first C gases into K groups contribute \lfloor \frac{N}{K}\rfloor gases in each group evenly. Now, only N \bmod K gases are left, each of which is divided into the first N \bmod K groups.

Hence, first N \bmod K groups have \lfloor \frac{N}{K}\rfloor +1 elements, and rest K - N \bmod K rows have \lfloor \frac{N}{K}\rfloor elements.

For computing the number of elements in the first r rows, we can see that

- if r \leq N \bmod K, then all rows have \lfloor \frac{N}{K}\rfloor+1 elements, leading to \displaystyle r * \left(\left\lfloor \frac{N}{K}\right\rfloor+1\right) elements.

- Otherwise first N \bmod K rows have \lfloor \frac{N}{K}\rfloor+1 elements, and r - N \bmod K rows have \lfloor \frac{N}{K}\rfloor elements, leading to \displaystyle (N \bmod K)* \left (\left \lfloor \frac{N}{K} \right\rfloor+1 \right) + (r - N \bmod K) * \frac{N}{K}

Simplicifation

We can write number of elements in first r rows as r * \left\lfloor\frac{N}{K}\right\rfloor + min(r, N \bmod K), as Each row contributes \left\lfloor\frac{N}{K}\right\rfloor and first min(r, N \bmod K) rows may contribute an additional element.

Hence, if we know row containing p, we can count the number of elements in rows before that row. Also, based on our grouping, we have p appearing in row indexed p \bmod K.

Now, within the current group r, First, r is processed, then K + r is processed, and so on. We want to find the index of p in the current row, which can be computed in the same way as computing the index of a term in AP. Specifically, p is processed at index n, such that n = (p-r)/K+1.

Summarizing, the day on which gas p is processed can be written as \displaystyle (p \bmod K) * \frac{N}{K} + min(p \bmod K, N \bmod K) + \frac{p-p \bmod K}{K} + 1 which can be computed in O(1) time.

#
[](#time-complexity-7)TIME COMPLEXITY

The time complexity is O(1) per test case.

#
[](#solutions-8)SOLUTIONS

Setter's Solution
``#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace std;
using namespace __gnu_pbds;
#define int long long int
#define ordered_set tree<int, nuint_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
mt19937 rng(std::chrono::duration_cast<std::chrono::nanoseconds>(chrono::high_resolution_clock::now().time_since_epoch()).count());
#define mp make_pair
#define pb push_back
#define F first
#define S second
const int N=2005;
#define M 998244353
#define BINF 1e9
#define init(arr,val) memset(arr,val,sizeof(arr))
#define MAXN 501
#define deb(xx) cout << #xx << " " << xx << "\n";
const int LG = 22;

void solve(){

    int n, i, k;
    cin >> n >> i >> k;

    int ex = n % k, ind = i % k;

    int ans = 0;
    if(ind > 0){
        int p = n / k;
        ans += p * ind;
        if(ex > 0){
            ans += min(ex, ind);
        }
    }

    i++;
    ans += (i + k - 1) / k;

    cout << ans << endl;

}

#undef int
int main() {
#define int long long int
ios_base::sync_with_stdio(false);
cin.tie(0);
cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("optput.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    while(t--){
        solve();
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

int solver(int N, int P, int K)
{
    --N;
    int Z = P % K;
    int S = N % K;
    int res = 0;
    if (Z <= S)
    {
	    res += Z * ((N + K) / K);
	    res += (P - Z) / K + 1;
    }
    else
    {
	    res += (S + 1) * ((N + K) / K);
	    res += (Z - S - 1) * ((N + K) / K - 1);
	    res += (P - Z) / K + 1;
    }
    return res;
}

int solverBF(int N, int P, int K)
{
    vector<pair<int,int> > v(N);
    forn(i, N)
	    v[i] = { i % K, i };
    sort(v.begin(), v.end());
    int res = 0;
    forn(i, N)
    {
	    if (v[i].second == P)
		    res = i;
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
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    forn(tc, T)
    {
	    int N, P, K;
 		cin >> N >> P >> K;
 		int res = solver(N, P, K);
 		cout << res << endl;
    }
    return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class CHFINVNT{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni(), p = ni(), K = ni();
        int pInd = p%K;

        int G1 = N%K, G2 = K-G1;
        int S1 = N/K+1, S2 = N/K;
        int ans = -1;
        if(pInd < G1){
            ans = pInd*S1 + p/K;
        }else{
            ans = G1*S1 + (pInd-G1)*S2 + p/K;
        }
        pn(ans+1);
        hold(G1*S1 + G2*S2 == N);
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
        new CHFINVNT().run();
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
