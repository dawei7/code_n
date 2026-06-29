# Non Zero Subarray Xor

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBARRAYXOR |
| Difficulty Rating | 2101 |
| Difficulty Band | 2000 to 2500 difficulty problems |
| Path | Become 5 star |
| Lesson | 2000 to 2500 difficulty problems |
| Official Link | [SUBARRAYXOR](https://www.codechef.com/practice/course/5-star-and-above-problems/DIFF2500/problems/SUBARRAYXOR) |

---

## Problem Statement

JJ is back with another challenge. He challenges you to construct an array $A$ containing $N$ integers such that the following conditions hold:
- For all $1 \le i \le N$, $1 \le A_i \le 10^6$
- Every [subarray](https://stackoverflow.com/a/45686639) has non-zero XOR. That is, for every $1 \le L \le R \le N$, $A_L \oplus A_{L+1} \oplus \ldots \oplus A_R \ne 0$. Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Can you complete JJ's challenge?

Under the given constraints, it can be proved that there always exists at least one array satisfying these conditions. If there are multiple possible arrays, **print any of them**.

---

## Input Format

- The first line contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$ — the size of the array $A$ to be constructed.

---

## Output Format

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of array $A$. The $i^{th}$ of these $N$ integers is $A_i$. If multiple arrays exist which satisfy the conditions, print any of them.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
1
6
6
```

**Output**

```text
7
1 2 4 8 16 32
2 3 5 7 11 13
```

**Explanation**

**Test Case $1$**: There is only one subarray, $[7]$. Its XOR is non-zero.

**Test Case $2$**: Some of the subarray XORS are:
- $\texttt{XOR}([2,4,8]) = 14 \ne 0$
- $\texttt{XOR}([1,2]) = 3 \ne 0$
- $\texttt{XOR}([4,8,16,32]) = 60 \ne 0$.

Similarly, it can be checked that every subarray has non-zero XOR.

**Test Case $3$**: Some of the subarray XORS are:
- $\texttt{XOR}([2,3,5,7]) = 3 \ne 0$
- $\texttt{XOR}([7, 11]) = 12 \ne 0$
- $\texttt{XOR}([2, 3, 5, 7, 11, 13]) = 5 \ne 0$

Similarly, it can be checked that every subarray has non-zero XOR.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
6
```

**Output for this case**

```text
1 2 4 8 16 32
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
2 3 5 7 11 13
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START23A/problems/SUBARRAYXOR)

[Contest Division 2](https://www.codechef.com/START23B/problems/SUBARRAYXOR)

[Contest Division 3](https://www.codechef.com/START23C/problems/SUBARRAYXOR)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Manan Grover](https://www.codechef.com/users/mexomerf)

Editorialist: [Lavish Gupta](https://www.codechef.com/users/lavish315)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

[Bitwise Xor](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)

#
[](#problem-4)PROBLEM:

JJ is back with another challenge. He challenges you to construct an array A containing N integers such that the following conditions hold:

- For all 1 \le i \le N, 1 \le A_i \le 10^6

- Every [subarray](https://stackoverflow.com/a/45686639) has non-zero XOR. That is, for every 1 \le L \le R \le N, A_L \oplus A_{L+1} \oplus \ldots \oplus A_R \ne 0. Here, \oplus denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Can you complete JJ’s challenge?

Under the given constraints, it can be proved that there always exists at least one array satisfying these conditions. If there are multiple possible arrays, **print any of them**.

#
[](#quick-explanation-5)QUICK EXPLANATION:

What if there is a subarray having XOR = 0?

If there is a subarray having XOR = 0, there will exist a pair of distinct values i, j such that the XOR of prefixes of length i and j will be equal.

Hence, if XOR of all prefixes are distinct, then there will be no subarray having XOR = 0.

Assigning XORs

So let us assign distinct positive XORs to each prefix length. One way can be to assign XOR_{[1, i]} = i.

This means that (i-1) \oplus A_i = i

#
[](#explanation-6)EXPLANATION:

\oplus_{[L, R]} denotes the XOR of the subarray starting at index L and ending at index R (inclusive).

Let’s say there exists a subarray [L, R] such that A_L \oplus A_{L+1} \oplus \ldots \oplus A_R = 0

Consider the XOR of the prefix [1 , L-1] and [1, R].

\oplus_{[1, R]} = (\oplus_{[1, L-1]}) \oplus (\oplus_{[L, R]}) \implies \oplus_{[1, R]} = \oplus_{[1, L-1]}

The above equation suggests that if there is a subarray having XOR = 0, there will exist a pair of distinct values i, j such that the XOR of prefixes of length i and j will be equal.

Hence, if XOR of all prefixes are distinct, then there will be no subarray having XOR = 0.

Now, there can be several ways in which we can assign the XOR values to each prefix length. One of the simplest way is to assign \oplus_{[1, i]} = i, i.e. for prefix of length i, let us assign it’s XOR value to be i.

Getting the array

So we have \oplus_{[1, i]} = i,  \forall i: 1 \leq i \leq N

XOR of prefix of length one = 1 = A_1

Now, for a general index i > 1, \oplus_{[1, i]} = \oplus_{[1, i-1]} \oplus A_i

Substituting values, i = (i-1) \oplus A_i \implies A_i = (i-1) \oplus i

It can be proved that the above value of A_i ensures that A_i  < 2\cdot i. Therefore,\forall i: 1 \leq i \leq N, A_i \leq 10^6

Bonus Problem

Suppose we modify the constraint of A_i, such that 1 \leq A_i \leq N. Can you construct an array now?

#
[](#time-complexity-7)TIME COMPLEXITY:

Assuming that taking XOR of two numbers is an O(1) operation, the above approach will take O(N) time for each testcase.

#
[](#solution-8)SOLUTION:

Setter's Solution
``#ifdef WTSH
    #include <wtsh.h>
#else
    #include <bits/stdc++.h>
    using namespace std;
    #define dbg(...)
#endif

#define IOS ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define int long long
#define endl "\n"
#define sz(w) (int)(w.size())
using pii = pair<int, int>;

const int N = 1e5 + 5;

int ans[N];

void precompute()
{
    ans[0] = 1;
    int cur = 1;
    for(int i = 1; i < N; i++)
    {
        ans[i] = (cur + 1) ^ cur;
        cur++;
    }
}

void solve(int n)
{
    for(int i = 0; i < n; i++)
        cout << ans[i] << " ";
    cout << endl;
}

int32_t main()
{
    IOS;
    precompute();
    int T; cin >> T;
    for(int tc = 1; tc <= T; tc++)
    {
        int n; cin >> n;
        solve(n);
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
    int n;
    cin>>n;
    for(int i = 0; i < n; i++){
      cout<<(i ^ (i + 1))<<" ";
    }
    cout<<"\n";
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

    int arr[n] ;
    arr[0] = 1 ;

    for(int i = 1 ; i < n; i++)
    {
        int req_xor = i+1 ;
        int req_ele = (req_xor ^ i) ;
        arr[i] = req_ele ;
    }

    for(int i = 0 ; i < n ; i++)
    {
        cout << arr[i] << ' ';
    }
    cout << endl ;
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
