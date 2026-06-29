# Hostel Room

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HOSTELROOM |
| Difficulty Rating | 1169 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [HOSTELROOM](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/HOSTELROOM) |

---

## Problem Statement

There are initially $X$ people in a room.

You are given an array $A$ of length $N$ which describes the following events:
- If $A_i \geq 0$, then $A_i$ people enter the room at $i$-th minute. For e.g. if $A_2 = 3$, then $3$ people enter the room at the $2$-nd minute.
- If $A_i \lt 0$, then $|A_i|$ people leave the room at $i$-th minute. Here $|A_i|$ denotes the absolute value of $A_i$. For e.g. if $A_4 = -2$, then $2$ people leave the room at the $4$-th minute.

Determine the maximum number of people in the room at any moment of time.

It is guaranteed in the input that at any moment of time, the number of people in the room does not become negative.

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case consists of two integers $N$ and $X$ - the length of the array $A$ and the number of people in the room initially.
- The second line of each test case contains $N$ integers $A_1, A_2, A_3, \dots A_N$.

---

## Output Format

For each testcase, output the maximum number of people in the room at any point of time.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $0 \leq X \leq 100$
- $-100 \leq A_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
5 8
0 3 3 -13 5
4 5
0 -2 2 3
3 5
-2 5 -2
```

**Output**

```text
14
8
8
```

**Explanation**

**Test case-1:** In the $3$-rd minute, the room contains $8 + 0 + 3 + 3 = 14$ people which is the maximum number of people in the room at any point of time.

**Test case-2:** In the $4$-th minute, the room contains $5 + 0 - 2 + 2 + 3 = 8$ people which is the maximum number of people in the room at any point of time.

**Test case-3:** In the $2$-nd minute, the room contains $5 - 2 + 5 = 8$ people which is the maximum number of people in the room at any point of time.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 8
0 3 3 -13 5
```

**Output for this case**

```text
14
```



#### Test case 2

**Input for this case**

```text
4 5
0 -2 2 3
```

**Output for this case**

```text
8
```



#### Test case 3

**Input for this case**

```text
3 5
-2 5 -2
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START26A/problems/HOSTELROOM)

[Contest Division 2](https://www.codechef.com/START26B/problems/HOSTELROOM)

[Contest Division 3](https://www.codechef.com/START26C/problems/HOSTELROOM)

[Contest Division 4](https://www.codechef.com/START26D/problems/HOSTELROOM)

**Setter:** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

**Tester:** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

There are initially X  people in a room.

You are given an array A of length N which describes the following events:

- If A_i \geq 0, then A_i people enter the room at i^{th} minute.

- If A_i < 0, then |A_i| people leave the room at i^{th} minute.

Determine the maximum number of people in the room at any moment of time.

#
[](#explanation-5)EXPLANATION:

We are given that there are X people in the room initially. We keep a count of the number of people in the room after each minute. This count is initialised with X.

Let Y denote the number of people in the room after the (i-1)^{th} minute. For the i^{th} minute:

- If A_i \geq 0, the number of people in the room becomes Y' = Y+A_i.

- If A_i < 0, the number of people in the room becomes Y' = Y-|A_i|.

We have to find the maximum number of people in the room at any time.

Thus, after each minute, we check if the number of people in the room (Y') can be a possible answer. We update the value of answer if Y' is greater than the current answer.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(N) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define db double
#define el "\n"
#define ld long double
#define rep(i,n) for(int i=0;i<n;i++)
#define rev(i,n) for(int i=n;i>=0;i--)
#define rep_a(i,a,n) for(int i=a;i<n;i++)

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int T=1;
    cin >> T;
    while(T--){

        int n,x,y;
        cin>>n>>x;

        int mx = x;
        rep(i,n){
            cin>>y;
            x+=y;
            if(x>mx) mx=x;
        }

        cout<<mx<<el;
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
	    int n, x;
	    cin>>n>>x;
	    int a[n];
	    for(int i = 0; i<n; i++){
	        cin>>a[i];
	    }

	    int maxm = x;
	    int curr_sum = x;
	    for(int i = 0; i<n; i++){
	        curr_sum += a[i];
	        maxm = max(maxm, curr_sum);
	    }
	    cout<<maxm<<endl;
	}
	return 0;
}
``

</details>
