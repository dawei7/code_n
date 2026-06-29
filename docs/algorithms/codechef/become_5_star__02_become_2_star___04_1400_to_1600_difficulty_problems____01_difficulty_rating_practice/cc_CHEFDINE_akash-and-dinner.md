# Akash and Dinner

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFDINE |
| Difficulty Rating | 1438 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHEFDINE](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHEFDINE) |

---

## Problem Statement

Akash got his money from CodeChef today, so he decided to have dinner outside.
He went to a restaurant having $N$ items on the menu. The $i^{th}$ item on the menu belongs to the *category* $A_i$ and requires $B_i$ time to be cooked.

Akash wants to have a *complete meal*. Thus, his meal should have **at least** $K$ **distinct** *categories* of food.
The total time required to get all the food Akash orders, is the **sum** of the cooking time of all the items in the order.

Help Akash find the **minimum time** required to have a complete meal or tell if it is not possible to do so.

---

## Input Format

- First line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines:
    - The first line of each test case contains two space-separated integers $N$ and $K$, denoting the number of dishes on the menu and the number of distinct categories in a complete meal.
    - The second line contains $N$ space-separated integers where the $i^{th}$ integer is $A_i$, denoting the category of the $i^{th}$ dish in the menu.
    - The third line contains $N$ space-separated integers where the $i^{th}$ integer is $B_i$, denoting the time required to cook the $i^{th}$ dish in the menu.

---

## Output Format

For each test case, output in a single line, the **minimum time** required to have a complete meal.

If it is impossible to have a complete meal, print $-1$ instead.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,K \leq 10^5$
- $1 \leq A_i \leq 10^5$
- $0 \leq B_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5
```

**Output**

```text
1
3
1
-1
```

**Explanation**

**Test case $1$:** Akash can choose dish with index $2$ having category $2$. The total time required to get the complete meal is $1$.

**Test case $2$:** Akash can choose dishes with index $3, 5,$ and $7$ from the menu.
- Dish $3$: The dish has category $2$ and requires time $0$.
- Dish $5$: The dish has category $4$ and requires time $2$.
- Dish $7$: The dish has category $3$ and requires time $1$.

Thus, there are $3$ distinct categories and the total time to get the meal is $0+2+1 = 3$. It can be shown that this is the minimum time to get the *complete meal*.

**Test case $3$:** Akash can choose the only available dish having category $5$. The total time required to get the complete meal is $1$.

**Test case $4$:** The total number of distinct categories available is $2$, which is less than $K$. Thus, it is impossible to have a *complete* meal.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 1
1 2 3
2 1 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
1 1
5
1
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5 3
1 1 2 2 1
1 1 0 3 5
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

[Practice](https://www.codechef.com/problems/CHEFDINE)

[Contest: Division 1](https://www.codechef.com/START69A/problems/CHEFDINE)

[Contest: Division 2](https://www.codechef.com/START69B/problems/CHEFDINE)

[Contest: Division 3](https://www.codechef.com/START69C/problems/CHEFDINE)

[Contest: Division 4](https://www.codechef.com/START69D/problems/CHEFDINE)

***Author:*** [justfun21](https://www.codechef.com/users/justfun21)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [mexomerf](https://www.codechef.com/users/mexomerf)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1438

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

A restaurant has N dishes; the i-th of which has category A_i and takes B_i time to be cooked.

Find the minimum possible time needed to get at least K distinct categories of food.

#
[](#explanation-5)EXPLANATION:

If there are less than K distinct categories the answer is -1.

This can be checked in several different ways, for example:

- Put all the A_i values into a set and check its size; or

- Sort the A_i values and count the number of indices such that A_i \leq A_{i+1}.

Now let’s deal with the case when there are \geq K distinct values.

Choosing two different dishes with the same category is clearly not optimal.

This means we choose at most one dish from each category.

For the least total time, from each category we obviously keep only the one that takes the least time to cook.

This can be computed using an array C of length 10^5, initially C_i = \infty for each 1 \leq i \leq 10^5.

Then, for each 1 \leq i \leq N, set C_{A_i} = \min(C_{A_i}, B_i).

Now, C_x contains the minimum time to cook a dish of category x.

The answer is then the sum of the K smallest values of C, which can be found by sorting C.

Instead of an array of size 10^5, you can also use a map (`std::map` in C++, `HashMap/TreeMap` in Java, `dict` in Python) to represent C.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log N) per testcase.

#
[](#code-7)CODE:

Setter's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main(){
    // setIO("input");
    ios_base::sync_with_stdio(false);
    cin.tie();cout.tie();
    long long TT = 1;
    long long suma = 0;
    cin>>TT;
    for(long long TR = 1;TR <= TT;TR++){
        long long n,k;
        cin>>n>>k;
        suma+=n;
        assert(n>=1 and n<=100000);
        assert(k>=1 and k<=100000);
        vector<long long>a(n),b(n);
        for(long long i=0;i<n;i++){
            cin>>a[i];
            assert(a[i]>=1 and a[i]<=100000);
        }
        for(long long i=0;i<n;i++){
            cin>>b[i];
            assert(b[i]>=0 and b[i]<=100000);
        }
        map<long long,long long>mp;
        for(long long i=0;i<n;i++){
            mp[a[i]] = 10000007;
        }
        for(long long i=0;i<n;i++){
            mp[a[i]] = min(mp[a[i]],b[i]);
        }
        vector<long long>time;
        for(auto it:mp){
            if(it.second!=10000007){
                time.push_back(it.second);
            }
        }
        sort(time.begin(),time.end());
        if(time.size()<k){
            cout<<-1<<"\n";
            continue;
        }
        long long ans = 0;
        for(long long i=0;i<k;i++){
            ans+=time[i];
        }
        cout<<ans<<"\n";
    }
    assert(suma>=1 and suma<=100000);
    return 0;
}
``

Tester's code (C++)
``#include <bits/stdc++.h>
using namespace std;
#define int long long
int32_t main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);
  cout.tie(0);
  int t;
  cin >> t;
  while (t--)
  {
    int n, k;
    cin >> n >> k;
    int a[n], b[n];
    map<int, int> mpp;
    for (int i = 0; i < n; i++){
      cin >> a[i];
    }
    for (int i = 0; i < n; i++){
      cin >> b[i];
    }
    for (int i = 0; i < n; i++){
      if(mpp.find(a[i]) == mpp.end()){
        mpp[a[i]] = b[i];
      }else{
        mpp[a[i]] = min(mpp[a[i]], b[i]);
      }
    }
    vector<int> v;
    for(auto &it: mpp){
      v.push_back(it.second);
    }
    sort(v.begin(), v.end());
    int sum = -1;
    if(v.size() >= k){
      sum = 0;
      for (int i = 0; i < k; i++){
        sum += v[i];
      }
    }
    cout << sum << "\n";
  }
  return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    least = [10**12 for i in range(10**5 + 5)]
    for i in range(n): least[a[i]] = min(least[a[i]], b[i])
    ans = sum(sorted(least)[0:k])
    print(ans if ans < 10**12 else -1)
``

</details>
