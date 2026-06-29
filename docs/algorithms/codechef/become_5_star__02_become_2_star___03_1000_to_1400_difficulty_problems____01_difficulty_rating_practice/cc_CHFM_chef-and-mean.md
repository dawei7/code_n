# Chef and Mean  

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHFM |
| Difficulty Rating | 1229 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [CHFM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/CHFM) |

---

## Problem Statement

Chef has invested his savings into $N$ coins (numbered $1$ through $N$). For each valid $i$, the $i$-th coin has value $A_i$. Chef does not want to know how much money he has, so he remembers the mean value of the coins instead of the sum of their values.

A waiter from Chef's restaurant plans to steal exactly one of Chef's coins, but he does not want Chef to know about this, so he can only steal a coin if the arithmetic mean of all remaining coins is the same as the original arithmetic mean of all coins. Since the waiter is not good at mathematics, can you help him complete his plan?

You have to determine whether it is possible to steal some coin and if it is possible, choose the coin the waiter should steal. If there are multiple coins that can be stolen, choose the one with the smallest number.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

### Output
For each test case, print a single line. If the waiter cannot steal any coin, this line should contain the string `"Impossible"` (without quotes). Otherwise, it should contain the number of the coin he should steal.

### Constraints
- $1 \le T \le 10$
- $2 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$

### Subtasks
**Subtask #1 (30 points):**
- $2 \le N \le 10^3$
- $1 \le A_i \le 10^3$ for each valid $i$
- $A_1 + A_2 + \ldots + A_N \le 10^9$

**Subtask #2 (70 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
5
1 2 3 4 5
4
5 4 3 6
10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
```

**Output**

```text
3
Impossible
1
```

**Explanation**

**Example case 1:** Stealing the third coin does not change the mean. Initially, it is $(1+2+3+4+5)/5 = 3$ and after stealing this coin, it is still $(1+2+4+5)/4 = 3$.

**Example case 2:** It is not possible to steal any coin without changing the mean.

**Example case 3:** The mean is always $10^9$, both initially and after removing any coin, so each coin can be stolen. In that case, we should choose the first coin.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 2 3 4 5
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
5 4 3 6
```

**Output for this case**

```text
Impossible
```



#### Test case 3

**Input for this case**

```text
10
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINKS :

Contest : [Division 1](https://www.codechef.com/JULY19A/problems/CHFM)

Contest : [Division 2](https://www.codechef.com/JULY19B/problems/CHFM)

[Practice](https://www.codechef.com/problems/CHFM)

**Setter :** [Tanay Mishra](https://www.codechef.com/users/mishra_tanay_)

**Tester :** [Alipasha Montaseri](https://www.codechef.com/users/alipasha132) / [Kasra Mazaheri](https://www.codechef.com/users/kmaaszraa)

**Editorialist :** [Anand Jaisingh](https://www.codechef.com/users/anand20)

# DIFFICULTY :

Cakewalk

# PREREQUISITES  :

Programming language basics

# PROBLEM :

Given an array A of size N \ge 2 , you need to find if it is possible to delete an element from the array without affecting the original mean of the array.

# QUICK EXPLANATION :

It can be proved that we just need to check if the mean of the originally given array exists in the array. If yes, we need to find the lowest index having such an element.

# EXPLANATION :

Let’s loop over each element of the array, and check if it is possible to delete this element, such that the mean of the array before and after deleting this element is the same.

Let the sum of the originally given array be sum. So, the mean of the initially given array is the number \frac{sum}{N}. ( this may not necessarily be an integer ). Now, on deleting the element present at index i, the mean transforms to  \frac{sum-A[i]}{N-1}

In an ideal world, just checking if these numbers  are equal for each i using long doubles would be enough. However, the world is hardly ideal, and to prevent precision issues of any kind, we need :

\frac{sum}{N}=\frac{sum-A[i]}{N-1}. This condition equals :

 sum \cdot (N-1) =N \cdot (sum-A[i]) .

Since each of the individual terms we use above are integers, their products are also integers. So, using this condition, we avoid precision issues of all kinds and deal only with integers. We just need to find the lowest i for which this condition holds.

**Additionally :**

On simplifying the expression above, we get :

 N \cdot sum - sum = N \cdot sum - N \cdot A[i] ,

 -sum = - N \cdot A[i] ,

 \frac{sum}{N} = A[i] .

This condition shows that the element we needed to remove must actually be the mean of the original array. So, we must just find the smallest element i, such that  A[i]=\frac{sum}{N}, or print -1 if such an element does not exist.

# COMPLEXITY ANALYSIS :

**Time Complexity** :  O(N)

**Space complexity** : O(N)

# SOLUTION LINKS :

Setter
``#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main(void)
{
    int t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        ll arr[n];
        ll sum=0;
        map <ll , int > m;
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
            sum+=arr[i];
            if(m[arr[i]]==0)
            {
                m[arr[i]]=i+1;
            }
        }
        if(sum%n==0)
        {
            ll mean=sum/n;
            if(m[mean]!=0)
            {
                cout<<m[mean];
            }
            else{
                cout<<"Impossible";
            }
        }
        else{
            cout<<"Impossible";
        }
        cout<<'\n';
    }
}
``

Tester

// KALAM

include<bits/stdc++.h>

``using namespace std;

const int N = 100000 + 77;
int n , T;
int a[N];
inline void Test() {
   unsigned long long tot = 0;
   scanf("%d" , & n);
   for(int i = 1;i <= n;++ i)
      scanf("%d" , a + i) , tot += a[i];
   for(int i = 1;i <= n;++ i)
      if(tot * (n - 1) == (tot - a[i]) * n) {
         printf("%d\n" , i);
         return ;
      }
   printf("Impossible\n");
}
int main() {
   scanf("%d" , & T);
   while(T --)
      Test();
   return 0;
}
``

Editorialist
``//#pragma GCC optimize("Ofast,no-stack-protector")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")
//#pragma GCC target("avx,tune=native")
// Anand Jaisingh

#include<bits/stdc++.h>

using namespace std;

typedef complex<double> base;
typedef long double ld;
typedef long long ll;

#define pb push_back
#define pii pair<int,int>
#define pll pair< ll , ll >
#define vi vector<int>
#define vvi vector< vi >

const int maxn=(int)(2e5+5);
const ll mod=(ll)(1e9+7);
int a[maxn];

int main()
{
    ios_base::sync_with_stdio(0);cin.tie(0);

    int t;cin>>t;

    while(t>0)
    {
        int n;cin>>n;

        ll sum=0;

        for(int i=0;i<n;i++)
        {
            cin>>a[i];

            sum+=a[i];
        }

        int res=-1;

        for(int i=0;i<n;i++)
        {
            ll y=sum-a[i];

            ll val1=sum*1ll*(n-1),val2=y*n;

            if(val1==val2)
            {
                res=i;break;
            }
        }

        if(res==-1)
        {
            cout<<"Impossible"<<endl;
        }

        else
        {
            cout<<(res+1)<<endl;
        }

        t--;
    }

    return 0;
}
``

Comments are welcome !

</details>
