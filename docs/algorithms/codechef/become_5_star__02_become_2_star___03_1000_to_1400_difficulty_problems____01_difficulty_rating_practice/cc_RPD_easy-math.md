# Easy Math

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RPD |
| Difficulty Rating | 1133 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [RPD](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/RPD) |

---

## Problem Statement

Chef is attending math classes. On each day, the teacher gives him homework. Yesterday, the teacher gave Chef a sequence of positive integers and asked him to find the maximum product of two different elements of this sequence. This homework was easy for Chef, since he knew that he should select the biggest two numbers.

However, today, the homework is a little bit different. Again, Chef has a sequence of positive integers $A_1, A_2, \ldots, A_N$, but he should find two different elements of this sequence such that the sum of digits (in base $10$) of their product is maximum possible.

Chef thought, mistakenly, that he can still select the two largest elements and compute the sum of digits of their product. Show him that he is wrong by finding the correct answer ― the maximum possible sum of digits of a product of two different elements of the sequence $A$.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of the input contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line containing one integer ― the maximum sum of digits.

### Constraints
- $1 \le T \le 100$
- $2 \le N \le 100$
- $1 \le A_i \le 10^4$ for each valid $i$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
2
2 8
3 
8 2 8
3
9 10 11
```

**Output**

```text
7
10
18
```

**Explanation**

**Example case 1:** The only two numbers Chef can choose are $2$ and $8$. Their product is $16$ and the sum of digits of $16$ is $7$.

**Example case 2:** Chef can choose $8$ and $8$; their product is $64$. Note that it is allowed to choose two different elements with the same value.

**Example case 3:** Chef can choose $9$ and $11$. Their product is $99$ and the sum of its digits is $18$. Note that choosing $10$ and $11$ will result in a larger product ($110$), but the sum of its digits is just $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 8
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
3
8 2 8
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
3
9 10 11
```

**Output for this case**

```text
18
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Div1](https://www.codechef.com/LTIME74A/problems/RPD)

[Div2](https://www.codechef.com/LTIME74B/problems/RPD)

[Practice](https://www.codechef.com/problems/RPD)

**Setter-**  [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Tester-**  [Roman Bilyi](https://www.codechef.com/users/romawhite)

**Editorialist-** [Abhishek Pandey](https://www.codechef.com/users/vijju123)

### DIFFICULTY:

CAKEWALK

### PRE-REQUISITES:

Implementation

### PROBLEM:

Given an array A of size N, find the largest sum of digits obtainable from product of any two numbers of the array.

### QUICK-EXPLANATION:

**Key to AC-** A look at the constraints and implementation skills!

Since the size of the array is only upto 100, there are \binom{N}{2}, i.e. \frac{N*(N-1)}{2} ways of choosing the elements. Hence we simply choose all possible pairs, find their product, find the sum of digits of the product, and report the maximum one out of those!

### EXPLANATION:

The solution is pretty straightforward, hence we will discuss it in a single section, along with code for reference.

The first thing after taking input is to formulate what we are doing. What we will do is-

- Pick a pair out of the \binom{N}{2} pairs.

- Find its product and sum of digits.

- If this is greater than sum of digits seen so far, update answer appropriately.

First, we will have to pick the pair of elements we wish to multiply. This is achieved by using 2 nested loops-

``for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            int product = arr[i] * arr[j];
        }
    }
``

The next step, is to find the sum of digits. It is a good practice to make functions for any common functionality we reuse - and to keep code clean. Hence, we will make a function to find and return sum of digit of the given number. We will then call it from the loops we just created.

``int sumOfDigits(int n)
{
    int sum=0;
    while(n>0)
    {
        sum+=n%10; // n%10 gives the digit at units place
        n/=10; // Integer division leads to loss of digit at unit's place, and shifts all digits by 1 place right.
    }
    return sum;
}
``

All that is left is to call this function, and update the answer appropriately. Our final code looks somewhat like this-

``int ans=0;

    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
        {
            int product = arr[i] * arr[j];
            int sum= sumOfDigits(product);
            ans=max(ans,sum);
        }
    }
``

### SOLUTION

Setter
`` #include <iostream>
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
int n;
int arr[111];

int sumdig(int x){
	if(x==0)return 0;
	return (x%10) + sumdig(x/10);
}

int main(){
	//freopen("00.txt","r",stdin);
	//freopen("00o.txt","w",stdout);
	T=readIntLn(1,100);
	while(T--){
		int sl = 0;
		n=readIntLn(1,100);
		for(int i=0;i<n;i++){
			if(i==n-1){
				arr[i]=readIntLn(1,10000);
			} else {
				arr[i]=readIntSp(1,10000);
			}
		}
		for(int i=0;i<n;i++){
			for(int j=i+1;j<n;j++){
				sl = max(sl, sumdig(arr[i] * arr[j]));
			}
		}
		cout<<sl<<endl;
	}
	assert(getchar()==-1);
}
``

Tester
``#include "bits/stdc++.h"
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
const int MAX = 307;

const int MOD = 998244353;

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
void assertEof(){
    assert(getchar()==-1);
}

int f(int n)
{
    int res = 0;
    while (n)
    {
        res += n % 10;
        n /= 10;
    }
    return res;
}

int main(int argc, char* argv[])
{
	// freopen("in.txt", "r", stdin);
	//ios::sync_with_stdio(false); cin.tie(0);

    int t = readIntLn(1, 100);
    FOR(tt,0,t)
    {
        int n = readIntLn(2, 100);
        VI A(n);
        FOR(i,0,n)
            A[i] = readInt(1, 10000, (i + 1 < n ? ' ' : '\n'));
        int res = 0;
        FOR(i,0,n)
            FOR(j,i + 1,n)
                res = max(res, f(A[i] * A[j]));
        cout << res << endl;
    }

    assertEof();

    cerr << 1.0 * clock() / CLOCKS_PER_SEC << endl;

}
``

Editorialist
``  /*
 *
 ********************************************************************************************
 * AUTHOR : Vijju123                                                                        *
 * Language: C++14                                                                          *
 * Purpose: -                                                                               *
 * IDE used: Codechef IDE.                                                                  *
 ********************************************************************************************
 *
 Comments will be included in practice problems if it helps ^^
 */

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

//I never understand why people put useless functions at top of code. Makes it so unreadable ughhhh.
int mod=pow(10,9)+7;
int fastExpo(long long a,long long n, int mod)
{
    a%=mod;
    if(n==2)return a*a%mod;
    if(n==1)return a;
    if(n&1)return a*fastExpo(fastExpo(a,n>>1,mod),2,mod)%mod;
    else return fastExpo(fastExpo(a,n>>1,mod),2,mod);
}
inline void add(vector<vector<int> > &a,vector<vector<int> > &b,int mod)
{
    for(int i=0;i<a.size();i++)for(int j=0;j<a[0].size();j++)b[i][j]=(b[i][j]+a[i][j])%mod;
}

void multiply(vector<vector<int> > &a, vector<vector<int> > &b,int mod,vector<vector<int> > &temp)
{
    assert(a[0].size()==b.size());
    int i,j;
    for(i=0;i<a.size();i++)
    {
        for(j=0;j<b[0].size();j++)
        {
            temp[i][j]=0;
            for(int p=0;p<a[0].size();p++)
            {
                temp[i][j]=(temp[i][j]+1LL*a[i][p]*b[p][j])%mod;
            }
        }
    }
}

void MatExpo(vector<vector<int> > &arr,int power,int mod)
{
    int i,j,k;
    vector<vector<int> >temp,temp2,temp3;
    vector<int> init(arr[0].size());
    for(i=0;i<arr.size();i++){temp.push_back(init);}
    temp3=temp;
    temp2=temp;
    for(i=0;i<arr.size();i++)temp3[i][i]=1;
    while(power>0)
    {
        if(power&1)
        {
            multiply(arr,temp3,mod,temp);
            swap(temp3,temp);
        }
        multiply(arr,arr,mod,temp2);
        swap(arr,temp2);
        power>>=1;
    }
    swap(arr,temp3);
}

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

vector<int> primes;
int isComposite[1000001]={1,1};
void sieve()
{
    int i,j;
    for(i=2;i<=1000000;i++)
    {
        if(!isComposite[i])
        {
            primes.push_back(i);
            isComposite[i]=i;
        }
        for(j=0;j<primes.size() and i*primes[j]<=1000000;j++)
        {
            isComposite[primes[j]*i]=i;
            if(i%primes[j]==0)break;
        }
    }
}

int sumOfDigits(int n)
{
    int sum=0;
    while(n>0)
    {
        sum+=n%10;
        n/=10;
    }
    return sum;
}

int main() {
	// your code goes here
	#ifdef JUDGE
	string in,out;
	cin>>in>>out;
	in+=".in";
	if(in!="z.in")
        out+=".out";
    else out+=".in";
	if(in!="z.in")
    freopen(in.c_str(), "rt", stdin);
    freopen(out.c_str(), "wt", stdout);
    #endif
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	srand(time(NULL));
	mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int arr[n],i,j,k;
	    for(i=0;i<n;i++)cin>>arr[i];
	    int ans=0;

	    for(i=0;i<n;i++)
	    {
	        for(j=i+1;j<n;j++)
	        {
	            int product = arr[i] * arr[j];
	            int sum= sumOfDigits(product);
	            ans=max(ans,sum);
	        }
	    }
	    cout<<ans<<endl;
	}

	assert(getchar()==-1);
	return 0;
}
``

Time Complexity=O(N^2LogA_i)

Space Complexity=O(N)

### CHEF VIJJU’S CORNER

1.Discuss solution if constraints of A_i are raised upto 10^{18}. Does the solution change at all?

2. Discuss solution if constraints of A_i are raised upto 10^{300}. How will you solve it without using Big Integer libraries?

Hint

Take input of A_i as a string!! Or, explore ways by which you can declare an integer array, which takes only 1 digit in input.

3.How many steps does it take to find sum of digit of a number \leq 10^4 ? Answer the same for finding sum of digit of a number \leq 10^{300}

Answer

5 and 301 respectively. In general, if there are N digits in a number, it takes O(N) time to find sum of digits!

</details>
