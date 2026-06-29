# Gift Shop and Coupon

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | GFTSHP |
| Difficulty Rating | 1364 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [GFTSHP](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/GFTSHP) |

---

## Problem Statement

Chef wants to impress Chefina by giving her the maximum number of gifts possible.

Chef is in a gift shop having $N$ items where the cost of the $i^{th}$ item is equal to $A_{i}$.
Chef has $K$ amount of money and a $50 \%$ off discount coupon that he can use for **at most one** of the items he buys.

If the cost of an item is equal to $X$, then, after applying the coupon on that item, Chef only has to pay ${\bf \left\lceil \frac{X}{2} \right\rceil}$ (rounded up to the nearest integer) amount for that item.

Help Chef find the **maximum number** of items he can buy with $K$ amount of money and a $50 \%$ discount coupon given that he can use the coupon on **at most one** item.

---

## Input Format

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The next line contains $N$ space-separated integers, where the $i^{th}$ integer $A_{i}$ denotes the cost of the $i^{th}$ item.

---

## Output Format

For each test case, print a single line containing one integer ― the **maximum number** of items Chef can buy.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq A_{i} \leq 10^9$
- $0 \leq K \leq 10^9$
- Sum of $N$ over all test cases does not exceed $2\cdot10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1 4
5
3 15
4 4 5
3 10
6 7 4
```

**Output**

```text
1
3
2
```

**Explanation**

**Test case $1$:** After applying the discount, Chef can buy the only available item at ${\left\lceil \frac{5}{2} \right\rceil} = 3$.

**Test case $2$:** Chef can buy all three items even without using the coupon.

**Test case $3$:** After applying coupon on the third item, Chef can buy the second and the third item at $7 + {\left\lceil \frac{4}{2} \right\rceil} = $ $ 7 + 2 = 9$.
It is not possible for Chef to buy more than two items.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 4
5
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 15
4 4 5
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
3 10
6 7 4
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

[Contest Division 1](https://www.codechef.com/START30A/problems/GFTSHP)

[Contest Division 2](https://www.codechef.com/START30B/problems/GFTSHP)

[Contest Division 3](https://www.codechef.com/START30C/problems/GFTSHP)

[Contest Division 4](https://www.codechef.com/START30D/problems/GFTSHP)

Setter: [ Pranav Dev](https://www.codechef.com/users/pd_codes)

Tester: [Abhinav Sharma](https://www.codechef.com/users/inov_360), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Sorting

#
[](#problem-4)PROBLEM:

Chef wants to impress Chefina by giving her the maximum number of gifts possible.

Chef is in a gift shop having N items where the cost of the i^{th} item is equal to A_{i}.

Chef has K amount of money and a 50 \% off discount coupon that he can use for **at most one** of the items he buys.

If the cost of an item is equal to X, then, after applying the coupon on that item, Chef only has to pay {\bf \left\lceil \frac{X}{2} \right\rceil} (rounded up to the nearest integer) amount for that item.

Help Chef find the **maximum number** of items he can buy with K amount of money and a 50 \% discount coupon given that he can use the coupon on **at most one** item.

#
[](#explanation-5)EXPLANATION:

Let M be the maximum number of items that Chef will buy, and let \{i_1, i_2, \ldots i_M\} be the list of items that costs minimum among all possible list of items of size M. Also, let S = \sum_{\alpha = 1}^{M} A_{i_{\alpha}}

**Observation 1:**  Chef will always use the discount coupon on the most expensive item. This is because the amount of money that Chef will pay will be S - discount, and as the price increases, the discount increases.

**Observation 2:** The list of items will have the M lowest priced items. To prove this, let us introduce a new item j in the list of items and remove i_\alpha such that A_{i_\alpha} < A_j. We can make 4 cases on {discount on A_{i_\alpha}, discount on A_{j}} and in each case, we can see that the original list results in less overall cost.

So we can first sort the items in the increasing order of price, and for each i such that 1 \leq i \leq N, check if we can take first i elements by applying discount on the i^{th} item. The largest feasible i will be our answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N \cdot \log{N}) for each test case.

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#define ll long long
#define fo(i , n) for(ll i = 0 ; i < n ; i++)
#include<bits/stdc++.h>
using namespace std ;

void solve()
{
    ll n , k ;
    cin >> n >> k ;

    ll arr[n] ;
    for(int i = 0 ; i < n ; i++)
        cin >> arr[i] ;
    sort(arr , arr+n) ;

    ll sum = 0, ans = 0;

    for(ll i = 0 ; i < n ; i++)
    {
        ll new_cost = (arr[i] + 1)/2 ; // ceil division
        if(sum + new_cost <= k)
        {
            ans++ ;
            sum += arr[i] ; // updating sum for next iteration
        }
        else
            break ;
    }

    cout << ans << '\n' ;
    return ;
}

int main()
{

    ll t = 1 ;
    cin >> t ;
    while(t--)
    {
        solve() ;
    }

    cerr << "Time : " << 1000 * ((double)clock()) / (double)CLOCKS_PER_SEC << "ms\n";

    return 0;
}
``

</details>
