# Problems in your to-do list

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TODOLIST |
| Difficulty Rating | 580 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [TODOLIST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TODOLIST) |

---

## Problem Statement

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*
- *Recent Contest Problems - contains only problems from the last 2 contests*
- *Separate Un-Attempted,  Attempted, and All tabs*
- *Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*
- *Popular Topics and Tags*

Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic **'+'** symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his [to-do](https://www.codechef.com/practice/todo) list without looking at their difficulty rating.

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than $1000$. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should **remove** from his to-do list, so that he is only left with problems of difficulty rating less than $1000$.

---

## Input Format

- The first line of input will contain a single integer $T$, the number of test cases. Then the testcases follow.
- Each testcase consists of 2 lines of input.
- The first line of input of each test case contains a single integer, $N$, which is the total number of problems that the Chef has added to his to-do list.
- The second line of input of each test case contains $N$ space-separated integers $D_1, D_2, \ldots, D_N$, which are the difficulty ratings for each problem in the to-do list.

---

## Output Format

For each test case, output in a single line the number of problems that Chef will have to remove so that all remaining problems have a difficulty rating strictly less than $1000$.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq D_i \leq 5000$

---

## Examples

**Example 1**

**Input**

```text
5
3
800 1200 900
4
999 1000 1001 1002
5
1 2 2 2 5000
5
1000 1000 1000 1000 1000
3
900 700 800
```

**Output**

```text
1
3
1
5
0
```

**Explanation**

**Test case $1$:** Among the three difficulty ratings, Chef only needs to remove the problem with difficulty rating $1200$, since it is $\ge 1000$. So, the answer is $1$.

**Test case $2$:** Among the four difficulty ratings, Chef needs to remove the problems with difficulty ratings of $1000$, $1001$, and $1002$, since they are $\ge 1000$. So, the answer is $3$.

**Test case $3$:** Among the five difficulty ratings, Chef needs to remove the problem with a difficulty rating of $5000$, since it is $\ge 1000$. So, the answer is $1$.

**Test case $4$:** Chef needs to remove all the five problems, since they are all rated $\ge 1000$. So, the answer is $5$.

**Test case $5$:** Chef does not need to remove any problem, since they are all rated $\lt 1000$. So, the answer is $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
800 1200 900
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
999 1000 1001 1002
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
5
1 2 2 2 5000
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
5
1000 1000 1000 1000 1000
```

**Output for this case**

```text
5
```



#### Test case 5

**Input for this case**

```text
3
900 700 800
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/LTIME108A/problems/TODOLIST)

[Contest Division 2](https://www.codechef.com/LTIME108B/problems/TODOLIST)

[Contest Division 3](https://www.codechef.com/LTIME108C/problems/TODOLIST)

[Contest Division 4](https://www.codechef.com/LTIME108D/problems/TODOLIST)

**Setter:** [Hrishikesh](https://www.codechef.com/users/hrishik85)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Trung Dang](https://www.codechef.com/users/kuroni)

#
[](#difficulty-2)DIFFICULTY:

580

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than 1000. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should **remove** from his to-do list, so that he is only left with problems of difficulty rating less than 1000.

#
[](#explanation-5)EXPLANATION:

We loop through the list of difficulty ratings and count the number of problems that are at least 1000 in rating.

#
[](#time-complexity-6)TIME COMPLEXITY:

Time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Preparer's Solution
``#include<iostream>

using namespace std;

int q,n,a;

int main()
{
	cin>>q;

	while(q--)
	{
		cin>>n;
		int cnt = 0;
		for(int i=1;i<=n;i++)
		{
			cin>>a;
			if(a >= 1000)
				cnt++;
		}
		cout<<cnt<<"\n";
	}
}
``

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
ll n;
void solve(int rr){
	cin >> n;
	int ans=0;
	for(int i=1; i<=n ;i++){
		int x;cin >> x;ans+=(x>=1000);
	}
	cout << ans << '\n';
}
int main(){
	ios::sync_with_stdio(false);cin.tie(0);
	int t;cin >> t;
	for(int i=1; i<=t ;i++) solve(i);
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }
        cout << count_if(a.begin(), a.end(), [](int u) { return u >= 1000; }) << '\n';
    }
}
``

</details>
