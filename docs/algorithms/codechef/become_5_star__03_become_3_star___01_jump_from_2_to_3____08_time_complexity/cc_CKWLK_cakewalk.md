# Cakewalk

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CKWLK |
| Difficulty Rating | 1474 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [CKWLK](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/CKWLK) |

---

## Problem Statement

You are playing EVE Online. Initially, you have one dollar, but you have somehow acquired two cheat codes. The first cheat code multiplies the amount of money you own by $10$, while the second one multiplies it by $20$. The cheat codes can be used any number of times.

You want to have exactly $N$ dollars. Now you are wondering: can you achieve that by only using some sequence of cheat codes?

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

### Output
- For each test case, print a single line containing the string `"Yes"` if you can make exactly $N$ dollars or `"No"` otherwise.

### Constraints
- $1 \le T \le 100$
- $1 \le N \le 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
4
200
90
1000000000000
1024000000000
```

**Output**

```text
Yes
No
Yes
No
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
200
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
90
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
1000000000000
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
1024000000000
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CKWLK)

[Contest: Division 1](https://www.codechef.com/COOK111A/problems/CKWLK)

[Contest: Division 2](https://www.codechef.com/COOK111B/problems/CKWLK)

**Setter:** [Kasra Mazaheri](https://www.codechef.com/users/kmaaszraa)

**Tester:** [Arshia](https://www.codechef.com/users/ckodser)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Easy

# PREREQUISITES:

Basic Math

# PROBLEM:

You are playing game EVE online and Initially, you have 1 dollar. You have two cheat codes, the first one multiplies the amount of money you own by 10 and the second cheat code multiplies the amount of money you own by 20. Determine whether is it possible to own exactly N dollars through a sequence of cheat codes.

# QUICK EXPLANATION

- Let’s write N as 2^x*5^y. If it’s not possible to write in this way, we can see that we cannot obtain exactly N dollars, since No cheat code multiplies the number of dollars by any prime other than 2 or 5.

- Now, if x < y or x > 2*y, then too there’s no way to obtain N dollars since we use cheat codes exactly y times and each cheat code increases x by either 1 or 2.

# EXPLANATION

Let us analyze the cheat codes. Assuming the current number of dollars is K which is of the form 2^x*5^y

- The first cheat code multiplies K by 10 which is the same as increasing both x and y by 1 each.

- Second cheat code multiplies K by 20 which is same as increasing x by 2 and y by 1.

Hence, if the total number of operations applied is p, then y = p and p \leq x \leq 2*p which gives y \leq x \leq 2*y.

Hence, all N of the form 2^x*5^y can be obtained by a sequence of cheat codes where y \leq x \leq 2*y holds.

Also, if N contains any prime factor other than 2 and 5, then there’s no way to obtain exactly N dollars.

It is easy to check both cases and if the both cases are held, then we can obtain N dollars.

PS: a slightly different way to implement would be to write N in the form 2^x*10^y maximizing y first and then x and checking if the condition 0 \leq x \leq y holds.

**Bonus Problem**

Initially, you have X dollar and you have to apply cheat code at most N times, where each cheat code multiplies the number of dollars by any prime number in the range [1, K].

Determine whether you can obtain exactly M dollars.

# TIME COMPLEXITY

Time complexity is O(log_2(N)) per test case.

# SOLUTIONS:

Setter's Solution
``// In The Name Of The Queen
#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
	int q;
	scanf("%d", &q);
	for (; q; q --)
	{
	    ll n;
	    scanf("%lld", &n);
	    ll Pw10 = 0;
	    while (n % 10 == 0)
	        n /= 10, Pw10 ++;
	    if (__builtin_popcountll(n) != 1)
	        printf("No\n");
	    else if (__builtin_ctzll(n) > Pw10)
	        printf("No\n");
	    else
	        printf("Yes\n");
	}
}
``

Tester's Solution
``#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>
#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif

int gcd(int a, int b) {return b == 0 ? a : gcd(b, a % b);}

#define ll long long
#define pb push_back
#define ld long double
#define mp make_pair
#define F first
#define S second
#define pii pair<ll,ll>

using namespace :: std;

const ll maxn=1e5+500;
const ll inf=1e9+800;
const ll mod=1e9+7;

int main(){
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	int t;
	cin>>t;
	while(t--){
	    ll n;
	    cin>>n;
	    ll a=0,b=0;
	    while(n%10==0){
	        n/=10;
	        a++;
	    }
	    while(n%2==0){
	        n/=2;
	        b++;
	    }
	    if(n!=1 || b>a){
	        cout<<"No"<<endl;
	    }else{
	        cout<<"Yes"<<endl;
	    }
	}
}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class CKWLK{
	//SOLUTION BEGIN
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    long n = nl();
	    int ten = 0, two = 0;
	    while(n%10 == 0){n /= 10;ten++;}
	    while(n%2 == 0){n /= 2;two++;}
	    if(n == 1 && two <= ten)pn("Yes");
	    else pn("No");
	}
	//SOLUTION END
	void hold(boolean b)throws Exception{if(!b)throw new Exception("Hold right there, Sparky!");}
	DecimalFormat df = new DecimalFormat("0.00000000000");
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
	    new CKWLK().run();
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
