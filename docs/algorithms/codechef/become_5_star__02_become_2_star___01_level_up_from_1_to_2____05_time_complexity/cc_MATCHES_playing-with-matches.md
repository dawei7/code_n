# Playing with Matches

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATCHES |
| Difficulty Rating | 986 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [MATCHES](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/MATCHES) |

---

## Problem Statement

Chef's son Chefu found some matches in the kitchen and he immediately starting playing with them.

The first thing Chefu wanted to do was to calculate the result of his homework — the sum of $A$ and $B$, and write it using matches. Help Chefu and tell him the number of matches needed to write the result.

Digits are formed using matches in the following way:
![](https://codechef_shared.s3.amazonaws.com/download/Images/COOK110/MATCHES/97JCfQw.gif)

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $A$ and $B$.

### Output
For each test case, print a single line containing one integer — the number of matches needed to write the result ($A+B$).

### Constraints
- $1 \le T \le 1,000$
- $1 \le A, B \le 10^6$

---

## Examples

**Example 1**

**Input**

```text
3
123 234
10101 1010
4 4
```

**Output**

```text
13
10
7
```

**Explanation**

**Example case 1:** The result is $357$. We need $5$ matches to write the digit $3$, $5$ matches to write the digit $5$ and $3$ matches to write the digit $7$.

**Example case 2:** The result is $11111$. We need $2$ matches to write each digit $1$, which is $2 \cdot 5 = 10$ matches in total.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
123 234
```

**Output for this case**

```text
13
```



#### Test case 2

**Input for this case**

```text
10101 1010
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
4 4
```

**Output for this case**

```text
7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MATCHES)

[Contest: Division 1](https://www.codechef.com/COOK110A/problems/MATCHES)

[Contest: Division 2](https://www.codechef.com/COOK110B/problems/MATCHES)

**Setter:** [Hasan](https://www.codechef.com/users/kingofnumbers)

**Tester:** [Roman Bilyi](https://www.codechef.com/users/romawhite)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

# DIFFICULTY:

Cakewalk

# PREREQUISITES:

None

# PROBLEM:

Given two values A and B, Find the number of matches required to write S = A+B as explained in the problem statement.

# EXPLANATION

Since matches used for each digit is independent, we just need to write each digit of A+B separately and count the number of matches required for each digit. From the image

We can see that 6 matches are needed to write 0 on display, 2 matches are needed to write 1 on display and so on. We can count this for all digits and store it in an array, say count. count[x] denotes the number of matches required to write digit x on display.

Now, to obtain digits of S = A+B, we can see that taking remainder by 10 gives the last digit of S and dividing S by 10 removes the last digit. These two observations give us a way to get all digits of S.

``while S > 0:
       D = S%10 //D is the least significant digit of S
       ANS = ANS + count[D]
       S = S/10 //Least significant digit is discarded
``

**Bonus problem**

Count the number of Matches needed to write A+B **in base x** using matches where 2 \leq x \leq 10

# TIME COMPLEXITY

For each test case, time taken is the number of digits of A+B in base 10, which is log_{10}(A+B), so time complexity per test case is O(log_{10}(A+B))

# SOLUTIONS:

Setter's Solution
``#include <iostream>
#include <algorithm>
#include <string>
#include <assert.h>
using namespace std;

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
			assert(cnt>0);
			if(is_neg){
				x= -x;
			}
			assert(l<=x && x<=r);
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

int T;
int A,B;

int num[10]={6,2,5,5,4,5,6,3,7,6};

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,1000);
	while(T--){
		A=readIntSp(1,1000000);
		B=readIntLn(1,1000000);
		int s= A+B;
		int ans = 0;
		while(s>0){
			ans += num[s % 10];
			s /= 10;
		}
		cout<<ans<<endl;
	}
	assert(getchar()==-1);
}
``

Tester's Solution
``#include "bits/stdc++.h"
#pragma GCC optimize("Ofast")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,avx,avx2")
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define RFOR(i,b,a) for (int i = (b) - 1; i >= (a); i--)
#define ITER(it,a) for (__typeof(a.begin()) it = a.begin(); it != a.end(); it++)
#define FILL(a,value) memset(a, value, sizeof(a))

#define SZ(a) (int)a.size()
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef long long Int;
typedef vector<int> VI;
typedef pair<int, int> PII;

const double PI = acos(-1.0);
const int INF = 1000 * 1000 * 1000;
const Int LINF = INF * (Int) INF;
const int MAX = 100007;

const int MOD = 1000000007;

const double Pi = acos(-1.0);

int d[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

int f(int x)
{
	int res = 0;
	while(x)
	{
	    res += d[x % 10];
	    x /= 10;
	}
	return res;
}

int main(int argc, char* argv[])
{
	// freopen("in.txt", "r", stdin);
	//ios::sync_with_stdio(false); cin.tie(0);

	int t;
	cin >> t;
	assert(t <= 1000);
	FOR(tt,0,t) {
	    int a, b;
	    cin >> a >> b;
	    assert(a >= 1 && a <= 1000000);
	    assert(b >= 1 && b <= 1000000);
	    cout << f(a + b) << endl;
	}

	cerr << 1.0 * clock() / CLOCKS_PER_SEC << endl;

}
``

Editorialist's Solution
``import java.util.*;
import java.io.*;
import java.text.*;
class MATCHES{
	//SOLUTION BEGIN
	int[] mp = new int[]{6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
	void pre() throws Exception{}
	void solve(int TC) throws Exception{
	    int s = ni()+ni(), ans = 0;
	    while(s>0){
	        ans+=mp[s%10];
	        s/=10;
	    }
	    pn(ans);
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
	    new MATCHES().run();
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

Feel free to share your approach, if you want to. (even if its same  ) . Suggestions are welcomed as always had been.

</details>
