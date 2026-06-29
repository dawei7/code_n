# Maximising Vacations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXVAC |
| Difficulty Rating | 2147 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [MAXVAC](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/MAXVAC) |

---

## Problem Statement

You are given Chef's calendar for the next $N$ days, defined as a binary string $S$ of length $N$ where $S_i = 0$ means that Chef has a holiday on the $i^{th}$ day from now, and $S_i = 1$ means that Chef has to work on that day.

Chef wants to plan his vacations. For each vacation, Chef needs $X$ consecutive holidays in his calendar. Obviously, he can only go on one vacation at a time.

Chef can take at most one extra holiday. That is, he can flip at most one digit in $S$ from $1$ to $0$. If he does this optimally, what is the **maximum** number of vacations that he can go on?

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $X$.
- The second line of each test case contains a binary string $S$ of length $N$ — Chef's schedule.

---

## Output Format

For each test case, output on a new line the answer — the maximum number of vacations Chef can take if he takes at most one more extra holiday.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq X \leq N$
- The sum of $N$ across all test cases does not exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
7 2
0010001
4 3
1010
5 2
00100
```

**Output**

```text
3
1
2
```

**Explanation**

**Test Case $1$:** Chef can flip the $3^{rd}$ digit to make his calendar $0000001$. This allows him to take $3$ vacations in the first $6$ days.

**Test Case $2$:** Chef can flip the $3^{rd}$ digit to make his calendar $1000$. This allows him to take one vacation using the last $3$ days.

**Test Case $3$:** Regardless of whether Chef flips the $3^{rd}$ digit or not, he can take at most $2$ vacations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7 2
0010001
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 3
1010
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 2
00100
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

[Contest Division 1](https://www.codechef.com/START23A/problems/MAXVAC)

[Contest Division 2](https://www.codechef.com/START23B/problems/MAXVAC)

[Contest Division 3](https://www.codechef.com/START23C/problems/MAXVAC)

Setter: [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

[Prefix Sum](https://en.wikipedia.org/wiki/Prefix_sum)

#
[](#problem-4)PROBLEM:

You are given Chef’s calendar for the next N days, defined as a binary string S of length N where S_i = 0 means that Chef has a holiday on the i^{th} day from now, and S_i = 1 means that Chef has to work on that day.

Chef wants to plan his vacations. For each vacation, Chef needs X consecutive holidays in his calendar. Obviously, he can only go on one vacation at a time.

Chef can take at most one extra holiday. That is, he can flip at most one digit in S from 1 to 0. If he does this optimally, what is the **maximum** number of vacations that he can go on?

#
[](#explanation-5)EXPLANATION:

What if no extra holiday is allowed?

Consider a contiguous segment of 0's of length len. The number of times Chef can go to a vacation during this contiguous segment will be len/K.

So, if no extra holiday is allowed, we can first get the length of all contiguous segments of 0's in the string. The answer would be the sum of len/X for all len values that we encounter.  Let’s call this answer orig\_ans

What happens when a holiday is taken?

Let’s say we take a holiday on i^{th} day. Then, the contiguous segment of 0's ending at index i-1 is merged with the contiguous segment of 0's starting at index i+1, with S_i also becoming 0.

So now, we need to account for these changes in the previous contiguous segments of 0's to get the maximum number of vacations that Chef can go to, when a holiday is taken on i^{th} day.

Calculating efficiently

The information that we need, when taking a holiday on i^{th} day, is the length of contiguous segment of 0's ending at index i-1 (let’s say len\_end_{i-1}) and the length of contiguous segment of 0's starting at index i+1 (let’s say len\_start_{i+1}).

Consider the original contiguous segments of 0's. After this change, we now have removed contiguous segments of length  len\_end_{i-1} and len\_start_{i+1}, and have added a new segment of length len_i = len\_end_{i-1} + len\_start_{i+1} + 1.

So the answer when a holiday is taken on i^{th} day, let say ans_i will be:

ans_i = orig\_ans - \frac{len\_end_{i-1}}{K} - \frac{len\_start_{i+1}}{K} + \frac{len_i}{K}.

To get our final answer, we need to take the max of ans_i \forall i: S_i = 1

So we can first calculate the length of contiguous segments of 0's that ends at index i, and length of contiguous segments of 0's that start at index i, for all 1 \leq i \leq N. After this computation, we can efficiently calculate the maximum number of vacations that the Chef can go to, when the holiday is taken on i^{th} day, and finally take the maximum of all these numbers.

#
[](#time-complexity-6)TIME COMPLEXITY:

The above approach will take O(N) time for each test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int n, x;
    cin>>n>>x;
    string s;
    cin>>s;
    int ans = 0;
    vector<int> v;
    v.push_back(-1);
    int tot = 0;
    for(int i = 0; i < n; i++){
      if(s[i] == '1'){
        tot += (i - v.back() - 1) / x;
        v.push_back(i);
      }
    }
    tot += (n - v.back() - 1)/x;
    v.push_back(n);
    for(int i = 1; i < v.size() - 1; i++){
      int temp = tot - (v[i] - v[i - 1] - 1) / x - (v[i + 1] - v[i] - 1) / x + (v[i + 1] - v[i - 1] - 1) / x;
      ans = max(ans, temp);
    }
    cout<<ans<<"\n";
  }
  return 0;
}
``

Editorialist's Solution
``#include<bits/stdc++.h>
#define ll long long
using namespace std ;

const ll z = 1000000007 ;

void solve()
{
    int n , k ;
    cin >> n >> k ;
    string str ;
    cin >> str ;

    int left[n] , right[n] ;

    left[0] = (str[0] == '0') ;
    right[n-1] = (str[n-1] == '0') ;

    for(int i = 1 ; i < n ; i++)
    {
        if(str[i] == '0')
            left[i] = left[i-1]+1 ;
        else
            left[i] = 0 ;
    }

    for(int i = n-2 ; i >= 0 ; i--)
    {
        if(str[i] == '0')
            right[i] = right[i+1]+1 ;
        else
            right[i] = 0 ;
    }

    int ans = 0 ;
    for(int i = 0 ; i < n ; i++)
    {
        if(left[i] == 0 && i > 0)
            ans += (left[i-1]/k) ;
    }

    ans += left[n-1]/k ;
    int orig_ans = ans ;

    for(int i = 0 ; i < n ; i++)
    {
        if(str[i] == '0')
            continue ;

        int orig_left = 0 , orig_right = 0 ;
        if(i > 0)
            orig_left = left[i-1] ;
        if(i < n-1)
            orig_right = right[i+1] ;

        int change = (orig_left + orig_right + 1)/k - orig_right/k - orig_left/k ;
        ans = max(ans, orig_ans+change) ;
    }
    cout << ans << endl ;
    return ;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    #ifndef ONLINE_JUDGE
    freopen("inputf.txt" , "r" , stdin) ;
    freopen("outputf.txt" , "w" , stdout) ;
    freopen("error.txt" , "w" , stderr) ;
    #endif

    int t;
    cin >> t ;
    while(t--)
        solve() ;

    return 0;
}
``

</details>
