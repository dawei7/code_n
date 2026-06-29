# Chroma Swap

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ASH57 |
| Difficulty Rating | 2271 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [ASH57](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/ASH57) |

---

## Problem Statement

You have two arrays $A = A_1, A_2, \ldots, A_N$ and $B = B_1, B_2, \ldots, B_N$. Each of these elements also has a color associated with them, which is an integer. This is denoted by the arrays $ColorA_1, ColorA_2, \ldots, ColorA_N$, and $ColorB_1, ColorB_2, \ldots, ColorB_N$.

In a single operation, you can swap any element of array $A$ with any element of array $B$, if they have the same color.

Your goal is to do as many operations as you want, and eventually have the elements in array $A$ be in non-decreasing order. That is, after you are done with the operations, you want $A_1 \leq A_2 \leq \ldots \leq A_N$.

Output "Yes" if this is possible to do so, and "No" otherwise.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of five lines of input.
    - The first line of each test case contains a single integer $N$, denoting the size of the arrays.
    - The next line has $N$ integers: $A_1, A_2, \ldots, A_N$
    - The next line has $N$ integers: $ColorA_1, ColorA_2, \ldots, ColorA_N$
    - The next line has $N$ integers: $B_1, B_2, \ldots, B_N$
    - The next line has $N$ integers: $ColorB_1, ColorB_2, \ldots, ColorB_N$

---

## Output Format

- For each testcase, in a new line, output "Yes" if it is possible to end up with the array $A$ having elements in non-decreasing order. Else, print "No".
- You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- $0 \leq ColorA_i, ColorB_i \leq 2N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2 
3 2
1 2 
1 2 
1 1
1
13
1
23
1
2
2 1 
2 1 
2 1
2 1
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Testcase 1:** The given arrays are:
- $A = [3, 2]$
- $ColorA = [1, 2]$
- $B = [1, 2]$
- $ColorB = [1, 1]$

$A_1$ and $B_1$ have the same color ($1$). So, we can swap them, and now we have the arrays as:
- $A = [1, 2]$
- $B = [3, 2]$

Now, array $A$ is sorted in non-decreasing order. So, it is possible to achieve this, and hence the answer is "Yes".

**Testcase 2:** The given arrays are:
- $A = [13]$
- $ColorA = [1]$
- $B = [23]$
- $ColorB = [1]$

We see that the array $A$ is already sorted. Hence, the answer is "Yes".

**Testcase 3:** The given arrays are:
- $A = [2, 1]$
- $ColorA = [2, 1]$
- $B = [2, 1]$
- $ColorB = [2, 1]$

We see that no matter how many operations we do, the two arrays will remain the same, and $A$ can never be sorted. Hence the answer is "No".

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
3 2
1 2
1 2
1 1
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
1
13
1
23
1
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
2
2 1
2 1
2 1
2 1
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ASH57)

[Contest: Division 1](https://www.codechef.com/START109A/problems/ASH57)

[Contest: Division 2](https://www.codechef.com/START109B/problems/ASH57)

[Contest: Division 3](https://www.codechef.com/START109C/problems/ASH57)

[Contest: Division 4](https://www.codechef.com/START109D/problems/ASH57)

***Author:*** [aniketash57](https://www.codechef.com/users/aniketash57)

***Tester:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Sorting/multisets, and maybe binary search

# [](#problem-4)PROBLEM:

You’re given two arrays A and B, both of length N.

Each element of both arrays also has a color, denoted by arrays c_A and c_B respectively.

In one move, you can pick indices i and j such that c_A[i] = c_B[j] and swap A_i with B_j.

Is it possible to reach a state where A_1 \leq A_2 \leq \ldots \leq A_N?

# [](#explanation-5)EXPLANATION:

Consider a fixed index i.

- If c_A[i] doesn’t appear in c_B at all, the value at this index can’t be swapped using our operation, and is fixed.

- If c_A[i] *does* appear in c_B, this color is ‘free’ - all the values at any index with this color can be freely moved around between indices.

Using this observation, let’s try to build a sorted array out of A.

Let’s go from left to right, i.e, iterate index i from 1 to N.

When at index i, our aim is to place something there that’s \geq A_{i-1} (for convenience, assume A_0 = 0).

For that,

- If A_i is a ‘fixed’ index as described above, we have no choice and can’t change it.

So, if A_i \lt A_{i-1}, the array can’t be sorted.

- Otherwise, recall that we can freely choose A_i to be any value that has the same color as c_A[i].

We want something that’s \geq A_{i-1} of course, but it’s also easy to see that we don’t want it to be too large, for that will make it harder for future elements to be sorted.

So, the optimal strategy is to choose the smallest value that’s \geq A_{i-1}.

Of course, if such a value doesn’t exist, the array can’t be sorted.

The only slow part here is finding the smallest value that’s \geq A_{i-1}.

To speed this up, store a sorted list of values corresponding to each color.

Then, finding the appropriate element can be done quickly with a simple binary search.

You also need to delete the chosen element so it can’t be used again; so the appropriate data structure is a multiset.

It’s also possible to implement this without a multiset or binary search, by maintaining pointers for each list corresponding to the last used element and incrementing them as required.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``/*
ANIKET ASH
*/
#include<bits/stdc++.h>
using namespace std;
using namespace chrono;

#define ios ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define int long long int
#define pb push_back
#define pf push_front
#define ppb pop_back
#define ppf pop_front
const int mod= 1e9+7;
#define rep(i,a,b) for(int i = a; i < b; i++)
#define mset(a , b) memset(a , b , sizeof(a))
#define mp make_pair
#define ff            first
#define ss            second
#define nl '\n'
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#ifdef quagmire
#include<bits/debug.h>
#else
#define dbg(x)
#endif
typedef set <int> si;
typedef vector <int> vi;
typedef vector <vi> vvi;
typedef multiset <int> msi;
typedef vector <string> vs;
typedef pair <int , int> pii;
typedef vector <char> vch;
typedef vector <pair <int, int>> vpi;
// typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update > pbds; // find_by_order, order_of_key//for multiset less_equal<int>

const int inf =1e18;
const double PI=2*acosl(0);
//overloads
template<typename T1, typename T2> ostream& operator<<(ostream& out, const pair<T1, T2>& x) {return out << x.ff << ' ' << x.ss;}//pairs input k liye hai
template<typename T1, typename T2> istream& operator>>(istream& in, pair<T1, T2>& x) {return in >> x.ff >> x.ss;}//cout<<pair<int,int> p<<nl;
template<typename T> istream& operator>>(istream& in, vector<T>& a) {for(auto &x : a) in >> x; return in;};//cin>> vi v>>nl;
template<typename T> ostream& operator<<(ostream& out, vector<T>& a) {for(auto &x : a) out << x << ' '; return out;};//cout<<v<<nl;
/*----------------------------- # --- MATH ALGORITHMS --- # -----------------------------*/
vector<int> sieve(int n) {int*arr = new int[n + 1](); vector<int> vect; for (int i = 2; i <= n; i++)if (arr[i] == 0) {vect.push_back(i); for (int j = 2 * i; j <= n; j += i)arr[j] = 1;} return vect;}
template <class T> T gcd(T a , T b){ while(a != 0){T temp = a; a = b % a; b = temp;}return b;}
template <class T> T egcd(T a , T b , T &x , T &y){T gcd , xt , yt;if(a == 0){gcd = b;x = 0 , y = 1;}else {gcd = egcd(b % a , a , xt , yt);x = yt - (b/a)*xt; y = xt;}return gcd;}
template <class T> T expo(T base , T exp , T m){T res = 1;base = base % m;while (exp > 0){if (exp & 1)res = (res*base) % m;exp = exp>>1;base = (base*base) % m;}return res;}
template <class T> T modinv(T a ){T x , y; egcd<T>(a , mod , x , y);while(x < 0) x += mod; while(x >= mod) x -= mod; return x;}
template <class T> bool rev(T a , T b){return a > b;}
template <class T> int maxpower(T a , T b){int ans = 0;while(a >0 && a % b == 0){ans++;a /= b;}return ans;}
template <class T> T mceil(T a, T b){if(a % b == 0) return a/b; else return a/b + 1;}
template <class T> T lcm(T a, T b){return (a*b)/gcd<T>(a, b);}
int modinv_prime(int a, int b) {return expo(a, b - 2,mod);}//modinvfermat
 int mod_add(int a, int b, int m) {a = a % m; b = b % m; return (((a + b) % m) + m) % m;}
int mod_mul(int a, int b, int m) {a = a % m; b = b % m; return (((a * b) % m) + m) % m;}
int mod_sub(int a, int b, int m) {a = a % m; b = b % m; return (((a - b) % m) + m) % m;}
int mod_div(int a, int b, int m) {a = a % m; b = b % m; return (mod_mul(a, modinv_prime(b, m), m) + m) % m;}
void solve()
{
  int n;
  cin>>n;
  vector<int> a(n),b(n);
  vector<int>colora(n),colorb(n);
  for(int i =0;i<n;i++) cin>>a[i];
  for(int i =0 ;i<n;i++) cin>>colora[i];
  for(int i = 0 ;i<n;i++) cin>>b[i];
  for(int i = 0;i<n;i++) cin>>colorb[i];
  map<int,multiset<int>> M;//stores color and set of elements having that color
  // dbg('a');
  for(int i =0; i<n;i++)
  {
    multiset<int> t;
    M[colorb[i]]= t;
  }
  // dbg(M);
  for(int i = 0 ;i<n;i++)
  {
    // if(M.count(colora[i]))
    auto it = M.find(colora[i]);
    if(it!=M.end())
    M[colora[i]].insert(a[i]);
    M[colorb[i]].insert(b[i]);
  }
  // dbg(M);
  // dbg('b');
  int prevElement = -1;
  for(int i = 0 ;i<n;i++)
  {
    // dbg(i);
    auto it = M.find(colora[i]);
    if(it==M.end())
    {
      if(a[i]>=prevElement)
      {
        prevElement=a[i];
      }
      else
      {
        cout<<"NO"<<"\n";
        return;
      }
      continue;
    }
    multiset<int> & s = it->second;
    auto ix = s.lower_bound(prevElement);
    if(ix==s.end())
    {
      cout<<"NO"<<"\n";
      return;
    }
    prevElement=*ix;
    s.erase(ix);
  }

  cout<<"YES"<<"\n";
}
int32_t main()
{
#ifdef quagmire
   freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
  freopen("error.txt", "w", stderr);
#endif
ios
int test_case=1;
cin>>test_case;
for(int _=1;_<=test_case;_++)
{
	solve();
}
return 0;
}
``

Editorialist's code (Python)
``import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cola = list((map(int, input().split())))
    b = list(map(int, input().split()))
    colb = list((map(int, input().split())))

    values = [ [] for _ in range(2*n+1)]
    canswap = set(colb)
    for i in range(n):
        values[cola[i]].append(a[i])
        values[colb[i]].append(b[i])
    for i in range(2*n+1): values[i] = sorted(values[i])[::-1]

    ans = []
    for i in range(n):
        if cola[i] not in canswap:
            ans.append(a[i])
            continue
        while values[cola[i]]:
            if len(ans) and values[cola[i]][-1] < ans[-1]:
                values[cola[i]].pop()
            else: break
        if values[cola[i]]:
            ans.append(values[cola[i]][-1])
            values[cola[i]].pop()
    if len(ans) == n and ans == sorted(ans):
        print('Yes')
    else:
        print('No')
``

</details>
