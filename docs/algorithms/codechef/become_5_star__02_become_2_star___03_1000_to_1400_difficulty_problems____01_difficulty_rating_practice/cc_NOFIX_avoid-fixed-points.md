# Avoid Fixed Points

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | NOFIX |
| Difficulty Rating | 1250 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [NOFIX](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/NOFIX) |

---

## Problem Statement

Chef has a sequence of $N$ integers $A = [A_1, A_2,\dots,A_N]$. He can perform the following operation any number of times (possibly, zero):

- Choose **any** positive integer $K$ and insert it at any position of the sequence (possibly the beginning or end of the sequence, or in between any two elements).

For example, if $A=[5,3,4]$ and Chef selects $K=2$, then after the operation he can obtain one of the sequences $[\underline{2},5,3,4], [5,\underline{2},3,4], [5,3,\underline{2},4]$, or $[5,3,4,\underline{2}]$.

Chef wants this sequence to satisfy the following condition: for each $1\le i \le \mid A \mid $, $A_i \neq i$. Here, $\mid A\mid$ denotes the length of $A$.

Help Chef to find the **minimum** number of operations that he has to perform to achieve this goal. It can be proved that under the constraints of the problem, it's always possible to achieve this goal in a finite number of operations.

---

## Input Format

- The first line of input contains an integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$.

---

## Output Format

For each test case, print a single line containing one integer — the **minimum** number of operations that Chef has to perform to achieve the given condition.

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- Sum of $N$ over all test caes does not exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
2 4 5
3
4 1 3
4
3 2 4 2
```

**Output**

```text
0
1
2
```

**Explanation**

**Test case $1$:** The given sequence does not contain any index $i$ such that $A_i = i$. Hence Chef does not have to perform any operation.

**Test case $2$:** In the given sequence, $A_3 = 3$. Chef can choose $K = 2$ and insert it before the first element, making the sequence $A = [\underline{2}, 4, 1, 3]$, which does not contain any index $i$ for which $A_i = i$.

**Test case $3$:** In the given sequence, $A_2 = 2$. Chef can perform the following sequence of operations:
- Choose $K = 5$ and insert it before the first element. The sequence becomes $A = [\underline{5}, 3, 2, 4, 2]$, and now $A_4 = 4$.
- Choose $K = 3$ and insert it between the third and fourth element. The sequence becomes  $A = [5, 3, 2, \underline{3}, 4, 2]$, which does not contain any index $i$ for which $A_i = i$.

It can be verified that there is no way to satisfy the given condition in less than two operations.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 4 5
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
3
4 1 3
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
4
3 2 4 2
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

[Contest Division 1](https://www.codechef.com/FEB222A/problems/NOFIX)

[Contest Division 2](https://www.codechef.com/FEB222B/problems/NOFIX)

[Contest Division 3](https://www.codechef.com/FEB222C/problems/NOFIX)

**Setter:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Simple

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has a sequence of N integers A = [A_1, A_2, …, A_N]. He can perform the following operation any number of times (possibly, zero):

- Choose any positive integer K and insert it at any position of the sequence (possibly the beginning or end of the sequence, or in between any two elements).

Chef wants this sequence to satisfy the following condition:

- For each 1 \leq i \leq |A|, A_i \neq i. Here |A| denotes the length of A.

Help Chef to find the minimum number of operations that he has to perform to achieve this goal. It can be proved that under the constraints of the problem, it’s always possible to achieve this goal in a finite number of operations.

#
[](#explanation-5)EXPLANATION:

Observation 1

For a given element A_i which was initially present at position i, if there were X number of insertions made before position i, the new position of A_i is (i+X).

Observation 2

Note that the position of an element can never be decreased. In other words, an element can only be shifted to its right.

Solution

We refer to an element by its original position.

We traverse the array from left to right. Suppose we are at the i^{th} position and we have already made X operations by now to satisfy the given condition for all indices from 1 to i-1. This means that the new position of the i^{th} element is (i+X). There are two possible cases:

-
A_i \neq (i+X): This means that we do not need to perform any operation for this element as its updated position already satisfies the condition. For any elements with index >i, we make perform operations such that the position of this element does not change anymore.

-
A_i = (i+X): This means that we need to change the position of this element. We can do this by performing only 1 operation.

We insert a number Y\neq (i+X) at position (i+X). The position of A_i now becomes (i+X+1) and the condition is satisfied. Note that we have now performed (X+1) operations in total and all the elements from positions 1 to i satisfy the given condition now.

We keep updating X (the count of operations) in each iteration and the value of X at the end is our final answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Setter's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int ans = 0;
		for(int i = 1; i <= n; i++){
			int x;
			cin >> x;
			if(i + ans == x){
				ans++;
			}
		}
		cout << ans << '\n';
	}
}
``

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--) {
		int n; cin >> n;
	    int a[n];
	    for(int i = 0; i < n; i++) cin >> a[i];
	    int ans = 1;
	    for(int i = 0; i < n; i++)
	        if(a[i] == i + ans)
	            ans++;
	    cout << ans - 1 << "\n";
	}
	return 0;
}
``

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;

	while(t--){
	    int n;
	    cin>>n;

	    int a[n+1];
	    for(int i = 1; i<=n; i++){
	        cin>>a[i];
	    }

	    int inserted = 0;
	    for(int i = 1; i<=n; i++){
	        if(a[i] == (i+inserted)){
	            inserted++;
	        }
	    }
	    cout<<inserted<<endl;
	}
	return 0;
}
``

</details>
