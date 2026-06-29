# Distinct Elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DISTELE |
| Difficulty Rating | 1762 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [DISTELE](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/DISTELE) |

---

## Problem Statement

You are given an array $A$ containing $N$ integers. A [subsequence](https://en.wikipedia.org/wiki/Subsequence) of this array is called *good* if all the elements of this subsequence are distinct.

Find the number of *good* non-empty subsequences of $A$. This number can be large, so report it modulo $10^9 + 7$.

Note that two subsequences are considered different if they differ in the indices chosen. For example, in the array $[1, 1]$ there are 3 different non-empty subsequences: $[1]$ (the first element), $[1]$ (the second element) and $[1, 1]$. Out of these three subsequences, the first two are good and the third is not.

---

## Input Format

- The first line contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, denoting the number of elements in $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer — the number of good subsequences modulo $10^9 + 7$

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ over all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
2
2
1 1
2
1 2
```

**Output**

```text
2
3
```

**Explanation**

- **Test Case $1$**: Explained in the problem statement.

- **Test Case $2$**: There are 3 non-empty subsequences: $[1]$, $[2]$ and $[1, 2]$. All three subsequences are good.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 1
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DISTELE)

[Contest: Division 1](https://www.codechef.com/START19A/problems/DISTELE)

[Contest: Division 2](https://www.codechef.com/START19B/problems/DISTELE)

[Contest: Division 3](https://www.codechef.com/START19C/problems/DISTELE)

***Authors:*** [Lavish Gupta](https://www.codechef.com/users/lavish315)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Sorting or maps/dictionaries

#
[](#problem-4)PROBLEM:

A non-empty subsequence of an array is said to be *good* if all its elements are distinct. Given an array A, count the number of *good* subsequences it has.

#
[](#quick-explanation-5)QUICK EXPLANATION:

Let F_x denote the number of times x occurs in the array. The answer is

\prod_{x} (1 + F_x) - 1

where the product is taken over all x which appear in the array.

#
[](#explanation-6)EXPLANATION:

Let F_x denote the number of times x appears in A.

Checking every subsequence of A for whether it’s good or not is obviously going to be too slow, since there are 2^N of them in total.

Let’s look at it differently. Consider some good subsequence S. It must have distinct elements, so let’s look at them one by one.

- Either S contains 1, or it doesn’t. If it does contain 1, there are F_1 choices for which index this 1 is chosen to be. So, in total this gives us F_1 + 1 possibilities for 1.

- Either S contains 2, or it doesn’t. If it does, there are F_2 choices for the index of 2. Once again, this gives us F_2 + 1 possibilities.

- Similarly, it either doesn’t contain 3; and if it does contain 3, there are F_3 choices for it. Again, F_3 + 1 possibilities for 3.

\vdots

So in general, considering some integer x, there are F_x + 1 possibilities provided by it — either x is not present at all, or there are F_x possible indices from where to choose x.

These choices are independent for each x, which means the total number of possibilities is (F_1 + 1)\cdot (F_2 + 1) \cdot \ldots \cdot (F_M + 1) where M is the maximum possible number in A (in this case, M = 10^6).

Note that this product also allows the choice of the empty subset - where we choose not to take any element. To exclude this case, subtract 1 from the above product.

The complexity of our solution (so far) is \mathcal{O}(M) per test case. However, there can be up to 10^5 test cases, and M = 10^6 so this isn’t quite fast enough.

##
[](#optimizing-further-7)OPTIMIZING FURTHER

The formula given above correctly computes the answer but is too slow. To optimize it, note that we don’t need to care about elements that don’t appear in the array, because they always contribute 1 to the product.

This allows us to optimize the computation in several ways, two of which are mentioned below.

Method 1: Maps

By far the simplest way to optimize the computation is to use maps (`std::map` or `std::unordered_map` in C++, `TreeMap` or `HashMap` in Java, `dict` in python) to compute the frequencies of the elements, and then just iterate over these maps. This ensures that we only consider elements that occur in the array at least once, of which there can be at most N.

Building the frequency table takes \mathcal{O}(N\log N) (or expected \mathcal{O}(N), if hashmaps are used), and the computation of the product is \mathcal{O}(N) afterward. The sum of N across all tests is bounded so this is fast enough.

Method 2: Sorting

It is also possible to accomplish this without any fancy data structures, with the help of sorting.

Note that all we really want to do is compute the frequencies of elements of A.

Suppose we sort A. Then, all equal elements will be present adjacent to each other.

This allows us to apply a simple two-pointer algorithm (or binary search) to find all segments of equal elements, and once we know those lengths we simply compute the desired product to solve the problem.

Once again, the time complexity of this is \mathcal{O}(N\log N) for the sort and \mathcal{O}(N) afterward, which is more than enough.

#
[](#time-complexity-8)TIME COMPLEXITY:

\mathcal{O}(N\log N) per test case.

#
[](#solutions-9)SOLUTIONS:

Setter's Solution (C++)
``
#include <bits/stdc++.h>
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

const int MAX_T = 100000;
const int MAX_N = 100000;
const int MAX_SUM_N = 1000000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll z = 1000000007;
int freq[1000005] ;

void solve()
{

    int n = readIntLn(1 , MAX_N) ;
    max_n = max(max_n , n) ;
    sum_n += n ;

    int arr[n] ;
    ll ans = 1 ;
    vector<int> v ;
    for(int i = 0 ; i < n-1 ; i++)
    {
        arr[i] = readIntSp(1 , 1000000);
        freq[arr[i]]++ ;
        if(freq[arr[i]] == 1)
            v.push_back(arr[i]) ;
    }
    arr[n-1] = readIntLn(1 , 1000000);
    freq[arr[n-1]]++ ;
    if(freq[arr[n-1]] == 1)
        v.push_back(arr[n-1]) ;

    for(int i = 0 ; i < v.size() ; i++)
    {
        int cnt = freq[v[i]]+1;
        ans = (ans * cnt)%z ;
        freq[v[i]] = 0 ;
    }
    cout << (ans+z-1)%z << endl ;
    return ;
}

signed main()
{
    // fast;
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
    assert(sum_n <= MAX_SUM_N);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Tester's Solution (C++)
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

int sum_len = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;

const ll MX=200000;
ll fac[MX], ifac[MX];

const ll mod = 1000000007;

ll po(ll x, ll n ){
    ll ans=1;
     while(n>0){
        if(n&1) ans=(ans*x)%mod;
        x=(x*x)%mod;
        n/=2;
     }
     return ans;
}

void solve()
{
  int n;
  n = readIntLn(1, 1e5);
  sum_len+=n;
  max_n = max(max_n, n);
  ll a[n];
  for(int i=0; i<n-1; i++){
    a[i] = readIntSp(1, 1e9);
  }
  a[n-1] = readIntLn(1,1e9);

  map<ll,ll> mm;
  for(int i=0; i<n; i++){
    mm[a[i]]++;
  }

  ll ans = 1;
  for(auto h:mm){
    ans*=(h.second+1);
    ans%=mod;
  }
  ans--;
  ans+=mod;
  ans%=mod;
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

    t = readIntLn(1,1e5);

    for(int i=1;i<=t;i++)
    {
       solve();
    }

    assert(getchar() == -1);
    assert(sum_len <= 1e6);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_len << '\n';
    cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    //cerr<<"Answered yes : " << yess << '\n';
    //cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution (Python)
``for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 1
    mod = int(10**9 + 7)
    i = 0
    while i < n:
        j = i
        while j < n and a[j] == a[i]:
            j += 1
        ans *= (j - i + 1)
        ans %= mod
        i = j
    ans += mod - 1
    print(ans%mod)
``

</details>
