# Average of Three

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AVGOF3 |
| Difficulty Rating | 1141 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [AVGOF3](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/AVGOF3) |

---

## Problem Statement

It is Chef's birthday. You know that Chef's favourite number is $X$. You also know that Chef loves averages. Therefore you decide it's best to gift Chef $3$ integers $A_1, A_2, A_3$, such that:
- The mean of $A_1, A_2$ and $A_3$ is $X$.
- $1 \le A_1, A_2, A_3 \le 1000$.
- $A_1, A_2$ and $A_3$ are **distinct**.

Output any suitable $A_1, A_2$ and $A_3$ which you could gift to Chef.

As a reminder, the mean of three numbers $P, Q, R$ is defined as: $mean(P, Q, R) = \dfrac{P + Q + R}{3}$.

For example, $mean(2, 3, 5) = \frac{2 + 3 + 5}{3} = \frac{10}{3} = 3.33\bar{3}$, $mean(2, 2, 5) = \frac{2 + 2 + 5}{3} = \frac{9}{3} = 3$.

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains one integer $X$ — Chef's favourite number.

---

## Output Format

For each test case, one line containing $3$ space-separated integers — $A_1, A_2$, and $A_3$, which satisfy the given conditions. If there are multiple possible answers you may output **any** of them.

It can be shown that an answer always exists, under the given constraints.

---

## Constraints

- $1 \leq T \leq 100$
- $2 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
3
5
5
```

**Output**

```text
1 3 5
1 6 8
3 5 7
```

**Explanation**

**Test Case $1$:** $mean(1, 3, 5) = \frac{1 + 3 + 5}{3} = \frac{9}{3} = 3$

**Test Case $2$:** $mean(1, 6, 8) = \frac{1 + 6 + 8}{3} = \frac{15}{3} = 5$

**Test Case $3$:** $mean(3, 5, 7) = \frac{3 + 5 + 7}{3} = \frac{15}{3} = 5$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
```

**Output for this case**

```text
1 3 5
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
1 6 8
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
3 5 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START23A/problems/AVGOF3)

[Contest Division 2](https://www.codechef.com/START23B/problems/AVGOF3)

[Contest Division 3](https://www.codechef.com/START23C/problems/AVGOF3)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

It is Chef’s birthday. You know that Chef’s favourite number is X. You also know that Chef loves averages. Therefore you decide it’s best to gift Chef 3 integers A_1, A_2, A_3, such that:

- The mean of A_1, A_2 and A_3 is X.

-
1 \le A_1, A_2, A_3 \le 1000.

-
A_1, A_2 and A_3 are **distinct**.

Output any suitable A_1, A_2 and A_3 which you could gift to Chef.

As a reminder, the mean of three numbers P, Q, R is defined as: mean(P, Q, R) = \dfrac{P + Q + R}{3}.

For example, mean(2, 3, 5) = \frac{2 + 3 + 5}{3} = \frac{10}{3} = 3.33\bar{3}, mean(2, 2, 5) = \frac{2 + 2 + 5}{3} = \frac{9}{3} = 3.

#
[](#explanation-5)EXPLANATION:

There are several possible solutions to this problem. Here are two of them:

Based on Total Sum

Given that the average is X, the total sum of three elements will be S = 3 \cdot X.

Now, given 2 \leq X \leq 100, we will have 6 \leq S \leq 300.

Because we need to choose 3 **distinct** positive integers, let’s choose A_1 = 1, A_2 = 2. Now, A_3 = S - 3, so 3 \leq A_3 \leq 297, which satisfies all the constraints.

Based on Average

We want to make the average of three elements to X. One way to achieve this is to symmetrically distribute elements around X.

So, we can have one of the elements as X itself. Now, we have two remaining elements which we want to assign symmetrically, so we can have one of the element as X-1 and other as X+1.

This assignment satisfies all the constraints.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)

int32_t main()
{
    IOS;
    int T; cin >> T;
    while(T--)
    {
        int n; cin >> n;
        cout << n-1 << ' ' << n << ' ' << n+1 << '\n';
    }
    return 0;
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;
int main(){
  ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
  int t;
  cin>>t;
  while(t--){
    int x;
    cin>>x;
    cout<<1<<" "<<2<<" "<<3 * x - 3<<"\n";
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
    int n ;
    cin >> n ;

    cout << n-1 << ' ' << n << ' ' << n+1 << endl ;
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
