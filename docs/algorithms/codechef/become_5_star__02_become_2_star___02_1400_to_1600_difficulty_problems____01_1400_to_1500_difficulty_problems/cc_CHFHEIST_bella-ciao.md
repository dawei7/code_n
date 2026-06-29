# Bella ciao

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFHEIST |
| Difficulty Rating | 1410 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHFHEIST](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHFHEIST) |

---

## Problem Statement

Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/CHFHEIST.pdf),

Chef is planning a heist in the reserve bank of Chefland. They are planning to hijack the bank for $D$ days and print the money. The initial rate of printing the currency is $P$ dollars per day and they increase the production by $Q$ dollars after every interval of $d$ days. For example, after $d$ days the rate is $P+Q$ dollars per day, and after $2d$ days the rate is $P+2Q$ dollars per day, and so on. Output the amount of money they will be able to print in the given period.

### Input

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, four integers $D, d, P, Q$.

### Output
For each test case, output in a single line the answer to the problem.

### Constraints
- $1 \leq T \leq 10^5$
- $1 \leq d \leq D \leq 10^6$
- $1 \leq P, Q \leq 10^6$

### Subtasks
**Subtask #1 (15 points):** $d \leq D \leq 100$

**Subtask #2 (85 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2 1 1 1
3 2 1 1
5 2 1 2
```

**Output**

```text
3
4
13
```

**Explanation**

**Test Case $1$:**
- On the first day, the rate of production is $1$ dollar per day so $1$ dollar is printed on the first day.
- On the second day, the rate of production is $1 + 1 = 2$ dollars per day so $2$ dollars are printed on the second day.
- The total amount of money printed in $2$ days is $1 + 2 = 3$ dollars.

**Test Case $2$:**
- For the first two days, the rate of production is $1$ dollar per day so $1 \cdot 2 = 2$ dollars are printed on the first two days.
- On the third day, the rate of production is $1 + 1 = 2$ dollars per day so $2$ dollars are printed on the third day.
- The total amount of money printed in $3$ days is $2 + 2 = 4$ dollars.

**Test Case $3$:**
- For the first two days, the rate of production is $1$ dollar per day so $1 \cdot 2 = 2$ dollars are printed on the first two days.
- On the next two days, the rate of production is $1 + 2 = 3$ dollars per day so $3 \cdot 2 = 6$ dollars are printed on the next two days.
- On the last day, the rate of production is $3 + 2 = 5$ dollars per day so $5$ dollars are printed on the last day.
- The total amount of money printed in $5$ days is $2 + 6 + 5 = 13$ dollars.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 1 1 1
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3 2 1 1
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
5 2 1 2
```

**Output for this case**

```text
13
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/JUNE21A/problems/CHFHEIST)

[Contest Division 2](https://www.codechef.com/JUNE21B/problems/CHFHEIST)

[Contest Division 3](https://www.codechef.com/JUNE21C/problems/CHFHEIST)

[Practice](https://www.codechef.com/problems/CHFHEIST)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Istvan Nagy](https://www.codechef.com/users/iscsi)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY

Simple

# PREREQUISITES

Arithmetic Progression

# PROBLEM

Chef is planning a heist in the reserve bank of Chefland. They are planning to hijack the bank for D days and print the money. The initial rate of printing the currency is P dollars per day and they increase the production by Q dollars after every interval of d days. For example, after d days the rate is P+Q dollars per day, and after 2d days the rate is P+2Q dollars per day, and so on. Output the amount of money they will be able to print in the given period.

# QUICK EXPLANATION

- Ignoring the last D \bmod d days, all days are divided into  D/d groups of d days each where first d days Chef receives P dollars, next d days Chef receives P+Q dollars, and so on.

- Each group contains d values, so we can calculate the sum of dollars for 1 person in each group and multiply by d.

- The sum of values in each group is d times the sum of Arithmetic Progression with initial term P, common difference Q, and number of terms D/d.

- Last D \bmod d days, the Chef receives the same amount, calculated by computing the nth term of a similar Arithmetic Progression.

# EXPLANATION

For subtask 1, we can iterate up to D, maintaining track of the number of dollars earned and current earning per day, so I’ll focus on complete solution.

Let us see what the sequence looks like with D = 11, d = 4 for some P and Q

``Day			Dollars
1			P
2			P
3			P
4			P
5			P+Q
6			P+Q
7			P+Q
8			P+Q
9			P+2*Q
10			P+2*Q
11			P+2*Q
``

We can see that the same value appears in groups of d days, except the last group which may have less than d elements. Let’s ignore those now.

Let’s consider these groups, we can see that the terms P, P+Q, P+2*Q form an [arithmetic progression](https://en.wikipedia.org/wiki/Arithmetic_progression).

We need to compute d*P+d*(P+Q)+d*(P+2*Q) \ldots ... = d*(P+(P+Q)+(P+2*Q)+ \ldots )

What is the number of groups? In the above example, we had two groups, one with value P and one with value P+Q (Remember that we are ignoring the last group, which has less than d elements).

In the general case, we can see by basic maths that there are exactly N = D/d complete groups, and additionally, if D is not a multiple of d, there would be an incomplete group with D \bmod d elements.

Hence, ignoring last D \bmod d days, we can write sum of dollars earned as d * APsum(P, Q, D/d) where APsum(a, d, n) denotes the sum of first n terms of arithmetic progression with first term a and common difference d, given by formula \displaystyle \frac{n*(2*a+(n-1)*d)}{2}.

For the last D \bmod d days, the amount earned would be the same value, which is P+N*Q, since that is a part of (N+1)-th group. Hence, we can add (D \bmod d) * (P+N*Q) to account for dollars earned in last D \bmod d days.

In case of any doubt, refer to the implementations below.

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

const int maxt = 1e5, maxD = 1e6, maxp = 1e6;
const string newln = "\n", space = " ";

int main()
{
	int t; cin >> t;
	ll D, d, P, dP;
	while(t--){
	    cin >> D >> d >> P >> dP;
	    ll ans = P * D + dP * (d * (D / d - 1) * (D / d) / 2 + (D % d)  * (D / d));
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
		int64_t D = readIntSp(1, 1'000'000);
		int64_t d = readIntSp(1, D);

		int64_t P = readIntSp(1, 1'000'000);
		int64_t dP = readIntLn(1, 1'000'000);

		//d*P+d*(P+dp)
		//D*P
		//a=d*dp
		//b=D/d
		//a+2*a+3*a+..(b-1)*a = a*b*(b-1)/2
		//rem = D%d
		//rem*dp*b
		int64_t a = d * dP;
		int64_t b = D / d;
		int64_t rem = D % d;
		int64_t res = D * P + a*b*(b-1)/2 + rem * dP * b;

		printf("%lld\n", res);
	}
	return 0;
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
class CHFHEIST{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    long D = nl(), d = nl(), P = nl(), Q = nl();
	    long rem = D%d;
	    long N = D/d;
	    long sum = d * apSum(P, Q, N);
	    sum += rem * nth(P, Q, N+1);
	    pn(sum);
	}
	long apSum(long a, long d, long n){
	    return (n*(2*a+(n-1)*d))/2;
	}
	long nth(long a, long d, long n){
	    return a+(n-1)*d;
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
	    new CHFHEIST().run();
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
