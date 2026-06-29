# Playing with OR

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIZZBUZZ2304 |
| Difficulty Rating | 1365 |
| Difficulty Band | Bit Manipulation |
| Path | Data Structures and Algorithms |
| Lesson | Implementing Bitwise Operators |
| Official Link | [FIZZBUZZ2304](https://www.codechef.com/learn/course/bit-manipulation/BITM05/problems/FIZZBUZZ2304) |

---

## Problem Statement

You are given an array $A$ containing $N$ integers, and an integer $K$ ($1 \leq K \leq N$).
Find the number of *subarrays* of $A$ with length $K$ whose [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) is odd.

**Note:** A subarray of $A$ is a contiguous segment of elements of $A$.
For example, if $A = [1, 3, 2]$, then it has $6$ non-empty subarrays: $[1], [3], [2], [1, 3], [3, 2], [1, 3, 2]$.
In particular, $[1, 2]$ is *not* a subarray of $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the array and the subarray size you have to check, respectively.
    - The second line of each test contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the elements of the array.

---

## Output Format

For each test case, output on a new line the number of length-$K$ subarrays of $A$ whose bitwise OR is odd.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq K\leq N \leq 5\cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all tests doesn't exceed $5\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
2
5 2
5 7 13 4 6
4 3
2 6 7 4
```

**Output**

```text
3
2
```

**Explanation**

**Test case $1$:** There are four subarrays of length $K = 2$.
- $[5, 7]$, with bitwise OR equal to $7$.
- $[7, 13]$, with bitwise OR equal to $15$.
- $[13, 4]$, with bitwise OR equal to $13$.
- $[4, 6]$, with bitwise OR equal to $6$.

Three of them are odd, so the answer is $3$.

**Test case $2$:** There are two subarrays of length three, both of them have odd bitwise OR.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
5 7 13 4 6
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
4 3
2 6 7 4
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIZZBUZZ2304)

[Contest: Division 1](https://www.codechef.com/START106A/problems/FIZZBUZZ2304)

[Contest: Division 2](https://www.codechef.com/START106B/problems/FIZZBUZZ2304)

[Contest: Division 3](https://www.codechef.com/START106C/problems/FIZZBUZZ2304)

[Contest: Division 4](https://www.codechef.com/START106D/problems/FIZZBUZZ2304)

***Authors:*** [naisheel](https://www.codechef.com/users/naisheel), [jalp1428](https://www.codechef.com/users/jalp1428)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1365

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given an array A and a window size K, find the number of subarrays of A of length K whose bitwise OR is odd.

# [](#explanation-5)EXPLANATION:

First, we observe that an integer is odd *if and only if* it has the 0-th bit set.

It’s fairly easy to see why: the only odd power of 2 is 2^0 = 1, so if N can be written as the sum of several powers of 2 that don’t include 2^0, then N is the sum of several even numbers (and hence is itself even).

Bitwise OR is a bitwise operation, meaning it operates separately on each bit.

As noted above though, we only care about the 0-th bit - in particular, the bitwise OR of several integers is odd if and only if at least one of the numbers is odd.

This allows to restate our task as: find the number of subarrays of A of length K, such that they contain at least one odd number.

Of course, since N is large we don’t have the luxury of checking every possible subarray in \mathcal{O}(K) time each.

Solving this problem faster can be done in a variety of ways though.

One simple algorithm is to use a sliding window algorithm, as follows:

- First, count the number of odd integers in the first subarray, i.e, [A_1, A_2, \ldots ,A_K].

This is done with a simple loop.

- Next, we move to the subarray [A_2, A_3, \ldots A_{K+1}]$.

Here, instead of recomputing the entire thing, notice that there are only two changes: A_{K+1} got added into the subarray, and A_1 got removed.

So, it’s enough to add 1 to the counter if A_{K+1} is odd, and subtract 1 from the counter is A_1 is odd.

- Repeat this one-step move again to get the count for [A_3, A_4, \ldots, A_{K+2}], and so on.

This way, we are able to quickly check all the subarrays of length K in \mathcal{O}(N) time.

The answer is the number of times the odd-number counter was positive.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per testcase.

# [](#code-7)CODE:

Author's code (C++)
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        vector<int>arr(n);
        for(auto &x:arr)cin>>x;
        int cnt=0;
        for(int i=0;i<k-1;i++)
        {
            cnt+=(arr[i]%2);
        }
        int i=k-1;
        int ans=0;
        while(i<n)
        {
            cnt+=(arr[i]%2);
            ans+=(cnt>=1);
            cnt-=(arr[i-k+1]%2);
            i++;
        }
        cout<<ans<<endl;
    }
	// your code goes here
	return 0;
}
``

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    oddct = 0
    for i in range(k-1): oddct += a[i]%2
    for i in range(k-1, n):
        oddct += a[i]%2
        ans += oddct > 0
        oddct -= a[i-k+1]%2
    print(ans)
``

</details>
