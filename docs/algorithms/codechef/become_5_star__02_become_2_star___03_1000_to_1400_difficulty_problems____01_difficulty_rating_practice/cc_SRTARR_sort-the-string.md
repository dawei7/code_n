# Sort the String

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SRTARR |
| Difficulty Rating | 1112 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [SRTARR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/SRTARR) |

---

## Problem Statement

You have a **binary** string $S$ of length $N$. In one operation you can select a substring of $S$ and **reverse** it. For example, on reversing the substring $S[2,4]$ for $S=11000$, we change $1 \textcolor{red}{100} 0 \rightarrow 1 \textcolor{red}{001} 0$.

Find the **minimum** number of operations required to sort this binary string.
It can be proven that the string can always be sorted using the above operation finite number of times.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of $2$ lines of input.
    - The first line of each test case contains a single integer $N$ — the length of the binary string.
    - The second line of each test case contains a binary string $S$ of length $N$.

---

## Output Format

For each test case, output on a new line — the minimum number of operations required to sort the binary string.

---

## Constraints

- $1 \leq T \leq 2\cdot 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- Sum of $N$ over all test cases does not exceed $10^6$.
- String $S$ consists of only '$0$'s and '$1$'s.

---

## Examples

**Example 1**

**Input**

```text
4
3
000
4
1001
4
1010
6
010101
```

**Output**

```text
0
1
2
2
```

**Explanation**

**Test case $1$:** The string is already sorted, hence, zero operations are required to sort it.

**Test case $2$:** We can sort the string in the following way:  $\textcolor{red}{100} 1$ $\rightarrow$ $0011$.

**Test case $3$:** We can sort the string in the following way:
$1 \textcolor{red}{01} 0$ $\rightarrow$ $\textcolor{red}{1100}$ $\rightarrow$ $0011$.
It can be proven that this string cannot be sorted in less than $2$ operations.

**Test case $4$:** We can sort the string in the following way:
$0 \textcolor{red}{1010}1$ $\rightarrow$ $00 \textcolor{red}{10}11$ $\rightarrow$ $000111$.
It can be proven that this string cannot be sorted in less than $2$ operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
000
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
4
1001
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
1010
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
6
010101
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

[Contest Division 1](https://www.codechef.com/START46A/problems/SRTARR)

[Contest Division 2](https://www.codechef.com/START46B/problems/SRTARR)

[Contest Division 3](https://www.codechef.com/START46C/problems/SRTARR)

[Contest Division 4](https://www.codechef.com/START46D/problems/SRTARR)

[Practice](https://www.codechef.com/problems/SRTARR)

**Setter:** [Shivansh Agarwal](https://www.codechef.com/users/shivansh0809)

**Testers:** [Nishank Suresh](https://www.codechef.com/users/iceknight1093) and [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Anish Ashish Kasegaonkar](https://www.codechef.com/users/anish_ak)

#
[](#difficulty-2)DIFFICULTY

1112

#
[](#prerequisites-3)PREREQUISITES

Strings, Greedy

#
[](#problem-4)PROBLEM

You are given a binary string S of length N. You can reverse any substring of S in one operation, find the minimum number of operations required to sort S.

#
[](#explanation-5)EXPLANATION

###
[](#hint-6)Hint

The resulting string should be such that all '0's appear consecutively before a ‘1’ appears.

###
[](#detailed-explanation-7)Detailed Explanation

To sort S, we can iterate through the string and reverse every leftmost instance of “1,1,...,1,0,...,0,0”, i.e. a substring of S with consecutive '1's and then consecutive '0's. This is guaranteed to sort S in the minimum number of operations.

Intuition for correctness

While iterating through S, if you reverse an instance of “1,1,...,1,0,...,0,0” then you would obtain a prefix of '0's, as we are essentially *pushing forward* the occurrences of '1's that are present before a ‘0’. So, the resulting string would have a prefix of '0's and a suffix of '1's, and hence would be sorted in the minimum number of operations.

This simply reduces to counting the number of occurrences of “10” that appear in the string and printing it. This is because the number of "1,1,...,1,0,...,0,0"s that appear in the string are the same as the number of "10"s that appear in the string.

#
[](#time-complexity-8)TIME COMPLEXITY

The time complexity is O(|S|) per test case.

#
[](#solutions-9)SOLUTIONS

Setter's Solution
``// author: Shivansh Agarwal
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fastio ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0)
const int mod = 1000000007;
const double EPS = 1e-7;

int32_t main()
{
    fastio;
    auto begin = std::chrono::high_resolution_clock::now();
    int tt;
    cin >> tt;
    while(tt--)
    {
        int n;
        cin >> n;
        string s;
        cin >> s;
        int ans = 0;
        for (int i = 0; i < n - 1;i++) if(s[i] == '1' && s[i+1] == '0')
                ans++;
        cout << ans << "\n";
    }
    auto end = std::chrono::high_resolution_clock::now();
    cerr << setprecision(4) << fixed;
    cerr << "Execution time: " << std::chrono::duration_cast<std::chrono::duration<double>>(end - begin).count() << " seconds" << endl;
}
``

Tester's Solution 1
``#include <bits/stdc++.h>
using namespace std;

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

const int MAX_T = 1e5;
const int MAX_N = 1e5;
const int MAX_SUM_LEN = 1e5;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define ff first
#define ss second
#define mp make_pair
#define ll long long
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)
#define pb push_back

int sum_n = 0, sum_m = 0;
int max_n = 0, max_m = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll mod = 998244353;

void solve(){
    int n = readIntLn(1,2e5);
    sum_n+=n;

    string s = readStringLn(n,n);
    for(auto h:s) assert(h=='0' || h=='1');

    int ans=0;
    rep_a(i,1,n){
        if(s[i]=='0' && s[i-1]=='1') ans++;
    }

    cout<<ans<<'\n';

}

signed main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r" , stdin);
    freopen("output.txt", "w" , stdout);
    #endif
    fast;

    int t = 1;

    t = readIntLn(1,2e5);

    for(int i=1;i<=t;i++)
    {
    solve();
    }

    assert(getchar() == -1);
    assert(sum_n<=1e6);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n <<" "<<sum_m<<'\n';
    // cerr<<"Maximum length : " << max_n <<'\n';
    // // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's Solution 2
``for _ in range(int(input())):
    n = int(input())
    print(input().count('10'))
``

Feel free to share your approach. Suggestions are welcomed.

</details>
