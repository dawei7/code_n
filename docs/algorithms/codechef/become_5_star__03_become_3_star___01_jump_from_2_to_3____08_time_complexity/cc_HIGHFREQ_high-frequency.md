# High Frequency

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HIGHFREQ |
| Difficulty Rating | 1443 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [HIGHFREQ](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/HIGHFREQ) |

---

## Problem Statement

Chef has an array $A$ of length $N$.

Let $F(A)$ denote the maximum frequency of any element present in the array.

For example:

- If $A = [1, 2, 3, 2, 2, 1]$, then $F(A) = 3$ since element $2$ has the highest frequency $ = 3$.
- If $A = [1, 2, 3, 3, 2, 1]$, then $F(A) = 2$ since highest frequency of any element is $2$.

Chef can perform the following operation **at most once**:

- Choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) $S$ of the array such that every element of $S$ is the same, say $x$. Then, choose an integer $y$ and replace every element in this subsequence with $y$.

For example, let $A = [1, 2, 2, 1, 2, 2]$. A few examples of the operation that Chef can perform are:
- $[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]$
- $[1, \textcolor{red}{2}, 2, 1, \textcolor{red}{2, 2}] \to [1, \textcolor{blue}{19}, 2, 1, \textcolor{blue}{19, 19}]$
- $[\textcolor{red}{1}, 2, 2, 1, 2, 2] \to [\textcolor{blue}{2}, 2, 2, 1, 2, 2]$

Determine the **minimum** possible value of $F(A)$ Chef can get by performing the given operation at most once.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ denoting the length of array $A$.
    - The second line contains $N$ space-separated integers denoting the array $A$.

---

## Output Format

For each test case, output the minimum value of $F(A)$ Chef can get if he performs the operation optimally.

---

## Constraints

- $1 \leq T \leq 5000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 2 1 2
5
1 1 1 1 1
6
1 2 2 1 2 2
```

**Output**

```text
2
3
2
```

**Explanation**

**Test case $1$:** Chef cannot reduce the value of $F(A)$ by performing any operation.

**Test case $2$:** Chef can perform the operation $[\textcolor{red}{1}, 1, \textcolor{red}{1}, 1, \textcolor{red}{1}] \to [\textcolor{blue}{2}, 1, \textcolor{blue}{2}, 1, \textcolor{blue}{2}]$.
The value of $F(A)$ in this case is $3$, which is the minimum possible.

**Test case $3$:** Chef can perform the operation $[1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]$. The value of $F(A)$ in this case is $2$, which is the minimum possible.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
5
1 1 1 1 1
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
6
1 2 2 1 2 2
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START49A/problems/HIGHFREQ)

[Contest Division 2](https://www.codechef.com/START49B/problems/HIGHFREQ)

[Contest Division 3](https://www.codechef.com/START49C/problems/HIGHFREQ)

[Contest Division 4](https://www.codechef.com/START49D/problems/HIGHFREQ)

Setter: [Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

Tester: [ Jeevan Jyot Singh](https://www.codechef.com/users/jeevan_adm),[ Nishank Suresh](https://www.codechef.com/users/iceknight1093)

Editorialist: [Yash Kulkarni](https://www.codechef.com/users/kulyash)

#
[](#difficulty-2)DIFFICULTY:

1443

#
[](#prerequisites-3)PREREQUISITES:

[Hash Maps]

#
[](#problem-4)PROBLEM:

Chef has an array A of length N.

Let F(A) denote the maximum frequency of any element present in the array.

For example:

- If A = [1, 2, 3, 2, 2, 1], then F(A) = 3 since element 2 has the highest frequency  = 3.

- If A = [1, 2, 3, 3, 2, 1], then F(A) = 2 since highest frequency of any element is 2.

Chef can perform the following operation **at most once**:

- Choose any [subsequence](https://en.wikipedia.org/wiki/Subsequence) S of the array such that every element of S is the same, say x. Then, choose an integer y and replace every element in this subsequence with y.

For example, let A = [1, 2, 2, 1, 2, 2]. A few examples of the operation that Chef can perform are:

- [1, \textcolor{red}{2, 2}, 1, 2, 2] \to [1, \textcolor{blue}{5, 5}, 1, 2, 2]

- [1, \textcolor{red}{2}, 2, 1, \textcolor{red}{2, 2}] \to [1, \textcolor{blue}{19}, 2, 1, \textcolor{blue}{19, 19}]

- [\textcolor{red}{1}, 2, 2, 1, 2, 2] \to [\textcolor{blue}{2}, 2, 2, 1, 2, 2]

Determine the **minimum** possible value of F(A) Chef can get by performing the given operation at most once.

#
[](#explanation-5)EXPLANATION:

Let P be the element with the maximum frequency in A (having frequency freq_P) and Q be the element with the second maximum frequency in A (having frequency freq_Q) . It is possible that Q does not exist. Let us consider these 2 cases:

-
Q exists - Initially F(A) = freq_P. We should choose x = P because we need to minimize the final value of F(A) as in the question and it is always better to have y \neq Q. We should only replace a maximum of \lfloor\frac{freq_P}{2} \rfloor occurrences of P to y because if we replace more, then y becomes the new element with the maximum frequency. Also, replacing less than \lfloor\frac{freq_P}{2} \rfloor occurrences of P to y is not optimal because frequency of P can be further reduced by replacing more occurrences of P and hence F(A) can be reduced further. Hence, it is optimal to replace \lfloor\frac{freq_P}{2} \rfloor occurrences of P to some y \neq Q. Now, freq_P - \lfloor\frac{freq_P}{2} \rfloor is the final frequency of P and freq_Q is the final frequency of Q. The maximum among these two i.e. Max( freq_P - \lfloor\frac{freq_P}{2} \rfloor, freq_Q) has to be the answer because frequency of y = \lfloor\frac{freq_P}{2} \rfloor \leq freq_P - \lfloor\frac{freq_P}{2} \rfloor = frequency of P.

-
Q does not exist - Everything will remain same like the above point just freq_Q is 0. So, the answer is  freq_P - \lfloor\frac{freq_P}{2} \rfloor.

This can be implemented very easily using a hash map, which stores the number of occurrences of all elements in A.

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
    int n=readInt(2,100000,'\n');
    sumN+=n;
    assert(sumN<=200000);
    int A[n+1]={0};
    int freq[n+1]={0};
    for(int i=1;i<=n;i++)
    {
        if(i!=n)
            A[i]=readInt(1,n,' ');
        else
            A[i]=readInt(1,n,'\n');
        freq[A[i]]++;
    }
    vector <int> v;
    for(int i=1;i<=n;i++)
        v.pb(freq[i]);
    sort(all(v));
    reverse(all(v));
    int x=v[0];
    int y=v[1];
    cout<<max((x+1)/2,y)<<'\n';
}
int main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,5000,'\n');
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
	    unordered_map<int,int>ff;
	    for(int i=0;i<n;i++){
	        int t;
	        cin >> t;
	        ff[t]++;
	    }
	    vector<int>y;
	    for(auto i:ff)y.push_back(i.second);
	    sort(y.begin(),y.end());
	    int m=y.size();
	    int a=y[m-1];
	    int b=0;
	    if(m>1)b=y[m-2];
	    cout << max(a/2+(int)(a%2!=0),b) << endl;
	}
	return 0;
}

``

</details>
