# Divisors and Reciprocals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVREC |
| Difficulty Rating | 1848 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [DIVREC](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/DIVREC) |

---

## Problem Statement

Alice is teaching Bob maths via a game called $N$-guesser.

Alice has a positive integer $N$ which Bob needs to guess. She gives him two pieces of information with which to do this:

- A positive integer $X$, which denotes the sum of divisors of $N$.
- Two positive integers $A$ and $B$, which denote that the sum of reciprocals of divisors of $N$ is $A/B$.

Bob either needs to guess $N$ or tell that no such number exists.

It can be shown that if a valid $N$ exists, it is unique.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing three space-separated integers $X, A, B$.

---

## Output Format

For each test case, output a new line containing the answer — Alice's number $N$, or $-1$ if no such number exists.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \leq 10^9$
- $1 \leq A, B \leq 10^9$
- $\gcd(A, B) = 1$

---

## Examples

**Example 1**

**Input**

```text
2
4 4 3
4 1 1
```

**Output**

```text
3
-1
```

**Explanation**

**Test case $1$:** The divisors of $3$ are $1$ and $3$. Their sum is $4$ and the sum of their reciprocals is $4/3$.

**Test case $2$:** It can be proved that no positive integer $N$ exists whose divisors sum to $4$ and reciprocals of divisors sum to $1$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 4 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 1 1
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[https://www.codechef.com/START24C/problems/DIVREC](https://www.codechef.com/START24C/problems/DIVREC)

Setter: [ Harsh Vardhan Goenka](https://www.codechef.com/users/harsh2511)

Tester: [Aryan Chaudhary](https://www.codechef.com/users/aryanc403)

Editorialist: [Rishabh Gupta](https://www.codechef.com/users/rishabhdevil)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice is teaching Bob maths via a game called N-guesser.

Alice has a number N which Bob needs to guess.

Alice gives Bob a number X which represents the sum of divisors of N. Alice further provides Bob with A and B where A/B represents the sum of reciprocals of divisors of N.

Bob either needs to guess number N or tell that no such number exists.

#
[](#explanation-5)EXPLANATION:

The divisors of a number n are of the form a_1, n/a_1,  a_2, n/a_2, a_3, n/a_3 …sqrt(n) (only if it divides n). So, the sum of reciprocal of the divisors of a number is nothing but the sum of divisors of the number divided by the number n itself.

So, we can the get the number n as X*B/A. But, we have to check that this n yields the same sum of the divisors as given input X, which will require O(sqrt(n)) time.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(sqrt(n)) for each test case.

#
[](#solution-7)SOLUTION:

 Setter's Solution
``#include <bits/stdc++.h>
using namespace std;
int main(){
    long long t;
    cin>>t;
    while(t--){
        long long n,x,a,b;
        cin>>x>>a>>b;
        long long c=gcd(a,b);
        while(c!=1){
            c=c;
        }
        n=(x*b);
        if(n%a!=0){
            cout<<"-1\n";
            continue;
        }
        n/=a;
        if(n>1e9){
            cout<<"-1\n";
            continue;
        }
        long long sum=0ll;
        for(long long i=1;i*i<=n;i++){
            if(n%i==0){
                sum+=i;
                if(i!=n/i)
                    sum+=n/i;
            }
        }
        if(sum==x)
            cout<<n<<"\n";
        else
            cout<<"-1\n";
    }
}
``

 Editorialist''s Solution
``#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define dd double
#define endl "\n"
#define pb push_back
#define all(v) v.begin(),v.end()
#define mp make_pair
#define fi first
#define se second
#define vll vector<ll>
#define pll pair<ll,ll>
#define fo(i,n) for(int i=0;i<n;i++)
#define fo1(i,n) for(int i=1;i<=n;i++)
ll mod=1000000007;
ll n,k,t,m,q,flag=0;
ll power(ll a,ll b) {ll res=1;a%=mod; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%mod;a=a*a%mod;}return res;}
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/tree_policy.hpp>
// using namespace __gnu_pbds;
// #define ordered_set tree<int, null_type,less<int>, rb_tree_tag,tree_order_statistics_node_update>
// ordered_set s ; s.order_of_key(a) -- no. of elements strictly less than a
// s.find_by_order(i) -- itertor to ith element (0 indexed)
ll min(ll a,ll b){if(a>b)return b;else return a;}
ll max(ll a,ll b){if(a>b)return a;else return b;}
ll gcd(ll a , ll b){ if(b > a) return gcd(b , a) ; if(b == 0) return a ; return gcd(b , a%b) ;}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifdef NOOBxCODER
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #else
    #define NOOBxCODER 0
    #endif
    cin>>t;
    //t=1;
    while(t--){
        ll a,b,c;
        cin>>a>>b>>c;

        if(a%b !=0 || c>b){cout<<-1<<endl; continue;}
        c *= a/b;

        ll sum=0;
        for(int i=1;i*i<=c; i++){
            if(c%i!=0)continue;
            if(i*i==c)sum+=i;
            else sum+= i + c/i;
        }
        if(sum == a)cout<<c<<endl;
        else cout<<-1<<endl;

    }
    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";
    return 0;
}

``

</details>
