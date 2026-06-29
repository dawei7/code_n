# Lazy Salesman

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HOLIDAYS |
| Difficulty Rating | 1161 |
| Difficulty Band | Level up from 1* to 2* |
| Path | Become 5 star |
| Lesson | Time Complexity |
| Official Link | [HOLIDAYS](https://www.codechef.com/practice/course/1to2stars/LP1TO205/problems/HOLIDAYS) |

---

## Problem Statement

Ved is a salesman. He needs to earn at least $W$ rupees in $N$ days for his livelihood. However, on a given day $i$ ($1 \le i \le N$), he can only earn $A_i$ rupees by working on that day.

Ved, being a lazy salesman, wants to take as many holidays as possible. It is known that on a **holiday**, Ved does not work and thus does not earn anything. Help **maximize** the number of days on which Ved can take a holiday.

It is guaranteed that Ved can always earn at least $W$ rupees by working on all days.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $W$ - the size of the array $A$ and the money Ved has to earn in those $N$ days.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the money which Ved can earn on each day.

---

## Output Format

For each test case, output the maximum number of holidays Ved can take.

---

## Constraints

- $1 \le T \le 100$
- $1 \le W \le 10000$
- $1 \le N \le 100$
- $1 \le A_i \le 100$
- It is guaranteed that Ved can always earn at least $W$ rupees by working on all days.

---

## Examples

**Example 1**

**Input**

```text
3
5 10
3 2 6 1 3
4 15
3 2 4 6
6 8
9 12 6 5 2 2
```

**Output**

```text
2
0
5
```

**Explanation**

**Test case-1:** Ved can work on $2$-nd, $3$-rd and $5$-th day earning $2 + 6 + 3 = 11$ rupees $\ge W$ rupees. Thus he can take $2$ holidays on the $1$-st and the $4$-th day.

**Test case-2:** Ved has to work on all days to earn $\ge W$ rupees. Thus he can not take any holidays.

**Test case-3:** Ved can work on $2$-nd day earning $12$ rupees $\ge W$ rupees. Thus he can take holiday on the remaining days.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 10
3 2 6 1 3
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
4 15
3 2 4 6
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
6 8
9 12 6 5 2 2
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK138A/problems/HOLIDAYS)

[Contest Division 2](https://www.codechef.com/COOK138B/problems/HOLIDAYS)

[Contest Division 3](https://www.codechef.com/COOK138C/problems/HOLIDAYS)

[Contest Division 4](https://www.codechef.com/COOK138D/problems/HOLIDAYS)

**Setter:** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

**Tester:** [Harris Leung](https://www.codechef.com/users/gamegame)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

[Greedy](https://en.wikipedia.org/wiki/Greedy_algorithm)

#
[](#problem-4)PROBLEM:

Ved needs to earn atleast W rupees in N days.However, on a given day i (1 \leq i \leq N), he can only earn A_i rupees by working on that day.

Help maximise the number of days on which Ved can take a holiday, still earning the required amount.

#
[](#explanation-5)EXPLANATION:

Observation

Ved should work on the days when payment is more. Similarly, Ved can take holidays when pay is less for that day.

Solution

To maximise the payment, Ved should work on the days which pay the most. Since he needs W rupees only, he can take holidays for the rest of the days.

We sort the days based on payment in descending order. Keep a count of the money earned till day i in the sorted array. Once the amount reaches W, Ved can take holidays for all the days thereafter.

#
[](#time-complexity-6)TIME COMPLEXITY:

Sorting an array takes O(Nlog(N)) time. After sorting, we traverse the array in O(N). Thus, the time complexity is O(Nlog(N)) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define fi first
#define se second
const ll mod=998244353;
int t;
int n,m;
ll a[300001];
ll s=0;
int main(){
    ios::sync_with_stdio(false);cin.tie(0);
    int t;cin >> t;
    while(t--){
    	cin >> n >> m;
    	for(int i=1; i<=n ;i++){
    		cin >> a[i];
    		m-=a[i];
		}
		sort(a+1,a+n+1);
		for(int i=1; i<=n ;i++){
			if(a[i]+m>0){
				cout << i-1 << '\n';
				break;
			}
			m+=a[i];
		}
	}
}
``

Editorialist's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n, w;
	    cin>>n>>w;

	    vector<int> a(n);
	    for(int i = 0; i<n; i++){
	        cin>>a[i];
	    }
	    sort(a.rbegin(), a.rend()); //sorting a vector in descending order
	    int curr_sum = 0;
	    int curr_day = 0;
	    for(; curr_day<n; curr_day++){
	        curr_sum += a[curr_day];
	        if(curr_sum>=w){
	            break;
	        }
	    }

	    int rem_days = (n-1) - curr_day; //array is 0-indexed
	    cout<<rem_days<<endl;
	}
	return 0;
}
``

</details>
