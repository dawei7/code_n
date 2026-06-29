# Good Subarrays 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREFPRO4 |
| Difficulty Rating | 1300 |
| Difficulty Band | Prefix Sum Problems |
| Path | Data Structures and Algorithms |
| Lesson | Prefix and Suffix Sum |
| Official Link | [PREFPRO4](https://www.codechef.com/practice/course/prefix-sums/PREFIXSUMS/problems/PREFPRO4) |

---

## Problem Statement

Given an array consisting of n integers, find the number of good subarrays.

Good subarray: A subarray a$l$, a$l$+1, a$l$+2, . . . , a$r$−1, a$r$ is good if the sum of elements of this subarray is equal to the length of this subarray.

---

## Input Format

- The first line of input will contain a single integer $N$, denoting the length of the array.
- The second line of each test case contains n integers $A$1, $A$2, . . . $A$N.

---

## Output Format

Find the number of good subarrays

---

## Constraints

- $1 \leq N \leq 100000$
- $0 \leq Ai \leq 100000$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 2
```

**Output**

```text
3
```

**Explanation**

There are total 6 subarrays of :-

Subarray from 1st position to 1st position => [1]   => sum = 1,length = 1.

Subarray from 1st position to 2nd position => [1,1] => sum = 2,length = 2.

Subarray from 1st position to 3rd position => [1,1,2] => sum = 4,length = 3.

Subarray from 2nd position to 2nd position => [1] => sum = 1,length = 1.

Subarray from 2nd position to 3rd position => [1,2] => sum = 3,length = 2.

Subarray from 3rd position to 3rd position => [2] => sum = 2,length = 1.

There are total 3 subarrays with sum equal to the length of subarray.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisite** :- Prefix Sum.

**Explanation** :-

Given a subarray from L to R is considered good if its sum is equivalent to its length.

Iterate from Lth to Rth element to find the sum of the range.

Use prefix sum to optimize the previous step, find the sum of range in O(1) time using prefix array.

Pi represents the prefix sum till the ith index.

So according to the problem Pj - Pi  = j - i, so Pi - i = Pj - j.

Group prefix by value Pi - i for i from 0 to n, If we have n prefix with same value Pi - i then we have to add Pi - i to our answer.

**C++ Solution** :-

``#include <bits/stdc++.h>
using namespace std;

void solve(){
    long long n;
    long long fans = 0;
    cin>>n;
    vector<int>v(n,0);
    for(int i = 0;i<n;i++){
        cin>>v[i];
    }
    map<long,long>m1;
    vector<long long>pre(n+1,0);
    int sum = 0;
    m1[0] = 1;
    for(int i = 1;i<=n;i++){
        sum += v[i-1];
        fans += m1[sum-i];
        m1[sum-i]++;
    }
    cout<<fans<<"\n";
}
int main() {
    int freq = 1;
    while(freq--){
        solve();
    }
	// your code goes here

}

``

</details>
