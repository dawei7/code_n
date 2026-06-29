# Indivisible Permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INDIPERM |
| Difficulty Rating | 1329 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Basic Programming |
| Official Link | [INDIPERM](https://www.codechef.com/practice/course/2to3stars/LP2TO301/problems/INDIPERM) |

---

## Problem Statement

You are given an integer $N$. Construct an array $P$ of size $N$ such that:

- $P$ is a permutation of the first $N$ natural numbers, i.e, each integer $1, 2, 3, \ldots N$ occurs exactly once in $P$. For example, $[1, 3, 2]$ is a permutation of size $3$, but $[1, 3, 4]$ and $[2, 1, 2]$ are not.
- $P$ is **indivisible**. $P$ is said to be **indivisible** if $i$ does not divide $P_i$ for every index $2 \leq i \leq N$.

It can be proven that under the given constraints, there always exists an **indivisible** permutation. If there are multiple, you may print any of them.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$, denoting the size of the indivisible permutation you must construct.

---

## Output Format

- For every test case, print a single line containing $N$ space-separated integers. These integers must form an **indivisible**  permutation.

---

## Constraints

- $1 \leq T \leq 600$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
2
3
4
5
```

**Output**

```text
2 1 
1 3 2 
1 3 4 2 
4 5 2 3 1
```

**Explanation**

- For the last test case:
    - $P_2 = 5$ is not divisible by $2$
    - $P_3 = 2$ is not divisible by $3$
    - $P_4 = 3$ is not divisible by $4$
    - $P_5 = 1$ is not divisible by $5$
- Since $i$ does not divide $P_i$ for every index $2\leq i\leq N$, the permutation is **indivisible**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
2 1
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
1 3 2
```



#### Test case 3

**Input for this case**

```text
4
```

**Output for this case**

```text
1 3 4 2
```



#### Test case 4

**Input for this case**

```text
5
```

**Output for this case**

```text
4 5 2 3 1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/INDIPERM)

[Contest: Division 1](https://www.codechef.com/START19A/problems/INDIPERM)

[Contest: Division 2](https://www.codechef.com/START19B/problems/INDIPERM)

[Contest: Division 3](https://www.codechef.com/START19C/problems/INDIPERM)

***Authors:*** [Chaithanya Shyam D](https://www.codechef.com/users/dragonado)

***Testers:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360) and [Lavish Gupta](https://www.codechef.com/users/lavish315)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, construct a permutation P of the integers \{1, 2, 3, \ldots, N\} such that i does not divide P_i for each 2 \leq i \leq N.

#
[](#explanation-5)EXPLANATION:

One possible solution is to simply take the identity permutation P which has P_i = i for every i, and then rotate it right by one step.

This gives the permutation P = [N, 1, 2, 3, \ldots, N-1], which is a valid answer for every N.

Why?

For every 2 \leq i \leq N, we have P_i = i-1.

i does not divide i-1 for any integer i \geq 2 so this permutation is valid.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per test case.

#
[](#solutions-7)SOLUTIONS:

Tester's Solution (C++)
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

const int MAX_T = 600;
const int MAX_N = 100000;
const int MAX_SUM_N = 200000;

#define fast ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int sum_n = 0;
int max_n = 0;
int yess = 0;
int nos = 0;
int total_ops = 0;
ll z = 998244353;

void solve()
{
    int n = readIntLn(2 , MAX_N) ;
    sum_n += n ;

    for(int i = 1 ; i < n ; i++)
    {
        cout << i+1 << ' ';
    }
    cout << 1 << endl ;
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
    assert(sum_n <= MAX_SUM_N);

    cerr<<"SUCCESS\n";
    cerr<<"Tests : " << t << '\n';
    cerr<<"Sum of lengths : " << sum_n << '\n';
    // cerr<<"Maximum length : " << max_n << '\n';
    // cerr<<"Total operations : " << total_ops << '\n';
    // cerr<<"Answered yes : " << yess << '\n';
    // cerr<<"Answered no : " << nos << '\n';
}
``

Editorialist's Solution (Python)
``for _ in range(int(input())):
    n = int(input())
    print(str(n) + ' ' + ' '.join(str(i) for i in range(1, n)))
``

</details>
