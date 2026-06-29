# Retrieve the Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ARRAYRET |
| Difficulty Rating | 1193 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ARRAYRET](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ARRAYRET) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

Let $f(i)$ denote the sum $A_1 + A_2 + \dots + A_i \,$ and let $g(i)$ denote the sum $A_i + A_{i + 1} + \dots + A_N$.

Chef creates another array $B$ of length $N$ such that $B_i = f(i) + g(i)$ for all $1 \leq i \leq N$.

Now, Chef has lost the original array $A$ and needs your help to recover it, given array $B$. It is guaranteed that Chef has obtained the array $B$ from a valid array $A$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $B_1, B_2, \dots, B_N$ denoting the array $B$.

---

## Output Format

For each testcase, output $N$ space separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

Note that $1 \leq A_i \leq 10^5$ must hold for all $1 \leq i \leq N$ and it is guaranteed that a valid array $A$ that meets these constraints exists.

If there are multiple answers, output any.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- $1 \leq B_i \leq 2 \cdot 10^{10}$
- Th sum of $N$ over all test cases does not exceed $10^5$.
- $1 \leq A_i \leq 10^5$
- It is guaranteed that a valid array $A$ always exists.

---

## Examples

**Example 1**

**Input**

```text
4
1
6
3
7 8 9
4
13 15 13 14
2
25 20
```

**Output**

```text
3 
1 2 3 
2 4 2 3 
10 5
```

**Explanation**

**Test case 1:** For $A = [3]$, $B = [6]$. $B_1 = f(1) + g(1) = 3 + 3 = 6$.

**Test case 2:** For $A = [1, 2, 3]$, $B = [7, 8, 9]$.
- $B_1 = f(1) + g(1) = \underline{1} + \underline{1 + 2 + 3} = 7$
- $B_2 = f(2) + g(2) = \underline{1 + 2} + \underline{2 + 3} = 8$
- $B_3 = f(3) + g(3) = \underline{1 + 2 + 3} + \underline{3} = 9$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
6
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
3
7 8 9
```

**Output for this case**

```text
1 2 3
```



#### Test case 3

**Input for this case**

```text
4
13 15 13 14
```

**Output for this case**

```text
2 4 2 3
```



#### Test case 4

**Input for this case**

```text
2
25 20
```

**Output for this case**

```text
10 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START45A/problems/ARRAYRET)

[Contest Division 2](https://www.codechef.com/START45B/problems/ARRAYRET)

[Contest Division 3](https://www.codechef.com/START45C/problems/ARRAYRET)

[Contest Division 4](https://www.codechef.com/START45D/problems/ARRAYRET)

Setter: [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

Tester: [Takuki Kurokawa](https://www.codechef.com/users/tabr)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

1193

#
[](#prerequisites-3)PREREQUISITES:

[Basic Math]

#
[](#problem-4)PROBLEM:

Chef has an array A (1 \leq A_i \leq 10^5) of length N.

Let

pref_i = A_1 + A_2 + \dots A_i

suff_i = A_i + A_{i+1} + \dots A_N

Now Chef created another array B of length N such that B_i = pref_i + suff_i.

Chef lost the original array A and wants to recover it with the help of B. Help Chef to recover the array.

It is guaranteed in the input that there exists a valid array A for the given array B. In case of multiple valid arrays A, output any valid array.

#
[](#explanation-5)EXPLANATION:

Hint

There exists a unique solution.

Solution

Let us have a look at the elements of array B.

B_i = pref_i + suff_i = (A_1 + A_2 + ... A_i) + (A_i + A_{i+1} + ... A_N) = (A_1 + A_2 + ... A_N) + A_i.  Hence B_i = SUM_A + A_i, where SUM_A is the sum of the original array (A).

Now, let us have a look at the sum of the elements of the array B and use the above observation.

SUM_B = B_1 + B_2 + ... B_N = (SUM_A + A_1) + (SUM_A + A_2) + ... (SUM_A + A_N).

Hence SUM_B = (N + 1) \times SUM_A.

So, we can find out SUM_A using SUM_B i.e. SUM_A = SUM_B / (N+1). After knowing SUM_A and using the first observation (A_i = B_i - SUM_A), we can find all the elements of the original array (A), which is the required answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each test case.

#
[](#solution-7)SOLUTION:

Setter's solution
``#include <bits/stdc++.h>
#define ll long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
ll modInverse(ll a){return power(a,mod-2);}
const int N=500023;
bool vis[N];
vector <int> adj[N];
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
int sumN=0;
void solve()
{
    int n=readInt(1,100000,'\n');
    sumN+=n;
    assert(sumN<=100000);
    ll B[n+1]={0};
    for(int i=1;i<=n;i++)
    {
    	if(i==n)
    		B[i]=readInt(1,(ll)200000 * 1000000,'\n');
    	else
    		B[i]=readInt(1,(ll)200000 * 1000000,' ');
    }
    ll sum=0;
    for(int i=1;i<=n;i++)
    	sum+=B[i];
    assert((sum%(n+1))==0);
    sum/=(n+1);
    ll A[n+1]={0};
    for(int i=1;i<=n;i++)
    {
    	A[i]=B[i]-sum;
    	assert(A[i]>=1 && A[i]<=100000);
    	cout<<A[i]<<' ';
    }
    cout<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,1000,'\n');
    while(T--)
        solve();
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Editorialist's Solution
``using namespace std;

int main() {
	int T;
	cin >> T;
	while(T--){
	    int n;
	    cin >> n;
	    vector<long long>b(n);
	    long long big_sum=0;
	    for(int i=0;i<n;i++){
	        cin >> b[i];
	        big_sum+=b[i];
	    }
	    long long small_sum=big_sum/(n+1);
	    for(int i=0;i<n;i++){
	        cout << b[i]-small_sum << " ";
	    }
	    cout << endl;
	}
	return 0;
}
``

</details>
