# Special Triplets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SPCTRIPS |
| Difficulty Rating | 1673 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Number Theory - Sieving |
| Official Link | [SPCTRIPS](https://www.codechef.com/practice/course/3to4stars/LP3TO404/problems/SPCTRIPS) |

---

## Problem Statement

Gintoki has been very lazy recently and he hasn't made enough money to pay the rent this month. So the old landlady has given him a problem to solve instead, if he can solve this problem the rent will be waived.
The problem is as follows:

A triplet of integers $(A, B, C)$ is considered to be special if it satisfies the following properties for a given integer $N$ :

- $A \bmod B = C$
- $B \bmod C = 0$
- $1 \le A, B, C \le N$

**Example**: There are three special triplets for $N = 3$.
- $(1, 3, 1)$ is a special triplet, since $(1 \bmod 3) = 1$ and $(3 \bmod 1) = 0$.
- $(1, 2, 1)$ is a special triplet, since $(1 \bmod 2) = 1$ and $(2 \bmod 1) = 0$.
- $(3, 2, 1)$ is a special triplet, since $(3 \bmod 2) = 1$ and $(2 \bmod 1) = 0$.

The landlady gives Gintoki an integer $N$. Now Gintoki needs to find the number of special triplets. Can you help him to find the answer?

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

---

## Output Format

- For each testcase, output in a single line the number of special triplets.

---

## Constraints

- $1 \leq T \leq 10$
- $2 \leq N \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3
4
5
```

**Output**

```text
3
6
9
```

**Explanation**

**Test case $1$**: It is explained in the problem statement.

**Test case $2$**: The special triplets are $(1, 3, 1)$, $(1, 2, 1)$, $(3, 2, 1)$, $(1, 4, 1)$,  $(4, 3, 1)$, $(2, 4, 2)$. Hence the answer is $6$.

**Test case $3$**: The special triplets are $(1, 3, 1)$, $(1, 2, 1)$, $(3, 2, 1)$, $(1, 4, 1)$, $(4, 3, 1)$, $(1, 5, 1)$, $(5, 4, 1)$, $(5, 2, 1)$, $(2, 4, 2)$. Hence the answer is $9$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/AUG21A/problems/SPCTRIPS)

[Contest Division 2](https://www.codechef.com/AUG21B/problems/SPCTRIPS)

[Contest Division 3](https://www.codechef.com/AUG21C/problems/SPCTRIPS)

[Practice](https://www.codechef.com/problems/SPCTRIPS)

**Setter:** [Nishant Raj Lather](https://www.codechef.com/users/nlather)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

#
[](#difficulty-2)DIFFICULTY

Easy

#
[](#prerequisites-3)PREREQUISITES

Knowledge of [Sieve of Eranthoses](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) would be helpful.

#
[](#problem-4)PROBLEM

Given an integer N, find the number of triplets (A, B, C) such that

- A \bmod B = C

- B \bmod C = 0

- 1 \leq A, B, C \leq N

#
[](#quick-explanation-5)QUICK EXPLANATION

- Loop over all pairs (B, C) such that B is a multiple of C. There are O(N*log(N)) such pairs.

- Given N, B and C, we can see that A = x*B+C for some x \geq 0, leading to \displaystyle 0 \leq x \leq \frac{N-C}{B}. Each value of x corresponding to one value of A.

- So for pair (B, C), there are \displaystyle 1 + \frac{N-C}{B} candidates for A, we can sum it over all pairs.

#
[](#explanation-6)EXPLANATION

In most problems involving triplets or tuples, we tend to fix one or more parameters, so that we get a nice formula or a quick way of computing number of candidates for the remaining parameters. The number of candidates of fixed parameters should also be small enough so that we can iterate over those.

###
[](#fixing-a-7)Fixing A

Let’s suppose we iterate on all A. Then we have B \bmod C = 0 and We know A \bmod B = C for known A and unknown B and C. This doesn’t seem to help much, so moving on.

###
[](#fixing-b-8)Fixing B

Let’s suppose we fix B. Now we know that C is a factor of B, and A \bmod B = C, so C \lt B. Since C is a divisor of B, there would be d(C) candidates for C, where d(n) denotes the number of divisors of n. Let’s iterate over all those divisors of B in O(\sqrt B), So now we can loop over all pairs (B, C) in O(\sqrt B) such that B is multiple of C, we need to count the number of A such that 1 \leq A \leq N and A \bmod B = C \implies A = x*B + C.

Each value of x denotes a unique value of A and we have x \geq 0. so we need to count the values of x such that 0 \leq x and x*B+C \leq N which implies \displaystyle 0 \leq x \leq \frac{N-C}{B}. Hence, there are \displaystyle 1 + \left\lfloor \frac{N-C}{B}\right\rfloor candidates for A.

Hence, we can loop over all pairs (B, C) and sum over the number of candidates found for A for each pair.

This solution is taking time O(N * \sqrt N), as there are O(N) candidates for B and for each B, it takes O(\sqrt B) time to iterate over candidates of C. This solution is sufficient to get AC.

###
[](#fixing-c-9)Fixing C

Let’s suppose the value of C is fixed now. We know that B is a multiple of C. So there are \displaystyle \left\lfloor \frac{N}{C} \right\rfloor candidates for B up to N (All multiples of C up to N).

This way, we can first fix C and then loop over all multiples of C to choose it as a candidate for B, and use the same formula as above to calculate the number of candidates for A.

This solution is better, as we only iterated over pairs (B, C) such that B is a multiple of C. In the previous solution, we had to iterate up to \sqrt B to find factors, which included some non-candidates as well. So we can see that this solution is optimal than the previous solution.

Specifically, there are O(N) candidates for C and for each C, there are \displaystyle \left\lfloor \frac{N}{C} \right\rfloor candidates for B, so the number of pairs (B, C) can be written as \displaystyle \sum_{i = 1}^N \left\lfloor \frac{N}{i} \right\rfloor which can be approximated close to O(N*ln(N)) using [Harmonic numbers](https://en.wikipedia.org/wiki/Harmonic_number). This solution can also be seen similar to sieve of Eranthoses.

#
[](#time-complexity-10)TIME COMPLEXITY

The time complexity is O(N*\sqrt N) or O(N*log(N)) depending upon implementation.

#
[](#solutions-11)SOLUTIONS

Setter's Solution
``// nlather (Nishant Raj Lather)
// Chrollo_Lucifer

#include <bits/stdc++.h>
using namespace std;
#define boost ios_base::sync_with_stdio(false);cin.tie(nullptr);
#define rep(i, x, n) for(ll i = x; i < n; i++)
typedef long long int ll;

int main() {
    ll t;
    scanf("%lli", &t);
    while(t--) {
        ll n;
        scanf("%lli", &n);
        ll ans = 0;
        rep(b, 1, n+1) for(ll c = 2*b;c <= n; c += b) {
            ans += 1+(n-b)/c;
        }
        printf("%lli\n", ans);
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
	    uint32_t N;
	    uint64_t res = 0;
	    cin >> N;

	    fore(C, 1, N)
	    {
		    for (int B = 2 * C; B <= N; B += C)
		    {
			    res += 1 + (N - C) / B;
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
class SPCTRIPS{
    //SOLUTION BEGIN
    void pre() throws Exception{}
    void solve(int TC) throws Exception{
        int N = ni();
        long ans = 0;
        for(int C = 1; C <= N; C++){
            for(int B = C+C; B <= N; B+= C){
                //x*B+C <= N, 0 <= x
                //0 <= x <= (N-C)/B
                ans += (N-C)/B + 1;
            }
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
        new SPCTRIPS().run();
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
