# Chefs Favourite Function

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFFFUNC |
| Difficulty Rating | 2316 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [CHEFFFUNC](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/CHEFFFUNC) |

---

## Problem Statement

Chef's new friend hErd gave him two functions $f$ and $g$.

- The function $f$ is defined over $x$ $(x\geq 1)$ as:
$$
f(x) = \begin{cases}
0, & \text{if } x = 1 \\
f\left( \frac{x}{2} \right) + 1, & \text{if } x \text{ is even} \\
f\left( \left\lfloor \frac{x}{2} \right\rfloor \right), & \text{if } x \text{ is odd} \\
\end{cases}
$$

- The function $g$ is defined over $x$ $(x\geq 1)$ as:
$$
g(x) = \begin{cases}
1, & \text{if } x = 1 \\
2\cdot g\left( \frac{x}{2} \right) + 1, & \text{if } x \text{ is even} \\
2\cdot g\left( \left\lfloor \frac{x}{2} \right\rfloor \right), & \text{if } x \text{ is odd} \\
\end{cases}
$$

where $\left\lfloor z \right\rfloor$, denotes the greatest integer less than or equal to $z$.

He also gave Chef two integers $L$ and $R$. Chef has to find the **maximum** value of $f(x)+g(x)$ for $L \leq x \leq R$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The only line of each test case contains two space-separated integers $L$ and $R$, as mentioned in the statement.

---

## Output Format

For each test case, output on a new line the **maximum** value of $f(x)+g(x)$ for $L \leq x \leq R$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq L \leq R \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
1 1
1 2
1 20
```

**Output**

```text
1
4
35
```

**Explanation**

**Test case $1$:** $f(1)=0$ and $g(1)=1$. Hence, $f(x) + g(x) = 1$.

**Test case $2$:** There are $2$ possible values of $x$.
- $x = 1$: $f(1)+g(1)=1$
- $x = 2$: $f(2)+g(2)=(f(1) + 1) + (2\cdot g(1) + 1) = 1 + 3 = 4$.

Hence the maximum value of $f(x) + g(x) = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 2
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
1 20
```

**Output for this case**

```text
35
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CHEFFFUNC)

[Contest: Division 1](https://www.codechef.com/START75A/problems/CHEFFFUNC)

[Contest: Division 2](https://www.codechef.com/START75B/problems/CHEFFFUNC)

[Contest: Division 3](https://www.codechef.com/START75C/problems/CHEFFFUNC)

[Contest: Division 4](https://www.codechef.com/START75D/problems/CHEFFFUNC)

***Author:*** [indreshsingh](https://www.codechef.com/users/indreshsingh)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

Familiarity with bitwise operations

#
[](#problem-4)PROBLEM:

You’re given two functions f and g, whose definitions can be found in the statement.

You’re also given integers L and R.

Find the maximum value of f(x) + g(x) across all L \leq x \leq R.

#
[](#explanation-5)EXPLANATION:

Our first order of business should be figuring out what the functions f and g actually are, since they’re given to us in a recursive form.

This can be done by analyzing them a bit (or computing a few early values and putting the sequence into [OEIS](https://oeis.org/)  )

Computing f(x)

Looking at the definition of f should make you think of binary, since computing it requires us to divide by 2 each time.

You should quickly notice that, in terms of binary:

- If the last digit is 0 (meaning the number is even), we add 1 to the answer; otherwise we add 0 to the answer.

- Then, we delete the last digit (which corresponds to dividing by 2)

In other words, f(x) is simply the number of zeros in the binary representation of x.

Computing g(x)

Looking at the definition of g, we see the following:

- Suppose x = 2k. Then, g(x) = 2\cdot g(k)+1.

- Suppose x = 2k+1. Then, g(x) = 2\cdot g(k).

Notice that these are suspiciously similar: obtaining x from k is exactly the *opposite* of obtaining g(x) from g(k); in terms of adding 1 after multiplying by 2.

Now let’s contextualize this in terms of binary.

Any integer x can be obtained by starting with 1, then continually multiplying by 2 and adding either zero or one, depending on whether we need to add a new bit or not.

We can thus build g(x) as we build x; except that we add a bit to g(x) if and only if we *don’t* add a bit to x.

In other words, g(x) is obtained by *inverting all the bits of x*, except for the highest bit.

For example, if x = 17 = 1\color{red}{0001}\color{black}{_2}, then g(x) = 1\color{red}{1110}\color{black}{_2} = 30.

Now that we know f and g, let’s observe a couple of their properties.

-
f(x) is pretty small: since x \leq R \leq 10^9, we have f(x) \leq 30.

-
f(x) is largest when x is a power of 2.

- If x+1 is not a power of 2, then g(x) \gt g(x+1).

- In fact, if x+1 is not a power of 2, then g(x) = g(x+1)+1.

- If x+1 is a power of 2, then g(x) \lt g(x+1).

- In this case, g(x+1) is larger than g(y) for every y \leq x.

The above discussion tells us that to maximize f(x)+g(x), ideally x should be a power of 2.

So, if the range [L, R] contains a power of 2, simply choose x to be the largest power of 2 in this range and compute f(x) + g(x) for it — that’s the answer.

Now, what about when [L, R] doesn’t contain a power of 2?

Notice our third point above: g is a strictly decreasing function on this range, i.e, g(L)\gt g(L+1) \gt \ldots \gt g(R).

Also recall that f can only take values upto 30.

So, for any x \gt L+31, f(x)+g(x) can never be larger than f(L)+g(L), since f cannot make up for the difference between the g-values.

So, it’s enough to check for x = L, L+1, \ldots, L+31.

Compute f(x)+g(x) for each one, take the maximum of them all.

Computing f(x) and/or g(x) for a given x can be done in \mathcal{O}(\log x) using the given recursive definitions.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(\log^2 R) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int               long long
#define pb                push_back
#define ppb               pop_back
#define pf                push_front
#define ppf               pop_front
#define all(x)            (x).begin(),(x).end()
#define uniq(v)           (v).erase(unique(all(v)),(v).end())
#define sz(x)             (int)((x).size())
#define fr                first
#define sc                second
#define pii               pair<int,int>
#define rep(i,a,b)        for(int i=a;i<b;i++)
#define mem1(a)           memset(a,-1,sizeof(a))
#define mem0(a)           memset(a,0,sizeof(a))
#define ppc               __builtin_popcount
#define ppcll             __builtin_popcountll
#define debug(x)  cout<<(x)<<'\n';

template<typename T1,typename T2>istream& operator>>(istream& in,pair<T1,T2> &a){in>>a.fr>>a.sc;return in;}
template<typename T1,typename T2>ostream& operator<<(ostream& out,pair<T1,T2> a){out<<a.fr<<" "<<a.sc;return out;}
template<typename T,typename T1>T amax(T &a,T1 b){if(b>a)a=b;return a;}
template<typename T,typename T1>T amin(T &a,T1 b){if(b<a)a=b;return a;}

const long long INF=1e18;
const int32_t M=1e9+7;
const int32_t MM=998244353;

const int N=0;

//function which gives binary length of n ,eg n=8->1000 length is 4
int countBits(int n)
{
    int count = 0;
   while (n)
   {
        count++;
        n >>= 1;
    }
    return count;
}

//binary representation of n
string convertTobinary(int n)
{

string b;

while(n)
{
    if(n%2) b.pb('1');
    else b.pb('0');
    n=n/2;
}

reverse(all(b));
return b;

}

void solve(){

int l,r;
cin>>l>>r;

int length_l,length_r;

length_l=countBits(l);
length_r=countBits(r);

if(length_l<length_r) // eg : l=1,r=3->11 we can make all zeroes except first digit we get 10 so ans=1
{

cout<<length_r-1+(1ll<<(length_r))-1<<'\n';
return;

}

string sl,sr; //binary representation of l and r
int length=length_r;

sl=convertTobinary(l);
sr=convertTobinary(r);
int ans=0;
for(int i=l;i<=min(40+l,r);i++)
{

int j=i;
int curr=0;
int k=0;
while(j)
{

if(j==1)
{
    curr+=1ll<<k;
}
else if(j%2==0)
{
    curr+=1ll<<k;
}
j=j/2;
k++;

}
j=i;
while(j)
{

if(j%2==0) curr++;
j=j/2;
}

ans=max(ans,curr);

}
cout<<ans<<'\n';

}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);cout.tie(0);
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    #ifdef SIEVE
        sieve();
    #endif
    #ifdef NCR
        init();
    #endif
    int t=1;
    cin>>t;
    while(t--) solve();
    return 0;
}
``

Editorialist's code (Python)
``def f(x):
    ret = 0
    while x > 0:
        ret += 1 - x%2
        x //= 2
    return ret

def g(x):
    ret = x
    for i in range(30):
        if 2**(i+1) > x: break
        if x & (1 << i): x -= 1 << i
        else: x += 1 << i
    return x

import sys
input = sys.stdin.readline
for _ in range(int(input())):
    l, r = map(int, input().split())
    ans = 0
    if len(bin(l)) < len(bin(r)): # [L, R] contains a power of 2
        pw = len(bin(r))-3
        x = 2**pw
        ans = 2*x-1 + pw
    else:
        pw = 2**(len(bin(l))-3)
        for i in range(31):
            if l+i > r: break
            ans = max(ans, f(l+i) + g(l+i))
    print(ans)
``

</details>
