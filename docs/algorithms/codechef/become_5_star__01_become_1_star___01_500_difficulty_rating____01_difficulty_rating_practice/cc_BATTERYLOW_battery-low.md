# Battery Low

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BATTERYLOW |
| Difficulty Rating | 479 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BATTERYLOW](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BATTERYLOW) |

---

## Problem Statement

Chef's phone shows a Battery Low notification if the battery level is $15 \%$ or less.

Given that the battery level of Chef's phone is $X \%$, determine whether it would show a Battery low notification.

---

## Input Format

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains a single line of input, an integer $X$, denoting the battery level of the phone.

---

## Output Format

For each test case, output in a single line $\texttt{Yes}$, if the battery level is $15 \%$ or below. Otherwise, print $\text{No}$.

You may print each character of $\texttt{Yes}$ and $\text{No}$ in uppercase or lowercase (for example, $\texttt{YeS}$, $\texttt{YES}$, $\texttt{yes}$ will be considered identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
15
3
65
```

**Output**

```text
Yes
Yes
No
```

**Explanation**

**Test Case 1:** The battery level is $15$. Thus, it would show a battery low notification.

**Test Case 2:** The battery level is $3$, which is less than $15$. Thus, it would show a battery low notification.

**Test Case 3:** The battery level is $65$, which is greater than $15$. Thus, it would not show a battery low notification.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
15
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
Yes
```



#### Test case 3

**Input for this case**

```text
65
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

[Contest Division 1 ](https://www.codechef.com/LTIME105A/problems/BATTERYLOW)

[Contest Division 2 ](https://www.codechef.com/LTIME105B/problems/BATTERYLOW)

[Contest Division 3 ](https://www.codechef.com/LTIME105C/problems/BATTERYLOW)

[Contest Division 4 ](https://www.codechef.com/LTIME105D/problems/BATTERYLOW)

**Setter:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

**Tester:** [Harris Leung ](https://www.codechef.com/users/gamegame)

**Editorialist:** [Aman Dwivedi ](https://www.codechef.com/users/cherry0697)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

The chef’s phone shows a Battery Low notification if the battery level is 15\% or less.

Given that the battery level of Chef’s phone is X\%, determine whether it would show a Battery low notification.

#
[](#explanation-5)EXPLANATION:

if the battery percentage is greater than 15\%, you can simply print NO as it won’t give any notification. Otherwise, it would give a notification and hence print YES

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) per test case

#
[](#solutions-7)SOLUTIONS:

Author's
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int n;
	    cin>>n;
	    if(n <= 15) cout<<"yEs";
        else cout<<"NO";
        cout<<endl;
	}
	return 0;
}

``

Tester's
````

Editorialist
``#include<bits/stdc++.h>
using namespace std;

void solve()
{
  int x;
  cin>>x;

  cout<<((x>15)?"NO":"YES")<<"\n";
}

int main()
{
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int t;
  cin>>t;

  while(t--)
    solve();

return 0;
}

}

``

</details>
