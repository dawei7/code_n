# Chef and NextGen

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HELIUM3 |
| Difficulty Rating | 562 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [HELIUM3](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/HELIUM3) |

---

## Problem Statement

Chef is currently working for a secret research group called NEXTGEN.
While the rest of the world is still in search of a way to utilize Helium-3 as a fuel, NEXTGEN scientists have been able to achieve 2 major milestones:
1. Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
2. Obtaining every bit of Helium-3 from the moon's surface

Moving forward, the project requires some government funding for completion, which comes under one condition:
to prove its worth, the project should power Chefland by generating at least $A$ units of power each year for the next $B$ years.

Help Chef determine whether the group will get funded assuming that the moon has $X$ grams of Helium-3 and $1$ gram of Helium-3 can provide $Y$ units of power.

---

## Input Format

- The first line of input contains an integer $T$, the number of testcases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing four space-separated integers $A, B, X, Y$ respectively.

---

## Output Format

For each test case print on a single line the answer — `Yes` if NEXTGEN satisfies the government's minimum requirements for funding and `No` otherwise.

You may print each character of the answer string in either uppercase or lowercase (for example, the strings `"yEs"`, `"yes"`, `"Yes"` and `"YES"` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, X, Y, \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
1 2 3 4
4 3 2 1
2 18 9 4
1 100 2 49
```

**Output**

```text
Yes
No
Yes
No
```

**Explanation**

**Test case $1$:** Chefland requires $A = 1$ units of power for the next $B = 2$ years. In total, the moon must be capable of providing $A \cdot B = 2$ units of power. There are in total $X = 3$ grams of Helium-3 on the moon which is capable of providing $X \cdot Y = 12$ units of power. $12 \gt 2$, so the project satisfies the minimum requirements for funding. Thus, the answer is `Yes`.

**Test case $2$:** The total amount of power needed by Chefland is $A \cdot B = 12$, whereas the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 2$, which is insufficient to receive funding, so the answer is `No`.

**Test case $3$:** The total amount of power needed by Chefland is $A \cdot B = 2 \cdot 18 = 36$, and the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 9 \cdot 4 = 36$, which is sufficient to receive funding, so the answer is `Yes`.

**Test case $4$:** The total amount of power needed by Chefland is $A \cdot B = 1 \cdot 100 = 100$, and the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 2 \cdot 49 = 98$, which is insufficient to receive funding, so the answer is `No`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 3 4
```

**Output for this case**

```text
Yes
```



#### Test case 2

**Input for this case**

```text
4 3 2 1
```

**Output for this case**

```text
No
```



#### Test case 3

**Input for this case**

```text
2 18 9 4
```

**Output for this case**

```text
Yes
```



#### Test case 4

**Input for this case**

```text
1 100 2 49
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

[Contest Division 1](https://www.codechef.com/FEB222A/problems/HELIUM3)

[Contest Division 2](https://www.codechef.com/FEB222B/problems/HELIUM3)

[Contest Division 3](https://www.codechef.com/FEB222C/problems/HELIUM3)

**Setter:** [Daanish Mahajan](https://www.codechef.com/users/daanish_adm)

**Tester:** [Manan Grover](https://www.codechef.com/users/mexomerf), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

**Editorialist:** [Kanhaiya Mohan](https://www.codechef.com/users/notsoloud)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A project should power Chefland by generating at least A units of power each year for the next B years.

Help Chef determine whether the group will get funded assuming that the moon has X grams of Helium-3 and 1 gram of Helium-3 provides Y units of power.

#
[](#quick-explanation-5)QUICK EXPLANATION:

- If A \cdot B \leq X \cdot Y, the answer is `YES`. Otherwise, the answer is `NO`.

#
[](#explanation-6)EXPLANATION:

The requirement of Chefland is A units of power per year. For B years, a total of A \cdot B units of power is required.

Moon has X grams of Helium-3 and each gram can provide Y units of power. Thus, the total power available is X \cdot Y units.

The assignment would be funded only if the available power is greater than or equal to the required power.

Thus, the answer is `YES` if, A \cdot B \leq X \cdot Y. Otherwise the answer is `NO`.

#
[](#time-complexity-7)TIME COMPLEXITY:

The time complexity is O(1) per test case.

#
[](#solution-8)SOLUTION:

Editorialist's Solution
``#include <iostream>
using namespace std;

int main() {
	int t;
	cin>> t;
	while(t--){
	    int A, B, X, Y;
	    cin>>A>>B>>X>>Y;
	    if(A*B <= X*Y){
	        cout<<"YES";
	    }
	    else{
	        cout<<"NO";
	    }
	    cout<<endl;
	}
	return 0;
}
``

</details>
