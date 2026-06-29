# Number Hunt

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NUMHUNT |
| Difficulty Rating | 1638 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [NUMHUNT](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/NUMHUNT) |

---

## Problem Statement

Given a positive integer $X$, find the **smallest** positive integer $Y$ satisfying all of the following conditions:
- $Y$ should not be a [prime](https://en.wikipedia.org/wiki/Prime_number);
- $Y$ should not be a [perfect square](https://en.wikipedia.org/wiki/Square_number);
- No [factor](https://en.wikipedia.org/wiki/Divisor) of $Y$ other than $1$ is less than $X$.

Note that $Y$ might not fit in a $32$ bit integer.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a positive integer $X$ as mentioned in the statement.

---

## Output Format

For each test case, output on a new line, the **smallest** positive integer $Y$ satisfying the given conditions.

Note that $Y$ might not fit in a $32$ bit integer.

---

## Constraints

- $1 \leq T \leq 5$
- $1 \leq X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
6
6
15
```

**Explanation**

**Test case $1$:** Let us consider all values of $Y$ in increasing order:
- $Y = 2$: It is a prime.
- $Y = 3$: It is a prime.
- $Y = 4$: It is a perfect square $(4 = 2^2)$.
- $Y = 5$: It is a prime.
- $Y = 6$: It is neither prime, nor a perfect square. The non-$1$ factors of $6$ are $2, 3$ and $6$, none of which are less than $X = 1$.

Thus, $6$ is the smallest integer satisfying the given conditions.

**Test case $2$:** $Y = 6$ has non-$1$ factors $2, 3,$ and $6$, none of which are less than $X = 2$.

**Test case $3$:** The smallest integer satisfying the conditions is $15$. The non-$1$ factors of $15$ are $3, 5$ and $15$, none of which are less than $X = 3$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
15
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/NUMHUNT)

[Contest: Division 1](https://www.codechef.com/START142A/problems/NUMHUNT)

[Contest: Division 2](https://www.codechef.com/START142B/problems/NUMHUNT)

[Contest: Division 3](https://www.codechef.com/START142C/problems/NUMHUNT)

[Contest: Division 4](https://www.codechef.com/START142D/problems/NUMHUNT)

***Author:*** [just_a_looser1](https://www.codechef.com/users/just_a_looser1)

***Tester:*** [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

Primality testing in \mathcal{O}(\sqrt X)

# [](#problem-4)PROBLEM:

You’re given a positive integer X.

Find the smallest positive integer Y that is not prime, not a square, and has no factors smaller than X other than 1.

# [](#explanation-5)EXPLANATION:

We’d like Y to be a non-prime, meaning it must either be a power of a prime, or have at least two different prime factors.

***Case 1***: Suppose Y is a power of a prime, i.e, Y = p^k for some prime p and non-negative integer k.

- Y shouldn’t be a prime, so k cannot equal 1.

- Y shouldn’t be a square, so k cannot be even.

This means the smallest possible value of k is k = 3, i.e, Y could be the cube of a prime.

Now, p is a prime factor of Y, and so should be \geq X as per our requirement.

Clearly, the best choice is to choose p as the *smallest* prime that’s \geq X.

***Case 2***: Suppose Y isn’t a prime power; meaning it has (at least) two distinct prime factors.

Note that we require all the factors of Y to be \geq X, so its prime factors should certainly be \geq X.

Recall that p was already the smallest prime that’s \geq X.

Let’s also find q \gt p as the smallest prime larger than p.

The number Y = p\cdot q is then the smallest number that can be formed as the product of distinct primes not less than X.

Combining the two cases, the answer is simply \min(p^3, p\cdot q) once p and q have been found.

That only leaves the task of actually finding p and q.

Notice that all we really need to do is find the smallest prime that’s \geq a given integer.

That can be done using brute force!

That is, to find the smallest prime p that’s \geq X, the following simple algorithm works:

- Initialize p = X.

- While p is not prime, increment p by 1.

Checking whether p is a prime can be done in \mathcal{O}(\sqrt p) time.

Since X \leq 10^9 for us, the this algorithm will check at most 282 values of p before it finds a prime, because the maximal [prime gap](https://en.wikipedia.org/wiki/Prime_gap#Numerical_results) is quite small.

As an aside, the fact that the prime gap is so small allows for the p^3 case to be discarded entirely - that is, the answer is always the product of the two smallest primes not smaller than X.

Intuitively, this is because q is always not much larger than p, so pq is similar in magnitude to p^2 and so much smaller than p^3.

It can be formally proved (for X upto 10^9) by verifying via bruteforce for smaller values (say, for X \leq 10^5); and utilizing the fact that q \leq p+300 for 10^5 \lt X \leq 10^9.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(600\sqrt X) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <iostream>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <utility>
#include <iomanip>
#include <sstream>
#include <bitset>
#include <cstdlib>
#include <iterator>
#include <algorithm>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <math.h>
#include <ctime>
#include <cstring>
#include <unordered_set>
#include <unordered_map>
#include <cassert>
#define int long long int
#define pb push_back
#define mp make_pair
#define mod 1000000007
#define vl vector <ll>
#define all(c) (c).begin(),(c).end()
using namespace std;

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

bool isprime(int x){
    if(x==1) return false;
    for(int i=2;i*i<=x;i++){
        if(x%i==0) return false;
    }
    return true;
}

void solve()
{
    int x=readInt(1,1000000000,'\n');
    long long ans = 1;
    long long first = -1;
    long long second = -1;
    for(int i = x; second == -1; i++){
        if(isprime(i)){
            if(first == -1){
                first = i;
            } else {
                second = i;
            }
        }
    }
    cerr << first << ' ' << second << '\n';
    ans = first*second;
    cout << ans;
}
int32_t main()
{
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios_base::sync_with_stdio(false);
    cin.tie(NULL),cout.tie(NULL);
    int T=readInt(1,5,'\n');
    while(T--){
        solve();
        cout<<'\n';
    }
    assert(getchar()==-1);
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
bool isPrime(int x){
    if(x == 1){
        return false;
    }
    for(int i = 2; i * i <= x; i++){
        if(x % i == 0){
            return false;
        }
    }
    return true;
}
int32_t main() {
	int t;
	cin>>t;
	while(t--){
	    int x;
	    cin>>x;
	    int i = x;
	    int a = -1;
	    int b;
	    while(true){
	        if(isPrime(i)){
	            if(a == -1){
	                a = i;
	            }else{
	                b = i;
	                break;
	            }
	        }
	        i++;
	    }
	    cout<<a * b<<"\n";
	}
}
``

Editorialist's code (Python)
``def prime(x):
    if x == 1: return 0
    for p in range(2, x):
        if p*p > x: break
        if x%p == 0: return 0
    return 1

for _ in range(int(input())):
    x = int(input())

    p = x
    while not prime(p): p += 1
    q = p+1
    while not prime(q): q += 1
    print(min(p*q, p**3))
``

</details>
