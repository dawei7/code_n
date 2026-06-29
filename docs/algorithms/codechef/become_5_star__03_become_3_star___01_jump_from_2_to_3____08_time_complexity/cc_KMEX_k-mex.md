# K-MEX

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KMEX |
| Difficulty Rating | 1450 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [KMEX](https://www.codechef.com/practice/course/2to3stars/LP2TO308/problems/KMEX) |

---

## Problem Statement

You are given an array $A$ containing $N$ integers. Find if it is possible to choose **exactly** $M$ elements from the array such that the **MEX** of the chosen elements is **exactly** $K$.

Recall that the *MEX* of an array is the smallest non-negative integer that does not belong to the array. For example, the *MEX* of $[2, 2, 1]$ is $0$ because $0$ does not belong to the array, the *MEX* of $[3, 1, 0, 1]$ is $2$ because $0$ and $1$ belong to the array, but $2$ does not.

---

## Input Format

- The first line contains an integer $T$, denoting the number of test cases. The $T$ test cases then follow:
- The first line of each test case contains an integer $N, M, K$, denoting the length of the array, the number of elements to be chosen, and the required MEX respectively.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$, denoting the elements of the array.

---

## Output Format

For each test case, print `YES` if it is possible to choose $M$ elements from the array $A$ so that the MEX of the chosen elements is exactly $K$ and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes` and `YES` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N$
- $0 \leq A_i, K \leq N$

---

## Examples

**Example 1**

**Input**

```text
6
5 4 2
0 1 3 0 3
2 1 2
0 1
3 3 3
0 1 2
4 3 3
2 0 4 3
5 4 2
0 2 1 2 5
6 5 2
0 1 0 2 0 3
```

**Output**

```text
YES
NO
YES
NO
NO
YES
```

**Explanation**

**Test case $1$:** The chosen elements are $0, 1, 3, 0$ and $MEX([0, 1, 3, 0]) = 2$.

**Test case $3$:** The chosen elements are $0, 1, 2$ and $MEX([0, 1, 2]) = 3$.

**Test case $6$:** The chosen elements are $0, 1, 0, 0, 3$ and $MEX([0, 1, 0, 0, 3]) = 2$.

**Test case $2, 4, 5$:** There is no way to choose elements to obtain the required MEX.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4 2
0 1 3 0 3
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
2 1 2
0 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
3 3 3
0 1 2
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
4 3 3
2 0 4 3
```

**Output for this case**

```text
NO
```



#### Test case 5

**Input for this case**

```text
5 4 2
0 2 1 2 5
```

**Output for this case**

```text
NO
```



#### Test case 6

**Input for this case**

```text
6 5 2
0 1 0 2 0 3
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest](https://www.codechef.com/COOK143)

[Practice](https://www.codechef.com/problems/KMEX)

**Setter:** [soumyadeep_21](https://www.codechef.com/users/soumyadeep_21)

**Testers:** [gamegame](https://www.codechef.com/users/gamegame)

#
[](#difficulty-2)DIFFICULTY:

1450

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array with N integers. Find if you can select M elements from it, whose MEX is K.

#
[](#explanation-5)EXPLANATION:

We need to check three points:

- Does the array have M elements which are not K?

- Does the array have at least 1 element whose value is i, for every 0 \le i \lt K?

- Is M large enough so that all these values from 0 to K-1 can be selected?

If the answer to all these 3 points is Yes, then the final answer is Yes. Even if one of them is No, the final answer is No.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N).

#
[](#solution-7)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int t, n, m, k, a, Freq[101];

int main() {

    cin>>t;

    while(t--)
    {
        cin>>n>>m>>k;

        int notk=0;
        for(int i=0;i<=n;i++)
            Freq[i]=0;

        for(int i=1;i<=n;i++)
        {
            cin>>a;
            if(a!=k)
                notk++;
            Freq[a]++;
        }

        if((notk<m)||(m<k))
        {
            cout<<"no\n";
            continue;
        }

        int poss = 1;
        for (int i=0;i<k;i++)
        {
            if(Freq[i]==0)
            {
                poss=0;
                break;
            }
        }

        if(poss==0)
        {
            cout<<"no\n";
        }
        else
        {
            cout<<"yes\n";
        }

    }

	return 0;
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=1e9+7;
int n,m,k;
int f[501];
void solve(){
	cin >> n >> m >> k;
	for(int i=0; i<=n ;i++) f[i]=0;
	for(int i=1; i<=n ;i++){
		int x;cin >> x;f[x]++;
	}
	for(int i=0; i<k ;i++){
		if(f[i]==0){
			cout << "NO\n";
			return;
		}
	}
	if(m+f[k]>n || m<k) cout << "NO\n";
	else cout << "YES\n";
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;while(t--) solve();
}
``

Setter's Solution
``#include<bits/stdc++.h>
using namespace std;

int main() {
	ios_base :: sync_with_stdio(0);
	cin.tie(0);
	int tt;
	cin >> tt;
	while (tt--) {
		int n, m, k;
		cin >> n >> m >> k;
		vector<int> fre(n + 1);
		for (int i = 0; i < n; i++) {
			int x;
			cin >> x;
			fre[x]++;
		}
		bool flag = (m >= k) && (n - fre[k] >= m);
		for (int i = 0; i < k; i++) {
			flag &= (fre[i] > 0);
		}
		if (flag) {
			cout << "YES\n";
		} else {
			cout << "NO\n";
		}
	}
	return 0;
}
``

</details>
