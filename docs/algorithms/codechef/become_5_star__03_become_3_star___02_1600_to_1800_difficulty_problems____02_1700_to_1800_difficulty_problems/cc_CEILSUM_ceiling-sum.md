# Ceiling Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CEILSUM |
| Difficulty Rating | 1712 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [CEILSUM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/CEILSUM) |

---

## Problem Statement

You are given two integers $A, B$. You have to choose an integer $X$ in the range [minimum($A, B$), maximum($A, B$)] such that:

$$\Big \lceil \frac{B - X}{2} \Big \rceil + \Big \lceil \frac{X - A}{2} \Big \rceil$$ is maximum.

What is the maximum sum you can obtain if you choose $X$ optimally?

**Note:** $\lceil x \rceil$ : Returns the smallest integer that is greater than or equal to $x$ (i.e  rounds up to the nearest integer). For example, $\lceil 1.4 \rceil = 2$, $\lceil 5 \rceil = 5$, $\lceil -1.5 \rceil = -1$, $\lceil -3 \rceil = -3$ , $\lceil 0 \rceil = 0$.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, two integers $A, B$.

---

## Output Format

For each testcase, output the maximum sum of $\lceil \frac{B - X}{2} \rceil + \lceil \frac{X - A}{2} \rceil$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq A, B \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
1 11
13 6
```

**Output**

```text
0
6
-3
```

**Explanation**

- In the first test case, there is only one possible value of $X$ which is equal to $2$. So the sum is equal to $\lceil \frac{2 - 2}{2} \rceil + \lceil \frac{2 - 2}{2} \rceil$ = $\lceil \ 0 \rceil + \lceil \ 0 \rceil$  = $0 + 0 = 0$.

- In the second test case, we can choose $X$ to be $2$. So sum is equal to $\lceil \frac{11 - 2}{2} \rceil + \lceil \frac{2 - 1}{2} \rceil$ = $\lceil \ 4.5 \rceil + \lceil \ 0.5 \rceil$ = $5 + 1 = 6$. There is no possible way to choose an integer $X$ in the range $[1, 11]$ such that sum is greater than $6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
1 11
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
13 6
```

**Output for this case**

```text
-3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CEILSUM)

[Contest: Division 3](https://www.codechef.com/START7C/problems/CEILSUM)

[Contest: Division 2](https://www.codechef.com/START7B/problems/CEILSUM)

[Contest: Division 1](https://www.codechef.com/START7A/problems/CEILSUM)

**Author:** [Soumyadeep Pal](https://www.codechef.com/users/soumyadeep_21)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf)

**Editorialist:** [Vichitr Gandas](https://www.codechef.com/users/vichitr)

# DIFFICULTY:

SIMPLE

# PREREQUISITES:

Basic Maths

# PROBLEM:

Given two integers A,B. You have to choose an integer X in the range [minimum(A,B), maximum(A,B)] such that ?\frac{B?X}{2}?+?\frac{X?A}{2}? is maximum.

# QUICK EXPLANATION

Try solving it for following 3 cases separately: 1) A=B, 2) A>B and 3) A<B.

# EXPLANATION

Let’s divide the given problem in following three cases:

### Case 1: A=B

In this case, we have only one choice for X that is X=A=B. In this case given sum is ?\frac{B?X}{2}?+?\frac{X?A}{2}? = ?0?+?0? = 0.

### Case 2: A < B

**Observation 1**: Choose any X between the range [A, B], the given expression would always be either (B-A)/2 or (B-A)/2 + 1.

**Observation 2**: Its always possible to achieve the sum (B-A)/2+1 if A<B.

- Subcase (i): A-B is odd: in this case, by choosing X=A, we get the sum ?\frac{B?A}{2}? = (B-A)/2 +1.

- Subcase (ii): A-B is even: in this case, by choosing X=A+1, we get the sum ?\frac{B?A-1}{2}? +?\frac{A+1?A}{2}?= \frac{B-A}{2} +1 as ?\frac{1}{2}? = 1.

### Case 3: A > B

Lets solve it similar to the previous one.

- Subcase (i): A-B is odd, we get the sum (B-A)/2 for every X.

- Subcase (ii): A-B is even: in this case, by choosing X=A-1, we get the sum ?\frac{B?A+1}{2}? +?\frac{A-1?A}{2}?= \frac{B-A}{2} +1 + ?\frac{-1}{2}? = \frac{B-A}{2} +1 as ?\frac{-1}{2}? = 0.

# TIME COMPLEXITY:

O(1) per test case

# SOLUTIONS:

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

signed main() {
	ios_base :: sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int t = 1;
	cin >> t;
	while (t--) {
		int a, b;
		cin >> a >> b;
		assert(a >= 1 && b >= 1 && b <= 1e9 && a <= 1e9);
		if (a == b) {
			cout << "0\n";
		} else if (b > a) {
			cout << (b - a) / 2 + 1 << '\n';
		} else {
			if ((a - b) % 2 == 0) {
				cout << (b - a) / 2 + 1 << '\n';
			} else {
				cout << (b - a) / 2 << '\n';
			}
		}
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
    int a, b;
    cin>>a>>b;
    int temp = floor((b - a) / 2.0);
    if(a != b){
      temp++;
    }
    cout<<temp<<"\n";
  }
  return 0;
}
``

Editorialist's Solution
``/*
 * @author: vichitr
 * @date: 24th July 2021
 */

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fast ios::sync_with_stdio(0); cin.tie(0);

void solve() {
	int A, B; cin >> A >> B;
	int ans = 0;
	if (A < B)
		ans = (B - A) / 2 + 1;
	else if (A > B) {
		if ((A - B) % 2)
			ans = (B - A) / 2;
		else
			ans = (B - A) / 2 + 1;
	}
	cout << ans << '\n';
}

signed main() {
	fast;

#ifndef ONLINE_JUDGE
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif

	int t = 1;
	cin >> t;
	for (int tt = 1; tt <= t; tt++) {
		// cout << "Case #" << tt << ": ";
		solve();
	}
	return 0;
}
``

# VIDEO EDITORIAL:

If you have other approaches or solutions, let’s discuss in comments.If you have other approaches or solutions, let’s discuss in comments.

</details>
