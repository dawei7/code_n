# Again XOR problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KLXOR |
| Difficulty Rating | 1786 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [KLXOR](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/KLXOR) |

---

## Problem Statement

You may have solved a lot of problems related to XOR and we are sure that you liked them, so here is one more problem for you.

You are given a binary string $S$ of length $N$. Let string $T$ be the result of taking the XOR of **all** substrings of size $K$ of $S$. You need to find the number of `1` bits in $T$.

**Note**:
- A substring is a continuous part of string which can be obtained by deleting some (may be none) character's from the beginning and some (may be none) character's from the end.
- XOR of many similar-sized strings is defined [here](https://en.wikipedia.org/wiki/Exclusive_or).

---

## Input Format

- The first line of the input contains an integer $T$ - the number of test cases. The test cases then follow.
- The first line of each test case contains two integers $N$ and $K$.
- The second line of each test case contains a binary string $S$ of size $N$.

---

## Output Format

For each test case, output on a single line number of `1` bits in the XOR of all substrings of size $K$ of $S$.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq K \le N \leq 2 \cdot 10^5$
- $|S| = N$
- $S$ only contains characters `0` and `1`.

---

## Examples

**Example 1**

**Input**

```text
4
4 1
1010
4 2
1001
4 3
1111
4 4
0110
```

**Output**

```text
0
2
0
2
```

**Explanation**

- **Test case $1$**: All $1$-sized substrings of $S$ are:
    - `0`
    - `1`
    - `1`
    - `0`

The XOR of these strings is `0`, therefore the number of `1` bits is $0$.
- **Test case $2$**: All $2$-sized substrings of $S$ are:
    - `10`
    - `00`
    - `01`

The XOR of these strings is `11`, therefore the number of `1` bits is $2$.
- **Test case $3$**: All $3$-sized substrings of $S$ are:
    - `111`
    - `111`

The XOR of these strings is `000`, therefore the number of `1` bits is $0$.
- **Test case $4$**: All $4$-sized substrings of $S$ are:
    - `0110`

The XOR of these strings is `0110`, therefore the number of `1` bits is $2$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 1
1010
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4 2
1001
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4 3
1111
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
4 4
0110
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Again XOR Problem :

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KLXOR)

[Code Drive Contest Division 1](https://www.codechef.com/CDRV21A/problems/KLXOR)

[Code Drive Contest Division 2](https://www.codechef.com/CDRV21B/problems/KLXOR)

[Code Drive Contest Division 3](https://www.codechef.com/CDRV21C/problems/KLXOR)

***Author:*** [Sobhagya Singh Dewal](https://www.codechef.com/users/manoj_vajpeyi)

***Tester:*** [Lavish Gupta](https://www.codechef.com/users/lavish315) , [ Takuki Kurokawa](https://www.codechef.com/users/tabr)

#
[](#difficulty-2)DIFFICULTY:

EASY

#
[](#prerequisites-3)PREREQUISITES:

Strings ,Math, Prefix-arrays

#
[](#problem-4)PROBLEM:

You may have solved a lot of problems related to [XOR](https://en.wikipedia.org/wiki/Exclusive_or) and we are sure that you liked them, so here is one more gift for you.

You are given a binary string S of length N, you need to find how many bits will be set in the XOR of all substrings of size K in the given string.

**Note :**

Number of set bits is the number of ones in a binary string.

A substring is a continuous part of string which can be obtained by deleting some(may be none) character’s from front and some(may be none) character’s from the end.

XOR of 2 binary string is the standard logical XOR.

#
[](#quick-explanation-5)QUICK EXPLANATION:

There will be K index in the final string, and for each position we know which index will come from the initial string so we can just count the number of ones at each position.

#
[](#explanation-6)EXPLANATION:

In the question length of the string is N and we need to check for all K length substrings so we know that there will be total N-K+1 substrings of length K and we need to XOR all of them.

Lets say string S=S_{0}+S_{1}+S_{2}.....+S_{N-1} where S_{0},S_{1},S_{2}.....,S_{N-1} are N characters of strings.

And all K length substrings will be:

Sub_{0}=S_{0}+S_{1}+S_{2}+......+S_{K-1}

Sub_{1}=S_{1}+S_{2}+S_{3}+......+S_{K}

Sub_{2}=S_{2}+S_{3}+S_{4}+......+S_{K+1}

......

Sub_{N-K}=S_{N-K}+S_{N-K+1}+S_{N-K+2}+......+S_{N-1}

Now we know that in the final string at i^{th} position which characters will be occurs, so lets say final string is F then:

F_{0}=S_{0}\oplus S_{1}\oplus S_{2}.......\oplus S_{N-K}

F_{1}=S_{1}\oplus S_{2}\oplus S_{3}.......\oplus S_{N-K+1}

F_{2}=S_{2}\oplus S_{3}\oplus S_{4}.......\oplus S_{N-K+2}

........

F_{K-1}=S_{K-1}\oplus S_{K}\oplus S_{K+1}.......\oplus S_{N-1}

Now F_{i} can be easily calculated by number of ones from S_{i} to S_{N-K+i} that can be done with prefix array, we will store number of ones till i^{th} position in an array and then we can find number of ones in an range.

For example Pre_{i} is number of ones till i^{th} position in string S and we want to count number of ones from S_{i} to S_{N-K+i}

then it will be number of ones till S_{N-K+i}-number of ones till S_{i-1}.

So finally F_{i} will be (Pre_{N-K+i}-Pre_{i-1})\% 2.

Time Complexity: O(N) for each testcase.

#
[](#solutions-7)SOLUTIONS:

Setter’s Solution
``#include <bits/stdc++.h>
using namespace std;

void myfun()
{
	int n,k;
	cin>>n>>k;
	string s; cin>>s;
	int pre[n+1];
	pre[0]=0;
	for(int i=0;i<n;i++)
	{
		pre[i+1]=pre[i];
		if(s[i]=='1') pre[i+1]++;
	}
	int j=n-k+1,i=0;
	int res=0;
	while(j<=n)
	{
		int cur=pre[j]-pre[i];
		res=res+(cur%2);
        i++;
		j++;
	}
	cout<<res<<"\n";
}

int main()
{
	int t=1;
	cin>>t;
	while(t--)
	myfun();
	return 0;
}
``

Tester's (Lavish Gupta) Solution
``#include <bits/stdc++.h>
using namespace std;
#define ll long long

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

const int MAX_T = 10;
const int MAX_N = 200000;
const int MAX_SUM_N = 100000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll z = 1000000007;
ll sum_nk = 0 ;

void solve()
{
    int n = readIntSp(1 , MAX_N) ;
    int k = readIntLn(1 , n) ;

    sum_nk += (1LL * n * k) ;
    max_n = max(n , max_n) ;
    sum_n += n ;

    string str = readStringLn(n , n) ;
    for(int i = 0 ; i < n ; i++)
    {
        assert(str[i] == '0' || str[i] == '1') ;
    }

    int cnt[n] ;
    cnt[0] = (str[0] == '1') ;

    for(int i = 1 ; i < n ; i++)
    {
        cnt[i] = cnt[i-1] + (str[i] == '1') ;
    }

    int len = n-k+1, ans = 0 ;
    for(int l = 0 ; l < n ; l++)
    {
        int r = l+len-1 ;
        if(r >= n)
            break ;
        ll curr_cnt = cnt[r] ;
        if(l > 0)
            curr_cnt -= cnt[l-1] ;
        ans += curr_cnt%2 ;
    }

    cout << ans << '\n' ;
    return ;
}

signed main()
{
    //fast;
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t = 1;

    t = readIntLn(1,MAX_T);

    for(int i=1;i<=t;i++)
    {
        solve() ;
    }

    assert(getchar() == -1);
    // assert(sum_n <= MAX_SUM_N);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    cerr << "Sum of product : " << sum_nk << '\n' ;
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Tester's (Takuki Kurokawa) Solution
``#include <bits/stdc++.h>
using namespace std;
#ifdef tabr
#include "library/debug.cpp"
#else
#define debug(...)
#endif

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    int tt;
    cin >> tt;
    while (tt--) {
        int n, k;
        cin >> n >> k;
        string s;
        cin >> s;
        vector<int> pref(k + 1);
        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                pref[max(0, i - (n - k))] ^= 1;
                pref[min(k, i + 1)] ^= 1;
            }
        }
        for (int i = 0; i < k; i++) {
            pref[i + 1] ^= pref[i];
        }
        cout << accumulate(pref.begin(), pref.end(), 0) << '\n';
    }
    return 0;
}
``

</details>
