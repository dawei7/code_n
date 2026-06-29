# Weird Values

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WRDVLS |
| Difficulty Rating | 2393 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [WRDVLS](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/WRDVLS) |

---

## Problem Statement

You are given an array $A = [A_1, A_2, \ldots, A_N]$ containing $N$ integers.

Consider any subarray $[A_L, A_{L+1}, \ldots, A_R]$ of this subarray (where $1\leq L \leq R \leq N$). Ther `weirdness` of this subarray, denoted $w(L, R)$, is defined to be the number of indices $L \leq i \leq R$ such that $A_i$ equals the number of occurrences of $A_i$ in this subarray.

Formally, we define $w(L, R)$ for $1 \leq L \leq R \leq N$ as follows:
- For every integer $x$, let $f_{L, R}(x)$ denote the number of indices $L \leq j \leq R$ such that $A_j = x$.
- $w(L, R)$ then equals the number of $L \leq i \leq R$ such that $A_i = f_{L, R}(A_i)$

For example, let $A = [1, 3, 5, 2, 1, 2, 9, 5]$. Then,
- $w(1, 8) = 2$, which can be computed as follows.
We have
    - $f_{1, 8}(1) = 2$
    - $f_{1, 8}(2) = 2$
    - $f_{1, 8}(3) = 1$
    - $f_{1, 8}(5) = 2$
    - $f_{1, 8}(9) = 1$

The only indices which satisfy $f_{1, 8}(A_i) = A_i$ are $i = 4$ and $i = 6$, and hence $w(1, 8) = 2$.
- $w(3, 5) = 1$ — the subarray is $[5, 2, 1]$, and each of $1, 2, 5$ occur exactly once in this subarray. Of these, only $1$ equals the number of its occurrences in this subarray.

Given $A$, your task is to compute the sum of the `weirdness` of all subarrays of $A$, i.e, the value
$$\sum_{L = 1}^{N} \sum_{R = L}^N w(L, R)$$

---

## Input Format

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$, the size of the given array.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of $A$.

---

## Output Format

For each test case, output a single line containing a single integer — the sum of the `weirdness` of all subarrays of the given array.

---

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^6$
- $1 \leq A_i \leq 10^6$
- The sum of $N$ across all test cases does not exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
3
3 3 3
4
1 2 1 2
5
1 2 3 2 1
8
1 2 2 3 2 3 3 1
```

**Output**

```text
3
10
16
54
```

**Explanation**

**Test Case 1:** The only subarray with non-zero `weirdness` is the whole array, which has $w(1, 3) = 3$ because every value is $3$ and it appears thrice.

**Test Case 2:** There are $10$ subarrays. Their `weirdness` values are as follows:
- $w(1, 1) = 1$, because $A_1 = 1$ and $f_{1, 1}(1) = 1$.
- $w(1, 2) = 1$, because $A_1 = 1$ and $f_{1, 2}(1) = 1$; but $A_2 = 2$ and $f_{1, 2}(2) = 1 \neq 2$.
- $w(1, 3) = 0$, here $f_{1, 3}(1) = 2 \neq 1$ and $f_{1, 3}(2) = 1 \neq 2$ so no index satisfies the condition.
- $w(1, 4) = 2$, here indices $2$ and $4$ satisfy the condition.
- $w(2, 2) = 0$
- $w(2, 3) = 1$, index $3$ satisfies the condition.
- $w(2, 4) = 3$, all indices satisfy the condition.
- $w(3, 3) = 1$
- $w(3, 4) = 1$, index $3$ satisfies the condition.
- $w(4, 4) = 0$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
3 3 3
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4
1 2 1 2
```

**Output for this case**

```text
10
```



#### Test case 3

**Input for this case**

```text
5
1 2 3 2 1
```

**Output for this case**

```text
16
```



#### Test case 4

**Input for this case**

```text
8
1 2 2 3 2 3 3 1
```

**Output for this case**

```text
54
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

##
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/WRDVLS)

[Div1](https://www.codechef.com/START20A/problems/WRDVLS)

[Div2](https://www.codechef.com/START20B/problems/WRDVLS)

[Div3](https://www.codechef.com/START20C/problems/WRDVLS)

**Setter:**  [ Nishan Singh](https://www.codechef.com/users/retarded_ape)

**Tester:**  [ Aryan Choudhary](https://www.codechef.com/users/aryanc403)

**Editorialist:**  [Ajit Sharma Kasturi](https://www.codechef.com/users/ajit123q)

###
[](#difficulty-2)DIFFICULTY:

EASY

###
[](#prerequisites-3)PREREQUISITES:

None

###
[](#problem-4)PROBLEM:

Given and array A of N integers, the weirdness of the subarray A_L, A_{L+1}, \dots , A_R  denoted by w(L, R) is defined as the number of indices L \leq i \leq R for which A_i equals the number of occurrences of A_i in that subarray. We need to find  the value of \sum_{L=1}^{N} \sum_{R=L}^{N} w(L, R) .

###
[](#explanation-5)EXPLANATION:

-

First let us create an array vals_x for every unique value x present in A. vals_x denotes the array of integers i_1, i_2, i_3, \dots i_{cnt_x} for which A_{i_1} = A_{i_2} = \dots = A_{i_{cnt_x}} = x. Here, cnt_x denotes the total number of values in A equal to x.

-

Suppose we fix some x. Let us consider a technique of sliding window  with window of size x and keep sliding the window on the array vals_x.

-

Suppose our window is like i_j, i_{j+1}, \dots, i_{j+x-1}. Now let us solve this  problem which is, **how much does this window contribute to the answer?**

-

To solve this, we need to find the number of subarrays which contain this window and have no other index k apart from those in window with A_k = x.

-

Clearly, the starting point of such subarray can be in the range

[i_{j-1}+1, i_j] and the ending point of such subarray can be in the range [i_{j+x-1}, i_{j+x} -1]. ( If i_{j-1} doesn’t exist, we can replace it with 0 and if i_{j+x} doesn’t exist, we can replace it with N+1 ).

-

Therefore, the total number of such subarrays for the current window are

(i_j - i_{j-1}) \cdot (i_{j+x} - i_{j+x-1}).

-

Each subarray have x values equal to x, so each subarray contributes x to the answer. So, the total contribution will be  x \cdot (i_j - i_{j-1}) \cdot (i_{j+x} - i_{j+x-1}).

-

We can similarly do this for every window of every unique value x in  the array A and add its contribution to the answer.

###
[](#time-complexity-6)TIME COMPLEXITY:

O(N) for each testcase.

###
[](#solution-7)SOLUTION:

Editorialist's solution
``#include <bits/stdc++.h>
#define ll long long int
using namespace std;

ll solve(vector<int>& vals, int num, int original_array_size) {
      int n = vals.size();
      ll ans = 0;
      for (int i=0; i<n; i++) {
           if (i+num-1 >= n) {
                 break;
           }

           int l = vals[i], r = vals[i+num-1];
           int prev_l = -1, next_r = original_array_size;
           if(i-1 >= 0) prev_l = vals[i-1];
           if(i+num < n) next_r = vals[i+num];

           ans += 1LL * (l - prev_l) * (next_r - r) * num;
      }

      return ans;
}

int main()
{
      int tests;
      cin >> tests;
      while (tests--) {
          int n;
          cin >> n;
          vector<int> a(n);
          unordered_map<int, vector<int>> vals;

          for(int i=0; i<n; i++) {
                cin >> a[i];
                vals[a[i]].push_back(i);
          }

          ll ans = 0;
          for(auto p: vals) {
                ans += solve(p.second, p.first, n);
          }

          cout << ans << endl;
      }
      return 0;
}
``

Setter's solution
``#include<bits/stdc++.h>
using namespace std;
#define int long long

int calc(vector<int> &v, int num, int n){
    if(v.size()<num)return 0;

    int res = 0;
    for(int i = 0; i+num-1 < v.size(); i++){
        int pre, nex;
        if(i>0)pre = v[i] - v[i-1];
        else pre = v[i]+1;

        if(i+num<v.size())nex = v[i+num] - v[i+num-1];
        else nex = n-v[i+num-1];
        res += num*pre*nex;
    }
    return res;
}

vector<int> v[1000001];

void solve(){
    int n;
    cin >> n;
    int a[n];

    for(int i = 0; i<n; i++){
        cin >> a[i];
        if(a[i]<=n){
            v[a[i]].push_back(i);
        }
    }

    int ans = 0;
    for(int i = 1; i<=n; i++){
        ans += calc(v[i], i, n);
    }
    for(int i = 0; i<n; i++){
        v[i].clear();
    }

    cout << ans << "\n";

}

signed main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    #ifndef ONLINE_JUDGE
        freopen("./testgen/Tests/inputs/input1.txt", "r", stdin);
        freopen("./testgen/Tests/outputs/output1.txt", "w", stdout);
    #endif

    int test=0;
    cin >> test;

    while(test--){solve();}

    return 0;
}
``

Tester's solution
``def main():
    for _ in range(int(input())):
        n=int(input())
        a=[int(x) for x in input().split()]
        b=[[] for _ in range(n+1)]
        for i,x in enumerate(a):
            if x <=n:
                b[x].append(i)
        def solve(a,x):
            m=len(a)
            if m==0:
                return 0
            ans=0
            for i in range(m-x+1):
                L,R=i,i+x-1
                l=a[L]-(a[L-1] if L else -1)
                r=(a[R+1] if R+1<m else n)-a[R]
                ans+=l*r
            # print(ans,x)
            return ans
        print(sum(solve(v,i)*i for i,v in enumerate(b)))

main()

``

Please comment below if you have any questions, alternate solutions, or suggestions.

</details>
