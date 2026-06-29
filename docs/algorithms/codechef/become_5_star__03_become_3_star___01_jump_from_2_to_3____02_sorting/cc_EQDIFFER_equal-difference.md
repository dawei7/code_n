# Equal Difference

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | EQDIFFER |
| Difficulty Rating | 1500 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [EQDIFFER](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/EQDIFFER) |

---

## Problem Statement

You are given an array of $N$ integers. Find the *minimum* number of integers you need to delete from the array such that the absolute difference between each pair of integers in the remaining array will become equal.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer - the minimum number of integers to be deleted to satisfy the given condition.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
5
2 5 1 2 2
4
1 2 1 2
```

**Output**

```text
0
2
2
```

**Explanation**

**Test case $1$:** There is only one pair of integers and the absolute difference between them is $|A_1 - A_2| = |1 - 2| = 1$. So there is no need to delete any integer from the given array.

**Test case $2$:** If the integers $1$ and $5$ are deleted, the array A becomes $[2, 2, 2]$ and the absolute difference between each pair of integers is $0$. There is no possible way to delete less than two integers to satisfy the given condition.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
5
2 5 1 2 2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
4
1 2 1 2
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

[Practice](https://www.codechef.com/problems/EQDIFFER)

[Contest: Division 1](https://www.codechef.com/COOK132A/problems/EQDIFFER)

[Contest: Division 2](https://www.codechef.com/COOK132B/problems/EQDIFFER)

[Contest: Division 3](https://www.codechef.com/COOK132C/problems/EQDIFFER)

***Author:*** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

***Tester:*** [Shubham Anand Jain](https://www.codechef.com/users/TheOneYouWant)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

Sorting or usage of map/dictionary

#
[](#problem-4)PROBLEM:

Given an array A of length N, delete the minimum number of elements from it such that among the remaining elements, all pairwise differences are equal.

#
[](#quick-explanation-5)QUICK EXPLANATION:

If more than 2 elements remain, they must all be equal. So, the answer is either 0 (if N = 1), N-2, or N - M where M is the maximum frequency of some element of A.

#
[](#explanation-6)EXPLANATION:

First, note that any array of size \leq 2 trivially satisfies the condition, so there is no need to delete anything from it.

Now, suppose N \geq 3.

The above observation tells us that the answer will never be more than N-2, because we can simply delete any N-2 elements from the array and the remaining two elements will satisfy the condition.

What happens if the answer is less than N-2?

That would mean that at least 3 elements remain - say these are a, b, c with a\leq b\leq c.

The condition on pairwise differences tells us that c-b = c-a = b-a

This, of course, is only possible when a = b = c.

So, if the answer is less than N-2, all remaining elements must be equal.

This fact leads us to a simple solution - count the frequency of each element of A, and let M be the maximum of these frequencies. The answer is then \min(N-2, N-M).

How to count the frequency of every element fast?

Note that the elements of the array can be as large as 10^9, so creating a frequency array and updating the count of each element will not work, it would need too much memory.

Instead, do the same thing but using a map or unordered_map (C++) / TreeMap or HashMap (Java) / dictionary (python) to keep the memory usage down to \mathcal{O}(N)

There are other ways to do this as well without needing to resort to any data structures:

Sort the array. Now, all equal elements will form a continuous subarray, and the lengths of these subarrays can be found with binary search / two pointers.

#
[](#time-complexity-7)TIME COMPLEXITY:

\mathcal{O}(N) or \mathcal{O}(N\log N) per testcase, depending on implementation.

#
[](#solutions-8)SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

void solve(int tc) {
  int n; cin >> n;
  map<int, int> m;
  for (int i = 0; i < n; i++) {
    int x; cin >> x;
    m[x]++;
  }
  int ans = n, cnt = 0;
  for (auto u : m) {
    ans = min(ans, n - u.second);
    cnt++;
  }
  if (cnt >= 2) {
    ans = min(ans, n - 2);
  }
  cout << ans << '\n';
}

signed main() {
  ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
  int t; cin >> t;
  for (int i = 1; i <= t; i++) solve(i);
  return 0;
}
``

Tester's Solution
``//By TheOneYouWant
#include<bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0)

int main(){
	fastio;

	int tests;
	cin >> tests;

	while(tests--){
		int n;
		cin >> n;
		map<int,int> m;
		for(int i = 0; i < n; i++){
			int x;
			cin >> x;
			m[x]++;
		}
		if(n == 1){
			cout << 0 << endl;
			continue;
		}
		int ans = n-2;
		for(map<int,int>::iterator it = m.begin(); it != m.end(); it++){
			ans = min(ans, n - (*it).second);
		}
		cout << ans << endl;
	}

	return 0;
}
``

Editorialist's Solution
``import sys, collections
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    if n <= 2:
        print(0)
        continue
    freq = collections.Counter(a)
    ans = n-max(2, max(freq.values()))
    print(ans)
``

</details>
