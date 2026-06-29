# Janmansh and Assignments

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | JASSIGNMENTS |
| Difficulty Rating | 513 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [JASSIGNMENTS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JASSIGNMENTS) |

---

## Problem Statement

Janmansh has to submit $3$ assignments for Chingari before $10$ pm and he starts to do the assignments at $X$ pm. Each assignment takes him $1$ hour to complete. Can you tell whether he'll be able to complete all assignments on time or not?

---

## Input Format

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- The first and only line of each test case contains one integer $X$ - the time when Janmansh starts doing the assignments.

---

## Output Format

For each test case, output `Yes` if he can complete the assignments on time. Otherwise, output `No`.

You may print each character of `Yes` and `No` in uppercase or lowercase (for example, `yes`, `yEs`, `YES` will be considered identical).

---

## Constraints

- $1 \le T \le 10$
- $1 \le X \le 9$

---

## Examples

**Example 1**

**Input**

```text
2
7
9
```

**Output**

```text
Yes
No
```

**Explanation**

**Test case-1:** He can start at $7$pm and finish by $10$ pm. Therefore he can complete the assignments.

**Test case-2:** He can not complete all the $3$ assignments if he starts at $9$ pm.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
9
```

**Output for this case**

```text
No
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK139A/problems/JASSIGNMENTS)

[Contest Division 2](https://www.codechef.com/COOK139B/problems/JASSIGNMENTS)

[Contest Division 3](https://www.codechef.com/COOK139C/problems/JASSIGNMENTS)

[Contest Division 4](https://www.codechef.com/COOK139D/problems/JASSIGNMENTS)

**Setter:** [Janmansh Agarwal](https://www.codechef.com/users/janmansh)

**Tester:** [Takuki Kurokawa](https://www.codechef.com/users/tabr)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Janmansh has to submit 3 assignments for Chingari before 10 pm and he starts to do the assignments at X pm. Each assignment takes him 1 hour to complete. Can you tell whether he’ll be able to complete all assignments on time or not?

#
[](#explanation-5)EXPLANATION:

The time required to complete 1 assignment is 1 hour. Thus, 3 hours are required to complete all 3 assignments.

In order to complete the assignments before 10 pm, Janmansh has to start before 10-3 = 7 pm. Thus, the answer is `YES` if X \leq 7. Otherwise, the answer is `No`.

#
[](#time-complexity-6)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-7)SOLUTION:

Tester's Solution
``#include <bits/stdc++.h>
using namespace std;

int main() {
    int tt;
    cin >> tt;
    while (tt--) {
        int x;
        cin >> x;
        if (x <= 7) {
            cout << "Yes" << endl;
        } else {
            cout << "No" << endl;
        }
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
	    int x;
	    cin>>x;
	    if(x <= 7){
	        cout<<"yEs";
	    }
	    else{
	        cout<<"nO";
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
