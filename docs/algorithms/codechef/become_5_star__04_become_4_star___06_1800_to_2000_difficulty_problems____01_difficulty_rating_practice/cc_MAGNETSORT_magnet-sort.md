# Magnet Sort

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAGNETSORT |
| Difficulty Rating | 1804 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [MAGNETSORT](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/MAGNETSORT) |

---

## Problem Statement

There is an array $A$ with $N$ elements. Each element of $A$ has a **fixed** *polarity*: either north or south.

Chef is allowed to perform some (possibly zero) operations on the array $A$. In one operation, Chef can:

- Pick some subarray of array $A$, such that, the **first** and **last** elements of the subarray have **different polarities**, and, rearrange the elements in this subarray any way he wants.

Note that the polarity of each element remains unchanged after an operation.

Find the **minimum** number of operations required to sort the array in non-decreasing order, or state that it is impossible.

A subarray of $A$ is obtained by deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.

---

## Input Format

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow.
- The first line of each test case contains a single integer $N$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line of each test case contains a string of length $N$, the $i$th character of which is either $\texttt{N}$ or $\texttt{S}$, representing that the $i$th element of $A$ has north or south polarity, respectively.

---

## Output Format

For each test case, if it impossible to sort the array, output $-1$. Otherwise, output a single integer: the minimum number of operations required to sort the array.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases doesn't exceed $2 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
6
5
1 3 2 3 7
NNSNS
2
2 1
SS
3
1 8 12
SNS
3
3 2 1
NSN
5
1 2 3 5 4
NSNSN
5
1 1 2 2 1
SNSNN
```

**Output**

```text
1
-1
0
2
1
1
```

**Explanation**

Let's represent elements with a polarity of north in $\color{red}{\text{red}}$, and elements with a polarity of south in $\color{blue}{\text{blue}}$. The polarity of each element is also labelled above it.

- In the first test case, we can sort the array in a single operation as follows.
    - Rearrange the subarray $[A_1, A_2, A_3]$: $[\color{red}{\stackrel{\texttt{N}}{1}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{7}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{7}}\color{black}{]}$.

- In the second test case, the array $[\color{blue}{\stackrel{\texttt{S}}{2}}, \color{blue}{\stackrel{\texttt{S}}{1}}\color{black}{]}$ cannot be sorted, since no operations can be performed.

- In the third test case, the array is already sorted, so the answer is $0$.

- In the fourth test case, we can sort the array in two operations as follows.

    - Rearrange the subarray $[A_2, A_3]$: $[\color{red}{\stackrel{\texttt{N}}{3}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{1}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}\color{black}{]}$.
    - Rearrange the subarray $[A_1, A_2, A_3]$: $[\color{red}{\stackrel{\texttt{N}}{3}}, \color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}\color{black}{]} \to [\color{red}{\stackrel{\texttt{N}}{1}}, \color{blue}{\stackrel{\texttt{S}}{2}}, \color{red}{\stackrel{\texttt{N}}{3}}\color{black}{]}$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
1 3 2 3 7
NNSNS
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
2 1
SS
```

**Output for this case**

```text
-1
```



#### Test case 3

**Input for this case**

```text
3
1 8 12
SNS
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
3
3 2 1
NSN
```

**Output for this case**

```text
2
```



#### Test case 5

**Input for this case**

```text
5
1 2 3 5 4
NSNSN
```

**Output for this case**

```text
1
```



#### Test case 6

**Input for this case**

```text
5
1 1 2 2 1
SNSNN
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1 ](https://www.codechef.com/LTIME105A/problems/MAGNETSORT)

[Contest Division 2 ](https://www.codechef.com/LTIME105B/problems/MAGNETSORT)

[Contest Division 3 ](https://www.codechef.com/LTIME105C/problems/MAGNETSORT)

[Contest Division 4 ](https://www.codechef.com/LTIME105D/problems/MAGNETSORT)

**Setter:** [Flame Storm](https://www.codechef.com/users/flamestorm153)

**Tester:** [Harris Leung ](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Easy

#
[](#prerequisites-3)PREREQUISITES:

Observation

#
[](#problem-4)PROBLEM:

There is an array A with N elements. Each element of A has a **fixed** *polarity*: either north or south.

Chef is allowed to perform some (possibly zero) operations on the array A. In one operation, Chef can:

- Pick some subarray of the array A, such that, the **first** and **last** elements of the subarray have **different polarities**, and, rearrange the elements in this subarray any way he wants.

Note that the polarity of each element remains unchanged after an operation.

Find the **minimum** number of operations required to sort the array in non-decreasing order, or state that it is impossible.

#
[](#explanation-5)EXPLANATION:

Let’s first see when it is not possible to sort the array at all. Consider this situation and think about whether it is possible to achieve a sorted array or not.

- Given an unsorted array in which every element has the same polarity either north or south, then it won’t be possible to achieve a sorted array.

It’s easy to visualise cause you can’t take any subarray and rearrange elements, hence the array will remain as it was given to us.

In all other cases, it is possible to sort the array and the maximum operations in the worst case will be only 2.

Wait, how is that possible only 2?

-

Let’s say the polarity of the first and last element is the same i.e North. Now as there exists at least one element which will have different polarity. We can bring that element to the end or start of the array in one operation.

-

Now the start and end of the array will have different parity and hence you can rearrange the whole array as you like. So why not make the array sorted in this operation.

-

Hence the maximum number of operations required in the worst case will be 2.

So we are left with finding when it will require only a single operation. Let’s see:

-

Identify the sorted prefix and suffix of the given array. Let’s say the prefix starts from index 0 and ends at index p. Similarly, say suffix starts from index s and ends at index n-1.

-

Hence the subarray A[p+1, s-1] is the unsorted part of the given array. Now if there exists an element in prefix P[0,p+1] whose polarity is different to that of any elements in suffix S [s-1,n-1]. Then we can consider that subarray and rearrange the elements to get the sorted array.

-

In such cases, only 1 operation would be required.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N \log N) per test case

#
[](#solutions-7)SOLUTIONS:

Setter
``#include <bits/stdc++.h>

using namespace std;

const int MAX = 200007;
const int MOD = 1000000007;

void solve() {
	int n;
	cin >> n;
	int a[n + 7];
	for (int i = 0; i < n; i++) {
		cin >> a[i];
	}
	string s;
	cin >> s;
	if (is_sorted(a, a + n)) {cout << 0 << '\n'; return;}
	bool hasN = false, hasS = false;
	for (char c : s) {
		if (c == 'N') {hasN = true;}
		if (c == 'S') {hasS = true;}
	}
	if (!hasN || !hasS) {cout << -1 << '\n'; return;}
	if (s[0] != s[n - 1]) {cout << 1 << '\n'; return;}
	int sorted[n + 7];
	for (int i = 0; i < n; i++) {
		sorted[i] = a[i];
	}
	sort(sorted, sorted + n);
	bool seen = false;
	for (int i = 0; i < n; i++) {
		if (sorted[i] == a[i]) {
			if (s[i] != s[0]) {seen = true;}
		}
		else if (i == 0 || sorted[i - 1] == a[i - 1]) {
			if (s[i] != s[0]) {seen = true;}
			break;
		}
	}
	for (int i = n - 1; i >= 0; i--) {
		if (sorted[i] == a[i]) {
			if (s[i] != s[n - 1]) {seen = true;}
		}
		else if (i == n - 1 || sorted[i + 1] == a[i + 1]) {
			if (s[i] != s[n - 1]) {seen = true;}
			break;
		}
	}
	if (seen) {cout << 1 << '\n';}
	else {cout << 2 << '\n';}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt; cin >> tt; for (int i = 1; i <= tt; i++) {solve();}
    // solve();
}

``

Tester
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const int N=2e5+1;
int n;
ll a[N],b[N];
char c[N];
bool check(){
	for(int i=2; i<=n ;i++){
		if(b[i-1]>b[i]) return false;
	}
	return true;
}
void solve(){
	cin >> n;
	bool hvn=false,hvs=false;
	for(int i=1; i<=n ;i++) cin >> a[i];
	for(int i=1; i<=n ;i++){
		cin >> c[i];
		hvn|=c[i]=='N';
		hvs|=c[i]=='S';
	}
	for(int i=1; i<=n ;i++) b[i]=a[i];
	if(check()){
		cout << "0\n";
		return;
	}
	if(!hvn || !hvs){
		cout << "-1\n";
		return;
	}
	if(c[1]!=c[n]){
		cout << "1\n";
		return;
	}
	for(int i=1; i<=n ;i++) b[i]=a[i];
	int ptr=1;
	while(c[ptr]==c[1]) ptr++;
	sort(b+ptr,b+n+1);
	if(check()){
		cout << "1\n";
		return;
	}
	for(int i=1; i<=n ;i++) b[i]=a[i];
	ptr=n;
	while(c[ptr]==c[n]) ptr--;
	sort(b+1,b+ptr+1);
	if(check()){
		cout << "1\n";
		return;
	}
	cout << "2\n";
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	while(t--) solve();
	//solve();
}
``

</details>
